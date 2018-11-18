import queue as Q




q = Q.PriorityQueue()
q.put((-8,(222)))
q.put((-9,10))
q.put((-92,10))
# print(q.get_nowait())
# print(q.get_nowait())
# print(q.get())
print(q.queue[0])
q.qsize()
q.put((-7,0))
print(q.queue[0][0] < -7)