"""Recompute manifold presentations, trace conditions, and marked matrix witnesses."""
from importlib.metadata import version
from itertools import product
import json

import regina
import sympy as sp
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup

BASE = ((1, 2, -1, 2, 1, -2), (1, -2, -1, -2, 1, 2, 2))
SIG = "fvPQcdecedekrsnrs"
SUM = "qLvAAvvLQQQkcffggjkllklopnpopaaaaakrswskwsnrsn"


def cyclic(word):
    return min(tuple(w[i:] + w[:i]) for w in (word, tuple(-j for j in reversed(word)))
               for i in range(len(w)))


def triangulation(sig):
    tri = regina.Triangulation3.fromIsoSig(sig)
    assert tri.isoSig() == sig
    assert tri.isClosed() and tri.isValid() and tri.isConnected() and tri.isOrientable()
    presentation = tri.group()
    rels = []
    for i in range(presentation.countRelations()):
        word = []
        for term in presentation.relation(i).terms():
            letter = (term.generator+1) * (1 if term.exponent > 0 else -1)
            word.extend([letter]*abs(term.exponent))
        rels.append(tuple(word))
    return {"isosig": sig, "tetrahedra": tri.size(), "vertices": tri.countVertices(),
            "homology": str(tri.homology()), "generators": presentation.countGenerators(),
            "signed_relators": rels}


def traces():
    x, y, z, t = sp.symbols("x y z t")
    ident, a, b, c = [sp.eye(4).col(i) for i in range(4)]
    am = sp.Matrix.hstack(a, x*a-ident, -c+x*b+y*a+(z-x*y)*ident, b+z*a-y*ident)
    bm = sp.Matrix.hstack(b, c, y*b-ident, y*c-a)
    operators = {1: am, -1: x*sp.eye(4)-am, 2: bm, -2: y*sp.eye(4)-bm}
    eq = []
    for word in BASE:
        v = ident
        for letter in word:
            v = (operators[letter]*v).applyfunc(sp.expand)
        eq.append([sp.expand(i) for i in v-ident])
    assert sp.expand(eq[1][0] - (-x+y*z-1)) == 0
    assert sp.expand(eq[1][2].subs(x, y*z-1) - (z-y)) == 0
    f = t*t-t-1
    us, vs = [eq[0][i].subs({x:t*t-1, y:t, z:t}) for i in (0,2)]
    assert sp.expand(t*us + (t*t-1)*vs - f) == 0
    assert all(sp.rem(i.subs({x:t, y:t, z:t}), f, t) == 0 for e in eq for i in e)
    gram = sp.Matrix([[2,x,y,z], [x,x*x-2,z,x*z-y],
                      [y,z,y*y-2,y*z-x], [z,x*z-y,y*z-x,z*z-2]])
    defect = x*x + y*y + z*z - x*y*z - 4
    assert sp.factor(gram.det() + defect**2) == 0
    assert sp.rem(defect.subs({x:t,y:t,z:t}) - (t-2), f, t) == 0
    return {"third_trace_equation": str(f), "commutator_trace_minus_two": "t-2"}


