/* I am going to dedicated first 
to putt all the code related with Axios and then 
the only-client logic 

document.addEventListener("DOMContentLoaded", function () {
    const customerScoresElement = document.getElementById('puntuation');

    // Make an Axios GET request to your DRF endpoint
    axios.get('http://127.0.0.1:8000/game/game_points/3/')
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

*/