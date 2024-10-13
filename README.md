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
- Visually clear and simple layout to ensure clarity and keep distractions to a minimum.

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

![Screenshot of responsive suggest recipe form on mobile](docs/readme-images/suggest-recipe-mobile-top.png)
![Screenshot of responsive suggest recipe form on mobile](docs/readme-images/suggest-recipe-mobile.png)

***Edit Recipe Form***
- The same recipe form is used to edit a recipe.
- The form is pre-populated with the existing content and the existing recipe image is included so that the user can either select the same one or change it for another one.
- User authentication prevents a recipe from being edited successfully if they are not the recipe owner and logged in. In this case, an error message notifies the user that they must be logged in to edit a recipe.

![Screenshot of edit recipe form and error message](docs/readme-images/edit-recipe-error-message.png)

### Delete Recipe
- JavaScript triggers a delete recipe modal to display if the recipe owner clicks on the 'Delete Recipe' button.
- User authentication prevents the Delete Recipe button from displaying if the person logged in is not the recipe owner.
- User is reminded that this action cannot be undone and that the recipe will lose all comments and ratings once deleted.
- User requested to click on 'Delete' again to confirm action.

![Screenshot of delete recipe modal](docs/readme-images/delete-recipe-modal.png)

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

### Existing Features
- Responsive pages with effective styling to look good on different sized devices.
- Robust user authentication ensures that users can only access areas and functionality in accordance with their user role. 
- All form fields are correctly assigned with required or blank=True attributes and clear error messages are displayed to the user if field validation fails.
- This program is deployed and run on Heroku using the CI gitpod template.
- CRUD functionality (Create, Read, Update, Delete) is evident throughout the project. Refer to the CRUD functionality section for further details.

### Future Features

To expand on this project, there are a number of features that could be added to enhance user experience and functionality:
- A user profile page for registered users to track the recipes they have cooked and identify recipes that they would like to try.
- The profile page could include a list of all the comments they have left on other people's recipes.
- Registered users could tag a recipe as a 'favourite' and list these in their profile page.
- Improved functionality for SEN users could include a visual image for each step of the instructions in the recipe detail page. This would further break down each recipe into manageable steps and help the user to understand what is required of them.
- A Further Resources page could provide links to original recipes from other SEN focused cookery / recipe sites and include other useful information and resources.

## Design

### UX Design

Along with more usual UX considerations, TasteSENsation has been designed with SEN users in mind.

Design considerations and features include:
- Simple, uncluttered layout to keep distractions to a minimum and help maintain focus.
- Clear text with good contrast for easy reading.
- Consistent styling with clear instruction for all links and buttons across the site.
- Aria labels used wherever possible to improve accessability for screen reader users.
- Use of visual prompts alongside text. For example: The use of equipment icons as well as figure captions to provide further clarity for SEN users.
- Star icons for average rating and user rating form to provide clear visual understanding, along with aria labels for readers.
- User authentication used to ensure that only links and features that are appropriate for the particular user role are displayed to minimise confusion.
- Clear messaging throughout the site using green success message and red error message styling for clarity.
- Curated recipes with consistent styling throughout to ensure ease of use.
- The use of checkboxes and clear definition between steps to help SEN users to keep track of which step they are on in the recipe instructions.

### CRUD Functionality
Full CRUD (Create, Read, Update, Delete) functionality is evident throughout the site for both Registered Users and Admin SuperUsers.

![Screenshot of CRUD functionality as a recipe owner and commenter](docs/readme-images/CRUD-functionality-recipe-owner.png)

- Registered Users can:
    - Create a user rating for other people's published recipes
    - Update their own rating for other people's recipes
    - Create new comments for their own and other people's recipes within the Full Recipe Detail page.
    - Read all approved comments for all recipes, and read their own unnaproved comments awaiting approval.
    - Update their own comments (whether approved or not).
    - Delete their own comments (whether approved or not).
    - Create a new recipe to submit for approval by admin to be added to the site
    - Read all approved (published) recipes.
    - Update their own recipe as the recipe 'owner' and re-submit for approval
    - Delete their own recipe as the recipe 'owner'

- Admin SuperUsers can:
    - Create, Read, Update and Delete all comments from all users via the admin dashboard
    - Create, Read, Update and Delete all recipes from all users via the admin dashboard


### Agile Methodology

***Trello Board***

![Screenshot of initial TasteSENsation Trello Board](docs/readme-images/TasteSENsation-trello-board.png)

