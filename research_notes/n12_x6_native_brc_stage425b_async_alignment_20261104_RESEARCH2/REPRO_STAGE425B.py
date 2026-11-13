"""Stage425-B: exact asynchronous absolute alignment and bounded-tail obstruction.
Python 3 standard library; deterministic integer/Boolean computations.
"""
import itertools
import json

D = tuple(range(12))  # 0=+E1, 1=-E1, 2=+E2, 3=-E2, etc.

def direction(a):
    v = [0] * 6
    v[a // 2] = 1 if a % 2 == 0 else -1
    return tuple(v)

def observe(p, q):
    def obs(w):
        v = [0] * 6
        j = [0] * 144
        for a in w:
            d = direction(a)
            for k in range(6): v[k] += d[k]
        for a,b in zip(w, w[1:]): j[a*12+b] += 1
        return (tuple(v), tuple(j))
    return (obs(p), obs(q), sum(a == b for a, b in zip(p,q)))

class State:
    def __init__(self, p, q):
        self.p = list(p)
        self.q = list(q)
        self.k = sum(a == b for a,b in zip(p,q))
        self.ep, self.jp = observe(p,())[0]
        self.eq, self.jq = observe(q,())[0]
        self.ep, self.eq = list(self.ep), list(self.eq)
        self.jp, self.jq = list(self.jp), list(self.jq)

    def change(self, source, adds=(), deletes=0):
        w = self.p if source == 0 else self.q
        e = self.ep if source == 0 else self.eq
        j = self.jp if source == 0 else self.jq
        for _ in range(deletes):
            a = w.pop()
            d = direction(a)
            for i in range(6): e[i] -= d[i]
            if w: j[w[-1]*12+a] -= 1
        for a in adds:
            if w: j[w[-1]*12+a] += 1
            w.append(a)
            d = direction(a)
            for i in range(6): e[i] += d[i]

    def apply(self, adds_p=(), adds_q=(), pop_p=0, pop_q=0):
        assert not ((adds_p or adds_q) and (pop_p or pop_q))
        assert pop_p <= len(self.p) and pop_q <= len(self.q)
        old_min = min(len(self.p),len(self.q))
        old_p, old_q = self.p[:], self.q[:]
        self.change(0, adds_p, pop_p)
        self.change(1, adds_q, pop_q)
        new_min = min(len(self.p),len(self.q))
        if new_min > old_min:
            self.k += sum(self.p[i] == self.q[i] for i in range(old_min,new_min))
        elif new_min < old_min:
            self.k -= sum(old_p[i] == old_q[i] for i in range(new_min,old_min))
        expect=observe(self.p,self.q)
        got=((tuple(self.ep),tuple(self.jp)),(tuple(self.eq),tuple(self.jq)),self.k)
        assert got == expect
        return got

def k_relation(p,q,relation):
    return sum(p[i-1] == q[j-1] for i,j in relation if i<=len(p) and j<=len(q))

def relation_delta(p,q,pp,qq,relation):
    old={(i,j) for i,j in relation if i<=len(p) and j<=len(q)}
    new={(i,j) for i,j in relation if i<=len(pp) and j<=len(qq)}
    return (sum(pp[i-1]==qq[j-1] for i,j in new-old)
            -sum(p[i-1]==q[j-1] for i,j in old-new))

def experiments():
    small = [w for length in range(5) for w in itertools.product(range(3),repeat=length)]
    checks=0
    for p in small:
        for q in small:
            actions=[((a,),(),0,0) for a in range(3)]
            actions += [((),(b,),0,0) for b in range(3)]
            actions += [((a,),(b,),0,0) for a in range(3) for b in range(3)]
            if p: actions += [((),(),1,0)]
            if q: actions += [((),(),0,1)]
            if p and q: actions += [((),(),1,1)]
            if len(p)>=2 and len(q)>=2 and (p[-1]^1)==p[-2] and (q[-1]^1)==q[-2]:
                actions += [((),(),2,2)]
            for a,b,c,d in actions:
                State(p,q).apply(a,b,c,d)
                checks+=1
    # Check all 12x12 native simultaneous append choices.
    for a in D:
        for b in D:
            State((0,1,2,0),(0,2)).apply((a,),(b,))
            checks+=1
    # Generic, fixed absolute alignment relations: diagonal, offset, branching.
    relation_checks=0
    relations=[{(i,i) for i in range(1,8)},
               {(i,i+2) for i in range(1,8)},
               {(i,j) for i in range(1,8) for j in range(1,8) if abs(i-j)<=1}]
    tiny=[w for length in range(4) for w in itertools.product(range(3),repeat=length)]
    for r in relations:
        for p in tiny:
            for q in tiny:
                mods=[]
                for a in range(3): mods.append((p+(a,),q))
                for b in range(3): mods.append((p,q+(b,)))
                for a in range(3):
                    for b in range(3): mods.append((p+(a,),q+(b,)))
                if p: mods.append((p[:-1],q))
                if q: mods.append((p,q[:-1]))
                if p and q: mods.append((p[:-1],q[:-1]))
                for pp,qq in mods:
                    assert k_relation(pp,qq,r)-k_relation(p,q,r)==relation_delta(p,q,pp,qq,r)
                    relation_checks+=1
    # Nonfinite fixed-tail obstruction with exact preservation of endpoints, J, K.
    witness_count=0
    for L in range(1,129):
        p=(0,0,0,1,0)+(0,)*L
        pp=(0,1,0,0,0)+(0,)*L
        q=(0,)
        assert p[:1]==pp[:1] and p[-L:]==pp[-L:]
        assert observe(p,q)==observe(pp,q)
        assert observe(p,q+(0,))[-1]==2 and observe(pp,q+(0,))[-1]==1
        witness_count+=1
    return {"status":"STAGE425B_ASYNC_ALIGNMENT_EXACT_PASS",
            "alphabet":"12 signed native X6 directions; exhaustive tests use three typed directions",
            "all_pairs_lengths_0_to_4":len(small)**2,
            "incremental_full_observer_checks":checks,
            "relation_boundary_delta_checks":relation_checks,
            "fixed_tail_counterexample_lengths":witness_count,
            "fixed_tail_counterexample":"P=AAABA A^L, P'=ABAAA A^L, Q=A, then append A to Q",
            "post_append_K":[2,1],
            "integer_only":True}

if __name__=='__main__':
    print(json.dumps(experiments(),sort_keys=True,ensure_ascii=False,indent=2))
