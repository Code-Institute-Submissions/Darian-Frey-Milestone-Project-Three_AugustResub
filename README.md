
# Milestone Project 3

## [**Table of Contents**](#table-of-contents)

- [UX](#UX)
- [User Stories](#User-Stories)
- [Technologies](#Technologies)
- [Design](#Design)
- [Wireframe](#Wireframe)
- [Database Models and Schema](#Database-Models-and-Schema)
- [Media](#Media)
- [Features](#Features)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credits & Acknowledgements](#Credits-&-Acknowledgements)

## **UX**

## **User Stories**

- *"As a user, I want to immediately understand the purpose of the site"*
- *"As a user, I want to create my own reviews."* 
- *"As a user, I want to easily access my own content."* 
- *"As a user, I want to edit reviews I have created."*
- *"As a user, I want to control my own content."*  
- *"As a user, I want to be able to delete reviews I have created."*  
- *"As a user, I want to be able to delete my account."*  
- *"As a user, I want to be able to browse reviews created by other users."*
- *"As a user, I want to be directed to a site where I can buy a book."*
- *"As a user, I want a site that is visually appealing."*  
- *"As a user, I want a site that is easy to navigate."* 
- *"As a user, I want a site that is intuitive."*  

##### [Back to Table of Contents](#table-of-contents)

## **Technologies**
##### [Back to Table of Contents](#table-of-contents)

## **Technologies Used**

The Technologies used in this project are listed bellow.

### **Languages**
- **HTML** - used to create the structure of the application
- **CSS** - used to position and style the application 
- **JavaScript** - used to for interactivity
- **Python** - used to handle backend
- **Jinja** - Python templating language

### **Libraries and Frameworks**
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
- [Materialize CSS](https://materializecss.com/) 
- [Google Fonts](https://fonts.google.com/) 
- [Font Awesome](https://fontawesome.com/) 
- [jQuery](https://code.jquery.com/) 

### **Project Management**
- [Git](https://git-scm.com/) 
- [Gitpod](https://gitpod.io/) 
- [Github](https://github.com/) 
- [Heroku](https://signup.heroku.com)
- [MongoDB](https://www.mongodb.com/)

### **Tools**
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) 
- [WireFrameSketcher](https://wireframesketcher.com/)
- [Am I Responsive](http://ami.responsivedesign.is/)
- [Favicon](https://favicon.io/favicon-converter/) 
- [Coolors](https://coolors.co/)


## **Design**
##### [Back to Table of Contents](#table-of-contents)

## **Wireframe**
##### [Back to Table of Contents](#table-of-contents)

Wireframes created with [WireframeSketcher](https://wireframesketcher.com)

## **Database Models and Schema**
##### [Back to Table of Contents](#table-of-contents)

[QuickDBD](https://app.quickdatabasediagrams.com//)

```
User
-
UserID PK int
Username varchar(20)
Email email
Password password
UserReviews string FK >- Reviews.ReviewID
DateCreated datetime


Reviews
-
ReviewID PK int
Title varchar
Aurthor varchar
Genre varchar
BuyLink url
ImageURL url
Synopsis string
Review string
DateCreated datetime
```

<img src="Wireframes/quickdbd/QuickDBD.png"
     alt="Database design"/>

## **Media**
##### [Back to Table of Contents](#table-of-contents)

## **Features**
##### [Back to Table of Contents](#table-of-contents)

## **Testing**
##### [Back to Table of Contents](#table-of-contents)

## **Deployment**
##### [Back to Table of Contents](#table-of-contents)

## **Credits & Acknowledgements**
##### [Back to Table of Contents](#table-of-contents)
