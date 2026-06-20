// Fade out flash messages automatically
document.addEventListener('DOMContentLoaded', () => {
    const alerts = document.querySelectorAll('.alert');
    if (alerts.length > 0) {
        setTimeout(() => {
            alerts.forEach(alert => {
                alert.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
                alert.style.opacity = '0';
                alert.style.transform = 'translateY(-10px)';
                setTimeout(() => alert.remove(), 500);
            });
        }, 4000); // Wait 4 seconds before fading
    }
});

// Real-time validation for marks
function validateForm() {
    let inputs = document.querySelectorAll('input[type="number"]');
    for (let i = 0; i < inputs.length; i++) {
        // Skip 'age' field for the 0-100 check
        if (inputs[i].name === 'age' || inputs[i].name === 'student_id') continue;

        let val = parseFloat(inputs[i].value);
        if (val < 0 || val > 100) {
            inputs[i].style.borderColor = '#e53e3e';
            inputs[i].style.boxShadow = '0 0 0 3px rgba(229, 62, 62, 0.2)';
            alert("Error: Marks must be between 0 and 100 for " + inputs[i].name.toUpperCase());
            return false;
        } else {
            inputs[i].style.borderColor = '#e2e8f0';
            inputs[i].style.boxShadow = 'none';
        }
    }
    return true;
}