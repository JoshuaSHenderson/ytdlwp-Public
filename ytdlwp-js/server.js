const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000; // You can change the port if needed

// Serve static files (your HTML, CSS, and JavaScript files)
app.use(express.static(path.join(__dirname, 'public')));

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

