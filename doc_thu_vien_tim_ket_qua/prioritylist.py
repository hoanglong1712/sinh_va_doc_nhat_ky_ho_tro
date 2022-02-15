
class Node:
    def __init__(self, value, key, time):
        self.value = value
        self.key = key
        self.next = None
        self.time = time
        pass
    pass

class PriorityList:
    def __init__(self):
        self.head = None
        pass

    def add(self, key, value, time):
        n = Node(value, key, time)
        if self.head is None:
            self.head = n
            pass
        else:
            if key > self.head.key:
                n.next = self.head
                self.head = n
                pass
            else:
                t = self.head
                p = None
                while t is not None and t.key >= key and t.time > time:
                    p = t
                    t = t.next
                    pass
                p = n
                n.next = t
                pass
            pass
        pass
    def __iter__(self):
        n = self.head
        while n is not None:
            yield n
            n = n.next
            pass
        pass
