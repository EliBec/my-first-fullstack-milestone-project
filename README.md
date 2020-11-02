## Full Stack Development Milestone Project (MS4) for Code Institute
<hr>
This project is a practical illustration of the material learned in throughout the course: Front-End and BackEnd. Also, material learned about the DJANGO framwework has been applied to this project.

## Index
* [Project purpose](#project-purpose)
* [Functionality](#functionality)
* [Demo](#demo)
* [UX](#ux)
    * [User Stories](#user-stories)
    * [Design](#design)
        * [1. Font](#1-font)
        * [2. Color Scheme](#2-color-scheme)
        * [3. Logo](#3-logo)
        * [4. Skeleton](#4-skeleton)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Special Features](#special-features)
    * [Features to Implement](#features-to-implement)
* [Technologies Used](#technologies-used)
* [Databases](#databases)
* [Testing](#testing)
    * [Manual testing of all elements on all pages](#manual-testing-of-all-elements-on-all-pages)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Acknowledgements](#acknowledgements)

***

## Becks Outdoors

This is a business idea which emerged from the potential need I realize there is, in the area I live in; given the population and tourism growth we have been experiencing in the last couple of years. This project might be the starting point for a real life scenario for which an e-commerce site will be needed.

### Project purpose
The website's purpose is to serve as an online store (e-commerce website) for customers who are interested in outdoor activities such as paddleboarding, cycling and kayaking. The site serves as a one-stop online store for the items that make possible these activities.

### Functionality

### Demo
A live demo can be found [HERE](https://becks-outdoors.herokuapp.com/)

GitHub repository link can be found [HERE](https://github.com/EliBec/my-first-fullstack-milestone-project)

### UX

### User Stories
The user will be searching and hopefully purchasing an item of interest. The potential customer must find the items easily withouth the need to do too many clicks. 


**User Type (Scope)**
Given this is a site of a brick ann mortar business which also handles sales online of their inventory at the store (or drop-shipments), and as such as business, there will be visitors who are interested in visiting the physical store. So there are are 2 types of users:
1. The user who is looking for an item of interest and wishes to purchase online or at the physical store and, 
2. The user who is interested on knowing more about the businness and what it has to offer, as well as basic information such as contact information, location, etc. 

**As a user:**
- If I am a buyer I want to be able to:
1. Find the product(s) of interested easily.
2. Review the product's relavant information, such as illustrative picture, details, reviews, price and quantity
3. Be able to create a user account where my profile and shipping information can be saved and edited for future purchases
4. Easily pick product for purchase and store it on my shopping bag sesssion, so I can navigate and browse other items. Also, be able to access the shopping cart to see a list of the products I have picked so far
 as well as change the quantity right on the Shopping Cart page
5. Sort the items my price, category or brand
6. See a comprehensive list of products on the same page
7. Find Review information about the business I am considering to purchase from. 
8. Receive confirmation information on the purchase(s) I make
9. Access to my purchase history
10. Ability to book an appointment for bicycle service via the website
11. Access to the appoinments history
12. Ability to see other customer's reviews and also publish, edit or delete my review
13. I want the checkout process to be easy to follow and with a few steps. 
14. I would like to find the contact information of the business just in case I need assistance with the website or have a question about a product.

**As an Admin**
* Ability to manange products (Add, Update and Delete) on the website's front-end, so there is no need to log in to the Admin module to do so.
* If needed, I would like to be able to access the Admin module site, to manage products, users, product categories and sub-categories

**Developer:**
* As a Developer, I want to expand my knowledge with Python and DJANGO by creating an extensive management database application, including admin module
* As a Developer, I want to create a fully-responsive mobile-friendly multi-language faceted project to showcase what I have learned whilst on this course.
* As a Developer, I want a project which can evolve as I grow as a developer.
* As a Developer, I would like to extend this particular project to add the complexity of invetory management, which will be required if this business materialize

### Strategy
The website's strategy is centered in two words: simplicty and usefulness. This website is a resourceful, inconme-generating tool for a business that wishes to sell outside the walls of the physical store. 


### Structure used to help them users achieve these things:
- The website is mostly linear, with easy-to-read fonts and intuitive options to follow. 
- The website contains a separate page for each section, as opposed to a single long page. This will help he user do the task easily by placing the focus on the page's single task. 
- The header navigation bar is clipped to the top and remains that way as the user scrolls down or up, thus providing convenient way to access the pages. 
- Footer provides quick contact information. Available in all pages, the user won't need to navigate to a specific page


### Design
The website is fully responsive. To achieve this, I used [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/download/)

### Font
The font-family used is 'Acme' and 'Kanit'. The Acme is used to give more emphasis to relevant information such as product name and brand. The default font is sans-serif
Acme was imported from [Google Fonts](https://fonts.google.com/specimen/Acme?query=acme). 
Kanit was imported from [Google Fonts](https://fonts.google.com/?query=kanit).

### Logo
Simple logo for now, emphasizing branding over illustration. it was my wish to have more time to complete the design of an alternative logo, but only counting on only 1 month to complete this project, time was the biggst factors for all the improvements I wanted to make was unable to.
To generate this logo I used [Canvas Logo Maker](https://www.canva.com/tools/logo-maker-q1/?msclkid=9d6e8ceab70a1f66065dd375c4e6f6bd&utm_source=bing&utm_medium=cpc&utm_campaign=REV_US_EN_CanvaPro_Branded_Tier2_EM&utm_term=canva%20logo&utm_content=REV_US_EN_CanvaPro_Branded_Tier2_Logo_Maker_EM&gclid=CLGky_Xs4uwCFcgOgQod9RcLIg&gclsrc=ds) 


### Color Scheme
All colors were chosen using the [Adobe Color Wheel](https://color.adobe.com/create/color-wheel). Main colors used were green and dark brown to convey a message of nature and outdoors.

Nav color:
- ![#36A21E](https://placehold.it/15/36A21E/000000?text=+) #36A21E.

Some font color:
- ![#36250C](https://placehold.it/15/36250C/000000?text=+) #36250C

- Other colors:
  ![#008000](https://placehold.it/15/008000/000000?text=+) `Green`

- Font color: ![#fafafa](https://placehold.it/15/fafafa/000000?text=+) `#fafafa`

- Overlay: ![#CAF5C7](https://placehold.it/15/caf5c7/000000?text=+) #caf5c7


### Skeleton

Each wireframe file displays desktop, tablet and mobile phone view. 

[Landing Page wireframe](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Home-%20Index.html.png)

[Services wireframe](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Services.png)

[About us wireframe](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/About%20Us.png)

[Shoping Cart](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Shopping%20Cart.png)

[Checkout Page ](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Checkout.png)

[Checkout Confirmation](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Checkout%20Confirmation.png)

[Products Page](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Products%20Page%20(All%20Products%20or%20Category).png)

[Product Detail](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Product%20Detail.png)

[Add Product](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Add%20Product.png)

[Add Appointment](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Add%20Appointment.png)

[Sign Uo](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/Sign%20Up.png)

[User Profile](https://github.com/EliBec/my-first-fullstack-milestone-project/blob/master/wireframes/User%20Profile.png)

## Features
<hr>

Each page features a responsive navigation bar with conventional placing of logo (top left). Each page has a footer with copyright information, social media icons (currently, there is no real link social media pages for there is no existing social media accounts) and an illustrative map of the ficticious location of the business
Every non-ecommerce page displays a picture banner (same banner image for all pages).
A Back to Top button is included to help theuser navigate back to the top of the page when has scrolled down twice

#### Home page
Informational page with top navgation. it also offers the convenient "SHOP NOW" button, so users can go straight to the Products page

### Services
Informational page about bike repairs. It also includes a button to make a service appointment. Onlly users with an exixting account can book an appointment 

### Product Management
Accessible to Admin users only, this page is useful for adding products to the website. It inlcudes the ability to load a product photo

### Products
Comprehensive list of products based on the search or via menu choices 
On this page, a breadcrumb is conveniently located so user can navigate to pages related to this prouct to browse similar products
Finally, a Sort By box is included to help user review different products based on its criteria

### Product Detail
Provides all the relevant information about the product (description, picture, price, review(s) and quantity, as well as the "Add to Cart" button. 
From this page, customers who have previously purchased a product (and are logged in to their account) can publish, edit and delete a product Review. 
Admin users can Edit or Delete a product from this page

#### Shopping Cart
Provides the user with the information (price per product and total amount for the order) all the relevant inforation on the products saved on the Shopping Cart
While on this page, the user can update the quantity to purchase and even remove the item from the Shopping Cart (i.e. manage cart contents)
It also includes the Checkout button for when the user is ready to proceed

#### Checkout 
Here is where the payment process is submitted and committed. Users must have an account and be logged into that account in order to complete the purchase process and submit payment 

#### Checkout Confirmation
Friendly page showing the order placed and the products included on that order

#### User Profile
Page displays user's delivery information as well as order history. From this page, user can select the order number, which will take me to a separate page with the order confirmation page 

#### Add Appointments
Offers a form for the user to submit an service appointments.Only users with an account can use this features

#### Appointment 
Displays information on previously submitted service appointments

#### Appointment Detail 
Displays detail information on previously submitted service appointments

#### Add Review
Supplies the user with a form to enter product review information and rating as well as the submit button

#### Edit Review
Supplies the user with a form to edit product review information and rating


### Existing Features:
- Header logo and header website title: displayed on each page and positioned on the top lef-hand side. When clicked on, it will take the user to the home page.
- Header Navigation Bar: is present on each page. It is fixed to the top of the screen and available to the user as the screen is scrolled down or up. The nav's purpose is to conveniently navigate to the different pages. 
- Footer's Copyright Info: is present on every page. This is informational and with the purpose of protecting the author's rights.
- Footer's Social Icons: is present on every page. It offers the user an easy way to access social media pages. 
- Back to Top button for easy page navigation
- Anchor to the Review section in the Product Detail page

### Special Features
- Integration of Stripe for payment processing
- Django's Admin module for backend CRUD functionality 
- Product Manageent (CRUD) in the website's frontend
- Bootstrap's Toasts for messages and notifications to the user
- User account and authorization in order to complete purchase transaction, posts product reviews and booking appointments


### Features to implement:
Some of the features listed below could have been implemented, but time constraints did not make it possible for the moment
- Inventory management 
- Add the time and calendat icons for the Add Appointment form
- Product Specfication section on the Product Detail page (espacilly for bikes)


## Technologies Used

Frontend was built using: HTML5, CSS3, and [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/download/) frameworks

[Google Fonts](https://fonts.google.com/): for website fonts

[Font-Awesome-5](https://fontawesome.com/) and [FontAwesome's](https://www.bootstrapcdn.com/fontawesome/) Bootstrap CDN: for icons

[Gitpod](https://www.gitpod.io/): for IDE used on this project (MS2)

[Python](https://www.python.org/): backend programming language

[DJANGO templates](https://docs.djangoproject.com/en/3.1/topics/templates/)

[Django Frameworks](https://docs.djangoproject.com/en/3.1/)

Django's Allauth for user authentication and account
 
[jQuery](https://jquery.com/)

[Google API](https://cloud.google.com/maps-platform/): for Google Map on footer

[Heroku](https://www.heroku.com/): A cloud platform as a service enabling deployment for this CRUD application.

[stripe](https://stripe.com/)

[Amazon Web Services - Simple Storage Service (AWS -S3)]() to host the project's images


#### Tools Used:


[Adobe Color Wheel](https://color.adobe.com/create/color-wheel)
for color picking. 

Google Chrome Dev Tools - for testing of the application's responsiveness, on-th-fly testing css editing tool and for console monitoring for Javascript and JQuery 

[Balsamiq](https://balsamiq.com/) for the creation of wireframes

[Favicon Generator](https://favicon.io/) for the creation of a fav icon. It is not exactly the same as the logo (due to time contraints) but close enough to convey the brand.

[Free Formatter](https://www.freeformatter.com/html-validator.html) for HTML code checking

[CSS Validation Service](https://jigsaw.w3.org/css-validator/) for CSS code checking

[JSHint](https://jshint.com/) for Javascript code checking

[PEP 8 Online](http://pep8online.com) for Python code checking



## Testing

Test has been performed throughtout the different stages of the website build. Responsiveness of the website has been tested using both physical devices (including smart cellphones, tablets and desktop) as well as browser tools such as Google Chrome Dev Tool.
The website has been tested on a variety of internet browsers, such as: Google Chrome, Internet Explorer, Micresift Edge, Firefox and Opera to ensure compability. 

The following tools were used to ensure code quality:

For HTML: [Free Formatter](https://www.freeformatter.com/html-validator.html)

For CSS: [CSS Validation Service](https://jigsaw.w3.org/css-validator/)

For Javascript: [JSLint](https://jshint.com/) version 2.11.1

For Python: [PEP 8 Online](http://pep8online.com) for Python code checking


### Databases

Below are the list of models used: 

- Product Model: stores information about the product. 
- Category: stores category for a product
- Subcategory: stores a subcategory of a product
- Order: stores customer purchase information 
- OrderLine: stores product information on a order
- User Profile: stores cuatomer's account shipping information
- User (handled  by django's allauth): stores information about customer's account
- Appointment: custom model for user's appointment infomation 
- Rating: custom model for product's revew information

#### Model Relationship

PRODUCT <==> ORDER:  A product belongs to 1 order but 1 order can have many products
ORDER <==> ORDERLINEITEM: an order and have ma line items, but a line item belongs to a product
PRODUCT <==> CATEGORY: a product can belong to a single category, but a category can have many products
PRODUCT <==> SUBCATEGORY:  a product can belong to a single subcategory, but a subcategory can have many products
CATEGORY <==> SUBCATEGORY: a category can have many subcategories, but a subcategory belongs to a single category
PRODUCT <==> RATING: a product can have many ratings, but a rating can only belong to a single product

USER <==> ORDER: a user can have any orders, but an order belongs to a single user (customer)
USER <==> APPOINTMENT: a user can make many appointments, but each appointment belong to a single customer
USER <==> RATING: a user can publish many reviews (one per product) but a review belongs to a single user


#### User Experience testing: 

Testing was performed in order to verify the following:

- All links should resolve of a page (no orphans links, except to the social media icons on the footer)
- All navigation links should work
- Pages should be responsive and mostly consistent on different internet browsers
- Forms rules should be enforced (especially for required fields)

### Manual testing of all elements on all pages

The following tasks were tested:

- Live page is reachable after deployment
- User can navigate pages without page errors
- User can use the Sort By box
- User confirms Back to Top button shows up after soe scrolling down the page
- User can create, log in and log out an account. Creating an account adds a new reocrd to allauth user
- User can add, remove item(s) to the shopping cart. In shopping cart, user can update the quantity
- User can only proceed to checkout if she/he is logged in to the user account
- User is directed to an Order Confirmation page after checkout is succesful
- User receives an email confirmation after purchase is completed
- User can  process payment using the following ficticious credit card number:
   4242 4242 4242 4242 4242 (the card's zip code or expiration month and year can be anything, but make sure month and year are within the range)
- When the user checks out, a new record is created for the Order model. Each item purchased should be a new record on the Order Line Item. When the order is created, the total aount is updated
- Admin users can  Add, Delete and Edit products. These changes affect the Product model (adding, deleting or updating the record in question)
- User can update the Delivery information in the User Profile page
- User can view Order history in User Profile page
- User can only book an appointment if she/he is logged in to the user account. When a user adds an appointment, a new record in the Appointment model is created
- User can only posta review if she/he is logged in to the user account and has previusly made a purchase for the product he/she wants to post a review
- Admin users can access Django's module to perform CRUD operations on any model

#### Note:
Social media pages have not been created yet, but icons there are available on the front end.
Purchase ticket functionality has not been implemented yet, so Purchase Ticket buttons will not take the user to a purchasing page 


## Deployment


1. In heroku (heroku.com): create an app and give it a name
2. In heroku: >  create a new app > give it a new
3. In heroku:Resources tab >  Heroku Postgress > get the free version
4. In Gitpod: command line: pip3 install dj-database-url
5. In Gitpod: command line: pip3 install psycopg2-binary
6. In Gitpod: pip3 freeze > requirements.txt
7. import the dj-database url in settings.py (import dj_database_url)
8. comment out the default database in settings.py and replace the values with d_database_url and config var DATABASE_URL from heroku
9. Run migrations: python3 manage.py migrate
10. Create superuser
11. Install unicorn
12. Create Procfile and add web: gunicorn becks_outdoors.wsgi:application
13. Go to heroku and set DISABLE_COLLECTSTATIC=1 so that heroku won't try to collectstatic files when deploying
14. Add the host in the ALLOWED_HOSTS in settings.py
15. commit and push to github
16. push to heroku (git push heroku master).Might need to initalize heroku first (heroku git:remote -a name of the app
17. enable automatic deployment in heroku
18. Generate an automatic DJANGO secret key (using django online generator) and add it as a variable in heroku
19. Create AWS S3 account, set groups and policies and import the static files and media files
20. Add Stripe's secret and public keys in heroku
21. Set a new webhook receiver in Stripe and copy the webhook key in heroku


### Clone Repository
To clone the repository the steps below must be taken:

Select the Repository from the Github Dashboard.

Click on the "Clone or download" dropdown button which is located beside the Gitpod button to the right.

Click on the "clipboard icon" to the right to copy the web URL.

Open your preferred Integrated Development Environment (IDE) and navigate to the terminal window.

Change the directory to where you want to clone the repository too.

Paste the Git URL https://github.com/EliBec/my-first-fullstack-milestone-project.git and click "Ok".


## Credits

<hr>

### Content

- The use of the CRUD functionality was learned from the CI course. 

- Many code snippets were taken CI's project example (Boutique Ado) and modified to fit the project's case.

- Google Maps dynamic functionality code was learned from Google API and from from another student's [project](https://github.com/maliahavlicek/what2do2day) 



### Code

Some research was done using sites and learning material other than CI. There was a good aount of readon tutorials and DJANGO documentation

These are:

* [Stack Overflow](https://stackoverflow.com/)
* [W3Schools](https://www.w3schools.com/)
* [DJANGO Documentation](https://docs.djangoproject.com/en/3.1/)
* [IQ Tutorial on DJANGO](https://overiq.com/django-1-11/)
* [About DJANGO Signals](https://studygyaan.com/django/how-to-use-and-create-django-signals)
* [About DJANGO Sessions](https://www.tutorialspoint.com/django/django_sessions.htm)
* [STRIPE Documentation](https://stripe.com/docs)


### Media

- The image for both the banners and the About us page were take from [PEXELS](https://www.pexels.com/).

### Acknowledgements

- I would like give a huge thank you to the Slack community, the tutor support team (you guys rock!) and for all the guidance from my mentor Moosa Hassan

Disclaimer: This project's website is created as a educational project (Milestone project 3) for the Code Institute's Full Stack Developer course.