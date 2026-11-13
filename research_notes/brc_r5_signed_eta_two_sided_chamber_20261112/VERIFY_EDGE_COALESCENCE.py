#!/usr/bin/env python3
"""Exact rational R5 two-sided first phase coalescence at the open-chamber endpoints.
Uses only sibling full exact signed-eta verifier (losslessly gzip/base64 encoded).
No floating-point computation, no remote dependencies, 32768 labeled subsets.
"""
from fractions import Fraction as F
from pathlib import Path
import base64, gzip, contextlib, io

source = Path(__file__).with_name('VERIFY_R5_SIGNED_ETA.py.gz.b64').read_text('utf-8')
namespace = {'__name__':'__r5_signed_eta__'}
with contextlib.redirect_stdout(io.StringIO()) as prior:
    exec(compile(gzip.decompress(base64.b64decode(source)), 'VERIFY_R5_SIGNED_ETA.py', 'exec'), namespace)
r = namespace
x=r['x']; eps=r['epsmax']; kset=r['base_phases']; collision=r['collision']
assert len(kset)==1144
expected = {
 -1: (539,4108,850075412400,469532537808,380542874592,
      4096,379627579392,12,915295200),
 +1: (541,4109,852167301216,471427082208,380740219008,
      13,959619024,4096,379780599984)
}
for sign in (-1,+1):
    k,mask_total,pre_end,post_end,drop_total,mask_first,drop_first,mask_last,drop_last=expected[sign]
    eta=collision[15][3 if sign==-1 else 4]
    pivot=(x-23*eta)/15
    assert pivot==F(36)*x/k and pivot<eps
    assert r['X'][r['IX'][1,3]]+eta*r['H'][r['IX'][1,3]]>0
    limits, phases, reps, coords=r['min_thresholds'](eta)
    interior=set(phases)-{eps}
    assert len(interior)==1146
    assert len(interior-kset)==2
    assert phases[pivot]==mask_total
    counts=r['exact_counts'](limits,pivot)
    assert counts==(pre_end,post_end)
    assert counts[0]-counts[1]==drop_total
    print('EDGE',sign,'ETA',eta,'COINCIDENT_PHASE',pivot,'PHASES',len(interior),
          'PREFIX_MASKS',phases[pivot],'COUNTS_BEFORE_AFTER',*counts,'DROP',drop_total)
    # A rational point strictly in the signed open chamber near this boundary.
    inner=eta*F(999,1000)
    limits,phases,reps,coords=r['min_thresholds'](inner)
    base=F(36)*x/k
    moving=(x-23*inner)/15
    assert base!=moving
    cuts=sorted((('fixed',base),('moving',moving)),key=lambda pair:pair[1])
    assert [c[0] for c in cuts]==(['moving','fixed'] if sign==-1 else ['fixed','moving'])
    cutdata=[]
    for label,t in cuts:
        a,b=r['exact_counts'](limits,t)
        cutdata.append((label,phases[t],a,b,a-b))
        print('INNER_CUT',sign,label,'ETA',inner,'PHASE',t,
              'PREFIX_MASKS',phases[t],'COUNTS_BEFORE_AFTER',a,b,'DROP',a-b)
    assert sum(row[1] for row in cutdata)==mask_total
    assert sum(row[4] for row in cutdata)==drop_total
    assert (cutdata[0][1],cutdata[0][4],cutdata[1][1],cutdata[1][4])==(mask_first,drop_first,mask_last,drop_last)
    assert cutdata[0][2]==pre_end and cutdata[1][3]==post_end
    print('EDGE_MERGED_COUNT_IS_SUM_OF_TWO_NEIGHBOR_JUMPS',sign,True)
print('PASS_EXACT_TWO_SIDED_R5_FIRST_RESONANCE_EDGE_MERGING')
