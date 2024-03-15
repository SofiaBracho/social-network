<div align="center">
  <h1 align="center">Social Network</h1>
</div>
<br/>

<div align="center">

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-javascript](https://img.shields.io/badge/Made%20with-JavaScript-1f425f.svg)](https://www.javascript.com)
<br/>
<br/>
<a href="https://www.linkedin.com/in/sofiabrach0/">
![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=fff&style=for-the-badge)
</a>
<a href="https://github.com/SofiaBracho">
![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge)
</a>
</div>

This is a simple twitter-like social network built using Django. It allows users to create accounts, follow other users, post text messages, and like posts.

## ⚙️ Key Features

The social network has the following features:
  
- **User accounts**: Users can create accounts with their email address,  username and password in the `/register` view. They will be able to log in in the `/login` view.

- **Follow other users**: Users can follow and unfollow other users to check their activity in the `/following` view.

- **Post messages**: Using just text with a max of 280 characters.

- **Like posts**: clicking the 🤍 icon you can like any post you want. If you want to unlike it just click the ❤️ icon.

- **Edit posts**: Users can edit their own posts at any given time.

- **Check recent posts**: Posts are displayed in reverse chronological order.

- **Following page**: Check recent posts just by the users you follow in the `/following` view.
  
- **Profile page**: In the `/user_id/profile/` view, you can see all posts  made by that user and followers/following.


## 🖥️ Demo

![Flashcards Demo GIF](https://github.com/SofiaBracho/social-network/blob/master/network/static/demo.gif)


## 🛠️ Getting Started

### Prerequisites

Here's what you need to be able to run this App:

- Node.js
- Python

### 1. Clone the repository

```shell
git clone https://github.com/SofiaBracho/social-network.git
cd social-network
```

### 2. Migrate database models

```shell
python manage.py makemigrations
python manage.py migrate
```

### 3. Run the dev server

```shell
python manage.py runserver
```

### 4. Open the App in your local host

```shell
http://localhost:8000
```

### 5. Register and login

Create your user account in the `/register` route, then login into the form in the `/login` route.


## 🗄️ Models

The `models.py` file defines the database models for the social network. The following models are defined:

- **User**: represents a user of the social network
  - Username
  - Email
  - Password
- **Post**: represents a post on the social network. 
  - Content of the post
  - User who posted it
  - Date and time posted
  - Users who liked the post (many to many relationship with User)
- **PostLikes**: represents a like on a post.
  - User who liked the post
  - Post liked by the user (unique together)
- **UserFollowing**: represents a following relationship between two users. 
  - User
  - User following
  - 

## 🖇️ Views
The `views.py` file defines the views for the social network. The following views are defined:

- **Index**: displays the home page of the social network with all the recent posts.

![Profile view](https://github.com/SofiaBracho/social-network/blob/master/network/static/img/home.PNG)

- **Following**: displays the posts from the users that the current user is following.

![Profile view](https://github.com/SofiaBracho/social-network/blob/master/network/static/img/following.PNG)

- **Profile**: displays the posts by a specific user.

![Profile view](https://github.com/SofiaBracho/social-network/blob/master/network/static/img/profile.PNG)

- **Login**: displays a login form to athenticate the user.

![Login view](https://github.com/SofiaBracho/social-network/blob/master/network/static/img/login.PNG)

- **Register**: displays a registration form to create a new user.

![Login view](https://github.com/SofiaBracho/social-network/blob/master/network/static/img/register.PNG)


## 🔀 Contributing

This Django social network is an open-source project and anyone from the community can contribute to it.

If you'd like to contribute, fork the repository and make changes as you'd like. Pull requests are welcome.

### 👥 Author

<a href="https://github.com/SofiaBracho">
  <img src="https://github.com/SofiaBracho/social-network/blob/master/network/static/img/author.PNG" width="50px" alt="Author"/>
</a>

**Sofia Bracho**
<br>
Web developer