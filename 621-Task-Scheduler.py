class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = [0] * 26
        for t in tasks:
            task_count[ord(t) - ord('A')] -= 1
        task_heap = []
        for i in task_count:
            if i != 0:
                heapq.heappush(task_heap, i)
        time = 0
        while task_heap != []:
            tmp = []
            cnt = 0
            while cnt <= n:
                if task_heap != []:
                    t = heapq.heappop(task_heap) + 1
                    if t != 0:
                        tmp.append(t)
                time += 1
                cnt += 1
                if task_heap == [] and tmp == []:
                    break
            for t in tmp:
                heapq.heappush(task_heap, t)
                
        return time