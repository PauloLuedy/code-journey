from queue import Queue
from collections import deque

q = Queue()

q.put(1)
q.put(2)
q.put(3)


for i in range(3):
  print(q.get())
