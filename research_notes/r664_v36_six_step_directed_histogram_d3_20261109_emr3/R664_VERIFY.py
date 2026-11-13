#!/usr/bin/env python3
"""R664: exact directed-edge histogram vs V17 frame on based J(6,3) walks."""
from collections import Counter, defaultdict
from itertools import combinations, permutations
import json
from pathlib import Path

BASE=(0,1,2)
TRIADS=tuple(combinations(range(6),3))
NEIGH={t:tuple(s for s in TRIADS if len(set(t)&set(s))==2) for t in TRIADS}
ID=BASE

def step(a,b,labels):
    assert b in NEIGH[a]
    leave=next(iter(set(a)-set(b)))
    enter=next(iter(set(b)-set(a)))
    label=dict(zip(a,labels))
    label[enter]=label[leave]
    return tuple(label[x] for x in b)

def perm_step(a,b):
    # Position in old sorted triad assigned to each new position.
    leave=next(iter(set(a)-set(b)))
    enter=next(iter(set(b)-set(a)))
    return tuple(a.index(leave if x==enter else x) for x in b)

def mul(u,v):return tuple(u[v[i]] for i in range(3))
def inv(u):return tuple(u.index(i) for i in range(3))
def hol(w):
    p=q=ID
    for a,b in zip(w,w[1:]+(BASE,)):
        p=step(a,b,p)
        q=mul(q,perm_step(a,b))
    assert p==q
    return p

for old in TRIADS:
    for new in NEIGH[old]:
        for labels in permutations(range(3)):
            assert step(old,new,labels)==mul(labels,perm_step(old,new))

def signature(word):
    return tuple(sorted(Counter(zip(word,word[1:]+(BASE,))).items()))

summary={}
example=None
for n in range(2,7):
    fiber=defaultdict(Counter)
    first={}
    total=0
    def walk(seq,slots,edge_counts):
        global total,example
        depth=len(seq)-1
        at=seq[-1]
        if depth==n:
            if at!=BASE:return
            total+=1
            k=tuple(sorted(edge_counts.items()))
            fiber[k][slots]+=1
            if (k,slots) not in first:first[k,slots]=tuple(seq[:-1])
            return
        choices=(BASE,) if depth==n-1 else NEIGH[at]
        for dst in choices:
            if dst not in NEIGH[at]:continue
            e=(at,dst)
            edge_counts[e]+=1
            seq.append(dst)
            walk(seq,step(at,dst,slots),edge_counts)
            seq.pop()
            edge_counts[e]-=1
            if not edge_counts[e]:del edge_counts[e]
    walk([BASE],ID,Counter())
    amb={k:v for k,v in fiber.items() if len(v)>1}
    ordered=sum(sum(v.values())**2-sum(z*z for z in v.values()) for v in amb.values())
    summary[str(n)]={"closed_words":total,"distinct_directed_transition_histograms":len(fiber),
                     "ambiguous_histograms":len(amb),"different_holonomy_ordered_pairs":ordered}
    if n<6:assert not amb
    else:
        assert amb
        k,v=next(iter(amb.items()))
        a,b=list(v)[:2]
        example={"histogram":str(k),"first_word":first[k,a],
                 "second_word":first[k,b],"holonomies":(a,b)}

A=(BASE,(0,1,3),(0,2,3))
B=(BASE,(0,1,3),(1,2,3))
AB=A+B
BA=B+A
assert hol(A)==(0,2,1) and hol(B)==(2,1,0)
assert signature(AB)==signature(BA)
assert hol(AB)==(1,2,0) and hol(BA)==(2,0,1)
assert mul(hol(BA),inv(hol(AB)))==(1,2,0)

chart=((0,0,0,0,0,0),(1,0,0,0,0,0),(1,1,0,0,0,0),
       (1,1,1,0,0,0),(0,1,1,0,0,0),(0,0,1,0,0,0))
assert len(set(chart))==6
assert all(sum(abs(a-b) for a,b in zip(chart[i],chart[(i+1)%6]))==1 for i in range(6))
for W in (AB,BA):
    state=list(W)
    for t in range(6):
        future=[state[(i+1)%6] for i in range(6)]
        assert all(future[i] in NEIGH[state[i]] for i in range(6))
        state=future
    assert tuple(state)==W

assert [summary[str(n)]["closed_words"] for n in range(2,7)]==[9,36,369,2952,26937]
assert [summary[str(n)]["distinct_directed_transition_histograms"] for n in range(2,7)]==[9,36,333,2628,22647]
assert summary["6"]["ambiguous_histograms"]==108
assert summary["6"]["different_holonomy_ordered_pairs"]==288
result={"marker":"R664_MINIMAL_SIX_STEP_HISTOGRAM_D3_COLLISION_EXACT_PASS",
        "source":"V17/V20/V36, R663 author-side; frozen R462 unchanged",
        "domain":"based closed J(6,3) directed-edge paths, 2<=length<=6; repeats allowed",
        "enumeration":summary,
        "witness":{"triangle_A":A,"triangle_B":B,"A_then_B":AB,"B_then_A":BA,
                   "h_A":hol(A),"h_B":hol(B),"h_AB":hol(AB),"h_BA":hol(BA),
                   "relative":mul(hol(BA),inv(hol(AB))),
                   "same_directed_transition_histogram":True},
        "six_cell_x6_chart":chart,"v36_strict_copy_ring":True,
        "first_ambiguous_fiber_example":example,
        "scope":"Directed transition counts vs V17 group memory; V36 cyclic relation dynamics; no V29 H assumed.",
        "review":"AUTHOR_SIDE_UNREVIEWED"}
Path(__file__).with_name("R664_EVIDENCE.json").write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(result["marker"])
for n,row in summary.items():print(n,row)
print("Witness",result["witness"])
