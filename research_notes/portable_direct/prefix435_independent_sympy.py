"""Independent symbolic reconstruction of PREFIX-435's observer map."""
import sympy as S
I=S.I
A=(22+15*I)/8
B=(5+9*I)/4
q=[[0,1,0],[1,1,0],[0,0,1],[1,0,1],[A,A,B]]
tags=((0,1),(1,0),(1,1),(1,2))
rows=q+[[A,A*I**a,B*I**b] for a,b in tags]
h=S.symbols('d0 d1 d2 x01 y01 x02 y02 x12 y12',real=True)
H=S.Matrix([[h[0],h[3]+I*h[4],h[5]+I*h[6]],
            [h[3]-I*h[4],h[1],h[7]+I*h[8]],
            [h[5]-I*h[6],h[7]-I*h[8],h[2]]])
# Rows are declared as 1 by 3 complex linear observers.
# The Hermitian intensity row is c H c*, not c* H c.
values=[S.expand((S.Matrix([c])*H*S.Matrix([c]).conjugate().T)[0]) for c in rows]
M=S.Matrix([[S.simplify(S.diff(v,x)) for x in h] for v in values])
assert M[:5,:].rank()==5
assert M.rank()==9
assert M.det()==S.Rational(1001129928661,65536)
# Directly verify for two sources from PREFIX-434 that the old 5 probes collide.
u=S.I; v=S.Rational(1,2000)-S.I*S.Rational(123,490000)
Xplus=S.Matrix([1,u,v]); Xminus=S.Matrix([1,-u,v])
def direct(c,x):
    z=(S.Matrix([c])*x)[0]
    return S.simplify(S.expand(z*S.conjugate(z)))
qvals1=[direct(c,Xplus) for c in q]
qvals2=[direct(c,Xminus) for c in q]
assert qvals1==qvals2
extra1=[direct(c,Xplus) for c in rows[5:]]
extra2=[direct(c,Xminus) for c in rows[5:]]
assert extra1!=extra2
print('PASS_PREFIX435_INDEPENDENT_SYMPY')
print('rank_Q=',M[:5,:].rank(),'rank_augmented=',M.rank())
print('determinant=',M.det())
print('tagged_difference=',[S.factor(a-b) for a,b in zip(extra1,extra2)])
