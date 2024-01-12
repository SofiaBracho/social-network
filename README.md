 # Django Social Network

This is a simple social network built using Django. It allows users to create accounts, follow other users, post messages, and like posts.

## Getting Started

To get started, you will need to install Django and create a virtual environment. You can do this by following the instructions on the Django website.

Once you have created a virtual environment, you can install the project dependencies by running the following command:

```
pip install -r requirements.txt
```

Next, you will need to create a database. You can do this by running the following command:

```
python manage.py migrate
```

Finally, you can start the development server by running the following command:

```
python manage.py runserver
```

The development server will be running on port 8000. You can access the social network by visiting http://localhost:8000 in your web browser.

## Features

The social network has the following features:

* Users can create accounts, follow other users, post messages, and like posts.
* Posts are displayed in reverse chronological order.
* Users can edit their own posts.
* Users can follow and unfollow other users.
* Users can like and unlike posts.
* The social network uses a relational database to store user data and posts.

## Code Overview

The code for the social network is organized into the following files:

* `models.py` defines the database models for the social network.
* `views.py` defines the views for the social network.
* `urls.py` defines the URL patterns for the social network.
* `templates/network` contains the HTML templates for the social network.
* `static/network` contains the static files for the social network.

### Models

The `models.py` file defines the database models for the social network. The following models are defined:

* `User` represents a user of the social network.
* `Post` represents a post on the social network.
* `PostLikes` represents a like on a post.
* `UserFollowing` represents a following relationship between two users.

### Views

The `views.py` file defines the views for the social network. The following views are defined:

* `index` displays the home page of the social network.
* `following` displays the posts from the users that the current user is following.
* `profile` displays the posts by a specific user.
* `login` displays a login form to athenticate the user.
* `register` displays a registration form.
* `logout` logs out the currently authenticated user.