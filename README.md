# TasteSENsation

TasteSENsation is a recipe site with curated recipes for budding chefs with Special Educational Needs (SEN).

Users are invited to sign up to rate and comment on the recipes so that other visitors to the site can see which recipes are popular. They can also suggest their own recipes to be added to the cookbook recipe list for others to enjoy.

The simple, uncluttered layout and use of additional visual prompts help to make the site easy to understand and navigate with minimal distractions. This means that SEN users are more likely to be able to use the site and follow the steps unaided.

![TasteSENsation mock up on multiple devices](docs/readme-images/multi-screen-mock-up.png)

## User Authentication

Users are required to sign up and log in to access certain functionality or areas of the TasteSENsation site.

Different user roles are able to view and access different parts of the site.


***Authenticated Access and Functionality by Role***

  | **Functionality**          | **Casual User**| **Reg'd User**|  **Admin**   |
  |:---                        |      :---:     |      :---:    |    :---:     |
  |View Recipes List           |y               |y              |y             |
  |Filter Recipe List by Rating|y               |y              |y             |
  |View Recipe Details         |y               |y              |y             |
  |View Average Rating         |y               |y              |y             |
  |View Approved Comments      |y               |y              |y             |
  |View Own Unapproved Comments|-               |y              |y             |
  |View All Unapproved Comments|-               |-              |y             |
  |                            |                |               |              |
  |Add Rating                  |-               |y              |y             |
  |Edit Own Rating             |-               |y              |y             |                      
  |Edit Other's Ratings        |-               |-              |-             |                      
  |                            |                |               |              |                      
  |Add Comment                 |-               |y              |y             |                      
  |Edit Own Approved Comment   |-               |y              |y             |                      
  |Edit All Approved Comments  |-               |-              |y             |                      
  |Edit Own Unapproved Comment |-               |y              |y             |                     
  |Edit All Unapproved Comments|-               |-              |y             |                      
  |Delete Own Comment          |-               |y              |y             |                      
  |Delete All Comments         |-               |-              |y             |
  |                            |                |               |              |                          
  |Add Recipe                  |-               |y              |y             |                     
  |Edit Own Approved Recipe    |-               |y              |y             |                      
  |Edit All Approved Recipes   |-               |-              |y             |                      
  |Edit Own Unapproved Recipe  |-               |-              |y             |                      
  |Edit All Unapproved Recipes |-               |-              |y             |                      
  |Delete Own Recipe           |-               |y              |y             |                      
  |Delete All Recipes          |-               |-              |y             |
  |                            |                |               |              |    



***Casual User***

TasteSENsation recipes are intended to be accessible to all and some SEN users may not be able to easily provide the details required to register themselves.

Any visitor to the site who is not a registered user or not logged in can view the recipes list and the recipe detail pages so that they can enjoy making the recipe without having to register for the site. This includes viewing the average rating and approved comments, and filtering the recipes by the average rating.

![Screenshot of casual user nav bar](docs/readme-images/casual-user-nav-bar.png)

***Registered User***

Users are able to register for the TasteSENsation site via the Sign Up (signup.html) page which is linked in the navigation bar.
Once registered, a user can log in via the Log In (login.html) page whever they visit the site.

![Screenshot of Sign Up page](docs/readme-images/sign-up-page.png)

![Screenshot of Log In page](docs/readme-images/log-in-page.png)

Once logged in the registered user will see a note in the nav bar to confirm that they are logged as a specified user. The 'Sign Up' and 'Log In' nav links are then hidden to the user, but 'Suggest Recipe' and 'Log Out' links become visible.

![Screenshot of registered user nav bar](docs/readme-images/registered-user-nav-bar.png)

![Screenshot of Log Out page](docs/readme-images/log-out-page.png)



***Admin SuperUser***

*SuperUser login credentials are provided within the Code Institute project submission form.*

When logged in as a SuperUser, you are able to access the admin panel and create, read, update and delete any recipe or comment in the database.

Submitted comments are added to the database for approval, and any unapproved comments are visible to the user who submitted the comment, but are not visible to other users until they have been approved in the admin dashboard. 

This is to ensure that any offensive or inappropriate comments are not visible to potentially vulnerable SEN users.

Comments are approved by ticking the 'Approved' checkbox and saving the comment.

![Screenshot of Comment Approval in Admin Dashboard](docs/readme-images/admin-approve-comment.png)

![Screenshot of Comment Approval Checkbox](docs/readme-images/admin-approve-comment-checkbox.png)

When recipes are submitted via the Suggest Recipe page, these are added to the database, but are not visible in the recipe list until they have been 'Approved' in the admin dashboard. 

This is to ensure design continuity and simplicity in the curated recipes list for SEN users.

Recipes are approved by changing the 'Recipe Approved' status from Submitted to 'Approved' and saving the recipe.

![Screenshot of Recipe Approval in Admin Dashboard](docs/readme-images/admin-approve-recipe.png)

![Screenshot of Recipe Approval Dropdown](docs/readme-images/admin-approve-recipe-dropdown.png)














SAMPLE TABLE:

  | **Column 1**               |  **Column 2**  | **Column 3**  | **Column 4** |  **Column 5**      |
  |:---                        |      :---:     |      :---:    |    :---:     |        :---:       |
  |                            |                |               |              |                    |
  |                            |                |               |              |                    |
  |                            |                |               |              |                    |
  |                            |                |               |              |                    |
  |                            |                |               |              |                    |
  |                            |                |               |              |                    |
  |                            |                |               |              |                    |


