import threading
import time

# Worker function for the thread
def worker():
    print("Worker thread started")
    time.sleep(3)  # Simulating a time-consuming task
    print("Worker thread completed")

# Create and start a new thread
thread = threading.Thread(target=worker)
thread.start()

# Continue with other tasks in the main thread
print("Main thread continues")