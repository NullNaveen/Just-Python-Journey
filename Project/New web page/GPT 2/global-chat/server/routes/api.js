const express = require('express');
const router = express.Router();
const nodemailer = require('nodemailer');
const User = require('../models/user');

// Create a transporter for Nodemailer
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'your-email@gmail.com',
        pass: 'your-email-password'
    }
});

// POST /send-otp
router.post('/send-otp', (req, res) => {
    const email = req.body.email;
    if (!email) {
        return res.status(400).send('Email is required');
    }

    const otp = Math.floor(100000 + Math.random() * 900000);

    const mailOptions = {
        from: 'your-email@gmail.com',
        to: email,
        subject: 'Your OTP Code',
        text: `Your OTP code is ${otp}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error('Error sending OTP:', error);
            return res.status(500).send('Error sending OTP');
        } else {
            console.log('OTP sent:', info.response);
            // Here you should ideally save the OTP in a temporary store or database for verification later
            res.status(200).send('OTP sent successfully');
        }
    });
});

module.exports = router;
