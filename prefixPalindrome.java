String solution(String s) {
    return cutString(s);
}

String cutString(String s) {
    for (int i = s.length()-1; i>0; i--) {
        String prefix = s.substring(0,i+1);
        if (isPalindrome(prefix)) {
            System.out.println("Prefix: " + prefix);
            System.out.println("I = " +i+"Recursing on: " + s.substring(i+1));
            return cutString(s.substring(i+1));
        }
    }
    return s;
}

boolean isPalindrome(String s) {
    for (int i = 0; i<s.length()/2; i++) {
        if (s.charAt(i) != s.charAt(s.length()-i-1)) {return false;}
    }
    return true;
}



/*
You are given a string s. Consider the following algorithm applied to this string:

Take all the prefixes of the string, and choose the longest palindrome between them.
If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
Your task is to implement the above algorithm and return its result when applied to string s.

Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

Example

For s = "aaacodedoc", the output should be solution(s) = "".

The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut it from s.
Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut it from the current string and obtain the empty string.
Finally the algorithm ends on the empty string, so the answer is "".
For s = "codesignal", the output should be solution(s) = "codesignal".
The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

For s = "", the output should be solution(s) = "".

Input/Output

[execution time limit] 3 seconds (java)

[input] string s

A string consisting of English lowercase letters.

Guaranteed constraints:
0 ≤ s.length ≤ 1000.

[output] string

The result of the described algorithm.
 */
