#!/usr/bin/env python3
"""Exact Z/q^3Z digit-carry factorial-unit check for finite Clausen ports.
No native H0/B0 or Frobenius identification is asserted.
"""
from functools import lru_cache
from math import comb
import json
import hashlib
from pathlib import Path

PRIMES=(5,7,11,13,17,19,23,29,31,37,41,43,47)

class Q3:
    def __init__(self,q):
        self.q=q; self.mod=q**3
        mod=self.mod
        self.fact=[1]*q
        self.H=[0]*q; self.H2=[0]*q
        for i in range(1,q):
            inv=pow(i,-1,mod)
            self.fact[i]=self.fact[i-1]*i%mod
            self.H[i]=(self.H[i-1]+inv)%mod
            self.H2[i]=(self.H2[i-1]+inv*inv)%mod
        self.inv2=pow(2,-1,mod)
        self.fact_inv=[pow(t,-1,mod) for t in self.fact]
        self.powerfact=self.fact[-1]
        self._unit=lru_cache(maxsize=None)(self._unit_uncached)
    def valuation_fact(self,n):
        s=0
        while n:
            n//=self.q; s+=n
        return s
    def jet(self,a,N):
        t=self.q*N
        return (1+t*self.H[a] + t*t*self.inv2*(self.H[a]*self.H[a]-self.H2[a]))%self.mod
    def _unit_uncached(self,n):
        e=self.valuation_fact(n)
        v=pow(self.powerfact,e,self.mod)
        while n:
            a=n%self.q; n//=self.q
            v=v*self.fact[a]*self.jet(a,n)%self.mod
        return v
    def binom(self,n,k):
        if not 0<=k<=n: return 0
        e=self.valuation_fact(n)-self.valuation_fact(k)-self.valuation_fact(n-k)
        if e>=3: return 0
        mod=self.mod
        u=self._unit(n)*pow(self._unit(k)*self._unit(n-k)%mod,-1,mod)%mod
        return (self.q**e)*u%mod
    def two_ports(self,m,epsilon):
        mod=self.mod; A=B=0; inv2=pow(2,-1,mod); t=1
        for k in range(m+1):
            x=t*self.binom(m,k)*self.binom(2*m+epsilon,k)%mod
            A=(A+x)%mod
            B=(B+x*(1-6*epsilon+12*k))%mod
            t=t*inv2%mod
        return A,B
    def direct_ports(self,m,epsilon):
        mod=self.mod; A=B=0; inv2=pow(2,-1,mod); t=1
        for k in range(m+1):
            x=t*comb(m,k)*comb(2*m+epsilon,k)%mod
            A=(A+x)%mod
            B=(B+x*(1-6*epsilon+12*k))%mod
            t=t*inv2%mod
        return A,B

def run():
    checks=0; carry_checks=0; zero3=0; port_checks=0
    rows=[]; witnesses=[]
    for q in PRIMES:
        c=Q3(q); echecks=0; owncarry=0; zero=0
        # Exhaustive finite domain including n>=q and nontrivial carries.
        for n in range(0,151):
            for k in range(n+1):
                e=c.valuation_fact(n)-c.valuation_fact(k)-c.valuation_fact(n-k)
                a=c.binom(n,k); b=comb(n,k)%c.mod
                if a!=b: raise AssertionError((q,n,k,a,b,e))
                echecks+=1; checks+=1
                if e: owncarry+=1; carry_checks+=1
                if e>=3: zero+=1; zero3+=1
        # Full two-port q^3 tests: q-adic powers and digits cross q/q^2 boundaries.
        ms=sorted({0,1,2,q-1,q,q+1,2*q-1,2*q,2*q+1,2*q+2,q*q-1,q*q, q*q+1, 151, 203} )
        ms=[m for m in ms if m<=210]
        for m in ms:
            for eps in (0,1):
                p=c.two_ports(m,eps); d=c.direct_ports(m,eps)
                if p!=d: raise AssertionError((q,m,eps,p,d))
                port_checks+=1
                if (q,m,eps) in [(5,25,0),(7,8,0),(7,49,0),(13,28,0),(5,26,1)]:
                    sectors={}
                    t=1; mod=c.mod; inv2=pow(2,-1,mod)
                    for k in range(m+1):
                        n2=2*m+eps
                        e1=c.valuation_fact(m)-c.valuation_fact(k)-c.valuation_fact(m-k)
                        e2=c.valuation_fact(n2)-c.valuation_fact(k)-c.valuation_fact(n2-k)
                        if e1+e2<3:
                            term=t*c.binom(m,k)*c.binom(n2,k)%mod
                            key=str((e1,e2)); sector=sectors.setdefault(key,[0,0]); sector[0]=(sector[0]+term)%mod
                            sector[1]=(sector[1]+(1-6*eps+12*k)*term)%mod
                        t=t*inv2%mod
                    assert (sum(v[0] for v in sectors.values())%mod,sum(v[1] for v in sectors.values())%mod)==p
                    witnesses.append({'q':q,'m':m,'epsilon':eps,'A':p[0],'B':p[1], 'sector_contributions':sectors})
        rows.append({'q':q,'binomial_tests':echecks,'positive_valuation_tests':owncarry,'valuation_ge_3_tests':zero,'two_port_tests':2*len(ms)})
    result={
      'schema':'D25_Q3_FULL_DIGIT_CARRY_AUTHOR_CERT_V1',
      'date':'2026-11-11', 'scope':'EXACT_FINITE_COMPUTATION; AUTHOR_UNREVIEWED_NOT_ADMITTED',
      'prime_set':list(PRIMES), 'binomial_tests':checks,
      'binomial_positive_valuation_tests':carry_checks,
      'binomial_v_ge_3_tests':zero3,
      'full_two_port_tests':port_checks,
      'rows':rows,'witnesses':witnesses,
      'all_checks_passed':True
    }
    out=Path(__file__).with_name('d25_q3_full_digit_carry_ports_certificate_20261111.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows',)},ensure_ascii=False,indent=2))
    print('certificate sha256=',hashlib.sha256(out.read_bytes()).hexdigest())

if __name__=='__main__':run()
