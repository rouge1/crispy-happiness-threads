# Message Queue System

A simple message queue system implemented in Python using multiprocessing for inter-process communication.

## Components

- [`message_receiver.py`](message_receiver.py): Sets up a queue server that receives and displays messages
- [`message_sender.py`](message_sender.py): Client application that sends messages to the queue

## Requirements

- Python 3.x

## How to Use

1. First, start the receiver (server):
```bash
python message_receiver.py
```

2. Then, in a separate terminal, start the sender (client):
```bash
python message_sender.py
```

3. Type messages in the sender terminal and press Enter to send them. The messages will appear in the receiver terminal.

## Features

- Uses Python's multiprocessing manager for inter-process communication
- Timeout of 30 seconds on the receiver side
- Clean shutdown with Ctrl+C
- Error handling for connection issues

## Technical Details

- Port: 50000 (localhost)
- Authentication key: abc123
- Queue implementation: Python's standard `queue.Queue`
