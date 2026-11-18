"""Replay frozen N=16 Fourier data and exact lattice certificates (Python, NumPy, SciPy)."""
import argparse
import ast
import csv
import hashlib
import itertools
import json
import math
import os
import statistics
import sys
import time
import types
from collections import Counter
from pathlib import Path

import numpy as np
from scipy import fft


DIR = "research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/"
CHECK = "research_checks/CFD_SPECTRAL_HYBRID_292BCE_20260917.py"
PINS = {
    CHECK:"eaa378080453b967a47b820e2a66594b1eaec2398a9381e366c2cdbe65378856",
    DIR+"static_carrier_native_adapter.py":"c3a8975aaf60e858900146350909983546a86fd6bfe51388fc1c6217a587442b",
    DIR+"summary.json":"5eaca57874aa5327b1aaed5a7aeb796133d3dea8fc5b0c62a3f3a203105f11c7",
    DIR+"raw_trials.csv":"cf9d8733633b3191d480534f0e63eb0873574446b87fc323cec51ba5377567f2",
    "src/enterprise_math/_cell_slice_codec.py":"9eb64264a59e23402c51d8aa20ff9a21ff37dec5f8bd80a97da2f54bbb48a70b",
    "src/enterprise_math/cell_address.py":"b0ec81867994146ad69e81f73c74cfe58071c361150a84749be7a852536f1329"}
NAME = "heldout-xy-plane-generators"


def source(root):
    for path,h in PINS.items():
        assert hashlib.sha256((root/path).read_bytes()).hexdigest()==h, path
    adapter = types.ModuleType("transport_audit_pinned_adapter")
    sys.modules[adapter.__name__]=adapter
    exec(compile((root/(DIR+"static_carrier_native_adapter.py")).read_bytes(),str(root/DIR), "exec"),adapter.__dict__)
    # The selected FFT, pressure, RK4 and seeded initializer are executed from original AST.
    tree=ast.parse((root/CHECK).read_bytes())
    keep={"native_operators","DealiasedFFT","project","FFTEngine","rk4","set_mode","div_free_amp","structured","extract_support"}
    names={"N","K","M","NU","DT","STEPS","LIMIT","STRUCT_SEEDS"}
    selected=[]
    for node in tree.body:
        if isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.name in keep:
            selected.append(node)
        if isinstance(node,ast.Assign) and getattr(node.targets[0],"id",None) in names:
            selected.append(node)
    assert len(selected)==len(keep)+len(names)
    ns={"np":np,"fft":fft,"time":time}
    exec(compile(ast.Module(selected,[]),str(root/CHECK),"exec"),ns)
    sys.path.insert(0,str(root/"src"))
    from enterprise_math import cell_address
    return adapter,types.SimpleNamespace(**ns),cell_address


def true_1d(K,mod):
    return sum((x+y-z)%mod==0 for x,y,z in itertools.product(range(-K,K+1),repeat=3))


def r2(m):
    if m==0:
        return 1
    return 4*sum((1 if d%4==1 else -1 if d%4==3 else 0) for d in range(1,m+1) if m%d==0)


def r1(t):
    return 1 if t==0 else 2*int(math.isqrt(t)**2==t)


