const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const crypto = require('crypto');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Middleware
app.use(bodyParser.json());
app.use(express.static('public'));

// Nodemailer configuration
const transporter = nodemailer.createTransport({
    service: 'yahoo',
    auth: {
        user: 'nikcynike707@yahoo.com', // Replace with your email
        pass: 'Neevan@128'   // Replace with your email password or app-specific password
    }
});

// In-memory storage for OTPs and usernames
const users = {}; // Stores OTPs keyed by email
const usernames = new Set(); // Stores unique usernames

// Send OTP endpoint
app.post('/send-otp', (req, res) => {
    const email = req.body.email;
    if (!email) {
        return res.status(400).send('Email is required');
    }

    const otp = crypto.randomBytes(4).toString('hex');
    users[email] = otp;

    const mailOptions = {
        from: 'your-email@gmail.com',
        to: email,
        subject: 'Your OTP Code',
        text: `Your OTP code is ${otp}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error('Error sending email:', error);
            return res.status(500).send('Error sending email');
        }
        res.send('OTP sent');
    });
});

// Verify OTP endpoint
app.post('/verify-otp', (req, res) => {
    const { email, otp } = req.body;
    if (users[email] === otp) {
        delete users[email]; // OTP verified, remove it
        res.send('OTP verified');
    } else {
        res.status(400).send('Invalid OTP');
    }
});

// WebSocket connection
io.on('connection', (socket) => {
    console.log('A user connected');

    // Handle username registration
    socket.on('register username', (data, callback) => {
        const { email, username } = data;
        if (!/^[a-zA-Z]+$/.test(username)) {
            return callback('Username should only contain alphabets');
        }
        if (usernames.has(username)) {
            return callback('Username already taken');
        }
        usernames.add(username);
        callback(null);
        socket.username = username;
        io.emit('user joined', { username });
    });

    // Handle chat messages
    socket.on('chat message', (msg) => {
        io.emit('chat message', { username: socket.username, message: msg });
    });

    // Handle user disconnect
    socket.on('disconnect', () => {
        console.log('A user disconnected');
        if (socket.username) {
            io.emit('user left', { username: socket.username });
            usernames.delete(socket.username);
        }
    });
});

// Start server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
