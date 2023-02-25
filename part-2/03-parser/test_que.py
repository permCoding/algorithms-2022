# import queue

# q = queue.Queue()
# for i in range(3): q.put(i)  # FIFO = queue
# for _ in range(q.qsize()): print(q.get())
# while not q.empty(): print(q.get())

# q = queue.LifoQueue()
# for i in range(3): q.put(i)  # LIFO = stack
# for _ in range(q.qsize()): print(q.get())

# --------------------------

from collections import deque

dq = deque()

for i in range(3): dq.append(i)
print('stack', dq)
for _ in range(len(dq)): print(dq.pop())

for i in range(3): dq.appendleft(i)
print('stack reverse', dq)
for _ in range(len(dq)): print(dq.popleft())

for i in range(3): dq.append(i)
print('queue', dq)
for _ in range(len(dq)): print(dq.popleft())

for i in range(3): dq.appendleft(i)
print('queue reverse', dq)
for _ in range(len(dq)): print(dq.pop())
