# Phone Review

![Site view across devices]()

The live link can be found [HERE]()

## Table of Contents

+ [UX](#ux "UX")
  + [Site Purpose](#site-purpose "Site Purpose")
  + [Site Goal](#site-goal "Site Goal")
  + [Audience](#audience "Audience")
  + [Communication](#communication "Communication")
  + [Current User Goals](#current-user-goals "Current User Goals")
  + [New User Goals](#new-user-goals "New User Goals")
+ [User Stories](#user-stories "User Stories")
  + [Admin stories](#admin-stories "Admin stories")
  + [Artist stories](#artist-stories "Artist stories")
  + [Visitor stories](#visitor-stories "Visitor stories")
+ [Design](#design "Design")
  + [Colour Scheme](#colour-scheme "Colour Scheme")
  + [Typography](#typography "Typography")
  + [Imagery](#imagery "Imagery")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
  + [C.R.U.D](#crud "C.R.U.D")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")

## UX

### Site Purpose

### Site Goal

### Audience

### Communication

### Current User Goals

### New User Goals

### Future Goals

## User Stories

Not all stories have been implemented. Some have been left for future implementations as the site grows and expands.

### Admin stories

#### As an admin

### Visitor stories

#### As a visitor

## Design

### Wireframes

##### Home Page

##### Blog Page

##### Review Details

##### Site Navigation

### Database Schema ?

### Colour Scheme

### Typography

All fonts were obtained from the Google Fonts library. I chose the following fonts for the page:

### Imagery

## Features

### Existing Features

#### Home Page

#### Navigation Bar

##### Desktop

##### Mobile

#### Review Details Page

#### Log in, Log out & Sign up

##### Login

##### Logout

##### Sign-up

### C.R.U.D

### Features Left to Implement

## Testing

+ CSS styles not loading on blog page:

+ **crispy-forms**:

+ Django error message after adding comment form:

+ Submit multiple comments:

+ Testing CRUD functionality:

+ Each of the features were tested multiple times to ensure that numerous new reviews and comments could be submitted, and that each review and comment had the ability to be updated and edited by the creator.
+ If a comment is submitted by another user, the edit/delete buttons do not appear on the page.

### Validator Testing

+ html files pass through the [W3C validator](https://validator.w3.org/) with no html issues found

+ Errors listed only reference {%%} & {{}} tags.

+ CSS files pass through the [Jigsaw validator](https://jigsaw.w3.org/css-validator/) with no issues found.

![Jigsaw validator message](static/images-readme/readme-w3c-css.png)
<!--
- JS files pass through [JSHint](https://jshint.com/) with no issues found.

![JSHint overview]() -->

+ page has an excellent Accessibility rating in Lighthouse

![Accessibility score](static/images-readme/readme-lighthouse.png)

+ Python files passed through [PEP8 Online](http://pep8online.com/) with no issues found.

![PEP8 message](static/images-readme/readme-pep8.png)

+ Tested the site opens in Chrome & Safari without issues.

### Unfixed Bugs

## Technologies Used

### Main Languages Used

+ HTML5
+ CSS3
+ Python
+ Django
+ SQL - Postgres ?

### Frameworks, Libraries & Programs Used

+ Google Fonts - was used for the font families "PT Serif" and "Nunito Sans".
+ Font Awesome - was used to add the icon to indicate number of comments on a review.
+ Pexels - was used to provide the site with free photos.
+ Codeanywhere - was used for my IDE.
+ GitHub - was used to store my repository.
+ Balsamiq - was used to create mockups of the project prior to starting.
+ Am I Responsive? - was used to ensure the project looked good across all devices and provide a visual representation of this.
+ Django
+ Bootstrap

### Installed Packages

+ 'django<4' gunicorn
+ dj_database_url psycopg2
+ dj3-cloudinary-storage
+ django-summernote
+ django-allauth
+ django-crispy-forms

## Deployment

The site was deployed to Heroku using the following steps:

+ Install Django & Gunicorn:
```pip3 install 'django<4' gunicorn```
+ Install Django database & psycopg:
```pip3 install dj_database_url psycopg2```
+ Install Cloudinary:
```pip3 install dj3-cloudinary-storage```
+ Create the requirements.txt file with the following command:
```pip3 freeze --local > requirements.txt```
+ a django project was created using:
```django-admin startproject printstatements.```
+ the blog app was then created with:
```python3 manage.py startapp blog```
+ which was then added to the settings.py file within our project directory.
+ the changes were then migrated using:
```python3 manage.py migrate```
+ navigate to [Heroku](www.heroku.com) & created a new app called print-statements.
+ add the Heroku Postgres database to the Resources tab.
+ navigate to the Settings Tab, to add the following key/value pairs to the configvars:

1. key: SECRET_KEY | value: randomkey
2. key: PORT | value: 8000
3. key: CLOUDINARY_URL | value: API environment variable
4. key: DATABASE_URL | value: value supplied by Heroku

+ add the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file
+ add the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file
+ add an import os statement for the env.py file in the settings.py
+ add Heroku to the ALLOWED_HOSTS in settings.py
+ create the Procfile for [Heroku](www.heroku.com)
+ push the project to Github
+ connect github account to Heroku through the Deploy tab
+ connect my github project repository, and then clicked on the "Deploy" button

## Credits

### Content

+ [Martina Terlevic](https://github.com/SephTheOverwitch): My mentor who calmed me down in a state of panic and calmly described what was needed for the project. So that I had a plan going forward.
+ [Oscar Johansson](https://github.com/OskarJ1993): For being a rock throughout this course and being a support pillar.
+ “I think therefore I blog” walkthrough: Provided the initial steps for setting up & deploying the site. As well as using the instructions they provided in order to implement a django blog into my app, following the walkthrough once again step-by-step. This also includes, but is not limited to, some formatting for the way each blog post is displayed on the blog page and the comment model. Credits have been added as comments where code was used.
+ "I think therefore I blog" + "Hello Django" + Slack + Stackoverflow + [Martina Terlevic](http://github.com/SephTheOverWitch): aided in the creation of the CRUD function centered on the comments.
+ Adam from Tutor support: assisting in deciphering why crispy caused an error.
+ Joanne from Tutor support: assisting in deploying to heroku and explaining the "etag" error.
+ [Bootstrap](https://getbootstrap.com/docs/5.2/components/dropdowns/): dropdown nav menu.
