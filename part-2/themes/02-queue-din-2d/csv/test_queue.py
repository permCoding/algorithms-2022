import queue


q = queue.Queue()
for i in range(9):
    q.put(i)

# for _ in range(q.qsize()):
#     print(q.get())

while not q.empty():
    print(q.get())
