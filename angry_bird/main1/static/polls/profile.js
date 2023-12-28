
//RELATED TO THE IMAGE PROFILE

function image_on_profile() {
    let user_image = document.getElementsByTagName('img');
    const userID ='loggedInUserID';
    const url =  'http://127.0.0.1:8000/game/profile/image/<pk>';
    axios.get(url)
    .then(response => {
        const image_profile = response.data.profile_image; 
        document.getElementById('profile2').src = image_profile;
    })
    .catch(error => {
        console.error('Error fetching user image:', error);
        // Handle errors appropriately
    });

}

// document.getElementById('profile2').addEventListener('click', function postimage_on_profile(event) {
      
// }
function checkAuthentication() {
    // This is a placeholder; replace with actual authentication check
    // For example, checking if a user token exists in local storage
    const isAuthenticated = localStorage.getItem('userToken') !== null;
    return isAuthenticated;
}

// Call the function on page load if user is authenticated
document.addEventListener('DOMContentLoaded', () => {
    if (checkAuthentication()) {
        image_on_profile();
    } //If the user is authenticated, it then calls image() to fetch and display the user's image.
});




//RELATED TO THE SCORE

document.addEventListener("DOMContentLoaded", function () {
    const customerScoresElement = document.getElementById('puntuation');

    // Make an Axios GET request to your DRF endpoint
    axios.get('http://127.0.0.1:8000/game/profile/score/<pk>/')
        .then(response => {
            // Handle the response data
            const customerScores = response.data;

            // Update the HTML element with the received data
            customerScoresElement.textContent = JSON.stringify(customerScores, null, 2);
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
});



/*   
customerScoresElement.textContent = JSON.stringify(customerScores, null, 2);
        })

    This line updates the textContent 
    of the previously selected HTML element with the JSON 
    representation of the customerScores. JSON.stringify is 
    used to convert the JavaScript object into a string with f
    ormatted JSON, making it readable. The parameters null
     and 2 are used for formatting purposes (they specify no 
        custom replacer function and 2 spaces for indentation,
         respectively).        
*/


// RELATED TO THE RATING FORM

document.getElementById('rating_form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    const url =  'http://127.0.0.1:8000/game/profile/rating/<pk>';
    axios.post(url, data)
        .then(response => {
            console.log('Signup successful:', response.data);
            // Handle successful signup (e.g., redirect to login page)
        })
        .catch(error => {
            console.error('Signup error:', error);
            // Handle errors (e.g., display error message to user)
        });
});


//RELATED TO THE PROFILE FORM

document.getElementById('profile_form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    const url =  'http://127.0.0.1:8000/game/profile/form/<pk>';
    axios.post(url, data)
        .then(response => {
            console.log('Signup successful:', response.data);
            // Handle successful signup (e.g., redirect to login page)
        })
        .catch(error => {
            console.error('Signup error:', error);
            // Handle errors (e.g., display error message to user)
        });
});