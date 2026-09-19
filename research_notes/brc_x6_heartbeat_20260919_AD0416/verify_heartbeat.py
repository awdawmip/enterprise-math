"""Exact X6 radix-heartbeat specialization; no production or physical-law claim.
Run: PYTHONPATH=<enterprise-math>/src python verify_heartbeat.py
The standalone bundle carries the previously verified source modules under vendor/.
"""
from __future__ import annotations
import hashlib
import itertools
import json
from pathlib import Path
import random
import sys
from fractions import Fraction as F

HERE = Path(__file__).resolve().parent
if (HERE / 'vendor').is_dir():
    sys.path.insert(0, str(HERE / 'vendor'))
from enterprise_math import brc_transport as bt
from enterprise_math import predictive_quotient as pq

D = 6

def point(x):
    x = tuple(x)
    if len(x) != D or any(type(v) is not int for v in x):
        raise TypeError('six exact integer raw displacement coordinates required')
    return x

def radix(b):
    if type(b) is not int or b < 2:
        raise ValueError('integer radix >= 2 required')
    return b

def expand(x, b=2, residue=0):
    x = point(x); b = radix(b)
    if type(residue) is not int or not 0 <= residue < b:
        raise ValueError('residue out of range')
    return (b*x[-1]+residue,) + x[:-1]

def contract(x, b=2):
    x = point(x); b = radix(b)
    q, r = bt.euclidean_digits(x[0], (b,))
    return x[1:] + (q,), r[0]

def analyze(x, beats, b=2):
    if type(beats) is not int or beats < 0:
        raise ValueError('nonnegative exact beat count required')
    digits = []
    for _ in range(beats):
        x, r = contract(x, b); digits.append(r)
    return x, tuple(digits)

def synthesize(q, digits, b=2):
    for r in reversed(digits):
        q = expand(q, b, r)
    return q

def A(b=2):
    b = radix(b)
    rows = [[0]*D for _ in range(D)]
    rows[0][-1] = b
    for i in range(1, D): rows[i][i-1] = 1
    return bt.matrix(rows)

def measure_moment(mu):
    out = bt.sm(0, bt.eye(D+1))
    for x, w in mu.items():
        out = bt.ma(out, bt.sm(w, bt.point_moment(x)))
    return out

def push_contract(mu, b=2):
    out = {}
    for x, w in mu.items():
        q, _ = contract(x,b); out[q] = out.get(q,F(0))+w
    return out

def conditional_moment_contract(mu, b=2):
    inverse = bt.inv(A(b))
    out = bt.sm(0, bt.eye(D+1))
    for r in range(b):
        fiber = {x:w for x,w in mu.items() if x[0] % b == r}
        off = tuple(-v for v in bt.mv(inverse, (F(r),)+(F(0),)*5))
        packet = bt.EffectHistogram.from_terms(D, [(1, bt.Affine(inverse,off), 1)])
        out = bt.ma(out, packet.moment_action(measure_moment(fiber)))
    return out

