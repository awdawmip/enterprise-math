"""R63: persistent, seam-free rational circle source index; exact arithmetic.

Run with Python >=3.10: python check_r63.py
For frozen S23 endpoint tests we use rational enclosure endpoints, not an
uncertified irrational-parameter transport. No scientific input is re-pinned.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
import random, math, json, time

SCIENTIFIC_PIN = '43ec6098b1330ae86d0a7863be336c5d97f6ef34'
FROZEN_P = 262204504569236716045286
FROZEN_Q = 10**24

@dataclass(frozen=True, slots=True)
class Node:
    phase: int
    t: int
    priority: int
    left: Node | None = None
    right: Node | None = None
    max_t: int = 0


def make(phase: int,t: int,priority: int,left=None,right=None) -> Node:
    max_t = max(t, left.max_t if left is not None else t,
                right.max_t if right is not None else t)
    return Node(phase,t,priority,left,right,max_t)


def key(n): return (n.phase,n.t)


def split(n: Node | None,k: tuple[int,int]):
    """Persistent split: keys < k, keys >= k."""
    if n is None: return None,None
    if key(n)<k:
        a,b=split(n.right,k)
        return make(n.phase,n.t,n.priority,n.left,a),b
    a,b=split(n.left,k)
    return a,make(n.phase,n.t,n.priority,b,n.right)


def merge(l: Node | None,r: Node | None):
    if l is None:return r
    if r is None:return l
    if l.priority>r.priority:
        return make(l.phase,l.t,l.priority,l.left,merge(l.right,r))
    return make(r.phase,r.t,r.priority,merge(l,r.left),r.right)


def find(n: Node | None,k):
    while n is not None:
        if k==key(n):return True
        n=n.left if k<key(n) else n.right
    return False


def insert(n: Node | None, phase:int,t:int,priority:int):
    k=(phase,t)
    if n is None:return make(phase,t,priority)
    if k==key(n):raise ValueError('Duplicate timestamp in the active set')
    if priority>n.priority:
        l,r=split(n,k)
        return make(phase,t,priority,l,r)
    if k<key(n):return make(n.phase,n.t,n.priority,insert(n.left,phase,t,priority),n.right)
    return make(n.phase,n.t,n.priority,n.left,insert(n.right,phase,t,priority))


def erase(n:Node|None, k):
    if n is None:raise KeyError(k)
    if k==key(n):return merge(n.left,n.right)
    if k<key(n):return make(n.phase,n.t,n.priority,erase(n.left,k),n.right)
    return make(n.phase,n.t,n.priority,n.left,erase(n.right,k))


def mmax(a,b):
    return b if a is None else (a if b is None or a>=b else b)


def range_max(root: Node|None,lo,hi):
    """Return max timestamp in phase interval [lo,hi); O(tree height).

    Split-node search and two boundary spines, with subtree maxima over
    wholly included right/left subtrees, respectively.
    """
    if root is None or lo>=hi:return None
    n=root
    while n is not None and not (lo<=n.phase<hi):
        n=n.right if n.phase<lo else n.left
    if n is None:return None
    out=n.t
    p=n.left
    while p is not None:
        if p.phase>=lo:
            out=mmax(out,p.t)
            if p.right is not None:out=mmax(out,p.right.max_t)
            p=p.left
        else:p=p.right
    p=n.right
    while p is not None:
        if p.phase<hi:
            out=mmax(out,p.t)
            if p.left is not None:out=mmax(out,p.left.max_t)
            p=p.right
        else:p=p.left
    return out


class PersistentCircle:
    def __init__(self,p:int,q:int,seed=63011):
        assert 0<p<q
        self.p,self.q=p,q
        self.random=random.Random(seed)
        self.priorities={}
        self._arcs={}  # immutable history order, cached for each m
    def phase(self,t:int):return (t*self.p)%self.q
    def add(self,root,t:int):
        priority=self.priorities.setdefault(t,self.random.getrandbits(128))
        return insert(root,self.phase(t),t,priority)
    def remove(self,root,t:int):return erase(root,(self.phase(t),t))
    def max_in_arc(self,root,start,end):
        # endpoints may be exact Fractions, measured in units 1/q
        if start<end:return range_max(root,start,end)
        if start>end:return mmax(range_max(root,start,self.q),range_max(root,0,end))
        return root.max_t if root is not None else None   # full circle: m==1
    def labels(self,m:int):
        assert 1<=m<=self.q//math.gcd(self.p,self.q)  # distinct labelled history boundaries
        return sorted(((z*self.p)%self.q,z) for z in range(m))
    def history_arcs(self,m:int):
        """O(m log m) one-time preprocessing, then O(1) source-label arc lookup."""
        if m not in self._arcs:
            b=self.labels(m)
            arcs=[None]*m
            for k, (phase,z) in enumerate(b):
                arcs[z]=(phase,b[(k+1)%m][0])
            self._arcs[m]=arcs
        return self._arcs[m]
    def label_query(self,root,j:int,x:F,m:int,z:int):
        assert 0<=z<m
        lo_phase,hi_phase=self.history_arcs(m)[z]
        # source phase phi_t = {t theta}; observer phase is
        # {phi_t + (x-j theta)}.
        shift=(x-F((j*self.p)%self.q,self.q))%1
        lo=(F(lo_phase,self.q)-shift)%1*self.q
        hi=(F(hi_phase,self.q)-shift)%1*self.q
        latest=self.max_in_arc(root,lo,hi)
        return None if latest is None else j-latest


def oracle(p,q,active,j,x,m):
    theta=F(p,q)
    bounds=sorted((((z*p)%q,z) for z in range(m)))
    labels=[None]*m
    for t in sorted(active,reverse=True):
        phase=(x+F((t-j)*p%q,q))%1
        k=int(phase*q)
        # compare fractions exactly (k for integer phase only incorrect if phase has fractional grid coordinate)
        import bisect
        idx=bisect.bisect_right([F(a,q) for a,_ in bounds],phase)-1
        if idx<0:idx=m-1
        z=bounds[idx][1]
        if labels[z] is None:labels[z]=j-t
    return labels


def validate_tree(n:Node|None,lo=None,hi=None):
    if n is None:return 0,0
    k=key(n)
    assert (lo is None or lo<k) and (hi is None or k<hi)
    if n.left:assert n.priority>=n.left.priority
    if n.right:assert n.priority>=n.right.priority
    nl,ml=validate_tree(n.left,lo,k)
    nr,mr=validate_tree(n.right,k,hi)
    assert n.max_t==max(n.t,ml if nl else n.t,mr if nr else n.t)
    return 1+nl+nr, n.max_t


def run():
    rng=random.Random(20261111)
    records=[]
    queries=0
    updates=0
    old_version_queries=0
    anchor_queries=0
    exact_collisions=0
    start=time.perf_counter()
    # Small dynamic/versioned tests: include m=1, collision modulo q,
    # non-grid observer x, old version snapshots and random update history.
    for _ in range(360):
        q=rng.randrange(5,66)
        ps=[p for p in range(1,q) if math.gcd(p,q)==1]
        p=rng.choice(ps)
        m=rng.randint(1,min(q,8))
        pc=PersistentCircle(p,q,seed=rng.randrange(10**9))
        root=None
        active=set()
        snapshots=[(root,frozenset(active))]
        base=10**18*rng.randrange(1,100)
        for step in range(40):
            if active and rng.random()<0.46:
                t=rng.choice(tuple(active))
                root=pc.remove(root,t);active.remove(t)
            else:
                t=base+rng.randrange(-3*q,4*q)
                if t not in active:
                    root=pc.add(root,t);active.add(t)
            updates+=1
            if step%4==0:
                sz,_=validate_tree(root)
                assert sz==len(active)
                snapshots.append((root,frozenset(active)))
            j=base+10*q+rng.randrange(5*q)
            assert all(t<j for t in active)
            x=F(rng.randrange(-50,50),rng.randrange(2,51))
            truth=oracle(p,q,active,j,x,m)
            for z in range(m):
                assert pc.label_query(root,j,x,m,z)==truth[z],(p,q,m,z,truth)
                queries+=1
            if step%8==0:
                oldroot,oldactive=rng.choice(snapshots)
                truth_old=oracle(p,q,oldactive,j,x,m)
                for z in range(m):
                    assert pc.label_query(oldroot,j,x,m,z)==truth_old[z]
                    old_version_queries+=1
            if step%9==0:
                # Change j/x without modifying the tree: no phase relabelling.
                j2=j+10**24
                x2=x+F(19,31)
                truth2=oracle(p,q,active,j2,x2,m)
                for z in range(m):
                    assert pc.label_query(root,j2,x2,m,z)==truth2[z]
                    anchor_queries+=1
        # Explicitly include duplicate-phase group at timestamps t,t+q.
        t0=base-q
        rr=None
        rr=pc.add(rr,t0)
        rr=pc.add(rr,t0+q)
        assert pc.phase(t0)==pc.phase(t0+q)
        old=rr
        assert rr.max_t==t0+q
        rr=pc.remove(rr,t0+q)
        assert rr.max_t==t0 and old.max_t==t0+q
        exact_collisions+=1
    # Frozen S23 enclosure endpoints, original historical labels, age list.
    frozen=[]
    for p in [FROZEN_P,FROZEN_P+1]:
        pc=PersistentCircle(p,FROZEN_Q)
        H=225;m=128
        j=10**12+128
        active=set(range(j-H,j))
        root=None
        for t in sorted(active):root=pc.add(root,t)
        validate_tree(root)
        x=F(0)
        truth=oracle(p,FROZEN_Q,active,j,x,m)
        result=[pc.label_query(root,j,x,m,z) for z in range(m)]
        assert truth==result
        # Additional shift to nonzero observer on same persistent version.
        for jj,xx in [(j,F(1,3)),(j+10**18,F(2,7))]:
            independent=oracle(p,FROZEN_Q,active,jj,xx,m)
            assert [pc.label_query(root,jj,xx,m,z) for z in range(m)]==independent
            anchor_queries+=m
        frozen.append({'p':str(p),'q':str(FROZEN_Q),'m':m,'H':H,
            'first_12_ages':result[:12], 'nonempty_labels':sum(v is not None for v in result),
            'source_nodes':len(active)})
        queries+=m
    elapsed=time.perf_counter()-start
    evidence={
        'science_pin':SCIENTIFIC_PIN,'mode':'exact rational auxiliary observer',
        'random_test_cases':360,'dynamic_operations':updates,
        'fresh_exact_source_age_queries':queries,
        'historical_version_queries':old_version_queries,
        'unchanged_index_reanchored_queries':anchor_queries,
        'duplicate_phase_group_tests':exact_collisions,
        'frozen_endpoints':frozen,
        'all_assertions_passed':True,'wall_seconds_observed':round(elapsed,3),
        'limitations':'Finite tests corroborate mathematical proof; frozen endpoint calculations do not prove uniform irrational-parameter index ordering.'
    }
    return evidence

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
