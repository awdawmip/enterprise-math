#!/usr/bin/env python3
"""R23 exact 389-zero-increment certificate. Standard library only; no floats."""
from fractions import Fraction as Q
from bisect import bisect_left,bisect_right
LO=Q(262204504569236716045286,10**24)
HI=Q(262204504569236716045287,10**24)
M=128;END=1107
A=(-43,164);B=(59,-225);C=(102,-389);E=(145,-553);F=(-188,717);Z=(0,0)
def value(z,t):return z[0]+z[1]*t
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def add(x,y):return (x[0]+y[0],x[1]+y[1])
for th in (LO,HI):
 assert 0<value(F,th)<value(E,th)<value(A,th)<value(C,th)<value(B,th)
P=[(-(j*LO//1),j) for j in range(END)]
assert all(P[j][0]==-(j*HI//1) for j in range(END))
S=sorted(range(END),key=lambda j:value(P[j],LO))
assert S==sorted(range(END),key=lambda j:value(P[j],HI))
rank={j:k for k,j in enumerate(S)}
H=sorted(range(M),key=lambda j:rank[j])
HV=[value(P[j],LO) for j in H]
def gap(u,v):
 z=(P[v][0]-P[u][0]+int(rank[u]>rank[v]),v-u)
 assert all(0<value(z,t)<1 for t in (LO,HI))
 return z
def maxgap(rows):
 w=max((g for u,v,g in rows),key=lambda z:value(z,LO))
 assert all(value(w,HI)>=value(z,HI) for u,v,z in rows)
 return w
for th in (LO,HI):
 assert all((k*th)%1>value((-11,42),th) for k in range(-60,103) if k not in (0,42))
 assert all((k*th)%1>value((-27,103),th) for k in range(-24,128) if k not in (0,103))
 assert min(min((k*th)%1,1-(k*th)%1) for k in range(1,M))==value((16,-61),th)
for s in range(36):assert H[(H.index(25+s)+1)%M]==67+s
for s in range(25):assert H[(H.index(s)+1)%M]==103+s
for s in range(67):assert H[(H.index(61+s)+1)%M]==s
BKS=[
(492,25,0,A),(517,36,25,A),(553,67,61,E),(620,36,25,Z),
(656,25,0,E),(681,36,25,E),(717,25,0,Z),(742,36,25,Z),
(778,67,61,Z),(845,36,25,Z),(881,25,0,Z),(906,36,25,Z),
(942,67,61,Z),(1009,36,25,Z),(1045,25,0,Z),(1070,36,25,Z)]
assert sum(count for t,count,o,d in BKS)==614
assert all(BKS[i][0]==BKS[i-1][0]+BKS[i-1][1] for i in range(1,len(BKS)))
keys=sorted(rank[j] for j in range(M));cuts=[S[k] for k in keys]
arcs={j:[] for j in range(M)}
for k,u in enumerate(cuts):
 v=cuts[(k+1)%M];arcs[u]=[(u,v,gap(u,v))]
R=Z;hist={128:Z};base={}
for t in range(M,END):
 cur=next((row for row in BKS if row[0]<=t<row[0]+row[1]),None)
 if cur:
  t0,count,own0,expect=cur;own=own0+t-t0
  if t==t0:base[t0]=list(arcs[own0])
  assert arcs[own]==[(u+t-t0,v+t-t0,g) for u,v,g in base[t0]]
 pos=bisect_left(keys,rank[t]);u=cuts[pos-1] if pos else cuts[-1]
 v=cuts[pos] if pos<len(cuts) else cuts[0]
 own=H[(bisect_right(HV,value(P[t],LO))-1)%M]
 if cur:assert own==own0+t-t0
 old=arcs[own];before=(u,v,gap(u,v));assert before in old
 oldmax=maxgap(old)
 p=[(u,t,gap(u,t)),(t,v,gap(t,v))]
 assert add(p[0][2],p[1][2])==before[2]
 new=[]
 for row in old:
  if row==before:new.extend(p)
  else:new.append(row)
 arcs[own]=new
 delta=sub(oldmax,maxgap(new))
 if cur:assert delta==expect,(t,expect,delta)
 R=add(R,delta);hist[t+1]=R
 keys.insert(pos,rank[t]);cuts.insert(pos,t)
assert hist[492]==(-10432,39788)
assert hist[493]==(-10475,39952)
assert hist[553]==(-13055,49792)
assert hist[620]==hist[656]==(-3340,12741)
assert hist[717]==hist[1106]==(5505,-20992)
assert hist[1107]==(5317,-20275)
assert all(hist[n]==hist[717] for n in range(718,1107))
assert sub(hist[1107],hist[1106])==F
# Independent full-partition reconstruction; checks *source-labelled* base fibres.
def fresh(n):
 order=sorted(range(n),key=lambda j:value(P[j],LO))
 assert order==sorted(range(n),key=lambda j:value(P[j],HI))
 split={j:[] for j in range(M)}
 for k,u in enumerate(order):
  v=order[(k+1)%n]
  own=H[(bisect_right(HV,value(P[u],LO))-1)%M]
  split[own].append((u,v,gap(u,v)))
 risk=(1,0)
 for rows in split.values():risk=sub(risk,maxgap(rows))
 return risk,split
for t0,count,own,delta in BKS:
 risk,whole=fresh(t0)
 assert risk==hist[t0] and whole[own]==base[t0]
 assert fresh(t0+count)[0]==hist[t0+count]
for n in (292,328,456,492,493,553,620,656,717,742,845,942,1009,1106,1107):
 assert fresh(n)[0]==hist[n]
print("PASS_R23_SOURCE_LABELLED_389_PLATEAU")
print("PIN=43ec6098b1330ae86d0a7863be336c5d97f6ef34")
print("THETA_INTERVAL_OPEN",LO,HI)
print("FLOORS_AND_ORDER=0..1106; BASE_FIBRES=16; EXACT_UPDATES=614")
print("PLATEAU=718..1106; ZERO_INCREMENT_COUNT=389")
print("R492",hist[492],"R553",hist[553],"R620=R656",hist[620])
print("R717=R1106",hist[717],"R1107",hist[1107],"DELTA",F)
