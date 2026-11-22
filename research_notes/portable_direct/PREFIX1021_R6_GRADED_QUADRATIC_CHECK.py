"""Exact typed X6 BRC checker, PREFIX-1021: finite-horizon quadratic rank and grade 1."""
from collections import defaultdict
from sympy import Matrix, symbols, diff
D=[tuple(s if i==j else 0 for i in range(6)) for s in (1,-1) for j in range(6)]
Z=(0,)*6; E=D[0]
def plus(x,d): return tuple(a+b for a,b in zip(x,d))
def norm(v): return sum(z*z for z in v.values())
def add(a,b):
    r=defaultdict(int)
    for x,z in a.items(): r[x]+=z
    for x,z in b.items(): r[x]+=z
    return {x:z for x,z in r.items() if z}
def step(v,mode='all'):
    r=defaultdict(int)
    indices=range(12) if mode=='all' else (range(6) if mode=='positive' else range(6,12))
    for (x,h),a in v.items():
        for i in indices:
            if (x==Z and i==0) or (x==E and i==6): continue
            r[plus(x,D[i]),(i+6)%12]+=(1-6*(h==i))*a
    return {x:z for x,z in r.items() if z}
def flux(v):
    return tuple(sum((1-6*(h==i))*v.get((x,h),0) for h in range(12))
                 for x,i in ((Z,0),(E,6)))
def basis(s,sign):
    x=[0]*6;x[1]=s
    if sign=='-':x[0]=1
    return {(tuple(x),6 if sign=='+' else 0):1}

def horizon(H):
    w=[basis(s,z) for s in range(H) for z in '+-']
    states=w; rows=[]
    for _ in range(H):
        rows.extend([[flux(v)[j] for v in states] for j in range(2)])
        states=[step(v) for v in states]
    B=Matrix(rows);assert B.det()==1
    yy=Matrix([int(j%2==0) for j in range(2*H)])
    c=B.inv()*yy; assert all(z.q==1 for z in c)
    u=basis(3*H+3,'+')
    states=u
    for t in range(H):
        assert flux(states)==(0,0);states=step(states)
    a,*y=symbols('a '+' '.join('y'+str(t) for t in range(H)))
    yc=Matrix([y[j//2] if j%2==0 else 0 for j in range(2*H)])
    cs=B.inv()*yc
    n=[sum(z*z for z in cs)+a*a]
    for t in range(H):n.append(36*n[-1]-y[t]*y[t])
    pt={z:1 for z in [a]+list(y)}
    jac=Matrix([[diff(ni,z) for z in [a]+list(y)] for ni in n]).subs(pt).det()
    assert jac==(-1)**H * 2**(H+1)
    packet={}
    for ci,wi in zip(c,w):
        for k,z in wi.items():packet[k]=int(ci*z)
    packet.update(u)
    actual=[]
    for t in range(H+1):
        actual.append(norm(packet))
        if t<H:
            assert flux(packet)==(1,0);packet=step(packet)
    assert actual==[int(ni.subs(pt)) for ni in n]
    return {'H':H,'det_flux_matrix':1,'jacobian_det':int(jac),'norms':actual}

def grade(nmax=8):
    v0={(Z,6):1};v1={}; direct={(Z,6,0):1};out=[]
    for n in range(nmax+1):
        assert v0=={(x,h):z for (x,h,k),z in direct.items() if k==0}
        assert v1=={(x,h):z for (x,h,k),z in direct.items() if k==1}
        out.append([n,norm(v0),norm(v1)])
        if n==nmax:break
        v1,v0=add(step(v1,'positive'),step(v0,'negative')),step(v0,'positive')
        r=defaultdict(int)
        for (x,h,k),a in direct.items():
            for i,d in enumerate(D):
                kk=k+int(i>=6)
                if kk>1 or (x==Z and i==0) or (x==E and i==6):continue
                r[plus(x,d),(i+6)%12,kk]+=(1-6*(h==i))*a
        direct={k:z for k,z in r.items() if z}
    return out
if __name__=='__main__':
    for H in range(1,5):print('H',horizon(H))
    print('grades',grade())
    print('EXACT PASS')
