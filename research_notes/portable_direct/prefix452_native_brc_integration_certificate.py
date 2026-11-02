#!/usr/bin/env python3
"""PREFIX-452 pinned BRC source-class execution and exact source-state benchmarks.

Run: PYTHONPATH=/mnt/data/PREFIX452_work:/mnt/data/prefix452_work/prefix450
  python /mnt/data/PREFIX452_work/prefix452_native_brc_integration_certificate.py
No external dependencies. Pinned upstream modules are byte-identical; the
unused rational_prime_valuations import has a test-only helper adapter.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib, json, time
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState, eye, point_moment, ma, sm
from enterprise_math.brc_control_port import ControlPacket
from prefix450_arbitrary_degree_x6_certificate import construct, graded_indices, read_word

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
FROZEN_BLOBS = {
    'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
    'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
    'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
}
Q=3
D=2
N=Q+D-1
ZERO=(0,)*6

def git_blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def mass_moments(bins):
    out={}
    for (r,x),mass in bins.items():
        m=sm(mass,point_moment(x))
        out[r]=ma(out[r],m) if r in out else m
    return {r:MomentState.from_matrix(a) for r,a in out.items()}

def encfrac(z):
    z=Fraction(z)
    return [z.numerator,z.denominator]

def serialize_full(bins):
    entries=[[r,list(x),*encfrac(w)] for (r,x),w in sorted(bins.items())]
    return json.dumps({'bins':entries},sort_keys=True,separators=(',',':')).encode()

def serialize_mom(mom):
    entries=[[r,[encfrac(v) for v in mom[r].upper]] for r in sorted(mom)]
    return json.dumps({'sector_moments':entries},sort_keys=True,separators=(',',':')).encode()

def max_bits(mom):
    return max(max(v.numerator.bit_length(),v.denominator.bit_length()) for state in mom.values() for v in state.upper)

def path_family():
    return [(r,read_word(construct(Q,D,r,a),Q)[1]) for r in range(Q) for a in graded_indices(D)]

def dense_words():
    bins={(0,ZERO):1}
    for _ in range(N):
        nxt=defaultdict(int)
        for (r,x),c in bins.items():
            for axis,sgn in product(range(6),(-1,1)):
                y=list(x);y[axis]+=sgn
                rr=(r+(axis==0 and sgn==-1))%Q
                nxt[(rr,tuple(y))]+=c
        bins=dict(nxt)
    return bins

def main():
    start=time.perf_counter()
    home=Path(__file__).resolve()
    repo_native=home.parents[2]/'src'/'enterprise_math'
    root=repo_native if repo_native.is_dir() else home.parent/'enterprise_math'
    for name,blob in FROZEN_BLOBS.items():
        actual=git_blob((root/name).read_bytes())
        assert actual==blob, (name,actual,blob)
        print('PINNED_MODULE',name,'git_blob',actual,'PASS')
    family=path_family()
    assert len(family)==84 and len(set(family))==84
    for r,x in family:
        assert len(x)==6
    assert all(read_word(construct(Q,D,r,a),Q)[0]==r for r in range(Q) for a in graded_indices(D))
    identity=eye(6)
    edges=[(r,r,Fraction(1),Affine(identity,tuple(map(Fraction,x))),1) for r,x in family]
    first=ControlPacket.from_edges(Q,0,N,edges)
    first_a=ControlPacket.from_edges(Q,0,N,edges[::2])
    first_b=ControlPacket.from_edges(Q,0,N,edges[1::2])
    assert first_a.alternatives(first_b).blocks==first.blocks
    anchor={r:MomentState.from_point(ZERO) for r in range(Q)}
    observed=first.moment_action(anchor)
    sparse_bins={(r,x):Fraction(1) for r,x in family}
    assert observed==mass_moments(sparse_bins)
    for r in range(Q):
        direct=first.evaluate(r,ZERO)
        assert len(direct)==28
        assert all(target==r and h.total_mass==1 for (target,_),h in direct.items())
    print('NATIVE_Q3_N4_84_PATHS','ControlPacket+EffectHistogram+MomentState','PASS')
    shear=[list(row) for row in identity]
    shear[0][1]+=Fraction(1)
    shear=tuple(tuple(row) for row in shear)
    future_edges=[]
    for r in range(Q):
        shift=[Fraction(0)]*6
        shift[2]=Fraction(r+1)
        future_edges.append((r,r,Fraction(r+2,r+3),Affine(shear,tuple(shift)),1))
        shift=[Fraction(0)]*6
        shift[0]=Fraction(-1)
        future_edges.append((r,(r+1)%Q,Fraction(r+3,r+4),Affine(identity,tuple(shift)),1))
    future=ControlPacket.from_edges(Q,N,1,future_edges)
    composed=first.then(future)
    from_both=composed.moment_action(anchor)
    sequential=future.moment_action(observed)
    assert from_both==sequential
    manual_bins=defaultdict(Fraction)
    for r,x in family:
        for s,t,w,act,c in future_edges:
            if s==r:manual_bins[(t,act.apply(x))]+=w*c
    assert from_both==mass_moments(manual_bins)
    for r in range(Q):
        empirical=composed.evaluate(r,ZERO)
        actual=defaultdict(Fraction)
        for (target,x),hist in empirical.items():actual[(target,x)]+=hist.total_mass
        expect=defaultdict(Fraction)
        for rr,x in family:
            if rr!=r:continue
            for s,t,w,act,c in future_edges:
                if s==r:expect[(t,act.apply(x))]+=w*c
        assert dict(actual)==dict(expect)
    print('NATIVE_AFFINE_SERIAL_AND_CONDITIONAL_BRANCH','168 weighted paths','shear+translation','PASS')
    # Reconstruct known earliest history-sensitive collision at N=2.
    # Two 2-step signed words with endpoint ZERO, but sectors 0,1 respectively.
    assert read_word(((1,1),(1,-1)),Q)==(0,ZERO)
    assert read_word(((0,1),(0,-1)),Q)==(1,ZERO)
    mass_a={0:MomentState.from_point(ZERO)}
    mass_b={1:MomentState.from_point(ZERO)}
    different=ControlPacket.from_edges(Q,2,1,[(0,0,Fraction(2),Affine.identity(6),1),
                                             (1,1,Fraction(3),Affine.identity(6),1)])
    out_a=different.moment_action(mass_a)
    out_b=different.moment_action(mass_b)
    assert sum(s.upper[-1] for s in out_a.values())==2
    assert sum(s.upper[-1] for s in out_b.values())==3
    print('NATIVE_TWO_WORD_HISTORY_RESIDUAL','same endpoint','future masses 2 vs 3','PASS')
    dense=dense_words()
    assert len(dense)==1059 and sum(dense.values())==12**N==20736
    dense_mom=mass_moments(dense)
    sparse_mom=mass_moments(sparse_bins)
    assert dense_mom.keys()==sparse_mom.keys()==set(range(Q))
    dense_hist_bytes=len(serialize_full(dense));dense_mom_bytes=len(serialize_mom(dense_mom))
    sparse_hist_bytes=len(serialize_full(sparse_bins));sparse_mom_bytes=len(serialize_mom(sparse_mom))
    print('DENSE_SUPPORT',len(dense),'ordered_paths',sum(dense.values()),'moments',sum(len(t.upper) for t in dense_mom.values()))
    print('DENSE_COMPACT_JSON_BYTES','full',dense_hist_bytes,'moment',dense_mom_bytes,'ratio',round(dense_hist_bytes/dense_mom_bytes,3))
    print('SPARSE_SUPPORT',len(sparse_bins),'ordered_paths',len(family),'moments',sum(len(t.upper) for t in sparse_mom.values()))
    print('SPARSE_COMPACT_JSON_BYTES','full',sparse_hist_bytes,'moment',sparse_mom_bytes,'ratio',round(sparse_hist_bytes/sparse_mom_bytes,3))
    one_bin={(family[0][0],family[0][1]):Fraction(1)}
    single_hist_bytes=len(serialize_full(one_bin));single_mom_bytes=len(serialize_mom(mass_moments(one_bin)))
    print('SINGLE_SOURCE_COMPACT_JSON_BYTES','full',single_hist_bytes,'moment',single_mom_bytes,'ratio',round(single_hist_bytes/single_mom_bytes,3))
    print('FRACTION_MAX_BIT_LENGTH','dense',max_bits(dense_mom),'sparse',max_bits(sparse_mom))
    assert from_both and dense_hist_bytes>dense_mom_bytes
    print('SUCCESS', 'scientific_pin',PIN,'elapsed_seconds',round(time.perf_counter()-start,3))

if __name__=='__main__': main()
