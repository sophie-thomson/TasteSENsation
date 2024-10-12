const ratingForm = document.getElementById("rating-form");
const editRatingBtn = document.getElementById("edit-rating-btn");


/** 
 * Initializes display functionality for the rating form.
 * 
 * Removes the .hidden class from rating form so it will display 
 */
function show_rating_form() {
 
    ratingForm.classList.remove("hidden");

    hide_rating_button();
    
}


/**
* Initializes hide functionality for the edit rating button.
* 
* Adds the .hidden class to the button so it is hidden
*/
function hide_rating_button() {
    
    editRatingBtn.classList.add("hidden");
}


/**
* Adds an event listener to any message with .alert class.
* 
* Initiates setTimeout() function for alert messages with .alert class
* Adds .fade class to alert message and sets display to 'none' after
* 5000ms (5 seconds).
*/
document.addEventListener('DOMContentLoaded', function () {
    
    let alerts = document.querySelectorAll('.alert');

    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.classList.add('fade');
            setTimeout(function() {
                alert.style.display = 'none';
            }, 500);
        }, 5000);
    });
});