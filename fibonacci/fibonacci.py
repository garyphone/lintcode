class Solution:
    # recursive
    '''def fibonaci(self, n):
	if n == 1:
	   return 0
	elif n == 2:
	   return 1
	else:
	   return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    '''
    # non-recursive
    def fibonacci(self, n):
	num = [0,1]
	if n == 1:
	   return 0
	elif n == 2:
	   return 1
	for i in range(0, n - 2):
	    num.append(num[-1] + num[-2])
	return num[-1]
