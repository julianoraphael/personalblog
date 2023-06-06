# Personal Blog

This is a simple personal blog web application built with Django.

## Prerequisites

Make sure you have the following installed:

- Python (version 3.7 or higher)
- Django (version 3.2 or higher)

## Getting Started

1. Clone the repository:

   `<repository_url>`

2. Navigate to the project directory:

   `cd personalblog`

3. Install the required dependencies:

   `pip install -r requirements.txt`

4. Initialize the database:

   `python manage.py migrate`

5. Create a superuser account (for admin access):

   `python manage.py createsuperuser`

6. Run the development server:

   `python manage.py runserver`

7. Access the blog in your web browser:

   `http://localhost:8000/posts/`

8. Log in with your superuser account at:

   `http://localhost:8000/admin/`

## Usage

- To create a new blog post, log in as a user with admin privileges and click on "Create Post" on the admin interface or go to `http://localhost:8000/posts/create/`.
- Only logged-in users can create posts. Other visitors can view the list of posts and read individual posts.
- You can customize the templates, add features, and make other modifications to suit your requirements.

## Folder Structure

The folder structure of the project is as follows:

├── blog
│ ├── migrations
│ ├── static
│ ├── templates
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── personalblog
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── README.md


- The `blog` folder contains the Django app for the blog, including models, views, templates, and forms.
- The `personalblog` folder contains the project-level configuration files, including settings and URL configurations.
- The `manage.py` file is used for various management commands.

## License

This project is licensed under the [MIT License](LICENSE).
