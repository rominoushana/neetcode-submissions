class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        output = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for i, j in count.items():
            freq[j].append(i)

        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                output.append(j)
                if len(output) == k:
                    return output
                
        