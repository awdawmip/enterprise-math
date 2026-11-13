"""EC49AO exact Fraction certificate; author-side auxiliary positive BRC only."""
from fractions import Fraction as F
from itertools import combinations, product
import json
Z=F(0);O=F(1); ETA=F(1,25);C1=F(43,16);C2=F(13,16)
LOW=F(25,32);HIGH=F(43,48);COST=(1,1,2,2,0)

def solve(cols,rhs):
    n=len(rhs)
    a=[[F(cols[j][i]) for j in range(n)]+[rhs[i]] for i in range(n)]
    for p in range(n):
        j=next((j for j in range(p,n) if a[j][p]),None)
        if j is None:return None
        a[p],a[j]=a[j],a[p]; r=a[p][p];a[p]=[v/r for v in a[p]]
        for j in range(n):
            if j!=p and a[j][p]:
                r=a[j][p];a[j]=[v-r*t for v,t in zip(a[j],a[p])]
    return [a[i][-1] for i in range(n)]

def fullbuy_vertices():
    rhs=[O]*3+[6*C2-C1,C1-3*C2]
    cols=[tuple(int(w==i) for i in range(3))+(int(g==0),int(g==1))
          for w in range(3) for g in range(3)]
    coarse=set()
    for basis in combinations(range(9),5):
        sol=solve([cols[j] for j in basis],rhs)
        if sol is None or any(t<0 for t in sol):continue
        y=[[Z]*3 for _ in range(3)]
        for j,t in zip(basis,sol):y[j//3][j%3]=t
        coarse.add(tuple(tuple(row) for row in y))
    fine=set()
    for y in coarse:
        labels=[(w,g) for w in range(3) for g in range(2) if y[w][g]]
        for a in product((0,1),repeat=len(labels)):
            x=[[Z]*5 for _ in range(3)]
            for w in range(3):x[w][4]=y[w][2]
            for (w,g),bit in zip(labels,a):x[w][2*g+bit]=y[w][g]
            fine.add(tuple(tuple(row) for row in x))
    assert len(coarse)==9 and len(fine)==144
    return coarse,sorted(fine)

def first_cost_vertices():
    out=set()
    for m in range(3):
        others=[w for w in range(3) if w!=m]
        for i,j in product(range(5),repeat=2):
            need=C1-COST[i]-COST[j]
            for a,b in combinations(range(5),2):
                if not min(COST[a],COST[b])<need<max(COST[a],COST[b]):continue
                p=(need-COST[b])/F(COST[a]-COST[b])
                x=[[Z]*5 for _ in range(3)]
                x[others[0]][i]=x[others[1]][j]=O
                x[m][a]=p;x[m][b]=O-p
                out.add(tuple(tuple(row) for row in x))
    assert len(out)==168
    return sorted(out)

def fibers(x):
    for c,u in product(range(4),range(2)):
        q=[x[w][c]*(F(1,2)+(2*u-1)*(1-w)*ETA)/3 for w in range(3)]
        T=sum(q);V=sum(max(Z,43*qz-16*T) for qz in q)
        yield T,V
def cp(x):return sum((t for t,v in fibers(x)),Z)
def H(x):return sum((v/F(172) for t,v in fibers(x)),Z)
def lam():return F(553,946)*ETA-F(152,473)
def B():return F(22625,60544)-F(13825,30272)*ETA
def D(x):return H(x)-lam()*cp(x)
def mid(x,y):return tuple(tuple((a+b)/2 for a,b in zip(rx,ry)) for rx,ry in zip(x,y))

coarse,fine=fullbuy_vertices()
for x in fine:
    assert all(sum(row)==1 for row in x)
    assert sum(COST[c]*x[w][c] for w,c in product(range(3),range(5)))==C1
    assert cp(x)==C2
scores=[H(x) for x in fine]
assert max(scores)==F(77,688)
assert sum(z==F(77,688) for z in scores)==24
witness=((Z,F(3,16),F(1,4),Z,F(9,16)),
         (O,Z,Z,Z,Z),(Z,O,Z,Z,Z))
assert witness in fine and H(witness)==F(77,688)
vs=first_cost_vertices()
items=[(x,cp(x),B()-D(x)) for x in vs]
assert all(s>=0 for x,c,s in items)
low=[x for x,c,s in items if s==0 and c==LOW]
high=[x for x,c,s in items if s==0 and c==HIGH]
assert (len(low),len(high))==(12,4)
assert sum(s==0 for x,c,s in items)==16
assert min(c for x,c,s in items)==F(43,96)
assert max(c for x,c,s in items)==HIGH
m=min(s for x,c,s in items if s>0)
g=min(B()-D(mid(x,y)) for x in low for y in high)
assert m==F(27,137600) and g==F(2131,825600)
delta=m/10
assert -lam()/1000>=delta
lmin=F(901,2750);hmin=F(19,110)
assert lmin==(HIGH-C2-F(1,1000)-(HIGH-F(43,96))/10)/(HIGH-LOW)
assert hmin==(C2-LOW)/(HIGH-LOW)-F(1,10)
assert 2*g*lmin*hmin>=delta
upper=B()+lam()*C2-delta
assert upper==F(1715013,15136000)
assert upper-F(77,688)==F(21013,15136000)
P=Q=Z
for w,u,z in product(range(3),range(2),range(3)):
    t=F(1,2)+(2*u-1)*(1-w)*ETA
    p=t*(F(1,6) if z==w else F(1,12));q=t/9
    assert p>0 and q>0
    P+=p;Q+=q
assert P==Q==O
result={
  "schema":"EC49AO_EXACT_FIXED_COST_CERT_V1",
  "status":"PASS_EXACT_FRACTION_AUTHOR_UNREVIEWED",
  "model":"auxiliary positive 18+18 leaf BRC; independent behavioral coins; hidden w erased",
  "eta":str(ETA),"C1":str(C1),"C2":str(C2),
  "full_purchase_coarse_vertices":len(coarse),
  "full_purchase_labeled_vertices":len(fine),
  "full_purchase_optimum":str(max(scores)),"full_purchase_tied_optima":24,
  "original_C1_vertices":len(vs),"dual_tight_low":len(low),
  "dual_tight_high":len(high),"strict_vertex_minimum_gap":str(m),
  "cross_midpoint_minimum_gap":str(g),"all_behavioral_bound":str(upper),
  "new_certified_dual_gap":str(delta),
  "old_support":str(B()+lam()*C2),"lower_witness":str(F(77,688)),
  "remaining_global_gap":str(upper-F(77,688)),
  "scope_note":"Upper bound is all real causal policies; equality for the full-purchase subclass only; no native BRC/X6 or formal admission"
}
print(json.dumps(result,indent=2,ensure_ascii=False))
