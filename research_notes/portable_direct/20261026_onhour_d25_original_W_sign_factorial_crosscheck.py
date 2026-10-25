"""D25 original W exact factorial observer; independent of the adjacent-term recurrence.
Author-only: no native CM, formal checkpoint or independent mathematical review.
"""
def source_factorial_mod_p3(p: int) -> int:
    q=p**3
    fac=[1]*p
    for n in range(1,p): fac[n]=fac[n-1]*n%q
    invfac=[1]*p
    invfac[-1]=pow(fac[-1],-1,q)
    for n in range(p-2,-1,-1): invfac[n]=invfac[n+1]*(n+1)%q
    inv216=pow(216,-1,q)
    fac2=1;fac3=1;pow216=1;total=0
    for n in range(p):
        if n:
            fac2=fac2*(2*n-1)*(2*n)%q
            fac3=fac3*(3*n-2)*(3*n-1)*(3*n)%q
            pow216=pow216*inv216%q
        # Exactly (2n)!(3n)! / [216^n (n!)^5], denominator p-unit.
        term=fac2*fac3*pow(invfac[n],5,q)*pow216%q
        total=(total+(6*n+1)*term)%q
    return total

if __name__=="__main__":
    sample=(5,7,11,13,19,37,101,1009,19963,99991)
    for p in sample:
        expected=p if p%6==1 else p**3-p
        actual=source_factorial_mod_p3(p)
        assert actual==expected,(p,actual,expected)
        print(f'PASS independent factorial p={p} Wmodp3={actual} sign={"+" if p%6==1 else "-"}')
    print(f"PASS {len(sample)} factorial-based crosschecks")
