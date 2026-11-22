#!/usr/bin/env python3
"""Exact q0-only maximal-13 obstruction for frozen T6 (author calculation).
Requires SymPy; exact integer modular operations, exact HNF/LLL and fractions.
"""
from fractions import Fraction
from math import prod
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

P, CAP = 13, 2331
N = P - 1
W = [P*r-1 for r in range(1,P)]
A = [[int(i == j) for j in range(N)] for i in range(N)]
for k in range(1, 7):
    mod = P**k
    h = [pow(r, -k, mod) for r in range(1,P)]
    residues = [sum(a*b for a,b in zip(row,h)) % mod for row in A]
    pivot = next(i for i,v in enumerate(residues) if v % P)
    inv = pow(residues[pivot],-1,mod)
    old = A[pivot]
    A = [[mod*a for a in row] if i == pivot else
         [a - (residues[i]*inv%mod)*b for a,b in zip(row,old)]
         for i,row in enumerate(A)]
M = Matrix(A)
assert abs(M.det()) == P**21
H = hermite_normal_form(M.T).T
R = (H * Matrix.diag(*W)).lll(delta=Fraction(3,4))
assert abs(R.det()) == P**21 * prod(W)
for i in range(N):
    for j in range(N):
        assert int(R[i,j]) % W[j] == 0
    for k in range(1,7):
        mod=P**k
        assert sum((int(R[i,r])//W[r])*pow(r+1,-k,mod)
                   for r in range(N)) % mod == 0
G=R*R.T
mu=[[Fraction(0)]*N for _ in range(N)]
D=[]
for i in range(N):
    for j in range(i):
        mu[i][j] = (Fraction(int(G[i,j]))-
                    sum(mu[i][a]*mu[j][a]*D[a] for a in range(j)))/D[j]
    D.append(Fraction(int(G[i,i]))-
             sum(mu[i][j]**2*D[j] for j in range(i)))
d=min(D)
assert d == Fraction(78577530278042129705264382752517501995032553011464356025,
                     4243983974238642688103181306691645151538473248349)
assert d > 2*CAP*CAP
print('EXACT_GS_Q0_ELIMINATED',{'p':P,'index':int(abs(M.det())),
      'minimum_GS_square':str(d),'two_side_radius_square':2*CAP*CAP,
      'remaining':'p13 vertical orders >=1 and lower-prime completion'})
