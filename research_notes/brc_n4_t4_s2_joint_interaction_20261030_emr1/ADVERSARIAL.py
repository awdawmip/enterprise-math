"""Independent four-atom rational audit for the S2-only interaction witness.
This checker uses BU j masses directly, not the VERIFY.py leaf generator.
"""
from fractions import Fraction as F
from itertools import product

J_P=(F(1,40),F(9,40))
J_Q=(F(1,8),F(1,8))
# k=0: j0 decides P and j1 decides Q; k=1: reversed.
D={(0,0):'P',(0,1):'Q',(1,0):'Q',(1,1):'P'}

def output(jlaw):
    return {(d,k):sum((jlaw[j]/2 for j in range(2) if D[j,k]==d),F(0))
            for d,k in product(('P','Q'),(0,1))}
p,q=output(J_P),output(J_Q)
assert sum(p.values())==sum(q.values())==F(1,4)
for d in ('P','Q'):
    assert sum(p[d,k] for k in (0,1))==sum(q[d,k] for k in (0,1))==F(1,8)
for k in (0,1):
    assert sum(p[d,k] for d in ('P','Q'))==sum(q[d,k] for d in ('P','Q'))==F(1,8)
delta={(d,k):p[d,k]-q[d,k] for d,k in p}
assert delta=={('P',0):-F(1,20),('P',1):F(1,20),
               ('Q',0):F(1,20),('Q',1):-F(1,20)}
tv=sum((abs(x) for x in delta.values()),F(0))/2
assert tv==F(1,10)
mid={i:(p[i]+q[i])/2 for i in p}
for law in (p,q):
    assert sum((abs(law[i]-mid[i]) for i in mid),F(0))/2==F(1,20)
# Condition on each j, a shared k~Bernoulli(1/2) and the same j,k decision map.
for mass in (J_P,J_Q):
    assert output(mass)==(p if mass==J_P else q)
print('PASS_ADVERSARIAL_BU_S2_JOINT_ONLY_INTERACTION; atom_delta=checkerboard(+/-1/20); marginal_TV=0; joint_TV=1/10; radius=1/20')
