const editButtons = document.getElementsByClassName("btn-comment-edit");
const commentChoice = document.getElementById("id_suggested_comment");
const commentText = document.getElementById("id_own_comment");
const commentForm = document.getElementById("comment-form");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-comment-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


// console.log(editButton, commentText, commentForm, submitButton);
/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {    
    button.addEventListener("click", (e) => {
      // Get the comment ID from the button attribute
      let commentId = e.target.getAttribute("data-comment-id");
      // Get the values of the fields for that comment
      let suggestedComment = document.getElementById(`suggested_comment${commentId}`).innerText;
      
      let commentContent = document.getElementById(`own_comment${commentId}`).innerText;
      // Populate the fields with the current comment data
      commentChoice.value = suggestedComment;
      commentText.value = commentContent;
      console.log("Suggested Comment: ", suggestedComment);
      console.log("Own comment: ", commentContent);
      
      commentForm.setAttribute("action", `comment_edit/${commentId}`);
      submitButton.innerText = "Update Comment";
    });
}


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment-id");
        deleteConfirm.href = `comment_delete/${commentId}`;
        deleteModal.show();
    });
  }