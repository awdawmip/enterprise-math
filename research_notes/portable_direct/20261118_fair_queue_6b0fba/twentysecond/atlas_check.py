"""Local mathematical prototype. The project's registered runtime is imported read-only."""
import argparse
import hashlib
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import sys

PINS={
 'src/enterprise_math/_cell_slice_codec.py':'9eb64264a59e23402c51d8aa20ff9a21ff37dec5f8bd80a97da2f54bbb48a70b',
 'src/enterprise_math/cell_address.py':'b0ec81867994146ad69e81f73c74cfe58071c361150a84749be7a852536f1329',
 'EnterpriseMath/CellAddress/ThreeRegionSlice.lean':'2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02',
 'src/enterprise_math/brc_weighted_recurrent.py':'7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26',
 'coordinate_address_contract.json':'7e276582c73705e0659206fd7dab7c4b590d09ff2da8ce5c88173e04ae6d873a'}
ZERO=(0,)*6
# Each entry is (anchor in the fixed reference, named signed axes of local columns).
FRAMES={'X6-AUDIT-F0':(ZERO,(1,2,3,4,5,6)),
        'X6-AUDIT-F1':((2,-1,0,1,0,-1),(-3,1,5,2,-6,4)),
        'X6-AUDIT-F2':((-1,0,1,0,-2,0),(6,-1,2,3,4,5))}
ROOT='X6-AUDIT-F0'
CANDIDATE='candidate_x6_common_minimum'


def local_to_base(z,frame):
    anchor,axes=FRAMES[frame]
    out=list(anchor)
    for v,axis in zip(z,axes):out[abs(axis)-1]+=(1 if axis>0 else -1)*v
    return tuple(out)


def base_to_local(z,frame):
    anchor,axes=FRAMES[frame]
    return tuple((1 if d>0 else -1)*(z[abs(d)-1]-anchor[abs(d)-1]) for d in axes)


def zz(x):
    return 2*x if x>=0 else -2*x-1


def inv(z):
    return z//2 if z%2==0 else -(z+1)//2


def scalar_step(k,sgn):
    if sgn==1:return k+2 if k%2==0 else (0 if k==1 else k-2)
    return k+2 if k%2 else (1 if k==0 else k-2)


def plus(z,i,sign):
    y=list(z);y[i]+=sign;return tuple(y)


def sup(x,y):
    return max(abs(a-b) for a,b in zip(x,y))


def atlas(slice_api,old):
    def encode(z):
        if type(z) is not tuple or len(z)!=6 or any(type(t) is not int for t in z):raise ValueError('raw chart')
        p=slice_api.encode(z[:2])[:3];t=zz(z[2])
        return tuple(c+t for c in p)+tuple(zz(c) for c in z[3:])

    def read(q):
        if type(q) is not tuple or len(q)!=6 or any(type(t) is not int or t<0 for t in q):raise ValueError('natural fields')
        t=min(q[:3])
        if q[:3].count(t)!=1:raise ValueError('minimum tie')
        p=tuple(c-t for c in q[:3])+(0,0,0)
        return t,p

    def decode(q):
        t,p=read(q)
        return (*slice_api.decode(p),inv(t),*(inv(c) for c in q[3:]))

    def step(q,i,d):
        t,p=read(q)
        if type(i) is not int or type(d) is not int or i not in range(6) or d not in (-1,1):raise ValueError('direction')
        if i<2:
            p=slice_api.code_step(p,'E'+str(i+1)+('+' if d==1 else '-'))
            return tuple(c+t for c in p[:3])+q[3:]
        if i==2:
            t=scalar_step(t,d)
            return tuple(c+t for c in p[:3])+q[3:]
        return q[:i]+(scalar_step(q[i],d),)+q[i+1:]

    def canonical_wire(z):
        q=encode(z)
        if not any(z[2:]):
            return old.encode_raw_slice(z[:2]).to_wire()
        return {'schema':old.SCHEMA,'codec':CANDIDATE,'version':1,'frame':ROOT,'coordinates':list(q)}

    def wire_decode(w):
        if type(w) is not dict or set(w)!={'schema','codec','version','frame','coordinates'}:
            raise ValueError('malformed header')
        if w['codec']==old.CODEC:
            obj=old.FinalCellAddress.from_wire(w)
            return (*old.decode_raw_slice(obj),0,0,0,0)
        if (w['schema']!=old.SCHEMA
              or type(w['version']) is not int or w['version']!=1 or w['codec']!=CANDIDATE
              or w['frame']!=ROOT or type(w['coordinates']) is not list):raise ValueError('unlisted header')
        z=decode(tuple(w['coordinates']))
        if not any(z[2:]):raise ValueError('legacy slice uses its original complete header')
        return z
    return encode,decode,step,canonical_wire,wire_decode


