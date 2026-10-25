"""Independent literal ordered history DFS for Stage130; integer branch weights."""
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
N=14; WP=(3,1,20);WQ=(1,1,10)
DENP=24**N;DENQ=12**N
K=F(522693,802);L=F(244736,401)
B=(11,0,1);T=(14,7,4)

@lru_cache(None)
def optimum(n,a,b):
    offers={'P':K*F(2**(a+b),3**a),'Q':L}
    if n<N:
        offers['C']=1+sum(F(WP[j],24)*optimum(n+1,a+(j==0),b+(j==1))[0] for j in range(3))
    best=min(offers.values())
    return best,tuple(op for op,c in offers.items() if c==best)
assert optimum(0,0,0)[0]==F(52838467869186182216021,117157274574869495808)

res={}
for wb,vt in product((0,1),repeat=2):
    prefix=0;end=0; first=defaultdict(lambda:[0,0,0]);sums=[0,0,0,0]
    def visit(n,a,b,np,nq):
        # local recursion retains every ordered word separately, not aggregated at count states
        nonlocal_prefix[0]+=1
        s=(n,a,b)
        if s in (B,T):
            e=first[s];e[0]+=1;e[1]+=np*24**(N-n);e[2]+=nq*12**(N-n)
        if s==B:action='Q' if wb else 'C'
        elif s==T:action='P' if vt else 'Q'
        else:action=optimum(n,a,b)[1][0]
        assert action in optimum(n,a,b)[1]
        if action=='C':
            for j in range(3):visit(n+1,a+(j==0),b+(j==1),np*WP[j],nq*WQ[j])
        else:
            nonlocal_end[0]+=1
            pn=np*24**(N-n);qn=nq*12**(N-n)
            if action=='Q':sums[0]+=pn
            else:sums[1]+=qn
            sums[2]+=n*pn;sums[3]+=n*qn
    nonlocal_prefix=[0];nonlocal_end=[0]
    visit(0,0,0,1,1)
    obs=(F(sums[0],DENP),F(sums[1],DENQ),F(sums[2],DENP),F(sums[3],DENQ))
    d={str(k):{'literal_words':v[0],'P':str(F(v[1],DENP)), 'Q':str(F(v[2],DENQ))} for k,v in first.items()}
    res[str(wb)+str(vt)]={'moments':list(map(str,obs)),'prefix_visits':nonlocal_prefix[0],'terminal_words':nonlocal_end[0],'tie_hits':d}

C={k:tuple(map(F,v['moments'])) for k,v in res.items()}
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda a,k:tuple(x*k for x in a)
M=C['00'];dB=sub(C['10'],M);dT=sub(C['01'],M)
assert C['11']==add(add(M,dB),dT)
assert dT[2]==dT[3]==0
err=lambda x:x[0]-x[1]
w0=-err(M)/err(dB);slope=-err(dT)/err(dB)
assert w0==F(23520679218203837,81438720000000000)
assert slope==F(194887,61696000000)
points=[]
for v in (F(0),F(1)):
    w=w0+slope*v
    x=add(add(M,mul(dB,w)),mul(dT,v))
    assert 0<w<1 and x[0]==x[1] and x[2]>x[3] and x[2]+K*x[1]+L*x[0]==optimum(0,0,0)[0]
    points.append(list(map(str,x)))
assert F(points[0][0])==F(36696744060534746695,105616844785075617792)
assert F(points[1][0])==F(36696744084893090695,105616844785075617792)
assert F(points[1][2])==F(660257040358974188827,52808422392537808896)
print('CORNER_FIRSTHIT_00',json.dumps(res['00']['tie_hits'],ensure_ascii=False))
print('VISITS', {k:(v['prefix_visits'],v['terminal_words']) for k,v in res.items()})
print('ENDPOINTS',points)
print('AFFINE_B', list(map(str,dB)), 'AFFINE_T',list(map(str,dT)))
print('PASS STAGE130 INDEPENDENT INTEGER WORD DFS')
with (Path(__file__).resolve().parent/'ordered_evidence130.json').open('w') as fp:
    json.dump({'status':'AUTHOR_INDEPENDENT_IMPLEMENTATION_PASS','corners':res,'endpoint_observers':points,'w0':str(w0),'slope':str(slope)},fp,indent=2)
