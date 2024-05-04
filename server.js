const express = require('express');
const multer = require('multer');
const path = require('path');
const app = express();
const port = 3000;

// Multer configuration
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'images/'); // Storing in the 'images' directory
    },
    filename: function (req, file, cb) {
        cb(null, Date.now() + path.extname(file.originalname));
    }
});

const upload = multer({ storage: storage });
limits: {
    fileSize: 100 * 1024 * 1024 // Limit file size to 5MB
}

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Handle POST requests to /upload
app.post('/images', upload.single('image'), (req, res) => {
    if (!req.file) {
        return res.status(400).send('No files were uploaded.');
    }
    res.sendStatus(200); // Sending a simple success response
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
