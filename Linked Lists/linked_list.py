from abc import ABC, abstractmethod

# Abstract interface for Linked List
class AbstractLinkedList(ABC):
    @abstractmethod
    def get(self, index): pass

    @abstractmethod
    def append(self, value): pass

    @abstractmethod
    def prepend(self, value): pass

    @abstractmethod
    def insert(self, index, value): pass

    @abstractmethod
    def delete(self, index): pass

    @abstractmethod
    def reverseList(self, head): pass

    @abstractmethod
    def findMiddle(self, head): pass

    @abstractmethod
    def mergeTwoSortedLists(self, list1, list2): pass

    @abstractmethod
    def removeNthFromEnd(self, head, n): pass

    @abstractmethod
    def isPalindrome(self, head): pass

    @abstractmethod
    def detectCycle(self, head): pass

    @abstractmethod
    def __str__(self): pass

# Node class (same as ListNode in LeetCode)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Singly Linked List with LeetCode-style methods
class SinglyLinkedList(AbstractLinkedList):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        
        curr = self.head

        i = 0
        while i < index:
            curr = curr.next
            i += 1
        
        return curr.val


    def append(self, val):
        value = Node(val)
        if not self.head:
            self.head = value
            self.size += 1
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = value
        self.size += 1

    def prepend(self, val):
        value = Node(val)
        value.next = self.head
        self.head = value
        self.size += 1

    def insert(self, index, val):
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.prepend(val)
            return

        value = Node(val)
        
        curr = self.head

        i = 0
        while i < index - 1:
            curr = curr.next
            i += 1

        value.next = curr.next
        curr.next = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        curr = self.head
        i = 0
        while i < index - 1:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        self.size -= 1

    # LeetCode-style reverseList(head)
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    # LeetCode-style findMiddle(head)
    def findMiddle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # LeetCode-style hasCycle(head)
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # LeetCode-style mergeTwoSortedLists(list1, list2)
    def mergeTwoSortedLists(self, list1, list2):
        dummy = Node(-1)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next

    def removeNthFromEnd(self, head, n):
        dummy = Node(0)
        dummy.next = head
        slow = fast = dummy

        i = 0
        while i < n:
            fast = fast.next
            i += 1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
    
    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        curr = prev
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return True
    
    def detectCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if fast == None:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

    # Cycle-safe print
    def __str__(self):
        values = []
        curr = self.head
        visited = set()
        while curr:
            if id(curr) in visited:
                values.append("(cycle)")
                break
            visited.add(id(curr))
            values.append(str(curr.val))
            curr = curr.next
        return "[" + ", ".join(values) + "]"
