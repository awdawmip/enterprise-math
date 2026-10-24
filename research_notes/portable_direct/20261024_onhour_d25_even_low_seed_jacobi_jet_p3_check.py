#!/usr/bin/env python3
"""Author-side exact modular check of even-m (p=12r+1) LOW-seed Jacobi symmetry and p^3 jets.
No native benchmark/Source result. Uses original fixed T_{r,n} comparison.
"""
from math import factorial
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
path=Path(__file__).with_name('20261024_onhour_d25_low_seed_p3_parity_103_tail_collapse_check.py')
spec=spec_from_file_location('seed',path)
seed=module_from_spec(spec);spec.loader.exec_module(seed)

def jet_seed(p):
    assert p>=13 and p%12==1 and seed.is_prime(p)
    r=(p-1)//12; N=4*r; mod=p**3
    inv=lambda x:pow(x%mod,-1,mod)
    coeff=1
    Delta=0
    Theta=0
    sum_base=0
    sum_jet=0
    deriv=0
    for n in range(N+1):
        sum_base=(sum_base+coeff)%mod
        deriv=(deriv+n*coeff)%mod
        sum_jet=(sum_jet+coeff*(1+6*n*Delta+p*(Delta+3*n*(Delta*Delta-Theta))))%mod
        if n==N:break
        b=n-N
        c=2*n+1-2*N
        d=3*n+2
        assert b%p and c%p and d%p
        Delta=(Delta+5*inv(6)*inv(b)-inv(c)-inv(d))%mod
        Theta=(Theta+13*inv(36)*inv(b)**2-inv(c)**2-inv(d)**2)%mod
        coeff=coeff*(n-N)**2*inv((n+1)*(2*n+1-2*N))%mod
    assert deriv==0,(p,'polynomial derivative at 1/2 not zero')
    central=factorial(N)**3*inv(factorial(2*N)*factorial(N//2)**2)%mod
    assert sum_base==central,(p,'central Jacobi value mismatch',sum_base,central)
    A=factorial(6*r)*inv(3**(6*r)*factorial(2*r)**3)%mod
    return (p*A*sum_jet)%mod,sum_base,deriv

def main():
    count=0
    rows=[]
    for p in range(13,1001):
        if p%12!=1 or not seed.is_prime(p):continue
        jets, base, derivative=jet_seed(p)
        original=sum(t for t,v in seed.seed_modular_terms(p))%p**3
        assert jets==original,(p,jets,original)
        assert original%p==0,p
        rows.append((p,jets,original//p%p**2))
        count+=1
    print('PASS symmetric-Jacobi derivative and full p^3 even-LOW jet:',count,'primes <=1000')
    print('samples (p, S_r mod p^3, S_r/p mod p^2):',rows[:12])

if __name__=='__main__':main()
