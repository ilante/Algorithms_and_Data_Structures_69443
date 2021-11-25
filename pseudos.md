# Pseudos

# String matching

```
javascript=
var s = "JavaScript syntax highlighting";
alert(s);
```

Exact string matching brute force;
```python=
ESM-BF(P,S)
m = LENGTH(P), n = LENGTH(S)
k = 0       # number of matches 
for j=1,...,n - m + 1 do
    i=1
    while i ≤ m and P[i] == S[j+i] do
        i = i +1
    if i == m+1 then
        k=k+1 
return k
```
**RT**: Worst-case cost 

* $O(m(n-m+1)) = O(mn - m^2) < O(mn)$


```javascript=
ESM-KMP(P, S)        \\ pattern, string
    M = LENGTH(P), N = Lenght(S)
    k = 0           \\ number of matches
    i = 1           \\ starting position in P
    j = 1           \\ starting position in S
    F = KMP-FF (P)  \\ failure function for P
    while j ≤ n do
        if P[i] == S[j] then \\ match
            i = i + 1
            j = j + 1
            if i == M+1 then    # pattern found
                k = k + 1
                i = F[i]        # new starting index in P
        else                    # mismatch
            i = F[i]            # new starting index in P
            if i == 0 then      # 0 = failure ⇒ restart
                i = 1           # restart i
                j = j + 1
return k
```
Time complexity ESM-KMP:

 * Dependent on number of times the *while* is executed
 * At most N total decrements $O(n)$ 
 * Cost of the *while loop*: 
   * &Omega;(n) and $O(2n)$