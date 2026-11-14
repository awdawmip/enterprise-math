"""R762V: signed X6 three-axis six-step loop census and BRC projection.
Exact Python 3 / standard library only. All permutations are enumerated.
No native force-event admission or V39 transport is inferred.
"""
from collections import Counter, defaultdict
from itertools import permutations, combinations
import json

STEPS=(1,-1,2,-2,3,-3)

def data(word):
    p = [0,0,0]
    visits = set()
    early = False
    current = Counter()
    for t,s in enumerate(word, 1):
        before = tuple(p)
        axis=abs(s)-1
        p[axis] += 1 if s>0 else -1
        after = tuple(p)
        visits.add(after)
        if s>0:
            current[(before,axis)] += 1
        else:
            current[(after,axis)] -= 1
        if t < 6 and p == [0,0,0]:
            early = True
    assert p == [0,0,0]
    orientation = tuple(next(1 if s>0 else -1
                             for s in word if abs(s)==k)
                        for k in (1,2,3))
    target = {tuple(orientation[k] if k==j else 0
                    for k in range(3)) for j in range(3)}
    return {
        "orientation":orientation,
        "early_return":early,
        "backtrack":any(word[i]==-word[i+1] for i in range(5)),
        "covers_ports":target.issubset(visits),
        "two_source":tuple(s for s in word if abs(s)!=3),
        "edge_current":tuple(sorted((key,value) for key,value in current.items() if value))
    }

def run():
    whole=Counter()
    per_orientation=defaultdict(Counter)
    two_lifts=defaultdict(Counter)
    port_fibers=defaultdict(list)
    current_fibers=defaultdict(list)
    signed_port_counts=Counter()
    for word in permutations(STEPS):
        d=data(word)
        early, back = d["early_return"], d["backtrack"]
        assert not early or back
        kind = "early_with_backtrack" if early else (
            "first_return_with_backtrack" if back else "first_return_nonbacktracking")
        whole[kind] += 1
        per_orientation[d["orientation"]][kind] += 1
        per_orientation[d["orientation"]]["total"] += 1
        two_lifts[d["two_source"]]["first_return" if not early else "early"]+=1
        if d["covers_ports"]:
            signed_port_counts[d["orientation"]]+=1
            if d["orientation"]==(1,1,1):
                port_fibers[d["two_source"]].append((word,d))
                current_fibers[(d["two_source"], d["edge_current"])].append(word)

    assert sum(whole.values()) == 720
    assert whole == Counter({"early_with_backtrack":240,
                            "first_return_with_backtrack":240,
                            "first_return_nonbacktracking":240})
    assert len(per_orientation)==8
    assert all(c["total"]==90 and
               all(c[k]==30 for k in whole)
               for c in per_orientation.values())
    assert len(signed_port_counts)==8 and set(signed_port_counts.values())=={24}
    projections=Counter()
    for w,c in two_lifts.items():
        assert sum(c.values())==30
        projections[(w[0]+w[1]==0,c["first_return"],c["early"])]+=1
    assert projections==Counter({(True,8,22):8,(False,26,4):16})
    expected = {(1,-1,2,-2):(8,1), (2,-2,1,-1):(8,1),
                (1,2,-1,-2):(4,2), (2,1,-2,-1):(4,2)}
    assert len(port_fibers)==4
    for w,(n,first) in expected.items():
        assert len(port_fibers[w])==n
        assert sum(not d["early_return"] for _,d in port_fibers[w])==first
    assert sum(len(x) for x in port_fibers.values())==24
    joint_hist=Counter(map(len,current_fibers.values()))
    assert joint_hist==Counter({1:14,2:2,3:2})
    for w,stuff in port_fibers.items():
        assert len({d["early_return"] for _,d in stuff})==2
    cover_first=sum(not d["early_return"] for stuff in port_fibers.values() for _,d in stuff)
    assert cover_first==6
    return {
      "schema":"R762V_EXACT_SIX_STEP_TRIAXIS_BRC_CENSUS_V1",
      "scientific_scope":"signed native X6 coordinate paths only; candidate triad incidence, not force closure",
      "six_letter_words_per_three_axis_support":720,
      "three_class_partition":dict(sorted(whole.items())),
      "first_occurrence_orientation_classes":8,
      "words_per_orientation":90,
      "words_per_class_per_orientation":30,
      "all_two_source_word_fibers": {
        "total_per_four_letter_word":30,
        "first_return_given_projected_first_two_inverse":8,
        "first_return_given_projected_first_two_distinct":26,
        "projected_first_two_inverse_words":8,
        "projected_first_two_distinct_words":16
      },
      "port_covering_fixed_orientation": {
        "total":24,"first_return":cover_first,"early_return":24-cover_first,
        "projected_two_source_fibers":[
           {"word":list(w),"total":len(port_fibers[w]),
            "first_return":sum(not d["early_return"] for _,d in port_fibers[w])}
           for w in sorted(port_fibers)
        ],
        "joint_projected_word_and_rooted_edge_current_fiber_histogram":
           {str(n):c for n,c in sorted(joint_hist.items())},
        "conditional_repair_bits_for_full_ordered_path_from_two_source_word":3,
        "conditional_repair_bits_from_joint_two_source_word_and_rooted_current":2
      },
      "all_signed_axis_support_choices":20,
      "all_signed_orientations":160,
      "all_six_step_loops_over_all_three_axis_supports":14400,
      "all_first_return_loops_over_all_supports":9600,
      "verification":"Exact exhaustive enumeration of 720 distinct six-step signed words; 8 orientations, 24 projected words; S6 support reindexing is a bijection",
      "sources":["Frozen P000 a72226e2430ffa4786321ac86e7f0c599d5f0389",
                 "R762H PR #2288 (24 port-covering shortest witnesses)",
                 "R762R PR #2333 (6 spoke excursions, 3-cycle candidate update)",
                 "R762U PR #2347 (conditional token scheduling)"]
    }

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
