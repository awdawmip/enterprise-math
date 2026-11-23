#!/usr/bin/env python3
"""R284FZ: exact q=5 seven-pattern census and uniform stable-cut lifting.
All-q conclusion uses the proved 2-vertex cut induction, not finite extrapolation.
"""
PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
ADJ={(0,1),(0,3),(1,2),(2,3)}
BITS={p:(0,p&1,(p>>1)&1,(p>>2)&1) for p in range(1,8)}
LAST={}
for p in range(1,8):
    for i in range(4):
        for t in range(4):
            e=(i-1-t)%4
            if BITS[p][e]!=BITS[p][(e+1)%4]:
                LAST[p,i]=e
                break
CUTS={};DIST={};TWO={}
for i,j in PAIRS:
    edges=[(p,LAST[p,i],4+LAST[p,j]) for p in range(1,8)
           if BITS[p][i]!=BITS[p][j]]
    DIST[i,j]=tuple(p for p,_,_ in edges)
    best={}
    for s in range(1,256):
        mask=tuple(p for p,a,b in edges if s>>a&1 and s>>b&1)
        if mask: best[mask]=min(best.get(mask,9),s.bit_count())
    CUTS[i,j]=tuple(best.items())
    TWO[i,j]=tuple(mask for mask,t in CUTS[i,j] if t==2)

def compositions(total,parts):
    if parts==1:
        yield (total,)
        return
    for v in range(total+1):
        for tail in compositions(total-v,parts-1):
            yield (v,)+tail

def distance_ok(x,q):
    return all(sum(x[p-1] for p in DIST[i,j]) >=
               (2*q+5 if (i,j) in ADJ else 2*q+3)
               for i,j in PAIRS)

def stable_ok(x,q):
    return all(any(sum(x[p-1] for p in mask)>=q*t+3
                   for mask,t in CUTS[i,j]) for i,j in PAIRS)

def lift_ok(x,grow):
    return all(
        sum(p in DIST[i,j] for p in grow)>=1 and
        any(sum(x[p-1] for p in mask)>=13 and
            any(p in grow for p in mask)
            for mask in TWO[i,j])
        for i,j in PAIRS)

def lift(x,grow,q):
    return tuple(v+2*(q-5)*(p in grow) for p,v in enumerate(x,1))

def main():
    total=distance=0
    for k,expected,pure_expected,pair_counts in (
        (8,7,7,{(3,5):3,(3,6):1,(5,6):3}),
        (9,66,18,{(3,5):28,(3,6):10,(5,6):28})
    ):
        accepted=[]
        for x in compositions(20+k,7):
            total+=1
            if not distance_ok(x,5):continue
            distance+=1
            if stable_ok(x,5):accepted.append(x)
        assert len(accepted)==expected,(k,len(accepted))
        pure=sum(not any(x[p-1] for p in (1,2,4,7)) for x in accepted)
        assert pure==pure_expected
        groups={}
        for x in accepted:
            grow=tuple(p for p in (3,5,6) if x[p-1]>=12)
            assert len(grow)==2 and max(x[p-1] for p in (3,5,6)
                                      if p not in grow)<=3
            assert lift_ok(x,grow),(k,x)
            groups[grow]=groups.get(grow,0)+1
        assert groups==pair_counts,(k,groups)
        for q in (5,6,7,11,20,64):
            lifted=set()
            for x in accepted:
                grow=tuple(p for p in (3,5,6) if x[p-1]>=12)
                y=lift(x,grow,q)
                assert sum(y)==4*q+k
                assert distance_ok(y,q) and stable_ok(y,q),(k,q,x)
                assert tuple(p for p in (3,5,6)
                             if y[p-1]>=2*q+2)==grow
                lifted.add(y)
            assert len(lifted)==expected
        print('k=%s: exact q=5=%d, all-q lift groups=%s, pure=%d, mixed=%d'
              %(k,expected,groups,pure,expected-pure))
    assert total==2968064,total
    assert distance==73760,distance
    print('PASS: 7/66 all-q distinct stable-admissible templates for q>=5')

if __name__=='__main__':main()
