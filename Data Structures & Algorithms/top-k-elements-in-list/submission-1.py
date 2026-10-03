class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency ={

        }
        for n in nums:
            frequency[n] = frequency.get(n,0) +1
        
        result = sorted(frequency, key =frequency.get,reverse=True)

        return result[:k]
        

