#!/usr/bin/env python3
"""Exact full 16-bit number atlas and image-readback audit (research only).
Run: python experiment.py --output DIR
Requires numpy, Pillow; work/fixed_point.py is the hash-pinned Nollm helper.
All data images retain 16-bit samples. Preview colours are not identity storage.
"""
from __future__ import annotations
import argparse, csv, hashlib, importlib.util, json, math
from collections import Counter
from pathlib import Path
import numpy as np
from PIL import Image

N=1<<16
SIDE=256

def morton_decode(n):
    n=np.asarray(n,dtype=np.int64)
    x=np.zeros_like(n); y=np.zeros_like(n)
    for i in range(8):
        x|=((n>>(2*i))&1)<<i
        y|=((n>>(2*i+1))&1)<<i
    return x,y

def morton_encode(x,y):
    x=np.asarray(x,dtype=np.int64);y=np.asarray(y,dtype=np.int64)
    out=np.zeros_like(x+y)
    for i in range(8):
        out|=((x>>i)&1)<<(2*i)
        out|=((y>>i)&1)<<(2*i+1)
    return out

def hex_spiral(count):
    out=[(0,0)]
    dirs=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
    radius=1
    while len(out)<count:
        q,r=0,-radius
        for dq,dr in dirs:
            for _ in range(radius):
                if len(out)==count: return np.asarray(out,dtype=np.int32)
                out.append((q,r)); q+=dq; r+=dr
        radius+=1
    return np.asarray(out,dtype=np.int32)

