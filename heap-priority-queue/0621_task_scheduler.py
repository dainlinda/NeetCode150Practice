from typing import List
from heapq import heapify, heappop, heappush
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curr_time = 0
        task_freq = Counter(tasks)
        max_heap = [[-val, key] for key, val in task_freq.items()]
        heapify(max_heap)
        task_q = deque()  # task, time available

        while task_q or max_heap:
            # update time to match the next available task in q
            if not max_heap:
                curr_time = task_q[0][0]
            else:
                # process the most frequent task
                neg_freq, task_name = heappop(max_heap)
                neg_freq += 1  # decrement its frequency
                curr_time += 1  # processed

                # hold it to q until it becomes available
                if neg_freq < 0:  # still valid
                    task_q.append([curr_time + n, [neg_freq, task_name]])

            if task_q and task_q[0][0] == curr_time:
                _, task = task_q.popleft()
                heappush(max_heap, task)
        return curr_time


if __name__ == "__main__":
    sol = Solution()
    answer = sol.leastInterval(["A", "A", "A", "B", "C"], 3)
    print(
        f"The minimum number of CPU cycles required to complete all tasks is {answer}"
    )  # 9
