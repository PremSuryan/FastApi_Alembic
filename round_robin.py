"""
Round Robin problem 
input :
bursttime=[5,3,7]
quantum = 2 --->cpu execution level
"""

from collections import deque


def roundRobin(burstTime, quantum):
    queue =deque()
    print(type(queue))

    for i , burst in enumerate(burstTime):
        queue.append([i,burst])

    while queue:
        processId , remaining = queue.popleft()
        execution = min(remaining, quantum)

        remaining -= execution
        if remaining>0:
            queue.append([processId,remaining])

        else:
            print(f"Process {processId} is completed")

roundRobin([5,3,7], 2)