const deleteRecipeModal = new bootstrap.Modal(document.getElementById("deleteRecipeModal"));
const deleteRecipeButton = document.getElementById("btn-recipe-delete");
const deleteRecipeConfirm = document.getElementById("deleteRecipeConfirm");


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteRecipeButtons` collection:
* - Retrieves the associated recipe slug upon click.
* - Updates the `deleteRecipeConfirm` link's href to point to the 
* deletion endpoint for the specific recipe.
* - Displays a confirmation modal (`deleteRecipeModal`) to prompt 
* the user for confirmation before deletion.
*/
deleteRecipeButton.addEventListener("click", function() {
        let recipeSlug = deleteRecipeButton.getAttribute("data-recipe-slug");
        
        deleteRecipeConfirm.href = `/${recipeSlug}/recipe_delete/`;
        deleteRecipeModal.show();
});
