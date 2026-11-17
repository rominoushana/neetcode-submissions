class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        list_of_anagrams = defaultdict(list)

        for string in strs:
            subList = [0] * 26
            for char in string:
                subList[ord(char) - ord("a")] += 1
            list_of_anagrams[tuple(subList)].append(string)
        
        return list(list_of_anagrams.values())