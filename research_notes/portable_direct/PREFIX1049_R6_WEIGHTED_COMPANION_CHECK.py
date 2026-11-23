from fractions import Fraction as F
import sympy as s

L, n, t = s.symbols('L n t')
P = [-14929920*L*(L-3)*(L-2)*(L-1)*(2*L-3),
     15552*L*(L-2)*(L-1)*(316*L**2-632*L+437),
     -432*L*(L-1)*(2*L-1)*(368*L**2-368*L+409),
     4*L*(2536*L**4+2903*L**2+216),
     -2*(2*L+1)*(40*L**4+80*L**3+98*L**2+58*L+15),
     (L+1)**5]
r, N = 16, 5000
q = F(19,20)
D = s.Poly(-P[0].subs(L,n+s.Rational(3,2)),n)
nums = [s.Poly(r**k*P[k].subs(L,n+s.Rational(3,2)-k),n) for k in range(1,6)]
d5 = D.nth(5)
assert d5 > 0
assert D.as_expr() == s.expand(1866240*n*(2*n-3)*(2*n-1)*(2*n+1)*(2*n+3))
M = s.zeros(5)
M[0,:] = s.Matrix([[p.nth(5)/d5 for p in nums]])
E = s.zeros(5)
E[0,:] = s.Matrix([[p.as_expr() for p in nums]])
for i in range(1,5):
    M[i,i-1] = 1
    E[i,i-1] = D.as_expr()
V,J = M.jordan_form()
S = V*s.diag(1,s.Rational(1,8),s.Rational(1,64),1,1)
Si = S.inv()
assert Si*M*S == s.diag(s.Matrix([[s.Rational(4,9),s.Rational(1,8),0],[0,s.Rational(4,9),s.Rational(1,8)],[0,0,s.Rational(4,9)]]),s.Rational(1,2),s.Rational(4,5))
def norm(A):
    return max(sum(abs(A[i,j]) for j in range(5)) for i in range(5))
B = Si*E*S
Bp = [[s.Poly(B[i,j],n) for j in range(5)] for i in range(5)]
C = [max(sum(abs(Bp[i][j].nth(k)) for j in range(5)) for i in range(5))/d5 for k in range(6)]
dl = 1-sum(abs(D.nth(k)/d5)/N**(5-k) for k in range(5))
assert dl > 0
bound = sum(C[k]/N**(5-k) for k in range(6))/dl
assert bound < s.Rational(91,100) < s.Rational(19,20)
assert norm(S)*norm(Si) == 316368
coeff = [F(1)]
pols = [[F(p.nth(k)) for k in range(6)] for p in nums]
den = [F(D.nth(k)) for k in range(6)]
def pe(p,x):
    v = F(0)
    for a in reversed(p):
        v = v*x+a
    return v
for i in range(1,N):
    coeff.append(sum(pe(pols[k-1],i)*coeff[i-k] for k in range(1,min(5,i)+1))/pe(den,i))
assert max(map(abs,coeff[-5:])) < F(1,10**40)
Ctail = F(norm(S)*norm(Si))/10**40
t0 = Ctail*q/(1-q)
t1 = Ctail*((N-1)*q/(1-q)+q/(1-q)**2)
T = 30000*(sum(abs(z) for z in coeff[21:])+t0)+5200*(sum(i*abs(z) for i,z in enumerate(coeff) if i>20)+t1)
assert T < 16
x = s.symbols('x')
pol = 0
for i,z in enumerate(coeff[:21]):
    pol += s.Rational(z.numerator,z.denominator)*(x/r)**i*((36-x)*(538-12*x)-4*(36-x)**2*i-12*(47-x)*(30/(s.Rational(i)+s.Rational(5,2))-x/(s.Rational(i)+s.Rational(7,2))))
p = s.Poly(pol.subs(x,r*t),t)
d = p.degree()
assert d == 22
bern = [sum(p.nth(j)*s.binomial(k,j)/s.binomial(d,j) for j in range(k+1)) for k in range(d+1)]
assert min(bern) > 7000
assert F(7000-16,5) > 1396
print('PREFIX1049_EXACT_COMPANION_BERNSTEIN_CERTIFICATE_PASSED')
print('norm < 91/100; tail < 16; 23 Bernstein coefficients > 7000')
