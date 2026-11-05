#!/usr/bin/env python3
"""Author-side exact modular verification of the conditional Clausen one-jet Hensel formula.
No native H0/B0, no project Source execution, no mathematical admission.
"""
def primes_upto(limit):
    out=[]
    for n in range(2,limit+1):
        if all(n%d for d in range(2, int(n**0.5)+1)): out.append(n)
    return out
def direct_jets(p, mod):
    n=(p-1)//6
    term=1
    g=v=gj2=gj3=0
    for k in range(n+1):
        g=(g+term)%mod
        v=(v+2*k*term)%mod
        gj2=(gj2+4*k*(k-1)*term)%mod
        gj3=(gj3+8*k*(k-1)*(k-2)*term)%mod
        if k<n:
            j=k+1
            term=term*(j-1-n)*(j-1-2*n)*pow(j*(2*j-p),-1,mod)%mod
    return g,v,gj2,gj3
def eval_polynomial(z,p,mod):
    n=(p-1)//6
    coefficient=1
    zn=1
    g=v=0
    for k in range(n+1):
        g=(g+coefficient*zn)%mod
        if k: v=(v+k*coefficient*zn*pow(z,-1,mod))%mod
        if k<n:
            j=k+1
            coefficient=coefficient*2*(j-1-n)*(j-1-2*n)*pow(j*(2*j-p),-1,mod)%mod
            zn=zn*z%mod
    return g,(g*(g+12*z*v))%mod
def verify(limit=1200):
    report=[]
    count=0
    for p in primes_upto(limit):
        if p<7 or p%6!=1: continue
        mod=p**3
        g,v,g2,g3=direct_jets(p,mod)
        L=(g+6*v)%mod
        f=g*L%mod
        assert f%p == 0, ('first-digit test failed',p)
        assert ((g%p==0) != (L%p==0)), ('branch test failed',p)
        a1=(6*v*v+(8+6*p)*g*v+4*pow(3,-1,mod)*(p-1)**2*g*g)%mod
        L1=(13*v+6*g2)%mod
        a2=(v*L+g*L1)%mod
        assert a1==a2 and a1%p!=0,('first-jet derivative formula',p)
        L2=(25*g2+6*g3)%mod
        b=(g2*L+2*v*L1+g*L2)*pow(2,-1,mod)%mod
        branch='G' if g%p==0 else 'L'
        c= (2 if branch=='G' else 10)*pow(3,-1,p)%p
        assert (b-a1*c)%p==0, ('curvature constant',p)
        d=f*pow(a1,-1,mod)%mod
        x0=pow(2,-1,mod)
        x_one=(x0-d-c*d*d)%mod
        x_jet=(x0-d-(b*pow(a1,-1,mod)%mod)*d*d)%mod
        assert x_one==x_jet, ('hensel formula mismatch',p)
        _,phi=eval_polynomial(x_one,p,mod)
        assert phi==0,('Hensel root nonzero',p,phi)
        count+=1
        if p in [7,13,19,31,373,1153]:
            report.append({'p':p,'branch':branch,'Gmodp':g%p,'Lmodp':L%p,'a_mod_p':a1%p,'b_over_a_mod_p':c,'root_mod_p3':x_one,'lift_delta_mod_p3':d})
    print('PASS', count, 'primes 7<=p<=',limit,'p mod 6 = 1')
    for r in report: print(r)
if __name__=='__main__':verify()
