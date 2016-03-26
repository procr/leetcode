'''
Implementing a lru cache, to fulfill the requirement:
get op :O(1)
set op :O(1)

get: I use a hash table(dictory in python '''{}''' to make get op fast)

set: to maintain lru semantics, use linked list:
    evict: del list tail
    update: advance to head
    set: insert to head

'''

class Node(object):
    def __init__(self, key = None, val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class List(object):
    def __init__(self):
        self.head = Node()
        self.head.prev = self.head.next = self.head
        self.size = 0

    def listAddHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def listDel(self, node):
        if node == self.head:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

        return node

    def listDelTail(self):
        node = self.head.prev
        return self.listDel(node)
    
    def listAdvance(self, node):
        self.listDel(node)
        self.listAddHead(node)




class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.record = {}
        self.list = List()
        

    def get(self, key):
        """
        :rtype: int
        """

        if key not in self.record:
            return -1

        # shadow copy here, if deep copy is needed, use 
        # _obj = copy.deepcopy(obj)
        rec = self.record[key]

        self.list.listAdvance(rec)

        return rec.val
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        if key in self.record:
            rec = self.record[key]
            self.list.listAdvance(rec)
            rec.val = value
        else:
            node = Node(key, value)

            if self.list.size == self.capacity:
                delNode = self.list.listDelTail()

                del self.record[delNode.key]

            self.list.listAddHead(node)

            self.record[key] = node


cache = LRUCache(2)
cache.set(2, 1)
cache.set(2, 2)
print cache.get(2)
cache.set(1, 1)
cache.set(4, 1)
print cache.get(2)