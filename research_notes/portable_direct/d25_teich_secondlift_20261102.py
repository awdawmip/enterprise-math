"""Author-side exact p-adic second-order Teichmueller jet certificates (not H0/B0)."""
from math import isqrt
import json


def primes(n):
    flag=[True]*(n+1)
    flag[0]=flag[1]=False
    for d in range(2,isqrt(n)+1):
        if flag[d]:
            for x in range(d*d,n+1,d): flag[x]=False
    return [p for p in range(5,n+1) if flag[p] and p%24 in (13,19)]


def original_jets(p, base, family, c):
    """Compute original finite hypergeometric Euler jets through order 3 mod p^3."""
    M=p**3
    z=pow(base,-1,M)
    q=((pow(z,p-1,M)-1)%M)//p
    ratio=pow(z,p*p-1,M)
    omega=pow(z,p*p,M)
    assert ratio==((1+p*q+p*p*q)%M)
    assert omega==(z*ratio)%M
    assert pow(omega,p-1,M)==1
    f=[0]*4; g=[0]*4
    a=1; t=1
    for k in range(p):
        for j in range(4):
            term=pow(k,j,M)*a%M
            f[j]=(f[j]+term)%M
            g[j]=(g[j]+term*t)%M
        if k==p-1: break
        if family=='A':
            numerator=(2*k+1)*(3*k+1)*(3*k+2)
            den=36*(k+1)**3
        else:
            numerator=(4*k+1)*(2*k+1)*(4*k+3)
            den=288*(k+1)**3
        a=a*numerator*pow(den,-1,M)%M
        t=t*ratio%M
    assert f[0]%p==f[1]%p==0
    assert g[0]%p==g[1]%p==0
    half=pow(2,-1,M)
    for j in range(2):
        rhs=(f[j]+p*q*f[j+1]+p*p*(q*f[j+1]+half*q*q*(f[j+2]-f[j+1])))%M
        assert rhs==g[j],(p,family,j,rhs,g[j])
    assert (f[2]+p*q*f[3]-g[2])%(p*p)==0
    assert f[3]%p==g[3]%p
    n=p*p
    v0=(f[0]//p+p*(q*(f[1]//p)+half*q*q*f[2]))%n

    v1=(f[1]//p+q*f[2]+p*(q*f[2]+half*q*q*(f[3]-f[2])))%n

    v2=(f[2]+p*q*f[3])%n

    assert (v0,v1,v2,f[3]%p)==(g[0]//p,g[1]//p,g[2]%n,g[3]%p)
    orig=(f[0]+c*f[1])%M
    canon=(g[0]+c*g[1])%M
    assert orig%p==canon%p==0
    shift=((canon-orig)%M)//p
    expected=(v0+c*v1-((orig//p)%n))%n

    assert shift==expected
    assert shift%p==(c*q*f[2])%p
    second=(c*q*f[2]+p*(q*(f[1]//p)+c*q*f[2]+half*q*q*(f[2]+c*(f[3]-f[2]))))%n
    assert second==shift,(p,family,second,shift)
    # Any new rational p-adic representative with the same mod-p residue has the same Teich lift.
    for tau in (1,p-1):
        z_alt=z*(1+p*tau)%M
        assert pow(z_alt,p*p,M)==omega
    return {'q_mod_p2':q,'f0_divp_mod_p2':f[0]//p,'f1_divp_mod_p2':f[1]//p,
            'f2_mod_p2':f[2]%n,'f3_mod_p':f[3]%p,
            'canonical_four_ports':[v0,v1,v2,f[3]%p],
            'original_weighted_mod_p3':orig,'canonical_weighted_mod_p3':canon,
            'weighted_shift_divp_mod_p2':shift}


def certify(p):
    A=original_jets(p,2,'A',6)
    B=original_jets(p,9,'B',8)
    n=p*p
    change=(A['weighted_shift_divp_mod_p2']-2*B['weighted_shift_divp_mod_p2'])%n

    # independent direct evaluation at two representatives of the same residue
    return {'p':p,'A':A,'B':B,'signed_shift_divp_mod_p2':change,
            'signed_shift_first_digit':change%p,
            'signed_shift_second_digit':change//p}


def main():
    ps=primes(1000)
    out=[certify(p) for p in ps]
    assert len(out)==45
    r373=next(d for d in out if d['p']==373)
    assert r373['signed_shift_first_digit']==316
    compact={'coverage':'all p<=1000 with p mod24 in {13,19}',
             'type':'author-side exact modular arithmetic, not native H0/B0',
             'count':len(out), 'selected':{str(p):next(r for r in out if r['p']==p)
                                              for p in (13,19,37,61,373)},
             'all_second_order_formula_checks':True}
    print(json.dumps(compact,indent=2,ensure_ascii=False))
    with open('/mnt/data/d25_teich_secondlift_20261102.check.json','w') as f:
        json.dump({'metadata':compact,'all_results':out},f,indent=2)


if __name__=='__main__':main()
