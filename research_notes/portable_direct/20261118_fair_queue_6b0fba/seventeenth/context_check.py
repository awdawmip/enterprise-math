"""Replay DC03's finite signed tests, full transcript and empirical rounding check."""
from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, permutations, product
from pathlib import Path
import json
import sys

TARGET = (0, 0, 0, 0, 0, 1)
PORTS = tuple(range(6))
PAULI = ("XI", "IX", "XX", "IY", "YI", "YY", "XY", "YX", "ZZ")
BRC_SHA = "4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f"


def pack(bits):
    return sum(v << i for i,v in enumerate(bits))


def words(cells):
    return (tuple(pack(cells[3*i+j] for j in range(3)) for i in range(3))+
            tuple(pack(cells[3*i+j] for i in range(3)) for j in range(3)))


def multiply(a,b):
    if a == "I":
        return 0,b
    if b == "I":
        return 0,a
    if a == b:
        return 0,"I"
    c=({"X","Y","Z"}-{a,b}).pop()
    return (1 if a+b in ("XY","YZ","ZX") else 3),c


def operator_product(labels):
    phase=0
    symbols=["I","I"]
    for s in labels:
        for j in range(2):
            extra,symbols[j]=multiply(symbols[j],s[j])
            phase=(phase+extra)%4
    return phase,"".join(symbols)


def transcript_universe(brc):
    table = tuple(tuple(3*i+j for j in range(3)) for i in range(3))+tuple(
        tuple(3*i+j for i in range(3)) for j in range(3))
    for i,row in enumerate(table):
        for p in permutations(row):
            assert operator_product([PAULI[e] for e in p]) == (2*TARGET[i],"II")
    worlds={}
    wrong_at_vertex=Counter()
    error_spectrum=Counter()
    tomography=[Counter() for _ in PORTS]
    for bits in product(range(2),repeat=9):
        native=words(bits)
        errors=tuple((word.bit_count()%2)^target for word,target in zip(native,TARGET))
        error_spectrum[sum(errors)] += 1
        if sum(errors)==1:
            wrong_at_vertex[errors.index(1)] += 1
            for j,v in enumerate(native):
                tomography[j][v]+=1
        if any(errors[:3]):
            continue
        for e in range(9):
            alt=list(bits)
            alt[e]^=1
            w=native[:3]+words(alt)[3:]
            if tuple(v.bit_count()%2 for v in w)!=TARGET:
                continue
            assert w not in worlds
            # The mask records which setting-dependent pair differs. The 16 compatible
            # affine assignments define the external preparation for that mask.
            branch=brc.cwm_propagate(brc.cwm_edge(F(1,9)),brc.cwm_edge(F(1,16)))
            worlds[w]=(e,branch)
    assert sorted(wrong_at_vertex.values())==[16]*6
    assert error_spectrum=={1:96,3:320,5:96}
    assert len(worlds)==144
    weights=[{} for _ in PORTS]
    for w,(e,branch) in worlds.items():
        for j,v in enumerate(w):
            weights[j][v]=brc.cwm_recoalesce(weights[j].get(v,brc.CWM_ZERO),branch)
    for j in PORTS:
        assert len(weights[j])==4 and all(b.total==F(1,4) and b.count==36 for b in weights[j].values())
        assert all((F(tomography[j][v],96)==(F(5,24) if v.bit_count()%2==TARGET[j] else F(1,24)))
                   for v in range(8))
    return tuple(worlds),dict(error_spectrum),dict(baseline_minimax="1/6",
                   optimal_mismatch="1/9",single_fault_global_histories=144,
                   local_three_bit_string_probabilities=["1/4"]*4)


def crossing(w,subset):
    part=set(subset)
    result=[]
    for i,j in product(range(3),repeat=2):
        if (i in part) != (3+j in part):
            result.append(((w[i]>>j) if i in part else (w[3+j]>>i))&1)
    return pack(result)


