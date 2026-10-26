"""Exact author checker, Stage160 external N14 ternary iid; Python 3 stdlib."""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(2521611,8218); L=F(1229640,4109); N=14
J=(10,2,0); S=(13,5,2)
@lru_cache(None)
def bell(n,a,b):
    v={'P':K*F(2**(a+b),3**a),'Q':L}
    if n<N:
        v['C']=1+sum(P[i]*bell(*[(n+1,a+1,b),(n+1,a,b+1),(n+1,a,b)][i])[0] for i in range(3))
    m=min(v.values()); return m,tuple(k for k in v if v[k]==m),v
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
gaps=[v-m for n,a,b in states for (m,_,vals) in [bell(n,a,b)] for v in vals.values() if v>m]
ties={st:bell(*st)[1] for st in states if len(bell(*st)[1])>1}
assert len(states)==680 and len(gaps)==1238 and min(gaps)==F(565771,37868544)
assert ties=={J:('P','C'),S:('P','C')}
def act(st,j,s):
    if st==J:return 'P' if j else 'C'
    if st==S:return 'P' if s else 'C'
    assert len(bell(*st)[1])==1
    return bell(*st)[1][0]
@lru_cache(None)
def suffix(n,a,b,j,s):
    c=act((n,a,b),j,s)
    if c=='P':return (F(0),F(1),F(0),F(0))
    if c=='Q':return (F(1),F(0),F(0),F(0))
    v=[suffix(*st,j,s) for st in ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))]
    return (sum(P[i]*v[i][0] for i in range(3)),sum(Q[i]*v[i][1] for i in range(3)),
            1+sum(P[i]*v[i][2] for i in range(3)),1+sum(Q[i]*v[i][3] for i in range(3)))
def ordered(j,s):
    totals={k:defaultdict(int) for k in ('eP','eQ','tP','tQ','p','q')}
    hits={J:[0,0,0],S:[0,0,0]};nodes=0
    def walk(n,a,b,wp,wq):
        nonlocal nodes
        nodes+=1;st=(n,a,b)
        if st in hits:
            hits[st][0]+=1;hits[st][1]+=wp;hits[st][2]+=wq
        c=act(st,j,s)
        if c=='C':
            walk(n+1,a+1,b,3*wp,wq)
            walk(n+1,a,b+1,wp,wq)
            walk(n+1,a,b,20*wp,10*wq)
        else:
            totals['p'][n]+=wp;totals['q'][n]+=wq
            totals['tP'][n]+=n*wp;totals['tQ'][n]+=n*wq
            totals['eP' if c=='Q' else 'eQ'][n]+=wp if c=='Q' else wq
    walk(0,0,0,1,1)
    def total(k,den):return sum((F(v,den**n) for n,v in totals[k].items()),F(0))
    assert total('p',24)==total('q',12)==1
    obs=(total('eP',24),total('eQ',12),total('tP',24),total('tQ',12))
    return obs,nodes,{st:(h[0],F(h[1],24**st[0]),F(h[2],12**st[0])) for st,h in hits.items()}
M={};count={}
for j in (0,1):
 for s in (0,1):
    M[j,s]=suffix(0,0,0,j,s)
    check,n,hits=ordered(j,s)
    assert check==M[j,s];count[j,s]=n
base=M[0,0];dJ=tuple(M[1,0][k]-base[k] for k in range(4))
dS=tuple(M[0,1][k]-base[k] for k in range(4))
assert all(M[1,1][k]-M[1,0][k]-M[0,1][k]+base[k]==0 for k in range(4))
j0=-(base[0]-base[1])/(dJ[0]-dJ[1])
slope=-(dS[0]-dS[1])/(dJ[0]-dJ[1]);j1=j0+slope
assert j0==F(107743801834549,461157120000000) and slope==-F(793909,90069750)
assert 0<j1<j0<1
mix=lambda j,s:tuple(base[k]+j*dJ[k]+s*dS[k] for k in range(4))
left=mix(j1,1);right=mix(j0,0)
alpha159=F(381583997981821329445,1096459521159585595392)
V159=F(13168739674988914815857,1096459521159585595392)
assert left[0]==left[1]==alpha159 and left[2]==V159
assert right[0]==right[1]==F(381586508350717329445,1096459521159585595392)
assert right[2]==F(13167218152253362815857,1096459521159585595392)
assert right[0]>left[0] and left[2]>right[2]
assert left[2]>left[3] and right[2]>right[3]
assert all(v[2]+K*v[1]+L*v[0]==bell(0,0,0)[0] for v in (left,right))
assert (left[2]-right[2])/(right[0]-left[0])==K+L==F(4980891,8218)
print('STAGE160_AUTHOR_EXACT_PASS states=680 positive_gaps=1238 ties=J,S')
print('ordered_DFS_nodes',count)
print('ordered_first_hit',ordered(0,0)[2])
print('M00',base,'dJ',dJ,'dS',dS,'mixed=0')
print('j(s)',j0,slope,'left',left,'right',right)
print('width',right[0]-left[0],'slope',K+L,'Hroot',bell(0,0,0)[0])