def hist(a):
    v,c=np.unique(a,return_counts=True)
    return {str(int(x)):int(y) for x,y in zip(v,c)}

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def run(root):
    root.mkdir(parents=True,exist_ok=True); raw=root/'raw';raw.mkdir(exist_ok=True)
    n=np.arange(N,dtype=np.int64)
    mx,my=morton_decode(n)
    assert np.array_equal(morton_encode(mx,my),n)
    hx=hex_spiral(N)
    assert len(set(map(tuple,hx)))==N
    hr=int(np.abs(hx).max()); assert hr==148
    layouts={
        'row':(n%SIDE,n//SIDE,(SIDE,SIDE)),
        'morton':(mx,my,(SIDE,SIDE)),
        'hex':(hx[:,0]+hr,hx[:,1]+hr,(2*hr+1,2*hr+1)),
    }
    primes=np.ones(N,dtype=bool);primes[:2]=False
    spf=np.zeros(N,dtype=np.int64)
    for p in range(2,math.isqrt(N-1)+1):
        if primes[p]: primes[p*p::p]=False
    for p in np.flatnonzero(primes):
        ids=np.arange(p,N,p); blank=spf[ids]==0;spf[ids[blank]]=p
    v2=np.zeros(N,dtype=np.int64);v2[0]=16  # capped sentinel, not v_2(0)=16
    for i in range(1,16):v2[(n>0)&(n%(1<<i)==0)]=i
    bitcount=np.fromiter((int(x).bit_count() for x in n),np.int64,count=N)
    attrs={'labels':n,'prime':primes.astype(np.int64),'v2_capped':v2,
           'mod3':n%3,'mod6':n%6,'popcount':bitcount,'smallest_prime_factor':spf}
    for w in (2730,2731,49152):
        attrs[f'q16_quotient_w{w}']=n*w//N
        attrs[f'q16_remainder_w{w}']=n*w%N
    attrs['q16_one_unit_difference']=attrs['q16_quotient_w2731']-attrs['q16_quotient_w2730']
    attrs['three_phase_rounding_deficit']=n//8-(2*attrs['q16_quotient_w2731']+attrs['q16_quotient_w2730'])
    assert attrs['three_phase_rounding_deficit'].min()>=0
    maps={}; audits=[]
    for name,(x,y,shape) in layouts.items():
        occ=np.zeros(shape,dtype=np.uint8);occ[y,x]=255
        Image.fromarray(occ).save(raw/f'{name}_occupancy.png')
        for key,values in attrs.items():
            a=np.zeros(shape,dtype=np.uint16);a[y,x]=values.astype(np.uint16)
            path=raw/f'{name}_{key}_16bit.png'
            Image.fromarray(a).save(path)
            # Independent readback from the PNG file, before image-side analysis.
            b=np.asarray(Image.open(path),dtype=np.int64)
            assert np.array_equal(b[y,x],values)
            header=path.read_bytes();assert header[24:26]==bytes([16,0])
            if key=='labels':
                maps[name]=b
                recovered=b[np.asarray(Image.open(raw/f'{name}_occupancy.png'))>0]
                assert np.array_equal(np.sort(recovered),n)
                audits.append(dict(layout=name,pixels=int(occ.size),occupied=N,
                    unique_labels=len(np.unique(recovered)),minimum=int(recovered.min()),maximum=int(recovered.max()),
                    exact_roundtrip=True,sha256=sha(path)))
    # Derive numerical structure FROM the decoded image arrays.
    row=maps['row'];z=maps['morton']; yy,xx=np.indices(row.shape)
    rowdx=np.diff(row,axis=1);rowdy=np.diff(row,axis=0)
    assert np.all(rowdx==1) and np.all(rowdy==256)
    mixed=np.diff(np.diff(z,axis=0),axis=1)
    assert not mixed.any()
    assert np.all(z+np.rot90(z,2)==65535)
    pc=np.asarray([i.bit_count() for i in range(256)])
    assert np.array_equal(z%3,(pc[:,None]*2+pc[None,:])%3)
    # Recover small-prime exclusion directions by testing decoded labels.
    divtests=[]
    prime_row=np.asarray(Image.open(raw/'row_prime_16bit.png'),dtype=bool)
    for p in (3,5,17):
        mask=(xx+yy)%p==0
        exceptions=row[mask & prime_row]
        assert np.array_equal(exceptions,np.array([p]))
        maskfile=raw/f'row_divisible_{p}_16bit.png'
        Image.fromarray((row%p==0).astype(np.uint16)).save(maskfile)
        divtests.append(dict(p=p,formula=f'(x+y) mod {p}',prime_exceptions=exceptions.tolist(),
                              mask_pixels=int(mask.sum())))
    # Exact arithmetic rotation witness, with the layout held fixed.
    assert 65533==13*71**2
    prime_m=np.asarray(Image.open(raw/'morton_prime_16bit.png'),dtype=bool)
    overlap=int(np.sum(prime_m&np.rot90(prime_m,2)))
    assert overlap==0
    # Multiplication on finite labels: support vs multiplicity are distinct.
    multiplications=[]
    for a in (2,3,4,5,6,7,11,16,256):
        low=(a*n)%N;high=(a*n)//N
        mult=np.bincount(low,minlength=N)
        expected=math.gcd(a,N)
        assert (mult>0).sum()==N//expected
        assert np.all(mult[mult>0]==expected)
        assert np.array_equal((N*high+low)//a,n)
        if a in (2,3,4,5):
            arr=mult[z]
            Image.fromarray(arr.astype(np.uint16)).save(raw/f'morton_mul{a}_multiplicity_16bit.png')
        inv=pow(a,-1,N) if expected==1 else None
        if inv is not None:assert np.array_equal((low*inv)%N,n)
        multiplications.append(dict(multiplier=a,occupied=int((mult>0).sum()),
            multiplicity=expected,inverse_mod_65536=inv,overflow_pair_recovers_all=True))
    twice_x,twice_y=morton_decode((2*n)%N)
    assert np.array_equal(twice_x,(2*my)%SIDE) and np.array_equal(twice_y,mx)
    four_x,four_y=morton_decode((4*n)%N)
    assert np.array_equal(four_x,(2*mx)%SIDE) and np.array_equal(four_y,(2*my)%SIDE)
    # Q16 operator: inverse image sizes, exact dropped remainder, slow phase drift.
    weightrows=[]
    for w in (2730,2731,49152):
        q=np.asarray(Image.open(raw/f'row_q16_quotient_w{w}_16bit.png'),dtype=np.int64).ravel()
        r=np.asarray(Image.open(raw/f'row_q16_remainder_w{w}_16bit.png'),dtype=np.int64).ravel()
        assert np.array_equal((N*q+r)//w,n)
        diff=(np.roll(r,-24)[:-24]-r[:-24])%N
        drift=(24*w)%N
        assert np.all(diff==drift)
        # Recover multiplier from cyclic adjacent phase differences, without original labels.
        adj=(np.roll(r,-1)-r)%N
        assert np.all(adj==w%N)
        fibers=np.bincount(q,minlength=w)
        weightrows.append(dict(weight=w,quotient_distinct=int(np.unique(q).size),
            zero_inputs=int((q==0).sum()),quotient_preimage_histogram=hist(fibers),
            remainder_distinct=int(np.unique(r).size),remainder_period=N//math.gcd(w,N),
            recovered_weight_from_remainder=int(adj[0]),step24_drift=drift,
            input_recovery_from_quotient_and_remainder=True))
    # Bitplanes: exact scales recovered from label pixels; no visual extrapolation.
    blocklaws=[]
    for j in range(9):
        side=1<<j
        for y in range(0,256,side):
            for x in range(0,256,side):
                block=z[y:y+side,x:x+side].ravel();lo=int(block.min())
                assert lo%(side*side)==0
                assert np.array_equal(np.sort(block),np.arange(lo,lo+side*side))
        blocklaws.append(dict(side=side,states=side*side,blocks=(256//side)**2,all_contiguous=True))
    # What collapses when fixed scores are iterated? All inputs, not just full scale.
    iterrows=[]; cur=n.copy()
    for k in range(1,65):
        cur=cur*3//4
        exact=np.fromiter((int(v)*3**k//4**k for v in n),np.int64,count=N)
        if k in (1,4,8,12,16,24,32,36,37,38,39,40) or not cur.any():
            iterrows.append(dict(k=k,positive_iterated=int((cur>0).sum()),positive_single_round=int((exact>0).sum()),
                                distinct_iterated=int(np.unique(cur).size),maximum_error=int((exact-cur).max())))
        if not cur.any():break
    # Reuse actual fixed-point helper, rather than a substitute normalization rule.
    choices=[Path(__file__).parent/'work/fixed_point.py',
             Path(__file__).parent/'nollm_65536_image_atlas_20260910_c6c82_support/fixed_point.py']
    helper=next((p for p in choices if p.exists()),None)
    if helper is None:raise FileNotFoundError('hash-pinned fixed_point.py dependency missing')
    helpercheck=None
    if helper.exists():
        b=helper.read_bytes();blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        assert blob=='9ea00e3c84a82f480c692a6ca0ca717a579dab60'
        spec=importlib.util.spec_from_file_location('pinned_fixed_point',helper)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        weights=mod.normalize_q16_weights([72,4,4,4,4,4,4])
        assert sorted(weights)==[2730,2730,2731,2731,2731,2731,49152]
        helpercheck=dict(git_blob=blob,weights=list(weights),executed=True)
    delta=np.asarray(Image.open(raw/'row_q16_one_unit_difference_16bit.png'),dtype=np.int64)
    assert hist(delta)=={'0':32769,'1':32767}
    phase_def=np.asarray(Image.open(raw/'row_three_phase_rounding_deficit_16bit.png'),dtype=np.int64)
    summary=dict(schema='NOLLM_65536_EXACT_IMAGE_AUDIT_V1',status='PASS_RESEARCH_NOT_PROMOTED',
        population={'start':0,'stop_exclusive':N,'N':N,'Q16_one_is_an_extra_endpoint_not_in_this_population':True},
        raw_png_roundtrips=audits,raw_png_files=len(list(raw.glob('*_16bit.png'))),prime_count=int(primes.sum()),
        row_image_recovered_dx=hist(rowdx),row_image_recovered_dy=hist(rowdy),
        morton_image_dx_hist=hist(np.diff(z,axis=1)),morton_image_dy_hist=hist(np.diff(z,axis=0)),
        morton_mixed_difference_zero=True,morton_180_complement=65535,
        rotated_prime_overlap=overlap,complement_of_two_factors=[13,71,71],
        prime_exclusion_directions=divtests,morton_mod3_popcount_identity=True,
        complete_morton_blocks=blocklaws,
        hex_spiral={'last_radius':hr,'fully_completed_radius':147,'complete_inner_points':1+3*147*148,
                    'points_in_last_ring':N-(1+3*147*148),'complete_next_hex_count':1+3*148*149},
        modular_multiplication=multiplications,
        q16_inverse_audit=weightrows,one_unit_change_pixel_histogram=hist(delta),
        three_phase_integer_rounding_deficit_histogram=hist(phase_def),
        repeated_3over4=iterrows,pinned_helper=helpercheck,
        limits=['Population is deliberately 0..65535; Q16 full-scale 65536 is excluded.',
                'Morton and row grids are observation encodings, not Nollm physical-layer placements.',
                'Modulo-65536 multiplication is not unbounded integer multiplication or Q16 multiplication.',
                'Pseudo-colour previews are not the lossless integer images.',
                'Prime pictures do not prove novel prime distribution theorems.',
                'v2(0) uses sentinel16 only; it is not a finite valuation of zero.',
                'Finite exact image identities are not semantic-memory quality evidence.'])
    # A second pass follows the six visible vertex rays using only decoded images.
    ha=maps['hex']; hp=np.asarray(Image.open(raw/'hex_prime_16bit.png'))
    rayrows=[]
    for k,(dq,dr) in enumerate(((0,-1),(1,-1),(1,0),(0,1),(-1,1),(-1,0))):
        t=np.arange(1,148);v=ha[dr*t+148,dq*t+148]
        assert np.all(np.diff(v,2)==6)
        assert np.all(v==3*t*t+(k-3)*t+1)
        rayrows.append(dict(ray=k,axial_direction=[dq,dr],polynomial=[3,k-3,1],
            observed_second_difference=6,complete_radii=147,
            prime_count=int(hp[dr*t+148,dq*t+148].sum()),
            first_12_labels=v[:12].tolist(),even_count=int((v%2==0).sum()),
            multiple3_count=int((v%3==0).sum())))
    (root/'image_ray_analysis.json').write_text(json.dumps(rayrows,indent=2)+'\n')
    (root/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
    np.savez_compressed(root/'arrays.npz',labels_row=row,labels_morton=z,hex_qr=hx,**attrs)
    with (root/'all_65536_points.csv').open('w',newline='') as f:
        wr=csv.writer(f);wr.writerow(['n','row_x','row_y','morton_x','morton_y','hex_q','hex_r','prime','v2_capped','popcount'])
        wr.writerows((int(k),int(k%256),int(k//256),int(mx[k]),int(my[k]),int(hx[k,0]),int(hx[k,1]),
                      int(primes[k]),int(v2[k]),int(bitcount[k])) for k in n)
    (root/'raw_manifest.json').write_text(json.dumps({p.name:sha(p) for p in sorted(raw.glob('*.png'))},indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    return summary

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).parent)
    run(parser.parse_args().output)
