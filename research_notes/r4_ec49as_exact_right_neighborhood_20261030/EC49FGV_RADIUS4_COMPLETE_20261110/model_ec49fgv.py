"""Frozen original 9-state BRC observer and signed native X6 path enumerator."""
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def words(h,key):
    x,y,z=key
    a=z-1; b=x+y-h-1; f=h+1-y-2*z; g=h+1-x
    if min(a,b,f,g)<0:return
    for c in range(b+1):
        n=[a,c,b-c,z,f,g]
        def walk(w,q):
            if len(w)==h:
                if SIG[q] in REQ[h]:yield SIG[q],w
                return
            for j,op in enumerate(OPS):
                if n[j] and T[q][j]!=8:
                    n[j]-=1
                    yield from walk(w+op,T[q][j])
                    n[j]+=1
        yield from walk('',0)

def check(W):
    seen=set();keys=set();labels=set()
    for h,s,w in W:
        assert len(w)==h
        assert (h,s) not in labels;labels.add((h,s))
        pos=[0]*6;q=0;path=()
        for op in w:
            q=T[q][OPS.index(op)];assert q!=8
            for ax in STEPS[op]:
                pos[abs(ax)-1]+=1 if ax>0 else -1
                path+=(ax,);seen.add(path)
        assert SIG[q]==s and pos==[2,0,0,0,0,0],(h,s,w,SIG[q],pos)
        keys.add(tuple(sum(a==v for a in path) for v in (1,2,3)))
    assert labels=={(h,s) for h in REQ for s in REQ[h]}
    return len(seen),sorted(keys)
