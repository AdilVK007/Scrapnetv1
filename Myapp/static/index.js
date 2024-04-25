// index.js
let passwordsMatching = false;
let isConfirmPasswordDirty = false;

const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirmPassword');
const errorMessage = document.getElementById('errorMessage');

confirmPassword.addEventListener('keyup', () => {
    isConfirmPasswordDirty = true;
    if (password.value === confirmPassword.value) {
        passwordsMatching = true;
        // Hide the error message
        errorMessage.classList.add('hide-error');
    } else {
        passwordsMatching = false;
        // Show the error message
        errorMessage.classList.remove('hide-error');
    }
});

// Additional form validation logic for your specific form
// ...
/**
 * Created by ADIL HUB on 4/25/2024.
 */
