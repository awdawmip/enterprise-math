#!/usr/bin/env python3
"""Exact author-checks of the positive-rank subcutoff complement, distinct from Q_p."""
import importlib.util
from pathlib import Path

base = Path(__file__).with_name('20261026_hourly_d25_original_parameter_diagonal_source_bridge_r15_check.py')
spec = importlib.util.spec_from_file_location('d25_original_bridge',base)
bridge=importlib.util.module_from_spec(spec)
spec.loader.exec_module(bridge)


def check(p, digits=3):
    m, N, q, large = (p-1)//6, (p-1)//3-1, p**digits, p**(digits+2)
    fbig, rr = bridge.f_terms(p,large), bridge.r_terms(p,large)
    f=[x%q for x in fbig]
    beta=[0]*p
    for k in range(2*m+1,p):beta[k]=fbig[k]//(p*p)%q
    theta=-p*pow(6,-1,q)%q
    half=pow(2,-1,q)
    V0=[0]*(N+1);V1=V0.copy()
    for j in range(1,2*m+1):
        for ell in range(j+1,2*m+1):
            n=ell-j
            v=f[j]*beta[p-ell]%q
            V0[n]=(V0[n]+v)%q
            V1[n]=(V1[n]+j*v)%q
    Z=[(2*V1[n]-(p-n)*V0[n])%q for n in range(N+1)]
    E=[0]*(N+1)
    mu=[0]*(N+1)
    for n in range(1,N+1):
        E[n]=bridge.genuine_edge(n,m,p,f,beta,theta)%q
        mu[n]=(pow(2,n,q)+(p-n+half)*mu[n-1])*pow(p-n,-1,q)%q
    adj=sum(mu[n]*E[n] for n in range(1,N+1))%q
    assert adj==sum(pow(2,n,q)*Z[n] for n in range(1,N+1))%q
    U=sum(pow(2,n,q)*V0[n] for n in range(1,N+1))%q
    K=sum(pow(2,n,q)*V1[n] for n in range(1,N+1))%q
    c=pow(2,1-p,q)
    telescoped=c*(U+12*K-6*adj)%q
    direct=(2*sum((6*(j+p-ell)+1)*rr[j]*rr[p-ell]
                for j in range(1,2*m+1)
                for ell in range(j+1,2*m+1))%large)
    assert direct%(p*p)==0
    independently=(direct//(p*p))%q
    assert telescoped==independently,(p,telescoped,independently)
    return {'p':p,'positive_complement':telescoped,'positive_source':adj}


def main():
    data=[check(p) for p in bridge.primes()]
    assert len(data)==23
    known={x['p']:x for x in data}
    assert known[13]['positive_complement']==1715
    assert known[733]['positive_complement']==204955275
    assert known[733]['positive_source']==73541419
    print('PASS original positive-rank genuine-edge telescopes and independent ordered subcutoff, 23 primes')
    print(known[13]);print(known[733])

if __name__=='__main__':main()
