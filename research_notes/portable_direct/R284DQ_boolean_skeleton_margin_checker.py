#!/usr/bin/env python3
"""R284DQ: analytic eight skeletons; one-sided winner-margin certificate.
Run in research_notes/portable_direct next to R284DP and R284DM checkers.
"""
import hashlib
import json
from collections import Counter
from R284DP_eight_skeleton_fast_pair_generator_checker import (
    P, G, q3, residue, frozen_arcs, arc_dist,
)

REFERENCE = '7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a'

def verify():
    arcs = frozen_arcs()
    lower = [i for i in range(4096) if (i & 65) == 0]
    # Exact symbolic lemma: for w=1, q3 >= (t+1)(s+1) >= 60.
    # Equality forces a=b=2, u1=u2=u3=g=h=1, while x is free.
    direct = sorted(1056 | (x << 9) | (y << 8) | (z << 4)
                    for x in (0,1) for y in (0,1) for z in (0,1))
    selected = [i for i in lower if max(q3(i), q3(i^64)) <= 60]
    assert selected == direct
    assert direct == [1056,1072,1312,1328,1568,1584,1824,1840]
    assert Counter((q3(i),q3(i^64)) for i in direct) == Counter({(60,60):4,(60,59):4})

    pairs, winner_labels, gap_patterns, margins = [], Counter(), Counter(), []
    for low in direct:
        for upper in range(0,16,2):
            base = (upper<<12) | low
            gaps = []
            for flip in G:
                a = base ^ flip
                b = a ^ 4096
                delta = q3(a & 4095)
                assert delta in (59,60)
                x = residue(a)
                ds = [arc_dist(x, arc) for arc in arcs]
                best, second = sorted(range(64), key=lambda k: ds[k], reverse=True)[:2]
                margin = ds[best]-ds[second]
                assert margin > 2*delta
                # Each distance-to-arc function is 1-Lipschitz on the circle.
                # Hence the same arc remains the unique maximizer at y.
                y = (x-delta) % P  # exact beta3 determinant increment
                gap = abs(arc_dist(y, arcs[best])-ds[best])
                assert gap == delta
                gaps.append(gap)
                margins.append(margin)
                winner_labels[best] += 1
                pairs.append((min(a,b), max(a,b)))
            assert max(gaps) == 60
            gap_patterns[tuple(gaps)] += 1
    assert len(set(pairs)) == len(pairs) == 256
    digest = hashlib.sha256(b''.join(a.to_bytes(2,'big')+b.to_bytes(2,'big')
                             for a,b in sorted(pairs))).hexdigest()
    assert digest == REFERENCE
    assert gap_patterns == Counter({(60,60,60,60):32,(60,60,59,59):32})
    assert winner_labels == Counter({21:45,32:21,44:37,45:19,55:64,56:43,63:27})
    return {
        'schema':'R284DQ_BOOLEAN_SKELETON_MARGIN_CERTIFICATE_V1',
        'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'frozen_source':'enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py',
        'frozen_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
        'source_word_sha256_reference':'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4',
        'lower_representatives_checked':1024,
        'q3_evaluations':2304,
        'lower_skeletons':direct,
        'base_residues_by_determinant':256,
        'partner_residues_by_exact_increment':256,
        'point_arc_distance_evaluations':16640,
        'minimum_base_winner_margin':min(margins),
        'constructed_minimizer_pairs':len(pairs),
        'minimum_pair_sha256':digest,
        'label_histogram':dict(sorted(winner_labels.items())),
        'canonical_gap_patterns':{str(k):v for k,v in sorted(gap_patterns.items())},
        'global_delta_60_and_256_pair_count_input':'R284DN exact finite certificate; not recomputed',
        'independent_review':'NOT_REVIEWED',
    }

if __name__ == '__main__':
    result = verify()
    with open('R284DQ_boolean_skeleton_margin_certificate.json','w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
