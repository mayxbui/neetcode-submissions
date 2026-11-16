# input list strs
# output list of list str that are anagram, in any order
# questions:
    # how to handle empty list? no (1<=str.length)
    # handle empty string? valid, return the string [[""]]
    # duplicate words? can be, appear in same group
    # uppercase? no
    # are all strings in the same size? no, can be any size from 0-100 (strs[i].length from 0-100)
        # ["may","kat","amy",,"mail","liam","tat"]


# approach 2:
# create a dictionary that store key sorted(string): value list of anagrams {sorted(string):list}
# loop over each string:
    # store key as sorted string
    # if key is new, store string in key:[string]
# return values of dict in a list [[...],[...]] 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            dict.setdefault(key,[]).append(i)
        return list(dict.values())


# approach 1:
# sort each string sorted(strs[i]) --time: O(NlogN), space O(N) for n char in a string
# list of list ana-groups
# for i in strs:
    # if strs[i] already in ana-groups
        # continue
    # for j in strs:
        # if strs[i] == strs[j], append strs[j] to same-list
    # append same-list to ana-group
# return ana-group
# time: O(N^2) pairwise loop
# space: O(N) as N lists in ana-group

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if len(strs)==1:
        #     return [strs]
        # sorted_list=[]
        # for i in strs:
        #     sorted_list.append("".join(sorted(i)))
        # ana_group = []
        # visited = set() # track visited indices
        # for i in range(len(strs)):
        #     if i in visited:
        #         continue
        #     group = []
        #     for j in range(i,len(strs)):
        #         if sorted_list[i]==sorted_list[j]:
        #             group.append(strs[j])
        #             visited.add(j)
        #     ana_group.append(group)
        # return ana_group
        