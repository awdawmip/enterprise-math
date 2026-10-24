#!/usr/bin/env python3
"""C286 exact full-path monotonicity for all 125 C284 rational paths.

Inputs in the same directory:
  C275_STANDALONE_EXACT_REPLAY.py
  C284_187_EXACT_DYADIC_BRACKETS.json
  C285_EXACT_UNIFORM_DERIVATIVE.py
Uses exact Fraction comparisons only. Author evidence, not Source admission.
"""
from fractions import Fraction as R
from collections import Counter
import hashlib, json
import C275_STANDALONE_EXACT_REPLAY as src
from C285_EXACT_UNIFORM_DERIVATIVE import derivative_lower

SOURCE_SHA = 'fcdad45cb2ed5df659b1a153762d358e2b7fa4df3e14c1be3eb505d4209ef576'
DENOMINATOR = 2**18
LATE = [R(1,2), R(3,4), R(7,8), R(15,16),
        R(31,32), R(63,64), R(127,128), R(1)]

def verify():
    c284 = json.load(open('C284_187_EXACT_DYADIC_BRACKETS.json', encoding='utf8'))
    records = c284['records']
    raw = json.dumps(records, ensure_ascii=False, separators=(',', ':')).encode()
    assert c284['certificate_sha256'] == SOURCE_SHA
    assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA
    assert len(records) == 187
    hulls = src.hulls()
    paths = {}
    for i,j,witness,k in records:
        lo,hi,kind = hulls[(i,j)]
        w = src.WITNESSES[witness-1]
        h = src.high_point(lo,hi)
        assert kind != 'safe' and src.valid(w) and src.valid(h)
        assert src.inside(w,lo,hi) and src.inside(h,lo,hi)
        assert 0 <= k < 4096
        paths[(witness,h)] = (w,h)
    assert len(paths) == 125
    weights,_ = src.floor_fixed_masses()
    widths = Counter()
    leaves = 0
    for (wid,h),(w,_) in sorted(paths.items()):
        intervals = []
        def certify(a,b,depth):
            try:
                L = derivative_lower(w,h,a,b,weights)
            except AssertionError:
                L = None
            if L is not None and L > 0:
                assert DENOMINATOR*L > src.Q,(wid,h,a,b)
                intervals.append((a,b))
                return
            assert depth < 30,('uncertified',wid,h,a,b)
            m = (a+b)/2
            certify(a,m,depth+1)
            certify(m,b,depth+1)
        certify(R(0), R(1,2), 1)
        for a,b in zip(LATE,LATE[1:]):
            L = derivative_lower(w,h,a,b,weights)
            assert DENOMINATOR*L > src.Q,(wid,h,a,b)
            intervals.append((a,b))
        assert intervals[0][0] == 0 and intervals[-1][1] == 1
        assert all(x[1] == y[0] for x,y in zip(intervals,intervals[1:]))
        widths[len(intervals)] += 1
        leaves += len(intervals)
    assert dict(widths) == {8:55,9:68,10:1,11:1},widths
    assert leaves == 1073
    assert len({(r[0],r[1]) for r in records}) == 187
    print('C286_FULL_PATH_EXACT_PASS 125_paths 187_labels 1073_leaves '
          'max_denominator_128 Fprime_gt_Q_over_262144',dict(sorted(widths.items())))

if __name__ == '__main__':
    verify()
