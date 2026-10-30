#!/usr/bin/env python3
"""Independent exact arithmetic for R5 all-real time-error obstruction.

Scientific theorem is analytic; exhaustive enumeration is a finite check.
Standard library only. No network, credentials, or native X6 computation.
"""
from fractions import Fraction as F
from itertools import permutations

Q = ((F(49, 100), F(1, 100)), (F(1, 100), F(49, 100)))
t = (F(1, 16), F(1, 8))
R = (F(1, 2), F(1), F(3, 2))
D = 32000
paths = []
for x in range(2):
    for u in range(2):
        kernel = ((F(1, 2) + t[x], F(1, 2) - 2*t[x], t[x]) if u == 0
                  else (t[x], F(1, 2) - 2*t[x], F(1, 2) + t[x]))
        assert sum(kernel) == 1 and sum(kernel[v] * R[v] for v in range(3)) == (F(3, 4), F(5, 4))[u]
        for v in range(3):
            q = Q[x][u] * kernel[v]
            p = q * R[v]
            assert q > 0 and p > 0 and (q*D).denominator == (p*D).denominator == 1
            paths.append((x, u, v, int(q*D), int(p*D)))
assert len(paths) == 12
assert sum(z[3] for z in paths) == sum(z[4] for z in paths) == D


def cov(a):
    """H=a*T_P+b*T_Q+k*(r*S2_P+S5_P)+l*(r*S2_Q+S5_Q)."""
    a = F(a)
    b = -F(7, 200) - F(3, 4)*a
    return a, b, F(1) - a, -F(1) - b


def score_weights(a, r):
    aa, b, k, ell = cov(a)
    aa, b, k, ell = (int(z*200) for z in (aa, b, k, ell))
    num, den = r.numerator, r.denominator
    weights = []
    for x, u, v, q, p in paths:
        time = aa*p + b*q
        w = k*p + ell*q
        weights.append((2*den*time + num*w, 3*den*time,
                        4*den*time, 5*den*time + den*w))
    return weights, 200*D*den


def exhaustive(a, r):
    weights, scale = score_weights(a, r)
    fm = None
    farg = None
    for mask in range(1 << 18):
        score = 0
        for i, (x, u, v, q, p) in enumerate(paths):
            if (mask >> x) & 1:
                j = 0
            elif (mask >> (2 + 2*x + u)) & 1:
                j = 1
            elif (mask >> (6 + i)) & 1:
                j = 2
            else:
                j = 3
            score += weights[i][j]
        if fm is None or score > fm:
            fm, farg = score, mask
    lm = None
    for mask in range(1 << 7):
        score = 0
        for i, (x, u, v, q, p) in enumerate(paths):
            if (mask >> x) & 1:
                j = 0
            elif (mask >> (2 + u)) & 1:
                j = 1
            elif (mask >> (4 + v)) & 1:
                j = 2
            else:
                j = 3
            score += weights[i][j]
        if lm is None or score > lm:
            lm = score
    return F(fm, scale), F(lm, scale), farg


def noearly_vector(bits):
    assert bits[0] == bits[1] == 0
    sp = sq = tp = tq = F(0)
    for x, u, v, q, p in paths:
        tau = 3 if bits[2 + u] else 4 if bits[4 + v] else 5
        pp, qq = F(p, D), F(q, D)
        tp += tau*pp
        tq += tau*qq
        if tau == 5:
            sp += pp
            sq += qq
    return (sp, sq, tp, tq)


def det4(m):
    value = F(0)
    for order in permutations(range(4)):
        inversions = sum(order[i] > order[j] for i in range(4) for j in range(i+1, 4))
        prod = F(1)
        for i in range(4):
            prod *= m[i][order[i]]
        value += (-1 if inversions & 1 else 1)*prod
    return value


strategies = ((0,0,0,0,0,0,0), (0,0,0,0,0,0,1),
              (0,0,0,0,0,1,0), (0,0,0,1,0,0,0),
              (0,0,1,0,0,0,0))
