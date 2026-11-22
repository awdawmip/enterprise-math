#!/usr/bin/env python3
"""R284EK: sharp one-fault source-tag repair; run beside frozen R284CO checker.
This is a finite exact computation of the cross-label confusability graph.
"""
import json
from collections import Counter
from pathlib import Path
from R284CO_spectral_witness_checker import P, FROZEN_SHA, arcs, words, dist

N = 1 << 16
Q = 65
E = 8656

def label(i):
    return ((i >> 12) & 1) | (((i >> 14) & 1) << 1)

def encode(v):
    a, b = v & 1, (v >> 1) & 1
    return tuple((a * int(x) + b * int(y)) % 2 for x,y in zip('11100', '10011'))

def hamming(a,b):
    return sum(x != y for x,y in zip(a,b))

def acquire(bits, faulty_read):
    q = [bits[0],bits[0],bits[1],bits[1]]
    if faulty_read < 4:
        q[faulty_read] ^= 1
    if q[0] != q[1]:
        q.append(bits[0])
    if q[2] != q[3]:
        q.append(bits[1])
    decoded = (q[0] if q[0] == q[1] else q[4],
               q[2] if q[2] == q[3] else q[4])
    return decoded, len(q)

def main():
    residue = words()  # original frozen R284CO checksum is checked here
    aa = arcs()
    assert len(residue) == N and len(aa) == 64
    f = [max(dist(x, arc) for arc in aa) for x in residue]
    order = sorted(range(N), key=lambda i: (f[i], i))
    edges = Counter()
    witnesses = {}
    min_cross = {}
    nearby_comparisons = 0
    same_class_close = 0
    for k, i in enumerate(order):
        jpos = k-1
        while jpos >= 0 and f[i] - f[order[jpos]] <= 2*E:
            j = order[jpos]
            nearby_comparisons += 1
            delta = max(abs(f[i]-f[j]), abs(f[i^Q]-f[j^Q]))
            if delta <= 2*E:
                a,b = sorted((label(i), label(j)))
                if a == b:
                    same_class_close += 1
                else:
                    edge = (a,b)
                    edges[edge] += 1
                    if edge not in min_cross or delta < min_cross[edge]:
                        min_cross[edge] = delta
                        witnesses[edge] = [min(i,j), max(i,j)]
            jpos -= 1
    assert same_class_close == 0
    assert set(edges) == {(a,b) for a in range(4) for b in range(a+1,4)}
    code = [encode(v) for v in range(4)]
    assert min(hamming(code[a],code[b]) for a in range(4) for b in range(a+1,4)) == 3
    for v in range(4):
        for flip in range(6):
            stored = list(code[v])
            if flip < 5: stored[flip] ^= 1
            assert [u for u in range(4) if hamming(stored,code[u]) <= 1] == [v]
        for wrong in range(5):
            assert acquire((v&1,(v>>1)&1),wrong)[0] == (v&1,(v>>1)&1)
    assert all(4*(n+1)>2**n for n in range(1,5))  # storage lower bound
    assert 4*5>2**4  # adaptive acquisition lower bound: 20 distinct leaves required
    cert = {
      'schema':'R284EK_ONE_FAULT_SOURCE_TAG_CERTIFICATE_V1',
      'frozen_source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
      'frozen_source_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
      'frozen_residue_sha256':FROZEN_SHA,
      'state_count':N, 'arc_count':len(aa), 'port_offsets':[0,Q],
      'numeric_error_radius_per_port':E,
      'confusability_threshold':2*E,
      'candidate_pair_comparisons':nearby_comparisons,
      'same_label_confusable_pairs':same_class_close,
      'cross_label_confusability_graph':'K4',
      'cross_label_edges':[{'classes':list(edge), 'confusable_pair_count':edges[edge],
                            'min_linf_distance':min_cross[edge], 'witness':witnesses[edge]}
                           for edge in sorted(edges)],
      'encoder_generators':['11100','10011'],
      'codewords':[''.join(map(str,w)) for w in code],
      'minimum_codeword_hamming_distance':3,
      'tag_storage_bits_sharp':5,
      'single_storage_fault_test_cases':24,
      'source_bit_acquisition_queries_worst_case_sharp':5,
      'source_bit_acquisition_no_fault_queries':4,
      'acquisition_test_cases':20,
      'arithmetic':'unbounded exact integers',
      'status':'AUTHOR_EXACT_CHECKED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED'
    }
    dest=Path(__file__).with_name('R284EK_one_fault_tag_certificate.json')
    dest.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','edges':cert['cross_label_edges'],
                      'checks':{'candidate_pairs':nearby_comparisons,
                                'source_acquisition':20,'storage_flips':24}},ensure_ascii=False))

if __name__ == '__main__':
    main()
