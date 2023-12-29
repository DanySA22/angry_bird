const token = localStorage.getItem('token');
console.log("Retrieved token:", token);
if (token) {
    axios.defaults.headers.common['Authorization'] = `Token ${token}`;
}


document.addEventListener("DOMContentLoaded", function() {
    // URL of the logout endpoint
    const logoutUrl = 'http://127.0.0.1:8000/game/log_out/';

    axios.post(logoutUrl)
        .then(function(response) {
            // Handle successful logout
            console.log('Logout successful', response.data);

        })
        .catch(function(error) {
            // Handle any error in the logout process
            console.error('Logout error', error);
        });
});
