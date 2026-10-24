"""Author-only exact regression for the ordinary Hesse coefficient carrier; NOT a native CM test."""

def source_candidate(p):
    assert p >= 13 and p % 24 in (13, 19)
    n, m = (p - 1)//3, p**3
    def mul(x, y):
        return ((x[0]*y[0]+2*x[1]*y[1])%m,
                (x[0]*y[1]+x[1]*y[0])%m)
    u = (2*pow(4, -1, m)%m, -pow(4, -1, m)%m)
    c, power, value = 1, (1, 0), (0, 0)
    for k in range(n+1):
        value = ((value[0]+c*power[0])%m,
                 (value[1]+c*power[1])%m)
        if k < n:
            c = c*(3*k+1)*(3*k+2)*(3*k+3)*pow(27*(k+1)**3,-1,m)%m
            power = mul(power,u)
    a,b = value
    assert a%p==b%p==0  # only the finite tested primes
    return (a//p,b//p,(a//p)**2-2*(b//p)**2)

expected={13:107,19:316,37:186,43:1002,61:2872,67:3454,211:23075,373:122102}
for p, n in expected.items():
    a,b,N=source_candidate(p)
    assert N%(p*p)==n,(p,a,b,N)
assert source_candidate(373)[:2] == (92060,21788)

p, m = 13, 13**2
def sigma(x): return (x[0],(-x[1])%m)
def mul(x,y):
    return ((x[0]*y[0]+2*x[1]*y[1])%m,
            (x[0]*y[1]+x[1]*y[0])%m)
def inv(x):
    a,b=x
    ni=pow((a*a-2*b*b)%m,-1,m)
    return (a*ni%m, -b*ni%m)
branches=[0,0]
for a in range(m):
    for b in range(m):
        if (a*a-2*b*b)%m != 1:
            continue
        t=(a,b)
        if (a%p,b%p)==(p-1,0):
            z=mul((0,1),((1-a)%m,b))
            branches[1]+=1
        else:
            z=((1+a)%m,(-b)%m)
            branches[0]+=1
        assert mul(sigma(z),inv(z))==t,(t,z)
assert branches == [169,13],branches
print("PASS: eight source norms, p373 second digit, p13 all 182 norm-one gauges",branches)
