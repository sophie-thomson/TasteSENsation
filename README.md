# TasteSENsation

[TasteSENsation](https://tastesensation-pp4-54d01fbc1628.herokuapp.com/) is a recipe site with curated recipes for budding chefs with Special Educational Needs (SEN).

Users are invited to sign up to rate and comment on the recipes so that other visitors to the site can see which recipes are popular. They can also suggest their own recipes to be added to the cookbook recipe list for others to enjoy.

The simple, uncluttered layout and use of additional visual prompts help to make the site easy to understand and navigate with minimal distractions. This means that SEN users are more likely to be able to use the site and follow the steps unaided.

![TasteSENsation mock up on multiple devices](docs/readme-images/multi-screen-mock-up.png)

## Features

### Site Wide

***Favicon***
- A favicon with a bold letter 'T' for TasteSENsation so it is easily identifiable among multiple tabs.

![Screenshot of TasteSENsation favicon](docs/readme-images/tastesensation-favicon.png)

***Nav Bar***
- Navigation bar with clear brand heading for TasteSENsation. 
- SEN section of the brand title has different font weight and scale to stand out and reinforce message that this is a recipe site for people with Special Educational Needs (SEN). 
- Includes links for easy navigation around the site. Only links that are accordant with user role and authentication are displayed for better user experience.
- Fully responsive with navigation links collapsable into a burger 'Menu' icon on smaller devices to keep layout clean and uncluttered.
- Includes note to display log in status and username to the user at all times.

![Screenshot of TasteSENsation nav bar on small device](docs/readme-images/nav-bar-small-device.png)

![Screenshot of TasteSENsation nav bar on larger devices](docs/readme-images/nav-bar-tablet.png)

![Screenshot of log in feedback message if not logged in](docs/readme-images/not-logged-in.png)
![Screenshot of log in feedback message if logged in](docs/readme-images/logged-in-as.png)

***Footer***
- Footer with dark background to frame bottom of html page.
- Includes information on the site designer and links to social media profiles.
- Links open in a new tab for better UK and include aria tags for better accessibility.
- Responsive format to look good on all devices.

![Screenshot of footer](docs/readme-images/footer.png)

***Alert Messages***
- Messages are displayed over the top of the screen to feedback confirmation to the user of certain actions throughout the site.
- Successful confirmation messages are displayed in green to highlight success of the action and provide useful feedback.
- Error messages are displayed in red to highlight that there is something wrong and attention or alternative action is required.
- JavaScript is used to make the messages automatically disappear after 5 seconds for better user experience.
- User can click on 'x' to close the message more quickly if they prefer.

![Screenshot of example successful confirmation message](docs/readme-images/signed-out-message.png)
![Screenshot of example error message](docs/readme-images/not-authenticated-suggest-recipe-error-message.png)


### Recipes Page

***Filter by Rating***
- The user is able to filter the list of recipes so that they can more quickly access recipes with a particular rating such as those that others have enjoyed the most.
- The filter by rating form has the same appearance as the nav bar so that it blends in and appears to be a seamless extension of the nav bar.
- The list of filtered results is displayed with 6 recipes per page. If there are lots of recipes, the filtered recipes continue across multiple pages.
- It is possible for the user to filter the recipes by:
  - 1 star
  - 2 stars
  - 3 stars
  - 4 stars
  - 5 stars
  - Unrated recipes
  - All Recipes

![Screenshot of filter by rating feature and banner text](docs/readme-images/filter-by-rating-and-banner.png)

***Banner paragraph***
- Lead paragraph to explain that the recipes displayed in TasteSENsation have been chosen specifically with SEN users in mind.
- Call to action text to highlight features only available to registered users and prompt casual users to sign up and log in.
- Visually clear and simple layout to ensure clarity and keep distrations to a minimum.

![Screenshot of recipe list with 6 recipe cards](docs/readme-images/recipe-list.png)

***Recipe List***
- Initially all published recipes are displayed, with each recipe featured in a 'recipe card' including:

   - The recipe title (name of the dish). Colour changes to highlight selection and title links to the full recipe details.
   - A recipe image (this is the 'star of the show' and the main focal point for each card). Also links to the full recipe details so user can select either the title or the image to see the full recipe.
   - A 'You will use:' display of icons to represent the different equipment that the recipe requires. This enables users to quickly identify recipes that may not be suitable for SEN ability levels. For example, users may want to look at recipes which include no chopping or hob use.
   - An average rating for the recipe represented by a visual representation of 5 star icons (an aria-label is used to ensure that the average rating is accessible if the user uses a screen reader).
   - The username of the recipe owner (the person who submitted the recipe).

![Screenshot of responsive recipe list on tablet](docs/readme-images/recipe-list-responsive-tablet.png)

***Pagination***
- The recipe cards are displayed with 6 recipes per page to help manage the flow of information for SEN users who may get easily overwhelmed or distracted.
- Using 6 recipe cards also enables more responsive display for the optimum number of cards to be displayed using the grid structure on different devices (rows of 3 cards each on larger screens, 2 cards on tablets and 1 card on small devices). 
- Navigation buttons at the bottom of the page enable the user to view more recipes or go back to previous recipes.
- The page navigation buttons are only visible if there are further pages to view, or if there is a previous page to view.

![Screenshot of page navigation button](docs/readme-images/page-navigation-button.png)

### Full Recipe Details Page

***Recipe Title***
- Large clear heading at the top of the page to confirm the name of the dish.

***Recipe Image***
- The same hero image used for the recipe card in the recipe list for continuity and to confirm the user has selected the right recipe.
- The image size and format type is controlled at the point of creation using Cloudinary functionality so all recipes submitted through the suggest recipe form will feature same sized WEBP image for the hero image.
- Fully responsive image to ensure it looks good on different devices.

![Screenshot of full recipe details page](docs/readme-images/recipe-details-page.png)

***Equipment (You will use:)***
- An equipment list using emoji icon to represent the main items of equipment or skills that will be required for making this recipe.
- The icons enable users to quickly identify recipes that may not be suitable for SEN user abilities or skill level.
- Equipment icons are further explained with the use of figure captions on medium and larger devices. This also ensures that the icons are announced to users who use a screen reader.
- Enables the user to source the equipment that they may need such as a mixing bowl, whisk, colander or chopping board.

***Ingredients (You will need:)***
- A simple list of all ingredients and measurements that are required for making the recipe.
- Located high up on the page alongside the image so that users can source and prepare their ingredients before starting the recipe.

***Instructions***
- A standrad line of text for all recipes to remind the user to wash their hands before starting the recipe.
- A step by step ordered list of instructions clearly separated by a horizontal rule to help SEN users to keep track of the step that they are following.
- A checkbox that can be checked off by the user when each step is completed. Further enables the SEN user to maintain focus and keep track of the step that they are on.

![Screenshot of full recipe details feedback section](docs/readme-images/recipe-detail-feedback-section.png)

***Feedback Section***
- A feedback section for the recipe to enable users to see other people's comments and provide their own feedback.
- Access to the features in this section is controlled through user authentication.
 - **Rate This Recipe** - Registered users are able to provide a star rating for a recipe as long as it was not submitted by themselves. This prevents users from rating their own recipes higher than everyone else's. Casual Users are not able to rate a recipe.
 - **Comments** - Displays all approved comments for this recipe for all users to view. Registered Users are also able to view, edit and delete their own comments that are awaiting approval.
- **Leave a Comment** - Registered Users are able to write and submit their own comments using a simple form. Casual Users are not able to submit a comment.

![Screenshot of rating form with no previous rating](docs/readme-images/first-rating-mobile.png)
![Screenshot of edit rating section on mobile](docs/readme-images/edit-rating-mobile.png)

### Suggest Recipe Page and Edit Recipe Page

***Suggest Recipe Form***
- Form created from Recipe database model so that new recipes can be submitted by registered users.
- Once submitted, the user receives a successful submission confirmation message and the recipe is added to the recipe database model to be reviewed by the Superuser for approval.
- User authentication prevents a recipe from being submitted successfully if they are not a registered user and logged in. In this case, an error message notifies the user that they must be logged in to submit a recipe.
- Form includes:
    - Title (Name of dish)
    - Original recipe link (if recipe adapted from a recipe on another site)
    - Featured image field for user to upload a photo of the recipe. This field uses Cloudinary functionality to standardise the image size and set the image format to WEBP.
    - Ingredients section pre-populated with list items 1, 2 and 3 to make it easier for the registered user to edit and add items in the correct list format.
    - Instructions section pre-populated with example steps to update using html code to style in same way as recipes on the site (also adds attributes and aria label to checkbox for validation).
    - Equipment checkboxes to select which key items of equipment and skills will be used when maing this recipe.

***Edit Recipe Form***
- The same recipe form is used to edit a recipe.
- The form is pre-populated with the existing content and the existing recipe image is included so that the user can either select the same one or change it for another one.
- The edit recipe page is only 


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


## Design

### UX Design

- Average Rating
- Responsiveness
- 

### CRUD Functionality


### Agile Methodology

***Kanban Board***

***MoSCoW***

***Story Points***

***Sprints***

### Design Process

***Wireframes***

***Models***

## Technologies
- Bootstrap 5
- Django
- JavaScript
- HTML
- CSS
- Python

## Testing

***Bugs***

## Validation

## Deployment

## References















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


