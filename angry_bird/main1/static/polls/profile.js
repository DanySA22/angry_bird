const token = localStorage.getItem('token');
console.log("Retrieved token:", token);
if (token) {
    axios.defaults.headers.common['Authorization'] = `Token ${token}`;
}


//RELATED TO THE IMAGE PROFILE

// function image_on_profile() {
//     let user_image = document.getElementsByTagName('img');
//     const userID ='loggedInUserID';
//     const url =  'http://127.0.0.1:8000/game/profile/image/<pk>';
//     axios.get(url
        
//     )
//     .then(response => {
//         const image_profile = response.data.profile_image; 
//         document.getElementById('profile2').src = image_profile;
//     })
//     .catch(error => {
//         console.error('Error fetching user image:', error);
//         // Handle errors appropriately
//     });

// }

// // document.getElementById('profile2').addEventListener('click', function postimage_on_profile(event) {
      
// // }
// function checkAuthentication() {
//     // This is a placeholder; replace with actual authentication check
//     // For example, checking if a user token exists in local storage
//     const isAuthenticated = localStorage.getItem('userToken') !== null;
//     return isAuthenticated;
// }

// // Call the function on page load if user is authenticated
// document.addEventListener('DOMContentLoaded', () => {
//     if (checkAuthentication()) {
//         image_on_profile();
//     } //If the user is authenticated, it then calls image() to fetch and display the user's image.
// });




//RELATED TO THE SCORE

document.addEventListener("DOMContentLoaded", function () {
    const customerScoresElement = document.getElementById('puntuation');

    // Make an Axios GET request to your DRF endpoint
    axios.get('http://127.0.0.1:8000/game/profile/score/')
        .then(response => {
            // Handle the response data
            const customerScores = response.data.score;

            // Update the HTML element with the received data
            customerScoresElement.textContent = customerScores;
            console.log(response)
            
            
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
});



// RELATED TO THE RATING FORM

document.getElementById('rating_form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(event.target);
    let dataToSend = {};
    // Check if the checkbox is checked and add its value to dataToSend
    if (formData.get('rating') === '5') {
        dataToSend = { rating: 5 };
    }
    if (formData.get('rating') === '4') {
        dataToSend = { rating: 4 };
    }
    if (formData.get('rating') === '3') {
        dataToSend = { rating: 3 };
    }
    if (formData.get('rating') === '2') {
        dataToSend = { rating: 2 };
    }
    if (formData.get('rating') === '1') {
        dataToSend = { rating: 1 };
    }
    const url =  'http://127.0.0.1:8000/game/profile/rating/';
    axios.put(url, dataToSend)
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

document.addEventListener("DOMContentLoaded", function () {
    const profileForm = document.getElementById('profile_form');

    // Make an Axios GET request to your DRF endpoint
    axios.get('http://127.0.0.1:8000/game/profile/form/')
        .then(response => {
            const userData = response.data
            document.getElementById('username').value = userData.username || '';
            document.getElementById('first_name').value = userData.first_name || '';
            document.getElementById('last_name').value = userData.last_name || '';
            document.getElementById('email').value = userData.email || '';
            document.getElementById('password').value = userData.password || '';
            console.log(response)
          
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
});

document.getElementById('profile_form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    const url =  'http://127.0.0.1:8000/game/profile/form/';
    axios.put(url, data)
        .then(response => {
            console.log('Update successful:', response);
            // Handle successful signup (e.g., redirect to login page)
        })
        .catch(error => {
            console.error('Update error:', error);
            // Handle errors (e.g., display error message to user)
        });
});