# give int array nums, int k
# return k most frequent element in array, in any order
# questions/assumptions:
    # the k be 0? no
    # empty array? no
    # numbers can be negative? yes
    # numbers can be duplicate

# approach: dictionary
    # loop through the array and update the dict with {num: frequency}
        # time: O(N), space O(N) for n numbers
    # then return the most k frequent number by 
        # 1. sort the dict by freq and return k num 
            # time: O(NlogN) for sorting n numbers, space O(N)
        # 2. heapq.nlargest(k,dict.values()) -> return a list of top k number 
            # time: the heap never grows larger than k items because that's all it sees. it loop through N items in dict one by one. push/pop only hold K items O(logK) over N items -> O(N logK)
# time: O(NlogN), space O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i]=freq.get(i, 0) + 1
        return heapq.nlargest(k,freq.keys(), key=freq.get)

# nums = [1,2,2,3,3,3], k = 2
# loop through array and save in freq dictionary: time & space O(n)
    # i=1 -> freq={1:1}
    # i=2 -> freq={1:1,2:1}
    # i=2 -> freq={1:1,2:2}
    # i=3 -> freq={1:1,2:2,3:1}
    # i=3 -> freq={1:1,2:2,3:2}
    # i=3 -> freq={1:1,2:2,3:3}
# heap make a new list of sorted values decending 
    # heapq.nlargest(2,freq.keys(),key=freq.get): get 2 largest element sorted by values and return the list of them
    # time: O(n logk) which heap pop K items O(logK) over N items

