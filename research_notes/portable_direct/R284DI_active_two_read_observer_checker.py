#!/usr/bin/env python3
"""R284DI: exact two-read active observability on the frozen R284CO Port domain.
Dependency: sibling R284CO_spectral_witness_checker.py at the frozen source pin.
"""
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from R284CO_spectral_witness_checker import words, arcs, dist, P, D, Z, FROZEN_SHA

def u64_sha(values):
    h = hashlib.sha256()
    for value in values:
        h.update(value.to_bytes(8, 'big'))
    return h.hexdigest()

def state(index):
    ui, li = divmod(index, 4096)
    top = sum(((ui >> (3-j)) & 1) << j for j in range(4))
    lower = tuple(1 + ((li >> (11-j)) & 1) for j in range(12))
    return top, lower

def r_derivative(top, lower):
    u1, a, x, y, u2, w, b, z, u3, g, h, r = lower
    t, s = 6-a, 13-b
    u = t*s-x*w
    p1, p2 = s*u1+x*u2, t*u2+w*u1
    return ((1-D[0]+(top&1))*u
            +(Z[1]+1+((top>>1)&1))*p1
            +(Z[2]+1+((top>>2)&1))*p2)

def check():
    X, A = words(), arcs()
    assert len(X) == 65536 and len(A) == 64
    obs = []
    labels = []
    for x in X:
        readings = [dist(x, arc) for arc in A]
        v = max(readings)
        assert readings.count(v) == 1
        obs.append(v)
        labels.append(readings.index(v))
    fibers = defaultdict(list)
    for i, v in enumerate(obs):
        fibers[v].append(i)
    pairs = sorted((i, j) for ids in fibers.values()
                   for i, j in itertools.combinations(ids, 2))
    assert len(fibers) == 65139 and len(pairs) == 420
    assert Counter(map(len, fibers.values())) == {1:64760, 2:366, 3:8, 4:5}
    separations = [sum(obs[i^(1<<bit)] != obs[j^(1<<bit)]
                       for i,j in pairs) for bit in range(16)]
    joint_sizes = [len({(obs[i], obs[i^(1<<bit)]) for i in range(65536)})
                   for bit in range(16)]
    assert separations == [420,192,416,416,348,133,420,384,252,148,394,417,
                           196,184,396,412]
    assert joint_sizes == [65536,65308,65532,65532,65464,65257,65536,65500,
                           65368,65279,65510,65533,65312,65300,65512,65528]
    assert [bit for bit, n in enumerate(joint_sizes) if n == 65536] == [0,6]
    for i in range(65536):
        top, lower = state(i)
        shift = (3-2*lower[-1])*r_derivative(top, lower)
        assert (X[i]+shift)%P == X[i^1]
    gap_witnesses = {}
    for bit in (0,6):
        gap, (i,j) = min((abs(obs[i^(1<<bit)]-obs[j^(1<<bit)]), (i,j))
                          for i,j in pairs)
        gap_witnesses[str(bit)] = {
            'gap':gap, 'indices':[i,j], 'original_D':obs[i],
            'flipped_D':[obs[i^(1<<bit)],obs[j^(1<<bit)]]}
    assert gap_witnesses['0']['gap'] == 312638
    assert gap_witnesses['6']['gap'] == 23060
    return {
      'schema':'R284DI_ACTIVE_TWO_READ_OBSERVER_V1',
      'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'source':'R284CO_spectral_witness_checker.py @ acba2d8667903434aaa2a10720f43637fcc2421b',
      'source_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
      'frozen_sha256':FROZEN_SHA,
      'model':{'n_states':65536,'n_arcs':64,'single_observation_distinct':len(fibers),
               'equal_D_unordered_pairs':len(pairs),
               'fiber_size_histogram':dict(sorted(Counter(map(len,fibers.values())).items()))},
      'source_bits':'indices in product((1,2),repeat=4) x product((1,2),repeat=12) enumeration; bit0 toggles lower r; bit6 toggles lower w',
      'bit_flip_separated_equal_D_pairs':separations,
      'bit_flip_joint_observation_unique_sizes':joint_sizes,
      'complete_two_read_bits':[0,6],
      'minimum_conditional_second_read_gaps':gap_witnesses,
      'original_D_u64_be_sha256':u64_sha(obs),
      'r_two_read_pairs_u64_be_sha256':u64_sha(v for i in range(65536)
                                                    for v in (obs[i], obs[i^1])),
      'w_two_read_pairs_u64_be_sha256':u64_sha(v for i in range(65536)
                                                    for v in (obs[i], obs[i^64])),
      'r_derivative_exact_states':65536,
      'verification':'exact Python integers; exhaustive 65536 source states, 64 arcs, 420 collision pairs, 16 coordinate flips; separate author-controlled check; independent review NOT_REVIEWED'
    }

if __name__=='__main__':
    result = check()
    with open('R284DI_active_two_read_observer_certificate.json','w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
        f.write('\n')
    print(json.dumps({'complete_two_read_bits':result['complete_two_read_bits'],
                      'gap_witnesses':result['minimum_conditional_second_read_gaps']}))
