const token = localStorage.getItem('token');
console.log("Retrieved token:", token);
if (token) {
    axios.defaults.headers.common['Authorization'] = `Token ${token}`;
}

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
            alert('Rating updated')
        })
        .catch(error => {
            console.error('Signup error:', error);
            
        });
});


//RELATED TO THE PROFILE FORM

document.addEventListener("DOMContentLoaded", function () {
    const profileForm = document.getElementById('profile_form');

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
            alert('Profile updated')
        })
        .catch(error => {
            console.error('Update error:', error);
        });
});