@echo off
REM Create project directory structure
mkdir global-chat
cd global-chat

mkdir public
mkdir public\css
mkdir public\js
mkdir server
mkdir server\routes
mkdir server\models

REM Create HTML file
(
echo ^<!DOCTYPE html^>
echo ^<html lang="en"^>
echo ^<head^>
echo ^    <meta charset="UTF-8"^>
echo ^    <meta name="viewport" content="width=device-width, initial-scale=1.0"^>
echo ^    <title>Global Chat</title^>
echo ^    <link rel="stylesheet" href="css/styles.css"^>
echo ^</head^>
echo ^<body^>
echo ^    <header^>
echo ^        <h1>Welcome to Global Chat</h1^>
echo ^        <p>Connect with people from around the world.</p^>
echo ^    </header^>
echo ^    <main^>
echo ^        <form id="loginForm"^>
echo ^            <input type="email" id="email" placeholder="Email" required^>
echo ^            <button type="submit">Send OTP</button^>
echo ^        </form^>
echo ^        <div id="otpSection" style="display: none;"^>
echo ^            <input type="text" id="otp" placeholder="Enter OTP" required^>
echo ^            <button id="verifyOtp">Verify OTP</button^>
echo ^        </div^>
echo ^    </main^>
echo ^    <script src="js/script.js"^>^</script^>
echo ^</body^>
echo ^</html^>
) > public\index.html

REM Create CSS file
(
echo body {
echo     font-family: Arial, sans-serif;
echo     background-color: #f0f0f0;
echo     color: #333;
echo }
echo header {
echo     text-align: center;
echo     margin-top: 50px;
echo }
echo main {
echo     display: flex;
echo     justify-content: center;
echo     align-items: center;
echo     height: 80vh;
echo     flex-direction: column;
echo }
echo form, #otpSection {
echo     margin-top: 20px;
echo }
echo input {
echo     padding: 10px;
echo     margin: 5px;
echo     width: 200px;
echo }
echo button {
echo     padding: 10px;
echo     margin: 5px;
echo     cursor: pointer;
echo }
) > public\css\styles.css

REM Create JavaScript file
(
echo document.getElementById('loginForm').addEventListener('submit', function(event) {
echo     event.preventDefault();
echo     const email = document.getElementById('email').value;
echo     fetch('/send-otp', {
echo         method: 'POST',
echo         headers: {
echo             'Content-Type': 'application/json'
echo         },
echo         body: JSON.stringify({ email })
echo     }).then(response => {
echo         if (response.ok) {
echo             document.getElementById('otpSection').style.display = 'block';
echo         }
echo     });
echo });
echo document.getElementById('verifyOtp').addEventListener('click', function() {
echo     const otp = document.getElementById('otp').value;
echo     // Handle OTP verification
echo });
) > public\js\script.js

REM Create server files
(
echo const express = require('express'); > server\server.js
echo const bodyParser = require('body-parser'); >> server\server.js
echo const mongoose = require('mongoose'); >> server\server.js
echo const nodemailer = require('nodemailer'); >> server\server.js
echo const path = require('path'); >> server\server.js
echo const app = express(); >> server\server.js
echo const api = require('./routes/api'); >> server\server.js
echo const socketIo = require('socket.io'); >> server\server.js
echo app.use(bodyParser.json()); >> server\server.js
echo app.use(express.static(path.join(__dirname, '../public'))); >> server\server.js
echo mongoose.connect('mongodb://localhost/globalchat', { useNewUrlParser: true, useUnifiedTopology: true }); >> server\server.js
echo app.use('/', api); >> server\server.js
echo const server = app.listen(3000, () => { >> server\server.js
echo     console.log('Server running on port 3000'); >> server\server.js
echo }); >> server\server.js
echo const io = socketIo(server); >> server\server.js
echo io.on('connection', (socket) => { >> server\server.js
echo     console.log('New user connected'); >> server\server.js
echo     socket.on('chatMessage', (msg) => { >> server\server.js
echo         io.emit('chatMessage', msg); >> server\server.js
echo     }); >> server\server.js
echo     socket.on('disconnect', () => { >> server\server.js
echo         console.log('User disconnected'); >> server\server.js
echo     }); >> server\server.js
echo }); >> server\server.js
)

(
echo const express = require('express'); > server\routes\api.js
echo const router = express.Router(); >> server\routes\api.js
echo const nodemailer = require('nodemailer'); >> server\routes\api.js
echo const User = require('../models/user'); >> server\routes\api.js
echo router.post('/send-otp', (req, res) => { >> server\routes\api.js
echo     const email = req.body.email; >> server\routes\api.js
echo     const otp = Math.floor(100000 + Math.random() * 900000); >> server\routes\api.js
echo     const transporter = nodemailer.createTransport({ >> server\routes\api.js
echo         service: 'gmail', >> server\routes\api.js
echo         auth: { >> server\routes\api.js
echo             user: 'your-email@gmail.com', >> server\routes\api.js
echo             pass: 'your-email-password' >> server\routes\api.js
echo         } >> server\routes\api.js
echo     }); >> server\routes\api.js
echo     const mailOptions = { >> server\routes\api.js
echo         from: 'your-email@gmail.com', >> server\routes\api.js
echo         to: email, >> server\routes\api.js
echo         subject: 'Your OTP Code', >> server\routes\api.js
echo         text: `Your OTP code is ${otp}` >> server\routes\api.js
echo     }; >> server\routes\api.js
echo     transporter.sendMail(mailOptions, (error, info) => { >> server\routes\api.js
echo         if (error) { >> server\routes\api.js
echo             return res.status(500).send('Error sending OTP'); >> server\routes\api.js
echo         } else { >> server\routes\api.js
echo             res.status(200).send('OTP sent successfully'); >> server\routes\api.js
echo         } >> server\routes\api.js
echo     }); >> server\routes\api.js
echo }); >> server\routes\api.js
echo module.exports = router; >> server\routes\api.js
)

(
echo const mongoose = require('mongoose'); > server\models\user.js
echo const userSchema = new mongoose.Schema({ >> server\models\user.js
echo     username: String, >> server\models\user.js
echo     email: String, >> server\models\user.js
echo     friends: [String] >> server\models\user.js
echo }); >> server\models\user.js
echo const User = mongoose.model('User', userSchema); >> server\models\user.js
echo module.exports = User; >> server\models\user.js
)

REM Create .gitignore file
echo node_modules/ > .gitignore
echo .env >> .gitignore

REM Create package.json file
(
echo { > package.json
echo   "name": "global-chat", >> package.json
echo   "version": "1.0.0", >> package.json
echo   "description": "Global chat platform", >> package.json
echo   "main": "server/server.js", >> package.json
echo   "scripts": { >> package.json
echo     "start": "node server/server.js" >> package.json
echo   }, >> package.json
echo   "dependencies": { >> package.json
echo     "body-parser": "^1.19.0", >> package.json
echo     "express": "^4.17.1", >> package.json
echo     "mongoose": "^5.10.9", >> package.json
echo     "nodemailer": "^6.4.11", >> package.json
echo     "socket.io": "^3.0.3" >> package.json
echo   }, >> package.json
echo   "author": "", >> package.json
echo   "license": "ISC" >> package.json
echo } >> package.json
)

REM Create README.md file
echo # Global Chat Platform > README.md
echo A platform for real-time global chat. >> README.md
