"""Independent exhaustive full-observer future tree check for Stage458-B.
Budget scopes intentionally small. Future APPEND uses all 12 signed X6 directions.
"""
import itertools, functools, json, sys
sys.path.insert(0,'/mnt/data')
from STAGE458B import words, oracle
D=tuple((axis,sgn) for axis in range(6) for sgn in (-1,1))
A=(0,1);B=(0,-1)
def observer(p,q):
 def v(x):
  t=[0]*6
  for a,sgn in x:t[a]+=sgn
  return tuple(t)
 def J(x):
  return tuple(sorted((pair,n) for pair,n in __import__('collections').Counter(zip(x,x[1:])).items()))
 return len(p),len(q),v(p),v(q),J(p),J(q),sum(a==b for a,b in zip(p,q))
@functools.lru_cache(None)
def tree(p,q,b,rp,rq):
 children=[]
 if b and q:children.append(('QPOP',tree(p,q[:-1],b-1,rp,rq)))
 if rp:
  for d in D:children.append((('PAPP',d),tree(p+(d,),q,b,rp-1,rq)))
 if rq:
  for d in D:children.append((('QAPP',d),tree(p,q+(d,),b,rp,rq-1)))
 return (observer(p,q),tuple(children))
def tokenkey(p,q,m,n,b,rp):
 u=n-b;t=min(n,m+rp)
 if u>=m:
  S=sorted(set([m] if u==m else []) | {i for i in range(m+1,n+1) if i<=t or i>=u})
  return tuple(str(q[i-1]==B) for i in S)
 return tuple(([str(q[u-1]==B)] if u else []) + [str(p[i-1]==B)+str(q[i-1]==B) for i in range(u+1,m+1)] + [str(q[i-1]==B) for i in range(m+1,n+1)])

def main():
 checked=0;hist=0;pairs=0;all_positions=set()
 for m,n in [(3,4),(3,5),(4,5),(4,6)]:
  for kp in range(min(1,(m-2)//2)+1):
   for kq in range(min(2,(n-2)//2)+1):
    for d in range(0,3):
     for b in range(0,min(n,3)+1):
      for rp,rq in [(0,0),(1,0),(0,1),(1,1)]:
       xs=[(tuple(A if x==0 else B for x in p),tuple(A if x==0 else B for x in q)) for p in words(m,kp) for q in words(n,kq) if sum(i!=j for i,j in zip(p,q))==d]
       if not xs:continue
       keys=[tokenkey(p,q,m,n,b,rp) for p,q in xs]
       trees=[tree(p,q,b,rp,rq) for p,q in xs]
       for i in range(len(xs)):
        for j in range(i+1,len(xs)):
         assert (keys[i]==keys[j])==(trees[i]==trees[j]),(m,n,kp,kq,d,b,rp,rq,xs[i],xs[j])
         pairs+=1
       checked+=1;hist+=len(xs);all_positions.add('c<m' if n-b<m else 'c=m' if n-b==m else 'c>m')
 print(json.dumps({'marker':'STAGE458B_FULL_NATIVE_FUTURE_TREE_PASS','fibers':checked,'histories':hist,'pairs':pairs,'boundaries':sorted(all_positions),'native_append_directions':12,'cached_full_trees':tree.cache_info().currsize},indent=2))
if __name__=='__main__':main()
