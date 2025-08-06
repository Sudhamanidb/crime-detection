// Producing tilt effect using vanilla javascript


const officials = [
    { email: 'official1@example.com', password: 'password1' },
    { email: 'official2@example.com', password: 'password2' },
    { email: 'official3@example.com', password: 'password3' }
];

// Handle form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const official = officials.find(official => official.email === email && official.password === password);

    const errorMessage = document.getElementById('error-message');
    const successMessage = document.getElementById('success-message');

    if (official) {
        // Successful login
        errorMessage.textContent = '';  // Clear error message
        successMessage.textContent = 'Login Successful!';
    } else {
        // Login failed
        successMessage.textContent = '';  // Clear success message
        errorMessage.textContent = 'Invalid email or password!';
    }
});
