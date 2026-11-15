"""Exact symbolic sixth-order series certificate. Requires sympy (tested 1.13.1)."""
import sympy as S

s = S.symbols('s', real=True, positive=True)
Q = S.Rational
x = Q(2)              # x_u = d/(u*h), u=s/2 and d=sh
z = 2*s/(2-s)         # x_v = d/(v*h), v=1-s/2
u, v = s/2, 1-s/2
# log(sqrt(1-y*y)*atanh(y)/y) = -y^2/6 - 19*y^4/180 + O(y^6)
L2 = (x*x-z*z)/6
L4 = Q(19,180)*(x**4-z**4)
D1 = x+z
D3 = (x**3+z**3)/3
a = S.factor(L2/D1)
b = S.factor((L4-a*D3)/D1)
assert S.simplify(a-2*(1-s)/(3*(2-s))) == 0
assert S.simplify(b-16*(1-s)*(2*s*s-4*s+9)/(45*(2-s)**3)) == 0

def partial(q, ratio, sign):
    # sqrt(q^2-s^2*h^2) exp(sign*delta*atanh(s*h/q))
    # delta=a*h+b*h^3+O(h^5); collect coefficients of h^(0,2,4,6).
    e2 = sign*a*ratio
    e4 = sign*(b*ratio+a*ratio**3/3)
    e6 = sign*(b*ratio**3/3+a*ratio**5/5)
    return (q,
            q*(e2-ratio**2/2),
            q*(e4+e2**2/2-ratio**2*e2/2-ratio**4/8),
            q*(e6+e2*e4+e2**3/6
              -ratio**2*(e4+e2**2/2)/2-ratio**4*e2/8-ratio**6/16))

U=partial(u,x,1)
V=partial(v,z,-1)
z2,z4,z6=(S.factor(U[j]+V[j]) for j in (1,2,3))
cB2=S.factor(-z2)
cB4=S.factor(-z4+z2*z2/2)
cB6=S.factor(-z6+z2*z4-z2**3/3)
cT2=2*s
cT4=2*s+2*s**2
cT6=4*s+4*s**2+Q(8,3)*s**3
F2=S.factor(cT2/(2-s)-cB2)
F4=S.factor(cT4/(2-s)-cB4)
F6=S.factor(cT6/(2-s)-cB6)
P=270*s**5-1485*s**4+728*s**3+4296*s**2-8448*s+1264
A=-2*s*(1-s)*(9*s**2-40*s+4)/(9*(2-s)**3)
B=-4*s*(1-s)*P/(405*(2-s)**5)
assert F2==0
assert S.simplify(F4-A)==0
assert S.simplify(F6-B)==0
assert S.simplify(cB4 - 4*s*(11*s*s-22*s+20)/(9*(2-s)**3))==0
assert S.simplify(cB6 - 32*s*(179*s**4-716*s**3+1728*s*s-2024*s+968)/(405*(2-s)**5))==0
root=(20-2*S.sqrt(91))/9
F6root=S.radsimp(S.simplify(B.subs(s,root)))
F6root_expected=(22963736-2413784*S.sqrt(91))/3796875
assert S.simplify(F6root-F6root_expected)==0
# 9.53 < sqrt(91), and 9.53 exceeds the exact threshold needed for F6(root)<0
assert 953**2 < 91*100**2
assert 2413784*953 > 22963736*100
Aprime=S.simplify(S.diff(A,s).subs(s,root))
assert S.simplify(Aprime - (127*S.sqrt(91)-1183)/250)==0
assert 127*953 > 1183*100  # A'(root)>0
k=S.radsimp(S.simplify(-F6root/Aprime))
k_expected=(1946672-162368*S.sqrt(91))/2764125
assert S.simplify(k-k_expected)==0
assert 1946672 > 162368*10  # sqrt(91)<10 => k>0
print('PASS_BRC_S23_CHERNOFF_SIXTH_ORDER_CRITICAL_SHIFT_20261103')
print('sympy_version='+S.__version__)
print('delta1='+str(a))
print('delta3='+str(b))
print('F2=0; F4='+str(S.factor(F4)))
print('F6='+str(S.factor(F6)))
print('F6_at_sstar='+str(F6root)+' < 0 (exact integer certificates)')
print('F4prime_at_sstar='+str(Aprime)+' > 0')
print('critical_shift_k='+str(k)+' > 0')
print('exact_symbolic_equalities=10; integer_sign_certificates=4')
