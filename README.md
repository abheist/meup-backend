# meup-backend

So converted this project into template.

Will use this as a base for other projects.

### This containes
  - Register
  - Email verification
  - Login
  - Reset Password email link
  
### Tech used:
  - Python
  - Django
  - GraphQL
  - with other python packages to make it more productive

## How to get started:
1. Create new repository by clicking on `Use this template` button on this repo
2. Clone your new repo
3. Make a new virtualenv, you can use `virtualenvWrapper`
4. Get into project dir
5. Install the dependecies with: `pip install -r requirements.txt`
6. Once installed, run server with: `python manage.py runserver` or you can use runserver plus for better debugging `python manage.py runserver_plus`
7. Setup env file:
    - In a project root, make a file `.env`
    - Paste the following keys into it and set your key values
```
SECRET_KEY="your-django-key"
DEBUG=True
SENDGRID_API_KEY="sendgrid-api-key"
EMAIL_PORT=587
SENDGRID_USERNAME="abheist"
SENDGRID_HOST="sendgrid-host"
SENDGRID_SERVER_EMAIL="Abhishek <abhishek@abhiy.com>"
SENDGRID_DEFAULT_FROM_EMAIL="Abhishek <abhishek@abiy.com>"
```
