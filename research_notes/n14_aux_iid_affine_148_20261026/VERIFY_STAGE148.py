#!/usr/bin/env python3
"""Stage148 author exact finite evidence. Python stdlib; no floating-point arithmetic.

External ternary iid N=14. All ordered prefix policies are covered by
the universal Bellman lower bound; literal prefix DFS verifies chosen witnesses.
This is not native Heartbeat/P000 research admission.
"""
from fractions import Fraction as F
from collections import defaultdict

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(15834013488,41571575)
L=F(15595845464,41571575)
T=(7,1,2)
B=(11,0,1)
STATES=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s):
    n,a,b=s
    return (n+1,a+1,b),(n+1,a,b+1),(n+1,a,b)
def likelihood(s):
    return F(2**(s[1]+s[2]),3**s[1])

bellman={}
strict={}
ties=[]
gaps=[]
for s in reversed(STATES):
    opts={"P":K*likelihood(s),"Q":L}
    if s[0]<N:
        opts["C"]=F(1)+sum((P[i]*bellman[t] for i,t in enumerate(child(s))),F())
    minimum=min(opts.values())
    bellman[s]=minimum
    strict[s]=next(k for k,x in opts.items() if x==minimum)
    if sum(x==minimum for x in opts.values())>1:
        ties.append((s,tuple(k for k,x in opts.items() if x==minimum)))
    gaps.extend(x-minimum for x in opts.values() if x>minimum)

assert len(STATES)==680 and len(gaps)==1238
assert set(ties)=={(T,("Q","C")),(B,("Q","C"))}
assert min(gaps)==F(2016649859,121222712700)
ROOT=F(16707106935800437885154981,60728334498563346137088)
assert bellman[0,0,0]==ROOT

def action(s,v,b):
    if s==T: return "Q" if v else "C"
    if s==B: return "Q" if b else "C"
    return strict[s]

def backward(v,b):
    observer={}
    for s in reversed(STATES):
        act=action(s,v,b)
        if act=="P": y=(F(0),F(1),F(0),F(0))
        elif act=="Q": y=(F(1),F(0),F(0),F(0))
        else:
            suffix=[observer[t] for t in child(s)]
            y=tuple((F(1) if j>=2 else F(0))+
                    sum(((P if j%2==0 else Q)[i]*suffix[i][j]
                         for i in range(3)),F()) for j in range(4))
        observer[s]=y
    return observer[0,0,0]

def literal_ordered_prefix_DFS(v,b):
    # Probability weights are exactly P=(3,1,20)/24 and Q=(1,1,10)/12.
    stack=[(0,0,0,1,1)]   # length, count A, count B, P numerator, Q numerator
    total=[0]*4
    hits=defaultdict(lambda:[0,F(0),F(0)])
    visited=0
    while stack:
        n,a,c,x,y=stack.pop()
        s=(n,a,c)
        visited+=1
        if s in (T,B):
            hits[s][0]+=1
            hits[s][1]+=F(x,24**n)
            hits[s][2]+=F(y,12**n)
        act=action(s,v,b)
        if act=="C":
            assert n<N
            stack.extend(((n+1,a+1,c,x*3,y),
                          (n+1,a,c+1,x,y),
                          (n+1,a,c,x*20,y*10)))
        else:
            X=x*24**(N-n)
            Y=y*12**(N-n)
            if act=="Q": total[0]+=X
            if act=="P": total[1]+=Y
            total[2]+=n*X
            total[3]+=n*Y
    outcome=tuple(F(total[j],(24 if j%2==0 else 12)**N) for j in range(4))
    return outcome,visited,hits

CORNER={}
HITS={}
VISITED=[]
for v,b in ((0,0),(1,0),(0,1),(1,1)):
    literal,visited,hits=literal_ordered_prefix_DFS(v,b)
    assert literal==backward(v,b)
    CORNER[v,b]=literal
    HITS[v,b]=hits
    VISITED.append(visited)
assert VISITED==[583684,567934,583552,567802]
for hits in HITS.values():
    assert hits[T]==[70,F(21875,2985984),F(21875,1119744)]
    assert hits[B]==[11,F(107421875,1451188224),F(107421875,725594112)]

sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
M00=CORNER[0,0]
dT=sub(CORNER[1,0],M00)
dB=sub(CORNER[0,1],M00)
assert sub(sub(CORNER[1,1],CORNER[1,0]),dB)==(F(0),)*4
assert dT==(F(1191246875,9393093476352),
            -F(1878471875,20061226008576),
            -F(377661353125,31701690482688),
            -F(44855715625,1671768834048))
assert dB==(F(4619140625,2229025112064),
            -F(751953125,417942208512),
            -F(25673828125,278628139008),
            -F(17939453125,104485552128))
v0=(M00[1]-M00[0])/(dT[0]-dT[1])
vb=(dB[1]-dB[0])/(dT[0]-dT[1])
assert v0==F(8421218673713991,463750360640000)
assert vb==-F(25449600000,1449219877)
bstar=(1-v0)/vb
assert bstar==F(7957468313073991,8143872000000000)
assert 0<bstar<1
assert v0+vb==F(39620953387713,66250051520000)
assert v0+vb*bstar==1
def observer(b):
    v=v0+vb*b
    return tuple(M00[i]+v*dT[i]+b*dB[i] for i in range(4))
start=observer(F(1))
end=observer(bstar)
alpha147=F(246608842944125560263775,708830536865346112978944)
V147=F(273961171711816388948994643,22682577179691075615326208)
alpha148=F(6124245463802993075,17602807464179269632)
V148=F(35426720708566621357,2933801244029878272)
eta=F(38745474256605512970875,10933002200611098446587232256)
assert start[0]==start[1]==alpha147 and start[2]==V147
assert end[0]==end[1]==alpha148 and end[2]==V148
assert alpha148-alpha147==eta>0
assert start[2]-start[3]==F(386586105152287841810345,840095451099669467234304)>0
assert end[2]-end[3]==F(36781979533221897065,79212633588806713344)>0
for m in start,end:
    assert m[2]+L*m[0]+K*m[1]==ROOT
assert V147-V148==(K+L)*eta
assert K>0 and L>0
print("PASS_STAGE148_EXACT_FULL_REAL_INTERVAL_AND_SHARP_SUPPORT")
print("680 states, 1238 positive gaps, two count-state ties, four rational/DFS corner matches")
print("DFS nodes",VISITED)
print("alpha148",alpha148,"V148",V148,"eta148",eta,"slope148",K+L)
print("B saturation endpoint b=",bstar,"T saturated v=1")
