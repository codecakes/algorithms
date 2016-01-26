"""
Given a string S, find number of words in that string. For this problem a word is defined by a string of one or more English letters.

Note: Space or any of the special characters like ![,?.\_'@+] will act as a delimiter.

Input Format
The string will only contain lower case english alphabets, upper case english alphabets, blank spaces and this special characters: ![,?.\_'@+].


Output Format
In the first line, print number of words in the string. The words don't need to be unique. Also print each word in a separate line.

Sample Input

He is a very very good boy, isn't he?

Sample Output

10
He
is
a
very
very
good
boy
isn
t
he

"""
import re
c = re.compile(r"[a-zA-Z]+", re.IGNORECASE)

def split_w(S):
    ln = len(S)
    lo = 0
    hi = ln -1
    blackList = list("![,?.\_'@+]")
    stack = [(lo, hi)]
    s = ''
    out = []
    res = []

    # Klg(n)
    while stack:
        # lg(n)
        lo, hi = stack.pop()
        if lo<hi:
            mid = (lo+hi)/2
            stack.append((mid+1, hi))
            stack.append((lo, mid))
        else:
            # O(K) | K<=n or K>n
            res = c.findall(S[lo])
            if res:
                out.extend(res)
    print len(out)
    for w in out:
        print w

S = raw_input().strip("\n").split()
split_w(S)