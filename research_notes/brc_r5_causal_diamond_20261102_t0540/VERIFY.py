#!/usr/bin/env python3
"""Exact rational checks for the R5 causally coupled I->J diamond theorem.
Proof for the entire real parameter domain is in RESEARCH.md; finite checks
here validate the exact branch model, vertex algebra and rational witnesses.
"""
from fractions import Fraction as F
from itertools import product

Z = F(0)
ONE = F(1)

def add(u, v):
    return tuple(a + b for a, b in zip(u, v))

def scale(a, u):
    return tuple(a * x for x in u)

def sub(u, v):
    return add(u, scale(-1, v))

def dot(u, v):
    return sum((a * b for a, b in zip(u, v)), Z)

def positive_part(x):
    return max(Z, x)

def finish(p, q, time):
    """Four-observer contribution conditional on terminal natural P/Q kernels."""
    return (p, ONE - q, F(time), F(time))

STOP_I = (ONE, Z, ONE, ONE)
STOP_J = (ONE, Z, F(2), F(2))

class Diamond:
    def __init__(self, a, r, pb, qb, pi, qi, pe, qe):
        self.a, self.r = F(a), F(r)
        self.pb, self.qb, self.pi, self.qi = map(F, (pb, qb, pi, qi))
        self.pe, self.qe = F(pe), F(qe)
        assert all(Z < z < ONE for z in (self.a, self.r, self.pb,
            self.qb, self.pi, self.qi, self.pe, self.qe))
        self.b = ONE - self.a
        self.tail_b = finish(self.pb, self.qb, 3)
        self.tail_i = finish(self.pi, self.qi, 3)
        self.exit_i = finish(self.pe, self.qe, 2)
        self.base_i = add(scale(self.r, self.tail_i),
                          scale(ONE-self.r, self.exit_i))
        # V,B,C,D: provenance-tagged positive carriers; observers may be signed.
        self.V = add(scale(self.a, self.base_i),
                     scale(self.b, self.tail_b))
        self.B = scale(self.a, sub(STOP_I, self.base_i))
        self.C = scale(self.b, sub(STOP_J, self.tail_b))
        self.D = scale(self.a*self.r, sub(STOP_J, self.tail_i))

    def full_direct(self, x, yb, yi):
        """Independently expand all physical stop/natural branches."""
        x, yb, yi = F(x), F(yb), F(yi)
        bypass = add(scale(yb, STOP_J), scale(ONE-yb, self.tail_b))
        after_i = add(scale(yi, STOP_J), scale(ONE-yi, self.tail_i))
        continue_i = add(scale(self.r, after_i),
                         scale(ONE-self.r, self.exit_i))
        via_i = add(scale(x, STOP_I), scale(ONE-x, continue_i))
        return add(scale(self.a, via_i), scale(self.b, bypass))

    def full_formula(self, x, yb, yi):
        return add(add(add(self.V, scale(x, self.B)),
                       scale(yb, self.C)), scale((ONE-x)*yi, self.D))

    def lr(self, x, y):
        return self.full_direct(x, y, y)

    def full_vertices(self):
        return tuple(self.full_direct(*bits) for bits in product((Z, ONE), repeat=3))

    def lr_vertices(self):
        return tuple(self.lr(*bits) for bits in product((Z, ONE), repeat=2))

    def symbolic_gap(self, normal):
        beta, c, d = (dot(normal, self.B), dot(normal, self.C),
                      dot(normal, self.D))
        return max(positive_part(c)+positive_part(d),
                   beta+positive_part(c)) - max(positive_part(c+d),
                                               beta+positive_part(c))

    def vertex_gap(self, normal):
        return max(map(lambda o: dot(normal, o), self.full_vertices())) - \
               max(map(lambda o: dot(normal, o), self.lr_vertices()))


def separating_normal(C, D):
    """Rational n with n.C=1 and n.D=-1; requires independent vectors."""
    for i in range(4):
        for j in range(i+1, 4):
            determinant = C[i]*D[j] - C[j]*D[i]
            if determinant:
                n = [Z]*4
                n[i] = (D[j]+C[j])/determinant
                n[j] = (-D[i]-C[i])/determinant
                assert dot(n, C) == ONE and dot(n, D) == -ONE
                return tuple(n)
    raise AssertionError("C,D were collinear")


