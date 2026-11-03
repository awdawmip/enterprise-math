#!/usr/bin/env python3
"""EC49EXP: exact integer strong-suffix clique census for all H8/M5 triple-key schedules."""
from itertools import combinations
from collections import Counter
import json,time
HS=tuple(range(2,9))
def eligible(h):
    result={}
    for w in range(1,(h+1)//2+1):
        for u in range(2*h+3):
            for v in range(h+2):
                r=u+v-h-1
                f=h+1-v-2*w
                g=h+1-u
                if min(r,f,g)>=0 and (r>=1 or (r==0 and f>=1 and g>=1)):
                    result[(u,v,w)]=4 if r>=1 else 2
    return result
S={h:eligible(h) for h in HS}
assert [len(S[h]) for h in HS]==[1,4,9,17,28,43,62]
def cap(a,b):return 2*sum(min(a[i],b[i]) for i in range(3))-2
def bound(assign):
    groups={}
    for h,k in assign.items():
        groups.setdefault(k,[0,0,2*(sum(k)-1)])
        groups[k][0]+=1;groups[k][1]+=S[h][k]
    assert len(groups)==5
    keys=list(groups);length=[groups[k][2] for k in keys];m=[groups[k][1] for k in keys]
    edges={(i,j):cap(keys[i],keys[j]) for i in range(5) for j in range(i+1,5)}
    total=0
    for d in range(1,max(length)+1):
        q=[0 if d>L else (m[i] if d>=L-2 else 1) for i,L in enumerate(length)]
        best=0
        for mask in range(1,32):
            ids=[i for i in range(5) if mask>>i&1 and q[i]>0]
            if all(edges.get((i,j),-1)<d for i,j in combinations(ids,2)):
                best=max(best,sum(q[i] for i in ids))
        total+=best
    return total
def main():
    hist=Counter();rows=[];t=time.monotonic()
    for triple in combinations(HS,3):
        singles=[h for h in HS if h not in triple];cnt=Counter()
        common=set.intersection(*(set(S[h]) for h in triple))
        for shared in common:
            assign={h:shared for h in triple}
            def walk(i,used):
                if i==4:
                    b=bound(assign);hist[b]+=1;cnt[b]+=1;return
                h=singles[i]
                for k in S[h]:
                    if k in used:continue
                    assign[h]=k;walk(i+1,used|{k})
                assign.pop(h,None)
            walk(0,{shared})
        if cnt:
            rows.append({'windows':list(triple),'schedules':sum(cnt.values()),
               'min_lb':min(cnt),'max_lb':max(cnt),
               'excluded_lt80':sum(v for k,v in cnt.items() if k>=80),
               'excluded_le80':sum(v for k,v in cnt.items() if k>80)})
    assert sum(hist.values())==123147
    assert sum(v for k,v in hist.items() if k>=80)==106924
    print(json.dumps({'status':'PASS','triple_schedules':sum(hist.values()),
      'excluded_lt80':106924,'survivors_lt80':16223,
      'histogram':dict(sorted(hist.items())),'per_triple':rows,
      'elapsed_s':round(time.monotonic()-t,3)},indent=2))
if __name__=='__main__':main()
