
const express = require('express');
const app = express();
const port = 3000; // You can choose any port you prefer
const spawn = require('child_process').spawn;

app.use(express.static('public'))
// Define a route to handle the GET request
app.get('/play', (req, res) => {
  board = req.query.board
  spawn('python3.10', ['nim_player_gui_helper.py',board])
    .stdout.on('data', (data) => {
      board = data.toString()
      console.log(board)
      res.send(board)
    }
  );

  
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
