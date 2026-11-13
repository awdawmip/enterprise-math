from fractions import Fraction as F
from itertools import product

def obs(x, y, z):
    return (1-y/16-z/8, (y+z)/4, F(3, 2)+(x+y+z)/2,
            F(3, 2)+(x+y+z)/2)

def inverse(o):
    ep, eq, tp, tq = o
    assert tp == tq
    return 2*(tp-F(3,2))-4*eq, 8*eq-16*(1-ep), 16*(1-ep)-4*eq

def lr(x, y):
    return obs(x, y, x*y)

def full(x1, x2, a1, a2, b):
    x = (x1+x2)/2
    z = (x1*a1+x2*a2)/2
    return obs(x, b, z)

LR = [lr(F(x),F(y)) for x,y in product((0,1),repeat=2)]
FULL = [full(*(F(v) for v in bits)) for bits in product((0,1),repeat=5)]
n = (-8,-3,0,0)
dot = lambda o: sum(a*b for a,b in zip(n,o))
hlr, hf = max(map(dot,LR)), max(map(dot,FULL))
w = full(F(1),F(1),F(1),F(1),F(0))
assert w == (F(7,8),F(1,4),F(5,2),F(5,2))
assert (hlr,hf,dot(w)) == (-8,-F(31,4),-F(31,4))
assert hf-hlr == F(1,4)
mid = tuple((a+b)/2 for a,b in zip(lr(F(0),F(0)),lr(F(1),F(1))))
assert inverse(mid) == (F(1,2),F(1,2),F(1,2))
assert inverse(mid)[2] != inverse(mid)[0]*inverse(mid)[1]
q = [F(0),F(1,4),F(1,2),F(3,4),F(1)]
for x,y in product(q,repeat=2):
    assert inverse(lr(x,y)) == (x,y,x*y)
for x1,x2,a1,a2,b in product((F(0),F(1,2),F(1)),repeat=5):
    x,y,z = inverse(full(x1,x2,a1,a2,b))
    assert (x,y,z) == ((x1+x2)/2,b,(x1*a1+x2*a2)/2)
    assert 0 <= z <= x
print('LR policies=',len(LR),'FULL policies=',len(FULL))
print('W=',w,'n=',n,'hFULL=',hf,'hLR=',hlr,'gap=',hf-hlr)
print('Linf distance >=', (hf-hlr)/sum(map(abs,n)))
print('Midpoint inverse=',inverse(mid))
print('Exact inverse checks: LR=25, FULL=243')
print('PASS_EXACT_R5_TWO_MERGER_BYPASS_GRAPH_VS_POLYTOPE')
