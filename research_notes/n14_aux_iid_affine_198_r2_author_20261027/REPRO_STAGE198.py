"""Independent exact reference checker for Stage198 external finite-IID lemma."""
from fractions import Fraction as Q
from functools import cache
from itertools import product

pp=(Q(1,8),Q(1,24),Q(5,6))
qq=(Q(1,12),Q(1,12),Q(5,6))
rate=Q(55173536856,391511335)
site=(8,5,2)
terminal=(14,0,0)

def nxt(x,i):
    t,b,c=x
    return t+1,b+(i==0),c+(i==1)

@cache
def value(x):
    t,b,c=x
    costs={'P':rate*Q(2**(b+c),3**b), 'Q':rate}
    if t<14:
        costs['C']=1+sum(pp[j]*value(nxt(x,j))[0] for j in range(3))
    best=min(costs.values())
    return best,tuple(k for k in ('P','Q','C') if k in costs and costs[k]==best),[v-best for v in costs.values() if v>best]

space=[(t,b,c) for t in range(15) for b in range(t+1) for c in range(t-b+1)]
assert len(space)==680
assert value((0,0,0))[0]==Q(1175588567905831666473706183,10723597484515752903966720)
assert {x:value(x)[1] for x in space if len(value(x)[1])>1}=={site:('P','C'),terminal:('P','Q')}
strict=[v for x in space for v in value(x)[2]]
assert len(strict)==1238 and min(strict)==Q(28229681,4698136020)

def decision(x,r,z):
    if x==site:return 'P' if r else 'C'
    if x==terminal:return 'P' if z else 'Q'
    return value(x)[1][0]

@cache
def summary(x,r,z):
    t=x[0]
    action=decision(x,r,z)
    if action=='P':return Q(0),Q(1),Q(0),Q(0)
    if action=='Q':return Q(1),Q(0),Q(0),Q(0)
    children=[summary(nxt(x,i),r,z) for i in range(3)]
    return tuple(sum((pp if j%2==0 else qq)[i]*children[i][j] for i in range(3))+(int(j>=2)) for j in range(4))

obs={(r,z):summary((0,0,0),r,z) for r,z in product(range(2),repeat=2)}
origin=obs[0,0]
D1=tuple(obs[1,0][i]-origin[i] for i in range(4))
D2=tuple(obs[0,1][i]-origin[i] for i in range(4))
assert all(obs[1,1][i]-obs[1,0][i]-obs[0,1][i]+origin[i]==0 for i in range(4))
assert D1==(-Q(7741445,225434243432448),Q(927865,20061226008576),-Q(47302415,28179280429056),-Q(1683065,1671768834048))
assert D2==(-Q(6103515625,78364164096),Q(6103515625,78364164096),Q(0),Q(0))

# Unmerged full ordered history with common integer 24^14 denominator.
def traverse(r,z):
    count=[0]*4;calls=0;arrivals=[0,0,0]
    def walk(state,pm,qm,was_site=False):
        nonlocal calls
        calls+=1
        n=state[0]
        if state==site:
            arrivals[0]+=1
            was_site=True
        if state==terminal:
            arrivals[1]+=1
            arrivals[2]+=int(was_site)
        action=decision(state,r,z)
        if action=='C':
            for i,(pi,qi) in enumerate(zip((3,1,20),(2,2,20))):
                walk(nxt(state,i),pm*pi,qm*qi,was_site)
        else:
            mult=24**(14-n)
            if action=='Q':count[0]+=pm*mult
            else:count[1]+=qm*mult
            count[2]+=n*pm*mult
            count[3]+=n*qm*mult
    walk((0,0,0),1,1)
    return tuple(Q(a,24**14) for a in count), calls, tuple(arrivals)

counts=[]
for r,z in product(range(2),repeat=2):
    result,n,arr=traverse(r,z)
    assert result==obs[r,z]
    assert arr==(32,1,0)
    counts.append(n)
assert counts==[107482,107482,104410,104410]

a0=-((origin[0]-origin[1])/(D2[0]-D2[1]))
aslope=-((D1[0]-D1[1])/(D2[0]-D2[1]))
assert a0==Q(1658094956204453,81920000000000000)
assert aslope==-Q(2648916697,5120000000000000)
assert 0<a0+aslope<a0<1

def point(r):
    z=a0+aslope*r
    return tuple(origin[i]+D1[i]*r+D2[i]*z for i in range(4))
left,right=point(Q(0)),point(Q(1))
assert left[:2]==(Q(1849166467986692153,5258930030792146944),)*2
assert left[2]==Q(1152738894585765565,109561042308169728)
assert right[:2]==(Q(1849166499307598953,5258930030792146944),)*2
assert right[2]==Q(1152738710673976045,109561042308169728)
assert right[0]-left[0]==Q(1957556675,328683126924509184)
assert (left[2]-right[2])/(right[0]-left[0])==2*rate
assert all(v[2]>v[3] and v[0]==v[1] and v[2]+rate*v[1]+rate*v[0]==value((0,0,0))[0] for v in (left,right))
print('STAGE198_INDEPENDENT_EXACT_PASS',sum(counts),'ordered DFS nodes')
