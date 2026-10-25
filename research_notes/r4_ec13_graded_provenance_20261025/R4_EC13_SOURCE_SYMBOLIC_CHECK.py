#!/usr/bin/env python3
"""R4-EC13 concise symbolic certificate; exact SymPy computations."""
import sympy as S
from collections import deque

edges={0:((2,-1,-1),(2,1,-1)),1:((0,-1,-1),(0,1,-1)),2:((1,1,1),(2,1,-1))}
def step(s,a):
    q,r,e=s
    q1,eta,b=edges[q][a]
    ee=e*eta
    rr=2 if r==2 else (0 if a else (1 if r==0 else 2))
    return (q1,rr,ee),ee*b
todo=deque([(0,0,1)]);seen=set()
while todo:
    t=todo.popleft()
    if t in seen:continue
    seen.add(t)
    for a in (0,1):todo.append(step(t,a)[0])
states=sorted(seen); assert len(states)==14
index={s:i for i,s in enumerate(states)}
clean=[i for i,s in enumerate(states) if s[1]!=2]
assert len(clean)==8
assert [states[i] for i in clean]==[(0,0,-1),(0,0,1),(1,1,-1),(1,1,1),(2,0,-1),(2,0,1),(2,1,-1),(2,1,1)]
Ap=S.zeros(14);Am=S.zeros(14)
for i,st in enumerate(states):
    for bit in (0,1):
        target,inc=step(st,bit)
        assert inc==st[2]*(1-2*bit)
        (Ap if inc==1 else Am)[index[target],i]+=1
assert Ap**3==Ap**4
x,u=S.symbols('x u')
M=Ap.extract(clean,clean)+u*Am.extract(clean,clean)
v=S.zeros(8,1);v[1]=1
Delta=1-(1+u)*x+2*u**2*x**4-u**3*x**6
N=(1-u*x**2)*(1-u*x**3)
K=1+u*x**2
A=u*x-1; B=u*x**3+x-1;E=u**2*x**5-u*x**3-x+1
H=S.Matrix([-u*x**4*A,A*B,-u*x**3*A,u*x**2*E,-x**2*A,u*x*E,x*A*B,-u**2*x**5*A])
assert all(S.expand(t)==0 for t in (S.eye(8)-x*M)*H-K*Delta*v)
assert S.expand(sum(H)-K*N)==0
C=S.cancel(N/Delta)
D=1/(1-(1+u)*x)-C
assert S.factor(C.subs(u,1)-(1+x)/(1-x-x**2))==0
for j in range(1,6):
    G=S.cancel(S.diff(D,u,j).subs(u,0)/S.factorial(j))
    assert S.limit((1-x)**j*G,x,1)==2*j
print("PASS: bijection, 8-component exact polynomial certificate, all-j GF, fixed-j pole coefficients j=1..5")
