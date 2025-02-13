# Distributed Chat System

A distributed chat system built using sockets for real-time communication between clients and a server.

## Features

-   Real-time messaging between multiple connected clients.
-   Simple socket-based communication for scalability.
-   Lightweight and easy to deploy.
-   Basic nickname handling.
-   Chat Room functionality: Create and join different chat rooms.

## Getting Started

### Prerequisites

-   Python 3.x
-   No external modules are required (uses built-in `socket` and `threading`).

### Installation

1.  Clone the repository:

    ```
    git clone https://github.com/mukiralad/distributed-chat-system.git
    ```

2.  Navigate to the project directory:

    ```
    cd distributed-chat-system
    ```

### Running the Server

1.  Start the server:

    ```
    python server.py
    ```
    
### Running the Client

1.  Open a new terminal window.
2.  Run the client:

    ```
    python client.py
    ```

## Usage

-   Start the server first.
-   Run multiple clients to join the chat.

### Chat Room Commands

-   `/create <roomname>`: Creates a new chat room with the specified name and automatically joins it.
-   `/join <roomname>`: Joins an existing chat room with the specified name.

## Notes

-   The server listens on host `127.0.0.1` (localhost) and port `9999` by default. This can be modified in the `server.py` and `client.py` files.
-   To run multiple clients, open multiple terminal windows and run `python client.py` in each.
-   Clients start in the "general" chat room by default.

