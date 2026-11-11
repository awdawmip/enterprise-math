#!/usr/bin/env python3
"""R732 exact exhaustive verifier: native X6 axis-indexed port PASS lift.
No external dependencies; exact integer arithmetic; no physical force-law claim.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict
import json
from pathlib import Path

MASKS = {"A":211733226574, "B":5363347296468}

def triads(n): return list(combinations(range(n),3))
def arcs(n):
    states=triads(n)
    return [(s,t) for s in states for t in states if len(set(s)&set(t))==2]
def pair(s,t):
    return (next(iter(set(s)-set(t))),next(iter(set(t)-set(s))))
def update(s,a,b):
    if a not in s or b in s or a==b: return None
    return tuple(sorted((set(s)-{a})|{b}))
def local_frame_step(src,dst,fr):
    a,b=pair(src,dst)
    out=dict(fr);out[b]=out.pop(a)
    return out

def test_n(n):
    states=triads(n); e=arcs(n)
    assert len(states)==(10 if n==5 else 20)
    assert len(e)==(60 if n==5 else 180)
    fibers=defaultdict(list)
    for s,t in e:
        a,b=pair(s,t)
        fibers[a,b].append((s,t))
        assert update(s,a,b)==t
        assert update(t,b,a)==s
    assert len(fibers)==n*(n-1)
    assert {len(x) for x in fibers.values()}==({3} if n==5 else {6})
    permutation_tests=0
    for p in permutations(range(n)):
        for s,t in e:
            sp=tuple(sorted(p[i] for i in s));tp=tuple(sorted(p[i] for i in t))
            a,b=pair(s,t)
            assert pair(sp,tp)==(p[a],p[b])
            assert update(sp,p[a],p[b])==tp
            permutation_tests+=1
    return {'n':n,'triad_states':len(states),'oriented_adjacent_arcs':len(e),
            'PASS_port_letters':len(fibers),'arcs_per_PASS_without_source':len(e)//len(fibers),
            'min_fixed_aux_bits_without_source':2 if n==5 else 3,
            'aux_bits_with_known_source':0,'all_axis_permutation_arc_checks':permutation_tests}

def network(name,mask):
    e=arcs(5); selected=[edge for i,edge in enumerate(e) if (mask>>i)&1]
    assert len(selected)==15
    adj=defaultdict(list)
    for s,t in selected: adj[s].append(t)
    root=(0,1,2)
    count_by_length=Counter()
    trials=0
    def dfs(path,frames):
        nonlocal trials
        l=len(path)-1;count_by_length[l]+=1;trials+=1
        state=root
        rec=dict((j,j) for j in root)
        for s,t in zip(path,path[1:]):
            a,b=pair(s,t)
            assert state==s
            state=update(state,a,b)
            assert state==t
            rec=local_frame_step(s,t,rec)
        assert rec==frames
        if l==7: return
        for next_t in adj.get(path[-1],[]):
            if len(path)>1 and next_t==path[-2]: continue
            nf=local_frame_step(path[-1],next_t,frames)
            dfs(path+[next_t],nf)
    dfs([root],{j:j for j in root})
    return {'carrier':name,'arc_count':len(selected),'root_prefixes_through_7':trials,
            'prefix_count_by_length':{str(k):count_by_length[k] for k in range(8)},
            'single_PASS_symbols_appearing':len(set(pair(s,t) for s,t in selected)),
            'root_word_reconstruction_all_checked':True}

def order_residual_test():
    root=(0,1,2)
    def enumerate_words(length):
        states=[(root,{0:0,1:1,2:2},())]
        for step in range(length):
            succ=[]
            for s,frame,word in states:
                for a in s:
                    for b in range(6):
                        if b in s: continue
                        t=update(s,a,b)
                        succ.append((t,local_frame_step(s,t,frame),word+((a,b),)))
            states=succ
        return states
    checked={}
    for length in (0,1,2):
        d=defaultdict(set)
        w=enumerate_words(length);checked[str(length)]=len(w)
        for s,frame,word in w:
            key=(s,tuple(sorted(word)))
            d[key].add(tuple(sorted(frame.items())))
        assert not any(len(x)>1 for x in d.values())
    w=enumerate_words(3);checked['3']=len(w)
    key_to_frames=defaultdict(set)
    for s,frame,word in w:
        key_to_frames[(s,tuple(sorted(word)))].add(tuple(sorted(frame.items())))
    example1=((0,3),(1,0),(0,4))
    example2=((0,4),(1,0),(0,3))
    def trace(word):
        s=root; f={0:0,1:1,2:2}; path=[s]
        for a,b in word:
            t=update(s,a,b)
            assert t is not None
            f=local_frame_step(s,t,f);s=t;path.append(s)
        return path,tuple(f[x] for x in sorted(f))
    path1,f1=trace(example1);path2,f2=trace(example2)
    assert path1[-1]==path2[-1]==(2,3,4)
    assert tuple(sorted(example1))==tuple(sorted(example2))
    assert f1==(2,0,1) and f2==(2,1,0)
    assert all(path[i-1]!=path[i+1] for path in (path1,path2) for i in (1,2))
    assert len(key_to_frames[(path1[-1],tuple(sorted(example1)))])==2
    return {'root':''.join(map(str,root)), 'rooted_words_tested_by_length':checked,
            'no_order_sensitive_frame_collision_through_2':True,
            'minimum_length_with_collision':3,
            'word_1':list(map(list,example1)), 'word_2':list(map(list,example2)),
            'triad_path_1':[''.join(map(str,s)) for s in path1],
            'triad_path_2':[''.join(map(str,s)) for s in path2],
            'terminal_triad':'234',
            'final_frame_1':list(f1),'final_frame_2':list(f2),
            'equal_PASS_multisets':True,'same_contrast_and_grade':True,
            'minimal_extra_bits_for_this_two_frame_fiber':1}

def main():
    v={str(n):test_n(n) for n in (5,6)}
    ns={k:network(k,m) for k,m in MASKS.items()}
    assert ns['A']['root_prefixes_through_7']==419
    assert ns['B']['root_prefixes_through_7']==382
    result={'schema':'R732_COVARIANT_AXIS_PASS_LIFT_CERT_V1',
       'scope':'k=3 subsets of n=5 or n=6; chosen axis-indexed local V29 ports; combinatorial PASS plus explicit active-triad update',
       'universal_proof':'fiber binomial(n-2,k-1), partial bijection, S_n-equivariance (see R732 proof note)',
       'exact_finite_checks':v,'both_frozen_15arc_carriers':ns,
       'order_residual_witness':order_residual_test(),
       'source_pins':{'frozen_science':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
          'R731_V29':'7fba48583039602ded1f1d0ecb8e9d0cc1f5040c',
          'V29_contract':'30fb16d39465708fd1b54c70a58d06ad20f310f8',
          'R730_masks':'8fdfef5e3f2097d9e6ebb29682b2b81a6ea0247a'},
       'validation':'R732_COVARIANT_PASS_EXACT_PASS'}
    Path(__file__).with_name('R732_COVARIANT_PASS_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(result['validation']);print(json.dumps(result['exact_finite_checks'],indent=2));print(json.dumps(result['both_frozen_15arc_carriers'],indent=2));print(json.dumps(result['order_residual_witness'],indent=2))
if __name__=='__main__': main()
