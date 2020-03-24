import graphene
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(object):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)

    @login_required
    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()

    @login_required
    def resolve_me(self, info, **kwargs):
        user = info.context.user
        return user


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    @login_required
    def mutate(self, info, username, email, password):
        user = get_user_model()(
                username=username,
                email=email
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
