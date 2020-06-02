from collections import defaultdict
import sys
string=input()
co= len(set(list(string)))
n = len(string)
dist = defaultdict(int)
first = 0
sl = sys.maxsize
he = 0 
for j in range(n):
    dist[string[j]] += 1
    if dist[string[j]] == 1:
        he += 1
        
    if co == he:
        while dist[string[first]] > 1:
            if dist[string[first]] > 1:
              dist[string[first]] -= 1
            first += 1
          
        cl = j - first + 1
        sl = min(sl, cl)
print (sl)
