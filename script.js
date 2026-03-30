function validateForm(event) {
    // Prevent default form submission
    event.preventDefault();
    
    let isValid = true;
    
    // Clear previous errors
    resetErrors();

    // 1. Validate Student Name (not empty)
    const nameInput = document.getElementById('studentName');
    const nameGroup = document.getElementById('nameGroup');
    if (nameInput.value.trim() === '') {
        nameGroup.classList.add('invalid');
        isValid = false;
    }

    // 2. Validate Email ID (proper format)
    const emailInput = document.getElementById('emailId');
    const emailGroup = document.getElementById('emailGroup');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailInput.value.trim())) {
        emailGroup.classList.add('invalid');
        isValid = false;
    }

    // 3. Validate Mobile Number (valid 10 digits only)
    const mobileInput = document.getElementById('mobileNumber');
    const mobileGroup = document.getElementById('mobileGroup');
    const mobileRegex = /^[0-9]{10}$/;
    if (!mobileRegex.test(mobileInput.value.trim())) {
        mobileGroup.classList.add('invalid');
        isValid = false;
    }

    // 4. Validate Department (should be selected)
    const deptInput = document.getElementById('department');
    const deptGroup = document.getElementById('deptGroup');
    if (deptInput.value === '') {
        deptGroup.classList.add('invalid');
        isValid = false;
    }

    // 5. Validate Gender (at least one option selected)
    const genderRadios = document.getElementsByName('gender');
    const genderGroup = document.getElementById('genderGroup');
    let genderSelected = false;
    for (let i = 0; i < genderRadios.length; i++) {
        if (genderRadios[i].checked) {
            genderSelected = true;
            break;
        }
    }
    if (!genderSelected) {
        genderGroup.classList.add('invalid');
        isValid = false;
    }

    // 6. Validate Feedback Comments (not blank, minimum 10 words)
    const commentsInput = document.getElementById('feedbackComments');
    const commentsGroup = document.getElementById('commentsGroup');
    const commentsText = commentsInput.value.trim();
    const wordCount = commentsText === "" ? 0 : commentsText.split(/\s+/).length;
    
    if (commentsText === '' || wordCount < 10) {
        commentsGroup.classList.add('invalid');
        isValid = false;
    }

    // Show success message if all validations pass
    if (isValid) {
        document.getElementById('successMessage').style.display = 'block';
        // Hide success message after 3 seconds
        setTimeout(() => {
            document.getElementById('successMessage').style.display = 'none';
            document.getElementById('feedbackForm').reset();
        }, 3000);
    }

    return isValid;
}

function resetErrors() {
    const errorGroups = document.querySelectorAll('.form-group.invalid');
    errorGroups.forEach(group => {
        group.classList.remove('invalid');
    });
}

// Clear single error when user starts typing/interacting
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('#feedbackForm input, #feedbackForm select, #feedbackForm textarea');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            // Find parent form group and remove invalid class
            let parent = this.closest('.form-group');
            if (parent) {
                parent.classList.remove('invalid');
            }
        });
    });

    // Special case for radio buttons
    const radios = document.querySelectorAll('input[type="radio"]');
    radios.forEach(radio => {
        radio.addEventListener('change', function() {
            let parent = this.closest('.form-group');
            if (parent) {
                parent.classList.remove('invalid');
            }
        });
    });
});
