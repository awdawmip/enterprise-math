"""R143 exact rational certificate for the closed upper endpoint of the
Port-10 six-pair BRC near-direction tube (four positive weights).
"""
from fractions import Fraction as Q
from itertools import product

C = {(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)}
A = [t for t in product(range(-10,11), repeat=3)
     if t != (0,0,0)
     and max(sum(v for v in t if v>0),-sum(v for v in t if v<0))<=10
     and next(v for v in t if v)!=0 and next(v for v in t if v)>0]
assert len(A)==1935

def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[j]-h[i]) for i in range(4) for j in range(i+1,4))
G={a:gaps(a) for a in A}

def cap(B,D):return (136+B,312,136+D,B+176,B+D,176+D)
def F(a,B,D):return max(Q(g,s) for g,s in zip(G[a],cap(B,D)))

# R138's seven exact B-chambers at D=500, with eta_500(B)=K/(L0+L1*B).
CH=[(Q(0),Q(316,7),6,500,1),
    (Q(316,7),Q(320,7),7,636,0),
    (Q(320,7),Q(46),2,136,1),
    (Q(46),Q(556,7),6,500,1),
    (Q(556,7),Q(796,7),7,676,0),
    (Q(796,7),Q(136),3,176,1),
    (Q(136),None,1,104,0)]

def line_stats(fun,lo,hi):
    v0=fun(Q(0)); slope=fun(Q(1))-v0
    left=v0+slope*lo
    if hi is None:
        return left,slope,None
    return left,slope,v0+slope*hi

def nonneg(fun,lo,hi):
    left,slope,right=line_stats(fun,lo,hi)
    return left>=0 and (slope>=0 if right is None else right>=0)

opt_witness=[]; outsider_count=0; optimizer_lower_count=0; insider_count=0
endpoint_zeros=[]
for i,(lo,hi,K,L0,L1) in enumerate(CH):
    witness=next((a for a in A if all(nonneg(
      lambda B,j=j,a=a:K*cap(B,500)[j]-G[a][j]*(L0+L1*B),lo,hi)
      for j in range(6))),None)
    assert witness is not None
    opt_witness.append(witness)
    for a in A:
        assert any(nonneg(lambda B,j=j,g=g:g*(L0+L1*B)-K*cap(B,500)[j],lo,hi)
                   for j,g in enumerate(G[a]))
        optimizer_lower_count+=1
        if a not in C:
            assert any(nonneg(lambda B,j=j,g=g:5*g*(L0+L1*B)-8*K*cap(B,500)[j],lo,hi)
                       for j,g in enumerate(G[a]))
            outsider_count+=1
    for a in C:
        for j,g in enumerate(G[a]):
            fun=lambda B,j=j,g=g:125*K*cap(B,500)[j]-88*g*(L0+L1*B)
            left,slope,right=line_stats(fun,lo,hi)
            assert left>=0 and (slope>=0 if hi is None else right>=0)
            insider_count+=1
            if left==0: endpoint_zeros.append((i,a,j,'left',lo))
            if hi is not None and right==0: endpoint_zeros.append((i,a,j,'right',hi))
assert endpoint_zeros==[(0,(9,-5,1),3,'left',Q(0))],endpoint_zeros

# The excluded B=0,D=528 boundary has exactly three near directions.
B,D=Q(0),Q(528)
eta=min(F(a,B,D) for a in A)
near={a for a in A if 2*F(a,B,D)<3*eta}
assert eta==Q(1,88) and near==C-{(9,-5,1)}
assert F((9,-5,1),B,D)==Q(3,176)
boundary_eta=eta

# Exact upper-edge slack on the previously proved R137 B<=20 chamber.
for B in (Q(1,1000),Q(1),Q(5),Q(20)):
    eta,sc=Q(6,B+528),Q(3,B+176)
    assert min(F(a,B,Q(528)) for a in A)==eta
    assert F((9,-5,1),B,Q(528))==sc
    assert Q(3,2)-sc/eta==B/(B+176)
    for D in (Q(528)+2*B-Q(1,1000),Q(528)+2*B):
        e=min(F(a,B,D) for a in A)
        n={a for a in A if 2*F(a,B,D)<3*e}
        assert (9,-5,1) in n if D < Q(528)+2*B else (9,-5,1) not in n

print('R143 UPPER CLOSED ENDPOINT CERTIFICATE PASS')
print('population',len(A),'chambers',len(CH),'optimizer_lower',optimizer_lower_count,
      'outsider_8_5',outsider_count,'insider_margin',insider_count)
print('unique_closed_margin_zero',endpoint_zeros)
print('optimizer_witnesses',opt_witness)
print('boundary_B0_D528_eta',boundary_eta,'boundary_near',sorted(near))
print('pointwise_B<=20_upper_exit_D','528+2B')
