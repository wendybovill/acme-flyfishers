## Steps to Deployment                                                                                                                                             

|    |                                                                                                                                                                                                 |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    |                                                                                                                                                                                                 |
| 1  | Sign Up to Heroku or Sign in                                                                                                                                                                    |
| 2  | Create a new App on Heroku                                                                                                                                                                      |
| 3  | Go to ElephantSQL and sign up or sign in                                                                                                                                                        |
| 4  | Create a new database and Sign in                                                                                                                                                               |
| 5  | Then go to AWS Bucket Storage, and Join up or sign in                                                                                                                                           |
| 6  |  Go to Heroku and  in he Databse create a Superuser                                                                                                                                             |
| 7  |  In the dev terminal install heroku                                                                                                                                                             |
| 8  | When in Elephantsql                                                                                                                                                                             |
| 9  | In elephant sql check Browser and run SQL Query , you should see your new Superuser                                                                                                             |
| 10 | Add to your settings file: ACCOUNT_EMAIL_VERIFCATION = 'noneE'                                                                                                                                  |
| 11 | In AWS selecte ACLs and create your bucket policy.                                                                                                                                              |
| 12 | Add ACLs enabled and Bucket Preferred owner                                                                                                                                                     |
| 13 |  On the properties tab, static website hosting scroll down to the permissions tab                                                                                                               |
| 14 | Paste the CORS configuration into the Cross-origin-resource-sharing(CORS) setion                                                                                                                |
| 15 | Access the Access Control List and click and edit, to enable the Everyone getting  public access to List the content                                                                            |
| 16 | Then create a user group, and a user group policy which you will need to attach to the User Group (select permission dropdown)                                                                  |
| 17 | Connect to Django                                                                                                                                                                               |
| 18 | Install boto3 and Django storages in and django storages via python manage in the terminal                                                                                                      |
| 19 | Add storages as an installed app in django                                                                                                                                                      |
| 20 | Then add and if statement: if "USE_AWS in the environment if there is then define the AWS_STORAGE_BUCKET_NAME.                                                                                  |
| 21 | AWS_S3_REGION_NAME and our acess key, and secret access key we need to get from the environment. - Keep these secret, only add them to Heroku config Vars                                       |
| 22 | Then go to AWS and create a media storage folder, grant the public read access only                                                                                                             |
| 23 | Upload your Product images to the newly created media folder.                                                                                                                                   |
| 24 | Then click grant public read access to those Objects.                                                                                                                                           |
| 25 | Confirm the superuser on the Postgresdatabase. Do that in the django admin. You will need to use the email confirmation link to do this,                                                        |
|    | get this link from the Heroku logs.                                                                                                                                                             |
| 26 | Then go to Stripe to get the Stripe Keys.                                                                                                                                                       |
| 27 | Once you 've got them, go back to heroku and add them as config vars (found in settins)                                                                                                         |
| 28 | We need to create a new webhook  as the one created is used for the gitpod app,                                                                                                                 |
| 29 | Go to the developers menu add new webhook and a new end point for it /checkout/SH then select all the events to receive. And add the endpoint.                                                  |
| 30 | These variables need to match what is in your settings.py file                                                                                                                                  |
| 31 | Ensure you have your secret keys hidden and your environ file is set to be ignored in gitignore file.                                                                                           |
| 32 | Push your updated code to github.                                                                                                                                                               |
| 33 | If you have already connected your gitub to heroku and its set to automatically deploy, then all you have to do is push it and heroku will receive the update and rebuild the app and start it. |
| 34 | Heroku will direct the files on Github and run them like a web serter. But  you need to eploy to update the github to the latest version so that Heroku can deply it                            |
| 35 | When you have pushed the new committed git then click app to view the app. You can also view the logs to catch any errors.                                                                      |
|    |                                                                                                                                                                                                 |
|    | Make sure you have turned DEBUG off by setting it to False in you Env file but especially in you Heroku Config Vars in Settings                                                                 |
