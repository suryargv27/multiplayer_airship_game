# Multiplayer Airship Game

## Overview
This is a simple multiplayer airship game built using Python and Pygame, with networking handled via sockets. The game allows two players to compete in real-time, controlling airships to hit a moving ball. The server manages the game logic, while clients connect to play.

## Features
- **Real-time multiplayer gameplay**
- **Simple player controls** (left and right movement)
- **Scoring system**
- **Ball physics with collision detection**
- **Threaded server to handle multiple clients**

## Requirements
Ensure you have the following installed:

- Python 3.x
- Pygame (`pip install pygame`)
- Pickle (comes with Python)

## File Structure
```
multiplayer-airship-game/
│── client.py  # Client-side script
│── server.py  # Server-side script
│── network.py # Handles client-server communication
│── README.md  # Documentation
```

## Installation and Setup
1. **Clone the repository**
```sh
git clone https://github.com/your-username/multiplayer-airship-game.git
cd multiplayer-airship-game
```

2. **Install dependencies**
```sh
pip install pygame
```

## Running the Game
### 1. Start the Server
Run the server script on a machine that will host the game:
```sh
python server.py
```
The server will start listening for connections.

### 2. Start the Clients
Each player runs the client script:
```sh
python client.py
```
Ensure that the `IP` address in `network.py` matches the server's IP.

## How to Play
- Move your airship left and right using **arrow keys**
- Hit the ball to send it towards the opponent
- The game keeps score when the ball crosses the opponent's goal line
- First to reach a set score wins

## Network Communication
- The server listens on a predefined IP and port.
- Clients send and receive position data using sockets and Pickle for serialization.
- The game updates ball movement, collision detection, and scorekeeping on the server side.

## Troubleshooting
- Ensure both players and the server are on the same network.
- If clients cannot connect, check the firewall settings and verify the correct `IP` in `network.py`.
- If the game lags, try reducing the frame rate or optimizing network communication.

## Future Improvements
- Implement a GUI for matchmaking
- Add sound effects and animations
- Improve physics for a more realistic experience
- Expand to support more than two players

## License
This project is open-source and available under the MIT License.


