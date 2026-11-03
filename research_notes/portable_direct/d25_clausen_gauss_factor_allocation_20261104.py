"""D25 author-only finite Gauss moment factor-allocation checks."""

def primes(n):
    ok=[True]*(n+1)
    ok[:2]=[False,False]
    for i in range(2,int(n**0.5)+1):
        if ok[i]:
            for j in range(i*i,n+1,i): ok[j]=False
    return [p for p in range(5,n+1) if ok[p]]

counts={5:0,7:0,13:0,23:0}
for p in primes(2000):
    if p%8 not in (5,7): continue
    m=p*p
    v=1
    F=F1=0
    for k in range(p):
        F=(F+v)%m
        F1=(F1+k*v)%m
        if k+1<p:
            v=v*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,m)%m
    G=(F+16*F1)%m
    cls=p%24
    assert cls in counts
    counts[cls]+=1
    assert (F*G)%m==0, ('product',p)
    if cls in (13,23):
        assert F==0, ('Gauss factor',p,F,G)
    else:
        assert G==0, ('derivative factor',p,F,G)
    if p in (5,7,13,19,23,29,31,37,47,61,109,373):
        print('P',p,'mod24',cls,'F',F,'F+16thetaF',G)
print('PASS',sum(counts.values()),'primes p<=2000 with p mod8 in {5,7}; by mod24',counts)
print('The factor-wise p^2 vanishing is FINITE_TESTED; no general proof claimed.')
