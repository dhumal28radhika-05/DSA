
# Node class
class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


# Priority Queue using Linked List
class PriorityQueue:

    def __init__(self):
        self.front = None

    # 1. Add Patient
    def enqueue(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-3): "))

        if priority < 1 or priority > 3:
            print("Invalid Priority!")
            return

        new_node = Node(pid, name, priority)

        # If list is empty or new patient has higher priority
        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front

            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient added successfully!")

    # 2. Display Next Patient
    def display_next(self):
        if self.front is None:
            print("No patients waiting!")
        else:
            print("Next Patient:", self.front.name)
            print("Priority:", self.front.priority)

    # 3. Remove Patient
    def dequeue(self):
        if self.front is None:
            print("No patients to remove!")
        else:
            print("Patient treated:", self.front.name)
            self.front = self.front.next

    # 4. Display All Patients
    def display_all(self):
        if self.front is None:
            print("No patients waiting!")
        else:
            temp = self.front

            while temp is not None:
                print(temp.pid, temp.name, temp.priority)
                temp = temp.next


# Main Program
pq = PriorityQueue()

while True:
    print("\n1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        pq.enqueue()
    elif choice == 2:
        pq.display_next()
    elif choice == 3:
        pq.dequeue()
    elif choice == 4:
        pq.display_all()
    elif choice == 5:
        break
    else:
        print("Invalid Choice!")
