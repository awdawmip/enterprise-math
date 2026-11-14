"""PREFIX-778: sharp robustness radius for reflection-equivariant readout of four frozen Gamma cells.
Frozen input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
External killed-Pascal + independent unit Gamma clocks only; author-level exact integer evidence.
No native X6 comparator computation or task-claim is asserted.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
from decimal import Decimal, localcontext
import json
from pathlib import Path

N, DEN, W = 189, 768, 1 << 18
@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k)>W**n
@lru_cache(None)
def wide(n,k):
    if 2*k>n:return wide(n,n-k)
    m=k*W//n
    assert inside(n,k,m)
    if k==0:lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if inside(n,k,t):b=t
            else:a=t
        lo,hi=a,b
    a,b=m,W
    while b-a>1:
        t=(a+b)//2
        if inside(n,k,t):a=t
        else:b=t
    if 4*(a-hi)>W:return True
    if 4*(b-lo)<W:return False
    raise ValueError((n,k))

rows=[{0:1}]
for n in range(1,N+1):
    nxt=defaultdict(int)
    for k,c in rows[-1].items():
        nxt[k]+=c;nxt[k+1]+=c
    rows.append({k:c for k,c in nxt.items() if wide(n,k)})
assert not rows[N] and sum(map(len,rows[:N]))==9529
for n,row in enumerate(rows[:N]):
    assert all(row.get(k,0)==row.get(n-k,0) for k in row)
E=DEN**188; H=E*E*(1<<377)
K=[[comb(i+j,i)<<(376-i-j) for j in range(N)] for i in range(N)]
@lru_cache(None)
def surv(a):
    pa=[1];pb=[1];pd=[1]
    for i in range(N):
        pa.append(pa[-1]*a);pb.append(pb[-1]*(DEN-a));pd.append(pd[-1]*DEN)
    return [sum(c*pa[k]*pb[n-k] for k,c in row.items())*pd[188-n] for n,row in enumerate(rows[:N])]

def B(s,t,order=0):
    return sum(si*sum(kij*(i+j+1 if order else 1)*tj for j,(kij,tj) in enumerate(zip(K[i],t)) if tj)
               for i,si in enumerate(s) if si)

@lru_cache(None)
def moment(a,b):
    s,t=surv(a),surv(b)
    mu=(sum(s)+sum(t))*E*(1<<377)-B(s,t)
    m2=2*(sum((i+1)*v for i,v in enumerate(s))+sum((j+1)*v for j,v in enumerate(t)))*E*(1<<377)-B(s,t,1)
    return mu,m2*H-mu*mu

def diff(k,l):
    p00=moment(k,l);p10=moment(k+1,l);p01=moment(k,l+1);p11=moment(k+1,l+1)
    return tuple(p11[i]-p10[i]-p01[i]+p00[i] for i in (0,1))

d38,d39=diff(38,38),diff(39,39)
for d in (d38,d39):assert d[0]<0 and d[1]<0
assert diff(38,729)==tuple(-x for x in d38)
assert diff(39,728)==tuple(-x for x in d39)
# dmu/H and dw/H^2 are the physical mixed differences.
a38,a39=-d38[0],-d39[0]
b38,b39=-d38[1],-d39[1]
# r39>r38 iff H*(a39*b38-a38*b39)>0; common H cancels.
J=a39*b38-a38*b39
assert J>0
# Certify both |Delta variance| > 1/6.
assert 6*b38>H*H and 6*b39>H*H
# C=(b38*b39/(b38+b39))*(H*a39/b39-H*a38/b38)
#   = H*(a39*b38-a38*b39)/(b38+b39) / H^2 = J/(H*(b38+b39))
# (since a are numerators of mu, b of variance).
Cnum=J
Cden=H*(b38+b39)
assert Cnum>0 and Cden>0
# A simple strong bound with exact integer cross multiplication:
assert Cnum*10**8>27*Cden  # C > 2.7e-7.
assert Cnum*10**9<271*Cden # C < 2.71e-7.
# q0=(A38+A39)/(B38+B39)=H*(a38+a39)/(b38+b39)
q0_num=H*(a38+a39);q0_den=b38+b39
assert q0_num*b38>H*a38*q0_den  # r38<q0
assert q0_num*b39<H*a39*q0_den  # q0<r39
# Universal proof: for all real q, max(B38|q-r38|,B39|q-r39|) >= C.
# Equality exactly at q=q0, with opposite signed differences on R38/R39.
# Mirror cells give equal-magnitude opposite signs even at endpoints.

# The base diagonal squares R38 and R39 share only vertex (39,39).
# Under exact scalar reflection, both mirror mixed differences negate the bases.
# With per-corner error bounded by q*epsilon, the two base increments
# can be made zero simultaneously iff epsilon dominates
# max(|x38|/4,|x39|/4,|x39-x38|/6),
# where xk=A_k-q*B_k and A_k=-Delta(mu), B_k=-Delta(variance).
assert b39>b38>0
# Exact sharp radius: (A39*B38-A38*B39)/(2*(B38+2*B39)).
Rnum=J
Rden=2*H*(b38+2*b39)
assert Rnum>0 and Rden>0
# Strict rational bracket: 9.020758537e-8 < radius < 9.020758538e-8.
assert 9020758537*Rden < 10**17*Rnum < 9020758538*Rden
# Sharp q=(A38+2*A39)/(B38+2*B39).
qs_num=H*(a38+2*a39); qs_den=b38+2*b39
assert qs_num*b38>H*a38*qs_den
assert qs_num*b39<H*a39*qs_den
# Physical x_i=(a_i*H*qs_den-qs_num*b_i)/(H^2*qs_den)
X1=a38*H*qs_den-qs_num*b38
X2=a39*H*qs_den-qs_num*b39
assert X1<0<X2 and -X1==2*X2
# At the minimax intersection both |x38|/4 and |x39-x38|/6
# equal Rnum/Rden; |x39|/4 is strictly smaller.
assert (-X1)*Rden==4*Rnum*H**2*qs_den
assert (X2-X1)*Rden==6*Rnum*H**2*qs_den
assert 4*Rnum*Cden>Cnum*Rden
with localcontext() as ctx:
    ctx.prec=55
    dec=lambda a,b: str(Decimal(a)/Decimal(b))
    result={
      'schema':'PREFIX778_R6_REFLECTION_EQUIVARIANT_CORNER_RADIUS_V1',
      'date':'2026-11-14',
      'frozen_scientific_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'scope':'189-layer killed Pascal, two independent unit-rate Gamma clocks, four 1/768 grid cells',
      'survivor_nonzero_positions':9529,
      'cells':[[38,38],[39,39],[38,729],[39,728]],
      'B39_gt_B38_exact':True,
      'radius_exact_num':str(Rnum),
      'radius_exact_den':str(Rden),
      'radius_decimal':dec(Rnum,Rden),
      'radius_strict_bounds':['9020758537/10^17','9020758538/10^17'],
      'q_star_exact_num':str(qs_num),
      'q_star_exact_den':str(qs_den),
      'q_star_decimal':dec(qs_num,qs_den),
      'previous_C_four_decimal':dec(Cnum,Cden),
      'improvement_over_original_C_four_div_4':dec(4*Rnum*Cden,Cnum*Rden),
      'hypothesis':'For every relevant vertex, Vhat_q(p,1-z)=Vhat_q(p,z) and |Vhat_q-V_q|<=q*epsilon.',
      'theorem':'For all q>0, every epsilon<radius forces strict positive and negative mixed differences among the four fixed cells. The radius is optimal: at q_star an exact symmetric vertex perturbation erases all four differences.',
      'overlap_feasibility':'Cancellation of both base cells iff epsilon >= max(|x38|/4,|x39|/4,|x39-x38|/6).',
      'original_comparator_exclusion_count_increment':0,
      'verification':'ALL_CHECKS_PASS PREFIX778 REFLECTION_EQUIVARIANT_RADIUS',
      'status':'AUTHOR_EXACT_INTEGER_ALGEBRAIC_CERTIFICATE / UNREVIEWED / NOT_ADMITTED',
      'open':'Test typed signed-port/source-preserving native reflection and its verified scalar observation error bound.'
    }
Path(__file__).with_name('PREFIX778_R6_REFLECTION_EQUIVARIANT_RADIUS_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('radius_decimal','q_star_decimal','improvement_over_original_C_four_div_4','verification')},indent=2))
