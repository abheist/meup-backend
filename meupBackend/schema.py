import graphene
from graphql_auth import mutations

import users.schema


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_email = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Query(users.schema.Query, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
