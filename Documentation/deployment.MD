| 1. Sign Up to Heroku or Sign in                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2. Create a new App on Heroku                                                                                                                                                                   |
| 3. Go to ElephantSQL and sign up or sign in                                                                                                                                                     |
| 4. Create a new database and Sign in                                                                                                                                                            |
| 5. Then go to AWS Bucket Storag, and Join up or sign in                                                                                                                                         |
| 5. Go to Heroku and tLhe Databse                                                                                                                                                                |
| 6. In the dev terminal instaa                                                                                                                                                                   |
| 7. When in Elephantsql                                                                                                                                                                          |
| 8. In elephant sql check Browser and run SQL Query , you should see your new Superuser                                                                                                          |
| 9. Add to your settings file: ACCOUNT_EMAIL_VERIFCATION = 'noneE'                                                                                                                               |
| 10. In AWS selecte ACLs and create your bucket policy.                                                                                                                                          |
| 11. Add ACLs enabled and Bucket Preferred owner                                                                                                                                                 |
| 12. On the properties tab, static website hosting scroll down to the permissions tab                                                                                                            |
| 13. Paste the CORS configuration into the Cross-origin-resource-sharing(CORS) setion                                                                                                            |
| 14. Access the Access Control List and click and edit, to enable the Everyone getting  public access to List the content                                                                        |
| 15. Then create a user group, and a user group policy which you will need to attach to the User Group (select permission dropdown)                                                                  |
| Connect to Django                                                                                                                                                                               |
| Install boto3 and Django storages in and django storages via python manage in the terminal                                                                                                      |
| Add storages as an installed app in django                                                                                                                                                      |
| Then add and if statement: if "USE_AWS in the environment if there is then define the AWS_STORAGE_BUCKET_NAME.                                                                                  |
| AWS_S3_REGION_NAME and our acess key, and secret access key we need to get from the environment. - Keep these secret, only add them to Heroku config Vars                                       |
| Then go to AWS and create a media storage folder, grant the public read access only                                                                                                             |
| Upload your Product images to the newly created media folder.                                                                                                                                   |
| Then click grant public read access to those Objects.                                                                                                                                           |
| Confirm the superuser on the Postgresdatabase. Do that in the django admin. You will need to use the email confirmation link to do this,                                                        |
| get this link from the Heroku logs.                                                                                                                                                             |
| Then go to Stripe to get the Stripe Keys.                                                                                                                                                       |
| Once you 've got them, go back to heroku and add them as config vars (found in settins)                                                                                                         |
| We need to create a new webhook  as the one created is used for the gitpod app,                                                                                                                 |
| Go to the developers menu add new webhook and a new end point for it /checkout/SH then select all the events to receive. And add the endpoint.                                                  |
| These variables need to match what is in your settings.py file                                                                                                                                  |
| Ensure you have your secret keys hidden and your environ file is set to be ignored in gitignore file.                                                                                           |
| Push your updated code to github.                                                                                                                                                               |
| If you have already connected your gitub to heroku and its set to automatically deploy, then all you have to do is push it and heroku will receive the update and rebuild the app and start it. |
| Heroku will direct the files on Github and run them like a web serter. But  you need to eploy to update t                                                                                       |
| When you have pushed the new committed git then click app to view the app. You can also view the logs to catch any errors.                                                                      |
