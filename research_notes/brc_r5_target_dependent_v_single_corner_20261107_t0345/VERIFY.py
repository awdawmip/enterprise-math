"""Exact Fraction certificate: target-dependent v cannot improve the g=u0=1 LR cube.
Scientific inputs: frozen R5 P/Q kernel, δ=1/4; lower cube from commit 6f648b3c96a38cdaacda4633bee1cd5aba5904ff.
All-real proof is in RESEARCH.md; these exact calculations check identities and ray witnesses.
"""
from fractions import Fraction as F

W=(F(161801,180000),F(6499,18000),F(267,80),F(137,40))
D0=W[0]+W[1]-1
H=F(3543,3009580)
VSTAR=F(17741,21497)
R=(F(1,10),F(1,2),F(1),F(5,4),F(3,2),F(19,10))
def U1(v):return (1589-1661*v)/185360
def U2(v):return 3*(1113*v-887)/80360

def max_masses_at_positive_corner(v,h):
    v0=F(13,40)+v/80;v1=F(1,10)+9*v/40
    p=W[2]+h-(2+(3+5*v)/8)
    q=W[3]-h-(2+(1+v)/2)
    x0=3*q/2-p-v1/2
    x2=p-q/2-v1/2
    ma=F(509,900)*x0+F(47,1800)+67*v/720+x2/100
    mb=v0-x0
    return ma,mb

for v in (F(0),F(1)):
    for h in (F(0),F(1)):
        ma,mb=max_masses_at_positive_corner(v,h)
        assert ma==(8737-1661*v)/36000-F(1259,900)*h
        assert mb==(5*v-1)/20+F(5,2)*h
        d=D0+2*h;eq=W[1]+h
        assert eq/2+F(2,5)*ma-d==F(2317,1125)*(U1(v)-h)
        assert F(9,10)*ma+mb/2-d==F(2009,1000)*(U2(v)-h)

htrivial=1-W[0];vlow=F(17,40)-htrivial
assert htrivial==F(18199,180000) and vlow==F(58301,180000)
assert 1019*vlow>96
assert U1(VSTAR)==H==U2(VSTAR)
assert VSTAR>vlow and VSTAR<1
assert U1(F(0))>U1(F(1)) and U2(F(0))<U2(F(1))

def witness(t):
    v=VSTAR;h=H
    w=tuple(W[k]+h*t[k] for k in range(4))
    v0=F(13,40)+v/80;v1=F(1,10)+9*v/40;v2=F(3,40)+21*v/80
    x2=F(81993,1719760)+h*t[2]-h*t[3]/2
    x0=x2+2*(w[3]-2-(1+v)/2-(w[2]-2-(3+5*v)/8))
    x1=v1
    ea=F(78158903,386946000)+F(1181,902874)*(t[0]+t[1])-F(1181,1805748)*t[2]+F(1181,1203832)*t[3]
    d=w[0]+w[1]-1
    eb=2*d-F(9,5)*ea
    e1=w[1]-ea-eb
    m={
      F(1,10):F(509,900)*x0+x2/100+F(47,1800)+67*v/720,
      F(1,2):v0-x0,
      F(1):F(382,900)*(x0+x2)+F(43,900)+7*v/180,
      F(5,4):(1-v)/2,
      F(3,2):v2-x2,
      F(19,10):x0/100+F(509,900)*x2+F(47,1800)+67*v/720}
    e={r:F(0) for r in R}
    e[F(1,10)],e[F(1,2)],e[F(1)]=ea,eb,e1
    slacks=(x0,x1,x2,v0-x0,v1-x1,v2-x2)+tuple(e[r] for r in R)+tuple(m[r]-e[r] for r in R)
    assert all(s>=0 for s in slacks)
    assert sum(m.values())==1 and sum(r*m[r] for r in R)==1
    assert sum(e.values())==w[1] and 1-sum(r*e[r] for r in R)==w[0]
    assert 2+(1+v)/2+x0+x1+x2==w[3]
    assert 2+(3+5*v)/8+x0/2+x1+3*x2/2==w[2]
    return x0,x1,x2,ea,eb,e1,min(slacks)

for t in ((F(0),)*4,(F(1),F(1),F(1),F(-1))):
    x0,x1,x2,ea,eb,e1,slack=witness(t)
    print('EXACT_WITNESS',tuple(map(str,t)),'X',x0,x1,x2,'E',ea,eb,e1,'MIN_SLACK',slack)
print('FROZEN_GLOBAL_PIN a01383f825ef9d43b4b754254303298c64041568')
print('FROZEN_EM_PIN 86149263e38c22292c9def1e0f69092efa1be77e')
print('PRIOR_VERIFIED_LOWER_COMMIT 6f648b3c96a38cdaacda4633bee1cd5aba5904ff')
print('SAME_CORNER (+,+,+,-) CAPACITY_1','2317/1125*(U1(v)-h)')
print('SAME_CORNER (+,+,+,-) CAPACITY_2','2009/1000*(U2(v)-h)')
print('ALL_REAL_VARIABLE_V_OPTIMUM',H,'AT',VSTAR)
print('PROVED_SUBFAMILY g=u0=1; v may depend arbitrarily on W; all six LR declaration keys')
print('PASS_EXACT_R5_TARGET_DEPENDENT_V_SINGLE_CORNER_OPTIMUM')
