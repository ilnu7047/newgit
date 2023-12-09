import queue

class MyPriorityQueueManager:
    def __init__(self):
        self.my_priority_queue = queue.PriorityQueue()

    def add_element(self, priority, element):
        self.my_priority_queue.put((priority, element))

    def pop_element(self):
        return self.my_priority_queue.get()

    def display_priority_queue(self):
        return list(self.my_priority_queue.queue)


priority_queue_manager = MyPriorityQueueManager()
priority_queue_manager.add_element(3, "P Element")
popped_element = priority_queue_manager.pop_element()
print("Original Priority Queue: ", priority_queue_manager.display_priority_queue())
print("Element Added: (3, 'P Element')")
print("Popped Element: ", popped_element)
