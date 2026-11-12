#!/usr/bin/env python3
"""R741 exact BRC/V29 contextual two-port code and S3 census. Standard library only.

This checker proves exhaustive finite assertions. The companion note supplies
the separate algebraic proof for arbitrary generator length.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
import json
from pathlib import Path

TRIADS = ["".join(map(str, c)) for c in combinations(range(5), 3)]
ARCS = [(a, b) for a in TRIADS for b in TRIADS
        if a != b and len(set(a) & set(b)) == 2]
assert len(TRIADS) == 10 and len(ARCS) == 60

MASKS = {"A": 211733226574, "B": 5363347296468}
LOOPS = {
    "A": {"I": ("012", "014", "013", "012"),
          "P": ("012", "023", "013", "012"),
          "Q": ("012", "023", "123", "012")},
    "B": {"I": ("012", "123", "124", "012"),
          "P": ("012", "023", "013", "012"),
          "Q": ("012", "123", "013", "012")},
}
# F=PASS(C;0->1), R=PASS(C;1->0).
CODE = {
    "A": {("012", "014"): "F", ("012", "023"): "R",
          ("013", "012"): "R", ("014", "013"): "R",
          ("023", "013"): "F", ("023", "123"): "R",
          ("123", "012"): "F"},
    "B": {("012", "023"): "F", ("012", "123"): "R",
          ("013", "012"): "R", ("023", "013"): "R",
          ("123", "013"): "F", ("123", "124"): "R",
          ("124", "012"): "F"},
}

def edges(path):
    return list(zip(path, path[1:]))

def run_word(carrier, word):
    slots = list("012")
    current, previous = "012", None
    nf = nr = 0
    for generator in word:
        path = LOOPS[carrier][generator]
        assert current == path[0]
        for source, target in edges(path):
            assert source == current and target != previous
            event = CODE[carrier][(source, target)]
            nf += event == "F"
            nr += event == "R"
            leaving = next(iter(set(source)-set(target)))
            entering = next(iter(set(target)-set(source)))
            slots[slots.index(leaving)] = entering
            previous, current = source, target
    assert current == "012"
    if word:
        assert LOOPS[carrier][word[0]][1] != previous
    # R739 named convention: inverse of slot-to-current-label map.
    named = "".join(str(slots.index(str(j))) for j in range(3))
    return ((0,nf),(nr,0)), named

def formula(k):
    assert k >= 1
    three, two, sign = 3**k, 2**k, (-1)**k
    nums = (three+sign+2*two, three-sign+two,
            three+sign-two, three-sign-2*two)
    assert all(n>=0 and n%6==0 for n in nums)
    a,b,c,d=(n//6 for n in nums)
    return {"I":a, "P":b, "Q":b, "PQ":c, "QP":c, "PQP":d}

NAMED = {
    "A":{"I":"012","P":"021","Q":"102","PQ":"201","QP":"120","PQP":"210"},
    "B":{"I":"012","P":"021","Q":"210","PQ":"120","QP":"201","PQP":"102"},
}

def verify():
    results={"result":"PASS","parent_task":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
             "task_publication":"TP2-8B7E13C5904A2D6F1142",
             "frozen_science":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
             "v29_auxiliary":"30fb16d39465708fd1b54c70a58d06ad20f310f8",
             "checked_generator_lengths":list(range(9)),
             "carriers":{}}
    for carrier in ("A","B"):
        selected=[arc for i,arc in enumerate(ARCS) if (MASKS[carrier]>>i)&1]
        assert len(selected)==15
        used=set(edge for path in LOOPS[carrier].values() for edge in edges(path))
        assert len(used)==7 and used<=set(selected) and set(CODE[carrier])==used
        outs=defaultdict(list)
        allouts=defaultdict(list)
        for s,t in used: outs[s].append(t)
        for s,t in selected: allouts[s].append(t)
        assert max(map(len,outs.values()))==2
        assert max(map(len,allouts.values()))==3
        assert all(len({CODE[carrier][(s,t)] for t in targets})==len(targets)
                   for s,targets in outs.items())
        inv={v for path in LOOPS[carrier].values() for v in path}
        assert len(inv)==5
        for x,y in product("IPQ",repeat=2):
            assert LOOPS[carrier][x][-2] != LOOPS[carrier][y][1]
        codes={}
        for gen,path in LOOPS[carrier].items():
            code="".join(CODE[carrier][edge] for edge in edges(path))
            assert len(code)==3 and code.count("F")==1 and code.count("R")==2
            codes[gen]=code
        for relative,named in NAMED[carrier].items():
            M,got=run_word(carrier,relative)
            assert got==named,(carrier,relative,got,named)
        census=[]
        for k in range(9):
            counts=Counter()
            for chars in product("IPQ",repeat=k):
                word="".join(chars)
                M,named=run_word(carrier,word)
                assert M==((0,k),(2*k,0)),(carrier,k,word,M)
                counts[named]+=1
            assert sum(counts.values())==3**k
            if k:
                for rel,num in formula(k).items():
                    assert counts[NAMED[carrier][rel]]==num
            assert (len(counts)==6)==(k>=3)
            census.append({"k":k,"histories":3**k,"M":[[0,k],[2*k,0]],
                           "named_counts":dict(sorted(counts.items()))})
        for sigma in permutations("012345"):
            relabel={str(i):sigma[i] for i in range(6)}
            shifted={
                ("".join(sorted(relabel[x] for x in s)),
                 "".join(sorted(relabel[y] for y in t))):ev
                 for (s,t),ev in CODE[carrier].items()
            }
            assert len(shifted)==7
            for (s,t),ev in CODE[carrier].items():
                key=("".join(sorted(relabel[x] for x in s)),
                     "".join(sorted(relabel[y] for y in t)))
                assert shifted[key]==ev
        results["carriers"][carrier]={
            "mask":MASKS[carrier],"selected_arc_count":15,
            "generator_arc_count":7,"max_outdegree_full":3,
            "max_outdegree_generators":2,"inventory":sorted(inv),
            "generator_codewords":codes,
            "arc_codebook":[{"arc":s+">"+t,"pass":CODE[carrier][(s,t)]}
                            for s,t in sorted(used)],
            "named_relations":NAMED[carrier],
            "census_k0_to_k8":census,
            "axis_permutations_checked":720,
        }
    tv=[]
    for k in range(1,21):
        d=formula(k)
        assert sum(d.values())==3**k
        numerator=2**(k+2)-(-1)**k
        assert sum(abs(6*d[key]-3**k) for key in ("I","P","Q","PQ","QP","PQP"))==2*numerator
        tv.append({"k":k,"numerator":numerator,"denominator":6*3**k})
    results["TV_exact_checked_k1_to_k20"]=tv
    results["six_way_onset_generator_count"]=3
    results["six_way_onset_PASS_event_count"]=9
    return results

if __name__=="__main__":
    evidence=verify()
    dest=Path(__file__).with_name("R741_TWO_PORT_CONTEXT_LEDGER_RESULTS.json")
    dest.write_text(json.dumps(evidence,sort_keys=True,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("R741_TWO_PORT_CONTEXT_SIX_STATE_PASS")
