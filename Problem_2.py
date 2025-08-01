'''
23 Merge K sorted lists
https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

Solution:
Let  K = number of lists, N = avg length of list
1. Brute Force:
Traverse each linked list, store all the node values in a
a new array (size = NK), sort array and make a linked list out of it.
Time: O(NK log NK), Space: O(NK)

2. Min Heap: Add the head node of each list to a heap and heapify it. The head nodes in the heap will be reordered according to their node values. This is achieved by defining the dunder __lt__(self, other) in the class ListNode.
Then pop an item (say popped_node) from the heap and add it to the tail of the merged list. At the same time, push popped_node.next to the heap and heapify it.
https://youtu.be/PcrRJAwruKg?t=4068

Complexity: The size of the heap is K, and we push/pop NK elements into the heap.

Time: O(NK log K), Space: O(K)
'''
from linked_list import *
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeKLists(lists): # lists is a list of head nodes of linked lists
    if not lists:
        return None
    heap = []
    heapq.heapify(heap)
    dummy = ListNode(-1)
    for sll in lists:
        if sll:
            heapq.heappush(heap, sll)
    curr = dummy
    while heap:
        popped_node = heapq.heappop(heap)
        if popped_node.next:
            heapq.heappush(heap, popped_node.next)
        curr.next = popped_node
        curr = curr.next
    return dummy.next

def run_mergeKLists():
    tests = [([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
             ([], []),
             ([[]], [])]
    for test in tests:
        lists, ans = test[0], test[1]
        slls = []
        head_merge_sll = []
        print("\n")
        for i, arr in enumerate(lists):
            slls.append(build_linked_list(arr))
            if slls[i]:
                print(f"Linked List {i} = {slls[i].to_array()}")
            else:
                print(f"Linked List {i} = None")
        head_merge_sll = mergeKLists(slls)
        if head_merge_sll:
            merged_list = head_merge_sll.to_array()
        else:
            merged_list = []
        print(f"Merged Linked List = {merged_list}")
        success = (ans == merged_list)
        print(f"Pass: {success}")
        if not success:
            return

run_mergeKLists()