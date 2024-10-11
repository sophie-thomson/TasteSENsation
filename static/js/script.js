console.log("Script loaded successfully");
const ratingForm = document.getElementById("rating-form");
const editRatingBtn = document.getElementById("edit-rating-btn");


/** Removes the .hidden class from rating form so it will display */
function show_rating_form() {
 
    ratingForm.classList.remove("hidden");

    hide_rating_button()
    
}
/** Adds the .hidden class to Edit Rating button so it is hidden */
function hide_rating_button() {
    
    editRatingBtn.classList.add("hidden");
}


console.log("This is loading");
document.addEventListener('DOMContentLoaded', function () {
    // Set a timeout for each alert to fade out after 5 seconds (5000 ms)
    let alerts = document.querySelectorAll('.alert');
    console.log(alerts);

    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.classList.add('fade');
            setTimeout(function() {
                alert.style.display = 'none'; // Remove the alert after fade out
            }, 500); // Matches the Bootstrap fade transition duration
        }, 5000); // Time to display the message before fade out (5000 ms = 5 seconds)
    });
});