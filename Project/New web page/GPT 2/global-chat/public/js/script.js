document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;

    fetch('/send-otp', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email })
    })
    .then(response => {
        if (response.ok) {
            console.log('OTP sent successfully');
            document.getElementById('otpSection').style.display = 'block';
        } else {
            console.error('Error sending OTP');
            return response.text();
        }
    })
    .catch(error => console.error('Fetch error:', error));
});