def check(model):
    count = 0
    for x, yb, yi in product((Z, ONE, F(1, 3)), repeat=3):
        assert model.full_direct(x, yb, yi) == model.full_formula(x, yb, yi)
        assert model.lr(x, yb) == model.full_direct(x, yb, yb)
        count += 2
    normals = ((-7,-5,0,0),(-1,-1,0,0),(1,1,0,0),
               (0,1,-2,3),(4,-1,-3,2),(0,0,1,-1))
    for n in normals:
        n = tuple(map(F, n))
        assert model.vertex_gap(n) == model.symbolic_gap(n)
        assert model.vertex_gap(n) >= 0
        count += 2
    assert model.C[2] == -model.b
    assert model.D[2] == -model.a*model.r
    if (model.pb,model.qb)!=(model.pi,model.qi):
        n = separating_normal(model.C, model.D)
        opposite = scale(-ONE, n)
        assert model.vertex_gap(n)+model.vertex_gap(opposite) == ONE
        assert max(model.vertex_gap(n),model.vertex_gap(opposite)) >= F(1,2)
        count += 2
    else:
        for x, u, v in product((Z, F(1,3),F(2,3),ONE), repeat=3):
            denom = model.b + model.a*model.r*(ONE-x)
            y = (model.b*u + model.a*model.r*(ONE-x)*v) / denom
            assert Z <= y <= ONE
            assert model.full_direct(x,u,v) == model.lr(x,y)
            count += 1
    return count

if __name__ == '__main__':
    total = 0
    fixed = lambda a, r: Diamond(a,r,F(3,4),F(1,4),
                                  F(1,4),F(3,4),F(1,2),F(1,2))
    vals=(F(1,4),F(1,3),F(1,2),F(2,3),F(3,4))
    for a,r in product(vals, repeat=2):
        m=fixed(a,r)
        total += check(m)
        n=tuple(map(F, (-7,-5,0,0)))
        gap = min(2*(ONE-a),4*a*r)
        assert m.vertex_gap(n) == gap and gap > 0
        assert dot(n,m.full_direct(Z,ONE,Z)) == max(
            dot(n,o) for o in m.full_vertices())
        total += 2
    # Further rational kernels with unequal or equal provenance responses.
    for pb,qb,pi,qi in ((F(2,5),F(4,7),F(5,8),F(1,3)),
                        (F(1,3),F(3,5),F(1,3),F(3,5)),
                        (F(4,5),F(1,5),F(2,5),F(2,3)),
                        (F(2,7),F(6,7),F(2,7),F(6,7))):
        m=Diamond(F(2,5),F(3,7),pb,qb,pi,qi,F(3,5),F(2,5))
        total += check(m)
    m=fixed(F(1,2), F(1,2))
    expect={
        'V':(F(9,16),F(9,16),F(11,4),F(11,4)),
        'B':(F(5,16),F(-3,16),F(-3,4),F(-3,4)),
        'C':(F(1,8),F(-3,8),F(-1,2),F(-1,2)),
        'D':(F(3,16),F(-1,16),F(-1,4),F(-1,4))}
    assert all(getattr(m,k)==v for k,v in expect.items())
    n=tuple(map(F,(-7,-5,0,0)))
    W=m.full_direct(Z,ONE,Z)
    assert W == (F(11,16),F(3,16),F(9,4),F(9,4))
    hfull=max(dot(n,v) for v in m.full_vertices())
    hlr=max(dot(n,v) for v in m.lr_vertices())
    assert (hfull,hlr,hfull-hlr)==(F(-23,4),F(-27,4),ONE)
    Y=m.lr(Z,F(2,3))
    assert Y==(F(37,48),F(13,48),F(9,4),F(9,4))
    assert max(abs(w-y) for w,y in zip(W,Y))==F(1,12)
    # The normal gives the matching lower bound for every LR point/convex mix.
    assert (dot(n,W)-hlr) / sum(map(abs,n)) == F(1,12)
    total += 8
    print('MODEL  a=1/2 r=1/2 pb=3/4 qb=1/4 pi=1/4 qi=3/4 pe=qe=1/2')
    for label, vec in expect.items():
        print(label, ' '.join(map(str,vec)))
    for xy, vec in zip(product((0,1),repeat=2),m.lr_vertices()):
        print('LR_VERTEX',xy,' '.join(map(str,vec)))
    print('W_FULL', ' '.join(map(str,W)))
    print('DUAL_NORMAL', ' '.join(map(str,n)))
    print('SUPPORT_FULL',hfull,'SUPPORT_LR',hlr,'GAP',hfull-hlr)
    print('ACTUAL_LR_NEAREST', ' '.join(map(str,Y)))
    print('SHARP_LINF_DISTANCE',F(1,12))
    print('ALL_REAL_GAP_FORMULA', 'min(2*(1-a),4*a*r), 0<a,r<1')
    print('CHECKED_EXACT_RELATIONS',total)
    print('PASS_EXACT_R5_CAUSALLY_COUPLED_DIAMOND_COMPLETE_CLASSIFICATION')
