localStorage.setItem('token', userToken);
if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}
// Local storage provides a way to store data in the browser that persists even 
// after the browser is closed and reopened.  Every request made with Axios throughout your application will use these defaults header

document.getElementById('Log1').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    const url =  'http://127.0.0.1:8000/game/log_in/';
    axios.post(url, data)
        .then(response => {
            console.log('Signup successful:', response.data);
            // Handle successful signup (e.g., redirect to login page)
            const userToken = response.data.token;
            axios.defaults.headers.common['Authorization'] = `Bearer ${userToken}`;
        })
        .catch(error => {
            console.error('Signup error:', error);
            // Handle errors (e.g., display error message to user)
        });
});


// Certainly! The line const formData = new FormData(event.target); in JavaScript is quite powerful and serves a specific purpose in the context of handling forms. Let's break it down:

// Understanding the Components
// FormData:

// FormData is a JavaScript object that provides a way to easily construct a set of key/value pairs representing form fields and their values.
// It's used to simplify the process of collecting and sending form data in web applications.
// event.target:

// In the context of an event listener, event is the object representing the event that has occurred.
// event.target refers to the element that triggered the event. In the case of a form submission event, event.target is the form that was submitted.
// Therefore, event.target in a submit event handler will refer to the form element that the event is attached to.
// How It Works Together
// When the form is submitted, the event listener triggers, and the submit event object is passed to the function.
// new FormData(event.target) creates a new FormData object based on the form that triggered the submit event.
// This FormData object automatically captures all the form fields (<input>, <select>, <textarea>, etc.) within the submitted form.
// Each form field is added to the FormData object as a key/value pair, where the key is the name attribute of the field, and the value is the current value entered/selected in that field.
// Practical Use
// The FormData object can be directly used with AJAX requests (like with Axios) to send form data to a server.