document.getElementById('Auth1').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    const url =  'http://127.0.0.1:8000/game/sign_up/';
    axios.post(url, data)
        .then(response => {
            console.log('Signup successful:', response.data);
            // Handle successful signup (e.g., redirect to login page)
            redirectToLogin();
        })
        .catch(error => {
            console.error('Signup error:', error);
            // Handle errors (e.g., display error message to user)
        });
});

function redirectToLogin() {
    window.location.href = 'http://127.0.0.1:8000/sign_up_game/'; // Replace '/login' with the URL of your login page
}
