# DataStructure

Just some practice about data structure

## ClassTest.py
*1 简单的类的声明和实例化

## LinkedList.py
*1 单向链表的实现，可以直接一个一个插入建，也可以直接用一个数组建
*2单向链表中节点的插入、删除、直接往后加

## BinarySearchTree.py
二叉搜索树的实现

插入节点，删除节点，找最小节点

## Graph-AdjacencyList.py
Implement Graph as the adjacency list format

Breadth-First Search的实现，输出一个Breadth-first Search Tree

Implement the Depth-first Search algorithm

Implement Bellman-Ford algorithm and output the shortest path

Bellman-Ford computes the shortest paths from a single source vertex to all of the other vertices in a weighted digraph.

比Dijkstra慢，但是能处理有负边的图；原理就是对每条边反复relax，若n-1次后还能更新，说明图中有负环

Dijkstra好难写，复杂度还不对，现在是O(n^3)

有一个关于self.Vertexes = [Vertex()] * size 赋值后，所有的list单元指向同一个地址的问题

好像是浅拷贝和深拷贝的问题
