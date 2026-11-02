"""Exact C4 phase-tagged path-semirng checks for PREFIX-435 (model-level only)."""
from itertools import product
from math import factorial

def alt(x,y):
    return tuple(a+b for a,b in zip(x,y))

def seq(x,y):
    return tuple(sum(x[j]*y[(k-j)%4] for j in range(4)) for k in range(4))

def obs(x):
    amp=(x[0]-x[2],x[1]-x[3])
    return (sum(x),amp[0]**2+amp[1]**2,amp)

def complex_mul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

basis=tuple(tuple(int(i==k) for i in range(4)) for k in range(4))
for x in product(range(3),repeat=4):
    for y in product(range(3),repeat=4):
        z=seq(x,y)
        ox,oy,oz=obs(x),obs(y),obs(z)
        assert oz[0]==ox[0]*oy[0]
        assert oz[2]==complex_mul(ox[2],oy[2])
        assert obs(alt(x,y))[2]==(ox[2][0]+oy[2][0], ox[2][1]+oy[2][1])
        assert seq(x,y)==seq(y,x)
        assert sum(seq(x,basis[0]))==sum(x)
# Distinct ordered paths for primitive x6 displacement (+e1,+e2)
word12=(0,1);word21=(1,0)
assert word12 != word21
assert factorial(2)//(factorial(1)*factorial(1))==2
# Relative phase zeta=1,-1,i,-i, two 1-unit paths.
readout=[]
for k in range(4):
    h=alt(basis[0],basis[k])
    rotated=alt(basis[0],basis[(k+1)%4])
    readout.append((k,obs(h)[1],obs(rotated)[1]))
assert readout==[(0,4,2),(1,2,0),(2,0),(3,2,4)],readout
assert len({(a,b) for _,a,b in readout})==4
print('PASS_PREFIX435_PHASE_TAGGED_SEMIRING_6561_EXACT_PAIRS')
print('two_shortest_x6_paths=2 phase_intensity_pairs=',readout)
