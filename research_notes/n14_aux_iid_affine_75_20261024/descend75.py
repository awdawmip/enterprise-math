from collections import defaultdict
from math import factorial
import verify_n14_75 as m

def routed_stop():
 # each state tracks counts of ordered prefixes whose first stop occurs here,
 # and those that have passed A while alive, under old policy.
 current={(0,0,0):1} # (a,b,viaA); 0 no, 1 yes
 stopby=defaultdict(lambda:[0,0]); total_firsthit=0
 for n in range(m.N+1):
  nxt=defaultdict(int)
  for (a,b,via),k in current.items():
   st=(n,a,b)
   if st==m.A:
    assert via==0
    via=1;total_firsthit+=k
   z=m.act(st)
   if z!='C':
    stopby[(st,z)][via]+=k
    continue
   for i in range(3):nxt[(a+(i==0),b+(i==1),via)]+=k
  current=nxt
 assert not current
 return stopby,total_firsthit
if __name__=='__main__':
 stops,hit=routed_stop()
 print('A FIRSTHIT COUNT',hit)
 print('descendant first-stop states:')
 for (st,z),(other,via) in sorted(stops.items()):
  if via:print(st,z,other,via,'total',other+via)
 print('number',sum(x[1]>0 for x in stops.values()),'mass paths descendant',sum(x[1] for x in stops.values()))
