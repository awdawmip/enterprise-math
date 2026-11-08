"""Exact integer certificate for PREFIX-580-R6, from the PREFIX-579-R6 B matrix."""
from fractions import Fraction
import json

N = [[0,0,34,-24,-5,-5],
     [0,0,-24,14,5,5],
     [34,-24,0,0,-5,-5],
     [-24,14,0,0,5,5],
     [-5,5,-5,5,0,0],
     [-5,5,-5,5,0,0]]
T = [[1,-1,0,0,0,0],
     [17,-7,0,0,-5,-5],
     [0,0,1,-1,0,0],
     [0,0,17,-7,-5,-5],
     [1,1,1,1,1,1],
     [0,0,0,0,1,-1]]
H = [[int((i,j) in ((0,3),(3,0),(1,2),(2,1)))
      for j in range(6)] for i in range(6)]

def tr(A): return [list(row) for row in zip(*A)]
def mul(A, B):
    return [[sum(x*y for x,y in zip(row,col)) for col in tr(B)]
            for row in A]
def det(A):
    B = [[Fraction(x) for x in row] for row in A]
    n = len(B)
    answer = Fraction(1)
    for i in range(n):
        pivot = next((j for j in range(i,n) if B[j][i]), None)
        if pivot is None: return Fraction(0)
        if pivot != i:
            B[i], B[pivot] = B[pivot], B[i]
            answer = -answer
        d = B[i][i]
        answer *= d
        for j in range(i+1,n):
            f = B[j][i]/d
            for k in range(i,n):
                B[j][k] -= f*B[i][k]
    return answer
assert mul(mul(tr(T),H),T) == N
assert det(T) == -600
assert det([[34,-24],[-24,14]]) == -100
basis = [[1,1,0,0,0,0],[0,0,1,1,0,0],
         [0,0,0,0,1,0],[0,0,0,0,0,1]]
assert mul(mul(basis,N),tr(basis)) == [[0]*4 for _ in range(4)]
kernel = [[1,1,1,1,1,1],[0,0,0,0,1,-1]]
assert mul(N,tr(kernel)) == [[0,0] for _ in range(6)]
def q(a):
    return sum(a[i]*N[i][j]*a[j] for i in range(6) for j in range(6))
def split(a):
    c=a[4]+a[5]
    return 2*((a[0]-a[1])*(17*a[2]-7*a[3]-5*c)
             +(17*a[0]-7*a[1]-5*c)*(a[2]-a[3]))
for i in range(6):
    for j in range(6):
        a=[0]*6
        a[i]+=1; a[j]+=1
        assert q(a)==split(a)
assert q([1,0,1,0,0,0])==68
assert q([1,0,0,1,0,0])==-48
assert q([1,-1,1,-1,0,0])==192
print("ALL_CHECKS_PASS")
