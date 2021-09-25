# L 4 

- Solving recurrence equations for runtime analysis of recursive algorithms

<details>
<summary>How can you describe the running time of a recursive algorithm?</summary>
<br>
By a recurrence equation that describes a function in terms of its value on smaller input.
</details>

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