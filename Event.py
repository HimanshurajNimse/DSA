from collections import deque

# Create a queue to store events
event_queue = deque()

# Add an Event
def add_event(event):
    event_queue.append(event)
    print(f"Event '{event}' added to the queue.")

# Process the Next Event
def process_event():
    if event_queue:
        event = event_queue.popleft()
        print(f"Processed event: {event}")
    else:
        print("No events to process!")

# Display Pending Events
def display_events():
    if event_queue:
        print("Pending Events:", list(event_queue))
    else:
        print("No pending events!")

# Cancel an Event
def cancel_event(event):
    if event in event_queue:
        event_queue.remove(event)
        print(f"Event '{event}' canceled.")
    else:
        print("Event not found or already processed!")

# --- Demo ---
if __name__ == "__main__":
    while True:
        print("\n1. Add Event\n2. Process Next Event\n3. Display Pending Events\n4. Cancel Event\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            e = input("Enter event name: ")
            add_event(e)
        elif choice == "2":
            process_event()
        elif choice == "3":
            display_events()
        elif choice == "4":
            e = input("Enter event name to cancel: ")
            cancel_event(e)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
