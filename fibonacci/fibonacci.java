public class Solution {
    /*
     * @param n: an integer
     * @return: an integer f(n)
     */

    //The first solution is time limit exceeded, because we use recursion solution. The time complexity is O(2^n).
    /***
    public int fibonacci(int n) {
        if (n <= 1) {
    	    return 0;
	}

	if (n == 2) {
	    return 1;
 	}

	return fibonacci(n - 2) + fibonacci(n - 1);
    }
    ***/

    //The second solution is non-recursive. The time complexity is O(n).
    public int fibonacci(int n) {
        int n1 = 0;
	int n2 = 1;

	for (int i = 2; i <= n; i++) {
	    int n3 = n1 + n2;
	    n1 = n2;
            n2 = n3;
	}

	return n1;
    }

}
