class SimpleUndoRedo:
    def __init__(self, initial=""):
        self.undo_stack = []
        self.redo_stack = []
        self.current = initial

    def make_change(self, new_text):
        self.undo_stack.append(self.current)
        self.current = new_text
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo!")
            return
        self.redo_stack.append(self.current)
        self.current = self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo!")
            return
        self.undo_stack.append(self.current)
        self.current = self.redo_stack.pop()

    def display(self):
        print("Current Document:", self.current)


# --- interactive demo ---
if __name__ == "__main__":
    doc = SimpleUndoRedo("")

    while True:
        print("\nOptions: 1) Make Change  2) Undo  3) Redo  4) Display  5) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            new_text = input("Enter new document text: ")
            doc.make_change(new_text)
        elif choice == "2":
            doc.undo()
        elif choice == "3":
            doc.redo()
        elif choice == "4":
            doc.display()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")