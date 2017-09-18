class Solution:
   """
   @param: head: a ListNode
   @param: val: An integer
   @return: a ListNode
   """
   def removeElements(self, head, val):
        # write your code here
	if head is None:
	   return None
	# create a head number in the front of the list
	new = ListNode(0)
	new.next = head
	head = new
	pre = head
	while pre.next is not None:
	  if pre.next.val == val:
	      pre.next = pre.next.next
	  else:
	      pre = pre.next
	  new = new.next
	return head.next
