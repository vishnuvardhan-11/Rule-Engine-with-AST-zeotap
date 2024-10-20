document.getElementById('ruleForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the default form submission

    const department = document.getElementById('department').value;
    const age = document.getElementById('age').value;
    const ruleName = document.getElementById('ruleName').value;
    const salary = document.getElementById('salary').value;
    const experience = document.getElementById('experience').value;

    const data = {
        department: department,
        age: age,
        rule_name: ruleName,
        salary: salary,
        experience: experience
    };

    // Send data to the backend
    fetch('/save-rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseMessage').innerText = data.message;
        document.getElementById('ruleForm').reset();  // Reset the form
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('responseMessage').innerText = 'Error saving rule.';
    });
});
