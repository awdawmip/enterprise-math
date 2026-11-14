"""Exact R5 seedless-LR ray extension beyond the g=u0=1 ceiling.
All numerical certificates use Python Fraction, no floating-point inference.
Scientific frozen pins: global a01383f825ef9d43b4b754254303298c64041568;
EM 86149263e38c22292c9def1e0f69092efa1be77e.
"""
from fractions import Fraction as F

H = F(3543, 3009580)
h = F(9, 2500)
g = u0 = u1 = F(77, 80)
Wstar = (F(161801, 180000), F(6499, 18000), F(267, 80), F(137, 40))
R2 = (F(3, 4), F(5, 4))
R3 = (F(1, 2), F(1), F(3, 2))
R4 = (F(1, 10), F(1), F(19, 10))
Q3 = ((F(13, 20), F(1, 5), F(3, 20)),
      (F(1, 40), F(9, 20), F(21, 40)))
Q4 = ((F(509, 900), F(382, 900), F(9, 900)),
      (F(47, 180), F(43, 90), F(47, 180)),
      (F(67, 162), F(14, 81), F(67, 162)),
      (F(9, 900), F(382, 900), F(509, 900)))
R = (F(1, 10), F(1, 2), F(3, 4), F(1), F(5, 4), F(3, 2), F(19, 10))

for i in range(2):
    assert sum(Q3[i]) == 1 and sum(a*b for a,b in zip(R3,Q3[i])) == R2[i]
for j in range(3):
    for row in ([Q4[0]] if j == 0 else [Q4[3]] if j == 2 else [Q4[1], Q4[2]]):
        assert sum(row) == 1 and sum(a*b for a,b in zip(R4,row)) == R3[j]

v = tuple(sum(ui*Q3[i][j]/2 for i,ui in enumerate((u0,u1))) for j in range(3))
assert 0 <= u0 <= g <= 1 and 0 <= u1 <= g

def check(x, labels, expected):
    assert all(0 <= x[j] <= v[j] for j in range(3))
    mass = {r:F(0) for r in R}
    mass[F(1)] += 1-g
    for i,ui in enumerate((u0,u1)):
        mass[R2[i]] += (g-ui)/2
    for j in range(3):
        mass[R3[j]] += v[j]-x[j]
        z = x[j]/v[j]
        for i,ui in enumerate((u0,u1)):
            row = Q4[0] if j == 0 else Q4[3] if j == 2 else Q4[i+1]
            for k in range(3):
                mass[R4[k]] += (ui*Q3[i][j]/2)*z*row[k]
    assert sum(mass.values()) == 1
    assert sum(r*mass[r] for r in R) == 1
    E = {r:labels.get(r,F(0)) for r in R}
    assert all(0 <= E[r] <= mass[r] for r in R)
    eP = 1-sum(r*E[r] for r in R)
    eQ = sum(E.values())
    TP = 1+g+(3*u0+5*u1)/8+x[0]/2+x[1]+3*x[2]/2
    TQ = 1+g+(u0+u1)/2+sum(x)
    assert (eP,eQ,TP,TQ) == expected
    return mass,E

x_center = (F(3,16), F(3,10), F(1,80))
e_center = {F(1,10):F(1297,6000), F(1,2):F(879,6400),
            F(1):F(563,144000), F(19,10):F(349,96000)}
m_center,E_center = check(x_center,e_center,Wstar)
x_ray = (F(1723,10000), F(781,2500), F(117,10000))
e_ray = {F(1,10):F(458111,2160000), F(1,2):F(24407,160000),
         F(1):F(221,10800000), F(3,2):F(7,2400000)}
w_ray=tuple(Wstar[k]+h*s for k,s in enumerate((1,1,1,-1)))
m_ray,E_ray = check(x_ray,e_ray,w_ray)
assert h > H and h/H == F(451437,147625)
# Fix g=u0=u1=77/80. On the line between both exact policies,
# the three pooled LR continuation flows and declarations interpolate;
# each stopped mass is affine in those flows, so all 0<=s<=1 are legal.
for s in (F(0), F(1,4), F(1,2), F(3,4), F(1)):
    xs=tuple((1-s)*x_center[j]+s*x_ray[j] for j in range(3))
    es={r:(1-s)*E_center[r]+s*E_ray[r] for r in R}
    ws=tuple(Wstar[k]+s*h*t for k,t in enumerate((1,1,1,-1)))
    check(xs,es,ws)

print('FROZEN_GLOBAL_PIN a01383f825ef9d43b4b754254303298c64041568')
print('FROZEN_EM_PIN 86149263e38c22292c9def1e0f69092efa1be77e')
print('SEEDLESS_LR_BRANCH g=u0=u1',g)
print('Q_TIME3_CAPACITIES',','.join(map(str,v)))
print('CENTER_CONTINUE',','.join(map(str,x_center)))
print('RAY_CONTINUE',','.join(map(str,x_ray)))
print('RAY_STOPPED_Q_MASSES',' '.join(f'{r}:{m_ray[r]}' for r in R))
print('RAY_DECLARE_P_Q_MASSES',' '.join(f'{r}:{E_ray[r]}' for r in R))
print('CENTER_AND_RAY_PROBABILITIES_AND_MOMENTS_EXACT',True)
print('RAY_FOUR_OBSERVERS',','.join(map(str,w_ray)))
print('PREDECESSOR_RESTRICTED_BOUND',H,'NEW_RAY_H',h,'RATIO',h/H)
print('ALL_REAL_RAY_SEGMENT_CONSTRUCTED_BY_AFFINE_POLICY_INTERPOLATION',True)
print('SCOPE early-stop freedom; one ray segment, not centered 4D cube nor FULL-v-LR separation')
print('PASS_EXACT_R5_UNRESTRICTED_EARLY_CONTINUATION_RAY_BREACH')
