class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_duration = 0
        for i in range(1, len(timeSeries)):
            total_duration += min(timeSeries[i] - timeSeries[i-1], duration)
        
        total_duration += duration
        
        return total_duration
