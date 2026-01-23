function validateForm() {
    // Get all input fields that are for numbers
    let inputs = document.querySelectorAll('input[type="number"]');
    
    for (let i = 0; i < inputs.length; i++) {
        let val = parseFloat(inputs[i].value);
        
        // Simple Check: Marks shouldn't be negative or > 100
        if (val < 0 || val > 100) {
            alert("Error: Marks must be between 0 and 100.");
            return false; // Stop form submission
        }
    }
    return true; // Allow submission
}