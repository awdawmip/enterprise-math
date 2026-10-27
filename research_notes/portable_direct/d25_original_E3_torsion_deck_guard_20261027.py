"""Exact p=373^2 coefficient-ring check of E3 torsion-sheet involution.
Auxiliary original E3 comparator, not native H0/B0 divided-power output.
"""
p, N = 373, 12
q = p*p
inv2 = pow(2, -1, q)
zero, one = (0, 0), (1, 0)

def add(a, b): return ((a[0]+b[0])%q, (a[1]+b[1])%q)
def neg(a): return ((-a[0])%q, (-a[1])%q)
def mul(a, b): return ((a[0]*b[0]+2*a[1]*b[1])%q, (a[0]*b[1]+a[1]*b[0])%q)
def scale(k, a): return ((k*a[0])%q, (k*a[1])%q)
def summ(terms):
    value = zero
    for term in terms: value = add(value, term)
    return value

def product(a, b):
    return [summ(mul(a[i], b[k-i]) for i in range(k+1)) for k in range(N+1)]

def compose(a, inner):
    output = [zero]*(N+1)
    power = [one]+[zero]*N
    for k in range(N+1):
        output = [add(output[i], mul(a[k], power[i])) for i in range(N+1)]
        power = product(power, inner)
    return output

ic = pow(108, -1, q)
c = (2*ic%q, -ic%q)
D = [one, (-2%q, 0), one, scale(-4,c)] + [zero]*(N-3)
s = [one]
for k in range(1, N+1):
    target = D[k]
    cross = summ(mul(s[i], s[k-i]) for i in range(1,k))
    s.append(scale(inv2, add(target,neg(cross))))
assert product(s,s) == D
H = [one]
for k in range(1,N+1):
    H.append(neg(summ(mul(s[i],H[k-i]) for i in range(1,k+1))))
assert product(s,H) == [one]+[zero]*N
L = [zero]+[scale(pow(k,-1,q),H[k-1]) for k in range(1,N+1)]
den = [scale(2,one), add(s[1],neg(one))] + s[2:]
invden = [scale(inv2,one)]
for k in range(1,N+1):
    invden.append(neg(scale(inv2,summ(mul(den[i],invden[k-i]) for i in range(1,k+1)))))
assert product(den,invden) == [one]+[zero]*N
Jt = [zero]+[scale(-2,invden[k-1]) for k in range(1,N+1)]
x = [zero,one]+[zero]*(N-1)
assert [add(a,b) for a,b in zip(compose(L,Jt),L)] == [zero]*(N+1)
assert compose(Jt,Jt) == x
assert Jt[1] == neg(one)
assert Jt[2] == neg(one)
assert Jt[3] == neg(one)
assert Jt[4] == add(neg(one),neg(c))
print('PASS_E3_DECK_373_P2', {'ring':q,'degree':N,'c':c,'Jt_t4':Jt[4], 'L_inverse':True,'involution':True})
