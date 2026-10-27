#!/usr/bin/env python3
"""D25 author-side E.2-vs-original-216 theorem transfer: exact p-local only.
NOT a native H0/B0 experiment or an all-prime original W proof.
"""
from fractions import Fraction

def original_216(p):
    modulus=p**3
    term=1
    total=0
    middle_digit=None
    middle_start=(p-1)//3+1
    for n in range(p):
        weighted=(6*n+1)*term%modulus
        if n==middle_start:
            assert weighted%p==0 and weighted%(p*p)!=0, (p,n,weighted)
            middle_digit=(weighted//p)%p
        total=(total+weighted)%modulus
        if n<p-1:
            denom=36*(n+1)**3
            term=term*(2*n+1)*(3*n+1)*(3*n+2)*pow(denom,-1,modulus)%modulus
    return total,middle_digit

def e2(p):
    modulus=p**3
    term=1
    full=cut=0
    m=(p-1)//3
    for n in range(p):
        part=(6*n+1)*term%modulus
        full=(full+part)%modulus
        if n<=m:
            cut=(cut+part)%modulus
        else:
            assert term==0, (p,n,term)
        if n<p-1:
            denom=27*(n+1)**3
            term=-term*(3*n+1)**3*pow(denom,-1,modulus)%modulus
    assert full==cut
    return full,cut,m+1

def check():
    w1,w2=Fraction(7,18),Fraction(65,432)
    e1,e2_value=Fraction(-7,27),Fraction(104,729)
    scale=w1/e1
    assert scale==Fraction(-3,2)
    assert w2/e2_value==Fraction(135,128)!=scale**2
    rows=[]
    for p in (7,13,19,31,37,43,61,67,211,373):
        assert p%6==1
        W,mid=original_216(p)
        V,cut,k=e2(p)
        assert V==p%p**3, (p,'external E2 finite theorem regression',V)
        assert W==p%p**3, (p,'original D25 finite regression',W)
        rows.append((p,k,mid,W,V,(W-V)%p**3))
    return scale,w2/e2_value,rows

if __name__=='__main__':
    x,y,rows=check()
    print('FIRST_COEFFICIENT_ARG_SCALE',x)
    print('SECOND_COEFFICIENT_REQUIRED_SQUARE',y)
    for row in rows:
        print('p,first_p3_terminated_index,original_middle_digit,Wmodp3,E2modp3,W_minus_E2=',*row)
    print('PASS_D25_VAN_HAMME_E2_TRANSFER_SCOPE_ONLY')
