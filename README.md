# Interview question explanations

I figured since I spent so much time interviewing and preparing for various companies that I may as well document some of my undertakings.

You can consume my content one notebook at a time. All programming is done in Python 3.

If you just want to read my other ramblings 😅, feel free to [check out my blog](https://medium.com/attenchen-to-detail).

## misc heuristics

- sliding window/running counter/"pick up and process new, remove old" method
- sort
- DP
- DFS/BFS/backtracking
- always look to reduce runtime complexity
- double pass in trees, first time to compute some value(s), second time to find some value(s)
- trees do not have loops/cycles
- some kind of prefix sum (both 1D and 2D, although 2D is a lot more annoying - can just be horizontal or both horizontal and vertical)
- anagrams -> can sort or use hashmap to identify

### case study of prefix sums

for the 1D version of prefix sum, the flavors usually have you find the minimum subarray of some condition (sums up to k, sum is greater than k, has k distinct integers, etc)

naive is to search through all the solutions which is N^2 solutions
with prefix sum computed, you can "prune" the solution space (the idea is that for each set of minimum subarrays starting at some index, you can prune the ones that are never going to be any better than some current minimum)

usually some other data structure is used like a hashmap or a priority queue to help prune

if negative numbers are involved, usually entering LC hard, otherwise LC medium
eg. [LC medium min subarray with sum > k](https://leetcode.com/problems/minimum-size-subarray-sum/) vs [LC hard min subarray with sum > k](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)

for the 2D version, you usually calculate some horizontal or vertical prefix sum for all the rows/cols and then mix and match to calculate/prune whatever condition is specified

### good packages to know

- SortedList (also includes bisect functionality)
- heapq (ie. `from heapq import heappush, heappop`)
- bisect (you can bisect a vanilla sorted list using this - ie. `from bisect import bisect_left`)

### regular sys design

- https://leetcode.com/discuss/interview-question/1061256/Tips-on-System-design-from-a-20%2B-YOE-Engineer
- https://leetcode.com/discuss/interview-question/1140451/Helpful-list-of-LeetCode-Posts-on-System-Design-at-Facebook-Google-Amazon-Uber-Microsoft
- https://leetcode.com/discuss/interview-question/system-design/318811/Google-or-System-design-or-Design-a-translation-service-like-Google-Translate
