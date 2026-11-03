"""Independent first-digit coefficient trace for original finite 2304 Gauss factors."""
from collections import Counter

def primes(bound):
    s = bytearray(b'\x01') * (bound+1)
    s[:2] = b'\x00\x00'
    for k in range(2,int(bound**.5)+1):
        if s[k]: s[k*k:bound+1:k] = b'\x00'*((bound-k*k)//k+1)
    return [p for p in range(5,bound+1) if s[p]]


def root_indices(p):
    a = (-pow(8,-1,p)) % p
    b = (-3*pow(8,-1,p)) % p
    return a,b


def trace_f_g(p):
    a,b = root_indices(p)
    z = pow(9,-1,p)
    tf=tg=0
    for x in range(p):
        t=pow(x,p-1-b,p)*pow(1+x,a,p) %p
        h=(x+z)%p
        hpow=pow(h,b-1,p)
        tf=(tf-t*hpow*h)%p
        tg=(tg-t*hpow*(x+(1+16*b)*z))%p
    # When a=p-1 (only p=7), the x^(a+b) top term also aliases under finite-field summation.
    correction = int(a == p-1)
    return (tf-correction)%p, (tg-correction)%p


def binomial_f_g(p):
    a,b = root_indices(p)
    z=pow(9,-1,p)
    f=g=0
    c1=c2=1
    for k in range(min(a,b)+1):
        t=c1*c2*pow(z,k,p)%p
        f=(f+t)%p
        g=(g+(16*k+1)*t)%p
        if k<min(a,b):
            c1=c1*(a-k)*pow(k+1,-1,p)%p
            c2=c2*(b-k)*pow(k+1,-1,p)%p
    return f,g


def main(limit=10000):
    counts=Counter()
    rows=[]
    for p in primes(limit):
        if p%8 not in (5,7):
            continue
        f,g=trace_f_g(p)
        assert (f,g)==binomial_f_g(p), ('trace mismatch',p,f,g)
        selected='F' if p%24 in (13,23) else 'G'
        assert ((f if selected=='F' else g)==0), ('root class',p,f,g)
        assert ((g if selected=='F' else f)!=0), ('opposite root',p,f,g)
        counts[selected]+=1
        if p in (13,23,29,373,2053):rows.append({'p':p,'a':root_indices(p)[0],'b':root_indices(p)[1],'trace_F':f,'trace_G':g})
    print({'PASS':True,'limit':limit,'counts':dict(counts),'examples':rows})

if __name__=='__main__':main()
