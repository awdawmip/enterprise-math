#!/usr/bin/env python3
"""R284DR: 256 Port minimum-pair witnesses with zero point-to-arc calls in construction."""
import hashlib
import json
from collections import Counter
from R284DP_eight_skeleton_fast_pair_generator_checker import (
    G, P, q3, residue, frozen_arcs,
)
from R284DD_attributed_envelope_checker import (
    attributed_envelope, labeled_farthest,
)

EXPECTED = '7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a'

def verify():
    arcs = frozen_arcs()
    events, profiles = attributed_envelope(arcs)
    assert len(arcs) == 64 and len(events) == 194 and len(profiles) == 193
    lows = sorted(1056 | (x<<9) | (y<<8) | (z<<4)
                  for x in (0,1) for y in (0,1) for z in (0,1))
    assert lows == [1056,1072,1312,1328,1568,1584,1824,1840]
    pairs = set()
    labels = Counter()
    patterns = Counter()
    for low in lows:
        for upper in range(0,16,2):
            root = (upper<<12) | low
            gaps = []
            for shift in G:
                a = root ^ shift
                b = a ^ 4096
                change = q3(a & 4095)
                assert change in (59,60)
                x = residue(a)
                y = (x - change) % P
                dx, lx = labeled_farthest(x, events, profiles, len(arcs))
                dy, ly = labeled_farthest(y, events, profiles, len(arcs))
                assert len(lx) == len(ly) == 1 and lx == ly
                gap = abs(dx - dy)
                assert gap == change
                gaps.append(gap)
                labels[lx[0]] += 1
                pairs.add((min(a,b),max(a,b)))
            assert max(gaps) == 60
            patterns[tuple(gaps)] += 1
    assert len(pairs) == 256
    digest = hashlib.sha256(b''.join(a.to_bytes(2,'big')+b.to_bytes(2,'big')
                             for a,b in sorted(pairs))).hexdigest()
    assert digest == EXPECTED
    assert patterns == Counter({(60,60,60,60):32,(60,60,59,59):32})
    assert labels == Counter({21:45,32:21,44:37,45:19,55:64,56:43,63:27})
    return {
        'schema':'R284DR_BOOLEAN_EVENT_ENVELOPE_PAIR_CERTIFICATE_V1',
        'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'source_pin':'awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py',
        'minimum_and_pair_count_dependency':'R284DN full-universe finite theorem',
        'skeleton_iff_dependency':'R284DQ symbolic lower-variable theorem',
        'event_label_envelope_dependency':'R284DD exact two-slope envelope theorem',
        'lower_skeletons':lows,
        'arc_count':len(arcs),
        'envelope_event_count':len(events),
        'envelope_slabs':len(profiles),
        'source_determinant_calls_for_witness_bases':256,
        'partner_residue_values_by_exact_increment':256,
        'event_predecessor_lookup_calls':512,
        'point_to_arc_distance_calls_in_construction':0,
        'constructed_minimum_pairs':len(pairs),
        'pair_list_sha256':digest,
        'representative_gap_patterns':{str(k):v for k,v in sorted(patterns.items())},
        'winning_arc_labels':dict(sorted(labels.items())),
        'independent_review':'NOT_REVIEWED',
    }

if __name__=='__main__':
    cert=verify()
    with open('R284DR_boolean_event_envelope_certificate.json','w',encoding='utf-8') as f:
        json.dump(cert,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print(json.dumps(cert,ensure_ascii=False,indent=2))
