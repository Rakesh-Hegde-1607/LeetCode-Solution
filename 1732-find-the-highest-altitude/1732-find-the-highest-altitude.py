class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt=0
        maxalt=0
        for i in range(0,len(gain)):
            alt=alt+gain[i]
            maxalt=max(maxalt,alt)
        return maxalt