def graph_check(core,api):
    E,D,step,wire,unwire=api
    states=[(x,0,y,0,0,0) for x in (-1,0,1) for y in (-1,0,1)]
    new=sorted(states,key=lambda z:json.dumps(wire(z),sort_keys=True))
    atoms=[]
    for z in states:
        for i in (0,2):
            for d in (-1,1):
                dest=plus(z,i,d)
                if dest in states:
                    for name,weight in [('p',F(1,3)),('q',F(2,5))]:
                        atoms.append((z,i,d,name,weight,dest))
    def run(order,transport):
        mat=[[F(0) for _ in order] for _ in order];ledger=[]
        for z,i,sgn,port,w,t in atoms:
            if transport:
                start=unwire(wire(z));stop=D(step(E(start),i,sgn))
                assert unwire(wire(stop))==t
            else:start,stop=z,t
            ledger.append((start,i,sgn,port,w,stop));mat[order.index(start)][order.index(stop)]+=w
        return [core(mat,n) for n in (1,2,3)],ledger
    before,b0=run(states,False);after,b1=run(new,True)
    assert b0==b1
    for u,v in zip(before,after):
        assert all(u[i][j]==v[new.index(s)][new.index(t)] for i,s in enumerate(states) for j,t in enumerate(states))
    return {'states':len(states),'ordered_labelled_parallel_atoms':len(atoms),'lengths':[1,2,3],
            'frozen_core_calls':6,'start_central_return_length_two':str(before[1][4][4]),
            'typed_atom_ledger_sha256':hashlib.sha256(repr(b1).encode()).hexdigest()}


def run(repo):
    for path,sha in PINS.items():assert hashlib.sha256((repo/path).read_bytes()).hexdigest()==sha
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import _cell_slice_codec as slice_api,cell_address as old
    from enterprise_math.brc_weighted_recurrent import recurrent_mass_power
    api=atlas(slice_api,old);E,D,step,wire,unwire=api
    counts={'wire_roundtrips':0,'frame_pair_checks':0,'frame_triple_checks':0,'frame_direction_checks':0,'legacy_headers':0}
    for point in product((-1,0,1),repeat=6):
        assert D(E(point))==point and unwire(wire(point))==point
        counts['wire_roundtrips']+=1
        if not any(point[2:]):
            assert wire(point)==old.encode_raw_slice(point[:2]).to_wire()
            counts['legacy_headers']+=1
        charts={f:E(base_to_local(point,f)) for f in FRAMES}
        for f,oldq in charts.items():
            for g,current in charts.items():
                world=local_to_base(D(oldq),f)
                assert E(base_to_local(world,g))==current
                counts['frame_pair_checks']+=1
                for h in FRAMES:
                    assert E(base_to_local(local_to_base(D(current),g),h))==E(base_to_local(world,h))
                    counts['frame_triple_checks']+=1
            for i,signed_axis in enumerate(FRAMES[f][1]):
                for d in (-1,1):
                    nq=step(oldq,i,d)
                    assert local_to_base(D(nq),f)==plus(point,abs(signed_axis)-1,(1 if signed_axis>0 else -1)*d)
                    assert step(nq,i,-d)==oldq and sup(nq,oldq)<=2
                    counts['frame_direction_checks']+=1
    legal=illegal=0
    for q in product(range(5),repeat=6):
        try:z=D(q)
        except ValueError:
            assert q[:3].count(min(q[:3]))!=1;illegal+=1;continue
        assert E(z)==q;legal+=1
    three=[(a,b,c,0,0,0) for a,b,c in product(range(-2,3),repeat=3)]
    forward=inverse=F(0)
    for i,x in enumerate(three):
        for y in three[:i]:
            a,b=E(x),E(y);native=sup(x,y);encoded=sup(a,b)
            forward=max(forward,F(encoded,native))
            if (x[2]>=0)==(y[2]>=0):inverse=max(inverse,F(native,encoded))
    assert (forward,inverse)==(4,2)
    depth_clusters=[]
    for r in (1,7,1<<256):
        pts=[(0,0,*s) for s in product((r,-r),repeat=4)]
        ds=[(sup(E(x),E(y)),sup(x,y)) for i,x in enumerate(pts) for y in pts[:i]]
        assert set(ds)=={(1,2*r)}
        assert len({(min(q[:3])%2,*(c%2 for c in q[3:])) for q in map(E,pts)})==16
        depth_clusters.append({'R':str(r),'display_diameter':1,'all_distinct_native_pair_distances':str(2*r),'states':16})
    assert D(E((1,-2,3,-(1<<4096),5,-6)))==(1,-2,3,-(1<<4096),5,-6)
    hidden=[(0,0,0,0,0,0),(1,1,1,0,0,0)]
    assert E(hidden[0])!=E(hidden[1]) and all(z[0]-z[2]==z[1]-z[2]==0 for z in hidden)
    for wrong in [tuple([True]*6),(0,0,0,0,0,0),(2,2,3,4,5,6),(-1,2,3,4,5,6)]:
        try:D(wrong)
        except ValueError:pass
        else:raise AssertionError('malformed address')
    off=wire((0,0,1,0,0,0))
    try:old.FinalCellAddress.from_wire(off)
    except ValueError as e:assert str(e)=='UNREGISTERED_CELL_CODEC'
    else:raise AssertionError('current official registry unexpectedly accepts the proposal')
    for k,v in [('version',True),('frame','unknown'),('codec','other'),('schema','other')]:
        try:unwire({**off,k:v})
        except ValueError:pass
        else:raise AssertionError('invalid header admitted')
    return {'sources':PINS,'finite_exact_counts':counts,'wire_digit_box_0_to_4':{'valid':legal,'invalid':illegal},
            'candidate_registration':'official current runtime rejected this candidate as unregistered',
            'max_ratio_in_three_active_raw_box':{'forward':str(forward),'inverse_with_sign_tag_fixed':str(inverse)},
            'independent_fold_clusters':depth_clusters,'equal_STAR_projection_distinct_fields':[E(z) for z in hidden],'BRC_transport':graph_check(recurrent_mass_power,api)}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True,type=Path)
    print(json.dumps(run(p.parse_args().repo),indent=1,sort_keys=True))
