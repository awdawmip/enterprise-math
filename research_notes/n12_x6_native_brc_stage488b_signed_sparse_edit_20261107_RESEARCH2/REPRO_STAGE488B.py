#!/usr/bin/env python3
"""Stage488-B: exact signed X6 dense/sparse residual-edge DP and finite oracle.

Full source observation: P,Q lengths, 6-component signed displacements,
all 144 directed signed-pair counts, and initial positional K. Key partition
is the Stage486-B author-side (unreviewed) future-equivalence candidate.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from time import perf_counter
import json, gc, tracemalloc, os

D = 'ABCDEF'+'GHIJKL'  # +E1..+E6; -E1..-E6
V = {c: tuple((1 if i == j else 0) * (1 if j < 6 else -1)
               for i in range(6)) for j, c in enumerate(D[:6]) for _ in [0]}
V.update({D[j+6]:tuple(-int(i==j) for i in range(6)) for j in range(6)})

def displacement(word):
    return tuple(sum(V[c][j] for c in word) for j in range(6))

def edges(word, alphabet=D):
    pairs=Counter(zip(word,word[1:]))
    return tuple(pairs[x,y] for x in alphabet for y in alphabet)

def popedge(rem, index):
    if index is None or rem[index] == 0:return None
    a=list(rem);a[index]-=1;return tuple(a)

class BRC:
    def __init__(self,k,u,h,alphabet,T,W,H,sparse):
        self.k,self.u,self.h=k,u,h
        self.m=2*k+2
        self.n=self.m+k+u+2
        assert len(T)==self.m and len(W)==k and len(H)==u
        assert 0<=h<=self.n-1 and alphabet[0]=='A' and len(set(alphabet))==len(alphabet)
        assert set(T+W+H)<=(set(alphabet)) and set(alphabet)<=set(D)
        self.L=max(k+1,h-k-u-1);self.r=min(h,u)
        self.length=self.L+k+self.r
        self.letters=tuple(alphabet);self.d=len(alphabet)
        self.thetaP=edges(T,self.letters)
        self.thetaQ=edges(T+W+'A'+H+'A',self.letters)
        self.deltaP=displacement(T)
        self.deltaQ=displacement(T+W+'A'+H+'A')
        # fixed 144 components are retained as the external exact observer.
        self.fullP=edges(T);self.fullQ=edges(T+W+'A'+H+'A')
        self.sparse=sparse
        self.ids=tuple(i for i,v in enumerate(self.thetaQ) if v) if sparse else tuple(range(self.d*self.d))
        self.index={divmod(ident,self.d):pos for pos,ident in enumerate(self.ids)}
        self.pr=tuple(self.thetaP[i] for i in self.ids)
        self.qr=tuple(self.thetaQ[i]-self.thetaP[i] for i in self.ids)
        self.start=self.letters.index(T[0]);self.A=self.letters.index('A')
        self.transitions=0
        self._start=(-1,self.pr,self.qr,-1,-1)

    @lru_cache(None)
    def euler(self,s,t,e):
        if not any(e):return int(s==t)
        total=0
        for c in range(self.d):
            r=popedge(e,self.index.get((s,c)))
            if r is not None:total+=self.euler(c,t,r)
        return total

    @lru_cache(None)
    def step(self,i,state,c):
        self.transitions+=1
        last,pr,qr,fs,fh=state
        factor=1
        if i<self.L:
            if i==0: fs=c
            else:
                pr=popedge(pr,self.index.get((last,c)))
                if pr is None:return None
            if i==self.L-1:
                factor=self.euler(self.start,fs,pr)
                if not factor:return None
                pr=();fs=-1
        elif i<self.L+self.k:
            qr=popedge(qr,self.index.get((last,c)))
            if qr is None:return None
            if i==self.L+self.k-1:
                qr=popedge(qr,self.index.get((c,self.A)))
                if qr is None:return None
        else:
            if i==self.L+self.k:fh=c
            else:
                qr=popedge(qr,self.index.get((last,c)))
                if qr is None:return None
            if i==self.length-1:
                qr=popedge(qr,self.index.get((c,self.A)))
                if qr is None:return None
        return ((c,pr,qr,fs,fh),factor)

    def final_mass(self,state):
        return self.euler(self.A,state[-1] if self.r else self.A,state[2])

    def count(self):
        layer={self._start:(1,1)};layer_states=1;trans=0;maxwidth=1
        for i in range(self.length):
            nxt={}
            for state,(ways,mass) in layer.items():
                for c in range(self.d):
                    t=self.step(i,state,c)
                    if t is None:continue
                    st,f=t;trans+=1
                    w,m=nxt.get(st,(0,0))
                    nxt[st]=(w+ways,m+mass*f)
            layer=nxt;layer_states+=len(layer);maxwidth=max(maxwidth,len(layer))
        cl=mass=0
        for st,(ways,m) in layer.items():
            e=self.final_mass(st)
            if e:cl+=ways;mass+=m*e
        return dict(classes=cl,raw_mass=mass,layer_states=layer_states,
                    transitions=trans,max_width=maxwidth,terminal_states=len(layer),
                    euler_states=self.euler.cache_info().currsize)

    @lru_cache(None)
    def completions(self,i,state):
        if i==self.length:return int(self.final_mass(state)>0)
        return sum(self.completions(i+1,t[0]) for c in range(self.d)
                   if (t:=self.step(i,state,c)) is not None)

    def unrank(self,n):
        if not 0<=n<self.completions(0,self._start):raise IndexError(n)
        st=self._start;ans=[]
        for i in range(self.length):
            for c in range(self.d):
                t=self.step(i,st,c)
                if t is None:continue
                a=self.completions(i+1,t[0])
                if n>=a:n-=a
                else:ans.append(self.letters[c]);st=t[0];break
            else:raise AssertionError('unrank stalled')
        assert n==0
        return ''.join(ans)

    def rank(self,key):
        st=self._start;n=0
        assert len(key)==self.length
        for i,ch in enumerate(key):
            c=self.letters.index(ch)
            for x in range(c):
                t=self.step(i,st,x)
                if t:n+=self.completions(i+1,t[0])
            t=self.step(i,st,c)
            if not t:raise ValueError('unsupported key')
            st=t[0]
        if not self.final_mass(st):raise ValueError('unsupported key')
        return n

    def key(self,T,W,H):
        return T[-self.L:]+W+(H[-self.r:] if self.r else '')


def oracle(k,u,alphabet,T,W,H):
    p=edges(T,alphabet);q=edges(T+W+'A'+H+'A',alphabet)
    t_candidates=[];tail_candidates=[]
    for x in product(alphabet,repeat=len(T)-1):
        t=T[0]+''.join(x)
        if t[-1]==T[-1] and edges(t,alphabet)==p:t_candidates.append(t)
    tail_bag=tuple(a-b for a,b in zip(q,p))
    for v in product(alphabet,repeat=k+u):
        w=''.join(v[:k]);z=''.join(v[k:])
        if edges(T[-1]+w+'A'+z+'A',alphabet)==tail_bag:
            tail_candidates.append((w,z))
    return t_candidates,tail_candidates


def measured(k,u,alphabet,T,W,H,h, sparse, do_rank=True):
    gc.collect();tracemalloc.start()
    t0=perf_counter()
    b=BRC(k,u,h,alphabet,T,W,H,sparse)
    result=b.count()
    assert b.completions(0,b._start)==result['classes']
    if do_rank:
        for idx in {0,result['classes']//2,result['classes']-1}:
            if result['classes']:
                key=b.unrank(idx);assert b.rank(key)==idx
    elapsed=perf_counter()-t0
    _cur,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
    return b,{**result,'time_seconds':round(elapsed,6),'peak_tracemalloc_bytes':peak,
              'component_count':len(b.ids),'populated_directed_edge_types':sum(x>0 for x in b.thetaQ),
              'max_counter_bits':result['raw_mass'].bit_length(),
              'euler_memo_states':b.euler.cache_info().currsize}


def interior_edit_counterexample():
    k,u=2,2;T='ABGABA';W='GH';H1='AB';H2='BA';j=len(T)+len(W)+2-1 # 0-based first H index = m+k+1
    Q1=T+W+'A'+H1+'A';Q2=T+W+'A'+H2+'A'
    assert Q1[j]!=Q2[j]
    assert edges(Q1)==edges(Q2) and displacement(Q1)==displacement(Q2)
    assert edges(T)==edges(T)
    assert (Q1[:j]+'I'+Q1[j+1:])!=(Q2[:j]+'I'+Q2[j+1:])
    e1=edges(Q1[:j]+'I'+Q1[j+1:]);e2=edges(Q2[:j]+'I'+Q2[j+1:])
    assert e1!=e2
    # Q internal SET(j,I): no POP or APPEND consumed, only the directed-edge observer changed.
    return {'T':T,'W':W,'H_1':H1,'H_2':H2,'Q_1':Q1,'Q_2':Q2,
            'index_1based':j+1,'written_symbol':'I (-E3)',
            'before_same_full_144_edges':True,'after_same_full_144_edges':False,
            'after_difference':[(D[a//12]+D[a%12],e1[a]-e2[a]) for a in range(144) if e1[a]!=e2[a]],
            'original_pop_append_key_h0_same':True}


def run():
    # Each selected signed native letter occurs at least once in T+W+H.
    seeds=[
      ('ABGH','ABGABA','GH','BA',[0,1,2,8,11]),
      ('ABGHI','ABGABA','HI','GB',[0,1,2,8,11]),
      ('ABCGHI','ABGCIA','HI','GB',[0,1,2,8,11]),
      ('ABGH','AABGAABGAABGAA','ABGHAB','HAGBA',[0,5,11,20,26]),
    ]
    tests=[]
    for alphabet,T,W,H,hs in seeds:
        k=(len(T)-2)//2;u=len(H)
        assert len(T)==2*k+2 and len(W)==k
        assert set(alphabet)<=set(T+W+H)
        oT,oTail=(oracle(k,u,alphabet,T,W,H) if k<=2 else (None,None))
        for h in hs:
            dense,rd=measured(k,u,alphabet,T,W,H,h,False)
            sparse,rs=measured(k,u,alphabet,T,W,H,h,True)
            for a in ('classes','raw_mass','layer_states','transitions','max_width','terminal_states'):
                assert rd[a]==rs[a],(alphabet,h,a,rd[a],rs[a])
            assert dense.fullP==sparse.fullP and dense.fullQ==sparse.fullQ
            if oT is not None:
                count=Counter(dense.key(t,w,z) for t in oT for w,z in oTail)
                assert rd['raw_mass']==len(oT)*len(oTail)==sum(count.values())
                assert rd['classes']==len(count)
                if len(count)<1000:
                    for n,key in enumerate(sorted(count)):
                        assert dense.unrank(n)==sparse.unrank(n)==key
                        assert dense.rank(key)==sparse.rank(key)==n
            tests.append({'alphabet':alphabet,'k':k,'u':u,'h':h,
                'actual_initial_K':len(T),'deltaP':dense.deltaP,'deltaQ':dense.deltaQ,
                'full_144_nonzero':sum(bool(x) for x in dense.fullQ),
                'oracle_T':len(oT) if oT is not None else None,
                'oracle_tails':len(oTail) if oTail is not None else None,
                'dense':rd,'sparse':rs})
    return {'schema':'EM_STAGE488B_SIGNED_SPARSE_BRC_EXECUTION_V1',
      'signed_axes':{c:V[c] for c in D},'tests':tests,
      'interior_edit_counterexample':interior_edit_counterexample(),
      'assertions':'PASS'}

if __name__=='__main__':
    result=run()
    out=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'STAGE488B_EXECUTED.json')
    with open(out,'w') as f:json.dump(result,f,ensure_ascii=False,indent=2)
    print(json.dumps({'assertions':'PASS','cases':len(result['tests']),
       'case_summaries':[(x['alphabet'],x['h'],x['sparse']['classes'],x['sparse']['raw_mass'],x['dense']['component_count'],x['sparse']['component_count']) for x in result['tests']],
       'edit':result['interior_edit_counterexample']},ensure_ascii=False))
