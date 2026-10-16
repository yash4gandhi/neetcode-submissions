class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) < 2:
            return [strs]

        dic = {}

        for s in strs:
            sortedS = ''.join(sorted(s))

            if sortedS in dic:
                dic[sortedS].append(s)
            
            else:
                dic[sortedS] = [s]

        result = []

        for val in dic:
            result.append(dic[val])

        return result
