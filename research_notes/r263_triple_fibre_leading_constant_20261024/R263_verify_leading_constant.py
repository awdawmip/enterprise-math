"""R263 independent exact BRC source verifier; needs Python 3 and sympy.
The infinite local-limit claim is proved analytically in the companion paper.
"""
from collections import defaultdict
from itertools import product
from math import pi, sqrt
import sympy as S

z, L = S.symbols('z L')
phi = (1 + S.sqrt(5)) / 2
sigma2 = S.Rational(3,2) + 7*S.sqrt(5)/10

def step(q,e,k,a):
    if q < 2:
        qp,eta,b = (2 if q == 0 else 0),(-1 if a == 0 else 1),-1
    else:
        qp,eta,b = (1 if a == 0 else 2),1,(1 if a == 0 else -1)
    return qp,eta*e,eta*k+b

def mode(r,a):
    return 2 if r == 2 or (r == 1 and a == 0) else (1 if a == 0 else 0)

# Rebuild both transfer matrices from the original BRC source edges.
s8=[(p,e) for p in 'ABCD' for e in (1,-1)]
s6=[(q,e) for q in range(3) for e in (1,-1)]
i8={x:i for i,x in enumerate(s8)}; i6={x:i for i,x in enumerate(s6)}
qmap={'A':0,'B':2,'C':2,'D':1}
allowed={'A':[(0,'B'),(1,'C')],'B':[(1,'C')],
         'C':[(0,'D'),(1,'C')],'D':[(1,'A')]}
T=S.zeros(8); U=S.zeros(6)
for (p,e),j in i8.items():
    for a,p2 in allowed[p]:
        qp,ep,kp=step(qmap[p],e,0,a)
        assert qp==qmap[p2]
        T[i8[(p2,ep)],j] += z**(ep*kp)
for (q,e),j in i6.items():
    for a in (0,1):
        qp,ep,kp=step(q,e,0,a)
        U[i6[(qp,ep)],j] += z**(ep*kp)
assert S.cancel((L*S.eye(8)-T).det() -
    (L**2+1)*(L**6-(z+1/z)*L**5+2*L**2-1)) == 0
assert S.cancel((L*S.eye(6)-U).det() -
    L**2*(L-z-1/z)*(L**3+L-z-1/z)) == 0
v=S.Matrix([1,1,1/phi,1/phi,phi**2,phi**2,phi,phi])
w=S.Matrix([1,1,1/phi,1/phi,1,1,1/phi,1/phi])
assert all(S.simplify(x)==0 for x in T.subs(z,1)*v-phi*v)
assert all(S.simplify(x)==0 for x in w.T*T.subs(z,1)-phi*w.T)
assert S.simplify((w.T*v)[0]-10)==0
assert S.simplify(sigma2-phi**4/S.sqrt(5))==0
stationary=S.Matrix([S.Rational(1,8)]*4+[S.Rational(1,4)]*2)
assert U.subs(z,1)*stationary==2*stationary

# Positive-integer dynamic propagation, retaining q, eps, t, and source mode.
d={(0,1,0,0):1}
raw_words=0
reports=[]
for m in range(257):
    if m <= 13:
        direct=defaultdict(int)
        for bits in product((0,1),repeat=m):
            q,e,k,r=0,1,0,0
            for a in bits:
                q,e,k=step(q,e,k,a)
                r=mode(r,a)
            direct[(q,e,e*k,r)]+=1
            raw_words+=1
        assert dict(direct)==d
    if m in (16,32,64,96,128,192,256):
        best=max(min(d.get((2,e,t,r),0) for r in range(3))
                 for e in (1,-1) for t in range(-m,m+1,2))
        tm=m%2
        central=[d.get((2,1,tm,r),0) for r in range(3)]
        scale=float(phi)**m/sqrt(m)
        assert sum(d.values())==2**m
        for t in range(-m,m+1,2):
            assert sum(n for (_,_,tt,_),n in d.items() if tt==t)==int(S.binomial(m,(m+t)//2))
        reports.append((m,str(best),best/scale,[str(x) for x in central]))
    if m == 256: break
    nxt=defaultdict(int)
    for (q,e,t,r),n in d.items():
        for a in (0,1):
            qp,ep,kp=step(q,e,e*t,a)
            nxt[(qp,ep,ep*kp,mode(r,a))]+=n
    d=dict(nxt)
print('R263 symbolic char/Perron: PASS')
print('raw words: ',raw_words)
print('sigma2:',sigma2,'predicted constant:',float(1/(5*phi*S.sqrt(2*S.pi*sigma2))))
for m,b,ratio,c in reports: print('m',m,'M',b,'scaled',ratio,'central',c)
