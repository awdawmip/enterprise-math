#!/usr/bin/env python3
"""R284CG. Exact, self-contained finite certificate for modular-fiber signatures."""
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
import json

P = 17179869143
D = (1120832, 6, 13, 1651128)
Z = (0, 390139, 394465, 1497639)
SELECTED = (0, 1, 2, 4, 5, 6)
FROZEN_DIGEST = "b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4"


def formula(lower, top):
    u1, a11, x, y, u2, w, a22, z, u3, g, h, r = lower
    t, s = 6-a11, 13-a22
    u = t*s-x*w
    v = -r*u-z*(t*h+x*g)-y*(w*h+s*g)
    p1, p2 = s*u1+x*u2, t*u2+w*u1
    q1 = -r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2 = -r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3 = u*u3+p1*g+p2*h
    k = (u*D[3]+v, p1*D[3]+q1, p2*D[3]+q2, q3)
    base = D[0]*k[0]-Z[1]*k[1]-Z[2]*k[2]-Z[3]*k[3]-sum(k)
    return base-sum(k[j] for j in range(4) if top & (1<<j))


def lower_for_key(key, other):
    lower = [other]*12
    for j, pos in enumerate(SELECTED):
        lower[pos] = 1+((key>>(5-j)) & 1)
    return lower


def leibniz(lower, top):
    c = [[1+((top>>j)&1) for j in range(4)],
         list(lower[:4]), list(lower[4:8]), list(lower[8:12])]
    m = [[(D[i] if i == j else 0)-c[i][j]-(Z[j] if i == 0 else 0)
          for j in range(4)] for i in range(4)]
    out = 0
    for permutation in permutations(range(4)):
        parity = sum(permutation[i] > permutation[j]
                     for i in range(4) for j in range(i+1,4)) % 2
        term = 1
        for i,j in enumerate(permutation):
            term *= m[i][j]
        out += -term if parity else term
    return out


def circular_union(arcs):
    intervals=[]
    for a,width in arcs:
        b=a+width
        if b>=P:
            intervals.extend([(a,P),(0,b-P)])
        else:
            intervals.append((a,b))
    intervals.sort()
    merged=[]
    for a,b in intervals:
        if merged and a<=merged[-1][1]:
            merged[-1]=(merged[-1][0],max(merged[-1][1],b))
        else:
            merged.append((a,b))
    return len(merged), sum(b-a for a,b in merged)


def verify():
    arcs=[]
    for key in range(64):
        bottom=formula(lower_for_key(key,2),15)
        top=formula(lower_for_key(key,1),0)
        assert bottom==leibniz(lower_for_key(key,2),15)
        assert top==leibniz(lower_for_key(key,1),0)
        width=top-bottom
        assert 0<width<P/2
        arcs.append((bottom%P,width))
    assert min(w for _,w in arcs)==307592214
    assert max(w for _,w in arcs)==450181375

    words=[]
    digest=sha256()
    for topbits in product((1,2),repeat=4):
        top=sum((v-1)<<j for j,v in enumerate(topbits))
        for lower in product((1,2),repeat=12):
            x=formula(lower,top)%P
            words.append(x)
            digest.update(x.to_bytes(8,"big"))
    assert len(words)==65536 and len(set(words))==65536
    assert digest.hexdigest()==FROZEN_DIGEST
    ordered=sorted(words)
    min_code_gap=min([ordered[i+1]-ordered[i] for i in range(len(ordered)-1)]
                     +[P+ordered[0]-ordered[-1]])
    assert min_code_gap==59

    active_hist=Counter()
    forced_hist=Counter()
    forced_by_bit=[0]*6
    signatures=Counter()
    outside_margin=P
    outside_witness=None
    for x in words:
        candidates=[]
        for key,(a,width) in enumerate(arcs):
            d=(x-a)%P
            if d<=width:
                candidates.append(key)
            else:
                separation=min(d-width,P-d)
                if separation<outside_margin:
                    outside_margin=separation
                    outside_witness={"codeword":x,"arc_key":key,
                                     "arc_start":a,"arc_width":width,
                                     "distance":separation}
        assert candidates
        active_hist[len(candidates)]+=1
        signatures[tuple(candidates)]+=1
        forced=0
        for bit in range(6):
            choices={((key>>(5-bit))&1) for key in candidates}
            if len(choices)==1:
                forced_by_bit[bit]+=1
                forced+=1
        forced_hist[forced]+=1
    assert outside_margin==1183
    assert dict(sorted(active_hist.items()))=={1:23178,2:23094,3:16964,4:2300}
    assert dict(sorted(forced_hist.items()))=={0:4696,1:17702,2:7734,3:10426,4:1532,5:268,6:23178}
    assert forced_by_bit==[38486,34564,41552,34442,30026,31914]
    assert len(signatures)==114
    components,coverage=circular_union(arcs)
    assert (components,coverage)==(15,14595332646)
    return {
        "schema":"R284CG_MODULAR_FIBER_SIGNATURE_EXACT_V1",
        "model":{"p":P,"d":D,"z":Z,"selected_lower_positions":SELECTED},
        "frozen_codeword_sha256":FROZEN_DIGEST,
        "complete_candidate_matrices":len(words),
        "independent_leibniz_endpoint_checks":128,
        "global_min_codeword_gap":min_code_gap,
        "group_arcs":64,
        "min_arc_width":min(w for _,w in arcs),
        "max_arc_width":max(w for _,w in arcs),
        "unexpanded_arc_union_components":components,
        "unexpanded_arc_union_length":coverage,
        "outside_arc_min_distance":outside_margin,
        "outside_arc_witness":outside_witness,
        "stable_radius_strict_upper_bound":"1183/2",
        "signature_histogram_by_active_arc_count":dict(sorted(active_hist.items())),
        "distinct_active_arc_signatures":len(signatures),
        "forced_critical_bits_histogram":dict(sorted(forced_hist.items())),
        "forced_by_bit_count":forced_by_bit,
        "at_least_one_critical_bit_forced":len(words)-forced_hist[0],
        "all_six_critical_bits_forced":forced_hist[6],
        "sum_of_forced_bit_incidents":sum(forced_by_bit),
        "coverage":"entire 2^16 frozen binary matrix domain; exact integer arithmetic",
        "inference":"All signature and forced-bit counts hold for every circular real observation error radius rho<1183/2 if arcs are tested after inflation by the same rho.",
        "review":"NOT_REVIEWED"
    }


if __name__=="__main__":
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
