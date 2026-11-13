#!/usr/bin/env python3
"""Stage489-B: complete 144-pair native-X6 signed input and three-representation cost audit.
Five independent repeats; wall times are measurements, not reproducible exact integers.
"""
from collections import Counter
from math import factorial
from statistics import median
from time import perf_counter
import tracemalloc, json
D='ABCDEFGHIJKL'
V={D[i]:tuple(int(j==i) for j in range(6)) for i in range(6)}
V.update({D[i+6]:tuple(-int(j==i) for j in range(6)) for i in range(6)})

def complete_word():
    # Euler tour on K_12 with loops. One each of 144 directed pairs.
    out=[list(range(11,-1,-1)) for _ in range(12)]
    stack=[0]; order=[]
    while stack:
        i=stack[-1]
        if out[i]:stack.append(out[i].pop())
        else:order.append(stack.pop())
    w=''.join(D[i] for i in reversed(order))
    assert len(w)==145 and all(v==1 for v in Counter(zip(w,w[1:])).values())
    assert len(set(zip(w,w[1:])))==144
    return w

def bench(w,s):
    counts=Counter(zip(w,w[1:])); active=tuple(sorted(counts)); assert len(active)==s
    def base():
        c=Counter(zip(w,w[1:]))
        full=tuple(c.get((a,b),0) for a in D for b in D)
        delta=tuple(sum(V[z][i] for z in w) for i in range(6))
        assert sum(full)==len(w)-1
        return full,delta
    def sparse():
        e,_=base();ix=tuple(i for i,n in enumerate(e) if n)
        return ix,tuple(e[i] for i in ix)
    def trie():
        e,_=base();return {a:{b:e[12*i+j] for j,b in enumerate(D) if e[12*i+j]}
                             for i,a in enumerate(D) if any(e[12*i:12*i+12])}
    dense,_=base();ix,sv=sparse();tree=trie(); slot=dict(zip(active,range(s)))
    def cd(pair):
        i=12*D.index(pair[0])+D.index(pair[1]);v=list(dense);v[i]-=1;return tuple(v)
    def cs(pair):
        v=list(sv);v[slot[pair]]-=1;return tuple(v)
    def ct(pair):
        a,b=pair;v=dict(tree);row=dict(v[a]);row[b]-=1;v[a]=row;return v
    ops=tuple(active[i%s] for i in range(2500))
    def measure(fn,n):
        times=[];peaks=[]
        for _ in range(5):
            tracemalloc.start();t=perf_counter()
            for i in range(n):fn(i)
            dt=perf_counter()-t;_,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
            times.append(dt);peaks.append(peak)
        return {'seconds':round(median(times),6),'peak_B':int(median(peaks))}
    prep={k:measure(lambda i:f(),15) for k,f in [('dense',base),('sparse',sparse),('trie',trie)]}
    edits={k:measure(lambda i:f(ops[i]),2500) for k,f in [('dense',cd),('sparse',cs),('trie',ct)]}
    return {'s':s,'word_len':len(w),'full_observer_fields':144,'delta6':base()[1],
            'slots':{'dense':144,'sparse':s,'trie_nodes':1+len(tree)+s},
            'preprocess_15':prep,'decrement_2500':edits}

def main():
    word=complete_word()
    pop=12**10*factorial(12)*(factorial(11)**11)
    assert pop.bit_length()==343 and len(str(pop))==104
    result={'all_144_edges_once':True,'complete_word_len':len(word),
            'Euler_paths':str(pop),'Euler_bits':pop.bit_length(),'Euler_digits':len(str(pop)),
            'windows':[bench(word[:s+1],s) for s in (5,20,60,144)],
            'scope':'5 repeats; full from-word 144-field preprocess; 2500 independent single-edge decrements; Python tracemalloc peaks; no 144-edge DP'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))
if __name__=='__main__':main()