def arith():
    K=7
    B=list(itertools.product(range(-K,K+1),repeat=2))
    shells=Counter(x*x+y*y for x,y in B)
    calculated={m:r2(m)-4*sum(r1(m-x*x) for x in range(K+1,math.isqrt(m)+1)) for m in range(2*K*K+1)}
    assert shells==Counter({m:h for m,h in calculated.items() if h})
    pair_counts=Counter((x+s,y+t) for (x,y),(s,t) in itertools.product(B,repeat=2))
    retained=sum(pair_counts[m] for m in B)
    assert retained==169**2
    alias={}
    for M in (15,16,21,22,24):
        target={ (x%M,y%M) for x,y in B}
        n=sum(v for (x,y),v in pair_counts.items() if (x%M,y%M) in target)
        assert n==true_1d(K,M)**2
        alias[M]=dict(accepted=n,false=n-retained)
    # Enumerate all column-Hermite normal forms [[a,t],[0,c]] of index b^2.
    b=3*K+1
    forms=[]
    for a in range(1,b*b+1):
        if b*b%a:
            continue
        c=b*b//a
        for t in range(a):
            # x can be shifted through all residues differing by a.
            admissible=a>=b and all(min((j*t)%a,(-j*t)%a)>=b for j in range(1,(b-1)//c+1))
            if admissible:
                forms.append((a,t,c))
    smith=Counter(math.gcd(a,t,c) for a,t,c in forms)
    assert len(forms)==2*b-1 and smith=={1:20,2:20,11:2,22:1}
    codes={(x+b*y)%(b*b) for x,y in B}
    assert len(codes)==len(B)
    cyc=sum(v for (x,y),v in pair_counts.items() if (x+b*y)%(b*b) in codes)
    assert cyc==retained
    # Ordered Vortex witnesses: p=(7,0,0), q=(M-14,1,0), A=e_y, B=e_z.
    alias_vector={}
    for m in (16,21):
        p=np.array([7,0,0]); q=np.array([m-14,1,0])
        A=np.array([0,1,0]); Bv=np.array([0,0,1]); target=np.array([-7,1,0])
        out=np.cross(A,np.cross(q,Bv))+np.cross(Bv,np.cross(p,A))
        assert np.array_equal((p+q-target)%m,[0,0,0]) and not np.array_equal(p+q,target)
        assert not p@A and not q@Bv and not out@target and tuple(out)==(0,0,-1)
        alias_vector[m]=dict(q=q.tolist(),true_sum=(p+q).tolist(),wrapped=target.tolist(),projected_over_i=out.tolist())
    # Kernel of (x+22*y) modulo 483. List every erroneously selected ordered pair.
    det=b*b-1
    key=lambda p:(p[0]+b*p[1])%det
    destinations={key(p):p for p in B}
    assert len(destinations)==len(B)
    skew_false=[]
    for p,q in itertools.product(B,repeat=2):
        total=(p[0]+q[0],p[1]+q[1])
        m=destinations.get(key(total))
        if m is not None and total!=m:
            skew_false.append((p,q,m))
    assert skew_false==[((-7,-7),(-7,-7),(7,7)),((7,7),(7,7),(-7,-7))]
    in_box=[(x,y) for x,y in itertools.product(range(-3*K,3*K+1),repeat=2)
            if (x,y)!=(0,0) and key((x,y))==0]
    assert in_box==[(-21,-21),(21,21)]
    tangent=[np.array([1,-1,0]),np.array([0,0,1])]
    tested=0
    # A vector-valued complex quadratic form is determined by two basis squares
    # and their polarized mixed term. Integer vector identities therefore suffice.
    for p,q,m in skew_false:
        P=np.array((*p,0)); M=np.array((*m,0))
        for h,j in itertools.combinations_with_replacement(range(2),2):
            a,c=tangent[h],tangent[j]
            term=np.cross(a,np.cross(P,c))
            if h!=j:
                term+=np.cross(c,np.cross(P,a))
            assert not P@a and not P@c
            assert np.array_equal((M@M)*term-M*(M@term),np.zeros(3,dtype=int))
            tested+=1
        assert np.array_equal(np.cross(tangent[1],np.cross(P,tangent[1])),P)
    # For each nonzero discrepancy other than the four corners, retain a
    # genuinely nonparallel interaction producing transverse velocity.
    h=3*K
    separated=0
    for dx,dy in itertools.product(range(-h,h+1),repeat=2):
        if (dx,dy)==(0,0) or abs(dx)==abs(dy)==h:
            continue
        swap=abs(dy)>abs(dx)
        a,v=sorted((abs(dx),abs(dy)),reverse=True)
        x=next(i for i in range(1,K+1) if abs(2*i-a)<=K)
        y,z=next((i,j) for i,j in itertools.combinations(range(-K,K+1),2) if i+j==v-K)
        def undo(ix,iy):
            if swap:
                ix,iy=iy,ix
            return np.array([(-ix if dx<0 else ix),(-iy if dy<0 else iy),0])
        p,q=undo(x,y),undo(x,z)
        m=p+q-np.array([dx,dy,0])
        assert any(m) and max(abs(m))<=K
        A=np.array([-p[1],p[0],0]); ez=np.array([0,0,1])
        out=np.cross(A,np.cross(q,ez))+np.cross(ez,np.cross(p,A))
        assert not p@A and not q@ez and out[2] and not m@out
        separated+=1
    assert separated==(2*h+1)**2-5==1844
    # Distinct real Fourier phases isolate the same transverse term even at m=0.
    # p=(1,0),q=(1,1), A=e_y, B=i*e_z. The positive pair gives +e_z,
    # and its negative conjugate also gives +e_z. With period lattice
    # <(2,1),(0,100)> no other mixed pair contributes to the zero character.
    zero_mixed_raw=(0,0,2)
    delta=(2,1)
    p0,q0=np.array([1,0,0]),np.array([1,1,0])
    av,bv=np.array([0,1,0]),np.array([0,0,1])
    coeff=np.cross(av,np.cross(q0,bv))+np.cross(bv,np.cross(p0,av))
    assert tuple(-2*coeff)==zero_mixed_raw and tuple((p0+q0)[:2])==delta
    assert (p0[0]-q0[0]-2*(p0[1]-q0[1]))%200!=0
    # Independent enumeration of Hermite forms allowing only corner discrepancies.
    def leray_forms(index):
        good=[]
        for horizontal in range(h+1,index+1):
            if index%horizontal:
                continue
            vertical=index//horizontal
            for shear in range(horizontal):
                ok=True
                for j in range(1,h//vertical+1):
                    dist=min((j*shear)%horizontal,(-j*shear)%horizontal)
                    if dist<h or (dist==h and j*vertical!=h):
                        ok=False
                        break
                if ok:
                    good.append([horizontal,shear,vertical])
        return good
    extremals=leray_forms(b*b-1)
    assert all(not leray_forms(index) for index in range(1,det)) and extremals==[[483,22,1],[483,461,1]]
    total_hnf=sum(a*(det//a) for a in range(1,det+1))
    assert total_hnf==192020
    skew_report=dict(index=det,minimum_projected_index=det,optimal_projected_Hermite_forms=extremals,all_Hermite_forms_through_minimum=total_hnf,
                     all_noncorner_nonzero_discrepancies_separated=separated,mean_mode_projected_mixed_term=zero_mixed_raw,short_nonzero_lattice_vectors=in_box,
                     accepted_ordered_pairs=retained+len(skew_false),spurious_ordered_pairs=skew_false,
                     zero_projected_polynomial_coefficients_tested=tested,
                     raw_over_i_with_vertical_unit_amplitude_at_positive_corner=[7,7,0],
                     pressure_over_i_defect_at_wrapped_negative_corner=-1)
    # Shortest boundary-observation distinguisher for the four labelled unit shifts.
    def depth(p,q):
        return min(min(K-max(x,y)+1,K+min(x,y)+1) for x,y in zip(p,q) if x!=y)
    ds=Counter(depth(p,q) for p,q in itertools.combinations(B,2))
    assert max(ds)==K and sum(ds.values())==225*224//2
    return dict(distinguishing_depth_histogram=dict(sorted(ds.items())),shells=dict(sorted(shells.items())),retained_pairs=retained,all_ordered_pairs=len(B)**2,
                modular_pair_counts=alias,least_scalar_grid=b,cyclic_samples=b*b,cyclic_pairs=cyc,
                optimal_lattices=len(forms),smith_first_invariant=dict(sorted(smith.items())),nonzero_alias_witness=alias_vector,projected_skew_lattice=skew_report)


def checked_table(root,sca,h,ref):
    summary=json.loads((root/(DIR+"summary.json")).read_text())
    pretty=(json.dumps(summary,indent=2)+"\n").encode()
    serialized_hash=hashlib.sha256(pretty).hexdigest()
    assert serialized_hash=="a4cc2577e762d931a63ebdd14261e9007269eba7c352e20584739f783ab42d63"
    csv_bytes=(root/(DIR+"raw_trials.csv")).read_bytes()
    crlf_hash=hashlib.sha256(csv_bytes.replace(b"\n",b"\r\n")).hexdigest()
    assert crlf_hash=="5526f5ac3c3430ccf72bfe2a5a75d908bd3a1c9fd5a536cd9f4fa1bdb4e72965"
    row=next(r for r in summary["cases"] if r["name"]==NAME)
    with (root/(DIR+"raw_trials.csv")).open() as f:
        trials=[r for r in csv.DictReader(f) if r["case"]==NAME]
    for method in ("static","fft"):
        selected=[r for r in trials if r["mode"]==method]
        assert len(selected)==7
        assert statistics.median(float(r["total_seconds"]) for r in selected)==row["median_breakdown_seconds"][method]["total_seconds"]
    labels=ref.extract_support(h,16)[0]
    res=sca.truncated_additive_carrier(labels,7,384)
    assert len(labels)==row["initial_full_signed_support"]==4
    assert res.status==row["decision"] and len(res.carrier)==225
    assert (res.rounds,res.pair_tests,res.carrier_size)==(row["detector_rounds"],row["detector_pair_tests"],row["carrier_size"])
    assert sca.verify_carrier(res.carrier,7)
    return res,dict(summary_historical_serialization_sha256=serialized_hash,csv_historical_crlf_sha256=crlf_hash,initial_signed=4,rounds=res.rounds,detector_pairs=res.pair_tests,carrier_size=res.carrier_size,
                    raw_trial_rows=len(trials),fft_historical_median=row["median_breakdown_seconds"]["fft"]["total_seconds"],
                    static_historical_median=row["median_breakdown_seconds"]["static"]["total_seconds"])


def trajectory(root):
    sca,ref,codec=source(root)
    h=ref.structured(NAME)
    res,summary=checked_table(root,sca,h,ref)
    plane=res.carrier
    grid={(x,y) for x,y,z in plane}
    assert all(z==0 for x,y,z in plane) and len(grid)==225
    addr={xy:codec.encode_raw_slice(xy) for xy in grid}
    for xy,a in addr.items():
        assert codec.decode_raw_slice(codec.FinalCellAddress.from_wire(a.to_wire()))==xy
    start=codec.encode_raw_slice((0,0)); end=codec.step_cell(start,"E1_FORWARD")
    assert start.coordinates[:3]==(0,1,1) and end.coordinates[:3]==(1,0,1)
    for bad in ((0,0,1,0,0,0),(1,2,0,1,0,0)):
        try:
            codec.FinalCellAddress(bad)
        except ValueError:
            continue
        raise AssertionError("invalid slice address accepted")
    ordered=sorted(grid,key=lambda xy:addr[xy].coordinates)
    # Each k3 is a separate typed label; only k3>=0 is stored in the source rFFT.
    labels=[(x,y,z) for z in range(8) for x,y in ordered]
    whole_gather=sca.build_fixed_rfft_gather(itertools.product(range(-7,8),repeat=3),16)
    g_labels,ix,iy,iz,conj=whole_gather
    assert len(set(zip(ix,iy,iz)))==1800 and int(sum(conj))==1575
    ar=np.array(labels).T
    arr_idx=(ar[0]%16,ar[1]%16,ar[2])
    def pack(v):
        return np.ascontiguousarray(v[(slice(None),*arr_idx)])
    def unpack(v):
        out=np.zeros_like(h)
        out[(slice(None),*arr_idx)]=v
        return out
    eng=ref.FFTEngine()
    history=[]
    class Reference:
        def rhs(self,u):
            out=eng.rhs(u)
            history.append((pack(u),pack(out)))
            return out
    final_ref=ref.rk4(h,Reference())
    kk=np.sum(ar*ar,axis=0)
    inv=1.0/np.where(kk==0,1,kk)
    new_fft=ref.DealiasedFFT(16)
    same_bits=0
    omitted_mask_bits=0
    class Transported:
        stage=0
        def rhs(self,u):
            nonlocal same_bits,omitted_mask_bits
            actual=pack(new_fft.rotational(unpack(u)))
            sig=np.sum(ar*actual,axis=0)*inv
            pre=actual-ar*sig
            out=pre*np.ones_like(kk,dtype=bool)-ref.NU*kk*u
            omitted=pre-ref.NU*kk*u
            x,y=history[self.stage]
            assert np.array_equal(u,x) and np.array_equal(out,y) and np.array_equal(omitted,y), self.stage
            omitted_mask_bits+=int(omitted.tobytes()==y.tobytes())
            if u.tobytes()==x.tobytes() and out.tobytes()==y.tobytes():
                same_bits+=1
            self.stage+=1
            return out
    second=Transported()
    final_new=ref.rk4(pack(h),second)
    assert second.stage==len(history)==48
    assert np.array_equal(unpack(final_new),final_ref)
    assert all(np.array_equal(v[:,ar[2]>0],np.zeros_like(v[:,ar[2]>0])) for pair in history for v in pair)
    # Test the frozen projection independently with each diagonal/non-diagonal matrix entry.
    for j in range(3):
        g=np.zeros_like(h); g[j,:,:,:]=1
        original=pack(ref.project(g,eng.k,eng.inv,eng.keep))
        eye=pack(g)
        transported=eye-ar*(np.sum(ar*eye,axis=0)*inv)
        assert np.array_equal(original,transported)
    # Small operator-specific alias/shell checks and intrinsic order sensitivity.
    a,b,c=2.**53,1.,-2.**53
    assert (a+b)+c==0 and (a+c)+b==1
    return dict(source_table=summary,address_count=len(addr),source_half_storage_labels=len(labels),
                source_signed_box=len(g_labels),negative_third_axis_references=int(sum(conj)),
                same_value_crossing=[start.coordinates,end.coordinates],invalid_address_rejections=2,
                rhs_stages=second.stage,equal_stages=48,byte_equal_stages=same_bits,stage_rhs_byte_equal_after_omitting_keep=omitted_mask_bits,
                final_packed_byte_equal=bool(pack(final_ref).tobytes()==final_new.tobytes()),
                final_equal=bool(np.array_equal(pack(final_ref),final_new)),
                all_offplane_stage_entries_zero=True,retained_pressure_projector_columns_tested=3*len(labels))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-root",type=Path,default=os.environ.get("ENTERPRISE_MATH"))
    args=ap.parse_args()
    if not args.source_root:
        ap.error("provide the pinned enterprise-math checkout with --source-root or ENTERPRISE_MATH")
    report=dict(source_pins=PINS,exact=arith(),finite_source_replay=trajectory(Path(args.source_root)))
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
