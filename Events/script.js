document.querySelectorAll('.cta-button').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        alert('Thank you for registering for the event!'); // Simple alert for registration confirmation
    });
});
