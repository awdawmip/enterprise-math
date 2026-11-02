"""PREFIX-438 finite certificate; exact integers, Python standard library."""
from math import comb, factorial

def update(p,t,r,axis,sign):
    t ^= ((p & ((1 << (axis-1))-1)).bit_count() & 1)
    if axis < 6: p ^= 1 << (axis-1)
    if axis == 1 and sign == -1: r ^= 1
    return p,t,r

def word(steps):
    p=t=r=0
    x=[0]*6
    for axis,sign in steps:
        p,t,r=update(p,t,r,axis,sign)
        x[axis-1]+=sign
    return (p,t),r,tuple(x)

# Same endpoint, duration and original 64-state; the extra r_1 port differs.
a=word([(1,1),(1,-1)])
b=word([(2,1),(2,-1)])
assert a[0]==b[0] and a[2]==b[2] and a[1]!=b[1]

for n in range(1,21):
    even=lambda d: sum(comb(n,k)*(n-2*k)**d for k in range(0,n+1,2))
    odd=lambda d: sum(comb(n,k)*(n-2*k)**d for k in range(1,n+1,2))
    assert all(even(d)==odd(d) for d in range(n))
    assert even(n)-odd(n)==2**n*factorial(n)

# Reachable states: 5 coordinate parity bits, one sign-phase bit, one
# negative-e1 history bit. Current (t,r) or one future signed step
# distinguishes every pair of the 128 states.
def decode(c): return c&31,(c>>5)&1,(c>>6)&1

def advance(c,axis,sign):
    p,t,r=decode(c); p,t,r=update(p,t,r,axis,sign)
    return p|(t<<5)|(r<<6)

def seen(c): return (c>>5)&1,(c>>6)&1
for a in range(128):
    for b in range(a+1,128):
        assert seen(a)!=seen(b) or any(
            seen(advance(a,j,1))!=seen(advance(b,j,1)) for j in range(1,7))

assert [sum(comb(4,k)*(4-2*k)**j for k in range(0,5,2)) for j in range(5)] == [8,0,32,0,512]
assert [sum(comb(4,k)*(4-2*k)**j for k in range(1,5,2)) for j in range(5)] == [8,0,32,0,128]
print('PASS: length-2 return-port collision; n=1..20 moment identity; 8128 pairwise state separations; four-step moment witness')
