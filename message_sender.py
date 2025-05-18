import queue as queue_module
import time
from multiprocessing.managers import BaseManager

# Define the queue manager
class QueueManager(BaseManager):
    pass

def main():
    # Register the queue with the manager
    QueueManager.register('get_queue')
    
    # Connect to the queue manager
    manager = QueueManager(address=('localhost', 50000), authkey=b'abc123')
    manager.connect()
    
    # Get the queue from the manager
    queue_instance = manager.get_queue()
    
    print("Type messages and press Enter to send. Press Ctrl+C to exit.")
    
    while True:
        try:
            # Get input from user
            user_input = input("> ")
            queue_instance.put(user_input)
            print(f"Sent: {user_input}")
            
        except KeyboardInterrupt:
            print("\nSender stopping...")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == '__main__':
    main()