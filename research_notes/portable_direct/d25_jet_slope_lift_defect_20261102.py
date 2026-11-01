"""Exact p^2 original 216/2304 weighted projective-jet lift check. No native H0/B0."""
def primes(n):
    s = bytearray([1])*(n+1)
    s[:2] = b'\0\0'
    for q in range(2, int(n**0.5)+1):
        if s[q]:
            s[q*q::q] = bytes((n-q*q)//q+1)
    return [i for i in range(n+1) if s[i]]


def original_jets(p,series):
    m = p*p
    c = 1
    moments = [0]*4
    for k in range(p):
        for j in range(4):
            moments[j] = (moments[j] + pow(k,j)*c) % m
        if k+1 == p:
            break
        if series == 'A':
            num = (2*k+1)*(3*k+1)*(3*k+2)
            den = 36*(k+1)**3
        else:
            num = (4*k+1)*(2*k+1)*(4*k+3)
            den = 288*(k+1)**3
        c = c*num*pow(den,-1,m)%m
    w = 6 if series=='A' else 8
    jets = [(moments[i]+w*moments[i+1])%m for i in range(3)]
    return moments,jets


def test(p):
    m = p*p
    f,a = original_jets(p,'A')
    g,b = original_jets(p,'B')
    assert all(v%p==0 for v in (f[0],f[1],g[0],g[1]))
    assert a[1]%p != 0 and b[1]%p != 0
    ea = (a[2]-5*pow(3,-1,m)*a[1])%m
    eb = (b[2]-5*pow(16,-1,m)*b[1])%m
    assert ea == ((8*f[1]+2*f[0])*pow(3,-1,m))%m
    assert eb == ((12*g[1]+3*g[0])*pow(32,-1,m))%m
    defect = (16*b[2]*a[1]-3*b[1]*a[2])%m
    assert defect == (16*a[1]*eb-3*b[1]*ea)%m
    assert defect%p==ea%p==eb%p==0
    return defect//p,ea//p,eb//p,a,b


def main():
    ps = [p for p in primes(3000) if p%24 in (13,19)]
    zero = []
    for p in ps:
        d,x,y,a,b = test(p)
        if d==0: zero.append(p)
        if p in (13,19,37,61,373,1171):
            print(f'p={p}, D/p={d}, EA/p={x}, EB/p={y}, Y_A={a}, Y_B={b}')
    print(f'PASS {len(ps)} target primes <=3000: exact coefficient, jet, PF-derived')
    print('first-lift formulas and cross-multiplicative identity.')
    print('Zero first-defect digits in tested range:',zero)
    print('This finite test is not a universal nonvanishing proof.')


if __name__=='__main__':
    main()
