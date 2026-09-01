class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Map original node -> copied node
        old_to_new = {}

        # First pass: create all copied nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: connect next and random pointers
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]