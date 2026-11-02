
from collections import deque

queue = deque([((0,0), [])])
visited = set()

while queue:
    (a,b), path = queue.popleft()

    if (a,b) in visited:
        continue

    visited.add((a,b))
    path = path + [(a,b)]

    if a == 2:
        print("Solution Path:")
        for i in path:
            print(i)
        print("Goal Reached")
        break

    next = [
        (4,b),
        (a,3),
        (0,b),
        (a,0),
        (max(0,a-(3-b)), min(3,a+b)),
        (min(4,a+b), max(0,b-(4-a)))
    ]

    for state in next:
        if state not in visited:
            queue.append((state,path))
