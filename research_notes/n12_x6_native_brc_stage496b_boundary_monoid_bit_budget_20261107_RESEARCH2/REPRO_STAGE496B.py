"""Stage496-B: exact X6 boundary BRC summaries and dynamic text operations.
All 12 letters are distinct signed primitive X6 directions; exact integer arithmetic.
An implicit Cartesian rope stores exact path summaries, not a physical X6 dynamics law.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import product, combinations
import json, random, time, hashlib

DIRS = 'ABCDEFGHIJKL'
VECTOR = {a: tuple((1 if j==i else 0) for j in range(6)) for i,a in enumerate(DIRS[:6])}
VECTOR.update({a: tuple((-1 if j==i else 0) for j in range(6)) for i,a in enumerate(DIRS[6:])})
INDEX = {a:i for i,a in enumerate(DIRS)}
ZERO_E = (0,)*144
ZERO_V = (0,)*6

@dataclass(frozen=True)
class Summary:
    length: int
    disp: tuple[int,...]
    edges: tuple[int,...]

EMPTY=Summary(0,ZERO_V,ZERO_E)

def singleton(a):
    assert a in INDEX
    return Summary(1,VECTOR[a],ZERO_E)

def ends(s):
    if not s.length:return None,None
    assert sum(s.edges)==s.length-1
    # Subtract all outgoing edge source steps to recover last letter,
    # and all incoming edge target steps to recover first letter.
    outgoing=[0]*6;incoming=[0]*6
    for j,q in enumerate(s.edges):
        if q:
            a,b=DIRS[j//12],DIRS[j%12]
            for h in range(6):
                outgoing[h]+=q*VECTOR[a][h]
                incoming[h]+=q*VECTOR[b][h]
    last=tuple(s.disp[h]-outgoing[h] for h in range(6))
    first=tuple(s.disp[h]-incoming[h] for h in range(6))
    inv={v:k for k,v in VECTOR.items()}
    assert last in inv and first in inv,(last,first)
    return inv[first],inv[last]

def join(p,q):
    if not p.length:return q
    if not q.length:return p
    a=ends(p)[1]; b=ends(q)[0]
    k=12*INDEX[a]+INDEX[b]
    edges=[x+y for x,y in zip(p.edges,q.edges)]
    edges[k]+=1
    return Summary(p.length+q.length,tuple(x+y for x,y in zip(p.disp,q.disp)),tuple(edges))

def scan(w):
    n=len(w); d=[0]*6; E=[0]*144
    for a in w:
        for j,v in enumerate(VECTOR[a]):d[j]+=v
    for a,b in zip(w,w[1:]):E[12*INDEX[a]+INDEX[b]]+=1
    return Summary(n,tuple(d),tuple(E))

class Node:
    __slots__=('letter','priority','left','right','summary','size')
    def __init__(self,letter,priority):
        self.letter=letter;self.priority=priority
        self.left=None;self.right=None
        self.summary=singleton(letter);self.size=1

def state(node):return node.summary if node else EMPTY

def size(node):return node.size if node else 0

def update(node):
    if node:
        node.size=size(node.left)+1+size(node.right)
        node.summary=join(join(state(node.left),singleton(node.letter)),state(node.right))
    return node

def merge(a,b):
    if not a:return b
    if not b:return a
    if a.priority < b.priority:
        a.right=merge(a.right,b)
        return update(a)
    else:
        b.left=merge(a,b.left)
        return update(b)

def split(node,k):
    """First k nodes and remainder; O(height), preserving summaries."""
    if not node:return None,None
    assert 0<=k<=size(node)
    m=size(node.left)
    if k<=m:
        a,b=split(node.left,k);node.left=b
        return a,update(node)
    else:
        a,b=split(node.right,k-m-1);node.right=a
        return update(node),b

def flatten(node):
    if not node:return ''
    return flatten(node.left)+node.letter+flatten(node.right)

class Rope:
    def __init__(self,w='',seed=496):
        self.root=None;self.rng=random.Random(seed)
        for x in w:self.insert(size(self.root),x)
    def _new(self,a):return Node(a,self.rng.random())
    def insert(self,i,a):
        assert 0<=i<=size(self.root) and a in INDEX
        l,r=split(self.root,i);self.root=merge(merge(l,self._new(a)),r)
    def delete(self,i):
        assert 0<=i<size(self.root)
        l,rr=split(self.root,i);discard,r=split(rr,1)
        assert discard and size(discard)==1
        self.root=merge(l,r)
    def set(self,i,a):
        assert 0<=i<size(self.root) and a in INDEX
        l,rr=split(self.root,i);discard,r=split(rr,1)
        assert discard and size(discard)==1
        self.root=merge(merge(l,self._new(a)),r)
    def pop(self):self.delete(size(self.root)-1)
    def append(self,a):self.insert(size(self.root),a)
    def summary(self):return state(self.root)
    def word(self):return flatten(self.root)

def apply_plain(w,op,i=None,z=None):
    if op=='SET':return w[:i]+z+w[i+1:]
    if op=='INSERT':return w[:i]+z+w[i:]
    if op=='DELETE':return w[:i]+w[i+1:]
    if op=='POP':return w[:-1]
    if op=='APPEND':return w+z
    raise ValueError(op)

def evidence():
    t0=time.perf_counter()
    # Full finite proof-check of associative concatenation and endpoint recovery.
    W=['']+[''.join(w) for n in range(1,5) for w in product('ABC',repeat=n)]
    pairs=0;associative=0
    for u in W:
        su=scan(u)
        if u:assert ends(su)==(u[0],u[-1])
        for v in W:
            sv=scan(v)
            assert join(su,sv)==scan(u+v)
            pairs+=1
    # Three-way associativity, nonempty boundary, over shorter words.
    short=['']+[''.join(w) for n in range(1,4) for w in product('ABC',repeat=n)]
    for u in short:
        for v in short:
            for w in short:
                assert join(join(scan(u),scan(v)),scan(w))==join(scan(u),join(scan(v),scan(w)))
                associative+=1
    # Globally indistinguishable but distinguishable via indexed edits.
    a,b='AABA','ABAA'
    assert scan(a)==scan(b)
    a1,b1=apply_plain(a,'SET',1,'C'),apply_plain(b,'SET',1,'C')
    assert scan(a1)!=scan(b1)
    # Min-length exhaustive search: length<=3 lacks such a pair; length4 has one.
    min_len=0; witness_groups=[]
    for n in range(1,5):
        groups=defaultdict(list)
        for tup in product('ABC',repeat=n):
            w=''.join(tup);groups[scan(w)].append(w)
        witness=[]
        for g in groups.values():
            if len(g)>1:
                for u,v in combinations(g,2):
                    for j in range(n):
                        for z in 'ABC':
                            if scan(apply_plain(u,'SET',j,z))!=scan(apply_plain(v,'SET',j,z)):
                                witness.append((u,v,j,z));break
                        if witness:break
                    if witness:break
            if witness:break
        if witness and not min_len:min_len=n;witness_groups=witness
    assert min_len==4
    # Exact native P=T, Q=TWAHA embedding: same T/P, same initial Q observer.
    T,W='ABGABA','GH'
    q1,q2=T+W+'A'+a+'A',T+W+'A'+b+'A'
    assert scan(q1)==scan(q2) and scan(T)==scan(T)
    assert scan(apply_plain(q1,'SET',len(T)+len(W)+1+1,'C'))!=scan(apply_plain(q2,'SET',len(T)+len(W)+1+1,'C'))
    # Two dynamic SETs: first identical observer response; second reveals hidden arrangement.
    x,y='AAAABA','AAABAA'
    assert scan(x)==scan(y)
    seq=[('SET',1,'B'),('SET',2,'B')]
    t1,t2=x,y
    all_trace=[]
    for op,j,z in seq:
        t1=apply_plain(t1,op,j,z);t2=apply_plain(t2,op,j,z)
        all_trace.append((t1,t2,scan(t1)==scan(t2)))
    assert [q[-1] for q in all_trace]==[True,False]
    # All 12 signed X6 axes, random POP/APPEND/INSERT/DELETE/SET sequences.
    rng=random.Random(491496);trials=32;steps=0;len_peak=0
    for k in range(trials):
        start=''.join(rng.choice(DIRS) for _ in range(rng.randint(1,30)))
        rope=Rope(start,seed=k+11);w=start
        for j in range(125):
            opts=['INSERT','APPEND']
            if w:opts+=['SET','DELETE','POP']
            op=rng.choice(opts);z=rng.choice(DIRS)
            i=rng.randrange(len(w)) if op in ('SET','DELETE') else rng.randrange(len(w)+1) if op=='INSERT' else None
            if op=='SET':rope.set(i,z)
            elif op=='INSERT':rope.insert(i,z)
            elif op=='DELETE':rope.delete(i)
            elif op=='APPEND':rope.append(z)
            else:rope.pop()
            w=apply_plain(w,op,i,z)
            assert rope.summary()==scan(w)
            assert rope.word()==w
            if w:assert ends(rope.summary())==(w[0],w[-1])
            len_peak=max(len_peak,len(w));steps+=1
    elapsed=time.perf_counter()-t0
    return {'stage':'496-B','signed_native_X6_alphabet':12,'concat_pairs_exhaustive':pairs,'associativity_triples_exhaustive':associative,'min_fiber_separation_length_over_ABC':min_len,'minimal_witness':{'w1':a,'w2':b,'SET_index_0_based':1,'replacement':'C','after':[a1,b1]},'native_PQ_embedding':{'T':T,'W':W,'H_pair':[a,b],'Q_len':len(q1),'absolute_SET_index_0_based':len(T)+len(W)+2},'two_SET_witness':{'start':[x,y],'ops':seq,'trace':[{'w1':p,'w2':q,'observer_equal':eq} for p,q,eq in all_trace]},'random_rope_trials':trials,'random_rope_operations':steps,'peak_word_length':len_peak,'tests':'PASSED','seconds':round(elapsed,3)}

if __name__=='__main__':print(json.dumps(evidence(),ensure_ascii=False,sort_keys=True))
