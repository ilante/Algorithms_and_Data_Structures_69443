ctrl + shift + p 'Markdown all in one: print current doc to html'

# -1 Questions

Iteration method: I don't get the example of 
$T(n) = T(n-1)+n^4$
Check out the video (it will start exacly at this example)

<iframe width="560" height="315" src="https://www.youtube.com/embed/MOAVDta-0as?start=740" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

So were she said we wil take the n titration for $T(0)$;

1. Why does she pick input size of 0? How does that even make sense
2. Why does she talk about the big O notation when the input of 0 should clearly be the best case scenario?
3. How does she get to the series?

$T(n-n)+(n-(n-1))^4+...(n-3)^4+(n-2)^4+(n-1)^4+n^4$

I can follow her for the fist 2 terms, but what is the deal with the last 4 terms. I don't see how this is supposed to be a simplification if we just have the same terms in the end as previously.

* Also should the basecase not be n=1 &rarr; problemsize 1?

<details>
<summary> @Fede; &Theta;(n^2) example; Why is c_2 1/2? </summary>

Why is $1/2𝑛^2−3𝑛=\Theta(𝑛^2)$?
[see here](https://cs.stackexchange.com/questions/98669/why-is-dfrac12n2-3n-thetan2)

</details>

<details>
<summary>Template</summary>

* remember to leave an empty line after summary
* remember to leave an empty line after answer
* add break before end details

<br>
</details>

# L 0 Mathematical Background

<details>
<summary>Infinite series?</summary>

$\sum_{k=1}^{\infty} a_k$, &emsp; wich we interpret to mean &emsp; $\lim_{n \to \infty} \sum_{k=1}^{n} a_k$

* If the limit exists the series *converges*
* The terms of a convergent series **cannot** always be added in any order

<br>
</details>

<details>
<summary>Linearity</summary>

For any real number *c* and any finite series $a_1, a_2,...,a_n$ and $b_1, b_2,...,b_n$ we have; $$\sum_{k=1}^{n}(ca_k+b_k) = c \sum_{k=1}^{n} a_k + \sum_{k=1}^{n} b_k$$

* This liniarity property also applies to infinite series
* We can make use of the linearity property to manipulate summations incorporating the asymptotic notation; e.g.

* $\sum_{k=1}^{n} \Theta(f(k)) = \Theta(\sum_{k=1}^{n}f(k))$
  * Here the left side $\Theta$ notation applies to *k*
  * The right side $\Theta$ applies to *n*

<br>
</details>

<details>
<summary>What is value of the following arithmetic series?

$\sum_{k=1}^{n} k = 1 + 2 + ... + n$ 

</summary>

$$
\begin{aligned}
\sum_{k=1}^{n}k &= \frac{n(n+1)}{2} \\
&= \Theta(n^2)
\end{aligned}
$$

Remember the the $\Theta$ statement only hods true  if:

There exist positive constants $c_1, c_2$ and $n_0$ such that $0 \leq c_1 g(n) \leq f(n) c_g(n)$

for all $n \geq n_0$

![Thetha](https://kb.novaordis.com/images/6/6d/Theta_Notation.png)

<br>
</details>

<details>
<summary>Sum of squares?</summary>
<br>

$\sum_{k=0}^{n}k^2 = \frac{n(n+1)(2n+1)}{6}$

<br>
</details>

<details>
<summary>Sum of cubes?</summary>
<br>

$$
\sum_{k=0}^{n}k^3 = \frac{n^2(n+1)^2}{4}
$$

<br>
</details>

<details>
<summary>Geometric or exponential series?</summary>

For real $x \neq 1,$ the sumation
$$\sum_{k=0}^{n} x^k = 1+x+x^2+ ... + x^n$$

is a geometric series or an exponential series and has the value
$\sum_{k=0}^{n} x^k = \frac{1}{1-x}$

<br>
</details>

<details>
<summary>Geometric or exponential series with an infinite sum and 

$|x| \leq 1$ ?</summary>

$$\sum_{k=0}^{\infty} x^k = \frac{1}{1-x}$$
Because we assume that $0^0 = 1$, These formulas apply even when $x=0$

<br>
</details>

<details>
<summary>Harmonic series</summary>

* For $n > 0$, the $n^th$ harmonic number is:
* $H_n = \frac{1}{1}, \frac{1}{2}, \frac{1}{3}, ..., \frac{1}{n}$ 
* $\sum_{k=1}^{n}$
* $ln(n) + O(1)$ - where big O is the upper bound


<br>
</details>


<details>
<summary>Sum of log k?</summary>

* $\sum_{k=1}^{n} log k \approx n log n$ 

<br>
</details>


<details>
<summary> What is the value of:

$\sum_{k=1}^{n} k^p$ 

</summary>

* $= 1^p+ 2^p + ... + n^p \approx \frac{1}{p+1} n^{p+1}$

<br>
</details>

<br>

# L 1

<details>
<summary>What is a tree?</summary>
<br>

* A set of **nodes** connected by **edges**, so that there is **exaclty one** way to get from any node to any other node. 

</details>

<details><summary>What is the fundamental property of a non-empty tree?</summary>

* Every non-empty tree with $n$ nodes has **exactly** $n-1$ edges.

</details>

<details>
<summary>What is a set?</summary>
<br>

* Each element can occur only once
* The elements are not ordered
* The number of elements in a set S is the cardinality of the set $(|S|)$
    * If the cardinality if a natural number, then the S is a finite set 
    * Otherwise it is infinite

</details>

<details>
<summary>Definition of a tree</summary>

* A tree is a set of **nodes** connected by **edges** so that there is **exactly one** way to get from **any** node to **any other** node 

<br>
</details>

<details>
<summary>Properties of a tree</summary>

* Every non-empty tree with n nodes has **exactly** $n-1$ edges
* A tree is rooted if one of its nodes is distinguished as **root**.
  * This definition cas be used recursively; A **rooted tree** consists of a **root node** and a finite set of **sub-trees** which are themselves rooted trees
  
<br>
</details>

<details>
<summary>Definition of a binary tree</summary>

* A binary tree is an **ordered tree** which is either
  * Empty
  * or consists of a **root node** and two subtrees, that are themselves binary trees

Here a full binary tree as an example:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Full_binary.svg/1600px-Full_binary.svg.png)

<br>
</details>

<details>
<summary>Definition of running time of an algorithm on a particular input</summary>

* The number of **primitive operations** (steps) executed 
* It depends on the input and usually grows with input size

<br>
</details>

<details>
<summary>Definition of <b><i>order of growth</b></i></summary>

* Gives a simple characterization of the algorithms **efficiency**

</details>

<details>
<summary>What is asymptotic behaviour?</summary>

* We are analyzing the **asymptotic behaviour** of algorithms
* Describes how the running time increases as the **size of the input** increases
* asymptotic behaviour can be described by certain asymptotic notations
 
</details>

<details>
<summary>What does the &Theta; notation describe?</summary>

* Describes the "equality" 
* $f(n)=g(g)$
  
<br>
</details>

<details>
<summary>&Theta;</summary>

* Indicates equality:
* $f(n)=g(n)$
  
</details>

<details>
<summary>big O</summary>

* 'less than or equal to'
* $f(n) \leq g(n)$
  
</details>

<details>
<summary>&Omega;</summary>

* 'greater than or equal to'
* $f(n) \geq g(n)$
  
</details>

<details>
<summary>little o</summary>

* 'strictly less than'
* $f(n)<(n)$

</details>

<details>
<summary>&omega;</summary>

* 'strictly greater than'
* $f(n)>g(n)$
  
</details>

<details>
<summary>Merge algorithm and video:</summary>

* Given two sorted decks of cards; "Left" and "Right"
* Both "Left" and "Right" are stacked up on the table facing up 
* Both stacks are sorted from highest to lowest with the lowest being exposed and on top of the stack
* The third stack is "Output" and it is empty to start with
* If $Left(i) \leq Right(j)$ we move the element to the output stack
* Wheneve we copy the item to the output stack we have to increase the index of L or R and we also have to increment the index of the output stack
Merge


<iframe width="560" height="315" src="https://www.youtube.com/embed/6pV2IF0fgKY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</details>

<details>
<summary>Video of the merge sort algorithm</summary>

* It is a sorting algorithm that follows the divide and conquer approach

<iframe width="560" height="315" src="https://www.youtube.com/embed/mB5HXBb_HY8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</details>

<br>
<br>


# L 3 Sorting Algos and Growth of Functions

<details>
<summary>What is the big <i>O</i>-notation for?</summary>

* It is the formal mathematical way to express the **upper bound** of the running time &rarr; to describe the **worst case**
* Measures the **worst case** time complexity of the longest amount of time an algorithm can possibly take to complete
* $O(g(n)) = \{f(n)$ : there exist positive constants $c$ and $n_o$ such that $0 \leq f(n) \leq cg(n) for\ all\ n \geq n_0\}$
* By using the $O$-notation to bound the worst case of an algorithm, we have an upper bound $\implies$ we have a bound on the running time on every input.
* The worst case is often similar or the same as the average case

<img src="https://s2.qwant.com/thumbr/474x472/e/4/57cfed11b3f840151c91c0bb1f00cc402a951cbed81a39384468c619a775e2/th.jpg?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.oNQte90XxqslB0Z72VnujAHaHY%26pid%3DApi&q=0&b=1&p=0&a=0" width="200" height="200">

<br>
</details>

<details>
<summary>What is the &Omega; notation for?</summary>

* It is the formal mathematical way to express the **best case** &rarr; asymptotic **lower bound** of the running time &rarr; 
* It is pronounced like "**oh my god**" - which is why you can tell that we are talking about the best case
* Sometimes also referred to as "big-&Omega;"
* Measures the **best case** time complexity of the minimum amount of time an algorithm can possibly take to complete

<img src="https://s2.qwant.com/thumbr/474x494/4/b/1012382d29d3188074c2a65d24e3541306b058915b3e24a34ab68196b72b2a/th.jpg?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.0VlgVBjisdqZGs2Cf1SZtAHaHu%26pid%3DApi&q=0&b=1&p=0&a=0" width="200" height="200">
<br>
</details>


<details>
<summary>What is the &Theta;-notation for? </summary>

* When using the &Theta;-notation, we're saying that we have an asymptotically tight bound on the running time
  * 'Asymptotically', because it matters only for **large values of n**
  * 'Tight bound', because the running time of $f(n)$ is bounded by the function $g(n)$ that is multiplied by a constant factor $c_1$ for the lower bound and $c_2$ for the upper bound
  * Thus $g(n)$ is an asymptotic tight bound for $f(n)$
* The &Theta;-notation can also be called "sandwich-notation" **because**; 
* $\Theta(g(n)) = \{f(n)|$ there exist positive constants $n_0 \geq 0$, $c_1$ and $c_2$ such that $0 \leq c_1g(n) \leq f(n) \leq c_2g(n) \forall n \geq n_o\}$
* Simply put; 
  * For any value (to the right of) larger than $n_0$, the value of $f(n)$ lies 
    * **At or above** $c_1g(n)$
    * And **at or below** $c_2g(n)$ see sandwich below
* $f(n) \in \Theta g(n)$ which we will simply express as $f(n) = \Theta g(n)$ for mathematical convenience

<img src="https://1.bp.blogspot.com/-sOrn-Gb-TtU/XPhqa31EyHI/AAAAAAAABy0/GOTyvRcbKQAe4F2zY6VqDl60gt-9AM1ogCLcBGAs/s400/BigTheta.png" width='200' height='200'>

* $Theta(g(n)) is the set of functions whose $growth = g(n)$
* Measured with respect to the constant multiples $c_1$ and $c_2$ as *n* &rarr; $\infty$
<br>
</details>



# L 4 

- Solving recurrence equations for runtime analysis of recursive algorithms

<details>
<summary>How can you describe the running time of a recursive algorithm?</summary>
<br>
By a recurrence equation that describes a function in terms of its value on smaller input.
</details>

<br>

# L 5

Recording [here](https://virtuale.unibo.it/mod/page/view.php?id=542187)

- Heaps 
- Heapsort
- Priority queues
  
<details>
<summary>What is a full binary tree?</summary>
<br>
A binary tree in which each

-  node is either a leaf, or 
-  has a degree that is exactly 2 (number of children). 
-  Put differently: each node has either degree zero or degree 2.
</details>

<details>
<summary>Complete binary tree?</summary>
<br>
A binary tree in which ALL leaves have the same depth 

and all internal nodes have degree 2.

You never create a new level before finishing the previous level.

All leave nodes must be at the same level.
</details>

<details>
<summary>What is a heap?</summary>
<br>
A nearly complete binary tree with the two following properties;

1. Structural property: all levels are full, except possibly the last one, which is filled from left to right.
2. Order/heap property: for any node $i$ parent($i$) $\geq$ i.
The maximum value appears in the root &rarr; also called Max Heaps.
3. The height of a heap of $n$ elements is $\lfloor log_2 n \rfloor$
</details>

<details>
<summary>What is the distance to the root?</summary>
<br>
The number of nodes you have to pass through form a leaf for reaching the node. In this case you do NOT count the leave but only the nodes you have to pass throgh.
</details>

<details>
<summary>What is the height of a heap?</summary>
<br>
It is $\lfloor log_2 n \rfloor$ 
</details>

Recording minute 13: 

<details>
<summary>What is the difference between a full binary tree and a complete binary tree?</summary>
<br>
A full binary tree might have leafs with differeing distances to the root. Thus the tree does not look completely symmetric. 

All leafs of the complete binary tree on the other hand must have the exact same distance to the root. Thus the tree is completely symmetric.
</details>

<details>
<summary>
What is the difference between a full binary tree and a heap?</summary>
<br>
The distance to the root might differ between leafs. For a full binary tree the longest distance from a leaf to the root might be several levels higher than the distance from the shortest leaf.

For the heap the distance to the root of the longest leafs compared to the shortest leafs can only differ by 1.

A heap is almost a complete binary tree, except for the last level. The last level may be partial but has to be filled from left to right. 

The last level of a heap may be incomplete just as in a full binary tree but it must be filled from left to right.
</details>

<details>
<summary>
What is the height of any binary tree?</summary>
<br>
The height is $log_2 n$. We will always consider the longest path from any leaf to the root! 
</details>

<details>
<summary>
Why could the datastructure of the heap be useful instead of simply using an array?</summary>
<br>
Because in some applications we have to exctract the highest value quickly. That way you know you can always access the element of highest value in constant time!
</details>

<details>
<summary>
What is the problem with the heap datasturcture?</summary>
<br>
If you remove the root (the highest value) you have to reorder the tree, to move the second largest number to the root.
</details>

* During the exam she might ask: I gave you a max heap example; can you adjust the algorithm to a min-heap?

<details>
<summary>
Describe the Max-heapify algorithm.</summary>
<br>
Max-Heapify(A, i) &rarr; where A is an array and i is the index<br/>
&nbsp;&nbsp;&nbsp;&nbsp;l = 2i<br/>
&nbsp;&nbsp;&nbsp;&nbsp;r = 2i + 1<br/>
&nbsp;&nbsp;&nbsp;&nbsp;if l $\leq$ A.heap-size and A[l] $>$ A[i]<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;largest = l<br/>
&nbsp;&nbsp;&nbsp;&nbsp;else largest = i<br/>
&nbsp;&nbsp;&nbsp;&nbsp;if r $\leq$ A.heap-size and A[r] $>$ A[largest]<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;largest = r<br/>
&nbsp;&nbsp;&nbsp;&nbsp;if largest $\ne$ i<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exchange A[i] with A[largest]<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Max-Heapify(A,largest)<br/>
Note that the value of $i$ does indeed change while the key of $i$ remains the same...

The stopping condition is when we reach the leafnodes

&rarr; We have 2 stopping conditions:

* Either your childs value is a leaf node: (l or r) is larger than A.heap-size &rarr; not representing an element in the heap (out of range). So in the case your array is larger than the heap size. E.g. A.lengh $`\neq`$
  * So once you hit the leaf nodes you do not call the algorithm recursively again
* Or key of the child A[child] is smaller than largest 

&rarr; Remember this algo only works with Max-Heaps, thus it works only if there was one modification to the heap such as the the value change in the any internal node or the root root to a number smaller than the children. Thus the left and right sub-trees are still max heaps.

# 49:43
</details>

<details>
<summary> What is the worst case of Max-Heapify</summary>
<br>
When the heap property is violated by the root while at the same time the root holds the smallest number (key) in the entire heap. Thus the entrie tree must be explored from the top to the bottom. The height of the tree is O(log n)
</details>


<details>
<summary>What is the running time of Max-Heapify?</summary>
<br>


</details>

<details>
<summary>Why is the upper bound for MH log n?</summary>

* Because in the worst case we have to go from the root to the leave swapping in each instance. This is identical to the height of the tree which is also $\lfloor log n \rfloor$
* If you define the theight of the tree as $h=O(logn)$ you may also say the run time is $O(h)$

<br>
</details>

<details>
<summary>How to build a heap from an array?</summary>

* When we build a heap from an array the $Heapsize = A.length$ 
  * Keep in mind that heaps can be modified which is why after some operations the Heapsize might be smaller than the original $A.length$
  * The heap size is dynamic, the array size is not
* Given an array of $n$ elements - we have to rearrange its elements in a way that satisfy the Max-Heap property
* We have to add internal nodes left to right starting with the next highest values
  * All left children will hold keys of indices $2i$
  * All right children will hold keys of indices $2i+1$
* The leaves are the elements from $A.length/2 + 1$ to the end of $A.lengh$ 
  * We don't want to analyse the leafs
* We start by looking only at the internal nodes $$Nodes_internal = 1 ... \lfloor A.length/2 \rfloor$$
  * Here we treat the last intearnal nodes before the leafs as subtrees where the last internal node is the root of the subtree.
  * Thus we want to start at the last internal nodes $\lfloor A.length \rfloor downto 1$

<br>
</details>

<details>
<summary>Why does the algorithm go from the last internal node y to the top (the root)?</summary>

* First of all because the leaves are defined as $\lfloor A.length/2 \rfloor + 1 to n $ - because the leaves have no children ;)
  * The last internal node has the last children
  * The leaves are the stopping condition
* We are working only on subtrees 
* A requirement of Max-Heapify is that all my subtrees are max-heaps
  * By working on subtrees of 3 nodes (1 parent 2 children) we can be sure that the violation is just in one place

<br>
</details>

<details>
<summary>What is cost of Max-Heapyfy on a node?</summary>

* It is proportional to the height of the node in the tree
* The worst case is always the height of that internal node, that is treated as a root at a given i ("rooted at a given i")
* The closer you are to the root, the higher the cost
* For every level i we have the cost of Max-Heapify plus the number of nodes that are present in a given level
  
Ch-06 s 20


<br>
</details>

<details>
<summary>Why h = h - i ?</summary>

* Cate?
<br>
</details>

<details>
<summary>What is the level of a tree?</summary>

* Cate?
 
<br>
</details>

<details>
<summary>What is the complexity of building a Max-Heap?</summary>

* Its a linear time operation

<br>
</details>

<details>
<summary>What is the complexity of Max-Heapify?</summary>

* Its a $log n$ time operation

<br>
</details>

<details>
<summary>How can we use heaps to do sorting?</summary>

* We will build a Max-Heap from a given array of elements, using *Build-Max-Heap*
* Then we exploit the *Max-Heap-property* once we have a Max-Heap
    * We take the largest element, knowing that we'll always find it in the root
    * Thus, we take this largest element and put it into the last position (**i**) in the array
    * Hence we must reduce the heapsize by one
    * Restore the Max-Heap-property and continue in the same way
        * Thereafter we have to replace the key of the root that was moved with one of the other elements of the heap
    * We stop when the heap-size = 1

<br>
</details>

<details>
<summary>How can we use heaps to do sorting (different wording)?</summary>

* We will build a Max-Heap from a given array of elements, using *Build-Max-Heap*
* Then we exploit the *Max-Heap-property* once we have a Max-Heap
* We take the largest element, knowing that we'll always find it in the root and place it in the *last position* *i* of the array
* We 'discard' the last node by reducing the heapsize by one 
* We cal **Max-Heapify" on the new root to mainting (restore) the *max-heap-property*
* We have to replace the key of the root that was moved with one of the other elements of the hea
    * We repeat the process until the heap contains only one node

<br>
</details>

<details>
<summary>What is the running time of Heapsort?</summary>

* Build-Max-Heap(A)
    * O(n)
* Loop is executed n times but contains Max-Heapify
   * O(log n)
   * The runtime for the loop is therefore O(n log n)
 * Total runtime of the algo is O(n log n) + O(n) but as the first term is dominating the short answer is:

The runtime of Heapsort is O(n log n)

<br>
</details>

<details>
<summary>Why do we not define the theta bound runtime for Heapsort?</summary>

* Because the built in algorithms 
    * Build-Max-Heap
    * Max-Heapify 
* Cannot be defined in terms of thetha

<br>
</details>

<details>
<summary>What is the difference of complexity of Merge sort and Heap sort?</summary>

* MS: For sure n log n
* HS: can be better than n log n
<br>
</details>

<details>
<summary>What a Priority-Queue?</summary>

A Priority Queue is a data structure for maintaining a set of *S* elements, each with an **associated priority value** called a **key**.

<br>
</details>

<details>
<summary>What operations are supported by Max-priority queues?</summary>

1. Return the element of **S** with the largest key
2. Remove and return the element of **S** with the largest key
3. Increase the value of an element x's key to k, assuming $k \geq key_current$ at value x
4. Insert an element x into set **S**

<br>
</details>

<details>
<summary>When do we use priority queues?</summary>

* Hospitals
* Job scheduling on a computer
    * A max-priority queue keeps track of the jobs to be performed 
    * When a job is finished/interrupted;
        * Job with the highest priority is selected adding a new job to the queue
* Can be implemented with a max-heap
    * Jobs in the priority queue correspond to the nodes in the heap
  
<br>
</details>

<details>
<summary>What is the difference between Heap-Extract-Max and Heap-sort?</summary>

* Cate?

<br>
</details>
<br>

# 06L Ch 7 & 8

<details>
<summary>What is the difference between Merge sort and Quick sort?</summary>

* In Merge sort the dividing step is trivial
    * Because we just calculated the middle index of the array, which was enough to merge sort the left and the right part
  * The Combining step is the dificult part solved by the 'merge' algorithm, which was the main driving force of the algo
  
* In Quick sort the combination step is trivial
* The main work is in the dividing step
    * A[p..q-1] <= A[q] <= A[q+1..r]
        * A[q] is NOT the middle of the array!
        * Further here we are not really dividing but **partitioning**
        * Because we find the element A[q] and then all elements to its left need to be smaller while all elements to its right need to be larger than A[q]

<br>
</details>

<details>
<summary>Why is the combining part of quick sort so easy?</summary>

* This is because
    * Each element of the left subarray is by definition $\leq$ A[q]
    * And each element of the right subarray is by definition $\geq$ A[q]
* Thus the combination of the two subarrays will be very easy as none of the elements left or right to A[q] need to be moved anymore. They are already were they should be

<br>
</details>

<details>
<summary>Quicksort &rarr; Why do we initialize i = p - 1?</summary>

* Because A[p..i] contains the elements that are less than or equal to x
* If i was defined initially as p, then there would be just ONE element that is lesser than or equal to x 
* In order to start with an empty array we have to start with i = p -1
 
<br>
</details>

<details>
<summary>What is a set?</summary>

* Each element can occur only once
* The elements are not ordered
* The number of elements in a set S is the cardinality of the set $(|S|)$
    * If the cardinality if a natural number, then the S is a finite set 
    * Otherwise it is infinite

<br>
</details>

<details>
<summary>Pseudo code of Quicksort</summary>

&rarr; initial call of Quicksort takes A, 1 and A.lenght

```
Quicksort(A,p,r) 
1   if p < r
2         q = Partition(A,p,r)
3         Quicksort(A, p, q - 1) // left array with each el <= x
4         Quicksort(A, q + 1, r) // right array with each el >= x
```

<br>
</details>

<details>
<summary>Pseudo code of Partition?</summary>

```
Partition(A, p, r)
1 x = A[r]
2 i = p - 1
3 for j = p to r - 1  // first j starts at p = 1, loop ends at second last element
4     if A[j] <= x
5         i = i + 1
6         exchange A[i] with A[j]   // Moves A[j] <= x to left sub array 
7 exchange A[i + 1] with A[r]   // move x in position A[q]
8 return i + 1    // corresponding to q, nedded as input for recursive calles of Quicksort (line 3 and 4)
```

<br>
</details>

<details>
<summary>Best case of Quick-sort?</summary>

* Balanced partitioning, meaning that we will have 2 regions
    * One of size n/2
    * The other one of size n/2-1
* The recurrence is calcuated as follows:
* $T(n) = 2T(n/2)+\Theta(n)=\Theta(n log n)$ (same as merge sort)

<br>
</details>

<details>
<summary>Worst case of Quick-sort?</summary>

* Maximally unbalanced set:
    * One region has 0 elements and the other one has n - 1 elements
    * When the array is already sorted
    * When all elements are smaller than 8
* Running time of $\Theta(n^2)$

<br>
</details>

<details>
<summary>Average case of Quicksort</summary>

* All permutations of the input numbers are equally likely
* On a random input array, we will have a **mix** of well balanced and unbalanced splits
    * Because it is unrealistic that each split happenes in the same way
* Good and bad splits are randomly distributed throughout the tree
    * E.g. $(n-1)/2-1$ on one branch and $(n-1)/2$ on another branch
* This leads to the average case running time still being $\Theta(n log n)$ which is close to the best case running time!

<br>
</details>

<details>
<summary> Quick sort explained by GeeksforGeeks:</summary>

* Sortingalgo using the idea of divide and conquer
* Finds element that is called **pivot** which divided the array in two
* The left part of the array holds elements smaller or equal than **pivot** (x)
* The right holds elements strictly larger than the **pivot**
  
* We recursively perform three steps
    
1. Bring the pivot to its apropriate position such that left of the pivot is smaller and right is greater
2. Quick sort the left part
3. Quick sort the right part
  
* The counter variables are 
* *i* index of the smaller el
* j loop variable
* Test condition:
    * arr[j] <= pivot
    * if true
        * Swap(arr(i), arr(j))
    * else next iteration of for

<br>
</details>

<details>
<summary>What does the theorem say about running time of comparison based sort algos?</summary>

* Any comparison based sort algorithm requires $\Omega(n log n)$ comparisons in the **worst case**
* We can proof that by constructing a tree and check how many leaves *l* it has:
 * The tree will have at least $n!$ leaves &rarr;  $n!$ permutations of the input appearing as some leaf $\Rightarrow n! \leq l$
 * The tree will have at most $h^h$ leaves
 * $\Rightarrow n! \leq l \leq 2^h$
 * $\Rightarrow h \geq lg(n!) = \Omega(nlgn)$
 * *h* is the height of the tree

<br>
</details>


#### Comparison of Sorting Algorithms

<details>
<summary>Running time of insertion sort?</summary>

* Worst case: $\Theta(n^2)$ 
* Best case: $\Theta(n)$
* Sorts **in place**

<br>
</details>

<details>
<summary>Running time of merge sort?</summary>

* Worst case: $\Theta(n log n)$ 
* Best case: $\Theta(n log n)$ 
* Best and worst are the **same**
* But it does **not** sort in place
  * It creates additional arrays that require additional space 

<br>
</details>

<details>
<summary>Running time of heap sort?</summary>

* Worst case: $\Theta(n log n)$ 
* Best case: $\Theta(n log n)$ 
* Sorts **in place**

<br>
</details>

<details>
<summary>Running time of quick sort?</summary>

* Worst case: $\Theta(n^2)$ 
* Best case: $\Theta(n log n)$ 
* Sorts **in place**

<br>
</details>

<details>
<summary>Which of the previously mentioned sorting algo(s) are sorting in place?</summary>

1. Insertion sort
2. Heap sort
3. Quick sort 

<br>
</details>

<details>
<summary>Which sorting algo(s) does **not** sort in place?</summary>

*  Merge sort

<br>
</details>

<details>
<summary>Which algo has the fastest best-case?</summary>

* Insertion sort: $\Thetha(n)$  

<br>
</details>

<details>
<summary>Template</summary>

* 

<br>
</details>