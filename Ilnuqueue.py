import queue

class MyQueueManager:
    def __init__(self):
        self.my_queue = queue.Queue()

    def add_element(self, element):
        self.my_queue.put(element)

    def pop_element(self):
        return self.my_queue.get()

    def display_queue(self):
        return list(self.my_queue.queue)


queue_manager = MyQueueManager()
queue_manager.add_element("ilnu")
popped_element = queue_manager.pop_element()
print("Original Queue: ", queue_manager.display_queue())
print("Element Added: ilnu")
print("Popped Element: ", popped_element)
