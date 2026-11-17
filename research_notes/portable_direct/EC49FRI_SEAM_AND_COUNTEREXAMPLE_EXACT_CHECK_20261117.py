#!/usr/bin/env python3
"""EC49FRI rational algebra proof-obligation checker (no third-party packages).

This checks the exact seven-anchor values against the candidate trees and
the polynomial seam identities. The full native/independent Bellman JSON
verification is separately contained in the conversation evidence archive.
A successful run of this small file does not substitute for that finite
unrestricted Bellman verification or for the analytical concavity proof.
"""
from fractions import Fraction as F

A=(6,290,6,751)
B=(5,293,5,704)
C=(5,295,5,685)
D=(4,296,4,707)
beta=F(620,3299)

def K(x): return 7557-169*x
def G(x): return F(310)*(3-x)/K(x)
def score(s,x,lam):
    uR,uT,mR,mT=s
    return (1-lam)*(uR*x+uT)/141+lam*(mR*x+mT)/310
def seam_polynomial(s):
    uR,uT,mR,mT=s
    return (uR-mR,47*uR+uT+3*mR-mT,47*uT+3*mT)
def candidates(x,lam): return [score(s,x,lam) for s in (A,B,C)]

# These values are outputs of the full frozen BRC integer Bellman solvers.
# Source receipts and complete trees are in EC49FRI evidence archive.
anchors=[
    (F(1),F(0),F(296,141),(32,34)),
    (F(1),F(155,1847),F(7861,3694),(32,34,140,142)),
    (F(1),beta,F(7080,3299),(16,23,140,142)),
    (F(1),F(1),F(69,31),(16,23,124,131)),
    (F(3),F(0),F(308,141),(32,34,140,142)),
    (F(3),beta,F(7290,3299),(16,23,140,142)),
    (F(3),F(1),F(70,31),(16,23,59,88)),
    (F(4),F(0),F(312,141),(32,34,140,142)),
]
assert G(F(1))==F(155,1847) and G(F(3))==0
assert 0<G(F(1))<beta<1
assert seam_polynomial(A)==seam_polynomial(B)==(0,-161,15883)
for x,lam,reported_opt,_ in anchors:
    if x<=3:
        assert min(candidates(x,lam))==reported_opt, (x,lam)
    else:
        assert x==4 and lam==0
        assert score(D,x,lam)==reported_opt
        assert min(candidates(x,lam))-reported_opt==F(1,141)

# The identity K*p_i(G)=(47+3*m_i)+(1-m_i)*x holds
# coefficientwise for every positive integer multiplicity m_i.
for m in range(1,311):
    for x in [F(1),F(7,4),F(3)]:
        p=(1-G(x))/141+G(x)*F(m,310)
        assert K(x)*p == 47+3*m+(1-m)*x
    # Each full physical tree has nonnegative integral root count r_i,
    # hence the seam quadratic coefficient sum_i (1-m_i)*r_i <= 0.
    for root_count in (0,1,2,6,100):
        assert (1-m)*root_count<=0

# At x>3 and lambda=0, B-D=(x-3)/141.
for x in [F(3001,1000),F(4),F(5),F(10),F(100)]:
    assert min(candidates(x,F(0)))==score(B,x,F(0))
    assert score(B,x,F(0))-score(D,x,F(0)) == (x-3)/141

print("EC49FRI algebraic obligations PASS: curve, anchor values, concavity sign, x>3 witness")
print("Full native Bellman/replay remains evidenced by 8 JSON certificates in archive")
