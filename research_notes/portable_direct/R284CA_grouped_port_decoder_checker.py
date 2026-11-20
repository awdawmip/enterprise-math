#!/usr/bin/env python3
"""R284CA: exact grouped-index decoder certificate for R284BZ (stdlib only).

All arithmetic is integer. Input domain: 2^12 lower blocks and 2^4 top rows.
The interval sweep, in doubled integer coordinates, checks *every* real query
position on the residue circle (including half-integer interval endpoints).
"""
import bisect
import hashlib
import itertools
import json
from pathlib import Path

P = 17179869143
D0, D3, Z1, Z2, Z3 = 1120832, 1651128, 390139, 394465, 1497639
LOWER = list(itertools.product((1, 2), repeat=12))
HALF_DIAMETER_TWICE = 59  # closed rho=29.5; recovery rho<29.5


def block_record(L):
    u1, a11, x, y, u2, w, a22, z, u3, g, h, r = L
    t, s = 6-a11, 13-a22
    U = t*s-x*w
    V = -r*U-z*(t*h+x*g)-y*(w*h+s*g)
    p1, p2 = s*u1+x*u2, t*u2+w*u1
    q1 = -r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2 = -r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3 = U*u3+p1*g+p2*h
    k = (U*D3+V, p1*D3+q1, p2*D3+q2, q3)
    base = (D0*k[0]-Z1*k[1]-Z2*k[2]-Z3*k[3]-sum(k)) % P
    return base, k


def overlap_bound(records, bounds):
    """Maximum overlap of intervals [base-bound-29.5,base+29.5] on circle."""
    events = []
    for (base, _), bound in zip(records, bounds):
        for shift in (-P, 0, P):
            a = 2*(base+shift-bound)-HALF_DIAMETER_TWICE
            b = 2*(base+shift)+HALF_DIAMETER_TWICE
            if b < 0 or a > 2*P:
                continue
            events.append((max(a,0),0,1))
            events.append((min(b,2*P),1,-1))
    events.sort()
    overlap = maximum = 0
    coordinate = None
    for x, order, delta in events:
        overlap += delta
        if overlap > maximum:
            maximum, coordinate = overlap, x
    assert overlap == 0
    return maximum, coordinate


def verify():
    records = [block_record(L) for L in LOWER]
    assert len(records) == 4096
    assert all(all(k > 0 for k in ks) for _, ks in records)
    spans = [sum(ks) for _,ks in records]
    largest_span = max(spans)
    pairs = sorted((base, i) for i,(base,_) in enumerate(records))
    assert len({base for base,_ in pairs}) == 4096
    extended = sorted((base+shift,i) for base,i in pairs for shift in (-P,0,P))
    evalues = [base for base,_ in extended]

    def query_groups(y):
        begin = bisect.bisect_left(evalues,y-29)
        finish = bisect.bisect_right(evalues,y+largest_span+29)
        global_candidates = [extended[i][1] for i in range(begin,finish)]
        local_candidates = [j for j in global_candidates
                            if (records[j][0]-(y-29))%P <= spans[j]+58]
        return global_candidates, local_candidates

    def codeword(block_id, high_bits):
        base, k = records[block_id]
        return (base-sum(k[j] for j in range(4) if (high_bits>>j)&1))%P

    sha = hashlib.sha256()
    for top in itertools.product((1,2), repeat=4):
        high = sum((top[j]-1)<<j for j in range(4))
        for block_id in range(4096):
            sha.update(codeword(block_id,high).to_bytes(8,'big'))
    assert sha.hexdigest() == 'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'
    words = [(codeword(i,b),i,b) for i in range(4096) for b in range(16)]
    ordered = sorted(words)
    gaps = [ordered[j+1][0]-ordered[j][0] for j in range(65535)] + [P-ordered[-1][0]+ordered[0][0]]
    assert len({v for v,_,_ in words}) == 65536
    assert min(gaps)==59 and gaps.count(59)==64

    global_max, global_witness = overlap_bound(records,[largest_span]*4096)
    local_max, local_witness = overlap_bound(records,spans)
    assert global_max == 157 and local_max == 128
    max_observed_global = max_observed_local = 0
    total_local = 0
    checks = 0
    for exact,block_id,high in words:
        for err in (-29,0,29):
            observed = (exact+err)%P
            candidate_ids, filtered_ids = query_groups(observed)
            assert block_id in filtered_ids
            max_observed_global = max(max_observed_global,len(candidate_ids))
            max_observed_local = max(max_observed_local,len(filtered_ids))
            total_local += len(filtered_ids)
            checks += 1
    assert max_observed_global==157 and max_observed_local==128
    assert checks==196608
    explicit = 0
    for exact,block_id,high in words[::41]:
        for err in (-29,0,29):
            observed=(exact+err)%P
            _, groups=query_groups(observed)
            hits=[]
            for j in groups:
                for b in range(16):
                    v=codeword(j,b)
                    if min((v-observed)%P,(observed-v)%P)<=29:
                        hits.append((j,b))
            assert hits==[(block_id,high)]
            explicit+=1

    return {
        'schema':'EM_R284CA_GROUPED_PORT_DECODER_CERT_V1',
        'predecessor':'R284BZ_34BIT_GLOBAL_SHARP_GAP59_PORT_20261120.md',
        'prime':P, 'frozen_leaf_diagonals':[6,13],
        'free_controls':[D0,D3,Z1,Z2,Z3],
        'candidate_count':len(words), 'lower_block_count':len(LOWER),
        'top_row_variations_per_block':16,
        'positive_cofactor_extrema':[[min(k[j] for _,k in records),max(k[j] for _,k in records)] for j in range(4)],
        'span_extrema':[min(spans),max(spans)],
        'exact_circular_gap':59,'minimum_gap_multiplicity':64,
        'rowmajor_be64_sha256':sha.hexdigest(),
        'radius_used_for_global_interval_bound':'closed 29.5',
        'global_max_groups_before_span_filter':global_max,
        'global_max_groups_after_span_filter':local_max,
        'global_witness_doubled_coordinate':global_witness,
        'local_witness_doubled_coordinate':local_witness,
        'full_noisy_prefilter_checks':checks,
        'observed_max_groups_before_filter':max_observed_global,
        'observed_max_groups_after_filter':max_observed_local,
        'observed_average_groups_after_filter':total_local/checks,
        'explicit_full_decoder_checks':explicit,
        'guaranteed_max_high_row_candidates_per_observation':local_max*16,
        'materialized_sorted_index_records':4096,
        'legacy_full_lookup_records':65536,
        'claim':'certified exact lossless grouped index with uniform noise recovery rho<29.5; not a CPU speed claim',
        'review':'NOT_REVIEWED'
    }


if __name__=='__main__':
    result=verify()
    outfile=Path(__file__).with_name('R284CA_grouped_port_decoder_verification.json')
    outfile.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,sort_keys=True,indent=2))