class Ring:
    """Integers mod p, or pairs a+bu with u^2=c0+c1*u mod p."""
    def __init__(self, p, square=None):
        self.p = p
        self.size = p if square is None else p*p
        self.add, self.mul, self.neg = [], [], []
        for a in range(self.size):
            if square is None:
                self.neg.append(-a % p)
                self.add.append([(a+b) % p for b in range(p)])
                self.mul.append([a*b % p for b in range(p)])
            else:
                a0,a1 = a%p,a//p
                def pair(b0,b1):
                    return b0%p+p*(b1%p)
                self.neg.append(pair(-a0,-a1))
                self.add.append([pair(a0+b%p,a1+b//p) for b in range(self.size)])
                self.mul.append([pair(a0*(b%p)+square[0]*a1*(b//p),
                                      a0*(b//p)+a1*(b%p)+square[1]*a1*(b//p))
                                 for b in range(self.size)])

    def dot(self,a,b,c,d):
        return self.add[self.mul[a][b]][self.mul[c][d]]

    def mm(self, left, right):
        a,b,c,d = left
        x,y,z,w = right
        return self.dot(a,x,b,z),self.dot(a,y,b,w),self.dot(c,x,d,z),self.dot(c,y,d,w)

    def det(self, m):
        a,b,c,d = m
        return self.dot(a,d,self.neg[b],c)

    def inv(self, m):
        a,b,c,d = m
        return d,self.neg[b],self.neg[c],a

    def relations(self, a, b, words=BASE):
        ops = {1:a, 2:b, -1:self.inv(a), -2:self.inv(b)}
        ident = (1,0,0,1)
        for word in words:
            x = ident
            for k in word:
                x = self.mm(x, ops[k])
            if x != ident:
                return False
        return True

    def scalar_roots(self):
        return [t for t in range(self.size) if self.mul[t][t] == self.add[t][1]]

    def witness(self, t):
        a = (0,self.neg[1],1,t)
        for r,u in product(range(self.size), repeat=2):
            s = self.add[self.add[u][self.mul[t][r]]][self.neg[1]]
            b = (r,s,u,self.add[t][self.neg[r]])
            if self.det(b)==1:
                assert self.relations(a,b)
                return a,b
        raise AssertionError("missing conic point")

    def image_order(self, gens):
        done = {(1,0,0,1)}
        stack = list(done)
        while stack:
            g = stack.pop()
            for x in gens:
                y = self.mm(g,x)
                if y not in done:
                    stack.append(y)
                    done.add(y)
        return len(done)


def bruteforce(r):
    sl = [a for a in product(range(r.size),repeat=4) if r.det(a)==1]
    return sum(r.relations(a,b) for a,b in product(sl,repeat=2))


def lift_count(r, source):
    def lifts(a):
        result = []
        for delta in product(range(5),repeat=4):
            m = tuple(x+5*y for x,y in zip(a,delta))
            if r.det(m)==1:
                result.append(m)
        assert len(result)==125
        return result
    return sum(r.relations(a,b) for a,b in product(*(lifts(x) for x in source)))


def main():
    sphere, poincare, conn = [triangulation(s) for s in ("cPcbbbaaa", SIG, SUM)]
    assert sphere["generators"] == 0 and all(r["homology"] == "0" for r in [sphere,poincare,conn])
    assert regina.Example3.poincare().isoSig() == SIG
    joined = regina.Example3.poincare()
    joined.connectedSumWith(regina.Example3.poincare())
    assert joined.isoSig() == SUM
    assert {cyclic(w) for w in poincare["signed_relators"]} == {cyclic(w) for w in BASE}
    fg,a,b = free_group("a,b")
    defs = {1:a,-1:a**-1,2:b,-2:b**-1}
    words = []
    for w in BASE:
        h = fg.identity
        for i in w:
            h *= defs[i]
        words.append(h)
    cosets = FpGroup(fg,words).coset_enumeration([],strategy="relator_based",max_cosets=3000)
    cosets.compress()
    assert cosets.is_complete() and cosets.n == 120

    finite = {}
    for name,r in [("F2",Ring(2)),("F3",Ring(3)),("F4",Ring(2,(1,1))),
                   ("F5",Ring(5)),("F7",Ring(7)),("F9",Ring(3,(2,0))),
                   ("F11",Ring(11)),("Z/25",Ring(25)),("Z/121",Ring(121))]:
        roots = r.scalar_roots()
        witnesses = []
        for t in roots:
            matrices = r.witness(t)
            assert r.relations(*matrices, poincare["signed_relators"])
            o = r.image_order(matrices)
            assert o == (60 if name=="F4" else 120)
            witnesses.append({"trace":t,"A_B":matrices,"image_order":o})
        row = {"roots":roots,"witnesses":witnesses}
        if name in ("F2","F3","F4","F5"):
            row["hom_count_exhaustive"] = bruteforce(r)
            assert row["hom_count_exhaustive"] == 1 + len(roots)*r.size*(r.size**2-1)
        finite[name]=row
    r5 = Ring(5)
    witness5 = r5.witness(3)
    counts = [lift_count(Ring(25),witness5),lift_count(Ring(5,(0,0)),witness5)]
    assert counts==[0,625]

    # The re-decoded connected-sum presentation splits into disjoint generator pairs.
    rwords = conn["signed_relators"]
    assert all(all(0<abs(k)<=2 for k in w) for w in rwords[:2])
    assert all(all(2<abs(k)<=4 for k in w) for w in rwords[2:])
    sl5 = [g for g in product(range(5),repeat=4) if r5.det(g)==1]
    totals = []
    for shift, two in [(0,rwords[:2]), (2,rwords[2:])]:
        local = [tuple(k-shift if k>0 else k+shift for k in w) for w in two]
        totals.append(sum(r5.relations(a,b,local) for a,b in product(sl5,repeat=2)))
    assert totals == [121,121]
    print(json.dumps({"regina_distribution":version("regina"),"triangulations":[sphere,poincare,conn],
                      "trivial_subgroup_coset_count":cosets.n,"trace_certificate":traces(),
                      "ring_examples":finite, "fixed_mod5_observer_lifts_Z25_and_dual_F5":counts,
                      "connected_sum_mod5_total":totals[0]*totals[1]}, indent=2))


if __name__ == "__main__":
    main()
