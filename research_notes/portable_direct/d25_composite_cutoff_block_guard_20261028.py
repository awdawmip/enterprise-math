#!/usr/bin/env python3
"""Exact-combination and factorial-only certificate for a cutoff-extension falsifier.
No external packages, floating point, or modular division by n. Author evidence only.
"""
from math import comb, factorial


def summands(n, modulus, route):
    if route == 'comb':
        ta = comb(2*n, n)**2 * comb(3*n, n)
        sb = comb(2*n, n)**2 * comb(4*n, 2*n)
    elif route == 'factorial':
        ta = factorial(2*n)*factorial(3*n)//factorial(n)**5
        sb = factorial(4*n)//factorial(n)**4
    else:
        raise ValueError(route)
    assert ta >= 0 and sb >= 0
    a = (6*n+1)*ta*pow(216, -n, modulus)%modulus
    b = (8*n+1)*sb*pow(2304, -n, modulus)%modulus
    return a, b


def exact_sum(nmax, modulus, route='comb', block_size=None):
    ta=tb=0
    blocks=[]
    for n in range(nmax):
        a,b=summands(n,modulus,route)
        ta=(ta+a)%modulus;tb=(tb+b)%modulus
        if block_size is not None:
            if n%block_size==0:
                blocks.append([0,0,0])
            last=blocks[-1]
            last[0]=(last[0]+a)%modulus
            last[1]=(last[1]+b)%modulus
            last[2]=(last[2]+a-b)%modulus
    return ta, tb, blocks


def vp_factorial(n,p):
    out=0
    while n:
        n//=p;out+=n
    return out


def vp_kernels(n,p):
    return (vp_factorial(2*n,p)+vp_factorial(3*n,p)-5*vp_factorial(n,p),
            vp_factorial(4*n,p)-4*vp_factorial(n,p))


def run():
    outputs={}
    for N in (17,25,85):
        mod=N**3
        x=exact_sum(N,mod,'comb')
        y=exact_sum(N,mod,'factorial')
        assert x==y, (N,x,y)
        A,B,_=x
        outputs[N]=(A,B,(A-B)%mod,(A-B)%(N*N))
    assert outputs[17]==(4896,4896,0,0), outputs[17]
    assert outputs[25]==(3150,9400,9375,0), outputs[25]
    assert outputs[85]==(416500,144500,272000,4675), outputs[85]
    mod17=17**2
    a,b,blocks=exact_sum(85,mod17,'comb',17)
    independent=exact_sum(85,mod17,'factorial',17)
    assert (a,b,blocks)==independent
    assert blocks==[[272,272,0],[170,170,0],[255,0,255],
                    [238,204,34],[272,221,51]], blocks
    assert (a-b)%mod17==51 and 51==3*17
    assert vp_kernels(73,17)==(0,2)
    a73,b73=summands(73,mod17,'comb')
    assert b73==0 and a73%17!=0
    print('PASS_D25_N85_COMPLETE_CUTOFF_CRT_FALSIFIER')
    print('N17/N25/N85 [A,B,delta_mod_N3,delta_mod_N2]:',outputs)
    print('p17 indexed block residues [A,B,delta] mod289:',blocks)
    print('n73 valuations (v17(t_n),v17(s_n)):',vp_kernels(73,17))
    print('n73 weighted residues mod289:',a73,b73)


if __name__=='__main__':
    run()
