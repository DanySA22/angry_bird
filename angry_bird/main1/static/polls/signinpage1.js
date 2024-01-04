const token = localStorage.getItem('userToken');
if (token) {
   axios.defaults.headers.common['Authorization'] = 'Token ${token}';
}

// Local storage provides a way to store data in the browser that persists even 
// after the browser is closed and reopened.  Every request made with Axios throughout your application will use these defaults header

document.getElementById('Log1').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    const url =  '/game/log_in/';
    axios.post(url, data)
        .then(response => {
            console.log('Signup successful:', response.data);
        
            const userToken = response.data.token;
            localStorage.setItem('token', userToken);
            axios.defaults.headers.common['Authorization'] = 'Token ${userToken}';
            redirectToGame();
        })
        .catch(error => {
            console.error('Signup error:', error);
            
        });
});

function redirectToGame() {
    window.location.href = '/user_game/easy/'; 
    
}