def run():
    results = {}
    expected = {'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
                'predictive_quotient.py':'f27d9ddf908f5b07051acfaf0c69f359d499b98b',
                'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1'}
    source_dir = Path(bt.__file__).resolve().parent
    for name,sha in expected.items():
        data=(source_dir/name).read_bytes()
        actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert actual==sha, (name,actual,sha)
    results['source_blobs'] = expected
    for b in (2,3,5,7):
        assert bt.mpow(A(b),6)==bt.sm(b,bt.eye(D))
        for k in range(1,6):
            gram=bt.mm(bt.transpose(bt.mpow(A(b),k)),bt.mpow(A(b),k))
            assert sorted(gram[i][i] for i in range(D)) == [F(1)]*(D-k)+[F(b*b)]*k
    results['six_beat_closure']={'radices':[2,3,5,7],'A_power_6':'b I','intermediate_component_condition_number':'b'}
    count=0
    for x in itertools.product(range(-2,3),repeat=D):
        q,digits=analyze(x,6)
        assert q==tuple(v//2 for v in x)
        assert digits==tuple(v%2 for v in x)
        assert synthesize(q,digits)==x
        count+=1
    rng=random.Random(20260919)
    for _ in range(1000):
        x=tuple(rng.randrange(-10**12,10**12) for _ in range(D))
        b=rng.choice((2,3,5,7)); beats=rng.randrange(1,31)
        q,digits=analyze(x,beats,b)
        assert synthesize(q,digits,b)==x
    results['exact_roundtrips']={'exhaustive_sixbeat_vectors':count,'random_signed_multiscale_vectors':1000}
    points=set()
    for ds in itertools.product(range(2),repeat=6):
        points.add(synthesize((0,)*D,ds))
    assert points==set(itertools.product(range(2),repeat=6))
    results['fiber_capacity']={'sixbeat_residues':len(points),'onebeat_residues':2,'depth_k_cycles':'2^(6k) possibilities; 6k worst-case bits'}
    packet=bt.EffectHistogram.from_terms(D,[(F(1,2),bt.Affine(A(),(F(r),)+(F(0),)*5),1) for r in (0,1)])
    full=bt.EffectHistogram.unit(D)
    for _ in range(6): full=full.then(packet)
    output=full.evaluate((0,)*D)
    assert set(output)==points
    assert all(h.count==1 and h.total_mass==F(1,64) for h in output.values())
    assert full.forget_effects().count==64 and full.forget_effects().total_mass==1
    compressed=bt.MomentState.from_point((0,)*D)
    for _ in range(6): compressed=compressed.then(packet)
    assert compressed.to_matrix()==bt.explicit_moment(output)
    results['BRC_refinement']={'paths':64,'distinct_fine_positions':64,'each_mass':'1/64','total_mass':'1','moment_match':True}
    e=(0,0,0,0,0,1)
    outward=[e]
    for _ in range(6): outward.append(expand(outward[-1]))
    positions=tuple(outward[min(j,12-j)] for j in range(12))
    states=tuple(range(12)); actions={'tick':lambda j:(j+1)%12}
    profile=pq.predictive_block_profile(states,actions,lambda j:positions[j],3)
    assert profile==(7,12,12,12)
    assert positions[1]==positions[11] and positions[2]!=positions[0]
    results['phase_observer']={'raw_cycle_phases':12,'position_only_classes':7,'predictive_profile':profile,'same_position':'2e1','next_outward':'2e2','next_inward':'e6'}
    mu={(-1,0,0,0,0,0):F(1,2),(1,0,0,0,0,0):F(1,2)}
    nu={(-2,0,0,0,0,0):F(1,8),(0,0,0,0,0,0):F(3,4),(2,0,0,0,0,0):F(1,8)}
    assert measure_moment(mu)==measure_moment(nu)
    cm=measure_moment(push_contract(mu)); cn=measure_moment(push_contract(nu))
    assert cm!=cn and cm[5][6]==F(-1,2) and cn[5][6]==0
    assert conditional_moment_contract(mu)==cm and conditional_moment_contract(nu)==cn
    for _ in range(100):
        sample={tuple(rng.randrange(-9,10) for _ in range(D)):F(rng.randrange(1,10),11) for _ in range(12)}
        assert conditional_moment_contract(sample)==measure_moment(push_contract(sample))
    results['residue_conditioned_moments']={'pre_moments_equal':True,'post_last_means':['-1/2','0'],'post_last_second_moments':[str(cm[5][5]),str(cn[5][5])],'random_fiber_repairs':100,'onebeat_stored_moment_entries':56,'universal_constant_state_claim':False}
    x=(17,-3,0,4,5,6); q,digits=analyze(x,6)
    assert q==(8,-2,0,2,2,3) and digits==(1,1,0,0,1,0)
    assert synthesize(q,digits)==x
    moved_q=(q[0]+1,)+q[1:]
    moved=synthesize(moved_q,digits)
    assert moved==(19,-3,0,4,5,6)
    results['pulse_interaction']={'input':x,'coarse':q,'residues':digits,'no_interaction_output':x,'coarse_plus_e1_output':moved}
    # Relative coordinates around a selected anchor are used throughout, not final Cell addresses.
    p=(1,0,0,0,0,0); zero=(0,)*D
    assert analyze(p,6)[0]==analyze(zero,6)[0]
    assert analyze(p,6)[1]!=analyze(zero,6)[1]
    results['no_free_information_loss']={'distinct_points_same_coarse':True,'residue_restores_identity':True,'phase_not_residue':True}
    failures=0
    for thunk in (lambda:point((0,)*5),lambda:point((True,0,0,0,0,0)),lambda:expand(zero,1),lambda:expand(zero,2,2),lambda:analyze(zero,-1)):
        try: thunk()
        except (TypeError,ValueError): failures+=1
    assert failures==5
    results['invalid_inputs_rejected']=failures
    return {'schema':'EM_X6_RADIX_HEARTBEAT_PROBE_V1','status':'PASS','check_groups':10,'results':results,
            'limits':['research construction, not production integration','integer chart index scaling, not calibrated physical time or arbitrary native rotation','no semantic-memory efficacy claim','moment closure only for declared affine/refinement or explicitly residue-conditioned steps','no independent review or Lean formalization','timing phase cannot replace spatial residues','per-label arithmetic not global constant-cost field update']}

if __name__=='__main__':
    output=run()
    (HERE/'RESULTS.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(output,ensure_ascii=False,indent=2))
