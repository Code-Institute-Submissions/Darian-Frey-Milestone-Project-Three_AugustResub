#### [Back to README](README.md)

## **Testing**
### [**Table of Contents**](#table-of-contents)

- [User Stories](#user-stories)
- [Manual Testing of Navigation](#manual-testing-of-navigation)
- [Responsiveness](#responsiveness)
- [Bugs and Issues](#bugs-and-issues)
    - [Resolved](#resolved)
    - [Existing](#existing)

---

## **User Stories**

*"As a user, I want to immediately understand the purpose of the site"*
- *The Landing page explains the purpose of the site in a clear manor.*

*"As a user, I want to create my own reviews."*
- *Once a user is logged in they can choose to add a review by selecting add review from the Navbar.*

*"As a user, I want to easily access my own content."*
- *A user can view all their reviews by accessing their profile page.*

*"As a user, I want to edit reviews I have created."*
- *Users can edit their reviews by selecting the edit button on the review from their profile page.*

*"As a user, I want to be able to delete reviews I have created."*
- *Users can delete their reviews by selecting the delete button on the review from their profile page.*

*"As a user, I want to be able to delete my account."*
- *Users can delete their profile by the delete button at the bottom of their profile page.* 

*"As a user, I want to be able to browse reviews created by other users."*
- *Users can view all reviews by selecting Reviews from the Navbar.*

*"As a user, I want to be directed to a site where I can buy a book."*
- *Users can follow the "Buy This Book" link at the bottom of each review.*

*"As a user, I want a site that is visually appealing."*
- *The background image reflects the theme of the Readers Corner*
- *I've tried to creat a colour theme that is slightley sepia tone and off-white to reflect the colour of well read book.*

*"As a user, I want a site that is easy to navigate."*
- *The site navigation is clearly defiend in the Navbar.*
- *Buttons and icons are easily identifiable and colour coded.*
- *Consistency across the site is achieved with the navbar and footer remaining fixed across all pages.*

*"As a user, I want a site that is intuitive."*
- *The links are ordered in an intuitive manner.*
- *All content is located where it would be expected to be found.*
- *The profile also allows them to navigate to where ever they need to go to find or create content.*

## **Manual Testing of Navigation**
---

Each navigation link was tested while in development and once deployed 
to ensure correct functionality.

### **Navbar/Sidenav**

- *Navbar is fixed to top of every page.*
- *Each link was clicked to ensure it directed user to correct page.*
- *Nav brand logo clicked to ensure it returns user to index.html.*
- *Logged out user only has access to relevant links - 'Home', 'Log in', 'Sign up'.*
- *Logged in users have access to - 'Home', 'Reviews', 'Add Review', 'Profile' , 'LogOut'*
 - _'Log Out'_ link
    - logs user out of their account.
    - flash message informs user they have been logged out.
    - redirects user to _'Log In'_ page.
 - Hamburger icon is visible on small devices.

 ### **Footer**
- Is fixed at bottom of page regardless of content
- Is visible on all pages at all device sizes

### **index.html**
 - **_Log In_** Button:
    - Only visible if the user **_is not_** logged in
    - Changes colour on hover
    - Directs user to _'Log In'_ page
 - **_Sign Up_** Button:
    - Only visible if the user **_is not_** logged in
    - Changes colour on hover
    - Directs user to _'Sign Up'_ page
 - If user **_is_** logged in then **_Reviews_**, **_Add Reviews_**, **_Profile_** and the **_Log Out_** Button is displayed.
    - **_Reviews_** Button:
        - Changes colour on hover.
        - Directs user to the review page.
    - **_Add Review_** Button:
        - Changes colour on hover.
        - Directs user to the add review page.
    - **_Profile_** Button:
        - Changes colour on hover.
        - Directs user to their profile page.
    - **_Log Out_** Button:
        - Changes colour on hover.
        - Logs the user out and redirects them back to the log in page.

### **register.html**
- **_Form Validation_** 
    - All fields must be completed to submit form.
    - If _username_ already exists, flash message informs the user and form is reloaded.
    - If _email_ is already registered, flash message informs user and form is reloaded.
    - Minlength, maxlength and pattern attributes added to username input.
    - _'Sign Up'_ Button 
        - On button click:
            - If form is filled out correctly, submits user information to the users collection
            in the database 
            - Flash message informs user their registration was successful and loads user profile page
            - If form is not filled out correctly, user is informed to fill out missing field.
    -  _'Log In'_ Link - redirects to Log In page.

### **login.html**
- **_Form Validation_** 
    - All fields must be completed to submit form.
    - If _username and/or password_ are entered incorrectly flash message informs user and form is reloaded.
    - _'Log In'_ Button 
        - On button click:
            - If form is not filled out correctly, user is informed to fill out missing field.
         - If form is filled out correctly, users profile page is loaded.
    - _'Register'_ Link - redirects user to register.html.

### **profile.html**
- **_Profile Title_** 
    - Displays the users name
    - Visible on small devices

- **_Delete Account_** 
    - Allows user to delete their account
    - _'Delete Account'_ button:
        - Once pressed will delete the users account and redirect the user to the Home page.

- **_Users Reviews_** 
    - The Profile page will display all the users reviews, at the bottom of each review will be three buttons, Remove, Edit and Buy.
    - _'Remove'_ button:
        - On click will delete the current users review.
        - Redirects user back to the users profile page.
        - Flash message informs user "Review has been deleted"
    - _'Edit'_ button:
        - On click will directe the user to editreview.html.
    - _'Buy'_ button:
        - On click will direct the user to the onlins shop URL provided when the review was created.

### **Allreviews.html** 
- **_All reviews_**
    - The Reviews page will display all reviews by all users.
        - All reviews include the following information.
            - Book cover
            - Title
            - Author
            - Genre
            - Sysnopsis
            - Review
            - Created by
            - Created data
            - Shop Link (Buy This Book)
                - The "Buy This Book" link will redirect the user to the shop page setup during the creation of the review.

- **_Addreview.html_**
    - **_Add Review_**
    - Contains a form for user to add review
    - Allows user to add a review without having to navigate to profile page
    - _Form Validation_ 
        - All fields except _buy link_ and _cover image link_ must be completed to submit form 
            - There are default values set up for these fields if the user leaves them blank 
        - _'Save'_ button: 
            - If form is not filled out correctly, user is informed to fill out missing field
            - If form is filled out correctly, review is added to the database 
                - profile.html is loaded
                - Review is added to reviews.html
        - _'Cancel'_ button:
            - Redirects user back to profile.html

### **Editreview.html**
- **_Edit Review_**
    - Contains a form for user to edit their own review
    - Is popluated with the original infomation added by the user
    - _Form Validation_ 
        - All fields except _buy link_ and _cover image link_ must be completed to submit form 
            - There are default values set up for these fields if the user leaves them blank 
        - _'Save'_ button 
            - If form is not filled out correctly, user is informed to fill out missing field
            - If form is filled out correctly, review is updated in the database 
                - Users profile is loaded
        - _'Cancel'_ button 
            - No changes to the form are saved
            - Users profile is loaded

## **Responsive Design**
This app was developed using the _Mobile First_ philosophy.

Responsive design was tested throughout the development using [DevTools](https://developers.google.com/web/tools/chrome-devtools), [Am I Responsive](http://ami.responsivedesign.is/) and [Responsive Test Tool](http://responsivetesttool.com/)

## **_Code Validation_**

- Code validation was performed using the following tools.
    - [W3C](https://jigsaw.w3.org/css-validator/) - CSS Validation.
        - No errors found.
    - [W3C](https://validator.w3.org/) - HTML Markup Validation.
        - Shows many errors due to the fact I am using jinja2 templating which it does not recognise but other than the expected errors everything else passes.
    - [PEP8 online](http://pep8online.com/) - PEP8 validator.
        - No errors found.
    - [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) - generated the below reports:

    - **index.html**
        - Performance: 89
        - Accessiblity: 92
        - Best Practices: 87
        - SEO: 100

    - **login.html**
        - Performance: 92
        - Accessiblity: 92
        - Best Practices: 87
        - SEO: 100

    - **register.html**
        - Performance: 89
        - Accessiblity: 92
        - Best Practices: 87
        - SEO: 100

    - **profile.html**
        - Performance: 89
        - Accessiblity: 92
        - Best Practices: 87
        - SEO: 100

    - **index.html**
        - Performance: 89
        - Accessiblity: 92
        - Best Practices: 87
        - SEO: 100

    - **index.html**
        - Performance: 89
        - Accessiblity: 92
        - Best Practices: 87
        - SEO: 100

    - **index.html**
        - Performance: 89
        - Accessiblity: 92
        - Best Practices: 87
        - SEO: 100

    - **index.html**
        - Performance: 89
        - Accessiblity: 92
        - Best Practices: 87
        - SEO: 100