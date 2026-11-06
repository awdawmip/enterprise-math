"""Independent direct modular check of D25 outer perturbations at the two
known base-2 Wieferich primes. Native Source authorization not claimed."""
from d25_outer_fiber_strata_20261106 import outer_values, primes_to

def original_sum(p,lam):
    mod=p**3; m=(p-1)//6
    s=(2*m,3*m,4*m)
    v=[(-pow(3,-1,mod)+lam)%mod,
       -pow(2,-1,mod)%mod,
       (-2*pow(3,-1,mod)+lam)%mod]
    b=[1]*3;neg_half=pow(-2,-1,mod); factor=1; z=0;local_j1=None
    for j in range(p):
        term= factor*b[0]*b[1]*b[2]%mod
        z=(z+(6*j+1)*term)%mod
        if j==1:local_j1=term
        if j==p-1: break
        inv=pow(j+1,-1,mod)
        b=[(b[i]*(s[i]+p*v[i]-j)*inv)%mod for i in range(3)]
        factor=factor*neg_half%mod
    return z,local_j1

if __name__=='__main__':
    for p in (13,19,373,1093,3511):
        vals=outer_values(p)
        q2=((pow(2,p-1,p*p)-1)//p)%p
        baseline,local=original_sum(p,0)
        assert baseline==p,(p,'baseline',baseline)
        assert vals['k']==(-3*q2)%p,(p,'k',vals['k'],q2)
        assert (vals['T'][0]+vals['T'][2])%p==0
        for lam in (1,2):
            w,j1=original_sum(p,lam)
            diff=(w-baseline)%(p**3)
            observed=diff//(p*p)
            expected=(lam*vals['k']+lam*lam*vals['c'])%p
            assert diff%p**2==0,(p,lam,'first-digit failure')
            assert observed==expected,(p,lam,observed,expected)
            localdigit=((j1-local)%(p*p))//p
            assert localdigit== (lam*3*((p-1)//6)*pow(2,-1,p))%p,(p,localdigit)
            print('p',p,'q2',q2,'T13',vals['T'][0],vals['T'][2],
                  'k',vals['k'],'c',vals['c'],'lam',lam,
                  'signed_sum_modp3',w,'second_digit_diff',observed,
                  'labelled_j1_first_digit_diff',localdigit)
    print('PASS: independent full sums and local source checks at 5 primes, 2 shifts each')
