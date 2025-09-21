# real_inspect.py (snippet)
import tracemalloc

tracemalloc.start()
snap1 = tracemalloc.take_snapshot()

d = {}
for i in range(10000):
    d[i] = str(i) * 5

snap2 = tracemalloc.take_snapshot()
stats = snap2.compare_to(snap1, 'lineno')
for stat in stats[:10]:
    print(stat)
tracemalloc.stop()
