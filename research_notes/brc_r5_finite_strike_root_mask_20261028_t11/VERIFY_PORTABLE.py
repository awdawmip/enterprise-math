from fractions import Fraction as F
from itertools import product
Y = (F(1,2),F(1),F(3,2))
K = {'AU':(F(1,4),F(1,2),F(1,4)),
     'BU':(F(1,8),F(3,4),F(1,8))}
R = {'AU':F(1),'AV':F(1,4),'BU':F(1),'BV':F(2)}
Q = {'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
P = {'A':F(1,2),'B':F(3,2)}
S = {'A':F(1,2),'B':F(1,2)}
D = {h:list(zip(Y,k)) for h,k in K.items()}
D['AV']=[(F(1,4),F(1))]
D['BV']=[(F(2),F(1))]
assert sum(Q.values()) == sum(Q[h]*R[h] for h in Q) == 1
assert sum(S.values()) == sum(S[h]*P[h] for h in S) == 1
assert all(sum(p for y,p in c)==1 and sum(y*p for y,p in c)==R[h] for h,c in D.items())
assert len([p for c in D.values() for y,p in c])==8

def G(kernel,k):
    return min(F(1),k)-sum(p*min(y,k) for y,p in zip(Y,kernel))
assert (G(K['AU'],F(1)),G(K['BU'],F(1)))==(F(1,8),F(1,16))
assert (G(K['AU'],F(9,10)),G(K['BU'],F(9,10)))==(F(1,10),F(1,20))
a,b,u,v=F(1),F(9,10),F(0),F(7,100)
wA,wB=Q['AU'],Q['BU'];s=F(7,100)
assert s==(wA*G(K['AU'],b)+wB*G(K['BU'],b))/(wA+wB)
assert wA*max(G(K['AU'],b)-s,0)+wB*max(G(K['BU'],b)-s,0)==F(1,200)

def bellman(a,b,u,v):
    c=lambda r:u*r+v
    stop=lambda r,t:min(a*r,b)+t*c(r)
    terminal=lambda h:sum(p*min(a*y,b) for y,p in D[h])
    costs={h:({'P':b+2*c(R[h]),'Q':a*R[h]+2*c(R[h]),
                'C':terminal(h)+3*c(R[h])}) for h in R}
    def parent(root,common=None):
        h=root+'U';hv=root+'V'
        hcost=min(costs[h].values()) if common is None else costs[h][common]
        other=min(costs[hv].values())
        cont=(Q[h]*hcost+Q[hv]*other)/S[root]
        return min(stop(P[root],1),cont)
    full=sum(S[r]*parent(r) for r in 'AB')
    LR=min(sum(S[r]*parent(r,act) for r in 'AB') for act in 'PQC')
    return full,LR,costs,[(act,parent('A',act),parent('B',act)) for act in 'PQC']
assert bellman(F(1),F(9,10),F(0),F(7,100))[:2]==(F(77,100),F(77,100))
full,LR,costs,table=bellman(F(406),F(489),F(35),F(-14))
assert (full,LR,LR-full)==(F(364),F(731,2),F(3,2))
assert tuple(costs['AU'][a] for a in 'PQC')==(F(531),F(448),F(439))
assert tuple(costs['BU'][a] for a in 'PQC')==(F(531),F(448),F(454))
assert tuple(costs['AV'][a] for a in 'PQC')==(F(957,2),F(91),F(343,4))
assert tuple(costs['BV'][a] for a in 'PQC')==(F(601),F(924),F(657))
assert table == [('P',F(413,2),F(1055,2)),
                 ('Q',F(413,2),F(1049,2)),
                 ('C',F(407,2),F(1055,2))]
O=(F(7,16),F(7,24),F(9,4),F(5,2))
assert sum(x*y for x,y in zip((406,489,35,-14),O))==full
print('EIGHT_POSITIVE_LEAVES; P_Q_TOTALS=1,1')
print('CONDITIONAL_GAP=1/200; POSITIVE_DIRECTION_GLOBAL_GAP=0')
print('SIGNED_LAMBDA=(406,489,35,-14)')
print('V_FULL=364; V_LR=731/2; GAP=3/2')
print('FULL_WITNESS=(7/16,7/24,9/4,5/2)')
print('ALL EXACT CHECKS PASSED')
