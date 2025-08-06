const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const app = express();

// Define the directory for storing emergency videos
const emergencyAlertDir = path.join(__dirname, 'emergency_alert');

// Ensure the 'emergency_alert' directory exists (create it if it doesn't)
if (!fs.existsSync(emergencyAlertDir)) {
  fs.mkdirSync(emergencyAlertDir);
}

// Set up multer to store uploaded videos inside the 'emergency_alert' directory
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, emergencyAlertDir); // Save in the 'emergency_alert' directory
  },
  filename: (req, file, cb) => {
    // Customize the file name using timestamp
    const filename = `emergency_video_${Date.now()}.webm`;
    cb(null, filename); // Set the custom filename
  }
});

const upload = multer({ storage: storage });

// Middleware to handle JSON data (for location)
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Handle POST request for emergency alert
app.post('/sendEmergencyAlert', upload.single('video'), (req, res) => {
  const videoFile = req.file; // The video file
  const location = JSON.parse(req.body.location); // The location data
  
  // Log the file information and location for debugging
  console.log('Received video file:', videoFile);
  console.log('Received location:', location);
  

  const fullPath ='C:\Users\Sudha\Videos\emergency video' (__dirname, 'emergency_alert', videoFile.filename);
  // Respond to the client
  res.json(
    {
        "message": "Emergency alert received successfully",
        "videoPath": "/absolute/path/to/your/project/emergency_alert/emergency_video_1617884845363.webm"
      });
});

// Start the server
app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
