
# Milestone 4 Project: Ecommerce Full Stack Framework, Using Django, Python, AWS, SqlLite (ElephantSQL)
[Deployed Project Link](http://event-lister.herokuapp.com/)
![ACME Flydressers](https://github.com/wendybovill/milestone-project-4/blob/1e4de3814bbd065a365cb5473397696f5a1a58cd/Documentation/images/otherimages/ACMEdevices.jpeg)

## Index

[1 Target Audience](#target-audience)

[2 Purpose](#purpose)

[3 Database Schema and Plan](#database-schema-and-site-plan) <br>
&ensp;-&ensp;[3a Database Schema Plan Detail](#database-schema-plan-detail)

[4 User Stories](#user-stories)

[5 Technology Requirements](#tecnology-requirements)

[6 Development Process](#development-process)

[7 Security Features](#security-features)

[8 Site Design Process](#site-design-process)

[9 Future Development](#future-development)

[10 Deployment Process](#deployment-process)

[11 Acknowledgements](#acknowledgements)

[12 Debugging and Test Results](#debugging-and-test-results)

[13 Screenshots and Finished Site](#screenshots-of-finished-site) <br> 
&ensp;-&ensp;[13a Screenshots Showing Update and Delete](#screenshots-showing-update-and-delete) <br> 
&ensp;-&ensp;[13b Screenshots Responsive Design](#responsive-design-screenshots) <br> 

<hr>


# Target Audience

- Fly Fishers who use artificially made Flies to fish for Salmon, Trout and Bass using handmade 'Flies' dressed to look like real insects in order to catch the fish.

- People who want to fish using a specific method, that requires specific equipment and crafted flies are part of this special equipment, but they can't make the equipment themselves.

- The fly fishers who would like to buy these flies or have some bespoke flies made for them.

- Business owner who makes these flies and would like to sell them to his target audience.


# Purpose

- To provide the target audience with a means of purchasing these flies. 
- To provide various options of flies for various seasons. 
- The owner of the business to sell these flies and make a profit.
- To encourage new fly fishers to take up the sport by making these flies easily available and affordable.
- To enable site users to make purchases, orders and to make contact throug a contact form to the site owner.

[Back to Index](#index)

# Database Schema and Site Plan

1. A view that acts as a landing page to the store and a welcome. This view can be changed by the superuser, to add in and remove content on this landing page.

2. The landing page view has options to add sections and to add entries into these sections. The database schema plan shows the planing for these models and views and the way they relate to each other as entities.

3. The landing page also has a functioning contact form, and a view and model to match this is in the database schema. The Contact Us form draws data from the User fields in order to be populated automatically if a user is already logged in.

4. The Contact Us form serves as a way to email the store owner and for the store owner to accept any bespoke orders for products that are not yet available in his store. Customers can ask for specific Flies to purchase.

5. The products can be added and edited and deleted by the store owner when logged in. They can upload images, and link the products with a category and a season. There are 3 categories currently for the flies, they are: Dry flies, Wet flies and Nymphs. The Product model uses data from the Category model by linking with the Primary Key. The Product model also links with the Primary Key from the Seasons model. This enables various means of filtering the products so the user can quickly sort and find the type of fly they need. The Product model also has a price and hook size associated with each product. These are used in the Bag model and the Checkout model when the customer makes a purchase.

6. There signing up is handled by Django All Auth. But this information is passed to Stripe for payment processing. The checkout model creates the order, it is then saved to the user database where they can view their order history.

6. As part of the Product model, there is a Slide model and equivalent database schema, the Slide model is a means to upload slide images for the product page. A url is display and this can be used when creating the slide.

7. An email that gets sent to a user when signing up, to verify their email address. They need to follow
   the emails instructions and click the link that launches the internet browser where they have to input
   their email address and password to log in.

8. There is feedback right throughout the site. By messages from Bootsrap Toasts.



## Database Schema Plan Detail:

The database schema was designed after deciding what the site functionality should be like. It needed to be a Relational Database, which met the requirements for multiple users to be logged, their data
to be restored and orders to be shipped, the users can view their orders at anytime.

Once the views were identified, it was decided what each users would need for the views to operate correctly, portraying the correct information to each user, and this helped decide what routes were needed and therefore the functions to call and operate the routes and views by the user requirements.

This is a Relational Database using Elephant Postgresl, and also using AWS Services for the storage of media. Heroku is the webserver.

The Schema requires 15 tables, being: Site: Home, Entry, Section, Contact, User, Basket/Bag, Products, Categories, Seasons, as well as the Checkout table, Stripe Integration, a Store table for store admin to manage the products and their images etc.

Please view the Database Schema Plan below.




| Database Schema Plan 	|
|---	|
|![Database Schema](https://github.com/wendybovill/milestone-project-4/blob/1e4de3814bbd065a365cb5473397696f5a1a58cd/Documentation/images/otherimages/databaseschema.png)  |


   **Blueprint:** Site Flow Chart Website Views Plan 
![Site Flow Chart Blueprint](https://github.com/wendybovill/milestone-project-4/blob/1e4de3814bbd065a365cb5473397696f5a1a58cd/Documentation/images/otherimages/viewsplan.png)

[Back to Index](#index)



# User Stories

| User   Stories 	| User                        	| Case                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              	|
|----------------	|-----------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| 1              	| Pete - Owner                	| I need a website   I can sell the Fly Fishing flies from. These are handmade, and the site needs   to reflect the relaxing, yet classy sport, and have it appeal to all   generations. I need the site to have the products and categories available, a   checkout process, and an admin backend so that I can manage the products, and   view and dispatch the orders. I also need to be able to do a quote for a   custom order. And have a hidden product I can add to an invoice to be able to   customise that amount for that custom order. 	|
| 2              	| Karen - Admin   and Manager 	| As a site admin   I need to easily be able to add products to the site, and remove or update   them. I also need to be able to add or change special offers. I need to be   able to send emails to the clients when orders are dispatched.                                                                                                                                                                                                                                                                                                        	|
| 3              	| Andrew -   Customer         	| I need to be   able to access the products quickly by their type, and order quickly. I have   limitd time available to relax, and enjoy going fishing when I get the   chance. I want to be able to change the amount of any product ordered and   have a speedy checkout                                                                                                                                                                                                                                                                         	|
| 4              	| Micah - Customer            	| I enjoy fly   fishing but battle to tie my own flies, I'd like to be able to request a   particular fly before placing an order.                                                                                                                                                                                                                                                                                                                                                                                                                  	|
| 5              	| Sally - Customer            	| I don't know   much about fly fishing, but I'd like to be able to go on and view the   descriptions of each product so that I can choose some flies for his   birthday, that he can then use when he goes fly fishing.  I'm not very technical, so need to be able   to checkout easily and would like mutiple checkout options.                                                                                                                                                                                                                  	|
| 6              	| Alex - Customer             	| I need to be   able to save my information and login, and view past orders, so I can keep   and eye on how much I spend. I am saving for a car. I enjoy trout fishing   when I get to go. Its important to me to have the order history in my account   view.                                                                                                                                                                                                                                                                                     	|
| 7              	|                             	|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   	|
| 8              	|                             	|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   	|
| 9              	|                             	|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   	|

[Back to Index](#index)



# Technology Requirements

Html<br>
Css<br>
Javascript
Bootstrap (included in script and style links)<br>
Gitpod<br>
VS Code<br>
Git Repository<br>
JS Query<br>
Favicons (as pngs and linked in styles in html head section)<br>
FontAwesome<br>
ElephantSQL
Gunicorn
AWS S3 Bucket
Pillow - for python images
Heroku<br>
Adobe Illustrator to create the Favicon image<br>
Pexels.com for the free image used on the site<br>
Balsamiq for Wireframes<br>
Lucid Charts for the Site (Flowchart Diagram) and Database Schema<br>
Microsoft Excel to create the usercases that are then uploaded as CSV to convert to MD Tables<br>
MD Table converter<br>
Favicon Converter<br>
Chrome, Firefox, Safari<br>
Ipad, Iphone, Macbook for testing<br>
Windows, Android phone for testing<br>
Python<br>
Various Python Modules:<br>
-   blinker==1.6.2<br>
-   click==8.1.3<br>
-   dnspython==2.3.0<br>
-   Flask==2.3.2<br>
-   Flask-Ext==0.1<br>
-   Flask-Mail==0.9.1<br>
-   Flask-PyMongo==2.3.0<br>
-   ipywidgets==8.0.6<br>
-   itsdangerous==2.1.2<br>
-   jupyter==1.0.0<br>
-   jupyter-console==6.6.3<br>
-   jupyterlab-widgets==3.0.7<br>
-   pymongo==4.3.3<br>
-   qtconsole==5.4.3<br>
-   QtPy==2.3.1<br>
-   Werkzeug==2.3.4<br>
-   widgetsnbextension==4.0.7<br>

[Back to Index](#index)

# Development Process  

**Development Method:**

- After receiving technical specification and design requirements, wireframe was created in Balsamiq. The Html and CSS were created for the templates to, the base template was created using HTML and Django templatetags. Each html page was created as the python functions and routes were created requiring that view.
- CSS was modified on an ongoing basis in accordance with relevant view being developed. CSS was designed with Mobile First approach, allowing for larger screens responsiveness as a last modification requirement. Text across the site is scaled in accordance to the size of the viewing device.
  
- Javascript was used to assist forms and to enhance User Experience. Javascript is used to create a modal popup of the images in the 'View Product' route. Rather than a user just viewing the small image, and a larger image load into a new browser window which the user would then have to go back using the back arrows to get to the site, I applied a JS modal to allow the image to open on the same page and the user to then close it with as little fuss as possible. This is less annoying than a set size image opening and then having to try and find the browser tab you had opened previously. The functions for styles were taken from Bootstrap and adjusted and modified as required according to component instructions. Javascript component has been used for the slideshow on the products view.
  
- Research was done on StackFlow, and WC3 and many other sites, as well as using some code inspired from the CI modules. Function planning and route planning took place before routes were developed. These were planned on paper (I prefer working on paper for planning). Database Schema was also planned on paper before being compiled into a digital document.

- When deciding on the view, the basic variables were setup based on my rough sketches and page flows. The Contact Us form was planned and
implemented in accordance with the required routes, models, forms and urls, using the Django structure, and also retrieving variables and passing them into the routes and templates, such as user, name, email etc.

- The Home page editing was also planned out and then the modal view implemented based on python language requirements and django dependencies. Good practice was followed in order to keep the folder and file structures in place and keep the development environment secure while testing and developing.

- Testing took place at the same time as development. I would develop and then link the dependencies together and then test. Then make changes and test again. I tested right throughout using the problems raised within the Gitpod Visual Code workspace terminals, which has some additional apps from the market place installed that alerted me to an error when there was one. The debug environment was also set to true and this helped with troubleshooting and then continued development. This allowed me to correct code as I was writing throughout, I was testing on the live server.

- The development method involved me planning the site requirements based on user stories, in order to develop a site that was beneficial, we needed to get an idea of the site that needed to be developed and the specifications and features it would require.

- Once the Minimal Viable Product was developed, styles were corrected and then other features were added to enhance user experience, such as the image modal, and the ability for a superuser to change content on the Home page.

- Error correcting took place frequently as my internet connection kept dropping out, requiring me to redo part of the codes (repeatedly), and throwing errors when an incomplete code was committed to github and not updated properly. This meant the development took longer than anticipated and was rather tough for this project.

[Back to Index](#index)



# Security Features

|  	| Security Features Added in the Development Process and Deployment Process: 	|
|---	|---	|
| 1 	| This project contains the use of Allauth, which has robust security if the settigns are correct.  	|
| 2 	| On sign-up the user details are checked in the database to ensure there isn't an existing user, username or password 	|
| 3 	| A confirmation email was sen to the user. 	|
| 4 	| On sign-up a new user is sent an email to their email address where they then click a preconfigured url that will take them<br> to verify their email and log in with the credentials they selected on Sign Up. 	|
| 5 	| Both username and password are case sensitive 	|
| 6 	| The environment (env) file is added to .gitignore file and not made public 	|
| 7 	| Environment secret variables such as Secret_key, passwords, database info, and email host sending logins are set in the<br> Heroku database Var config and not made public, they are kept hidden 	|
| 8 	| Two factor authentication is setup on Heroku 	|
| 9 	| Further defensive programming was developed as part of the testing process, to ensure that a user has to be logged in<br>to make any changes, and that they can only access there own account and posts 	|
| 10 	| Defensive programming was completed to ensure a visitor to the site cannot alter the url to gain access to the backend<br> or to any of the signed up user accounts and features, for example to any area that is restricted to logged In<br> users, or the admin. When altering the url, the visitor is shown an error page and given feedback. 	|
| 11	| Debug mode is set to False in the app.py file  	|
| 12	| A User can only edit and update or delete their OWN entries, not those of others.<br>Those buttons are HIDDEN if the user is not the user who created that entry, or is not an admin user.<br>Admin can edit, update and delete their own and other users entries and profiles.  	|

[Back to Index](#index)


