document.getElementById('toggle-button').addEventListener('click', function() {
    const navbar = document.getElementById('navbar');
    navbar.classList.toggle('active'); // Toggle the active class
});

document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission for demo purposes
    alert('Thank you for your feedback!'); // Display thank you message
    // Here you can add code to handle form submission, e.g., sending data to a server
});
