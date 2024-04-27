class Solution(object):
    def hasCycle(self, head):

# slow fast pointers , O(1) space , O(n) time. 
        fast, slow = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False

