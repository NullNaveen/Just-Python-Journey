const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const nodemailer = require('nodemailer');
const path = require('path');
const app = express();
const api = require('./routes/api');
const socketIo = require('socket.io');

// Middleware
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../public')));

// Connect to MongoDB
mongoose.connect('mongodb://localhost/globalchat')
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// API routes
app.use('/', api);

// Start server
const server = app.listen(3000, () => {
    console.log('Server running on port 3000');
});

// Socket.io
const io = socketIo(server);
io.on('connection', (socket) => {
    console.log('New user connected');
    socket.on('chatMessage', (msg) => {
        io.emit('chatMessage', msg);
    });
    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});
