#!/usr/bin/env python3
"""Exact rational certificate for a two-history shared-gate BRC direction.
Independent tests use only Python's standard library and Fraction.
"""
from fractions import Fraction as F
from itertools import product

R2=(F(3,4),F(5,4)); Q2=(F(1,2),F(1,2))
R3=(F(1,2),F(1),F(3,2))
Q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
R4=(F(1,10),F(1),F(19,10))
Q4={
  (0,0):(F(509,900),F(382,900),F(9,900)),
  (1,0):(F(509,900),F(382,900),F(9,900)),
  (0,2):(F(9,900),F(382,900),F(509,900)),
  (1,2):(F(9,900),F(382,900),F(509,900)),
  (0,1):(F(1,90),F(44,45),F(1,90)),
  (1,1):(F(67,162),F(14,81),F(67,162)),
}
N=(F(-1),F(-1),-F(3,25),F(1,50))

def dot(x,y=N): return sum((a*b for a,b in zip(x,y)), F(0))
def plus(x,y):return tuple(a+b for a,b in zip(x,y))
def minus(x,y):return tuple(a-b for a,b in zip(x,y))

def W_gate(a,b,z):
    out=[F(0)]*4
    def add(q,r,t):
        # Bayes stop-declaration, ties r=1 -> Q
        for k,v in enumerate((q*r if r<=1 else F(0),q if r>1 else F(0),q*r*t,q*t)):
            out[k]+=v
    for i,(r2,q2) in enumerate(zip(R2,Q2)):
        ai=(a,b)[i]
        add(q2*(1-ai),r2,2)
        for j,(r3,q3) in enumerate(zip(R3,Q3[i])):
            q=q2*ai*q3
            zz=z if j==1 else F(0)
            add(q*(1-zz),r3,3)
            for r4,q4 in zip(R4,Q4[i,j]):
                add(q*zz*q4,r4,4)
    return tuple(out)

def terminal_W(actions):
    # deterministic seedless policy choices at t1,t2,t3,t4; Q/P/C for nonterminal
    t1,t2,t3,t4=actions
    out=[F(0)]*4
    def add(q,r,t,decision):
        for k,v in enumerate((q*r if decision=='Q' else F(0),q if decision=='P' else F(0),q*r*t,q*t)):
            out[k]+=v
    if t1!='C':
        add(F(1),F(1),1,t1)
    else:
        for i,(r2,q2) in enumerate(zip(R2,Q2)):
            if t2[i]!='C': add(q2,r2,2,t2[i]); continue
            for j,(r3,q3) in enumerate(zip(R3,Q3[i])):
                q=q2*q3
                if t3[j]!='C': add(q,r3,3,t3[j]); continue
                for k,(r4,q4) in enumerate(zip(R4,Q4[i,j])):
                    add(q*q4,r4,4,t4[k])
    return tuple(out)

def full_dp():
    def leaf(r,t):return max(N[0]*r+(N[2]*r+N[3])*t, N[1]+(N[2]*r+N[3])*t)
    def h3(i,j):
        r=R3[j]
        cont=sum(Q4[i,j][k]*leaf(r4,4) for k,r4 in enumerate(R4))
        return max(leaf(r,3),cont)
    def h2(i):
        r=R2[i]
        return max(leaf(r,2),sum(Q3[i][j]*h3(i,j) for j in range(3)))
    return max(leaf(F(1),1),sum(Q2[i]*h2(i) for i in range(2)))

# Each conditional P row is Q(s|h)*s/r and normalized.
for r, row, svals in [*( (R2[i],Q3[i],R3) for i in range(2)),*( (R3[j],Q4[i,j],R4) for i in range(2) for j in range(3))]:
    assert all(x>0 for x in row)
    assert sum(row)==1
    assert sum((x*s for x,s in zip(row,svals)),F(0))==r
assert sum(Q2)==1 and sum(q*r for q,r in zip(Q2,R2))==1

W0=W_gate(F(0),F(0),F(0))
B1=minus(W_gate(F(1),F(0),F(0)),W0)
B2=minus(W_gate(F(0),F(1),F(0)),W0)
C1=minus(W_gate(F(1),F(0),F(1)),W_gate(F(1),F(0),F(0)))
C2=minus(W_gate(F(0),F(1),F(1)),W_gate(F(0),F(1),F(0)))
assert W0==(F(3,8),F(1,2),F(2),F(2))
assert B1==(-F(9,80),F(3,40),F(3,8),F(1,2))
assert C1==(-F(19,9000),F(1,900),F(1,10),F(1,10))
assert B2==(F(37,160),-F(19,80),F(5,8),F(1,2))
assert C2==(-F(1273,7200),F(67,720),F(9,40),F(9,40))
assert (dot(B1),dot(C1),dot(B2),dot(C2))==(F(1,400),-F(9,1000),-F(47,800),F(49,800))
assert (dot(B1),-dot(C1),dot(plus(B2,C2)),dot(C2))==(F(1,400),F(9,1000),F(1,400),F(49,800))

best=None; count=0
for t1 in ('Q','P','C'):
 for t2 in product(('Q','P','C'),repeat=2):
  for t3 in product(('Q','P','C'),repeat=3):
   for t4 in product(('Q','P'),repeat=3):
    val=dot(terminal_W((t1,t2,t3,t4)))
    best=val if best is None or val>best else best
    count+=1
assert count==5832
assert best==-F(429,400)
full=full_dp()
assert full==-F(107,100)
gap=full-best
assert gap==F(1,400)
assert gap==min(dot(B1),-dot(C1),dot(plus(B2,C2)),dot(C2))
# Exact Gordan alternative example: co-oriented nonzero increments.
U=(F(0),F(0),F(1),F(0))
M=( (F(1),F(0),F(0),F(0)),tuple(-x for x in U),
    (F(0),F(1),F(1),F(0)),U )
assert all(sum((weight*M[k][j] for k,weight in enumerate((0,1,0,1))),F(0))==0 for j in range(4))
# Universal support-gap robustness for any direction within the radius:
# an O4 vector has coordinates in [0,1]^2 x [1,4]^2,
# so the oscillation of delta*n between any two vectors is <= 8||delta||_infty.
radius=F(1,6400)
assert gap-8*radius==F(1,800)
print('PASS_EXACT_R5_PAIRWISE_GORDAN_AND_ROBUST_CONE')
print('seedless_LR_deterministic_policy_count=',count)
print('W0=',tuple(map(str,W0)))
for label,v in [('B1',B1),('C1',C1),('B2',B2),('C2',C2)]:
    print(label+'=',tuple(map(str,v)))
print('four_strict_inequality_margins=',tuple(map(str,(dot(B1),-dot(C1),dot(plus(B2,C2)),dot(C2)))))
print('h_LR=',str(best),'h_FULL_HIST=',str(full),'gap=',str(gap))
print('open_ball_radius_sup_norm=',str(radius),'gap_lower_bound=',str(gap-8*radius))
print('cooriented_dual_lambda= (0,1,0,1)')
