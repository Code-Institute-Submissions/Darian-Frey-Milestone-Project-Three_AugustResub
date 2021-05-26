
# Milestone Project 3

## User Experience (UX)

## User Stories

## Technologies

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

## Design

## Wireframe

Wireframes created with [WireframeSketcher](https://wireframesketcher.com)

## Database Models and Schema

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

## Media

## Features

## Testing

## Deployment

## Credits & Acknowledgements