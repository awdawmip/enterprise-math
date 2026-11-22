"""R101: exact integer-scaled crosschecks for the strict sub-half tie atlas.
This is bounded experimental corroboration, not the proof for the infinite lattice.
"""
from fractions import Fraction as Q
from collections import defaultdict
import json

def port(a):
    return max(sum(max(v,0) for v in a),sum(max(-v,0) for v in a))

def directions(n):
    groups=defaultdict(list)
    for x in range(-n,n+1):
        for y in range(-n,n+1):
            for z in range(max(-n,-n-x-y),min(n,n-x-y)+1):
                a=(x,y,z)
                if not any(a) or next(v for v in a if v)!=abs(next(v for v in a if v)):continue
                p=port(a)
                if p>n:continue
                u=x+3*y+6*z
                v=3*x+12*y+30*z
                h=7*x+39*y+126*z
                groups[p].append((a,(abs(u),max(abs(v),abs(v-u)),max(abs(h),abs(h-u)),abs(h-v))))
    return groups

D=(6,-4,1);B=(9,-5,1);E=(15,-9,2);C=(24,-14,3)

def expected(s,t,p):
    x=s+1;y=t+1;z=s+t
    a=Q(3)/x;b=Q(6)/y
    cost=min(Q(1,2),2*b,max(a,b),2*a if p>=27 else Q(10**6))
    if cost>=Q(1,2):return None
    ties=set()
    if 2*b==cost: ties.add(D)
    if max(a,b)==cost:
        ties.add(B)
        if p>=17 and Q(9)/z<=cost:ties.add(E)
    if p>=27 and 2*a==cost:ties.add(C)
    return cost,ties

weights=[(7,28),(10,40),(13,52),(20,80),(13,13),(19,19),(25,25),
         (7,27),(7,29),(13,12),(13,14),(13,25),(13,26),(13,27),
         (20,37),(20,38),(20,39),(20,40),(20,41),(20,42),
         (8,25),(8,26),(8,27),(8,28),(8,29),
         (100,200),(100,198),(100,196),(100,204),(100,202),
         (15,100),(100,15),(2,2),(6,24),(12,12)]
weights=[(Q(x-1),Q(y-1)) for x,y in weights]
weights += [(Q(13,2),Q(26)),(Q(25,2),Q(25,2)),(Q(17,2),Q(35)),(Q(77,5),Q(99,4))]
weights=list(dict.fromkeys(weights))
byport=directions(40)
assert sum(len(v) for v in byport.values())==110740
checks=0
for s,t in weights:
    den=s.denominator*t.denominator
    sn=s.numerator*t.denominator
    tn=t.numerator*s.denominator
    X=sn+den;Y=tn+den;Z=sn+tn
    # Common denominator L=2XYZ: every F cost is an exact integer/L
    L=2*X*Y*Z
    f1=X*Y*Z
    fv=2*den*Y*Z
    fh=2*den*X*Z
    fk=2*den*X*Y
    best=10**90
    ties=set()
    for p in range(1,41):
        for a,(u,v,h,k) in byport[p]:
            score=max(u*f1,v*fv,h*fh,k*fk)
            if score<best:best=score;ties={a}
            elif score==best:ties.add(a)
        if p<11:continue
        e=expected(s,t,p)
        if e is None:
            assert best>=L//2,(s,t,p,best,L)
            continue
        score,eligible=e
        assert score*L==best,(s,t,p,score,best)
        assert eligible==ties,(s,t,p,eligible,ties)
        checks+=1
assert expected(Q(6),Q(27),17)[1]=={D,B,E}
assert expected(Q(12),Q(12),27)[1]=={B,E,C}
assert expected(Q(12),Q(12),26)[1]=={B,E}
assert expected(Q(6),Q(27),16)[1]=={D,B}
result={"status":"PASS","directions_per_weight":110740,"weights_tested":len(weights),"port_budgets_per_weight":30,"subhalf_checks":checks,"low_wall_witness":{"S":6,"T":27,"p":17,"ties":[list(x) for x in sorted({D,B,E})]},"high_wall_witness":{"S":12,"T":12,"p":27,"ties":[list(x) for x in sorted({B,E,C})]},"scope":"exact rational weights; bounded exhaustive q<=40; universal theorem established by symbolic proof using R99/R98"}
print(json.dumps(result,indent=2))
