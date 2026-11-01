"""D25 author-side low/low original signed boundary first-carry, with strict
base-binomial and harmonic deformation source separation. NOT NATIVE, NOT ADMITTED.
All arithmetic is integer modular; no nonunit inverses are taken.
"""
from d25_beta_middle_moment_fourport_20261101 import primes, beta, signed_bands_direct
from d25_beta_lowmiddle_signed_carry_20261101 import lowmiddle_carry


def suffix_weighted(seq, modulus):
    p=len(seq)
    s0=[0]*(p+1); s1=[0]*(p+1)
    for j in range(p-1,-1,-1):
        s0[j]=(s0[j+1]+seq[j])%modulus
        s1[j]=(s1[j+1]+j*seq[j])%modulus
    return s0,s1


def first_carry(p, direct=False):
    assert p>=13 and p%8==5
    a=(5*p-1)//8; b=(7*p-3)//8
    M=p*p
    c=[1]; e=[0]; cc=1; ee=0
    inv8=pow(8,-1,p); inv9=pow(9,-1,M)
    for i in range(a):
        cc=cc*(a-i)*(b-i)*inv9*pow(i+1,-2,M)%M
        ee=(ee-5*inv8*pow(a-i,-1,p)-7*inv8*pow(b-i,-1,p))%p
        c.append(cc);e.append(ee)
    # All information preserved: index and original factor, plus separate
    # first-order Pochhammer deformation (can be treated as a signed BRC port).
    ccmod=c+[0]*(p-len(c))
    ce=[(c[i]*e[i])%p for i in range(a+1)]+[0]*(p-a-1)
    cs,cjs=suffix_weighted(ccmod,M)
    es,ejs=suffix_weighted(ce,p)
    base=0;deform=0
    for i in range(p-a,a+1):
        base+=c[i]*((8*i+1)*cs[p-i]+8*cjs[p-i])
        deform+=2*ce[i]*((8*i+1)*(cs[p-i]%p)+8*(cjs[p-i]%p))
    base%=M;deform%=p
    assert base%p==0,(p,base)
    predicted=(base+p*deform)%M
    terms=beta(p,M)
    for i in range(a+1):
        assert terms[i]==(c[i]*(1+p*e[i]))%M,(p,i)
    ts,tjs=suffix_weighted(terms[:a+1]+[0]*(p-a-1),M)
    direct_ll=sum(terms[i]*((8*i+1)*ts[p-i]+8*tjs[p-i]) for i in range(p-a,a+1))%M
    assert direct_ll==predicted,(p,direct_ll,predicted)
    if direct:
        ports=signed_bands_direct(p,terms)
        assert ports[(0,0)]%M==predicted
    cm=lowmiddle_carry(p,terms)
    return base//p%p,deform,predicted//p%p,cm,(predicted//p+cm)%p


def main():
    data=[];n=0;class13=0;harmonic_nonzero=0;basic_nonzero=0
    for p in primes(3000):
        if p<13 or p%8!=5:continue
        z=first_carry(p,p in (13,29,37,53,61,109,373))
        n+=1;class13+=p%24==13
        harmonic_nonzero+=z[1]!=0
        basic_nonzero+=z[0]!=0
        # Empirical target carry claim, NOT a full-prime proof:
        chi=1 if p%3==1 else -1
        assert z[4]==-chi%p,(p,z)
        if p in (13,29,37,53,61,109,373):data.append((p,)+z)
    assert (n,class13)==(109,53)
    print('PASS',n,'primes, target',class13)
    print('nonzero baseline',basic_nonzero,'nonzero harmonic first carry',harmonic_nonzero)
    print('p | J0/p | 2 harmonic correction | LL/p | LM/p | (LL+LM)/p')
    for row in data: print(' | '.join(map(str,row)))

if __name__=='__main__':main()
