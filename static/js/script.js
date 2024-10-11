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


document.addEventListener('DOMContentLoaded', function () {
    
    let alerts = document.querySelectorAll('.alert');
    console.log(alerts);

    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.classList.add('fade');
            setTimeout(function() {
                alert.style.display = 'none';
            }, 500);
        }, 5000);
    });
});