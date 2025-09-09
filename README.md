# react-django-blogify
Blogify – a fullstack blog platform powered by Django &amp; React.


### Features Implemented
# Authentication

User registration, login, and logout using JWT (access & refresh tokens).

Token blacklisting implemented for secure logout.

Admin/superuser creation and permission handling for secure operations.

# Blog Models

Post: Users can create posts with title, content, category, and tags.

Category: Admin can create categories; public can view.

Tag: Admin can create tags; public can view.

# Permissions

Only authenticated users can create or edit posts.

Only authors or admin can update or delete their own posts.

Only admin users can create categories and tags.