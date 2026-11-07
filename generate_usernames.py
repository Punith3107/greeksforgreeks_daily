class Solution:
    def generateUsernames(self, arr):
        used = set(arr)
        seen = set()
        ans = []
        count = {}

        for name in arr:
            if name not in seen:
                ans.append(name)
                seen.add(name)
            else:
                i = count.get(name, 1)
                while name + str(i) in used:
                    i += 1

                new = name + str(i)
                ans.append(new)
                used.add(new)
                seen.add(new)
                count[name] = i + 1

        return ans
