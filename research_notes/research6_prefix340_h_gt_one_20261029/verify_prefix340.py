#!/usr/bin/env python3
"""PREFIX-340 exact rational audit; Python 3 + sympy.
Frozen global six-orbit exhaustiveness from PREFIX-339.
No floating point predicates, no phase angle grid.
"""
from itertools import combinations, product
from sympy import Matrix, Rational as Q, I, conjugate, simplify
import json
from pathlib import Path

A=Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
          [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
lam=Q(10,61); rho=Q(1,10**8)
b=[1360,128,2330,1864,1261]
q=[lam**2*Q(x,64) for x in b]
assert all(0<x<1 for x in q)
C=[[Q(v) for v in row] for row in [
 ['-9.872155986','-0.497496459','0.991123454','-1.977834057','3.013046410'],
 ['-9.851679166','0.672017894','0.997408380','1.897396211','3.094999288'],
 ['-6.837934178','6.406340759','1.820539644','1.328370101','4.317624519'],
 ['3.972277190','-3.655156020','5.069231734','1.852070781','7.206948698'],
 ['3.826943394','0.866306597','5.391314313','-1.020335300','8.029290029'],
 ['3.472972568','1.984555753','5.333493587','0.744208408','8.062257748']]]
def ri(z):
    return simplify((z+conjugate(z))/2),simplify((z-conjugate(z))/(2*I))
def src(v):return Matrix([v[0]+I*v[1],v[2]+I*v[3],v[4]])
def nsq(v):return simplify(sum(x*x+y*y for x,y in (ri(z) for z in v)))

# 45 ordered, provenance-preserving path-pair contributions.
a0=Matrix([4,5-2*I,7-4*I]); pairs=0
for j in range(5):
    z=[A[j,k]*a0[k] for k in range(3)]
    assert simplify(sum(z[k]*conjugate(z[l])
                        for k,l in product(range(3),repeat=2)))==b[j]
    pairs+=9
assert pairs==45
assert all(simplify(A[list(ix),:].det())!=0
           for ix in combinations(range(5),3))

# Recompute a Banach existence/uniqueness argument for C4 and C5.
R=[];S=[]
for j in range(5):
    rr=[];ss=[]
    for k in (0,1):
        x,y=ri(A[j,k]);rr.extend((x,-y));ss.extend((y,x))
    x,y=ri(A[j,2]);rr.append(x);ss.append(y)
    R.append(Matrix([rr]));S.append(Matrix([ss]))
H=[2*(R[j].T*R[j]+S[j].T*S[j]) for j in range(5)]
def banach(v):
    c=Matrix(v)
    F=Matrix([(R[j]*c)[0]**2+(S[j]*c)[0]**2-b[j] for j in range(5)])
    J=Matrix.vstack(*[2*((R[j]*c)[0]*R[j]+(S[j]*c)[0]*S[j])
                       for j in range(5)])
    assert J.det()!=0
    inv=J.inv()
    eta=max(abs(x) for x in inv*F)
    K=max(sum(abs(inv[i,j])*sum(abs(H[j][k,l]) for l in range(5))
              for j in range(5) for k in range(5)) for i in range(5))
    assert eta<Q(1,10**9) and K<30
    assert eta+K*rho**2/2<rho and K*rho<1 and v[4]>rho
    return {'eta':str(eta),'K':str(K)}
bo4,bo5=banach(C[3]),banach(C[4])
assert C[3][4]+rho<C[4][4]-rho

# The Nmax bound is conditional on PREFIX-339's six-orbit exhaustiveness.
bounds=[]
for v in C:
    mid=lam**2*sum(x*x for x in v)
    err=lam**2*(2*rho*sum(abs(x) for x in v)+5*rho**2)
    bounds.append((mid-err,mid+err))
M=max(x[1] for x in bounds)
assert M<Q(30014,10000)
u2=sum(A[2,k]*conjugate(A[2,k]) for k in range(3))/64
assert u2==Q(11,16)

def witness(zeta,eta,t,threshold):
    assert simplify(zeta*conjugate(zeta))==1
    assert simplify(eta*conjugate(eta))==1
    P=lam*zeta*src(C[3]);V=lam*eta*src(C[4])
    def port(phase,c):
        mid=ri(lam*phase*(A[2,:].dot(src(c)))/8)[1]
        x,y=ri(phase*A[2,0]);z=ri(phase*A[2,2])[1]
        err=lam*rho*(abs(x)+abs(y)+abs(z))/8
        return mid,err
    mp,ep=port(zeta,C[3]);mv,ev=port(eta,C[4])
    assert mp-ep>t and mv-ev>t and mp+ep<1 and mv+ev<1
    D=P-V
    d2=nsq(D)
    l1=sum(abs(x)+abs(y) for x,y in (ri(z) for z in D))
    epsilon=6*lam*rho
    low=(d2-2*epsilon*l1)/4
    high=(d2+2*epsilon*l1+epsilon**2)/4
    assert low>threshold
    return {'phase_4':str(zeta),'phase_5':str(eta),
        'im4_mid':str(mp),'im4_error':str(ep),
        'im5_mid':str(mv),'im5_error':str(ev),
        'h_upper':str(1+t),'MEB2_lower':str(low),
        'MEB2_upper':str(high),'strict_gt':str(threshold)}
wide=witness((24+7*I)/25,(-3-4*I)/5,Q(14,25),Q(62,25))
strong=witness((513+184*I)/545,(-133-156*I)/205,
               Q(51,100),Q(257,100))
L=Q(1062562,458329)
assert Q(257,100)>L and Q(62,25)>L
upper=M-Q(1,4)/u2
assert Q(257,100)<upper<Q(66,25)

output={'schema':'PREFIX340_EXACT_RATIONAL_REPRODUCER_V1',
 'status':'PASS_AUTHOR_SIDE_EXACT_RATIONAL_WITH_FROZEN_SIX_ORBIT_EXHAUSTIVENESS',
 'two_independently_checked_banach_boxes':[bo4,bo5],
 'BRC_ordered_path_pairs':pairs,'ten_full_spark_minors_nonzero':True,
 'q':[str(x) for x in q],'max_norm_squared_upper':str(M),
 'wide_h_witness':wide,'strong_h_witness':strong,
 'h_1p5_full_fibre_lower':'257/100',
 'h_1p5_full_fibre_upper':str(upper),
 'strict_simple_upper':'66/25','baseline_L':str(L),
 'dependency':'PREFIX339 six true phase-orbits exhaust full fibre',
 'non_antipodal':'For h>1 all feasible port3 imaginary coordinates strictly positive'}
dest=Path(__file__).with_name('REPRODUCER_RESULTS_PREFIX340.json')
dest.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(output['status'])
print('257/100 < MEB2(S(3/2)) < 66/25')
