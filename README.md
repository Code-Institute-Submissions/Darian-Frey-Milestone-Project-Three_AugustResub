
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

The Technologies used in this project are listed bellow.

- [QuickDBD](https://app.quickdatabasediagrams.com//)
- [Materialize](https://materializecss.com/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5/)
- [CSS3](https://en.wikipedia.org/wiki/CSS/)
- [MongoDB](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)
- [GitHub](https://github.com/Darian-Frey/)
- [Gitpod](https://www.gitpod.io/)
- [jQuery](https://jquery.com/)

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