- View the live [Trello TasteSENsation Board](https://trello.com/b/vH7TCYBx/tastesensation-your-one-stop-directory-of-user-friendly-sen-accessible-recipes-and-kitchen-skills-training)
- I first created a Trello Board As a starting point for gathering information and mapping out the general idea for TasteSENsation.
- This included the following:
  - TO DO list with a variety of items some of which became EPICS and User Stories later on
  - General Applications to be included in the django project
  - CRUD functionality plans to ensure that this aspect of teh assessment criteria is met
  - Initial UX Design considerations with SEN users in mind
  - Possible Filtering Options to improve the functionality and flexibility for users
  - Source Sites of other SEN focused recipe sites and youtube videos
  - Other Resources list of tutorials, links, Stack Overflow discussions, Django documentation and many others that I used along the way to help with building the project and resolving issues.

***Kanban Board***

![Screenshot of GitHub Kanban Board](docs/readme-images/tastesensation-github-kanban-board.png)

- View the live [TasteSENsation Project Kanban Board](https://github.com/users/sophie-thomson/projects/3)
- Following the principles outlined in the Code Institute Agile Working units, I created a GitHub Kanban Board and using Project Issues, Milestones and Labels I mapped out the TasteSENsation project into:
   - EPICS (Overarching blocks of work broken down into USER STORY Issues)
   - To Do (USER STORY issues with acceptance criteria and tasks)
   - In Progress (USER STORY Issues in progress during each Milestone or 'Sprint')
   - Completed (USER STORY Issues that have been completed)
   - BUGS (BUG issues that define a particular issue encountered during the project and how it was resolved)

![Screenshot of GitHub EPIC issue](docs/readme-images/epic-kanban.png)

![Screenshot of GitHub USER STORY issue](docs/readme-images/user-story-kanban.png)

![Screenshot of GitHub BUG issue](docs/readme-images/bug-kanban.png)

***MoSCoW***

- Using MoSCoW Prioritisation, each USER STORY and EPIC issue in the kanban board was assigned a label:
   - **Must Have** - High priority Epics, User Stories and Tasks that MUST be included and working in the finished project in order to have a working project and address the Assessment Criteria.
   - **Should Have** - Epics, User Stories and Tasks that SHOULD be included in the project, but that won't cause the project to break and are not required in order to address the assessment criteria.
   - **Could Have** - Epics, User Stories and Tasks that COULD be included in the project, but that are more of a nice to have addition and should not be prioritised over the Must Have or Should Have issues.
   - **Won't Have** - Epics, User Stories and Tasks that WON'T be included in the project. These are issues that would have been nice to include given more time, but do not affect the usability of the project and are not required to address the assessment criteria.


***Sprints and Story Points***

![Screenshot of GitHub Milstone Sprints](docs/readme-images/milestone-sprints.png)

- Having broken down each EPIC into USER STORY issues and identified the Must Have priorities, I then split the time I had available until the submission date down into 4-day development 'Sprints' and assigned a date range to each of the Milestones. 
- Estimating that I could work an average of 6hrs per day on my project, I then broke each 'day' into two 'Story Point' blocks of 1-3hrs per block (8 Story Points per Sprint).
- Given my previous experience and my level of understanding and programming skills, I made an estimate of how many Story Point blocks it would take me to complete the tasks for each User Story.
- Arranging each User Story Issue in logical progressional order, I assigned each User Story a certain number of Story Points and a particular Milestone Sprint within which I would aim to complete that set of tasks.
- This approach kept me on track to complete all of the Must Have labelled User Stories required to complete a working project and address the assessment criteria for PP4.


### Design Process

***Wireframes***

- Initial Wireframe designs were used to plan out the layout for the Recipe List and Recipe Detail pages

![Recipe Cards Wireframe Design](docs/readme-images/recipe-cards-wireframe.png)

![Recipe Detail Wireframe Design](docs/readme-images/recipe-detail-wireframe.png)

***Models***

- The next step was to plan and devise an ERD for each of my database models and a schema to map out and understand the relationships between them. I created an ERD and model schema for the project based on all of the elements that I would like to include if I was able (this included the Should Have and Could Have User Story issues).
- As the project progressed it became apparent that would not require all of the models:
    - The 'User model' already existed within the Django framework, so did not require an additional model to be created. 
    - The functionality for the 'Suggestion Model' to create, update and delete recipes could be achieved using methods within the recipe model and views to manipulate the data.
    - Unfortunately I was not going to have time to create a User Profile page for the project at this time.

![TasteSENsation model schema](docs/readme-images/model-schema.png)

- I created an ERD for the following models:
  - Recipe Model (Used in final project)
  - Comment Model (Used in final project)
  - Rating Model (Used in final project)
  - User Model (Automatically created in Django framework)
  - Suggestion Model (Not required)
  - Profile Model (Not required)

![TasteSENsation Recipe model](docs/readme-images/recipe-model-erd.jpg)
![TasteSENsation Rating model](docs/readme-images/rating-model-erd.jpg)
![TasteSENsation Comment model](docs/readme-images/comment-model-erd.jpg)
![TasteSENsation User model](docs/readme-images/user-model-erd.jpg)
![TasteSENsation Suggestion model](docs/readme-images/suggestion-model-erd.jpg)
![TasteSENsation Profile model](docs/readme-images/profile-model-erd.jpg)

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


