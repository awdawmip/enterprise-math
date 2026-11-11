#!/usr/bin/env python3
"""Independent exact verifier of D25/LIFT Lucas norm and p31 weighted-port collision."""
import json


def primes_up_to(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for j in range(2, int(n ** 0.5) + 1):
        if s[j]:
            s[j*j:n+1:j] = bytes((n-j*j)//j+1)
    return (p for p in range(7,n+1) if s[p])


def inv(a,p): return pow(a%p,-1,p)


def lucas_pair(m,c,p):
    if m == 0: return 2,0
    l0,l1,j0,j1=2,c,0,1
    for _ in range(2,m+1):
        l0,l1,j0,j1=l1,(c*l1-2*l0)%p,j1,(c*j1-2*j0)%p
    return l1,j1


def verify_one(p):
    eps=0 if p%6==1 else 1
    m=(p-1-4*eps)//6
    assert p==6*m+1+4*eps
    N=-inv(pow(2,2*m+eps,p),p)%p
    seen=set(); witnesses={}; count=0; fixed=0
    for t in range(p):
        if t in (0,p-1,p-2) or t in seen: continue
        v=-2*(t+1)*inv(t+2,p)%p
        assert v not in (0,p-1,p-2)
        assert -2*(v+1)*inv(v+2,p)%p==t
        orbit=sorted({t,v}); seen.update(orbit)
        lam=(t+v)%p
        assert lam!=p-1
        delta=((lam+4)**2-8)%p
        C=(lam**3+10*lam**2+27*lam+20)*inv(lam+1,p)%p
        R=(lam**2+6*lam+7)*inv(lam+1,p)%p
        L,J=lucas_pair(m,C,p); H=R*delta*J%p
        assert (C*C-8-R*R*delta)%p==0
        assert (L*L-(C*C-8)*J*J-4*pow(2,m,p))%p==0
        assert (H*H-delta*(L*L-4*pow(2,m,p)))%p==0
        us=[]; a=b=0
        for x in orbit:
            u=(x+1)*(x+2)**2*inv(x,p)%p; us.append(u)
            val=pow(u,m,p)*pow(x+2,eps,p)%p
            w=(2-12*eps-(3+10*eps)*x)*inv(x+2,p)%p
            a=(a+val)%p; b=(b+val*w)%p
        roots=us+[us[0]]*(2-len(us))
        assert sum(roots)%p==C and roots[0]*roots[1]%p==2
        assert sum(pow(u,m,p) for u in roots)%p==L
        if roots[0]!=roots[1]:
            J_direct=(pow(roots[0],m,p)-pow(roots[1],m,p))*inv(roots[0]-roots[1],p)%p
        else:
            J_direct=m*pow(roots[0],m-1,p)%p
        assert J==J_direct
        nu=1 if len(orbit)==2 else inv(2,p)
        if len(orbit)==1: fixed+=1
        if not eps:
            assert a==nu*L%p and b==nu*((2*lam+5)*L-2*H)%p
        else:
            Q=((lam+4)*L+H)*inv(2,p)%p
            assert a==nu*Q%p and b==nu*(16*L-13*Q)%p
        if p==31 and lam in (7,16):
            witnesses[lam]={'orbit':orbit,'U':us,'C':C,'R':R,'Delta':delta,
                            'L':L,'J':J,'H':H,'A_orbit':N*a%p,'B_orbit':N*b%p}
        count+=1
    if p==31:
        a,b=witnesses[7],witnesses[16]
        assert a['orbit']==[13,25] and b['orbit']==[2,14]
        assert (a['L'],a['Delta'])==(b['L'],b['Delta'])==(1,20)
        assert (a['H'],b['H'])==(23,8)
        assert (a['B_orbit'],b['B_orbit'])==(27,10)
    return count,fixed,witnesses


if __name__=='__main__':
    total=total_fixed=prime_count=0
    coll={}
    for p in primes_up_to(2500):
        n,f,w=verify_one(p)
        total+=n;total_fixed+=f;prime_count+=1
        if p==31: coll=w
    out={'schema':'D25_LUCAS_NORM_COLLISION_CERT_V1','prime_count':prime_count,
         'range':'7<=p<=2500','orbit_count':total,'fixed_orbits':total_fixed,
         'collision_p31':coll,'result':'PASS','admission':'AUTHOR_ONLY_UNREVIEWED'}
    print(json.dumps(out,ensure_ascii=False,sort_keys=True))
