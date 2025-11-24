class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item. Return None if empty."""
        if not self.items:
            print("Warning: Dequeue from empty queue.")
            return None
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it. Return None if empty."""
        if not self.items:
            print("Warning: Peek from empty queue.")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# --- Interactive part ---
def main():
    q = Queue()
    print("Queue Program Started. Commands: enqueue <value>, dequeue, peek, size, exit")

    while True:
        command = input("Enter command: ").strip().lower()

        if command.startswith("enqueue"):
            try:
                _, value = command.split()
                q.enqueue(value)
                print(f"Enqueued {value}. Queue: {q.items}")
            except ValueError:
                print("Usage: enqueue <value>")

        elif command == "dequeue":
            result = q.dequeue()
            print(f"Dequeued: {result}. Queue: {q.items}")

        elif command == "peek":
            result = q.peek()
            print(f"Peek: {result}")

        elif command == "size":
            print(f"Queue size: {q.size()}")

        elif command == "exit":
            print("Exiting program.")
            break

        else:
            print("Unknown command. Try: enqueue <value>, dequeue, peek, size, exit")


if __name__ == "__main__":
    main()
