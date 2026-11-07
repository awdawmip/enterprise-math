"""Stage407-B: integer Euler/Dual BRC and finite two-letter trace certificate."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product
import json
A=1;B=-1;D=(A,B)
def j(w):return tuple(Counter(zip(w,w[1:])).get(e,0) for e in product(D,repeat=2))
def o(p,q):return (len(p),len(q),sum(p),sum(q),j(p),j(q),sum(x==y for x,y in zip(p,q)))
def E(s):return tuple(A if t=='A' else B for t in s)
def count_keys(p,edges,k):
    edges=tuple(edges.items())
    @lru_cache(None)
    def walk(pos,last,left,kk,tail):
        if pos==len(p):return {tail:1} if kk==k and all(z==0 for z in left) else {}
        out=defaultdict(int)
        for i,((u,v),n) in enumerate(zip((e for e,_ in edges),left)):
            if n==0 or last!=u:continue
            rr=list(left);rr[i]-=1
            for t,c in walk(pos+1,v,tuple(rr),kk+(p[pos]==v),(tail+(v,))[-4:]).items():out[t]+=c
        return dict(out)
    r=defaultdict(int)
    for first in D:
        for t,c in walk(1,first,tuple(n for _,n in edges),int(first==p[0]),(first,)).items():r[t]+=c
    return dict(r)
def equal(p,q,r,s):
    assert o(p,q)==o(r,s)
    start=(p,q,r,s,0,0,0); seen={start};todo=deque([start]);checks=0
    while todo:
        p,q,r,s,up,uc,run=todo.popleft()
        if run==4:continue  # proved 4-APP shield
        for act in [('APP',a,b) for a,b in product(D,repeat=2)]+[('POP',),('CAN',)]:
            k=act[0]
            if k=='POP' and up or k=='CAN' and uc:continue
            e1=e2=True
            if k=='POP':e1=bool(q);e2=bool(s)
            if k=='CAN':e1=len(p)>=2 and len(q)>=2 and p[-1]==-p[-2] and q[-1]==-q[-2];e2=len(r)>=2 and len(s)>=2 and r[-1]==-r[-2] and s[-1]==-s[-2]
            checks+=1
            if e1!=e2:return False,checks,len(seen),act
            if not e1:continue
            if k=='APP':a,b=act[1:];t=(p+(a,),q+(b,),r+(a,),s+(b,),up,uc,run+1)
            elif k=='POP':t=(p,q[:-1],r,s[:-1],1,uc,0)
            else:t=(p[:-2],q[:-2],r[:-2],s[:-2],up,1,0)
            if o(t[0],t[1])!=o(t[2],t[3]):return False,checks,len(seen),act
            if t not in seen:seen.add(t);todo.append(t)
    return True,checks,len(seen),None
def brc(end):
    d={(0,)*6:(1,1)}
    for _ in range(6):
        n=defaultdict(lambda:(0,0))
        for z,(c,w) in d.items():
            for i in range(6):
                for s in (-1,1):
                    x=list(z);x[i]+=s;x=tuple(x);cc,ww=n[x]
                    n[x]=(cc+c,ww+w*(2 if (i,s)==(0,1) else 3 if (i,s)==(0,-1) else 1))
        d=dict(n)
    return d.get(end,(0,0))
def main():
    p=E('AAAAAA');q=[E(x) for x in ('AABABA','ABAABA','ABABAA')]
    assert all(o(p,v)==o(p,q[0]) for v in q)
    counts=count_keys(p,Counter(zip(q[0],q[0][1:])),4)
    assert counts=={v[-4:]:1 for v in q}
    brute=[v for v in product(D,repeat=6) if o(p,v)==o(p,q[0])]
    assert set(brute)==set(q)
    t=[equal(p,q[i],p,q[j]) for i,j in ((0,1),(0,2),(1,2))]
    assert [v[0] for v in t]==[True,False,False]
    assert brc((6,0,0,0,0,0))==(1,64)
    assert brc((2,0,0,0,0,0))==(4665,32760)
    print(json.dumps({'status':'STAGE407B_EXACT_ASYNC_FIBER_PASS','fiber':3,'raw_keys':3,'minimal_states':2,'classes':[[0,1],[2]],'checks':t,'brcP':[1,64],'brcQ':[4665,32760]},sort_keys=True))
if __name__=='__main__':main()
