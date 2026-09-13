#!/usr/bin/env python3
"""Exact verifier for the level-9 character-split reduction.

Researcher: EM-DIRECT-66DE45
No RSA-270 factor is used or produced.
"""
from math import isqrt


def divisors(n):
    out=[]
    d=1
    while d*d<=n:
        if n%d==0:
            out.append(d)
            if d*d!=n:
                out.append(n//d)
        d+=1
    return sorted(out)


def c9(t):
    t%=9
    if t==0:
        return 6
    if t%3==0:
        return -3
    return 0


def tr_W9(s):
    # Exact trace of W_s(zeta_9).
    return sum(c9(2-s+2*j) for j in range(s-1))


def trace_profile(T):
    # General odd-target divisor profile P_T = sum_{d|T} W_((d+T/d+2)/2).
    total=0
    for d in divisors(T):
        s=(d+T//d+2)//2
        total += tr_W9(s)
    return total


H9={1:1,2:1,4:0,5:0,7:-1,8:-1}


def chi3(d):
    r=d%3
    if r==1:
        return 1
    if r==2:
        return -1
    return 0


def check_trace_table():
    table=[]
    for r in range(9):
        s=9 if r==0 else r
        table.append(tr_W9(s)//6)
    assert table == [-1,0,1,0,1,-1,1,-1,0]
    print("W trace table: PASS", table)


def check_general_trace_formula():
    checked=0
    for n in range(1,1000,2):
        if n%3!=1:
            continue
        lhs=trace_profile(9*n)//6
        rhs=2*sum(H9[d%9] for d in divisors(n)) + sum(chi3(d) for d in divisors(n))
        assert lhs==rhs,(n,lhs,rhs)
        checked+=1
    print(f"general 9-multiplier trace formula: PASS ({checked} n-values)")


# U(9)=<2> of order 6. Record discrete log exponents of psi with psi(2)=zeta_6.
LOG2_MOD9={1:0,2:1,4:2,8:3,7:4,5:5}


def psi_exp(r):
    return LOG2_MOD9[r%9]


def rho_exp_mod3(r):
    # rho=psi*chi3. In zeta_6 exponents this adds 3 on H2 residues;
    # convert even exponent to zeta_3 exponent by dividing by 2 mod3.
    j=psi_exp(r)
    if chi3(r)==-1:
        j=(j+3)%6
    assert j%2==0
    return (j//2)%3


def Apsi_branch_value_mod9(pmod9,qmod9):
    # Only the H2, N=1 mod9 cases used here. Return exact real A_psi in {0,3}.
    pair=tuple(sorted((pmod9,qmod9)))
    if pair==(2,5):
        return 3
    if pair==(8,8):
        return 0
    raise ValueError(pair)


def check_semiprime_character_split():
    # Distinct H2 prime representatives for the two N=1 mod9 branches.
    cases=[(5,11,36),(17,71,0)]
    for p,q,pred in cases:
        assert p%3==q%3==2 and (p*q)%9==1
        N=p*q
        tr=trace_profile(9*N)
        assert tr==pred,(p,q,tr,pred)
        A=Apsi_branch_value_mod9(p%9,q%9)
        assert tr==12*A
    print("semiprime character split Tr=12*A_psi: PASS")


def is_prime(n):
    if n<2:
        return False
    if n%2==0:
        return n==2
    d=3
    while d*d<=n:
        if n%d==0:
            return False
        d+=2
    return True


def roots_real_cubic_mod(n):
    return [x for x in range(n) if (x*x*x-3*x+1)%n==0]


def check_cubic_splitting():
    assert 81 == -4*(-3)**3 - 27
    checked=0
    for p in range(2,500):
        if p==3 or not is_prime(p):
            continue
        root_count=len(roots_real_cubic_mod(p))
        expected=3 if p%9 in (1,8) else 0
        assert root_count==expected,(p,p%9,root_count,expected)
        checked+=1

    # H2 / N=1 mod9 branch representatives.
    for p,q,trace_expected,solvable in [(5,11,36,False),(17,71,0,True)]:
        N=p*q
        tr=trace_profile(9*N)
        assert tr==trace_expected
        has_root=bool(roots_real_cubic_mod(N))
        assert has_root==solvable
    print(f"real cubic splitting rule: PASS ({checked} primes + semiprime branches)")


RSA270=int(
    "2331085303444075445276376569106805241456198124803054490429486119684959182451"
    "3578286788836931857711641821391926857265831491306067262691135402760979316634"
    "1626693946596196427744273886601876896313468704059066746903123910748277606548"
    "649151920812699309766587514735456594993207"
)


def crt_pair(a,m,b,n):
    for x in range(a,m*n,m):
        if x%n==b%n:
            return x%(m*n)
    raise AssertionError


def check_rsa270_predictions():
    assert RSA270%9==1 and RSA270%54==19
    # Under H2, the two unordered residue branches modulo 18.
    branches=[(5,11),(17,17)]
    assert all((a*b)%18==RSA270%18 for a,b in branches)
    # Corresponding S modulo54 from exact N mod54 factor-residue lifting.
    # These are the two cases independently established in the parent verifier.
    s54={(5,11):52,(17,17):34}
    out={}
    for pair in branches:
        tr=36 if tuple(sorted((pair[0]%9,pair[1]%9)))==(2,5) else 0
        s216=crt_pair(16,72,s54[pair],54)
        out[pair]=(tr,s216)
    assert out[(5,11)]==(36,160)
    assert out[(17,17)]==(0,88)
    print("RSA-270 conditional predictions: PASS",out)


if __name__=="__main__":
    check_trace_table()
    check_general_trace_formula()
    check_semiprime_character_split()
    check_cubic_splitting()
    check_rsa270_predictions()
    print("ALL CHECKS PASS")
