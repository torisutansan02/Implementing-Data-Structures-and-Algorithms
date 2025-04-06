from linked_list import SinglyLinkedList, Node

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create a cycle starting at index 2
def createCycle(head, pos):
    if pos == -1:
        return head

    cycle_start = None
    curr = head
    index = 0

    # Save the node at position `pos`
    while curr.next:
        if index == pos:
            cycle_start = curr
        curr = curr.next
        index += 1

    # Link last node back to the `cycle_start`
    curr.next = cycle_start

# Base list for testing
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.prepend(0)
ll.append(3)
ll.insert(2, 3)
print("Original list:", ll, "\n")

ll.delete(1)
print("After deleting index 1:", ll, "\n")

# Reverse in-place using head
ll.head = ll.reverseList(ll.head)
print("Reversed list:", ll, "\n")

middle = ll.findMiddle(ll.head)
print("Middle node value:", middle.val, "\n")

# Create a cycle manually
ll.append(2)
tail = ll.head
createCycle(ll.head, 1)
print("Has cycle?", ll.hasCycle(ll.head), "\n")

# Remove cycle to safely continue
tail.next = None

# Merge two sorted lists (LeetCode-style)
l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(5)

l2 = Node(2)
l2.next = Node(3)

mergedList = SinglyLinkedList()
merged_head = mergedList.mergeTwoSortedLists(l1, l2)
print("Merged sorted lists:")
printList(merged_head)
print("\n")

# Remove Nth from End
ll = SinglyLinkedList()
for i in range(6):
    ll.append(i)
print(ll)
ll.removeNthFromEnd(ll.head, 2)
print(ll, "\n")

# Is it a palindrome?

ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(1)

print(ll)
print(ll.isPalindrome(ll.head))

ll.delete(0)
print(ll)
print(ll.isPalindrome(ll.head), "\n")

# Detect the start of a cycle
ll = SinglyLinkedList()
for i in range(6):
    ll.append(i)
createCycle(ll.head, 2)

print(ll)
start = ll.detectCycle(ll.head)
print("Cycle starts at:", start.val if start else "No cycle")