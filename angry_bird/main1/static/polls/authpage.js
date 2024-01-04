document.getElementById('Auth1').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    const url =  '/game/sign_up/';
    axios.post(url, data)
        .then(response => {
            console.log('Signup successful:', response.data);
            redirectToLogin();
        })
        .catch(error => {
            console.error('Signup error:', error);
        });
});

function redirectToLogin() {
    window.location.href = '/sign_up_game/'; 
}
