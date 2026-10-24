#!/usr/bin/env python3
"""D25: exact fixed-prime p^4 five-port WZ transport, p<=20000.

Original WZ five sources are preserved; no Source research authority or native
benchmark is claimed. Reuses exact factored WZ boundary from c7fb90fd and
p^3 transfer from 7724e73f, with one additional p-adic jet digit.
"""
from __future__ import annotations
import argparse
from d25_p4_precision_boundary_scan import target_primes, original_endpoint_mod_p4


class PrimeUnitContext:
    def __init__(self,p):
        self.p=p;self.m=(p-1)//6;self.mod=p**4
        M=self.mod;nmax=12*self.m
        f=[1]*(nmax+1)
        for n in range(1,nmax+1):f[n]=f[n-1]*(n if n%p else 1)%M
        invf=[1]*(nmax+1); invf[nmax]=pow(f[nmax],-1,M)
        for n in range(nmax,0,-1):invf[n-1]=invf[n]*(n if n%p else 1)%M
        self.fac=f;self.ifac=invf
        self.pow216=[1]*(4*self.m+2)
        for n in range(1,len(self.pow216)):
            self.pow216[n]=self.pow216[n-1]*pow(216,-1,M)%M
        self.pow3=[1]*(6*self.m+1)
        for n in range(1,len(self.pow3)):
            self.pow3[n]=self.pow3[n-1]*pow(3,-1,M)%M

    def raw_unit_v(self,r,n):
        """A_r R_(r,n)=p^v*unit, exact at mod p^4."""
        p=self.p;M=self.mod;f=self.fac;g=self.ifac
        v=((6*r)//p+(4*r+2*n)//p+(3*n)//p
           -(2*r)//p-2*(n//p)-2*((2*r+n)//p)-(4*r+n)//p)
        u=(f[6*r]*f[4*r+2*n]*f[3*n]*g[2*r]*g[n]*g[n]
           *g[2*r+n]*g[2*r+n]*g[4*r+n]*self.pow3[6*r]*self.pow216[n])%M
        return v,u

    def rank_endpoint(self,r):
        M=self.mod;p=self.p;total=0
        for n in range(4*r+1):
            v,u=self.raw_unit_v(r,n)
            assert v>=0,(p,r,n,v)
            total=(total+pow(p,v,M)*u*(6*n+12*r+1))%M
        return total

    def five_norm_ports(self,k):
        """Return five labeled E_j/p, each modulo p^3. No p inversion."""
        p=self.p;M=p**3;N=4*k+1
        v,u=self.raw_unit_v(k,N)
        q=8*k+3
        eps=int(q==p)
        exp=v-1-eps
        assert exp>=0,(p,k,'old',v,eps)
        Q=360*k*k+274*k+49
        cq=2*(3*k+1)*Q*pow(3*(2*k+1)*(q//p if eps else q),-1,M)%M
        old=pow(p,exp,M)*(u%M)*cq%M
        tails=[]
        for j in range(1,5):
            r=k+1; n=4*k+j
            vj,uj=self.raw_unit_v(r,n)
            assert vj>=1,(p,k,j,vj)
            tails.append(pow(p,vj-1,M)*(uj%M)*(36*k+6*j+13)%M)
        return (old,*tails)

    def reconstructed_endpoint(self):
        m=self.m;ell=(m+1)//2;p=self.p
        seed=self.rank_endpoint(ell)
        ports=[0]*5
        for k in range(ell,m):
            each=self.five_norm_ports(k)
            for i,t in enumerate(each):ports[i]=(ports[i]+t)%(p**3)
        reconstructed=(seed+p*sum(ports))%self.mod
        return ell,seed,ports,reconstructed


def main(limit):
    count=0
    samples={}
    for p in target_primes(limit):
        c=PrimeUnitContext(p)
        ell,seed,ports,endpoint=c.reconstructed_endpoint()
        direct=original_endpoint_mod_p4(p)
        assert endpoint==direct['S_mod_p4'],(p,ell,seed,ports,endpoint,direct)
        assert c.rank_endpoint(c.m)==endpoint
        if p in (13,19,37,211,307,19963):
            samples[p]={'ell':ell,'seed_mod_p4':seed,'port_totals_over_p_mod_p3':ports,
                        'endpoint_mod_p4':endpoint,'delta_mod_p':direct['delta_mod_p']}
        count+=1
    return count,samples


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=1000)
    options=parser.parse_args()
    count,samples=main(options.limit)
    print('PASS: ',count,'primes, exact FIVE/source ports and full original rank at p^4')
    for p,ex in samples.items():print('sample',p,ex)
