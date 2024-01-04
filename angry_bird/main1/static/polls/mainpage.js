const token = localStorage.getItem('token');
console.log("Retrieved token:", token);
if (token) {
    axios.defaults.headers.common['Authorization'] = `Token ${token}`;
}


document.addEventListener("DOMContentLoaded", function() {
    const logoutUrl = '/game/log_out/';
    axios.post(logoutUrl)
        .then(function(response) {
            console.log('Logout successful', response.data);

        })
        .catch(function(error) {
            console.error('Logout error', error);
        });
});
