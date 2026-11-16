# Multi-Threaded TCP Chatroom

A lightweight, real-time command-line chat server and client built from scratch in Python using raw TCP sockets and multithreading.

## Overview

This project was built to explore how network protocols, concurrent client connections, and socket state management work at Layer 4 (TCP) and Layer 7 (Application) without relying on high-level web frameworks.

### Key Features & Concepts Demonstrated
* **Raw TCP Socket Programming:** Uses Python's `socket` module (`AF_INET`, `SOCK_STREAM`) to manage client-server connections over TCP/IP.
* **Concurrent Client Handling:** Uses `threading` on the server to handle multiple simultaneous client sessions and on the client to listen for incoming broadcasts while reading user input.
* **Custom JSON Application Protocol:** Structures payloads with message types (`username`, `message`) to separate session initialisation from chat broadcasts.
* **Socket Reuse Handling:** Implements `SO_REUSEADDR` to prevent `Address already in use` errors caused by sockets lingering in the `TIME_WAIT` state after server restarts.

## Project Structure

```text
chatroom/
├── server.py         # Multi-threaded TCP server handling connections and message broadcasting
├── client.py         # CLI client with concurrent send/receive threads
├── pyproject.toml    # Project configuration managed with uv
└── README.md
```

## Prerequisites

* Python 3.10+
* [uv](https://github.com) (or standard Python)

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Start the server:**
   ```bash
   uv run server.py
   ```
   *(The server binds to `0.0.0.0:8080` by default and waits for incoming connections.)*

3. **Connect one or more clients (in separate terminals):**
   ```bash
   uv run client.py
   ```
   Enter a username when prompted and start sending messages.

## Planned Improvements (Roadmap)

* [ ] Add `try...finally` connection cleanup and `threading.Lock` for thread-safe client list management.
* [ ] Implement newline-delimited message framing (`\n`) to handle TCP stream buffering cleanly.
* [ ] Containerise the server and client with Docker to test multi-container networking.
