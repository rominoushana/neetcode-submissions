class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupAna = defaultdict(list)

        for string in strs:
            count = [0] * 26
            
            for char in string:
                count[ord(char) - ord("a")] += 1

            groupAna[tuple(count)].append(string)
        
        return list(groupAna.values())
            


        