def memory(worlds):
    count={}
    signatures={}
    for k in range(7):
        for a in combinations(PORTS,k):
            b=tuple(v for v in PORTS if v not in a)
            conditional=defaultdict(Counter)
            suffix_classes={}
            for w in worlds:
                p=tuple(w[i] for i in a)
                s=tuple(w[i] for i in b)
                conditional[p][s]+=1
                suffix_classes[s]=crossing(w,b)
            laws=set()
            for cn in conditional.values():
                tot=sum(cn.values())
                laws.add(tuple(sorted((v,F(n,tot)) for v,n in cn.items())))
            count[a]=len(laws)
            if a==(0,1,3):
                # One representative recorded prefix/suffix for every 5-bit frontier.
                prefix_by_cut={crossing(w,a):tuple(w[i] for i in a) for w in worlds}
                suffix_by_cut={v:s for s,v in suffix_classes.items()}
                # The parity of A's crossing equals sum of its target bits (zero)
                # precisely when its internal mismatch count is zero.
                keys=sorted(range(32),key=lambda x:(x.bit_count()%2,x))
                minor=[[int(suffix_by_cut[y] in conditional[prefix_by_cut[x]]) for y in keys] for x in keys]
                assert all(minor[i][i]==1 and not any(minor[i][:i]) for i in range(32))
                for i,x in enumerate(keys):
                    for j,y in enumerate(keys):
                        expected=x==y or (i<16 and j>=16 and (x^y).bit_count()==1)
                        assert bool(minor[i][j])==expected
            if a==(0,1,2):
                assert len(conditional)==len(suffix_classes)==48
                assert all(len(cn)==3 for cn in conditional.values())
                assert max(len(set(l)&set(r)) for l,r in combinations(conditional.values(),2))==1
            cut=(sum(i<3 for i in a),sum(i>=3 for i in a))
            assert cut not in signatures or signatures[cut]==len(laws)
            signatures[cut]=len(laws)
    profiles=Counter()
    general=Counter()
    for order in permutations(PORTS):
        prefix=tuple(count[tuple(sorted(order[:i]))] for i in range(7))
        profiles[prefix]+=1
        all_same=len({i<3 for i in order[:3]})==1
        general[48 if all_same else 32]+=1
    assert sorted(profiles.values())==[72,216,432] and general=={32:648,48:72}
    return dict(cut_state_counts=[[signatures[i,j] for j in range(4)] for i in range(4)],
                observable_profiles=[dict(states=list(p),orders=n) for p,n in sorted(profiles.items())],
                hidden_randomized_peak_orders=dict(sorted(general.items())),
                mixed_cut_unit_triangular_minor=32,row_cut_rectangle_max_size=3,
                approximate_hidden_width_32_if_full_joint_TV_below="1/(144*(5+sqrt(29)))")


def finite_graph_checks():
    # Independent full image with one signed occurrence at each end of each edge.
    tested={}
    for n in (3,4,5):
        signatures=Counter()
        for x in product((0,1),repeat=2*n):
            bad=tuple(x[2*v-1]^x[2*v]^(v==0) for v in range(n))
            mismatches=tuple(x[2*e]^x[2*e+1] for e in range(n))
            signatures[bad+mismatches]+=1
        assert len(signatures)==2**(2*n-1) and set(signatures.values())=={2}
        assert all(sum(v)%2==1 for v in signatures)
        # All n contexts demand anticorrelation, with identical values across edges.
        consistent=sum(all(x[v-1]^x[v] for v in range(n)) for x in product((0,1),repeat=n))
        assert consistent==(2 if n%2==0 else 0)
        tested[str(n)]={"frustrated_defect_images":len(signatures),
                        "all_anticorrelation_global_assignments":consistent}
    return tested


def experiment():
    # Minus the last column: these are all signed correlations in the six-term sum.
    corr=[F(n,100) for n in (92,93,90,90,89,91)]
    n=1100
    possible=[[k for k in range(n+1) if abs(1-F(2*k,n)-v)<=F(1,200)] for v in corr]
    hist=Counter()
    for k in product(*possible):
        total=6-F(2*sum(k),n)
        if abs(total-F(546,100))<=F(1,200) and abs(1-F(2*k[-1],n)-F(913,1000))<=F(1,2000):
            hist[sum(k)] += 1
    assert hist=={295:123,296:193,297:275,298:360,299:435}
    return dict(source="Kirchmair et al., arXiv:0904.1655v2, Fig. 2, Eq. (2), Eq. (3), Methods (5)",
                displayed_signed_scores=list(map(str,corr)),displayed_sum=str(sum(corr)),
                total_reported="5.46(4)",rounded_error_count_candidates=dict(sorted(hist.items())),
                number_of_candidate_six_tuples=sum(hist.values()),
                three_decimal_last_column_error_count=48,conditional_mismatch_sum_lower="0.73",
                reported_other_observer="2.23(5)",other_observer_threshold=2,
                raw_events_analyzed=0)


def main():
    parser=ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--json",type=Path)
    args=parser.parse_args()
    src=args.repo/"src"
    assert sha256((src/"enterprise_math/brc_weighted.py").read_bytes()).hexdigest()==BRC_SHA
    sys.path.insert(0,str(src))
    from enterprise_math import brc_weighted
    words_,errors,witness=transcript_universe(brc_weighted)
    out=dict(task="RS-DISC-COMPAT-20261026-03",native_verdict="MISSING_COMPONENT",
             brc_sha256=BRC_SHA,static_assignments_by_failures=errors,external_witness=witness,
             memory=memory(words_),cycle_distinct_defect_images=finite_graph_checks(),
             public_experimental_aggregate=experiment())
    data=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.json: args.json.write_text(data)
    else: print(data,end="")


if __name__=="__main__":
    main()
