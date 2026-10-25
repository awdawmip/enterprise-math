"""Independent EC27 audit, EC28 quantitative bound and X6 path-fiber witness.
Only Python standard library; all computations are exact integers.
"""
import json
from math import comb
from pathlib import Path

N=120
J=N//2
r=[0]*(J+1)
r[0]=1
for k in range(1,J+1):
    convolution=sum(r[i]*r[k-1-i] for i in range(k))
    r[k]=convolution-(2*r[k-2] if k>=2 else 0)+(r[k-3] if k>=3 else 0)
y=r[:]
y[0]-=1
y[1]-=1
h=[y[k]-(y[k-1] if k else 0) for k in range(J+1)]
assert all(y[k]>=0 for k in range(J+1))
assert y[:4]==[0,0,0,0] and y[4]==1
assert all(h[k]>=2**(k-5) for k in range(5,J+1))

def conv(a,b):
    out=[0]*(J+1)
    for i,x in enumerate(a):
        for k in range(J+1-i):
            out[i+k]+=x*b[k]
    return out

powers=[[1]+[0]*J]
for _ in range(N+1):
    powers.append(conv(powers[-1],r))

E=[]
for n in range(N+1):
    cur=[0]*(n+1)
    if n==0:cur[0]+=1
    if n==2:cur[1]-=1
    for d,grade,c in [(1,0,1),(1,1,1),(4,2,-2),(6,3,1)]:
        if n>=d:
            for k,val in enumerate(E[n-d]):
                cur[k+grade]+=c*val
    E.append(cur)

checks=bound_checks=0
min_slack=None
for n in range(N+1):
    for j in range(n//2+1):
        p=n-2*j+1
        diff=E[n][j]-(E[n][j-1] if j else 0)
        rhs=powers[p][j]-(powers[p][j-1] if j else 0)
        assert diff==rhs,(n,j,diff,rhs)
        checks+=1
        if j>=5 and 2*j<=n<=3*j-3:
            lower=p*2**(j-5)
            assert diff>=lower,(n,j,diff,lower)
            bound_checks+=1
            slack=diff-lower
            if min_slack is None or slack<min_slack:
                min_slack=slack

n=10
U3,U4=comb(n,3),comb(n,4)
V3,V4=U3*2**(n-3),U4*2**(n-4)
assert (U3,U4,V3,V4)==(120,210,15360,13440)
assert U3<U4 and V3>V4
# Three-coordinate native displacement and remaining three native fields are all
# explicitly fixed for this witness; no claim that it is a complete native slice.
endpoint_support=[(n-j,j,0,0,0,0) for j in range(n+1)]
assert len(set(endpoint_support))==11
report={
    'research_unit':'R4-EC28',
    'verified_statement':'positive lower bound and support-to-source non-transfer witness',
    'model':'auxiliary BRC E(x,u) and two explicitly defined X6 primitive-axis path systems',
    'integer_arithmetic':True,
    'n_max':N,
    'diagonal_identity_pairs':checks,
    'quantitative_bound_pairs':bound_checks,
    'smallest_bound_margin':str(min_slack),
    'quantitative_bound': 'E[n,j]-E[n,j-1] >= (n-2*j+1)*2**(j-5) for j>=5 and 2*j<=n<=3*j-3',
    'countermodels': {
        'n':n,'j_previous':3,'j_current':4,
        'single_source':[U3,U4], 'double_e1_source':[V3,V4],
        'current_minus_previous':{'single_source':U4-U3,'double_e1_source':V4-V3},
        'same_endpoint_support':True,
        'primitive_steps':'A and A0/A1 are +E1, B is +E2; copies distinguished by provenance',
        'claim':'endpoint support and grade-preserving step map do not determine provenance counts or their unimodality'
    },
    'limits':['finite checks not proof of universal bound','no proven native X6 dynamics/three-dimensional slice correspondence','not an independent Driver review']
}
Path(__file__).resolve().with_name('EC28_report.json').write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,sort_keys=True))
