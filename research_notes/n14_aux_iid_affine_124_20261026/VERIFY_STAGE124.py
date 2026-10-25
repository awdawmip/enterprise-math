"""R1/N14 Stage124 author-level exact verification (Python 3, stdlib only).
The four-moment count quotient is certified only for this external iid model.
"""
from fractions import Fraction as F
from functools import lru_cache

N=14
P=(F(1,8),F(1,24),F(5,6))
A=(9,3,0)
T=(14,7,4)
O=(0,0,0)
K=F(1245231873,1658336)
L=F(36440256,51823)
ALPHA123=F(2573845365525582162925,7411551152237344456704)
VALUE123=F(377878052586265662571445,29646204608949377826816)
Y123=F(151539326395319,415627392000000)

def children(s):
    n,a,b=s
    return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))

H={}
policy={}
ties={}
gaps=[]
for n in range(N,-1,-1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b)
            actions=[K*F(2**(a+b),3**a),L]
            if n<N:
                actions.append(F(1)+sum(P[j]*H[t] for j,t in enumerate(children(s))))
            h=min(actions)
            H[s]=h
            optimal=[i for i,v in enumerate(actions) if v==h]
            policy[s]=optimal[0]
            if len(optimal)>1:
                ties[s]=optimal
            gaps.extend(v-h for v in actions if v>h)
assert len(H)==680
assert len(gaps)==1238
assert ties=={A:[0,2],T:[0,1]}
assert min(gaps)==F(294166217221,39614118100992)
ROOT=F(5878829162353591081475135,11355563791072559628288)
assert H[O]==ROOT==VALUE123+(K+L)*ALPHA123

@lru_cache(None)
def moment(y,z):
    @lru_cache(None)
    def walk(s):
        if s==A:
            c=cont(s)
            stop=(F(0),F(1),F(0),F(0))
            return tuple(y*stop[i]+(1-y)*c[i] for i in range(4))
        if s==T:
            return (1-z,z,F(0),F(0))
        action=policy[s]
        if action==0:
            return (F(0),F(1),F(0),F(0))
        if action==1:
            return (F(1),F(0),F(0),F(0))
        return cont(s)
    def cont(s):
        c=[walk(t) for t in children(s)]
        return (sum(P[j]*c[j][0] for j in range(3)),
                sum((F(1,12),F(1,12),F(5,6))[j]*c[j][1] for j in range(3)),
                F(1)+sum(P[j]*c[j][2] for j in range(3)),
                F(1)+sum((F(1,12),F(1,12),F(5,6))[j]*c[j][3] for j in range(3)))
    return walk(O)

m00=moment(F(0),F(0))
m10=moment(F(1),F(0))
m01=moment(F(0),F(1))
m11=moment(F(1),F(1))
da=tuple(m10[i]-m00[i] for i in range(4))
dt=tuple(m01[i]-m00[i] for i in range(4))
assert m11==tuple(m00[i]+da[i]+dt[i] for i in range(4))
assert m00==(F(608919703452600011,1752976676930715648),
             F(55715889515225,160489808068608),
             F(2798007941169380921,219122084616339456),
             F(161747615623729,13374150672384))
assert da==(F(-1921609375,7925422620672),
            F(259765625,835884417024),
            F(-20758609375,330225942528),
            F(-1476453125,69657034752))
assert dt==(F(-165875,25048249270272),
            F(165875,26748301344768),F(0),F(0))

def difference(m):
    return m[0]-m[1]
y0=-difference(m00)/difference(da)
y_slope=-difference(dt)/difference(da)
assert y0==F(151548960415319,415627392000000)
assert y_slope==F(-160567,6927123200)

def balanced(z):
    y=y0+y_slope*z
    m=tuple(m00[i]+da[i]*y+dt[i]*z for i in range(4))
    return y,m

y_start,m_start=balanced(F(1))
y_end,m_end=balanced(F(0))
ETA=F(8596140125,8578184203978407936)
ALPHA124=F(2573845372952647230925,7411551152237344456704)
VALUE124=F(377878009388672358128945,29646204608949377826816)
assert y_start==Y123
assert m_start[0]==m_start[1]==ALPHA123 and m_start[2]==VALUE123
assert m_end[0]==m_end[1]==ALPHA124 and m_end[2]==VALUE124
assert m_start[0]+ETA==m_end[0]
assert m_start[2]-m_end[2]==(K+L)*ETA
assert m_start[2]-m_start[3]==F(19564551641189828171621,29646204608949377826816)
assert m_end[2]-m_end[3]==F(19564523009155753489121,29646204608949377826816)
assert 0<y_start<y_end<1
assert m_start[2]+(K+L)*m_start[0]==ROOT
assert m_end[2]+(K+L)*m_end[0]==ROOT

# Next dual candidate is exploration, not a proved successor primal interval.
DK=F(-1)
DL=F(-608000,474363)
deriv={}
decreasing=[]
for n in range(N,-1,-1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b)
            lr=F(2**(a+b),3**a)
            v=[K*lr,L]
            d=[DK*lr,DL]
            if n<N:
                v.append(F(1)+sum(P[j]*H[c] for j,c in enumerate(children(s))))
                d.append(sum(P[j]*deriv[c] for j,c in enumerate(children(s))))
            selected=1 if s==T else policy[s]
            deriv[s]=d[selected]
            for i in range(len(v)):
                gap=v[i]-v[selected]
                slope=d[i]-d[selected]
                assert gap>=0
                if gap==0 and s==A:
                    assert slope==0
                if gap>0 and slope<0:
                    decreasing.append((-gap/slope,s,i))
step,state,action=min(decreasing)
assert (step,state,action)==(F(13731333106707,1006541960224),(12,7,5),1)
K125=K+DK*step
L125=L+DL*step
assert K125==F(3579845625,4855672)
assert L125==F(416181048,606959)
H125={}
ties125={}
positive125=[]
for n in range(N,-1,-1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b)
            acts=[K125*F(2**(a+b),3**a),L125]
            if n<N:
                acts.append(F(1)+sum(P[j]*H125[t] for j,t in enumerate(children(s))))
            value=min(acts)
            H125[s]=value
            opts=[i for i,v in enumerate(acts) if v==value]
            if len(opts)>1:
                ties125[s]=opts
            positive125.extend(v-value for v in acts if v>value)
assert ties125=={A:[0,2],(12,7,5):[1,2]}
assert len(positive125)==1238
assert min(positive125)==F(578968738307,115991671209984)
assert H125[O]==F(16854019707653693377319545,33249530339162194968576)
print('PASS Stage124: 680 Bellman states / 1238 positive gaps / two ties')
print('support',ROOT,'slope',K+L)
print('balance: y(z)=',y0,'+',y_slope,'z')
print('interval delta=',ETA,'alpha124=',ALPHA124,'V124=',VALUE124)
print('Stage125 DUAL ONLY: K=',K125,'L=',L125,'new tie',(12,7,5))
