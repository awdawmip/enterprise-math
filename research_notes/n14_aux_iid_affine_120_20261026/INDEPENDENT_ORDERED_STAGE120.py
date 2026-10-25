"""Independent literal ordered-prefix integer mass audit of N14 Stage120.
Separate recursive Bellman construction from published bottom-up author checker.
Does NOT import the primary verifier. External iid only, no native X6 claim.
"""
from fractions import Fraction
from functools import cache
from collections import defaultdict
import json
from pathlib import Path

TMAX=14
pnum=(3,1,20);qnum=(1,1,10)
P=tuple(Fraction(x,24) for x in pnum)
K=Fraction(1527132609,1903099)
L=Fraction(1463947128,1903099)
critical={(9,1,2):('Q','C'),(9,3,0):('P','C')}

@cache
def decide(n,c0,c1):
    costs={'P':K*Fraction(2**(c0+c1),3**c0),'Q':L}
    if n<TMAX:
        costs['C']=1+sum(P[j]*decide(n+1,c0+(j==0),c1+(j==1))[0] for j in range(3))
    v=min(costs.values())
    min_actions=tuple(k for k,x in costs.items() if x==v)
    return v,min_actions

# No shared value/moment functions from primary checker.
results={};hit0=None;visits={}
for dstop in (0,1):
    for astop in (0,1):
        acc=[0,0,0,0,0]
        arrivals=defaultdict(lambda:[0,0,0])
        def descend(depth,z,o,wp,wq):
            acc[4]+=1
            s=(depth,z,o)
            opts=decide(depth,z,o)[1]
            if s in critical:
                assert opts==critical[s]
                arrivals[s][0]+=1
                arrivals[s][1]+=wp*24**(TMAX-depth)
                arrivals[s][2]+=wq*12**(TMAX-depth)
            if s==(9,1,2):choice='Q' if dstop else 'C'
            elif s==(9,3,0):choice='P' if astop else 'C'
            else:choice=opts[0]
            if choice=='C':
                for idx in range(3):
                    descend(depth+1,z+(idx==0),o+(idx==1),wp*pnum[idx],wq*qnum[idx])
            else:
                pweight=wp*24**(TMAX-depth);qweight=wq*12**(TMAX-depth)
                if choice=='Q':acc[0]+=pweight
                else:acc[1]+=qweight
                acc[2]+=depth*pweight;acc[3]+=depth*qweight
        descend(0,0,0,1,1)
        moments=(Fraction(acc[0],24**TMAX),Fraction(acc[1],12**TMAX),Fraction(acc[2],24**TMAX),Fraction(acc[3],12**TMAX))
        results[f'{dstop}{astop}']=list(map(str,moments))
        visits[f'{dstop}{astop}']=acc[4]
        if dstop==0 and astop==0:
            hit0={str(k):{'count':v[0],'P_mass':str(Fraction(v[1],24**TMAX)),'Q_mass':str(Fraction(v[2],12**TMAX))} for k,v in arrivals.items()}

assert decide.cache_info().currsize==680
import ast
assert sorted(critical)==sorted(ast.literal_eval(s) for s in hit0)
expected=json.loads(Path(__file__).with_name('certificate120.json').read_text())
m_base=tuple(map(Fraction,expected['four_moments']['M00']))
gD=tuple(map(Fraction,expected['four_moments']['dD']))
gA=tuple(map(Fraction,expected['four_moments']['dA']))
for dw in (0,1):
    for ap in (0,1):
        got=tuple(map(Fraction,results[f'{dw}{ap}']))
        assert got==tuple(m_base[i]+dw*gD[i]+ap*gA[i] for i in range(4))
assert visits==expected['execution']['corners_integer_DFS_visits']
for state,label in (('(9, 1, 2)','D'),('(9, 3, 0)','A')):
    for k,v in hit0[state].items():assert v==expected['first_hit'][label][k],(label,k,v)
# Check support identities and saturation purely from four literal-Dfs moments.
M0=tuple(map(Fraction,results['00']))
Md=tuple(map(Fraction,results['10']))
Ma=tuple(map(Fraction,results['01']))
Mda=tuple(map(Fraction,results['11']))
dD=tuple(x-y for x,y in zip(Md,M0))
dA=tuple(x-y for x,y in zip(Ma,M0))
assert Mda==tuple(M0[i]+dD[i]+dA[i] for i in range(4))
E=lambda m:m[0]-m[1]
w_init=-E(M0)/E(dD);dw_dy=-E(dA)/E(dD)
ymax=(1-w_init)/dw_dy
assert 0<ymax<1
assert w_init==Fraction(expected['mixing']['w0'])
assert ymax==Fraction(expected['mixing']['y_end'])
end=tuple(M0[i]+dD[i]+ymax*dA[i] for i in range(4))
assert end[0]==end[1]==Fraction(expected['mixing']['alpha_end'])
assert end[2]==Fraction(expected['mixing']['value_end']) and end[2]>end[3]
print(json.dumps({'independent_literal_DFS':'PASS','states':decide.cache_info().currsize,'moments':results,'visits':visits,'first_hits':hit0,'max_y':str(ymax),'endpoint_alpha':str(end[0]),'endpoint_value':str(end[2])},indent=2))
