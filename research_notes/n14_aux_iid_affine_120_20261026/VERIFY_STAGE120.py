"""Executable exact Stage120 auxiliary iid certificate; standard library only.
No native P000 X6 transfer or claim of independent Driver review.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(1527132609,1903099)
L=F(1463947128,1903099)
D=(9,1,2)
A=(9,3,0)
root=(0,0,0)

def ch(s):
    n,a,b=s
    return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))

V={}
policy={}
ties={}
gaps=[]
for n in range(N,-1,-1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b)
            opts={'P':K*F(2**(a+b),3**a),'Q':L}
            if n<N:
                opts['C']=1+sum(P[j]*V[x] for j,x in enumerate(ch(s)))
            minimum=min(opts.values())
            V[s]=minimum
            mm=[k for k,v in opts.items() if v==minimum]
            policy[s]=mm[0]
            if len(mm)>1:ties[s]=mm
            gaps.extend(v-minimum for v in opts.values() if v>minimum)
assert len(V)==680 and len(gaps)==1238
assert min(gaps)==F(76168651372577,4909786414055424)
assert ties=={D:['Q','C'],A:['P','C']}

@lru_cache(None)
def moments(s,w,y):
    def continued():
        m=[moments(x,w,y) for x in ch(s)]
        return (
            sum(P[j]*m[j][0] for j in range(3)),
            sum(Q[j]*m[j][1] for j in range(3)),
            1+sum(P[j]*m[j][2] for j in range(3)),
            1+sum(Q[j]*m[j][3] for j in range(3))
        )
    if s==D:
        c=continued()
        return tuple(w*x+(1-w)*v for x,v in zip((F(1),F(0),F(0),F(0)),c))
    if s==A:
        c=continued()
        return tuple(y*x+(1-y)*v for x,v in zip((F(0),F(1),F(0),F(0)),c))
    if policy[s]=='Q':return (F(1),F(0),F(0),F(0))
    if policy[s]=='P':return (F(0),F(1),F(0),F(0))
    return continued()

m00=moments(root,F(0),F(0))
m10=moments(root,F(1),F(0))
m01=moments(root,F(0),F(1))
m11=moments(root,F(1),F(1))
minus=lambda x,z:tuple(a-b for a,b in zip(x,z))
dD=minus(m10,m00)
dA=minus(m01,m00)
assert m11==tuple(m00[i]+dD[i]+dA[i] for i in range(4))
diff=lambda x:x[0]-x[1]
w0=-diff(m00)/diff(dD)
rate=-diff(dA)/diff(dD)
ymax=(1-w0)/rate
assert w0==F(376517470455067,1042086080000000)
assert rate==F(6494178,2326085)
assert ymax==F(665568609544933,2909391744000000)
assert 0<w0<1 and 0<ymax<1
def eval_y(y):
    w=w0+rate*y
    return tuple(m00[i]+w*dD[i]+y*dA[i] for i in range(4))
start,end=eval_y(F(0)),eval_y(ymax)
assert start[0]==start[1]==F(900390183707375071351,2592933255351443128320)
assert start[2]==F(132634859722005927805223,10371733021405772513280)
assert end[0]==end[1]==F(2573764724900518487425,7411551152237344456704)
assert end[2]==F(378361860665073597077285,29646204608949377826816)
assert start[2]>start[3] and end[2]>end[3]
eta=end[0]-start[0]
assert eta==F(1266642955256352447367,77958194918387612186050560)
assert all(V[root]==m[2]+(K+L)*m[0] for m in (start,end))

# Literal DFS with integer numerator weights, not count-state moment recursion.
pnum=(3,1,20)
qnum=(1,1,10)
corner={}
visit={}
hit0={}
for w in (0,1):
    for y in (0,1):
        acc=[0,0,0,0,0]
        arrivals=defaultdict(lambda:[0,0,0])
        def walk(s,wp,wq):
            acc[4]+=1
            n,a,b=s
            if s in ties:
                r=arrivals[s]
                r[0]+=1
                r[1]+=wp*24**(N-n)
                r[2]+=wq*12**(N-n)
            act=('Q' if w else 'C') if s==D else ('P' if y else 'C') if s==A else policy[s]
            if act=='C':
                for j,x in enumerate(ch(s)):
                    walk(x,wp*pnum[j],wq*qnum[j])
                return
            wp0=wp*24**(N-n)
            wq0=wq*12**(N-n)
            if act=='Q':acc[0]+=wp0
            else:acc[1]+=wq0
            acc[2]+=n*wp0
            acc[3]+=n*wq0
        walk(root,1,1)
        m=(F(acc[0],24**N),F(acc[1],12**N),F(acc[2],24**N),F(acc[3],12**N))
        assert m==tuple(m00[j]+w*dD[j]+y*dA[j] for j in range(4))
        key=str(w)+str(y)
        corner[key]=list(map(str,m))
        visit[key]=acc[4]
        if (w,y)==(0,0):
            hit0={str(s):[data[0],str(F(data[1],24**N)),str(F(data[2],12**N))] for s,data in arrivals.items()}
assert hit0[str(D)]==[172,'671875/53747712','671875/20155392']
assert hit0[str(A)]==[84,'109375/1990656','109375/6718464']
assert visit=={'00':893725,'01':888685,'10':885985,'11':880945}
print(json.dumps({'PASS':True,'states':len(V),'strict_gaps':len(gaps),'min_gap':str(min(gaps)),
    'ties':{str(k):v for k,v in ties.items()},'first_hit':hit0,'visits':visit,
    'w0':str(w0),'w_slope':str(rate),'ymax':str(ymax),
    'eta':str(eta),'alpha120':str(end[0]),'V120':str(end[2])},indent=2))
