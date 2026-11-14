#!/usr/bin/env python3
"""R762AR exact ordered V29-like causal-token residual verifier.
Standard-library Python 3. Uses integer-only complete finite enumeration.
"""
import itertools
import json

V=("A","B","C")
EDGES=tuple((a,b) for a in V for b in V)

def residual(word, vertices):
    D={v:0 for v in vertices}
    H={v:0 for v in vertices}
    for a,b in word:
        H[a]=max(H[a],D[a]+1)
        D[a]+=1
        D[b]-=1
    return D,H

def compose(r1,r2,vertices):
    d1,h1=r1
    d2,h2=r2
    return ({v:d1[v]+d2[v] for v in vertices},
            {v:max(h1[v],d1[v]+h2[v]) for v in vertices})

def replay(word,repeat,inventory):
    n=dict(inventory)
    for _ in range(repeat):
        for a,b in word:
            if n[a]<1:
                return False,n
            n[a]-=1
            n[b]+=1
    return True,n

def predicted(d,h,r):
    return {v:h[v]+(r-1)*max(0,d[v]) for v in d}

def check():
    counts=[]
    balanced=0
    total=0
    checks=0
    split_checks=0
    for length in range(1,7):
        count=0
        for word in itertools.product(EDGES,repeat=length):
            count+=1
            total+=1
            d,h=residual(word,V)
            assert sum(d.values())==0
            balanced+=int(all(x==0 for x in d.values()))
            if length<=5:
                for k in range(length+1):
                    combined=compose(residual(word[:k],V),
                                     residual(word[k:],V),V)
                    assert combined==(d,h)
                    split_checks+=1
            for r in (1,2,3,4):
                expected=predicted(d,h,r)
                d_full,h_full=residual(word*r,V)
                assert h_full==expected
                assert all(d_full[v]==r*d[v] for v in V)
                ok,end=replay(word,r,expected)
                assert ok
                assert all(end[v]==expected[v]-r*d[v] for v in V)
                for v in V:
                    if expected[v]>0:
                        less=dict(expected)
                        less[v]-=1
                        assert not replay(word,r,less)[0]
                checks+=1
        counts.append(count)
    grouped=[("A","B"),("A","B"),("B","A"),("B","A")]
    alternating=[("A","B"),("B","A"),("A","B"),("B","A")]
    assert residual(grouped,V)[1]["A"]==2
    assert residual(alternating,V)[1]["A"]==1
    assert residual([("A","A")],V)[1]["A"]==1
    def historical(shared):
        tri=[("A0","A1"),("A1","A2"),("A2","A0")]
        outgoing=[("A0","B1")]*2+[("A1","B1")]*4+[("A2","B1")]*3
        if shared:
            outgoing=[(a,"B0") for a,_ in outgoing]
        word=tri+outgoing+[("B0","A3")]*10
        nodes=tuple(sorted({v for edge in word for v in edge}))
        d,h=residual(word,nodes)
        seed=sum(h.values())
        rate=sum(max(0,x) for x in d.values())
        expected=10 if shared else 19
        assert len(word)==22 and seed==rate==expected
        assert replay(word,4,predicted(d,h,4))[0]
        return {"seed":seed,"slope":rate,"four_repeats_seed":seed+3*rate}
    evidence={
        "research_unit":"R762AR",
        "model":"conditional V29 causal-token ordered-event semantics",
        "frozen_science_commit":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "arithmetic":"exact_integer",
        "graph":"3 labeled ports; all 9 directed edges including loops",
        "word_lengths":[1,2,3,4,5,6],
        "words_by_length":counts,
        "total_words":total,
        "balanced_words":balanced,
        "unbalanced_words":total-balanced,
        "repeat_factors":[1,2,3,4],
        "repetition_instances":checks,
        "composition_splits_checked":split_checks,
        "grouped_vs_alternating_hA":[2,1],
        "self_loop_hA":1,
        "historical_original":historical(False),
        "historical_shared_port":historical(True),
        "native_force_admission":False,
        "independent_driver_review":False
    }
    assert total==597870 and balanced==40572 and checks==2391480
    print(json.dumps(evidence,ensure_ascii=False,indent=2,sort_keys=True))
if __name__=="__main__":
    check()
