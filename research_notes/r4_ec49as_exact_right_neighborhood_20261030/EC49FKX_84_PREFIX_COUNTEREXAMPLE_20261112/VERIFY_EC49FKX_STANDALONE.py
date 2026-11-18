#!/usr/bin/env python3
"""Self-contained direct check of a 24-word BRC/X6 witness. No generator/solver imports."""
import json, pathlib, sys
OPS = 'acdefg'
TRANS = (
    (1,2,3,1,4,5), (1,6,7,1,1,1), (2,2,8,2,2,2),
    (3,8,3,3,3,3), (4,2,7,4,4,4), (5,6,3,5,5,5),
    (6,6,8,6,6,6), (7,8,7,7,7,7), (8,8,8,8,8,8)
)
SIG = (0,0,4,1,16,32,8,2,0)
STEPS = {'a':(-1,-1), 'c':(1,2,-1,-2), 'd':(2,1,-2,-1), 'e':(3,1,1,-3), 'f':(1,-1), 'g':(2,-2)}
REQ = {2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
PIN = 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def verify(path):
    doc = json.loads(pathlib.Path(path).read_text())
    assert doc['frozen_scientific_pin'] == PIN
    expected = {(h,s) for h, values in REQ.items() for s in values}
    assert len(expected) == 24
    assert len(doc['demands']) == 24
    prefixes = set(); keys=set(); coverage=set(); microsteps_total=0; opsteps_total=0
    for record in doc['demands']:
        h, signature, word = record['window'], record['signature'], record['word']
        assert len(word) == h and (h,signature) in expected
        assert (h,signature) not in coverage, f'duplicate {(h,signature)}'
        coverage.add((h,signature))
        q=0; pos=[0]*6; seq=[]
        for op in word:
            assert op in OPS
            q = TRANS[q][OPS.index(op)]
            assert q != 8, f'invalid transition {word}'
            opsteps_total += 1
            for ax in STEPS[op]:
                pos[abs(ax)-1] += 1 if ax>0 else -1
                seq.append(ax)
        assert SIG[q] == signature and pos == [2,0,0,0,0,0], (record,q,pos)
        key=tuple(seq.count(axis) for axis in (1,2,3))
        assert tuple(record['raw_key']) == key
        keys.add(key)
        microsteps_total += len(seq)
        for j in range(1,len(seq)+1):
            prefixes.add(tuple(seq[:j])) # signed and ordered full six-axis history
    assert coverage==expected
    assert len(keys)==7,keys
    assert keys==set(map(tuple,doc['keys']))
    assert len(prefixes)==84, len(prefixes)
    assert doc['native_ordered_signed_prefix_count']==len(prefixes)
    assert doc['demand_count']==len(coverage)
    assert len({tuple(p) for p in prefixes}) == 84
    print('EC49FKX_STANDALONE_EXPLICIT_BRC_WITNESS_PASS',
          'demands',len(coverage),'keys',len(keys),'ordered_signed_native_prefixes',len(prefixes),
          'source_op_steps',opsteps_total,'expanded_microsteps',microsteps_total)
    print('KEYS', sorted(keys))

if __name__=='__main__':
    verify(sys.argv[1] if len(sys.argv)>1 else pathlib.Path(__file__).with_name('EC49FKX_EXPLICIT_84_WITNESS.json'))
