"""R5 exact 15% enlarged seedless LR cube certificate; only rational arithmetic."""
from fractions import Fraction as Q
from itertools import product

q3 = ((Q(13,20),Q(1,5),Q(3,20)), (Q(1,40),Q(9,20),Q(21,40)))
q4 = (
 ((Q(509,900),Q(382,900),Q(9,900)),(Q(47,180),Q(43,90),Q(47,180)),(Q(9,900),Q(382,900),Q(509,900))),
 ((Q(509,900),Q(382,900),Q(9,900)),(Q(67,162),Q(14,81),Q(67,162)),(Q(9,900),Q(382,900),Q(509,900))),
)
r2=(Q(3,4),Q(5,4));r3=(Q(1,2),Q(1),Q(3,2));r4=(Q(1,10),Q(1),Q(19,10))
R=tuple(sorted(set((Q(1),)+r2+r3+r4)))
v=Q(33,40)
h=Q(23,20000)
W0=(Q(161801,180000),Q(6499,18000),Q(267,80),Q(137,40))
V=tuple((q3[0][j]+v*q3[1][j])/2 for j in range(3))
assert V==(Q(1073,3200),Q(457,1600),Q(933,3200))
for i in range(2):
    assert sum(q3[i])==1 and all(x>0 for x in q3[i])
    assert sum(q3[i][j]*r3[j] for j in range(3))==r2[i]
    for j in range(3):
        assert sum(q4[i][j])==1 and all(x>0 for x in q4[i][j])
        assert sum(q4[i][j][z]*r4[z] for z in range(3))==r3[j]

# Each real t-coordinate lies in [-1,1].
def witness(t):
    assert len(t)==4
    W=tuple(W0[k]+h*t[k] for k in range(4))
    X2=(Q(51487)-Q(1824)*t[0]-Q(1824)*t[1]+Q(1150)*t[2]-Q(559)*t[3])/1000000
    Ea=(Q(204079)+Q(264)*t[0]+Q(264)*t[1]-Q(639)*t[2]+Q(967)*t[3])/1000000
    tp=W[2]-(2+(3+5*v)/8)
    tq=W[3]-(2+(1+v)/2)
    X0=X2+2*(tq-tp)
    X1=2*tp-tq-2*X2
    D=W[0]+W[1]-1
    Eb=2*D-Q(9,5)*Ea
    E1=W[1]-Ea-Eb
    X=(X0,X1,X2)
    E={r:Q(0) for r in R}
    E[Q(1,10)],E[Q(1,2)],E[Q(1)]=Ea,Eb,E1
    M={r:Q(0) for r in R}
    M[Q(5,4)]+=(1-v)/2
    for j in range(3):
        M[r3[j]]+=V[j]-X[j]
        for i in range(2):
            xij=(Q(1) if i==0 else v)*q3[i][j]*X[j]/(2*V[j])
            for z in range(3):
                M[r4[z]]+=xij*q4[i][j][z]
    assert sum(M.values())==1
    assert sum(r*M[r] for r in R)==1
    assert (1-sum(r*E[r] for r in R),sum(E.values()))==W[:2]
    assert (2+(3+5*v)/8+X[0]/2+X[1]+Q(3,2)*X[2],
            2+(1+v)/2+sum(X))==W[2:]
    slacks=X+tuple(V[j]-X[j] for j in range(3))+(Ea,Eb,E1)+(
        M[Q(1,10)]-Ea,M[Q(1,2)]-Eb,M[Q(1)]-E1)
    return slacks

labels=['X0','X1','X2','V0-X0','V1-X1','V2-X2','Ea','Eb','E1','M_a-Ea','M_b-Eb','M_1-E1']
mins=[min(witness(tuple(map(Q,t)))[i] for t in product((-1,1),repeat=4)) for i in range(12)]
assert mins==[
 Q(88099,500000),Q(67737,250000),Q(4613,100000),
 Q(292073,2000000),Q(21,1000000),Q(469437,2000000),
 Q(40389,200000),Q(730087,5000000),Q(2393,22500000),
 Q(1207849,68550000000),Q(31,2000000),Q(298306313,1713750000)]
assert min(mins)>0
for t in product((-1,Q(-1,2),Q(0),Q(1,2),Q(1)),repeat=4):
    assert min(witness(t))>0
print('MODEL', 'four-stage delta=1/4 g=u0=1 u1=33/40')
print('CENTER', *W0)
print('RADIUS',h,'PREVIOUS',Q(1,1000),'EXACT_GAIN',h/Q(1,1000))
print('AFFINE_X2_NUMERATOR', [51487,-1824,-1824,1150,-559], 'DENOMINATOR', 1000000)
print('AFFINE_Ea_NUMERATOR', [204079,264,264,-639,967], 'DENOMINATOR', 1000000)
for k,s in zip(labels,mins):print('MIN_SLACK',k,s)
print('CORNERS',16,'INDEPENDENT_GRID',625,'MIN_MARGIN',min(mins))
print('PASS_EXACT_R5_THREE_KEY_CUBE_RADIUS_23_OVER_20000')
