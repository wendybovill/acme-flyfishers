
# Milestone 4 Project: Ecommerce Full Stack Framework, Using Django, Python, AWS, SqlLite (ElephantSQL)
[Deployed Project Link](https://acmeflydressers-882ac53eca0c.herokuapp.com)

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


<hr>


# Target Audience

- Fly Fishers who use artificially made Flies to fish for Salmon, Trout and Bass using handmade 'Flies' dressed to look like real insects (" or a potential food item") in order to catch the fish.

- People who want to fish using a specific method, that requires specific equipment and crafted flies are part of this special equipment, but they can't make the equipment themselves.

- The fly fishers who would like to buy these flies or have some bespoke flies made for them.

- Business owner who makes these flies and would like to sell them to his target audience.


# Purpose

- To provide the target audience with a means of purchasing these flies. 
- To provide various options of flies for various seasons. 
- The owner of the business to sell these flies and make a profit.
- To encourage new fly fishers to take up the sport by making these flies easily available and affordable.
- To enable site users to make purchases, orders and to make contact through a contact form to the site owner.

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

This is a Relational Database using Elephant Postgresl, and also using AWS Services for the storage of media. Heroku is the webserver. The Relational database allows for Table (Schema) linking from one to another, using ForeignKeys. 

The Schema requires 13 tables (apart from the Site one itself): Home, Entry, Section, Contact, User, Basket/Bag, Products, Categories, Seasons, as well as the Checkout table, Stripe Integration, a Store table for store admin to manage the products and their images etc.

Please view the Database Schema Plan below.
It portrays how each table(schema) retrieves information from the other database and then returns information to be saved in itself or another table(schema).
I prefer Relatonal databases over non-relational databases. I find they keep themselves inorder and need little maintenance and its 



| Database Schema Plan 	|
|---	|
|![Database Schema](https://github.com/wendybovill/milestone-project-4/blob/1e4de3814bbd065a365cb5473397696f5a1a58cd/Documentation/images/otherimages/databaseschema.png)  |


**Site Flow Chart Website Views Plan**
![Site Flow Chart Blueprint](https://github.com/wendybovill/milestone-project-4/blob/1e4de3814bbd065a365cb5473397696f5a1a58cd/Documentation/images/otherimages/viewsplan.png)

[Back to Index](#index)



# User Stories

| User   Stories 	| User                        	| Case                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              	|
|----------------	|-----------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| 1              	| Pete - Owner                	| I need a website   I can sell the Fly Fishing flies from. These are handmade, and the site needs   to reflect the relaxing, yet classy sport, and have it appeal to all   generations. I need the site to have the products and categories available, a   checkout process, and an admin backend so that I can manage the products, and   view and dispatch the orders. I also need to be able to do a quote for a   custom order. And have a hidden product I can add to an invoice to be able to   customise that amount for that custom order. 	|
| 2              	| Karen - Admin   and Manager 	| As a site admin   I need to easily be able to add products to the site, and remove or update   them. I also need to be able to add or change special offers. I need to be   able to send emails to the clients when orders are dispatched.                                                                                                                                                                                                                                                                                                        	|
| 3              	| Andrew -   Customer         	| I need to be   able to access the products quickly by their type, and order quickly. I have   limited time available to relax, and enjoy going fishing when I get the   chance. I want to be able to change the amount of any product ordered and   have a speedy checkout                                                                                                                                                                                                                                                                         	|
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
-   asgiref==3.7.2
-   boto3==1.28.5
-   botocore==1.31.5
-   dj-database-url==0.5.0
-   Django==3.2.20
-   django-allauth==0.41.0
-   django-colorfield==0.9.0
-   django-countries==7.2.1
-   django-crispy-forms==1.14.0
-   django-storages==1.13.2
-   gunicorn==20.1.0
-   jmespath==1.0.1
-   oauthlib==3.2.2
-   Pillow==10.0.0
-   psycopg2==2.9.6
-   python3-openid==3.2.0
-   pytz==2023.3
-   requests-oauthlib==1.3.1
-   s3transfer==0.6.1
-   sqlparse==0.4.4
-   stripe==5.5.0
-   urllib3==1.26.16

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
| 3 	| A confirmation email was sent to the user. 	|
| 4 	| On sign-up a new user is sent an email to their email address where they then click a preconfigured url that will take them<br> to verify their email and log in with the credentials they selected on Sign Up. 	|
| 5 	| Both username and password are case sensitive 	|
| 6 	| The environment (env) file is added to .gitignore file and not made public 	|
| 7 	| Environment secret variables such as Secret_key, passwords, database info, and email host sending logins are set in the<br> Heroku database Var config and not made public, they are kept hidden 	|
| 8 	| Two factor authentication is setup on Heroku 	|
| 9 	| Further defensive programming was developed as part of the testing process, to ensure that a user has to be logged in<br>to make any changes to their profile and view their orders. 	|
| 10 	| Defensive programming was completed to ensure a visitor to the site cannot alter the url to gain access to the backend<br> or to any of the signed up user accounts and features, for example to any area that is restricted to logged In<br> users, or the admin. When altering the url, the visitor is shown an error page and given feedback. 	|
| 11	| Debug mode is set to False in the settings.py file using Developement mode variables set in Heroku and the development environment hidden env.  	|
| 12	| A Registered User can only edit and update or delete their shipping details and personal information, not those of others. Historical Orders are rendered to view but can't be edited. Users can add products to basket, update their basket and remove items from their basket, as well as proceed to checkout.<br>Admin can edit, update and delete products and view orders and emails in the backend. Admins if logged into the backend can alter the Home Page content 	|

[Back to Index](#index)




# Site Design Process

1. Content:

The Front page is designed differently to accommodate content added by the SuperUser. As there is a background image, the footer is deliberately plain black.
The rest of the site uses a plain background and then the footer is an image to reflect the first page image. This is not an error, it was a design plan to remove any clashing of images on the front page, and the plain background for the rest of the site so as not to distract from the images of the products of handcrafted 'Flies'.


2. Design: 

**Wireframe with Balsamiq:**

| Mockups |
|----------------|
| ![Balsamiq Wireframe](https://github.com/wendybovill/milestone-project-4/blob/f746d83e02044ecc7e3cc33e38deaa298694d5bc/Documentation/images/otherimages/wireframe1.png)     |

*Logo:* Photo of a Handcrafted fly, edited in Photoshop and then imported into Illustrator, where it was converted to SVG and then the rest of the logo
was designed in Illustrator and hand drawn. Client gave specifics of what he required for his brand.

*Colours:* Red Outer Circle, but not solid, needs to look like thread. Logo text around the inside of the cirlce. Fly in the middle. 
(Colour symbolism: Red: excitement, and eyecatching, Gold (on hook): Sophistication and Class, Black: Daring and bold. The rest of the sites colours were in contrast with those to also encourage the user to reflect on the activity of being in nature, in solitude, at peace, while waiting to catch a fish.

3. Documentation including readme file, spec sheet. Estimated time 1 week.

4. Development strategy: Develop the base views and build on those then add the styles, which is then used as a template for the rest of the site pages, models etc.
   
5. The code for the Routes are determined by the Views required and the way they need to function and relate to the other models and views. The Database Schema is created based on the functionality plan and routes required.


## Design Variation:
The site has extra features added which are not in the original mockups/wireframes, such as a contact us link on the bottom of the page, the basket views, checkout views, view to edit front page, the Javascript feature of the modal image popup view, was added because as a Test User I found it frustrating that I had to keep closing the tab that was opened, and then trying to find the tab that I had previously been on. So instead I have made the image pop up with a button to click to close the modal and get returned to the same page the user was on before.

[Back to Index](#index)



# Future Development

1. Add a feature to add slides into the slidehow using a form on the admin front end login.

2. Add an option to be able to enter international postage into the Grand Total.

3. Add some Javascript to determine when the best time to fish is, based on Season and Time, and then to recommend the Fly that is best suited for that job.
 
4. Add the social login option using AllAuth.

6. Make changes to the logged in customer form, for a registered customer to upload an image, that they can then add to a new view where they cans show the latest fish they caught, and discuss the seasonal conditions and what fly was used etc. This requiring a checkbox approval from admin before being viewable.

7. Add a route, view and functions for the admin to see all uploaded images as a media library.

[Back to Index](#index)



# Deployment Process

|    	| Deployment Steps:                                                                                                                                                                                   	|
|----	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| 1  	| Sign Up to Heroku or Sign in                                                                                                                                                                        	|
| 2  	| Create a new App on Heroku                                                                                                                                                                          	|
| 3  	| Go to ElephantSQL and sign up or sign in                                                                                                                                                            	|
| 4  	| Create a new database and Sign in                                                                                                                                                                   	|
| 5  	| Then go to AWS Bucket Storage, and Join up or sign in                                                                                                                                               	|
| 6  	|  Go to Heroku and  in he Database create a Superuser                                                                                                                                                	|
| 7  	|  In the dev terminal install heroku                                                                                                                                                                 	|
| 8  	| When in Elephantsql                                                                                                                                                                                 	|
| 9  	| In elephant sql check Browser and run SQL Query , you should see your new   Superuser                                                                                                               	|
| 10 	| Add to your settings file: ACCOUNT_EMAIL_VERIFICATION = 'none'                                                                                                                                       	|
| 11 	| In AWS selecte ACLs and create your bucket policy.                                                                                                                                                  	|
| 12 	|    Add ACLs enabled and Bucket Preferred owner                                                                                                                                                      	|
| 13 	|  On the properties tab, static   website hosting scroll down to the permissions tab                                                                                                                 	|
| 14 	| Paste the CORS configuration into the Cross-origin-resource-sharing(CORS)   setion                                                                                                                  	|
| 15 	| Access the Access Control List and click and edit, to enable the Everyone   getting  public access to List the   content                                                                            	|
| 16 	| Then create a user group, and a user group policy which you will need to   attach to the User Group (select permission dropdown)                                                                    	|
| 17 	| Connect to Django                                                                                                                                                                                   	|
| 18 	| Install boto3 and Django storages in and django storages via python   manage in the terminal                                                                                                        	|
| 19 	| Add storages as an installed app in django                                                                                                                                                          	|
| 20 	| Then add an if statement: if "USE_AWS in the environment if there   is then define the AWS_STORAGE_BUCKET_NAME.                                                                                    	|
| 21 	| AWS_S3_REGION_NAME and our acess key, and secret access key we need to   get from the environment. - Keep these secret, only add them to Heroku config   Vars                                       	|
| 22 	| Then go to AWS and create a media storage folder, grant the public read   access only                                                                                                               	|
| 23 	| Upload your Product images to the newly created media folder.                                                                                                                                       	|
| 24 	| Then click grant public read access to those Objects.                                                                                                                                               	|
| 25 	| Confirm the superuser on the Postgres database. Do that in the django   admin. You will need to use the email confirmation link to do this,get the   link from the Heroku logs.                    	|
| 26 	| Then go to Stripe to get the Stripe Keys.                                                                                                                                                           	|
| 27 	| Once you 've got them, go back to heroku and add them as config vars   (found in settings)                                                                                                          	|
| 28 	| We need to create a new webhook  as   the one created is used for the gitpod app,                                                                                                                   	|
| 29 	| Go to the developers menu add new webhook and a new end point for it   /checkout/WH then select all the events to receive. And add the endpoint.                                                    	|
| 30 	| These variables need to match what is in your settings.py file                                                                                                                                      	|
| 31 	| Ensure you have your secret keys hidden and your environ file is set to   be ignored in gitignore file.                                                                                             	|
| 32 	| Push your updated code to github.                                                                                                                                                                   	|
| 33 	| If you have already connected your gitub to heroku and its set to   automatically deploy, then all you have to do is push it and heroku will   receive the update and rebuild the app and start it. 	|
| 34 	| Heroku will direct the files on Github and run them like a web server.   But  you need to deploy to update the   github to the latest version so that Heroku can deploy it                          	|
| 35 	| When you have pushed the new committed git then click app to view the   app. You can also view the logs to catch any errors.                                                                        	|
|    	| Make sure you have turned DEBUG off by setting it to False in you Env   file but especially in you Heroku Config Vars in Settings                                                                   	|



[Back to Index](#index)



# Acknowledgements

- Stackflow was referenced but the solutions I needed were not in there instead language documentation was used eg. python, django, stripe, aws, elephantsql along with previoius projects consulted for a refresher<br>
- I used notes I made during the module lessons, and the documentation for python and dependencies.<br>
- Pep8 Standards were followed and pylint in visual studio code was used
- Bootstrap for use of their css
- Markdown table generator used: https://www.tablesgenerator.com/markdown_tables
- Lucid Chart for the Site plan and the Database Schema Plan
- Favicon for its converter from png to favicons
- Adobe Illustrator and Photoshop to make the Logo and edit the images for the Site and Documentation
- Balsamiq to make the wireframes
- Gitpod for the Workspace environment
- Github for commits and keeping track
- Heroku for deployment and webserver
- ElephantSQL for a Relational database free tier
- Code Institue for training and instruction

[Back to Index](#index)



# Debugging and Test Results

**TEST CASES:**

| **Test Cases:** 	|
|---	|
| **ID 1** 	|
| Title Testing in Safari Browser with Gitpod 	|
| Owner wendybovill 	|
| Precondition Required: Sarari Browser. Heroku. Gitpod/Visual S Code Terminal. Debugging ON/True 	|
| Steps:  	|
| Opened Site. Tried to confirm email after sign up, but there was an Endblock error. FAIL It was a template error with a a missing end block in the template html file itself. Fix: Involved Adding the endblock. Opened Site. Loaded Signup page. Filled in Form. on submission sign up occurred and redirected as per route defined on call back. PASS 	|
| View Screenshot 	|
| Priority Medium 	|
| Status Completed 	|
| Estimate 30 minutes 	|
| Type Acceptance 	|
| Automation Manual 	|
| **ID 2** 	|
| Title Testing in Safari Browser with Gitpod 	|
| Owner wendybovill 	|
| Precondition Required: Sarari Browser. Heroku. Gitpod/Visual S Code Terminal. Debugging ON/True 	|
| Also required: Sign Up Email Account Verification 	|
| Steps:  	|
| After Sign Up, verification email was not received. The folder was not nested correctly. I corrected this and then the email appeared to be sent as following view was loaded to please confirm your email address and we could follow the link to verify email. FAIL. The Fix was to move the folder from where it was nested accidentally under another folder. The correct template could then be rendered. Email verification was then completed. PASS 	|
| Priority Medium 	|
| Status Completed 	|
| Estimate 25 minutes 	|
| Type Acceptance 	|
| Automation Manual 	|
| **ID 3** 	|
| Title Testing in Safari Browser with Gitpod 	|
| Owner wendybovill 	|
| Precondition Required: Sarari Browser. Heroku. Gitpod/Visual S Code Terminal. Debugging ON/True 	|
| Also required: Contact Us Email Sending 	|
| Steps:  	|
| Clicking contact us loads the correct form view. Filling in information and click send - no errors. Sending emails and loading next view (email success) PASS Locally. FAIL when deployed. The Fix to correct a typos in the setting in Heroku, where TLS was spelt TSL and so the correct settings were not being used to send the email. Once changed to to TLS, The correct template could then be rendered. Email sending in deployment was successful. Debugging was set to Off/False. PASS 	|
| Priority Medium 	|
| Status Completed 	|
| Estimate 40 minutes 	|
| Type Acceptance 	|
| Automation Manual 	|
| **ID 4** 	|
| Title Testing in Safari Browser with Gitpod and Heroku 	|
| Owner wendybovill 	|
| Precondition Required: Sarari Browser. Heroku. Gitpod/Visual S Code Terminal. Debugging ON/True 	|
| Steps:  	|
| Login was successful. Adding products to the basket to check out was successful. Going through checkout FAIL. The callback function after checkout rendered a template with an error in, again missing and endblock or endif. After correcting this the template rendered with no errors. PASS 	|
| Priority Medium 	|
| Status Completed 	|
| Estimate 20 minutes 	|
| Type Acceptance 	|
| Automation Manual 	|
| **ID 5** 	|
| Title Testing in Safari Browser 	|
| **Owner ** wendybovill 	|
| Precondition Required: Sarari Browser. Heroku. Gitpod/Visual S Code Terminal. Debugging ON/True 	|
| Steps:  	|
| Logging in as Admin reveals the product management page on the frontend and on the backend reveals the Database options to view orders and emails sent to the Admin. This was done successfully. PASS 	|
| Priority Medium 	|
| Status Completed 	|
| Estimate 10 minutes 	|
| Manual 	|
| **ID 6** 	|
| Title Adding Content to the Index Page as Admin Superuser 	|
| Owner wendybovill 	|
| Precondition Required: Testing in Safari Browser. Chrome Browser. Firefox Browser. Internet Explorer and mobile devices: 	|
| Admin User Adding Content to the front page landing page 	|
| Steps:  	|
| Despite there being content in the fields and in the template, this content was not being renenderd on the home page. FAIL. There was an endblock missing and and endif template tag. After this the content added by the admin in the backend was then visible on the frontpage. PASS 	|
| Priority Medium 	|
| Status Completed 	|
| Estimate 1 hour 	|
| Type Acceptance 	|
| Automation Manual 	|
| **ID 7** 	|
| Title Testing in Safari Browser 	|
| Owner wendybovill 	|
| Precondition Required: Sarari Browser. 	|
| Steps:  	|
| Tested adding products to website through admin user. PASS 	|
| Priority Medium 	|
| Status Completed 	|
| Estimate 10 minutes 	|
| Type Acceptance 	|
| Automation Automated 	|
| **ID 8** 	|
| Title Testing for Responsiveness 	|
| Owner wendybovill 	|
| Precondition Required: Testing in Safari Browser. Chrome Browser. Firefox Browser. Internet Explorer and mobile devices: 	|
| Mobiles Apple Iphone XS. Iphone 8 Plus and Android Hero. 11 and 12 Inch Ipads 	|
| Steps:  	|
| Tested many times. Kept failing due to internet connection issues and github not being updated correctly on commits (as connection errors were not sending complete commits). Now PASS 	|
| Priority Medium 	|
| Status Completed 	|
| Estimate REPEATED A FEW HOURS OR SO - INTERNET CONNECTION ISSUES 	|
| Type Acceptance 	|
| Automation Manual 	|
| **ID 9** 	|
| Title With w3 CSS 	|
| Owner wendybovill 	|
| Precondition Required: Testing in Safari Browser. Chrome Browser. Firefox Browser. Internet Explorer and mobile devices: 	|
| Mobiles Apple Iphone XS. Iphone 8 Plus and Android Hero. 11 and 12 Inch Ipads - W3C Schools html validators 	|
| Steps:  	|
| The validation service flagged up some code in the template files. These were actually in relation to labels for a dropdown menu component from bootstrap. There were no errors, it was required to enable the dropdown to work. The second ID it refers to was not an id at all but a label refering to the Id of the required element for the function to work. IGNORED as third party reliance, Bootstrap and Allauth 	|
| Priority Medium 	|
| Status Completed 	|
| Estimate 1 hour 	|
| Type Acceptance 	|
| Automation Manual 	|

[Test File Showing Screenshots](https://github.com/wendybovill/milestone-project-4/blob/a0a4038e58691aa39efb0301ac0b2a9f3e82d119/Documentation/Test.MD)



[Back to Index](#index) 


**Screenshots of Features**
[View Screenshots of Features](https://github.com/wendybovill/milestone-project-4/blob/9261f3dd13504c0ec4aa644f72deb24d10c0f5e6/Documentation/Screenshots_of_files.MD)
- Product Management for Admin
- Product Managment Restricted for Customer
- Home page content managment
- Emails sent and received


**User Testing:**

Manual Testing various possible user attempts to work around the site security was undertaken to ensure a user could not:
- urls cannot be changed to gain access to restricted areas, users are redirected either through http error status responses to the index page with a relevant message or on the same pages with flash messages instructing them they are not authorized and need to log in (where appropriate)
- Allauth has a robust system for authentication and security
- HTTPError handlers were setup to redirect for index page along with information about the errors.
- During testing signups, logins, logouts any errors were caught by the debugging system and then corrected.
- The worst errors came from styles not updating or saving properly and needing to be redone.
- Stripe has had intermittent handling failures but this is due to the checkouts not completing when I lost connection as been having issues with my internet connections. Everything is installed and implemented, there are both successes and failures in the logs and more recently there are more successes.


*References used to assist debugging:*

- W3 schools html validator: http://validator.w3.org

- W3 schools jigsaw css validator: http://jigsaw.w3.org

- Visual Studio intalled debuggers, and Pylint, and JSLint

- DevTools in the browser and the console

- Python documentation (Pep8), Django documentation

[Back to Index](#index)



