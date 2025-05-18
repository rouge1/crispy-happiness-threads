import queue as queue_module
from multiprocessing.managers import BaseManager

# Define the queue manager
class QueueManager(BaseManager):
    pass

def main():
    # Create the shared queue
    message_queue = queue_module.Queue()
    
    # Register the queue with the manager
    QueueManager.register('get_queue', callable=lambda: message_queue)
    
    # Start the queue manager
    manager = QueueManager(address=('localhost', 50000), authkey=b'abc123')
    manager.start()
    
    print("Receiver started. Waiting for messages...")
    
    try:
        queue_instance = manager.get_queue()
        
        while True:
            try:
                message = queue_instance.get(timeout=30)
                print(f"Received: {message}")
            except queue_module.Empty:
                print("No messages received for 30 seconds")
            
    except KeyboardInterrupt:
        print("\nReceiver stopping...")
    finally:
        manager.shutdown()

if __name__ == '__main__':
    main()