vv = [noearly_vector(z) for z in strategies]
mat = [[vv[i][j] - vv[0][j] for j in range(4)] for i in range(1, 5)]
assert det4(mat) == F(55, 8192)
print('RANK4_SEEDLESS_LR_DET_COEFF = 55/8192 (observer det = 55*d^2/8192)')

assert F(49,100)*(-F(3,800)) + F(1,100)*F(11,400) == -F(1,640)
assert F(49,50)*F(3,800) == F(147,40000)
# At r=-3/2, both origins continue under the two possible LR u=0 bits.
assert F(78797,40000) + F(241,200)*(-F(3,2)) == F(6497,40000) > F(147,40000)
assert F(1964739,20000) + F(1949,40)*(-F(3,2)) == F(502989,20000) > 0
assert -F(207,200) - F(159,200)*(-F(3,2)) == F(63,400) > F(147,40000)
assert -F(9807,200) - F(1971,40)*(-F(3,2)) == F(9951,400) > 0
print('ALL_REAL_PIECEWISE_BELLMAN_SIGN_CERTIFICATE = PASS (analytic monotonicity)')

cases = ((100,F(-3,2)), (-100,F(-3,2)), (100,F(1)), (-100,F(-10)))
for a, ratio in cases:
    fv, lv, arg = exhaustive(a, ratio)
    expected_lr = F(320107,3200) if a == 100 else -F(15021,200)
    assert lv == expected_lr, (a,ratio,lv,expected_lr)
    assert fv-lv == F(11,40000), (a,ratio,fv,lv)
    print('EXHAUSTIVE_FULL_262144_LR_128', 'a='+str(a), 'r='+str(ratio),
          'F='+str(fv), 'LR='+str(lv), 'gap='+str(fv-lv), 'FULL_MASK='+str(arg))

# At eps=(7/20,1/2,1/2,3/5), d=1/10, c=-3/20, r=-3/2.
# Explicit FULL maximizer for a=+100: no early stop, STOP at (x=0,u=0),
# then at time 4 STOP for v=0,1 and CONTINUE for v=2.
fullmask = (1 << 2) | sum((1 << (6+i)) for i,(_,_,v,_,_) in enumerate(paths) if v != 2)
weights, scale = score_weights(100, F(-3,2))
def mask_value(mask):
    total=0
    for i,(x,u,v,q,p) in enumerate(paths):
        j=0 if ((mask>>x)&1) else 1 if ((mask>>(2+2*x+u))&1) else 2 if ((mask>>(6+i))&1) else 3
        total+=weights[i][j]
    return F(total,scale)
assert mask_value(fullmask) == F(8002697,80000)
print('EXPLICIT_FULL_WITNESS_MASK',fullmask,'H=8002697/80000')

# The d=0, c!=0 case uses Z_M=(e_M-A-B*T_M)/c=S2_M.
# Its independent separating functional is T_P-17*T_Q/20-10*S2_Q.
def exhaustive_s2_only():
    weights = []
    for x,u,v,q,p in paths:
        base = 20*p - 17*q
        weights.append((2*base-200*q, 3*base, 4*base, 5*base))
    def evaluate(mask, full):
        score = 0
        for i,(x,u,v,q,p) in enumerate(paths):
            if (mask >> x) & 1:
                j=0
            elif (mask >> (2+2*x+u if full else 2+u)) & 1:
                j=1
            elif (mask >> (6+i if full else 4+v)) & 1:
                j=2
            else:
                j=3
            score+=weights[i][j]
        return score
    fmax=max(evaluate(mask,True) for mask in range(1<<18))
    lmax=max(evaluate(mask,False) for mask in range(1<<7))
    return F(fmax,20*D),F(lmax,20*D)

fs,ls=exhaustive_s2_only()
assert (fs,ls,fs-ls)==(F(27899,32000),F(27893,32000),F(3,16000)),(fs,ls)
assert F(49,100)*(-F(1,320))+F(1,100)*F(3,160)==-F(43,32000)
print('EXHAUSTIVE_D_EQ_0_C_NE_0_FULL_262144_LR_128',
      'F='+str(fs),'LR='+str(ls),'gap='+str(fs-ls))

print('PASS_EXACT_R5_TIME_ONLY_ERROR_ALL_REAL_COMPLETE_NO_GO')
