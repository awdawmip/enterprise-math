#!/usr/bin/env python3
"""Deterministic regression for the D25 period-tail jet gluing theorem.

The proof is the finite-tail quotient identity and its parameter derivatives in
d25_period_tail_jet_gluing_no_new_constraint_20260924.md.
"""
import sympy as sp

# Symbolic adjoint identities.
r0,r1,r2,C,A,w = sp.symbols('r0 r1 r2 C A w')
Z0,Z1,Z2,Z0n,Z1n,Z2n = sp.symbols('Z0 Z1 Z2 Z0n Z1n Z2n')
a1=r1/6
b2=r2/36

# Tail-quotient jet equations:
# r0*Z0n-Z0=-1
# r0*Z1n+r1*Z0n-Z1=0
# r0*Z2n+2*r1*Z1n+2*r2*Z0n-Z2=0
lx,lxn=-C*Z2/72,-C*Z2n/72
ly,lyn=-C*Z1/6,-C*Z1n/6
lz,lzn=-C*Z0,-C*Z0n
q2 = sp.expand(r0*lzn-lz).subs(r0*Z0n,Z0-1)
q1 = sp.expand(r0*lyn+a1*lzn-ly).subs(r0*Z1n,Z1-r1*Z0n)
q0 = sp.expand(r0*lxn+a1*lyn+b2*lzn-lx).subs(
    r0*Z2n,Z2-2*r1*Z1n-2*r2*Z0n)
assert sp.simplify(q2-C)==0
assert sp.simplify(q1)==0
assert sp.simplify(q0)==0

# Weighted q1 tail identity.
W0,W1,W0n,W1n=sp.symbols('W0 W1 W0n W1n')
wx,wxn=-A*W1/6,-A*W1n/6
wy,wyn=-A*W0,-A*W0n
w1=sp.expand(r0*wyn-wy).subs(r0*W0n,W0-w)
w0=sp.expand(r0*wxn+a1*wyn-wx).subs(r0*W1n,W1-r1*W0n)
assert sp.simplify(w1-A*w)==0
assert sp.simplify(w0)==0

# Exact removable-edge charts for small integer m.
a=sp.symbols('a')
def T(m,k):
    out=sp.Integer(1)
    for j in range(k):
        out*=(-m+a+j)*(-2*m+2*a+j)
    return sp.expand(out/(sp.factorial(k)**2*2**k))

for m in range(1,6):
    terms=[T(m,k) for k in range(2*m+1)]
    q0s=[t.subs(a,0) for t in terms]
    q1s=[sp.diff(t,a).subs(a,0)/6 for t in terms]
    for k in range(2*m+1):
        tail=sp.expand(sum(terms[k:]))
        Z=sp.cancel(tail/terms[k])
        lim=sp.limit(Z,a,0)
        if k<=m:
            expected=sp.simplify(sum(q0s[k:m+1])/q0s[k])
        else:
            expected=sp.simplify(sum(q1s[k:2*m+1])/q1s[k])
        assert sp.simplify(lim-expected)==0
    assert sp.simplify(sp.cancel(terms[-1]/terms[-1])-1)==0

print('PASS: q2 tail-jet adjoint, weighted-q1 tail adjoint, and removable zero-edge charts verified')
