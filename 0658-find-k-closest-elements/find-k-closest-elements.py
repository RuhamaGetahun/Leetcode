class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            distance = abs(num - x)

            if len(heap) < k:
                heapq.heappush(heap, (-distance, -num))
            elif distance < -heap[0][0] or (distance == -heap[0][0] and num < -heap[0][1]):
                heapq.heappushpop(heap, (-distance, -num))

        result = sorted([-p[1] for p in heap])
        return result    


        