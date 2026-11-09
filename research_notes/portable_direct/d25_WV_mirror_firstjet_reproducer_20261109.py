"""D25 mirror first jets, original binomial and independent rational recurrence.
Author-side exact arithmetic; not a native H0/B0 experiment.
"""
from math import comb, isqrt

def coefficients(p, kind, recurrence=False):
    mod = p**5
    if not recurrence:
        inv = pow(216 if kind == 'A' else 2304, -1, mod)
        return [(comb(2*n,n)**2*comb(3*n,n) if kind == 'A'
                 else comb(4*n,2*n)*comb(2*n,n)**2)*pow(inv,n,mod)%mod
                for n in range(p)]
    v=[1]
    for n in range(p-1):
        a,b = ((2*n+1)*(3*n+1)*(3*n+2),36*(n+1)**3) if kind=='A' else (
               (4*n+1)*(4*n+3)*(2*n+1),288*(n+1)**3)
        v.append(v[-1]*a*pow(b,-1,mod)%mod)
    return v

def verify(p):
    H=[0]*p
    for k in range(1,p): H[k]=(H[k-1]+pow(k,-1,p))%p
    output={}
    for kind,bound,den,w in [('A',3,36,6),('C',4,288,8)]:
        z=coefficients(p,kind)
        if p in (5,7,13,19,37,43,73,373):
            assert z==coefficients(p,kind,True)
        Q=(pow(216 if kind=='A' else 2304,p-1,p*p)-1)//p
        signed=0; count=0
        for q in range(1,p):
            if bound*q<=p or 2*q>=p: continue
            j=(3*pow(q,-1,p)-Q+(
                2*H[2*q]+3*H[3*q-p]-5*H[q] if kind=='A' else
                4*H[4*q-p]-4*H[q]))%p
            u=pow(den*q**3,-1,p*p)*(1+p*j)%(p*p)
            s=p-q
            assert u==(z[q]*z[s]%p**5)//p**3
            low=(z[q]%p**3)//p
            high=u*pow(low,-1,p*p)%(p*p)
            assert high==(z[s]%p**4)//p**2
            signed+=(1+w*s)*high
            count+=1
        assert p*p*signed%p**4==sum((1+w*(p-q))*z[p-q]
                       for q in range(1,p) if bound*q>p and 2*q<p)%p**4
        output[kind]=(count,p*p*signed%p**4)
    return output

def prime(n):return n>=5 and all(n%d for d in range(2,isqrt(n)+1))

if __name__=='__main__':
    ps=[p for p in range(5,212) if prime(p)]+[373]
    d={p:verify(p) for p in ps}
    assert len(ps)==46
    print('PASS',len(ps),'primes,',sum(v['A'][0] for v in d.values()),
          'A pairs,',sum(v['C'][0] for v in d.values()),'C pairs; independent recurrence on 8 primes')
    for p in (13,19,373):
        a=d[p]['A'][1];c=d[p]['C'][1]
        print(p,'grade2_A',a,'grade2_C',c,'grade2_W_minus_2V_mod_p4',(a-2*c)%p**4)
