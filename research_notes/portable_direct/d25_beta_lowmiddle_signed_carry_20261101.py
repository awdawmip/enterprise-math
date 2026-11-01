"""Author-side original signed low/middle carry certificate, p=5 mod8; NOT_NATIVE."""
from math import comb
from d25_beta_middle_moment_fourport_20261101 import primes,beta,signed_bands_direct


def lowmiddle_carry(p,terms):
    a,b=(5*p-1)//8,(7*p-3)//8
    mid=(0,)*(a+1)+tuple(terms[j]//p%p for j in range(a+1,b+1))
    # Prefix index aligned to original index. Entries outside M vanish.
    P=[0]*(p+1); W=[0]*(p+1)
    for j in range(p-1,-1,-1):
        v=mid[j] if j<len(mid) else 0
        P[j]=(P[j+1]+v)%p
        W[j]=(W[j+1]+j*v)%p
    c=0
    for i in range(p-b,a+1):
        low=comb(a,i)*comb(b,i)*pow(9,-i,p)%p
        assert low==terms[i]%p
        c+=2*low*((8*i+1)*P[p-i]+8*W[p-i])
    return c%p


def main():
    checked=0; count13=0
    cases=[]
    for p in primes(3000):
        if p<13 or p%8!=5: continue
        term=beta(p,p**3)
        predicted=lowmiddle_carry(p,term)
        # Direct double source sum at all primes up to 700, and fixed p=373;
        # this is independent of the suffix formula and uses original weights.
        if p<=700:
            a,b=(5*p-1)//8,(7*p-3)//8
            direct=sum(2*(8*(i+j)+1)*term[i]*term[j]
                for i in range(p-b,a+1)
                for j in range(max(a+1,p-i),b+1))%(p*p)
            assert direct==p*predicted,(p,direct,predicted)
        if p in (13,29,37,53,61,109,373):
            ports=signed_bands_direct(p,term)
            assert ports[(0,1)]% (p*p)==p*predicted,(p,ports[(0,1)],predicted)
            cases.append((p,predicted,ports[(0,0)]//p%p,(ports[(0,0)]+ports[(0,1)])//p%p))
        checked+=1
        count13+=p%24==13
    assert (checked,count13)==(109,53)
    print('PASS',checked,'prime middle/low predictions, including',count13,'p13 target primes')
    print('p | LM/p mod p | LL/p mod p | (LL+LM)/p mod p')
    for line in cases: print(' | '.join(map(str,line)))

if __name__=='__main__':main()
