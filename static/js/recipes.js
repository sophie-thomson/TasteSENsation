// const editButton = document.getElementById("btn-edit-recipe");


// editButton.addEventListener("click", function() {
//     let recipeId = this.getAttribute("data-id");

//     // window.location.href = `/suggest_recipe/recipe_edit/${recipeId}/`;
// });


// button.addEventListener("click", (e) => {
//     // Get the comment ID from the button attribute
//     let commentId = e.target.getAttribute("data-comment-id");
//     // Get the values of the fields for that comment
//     let suggestedComment = document.getElementById(`suggested_comment${commentId}`).innerText;
    
//     let commentContent = document.getElementById(`own_comment${commentId}`).innerText;
//     // Populate the fields with the current comment data
//     commentChoice.value = suggestedComment;
//     commentText.value = commentContent;
//     console.log("Suggested Comment: ", suggestedComment);
//     console.log("Own comment: ", commentContent);
    
//     commentForm.setAttribute("action", `comment_edit/${commentId}`);
//     submitButton.innerText = "Update Comment";
//   });

document.getElementById("btn-edit-recipe").addEventListener("click", function() {
    const recipeId = this.getAttribute("data-id");
    window.location.href = `/suggest-recipe/recipe_edit/${recipeId}/`;
});