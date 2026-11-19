"""Integer alias thresholds and minimum translated-grid cubatures for a 3D retained ball."""
import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations_with_replacement, product
from math import isqrt
from pathlib import Path
from runpy import run_path
from tempfile import TemporaryDirectory
import json

SOURCE="research_notes/CFD-B1F673/prior_3d/probe.py"
DIGEST="1d10429616026f13643f0ba1641acd8c23f3aecd1dc7c03b429f5e0c4381eb09"
GRIDS={1:[(0,0,0)],2:[(0,0,0),(1,1,1)],3:[(0,0,0),(0,1,1),(1,0,1)],4:[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]}


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def add(x,y):
    return tuple(a+b for a,b in zip(x,y))


def minus(x,y):
    return tuple(a-b for a,b in zip(x,y))


def scale(c,x):
    return tuple(c*a for a in x)


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])


def threshold(n,t,velocity=False):
    m,s=divmod(n,3)
    if velocity and t>2:
        raise ValueError("3-coordinate aliases are outside the retained anti-Nyquist ball")
    raw=t*m*m+(2*m+1)*((t*s+2)//3)
    boundary_loss=velocity and ((t==1 and s!=1) or (t==2 and s==0))
    return raw+int(boundary_loss)


def search(n,t,d):
    # Direct integer parents, reduced only by Cauchy's necessary bound on their dot with w.
    w=(1,)*t+(0,)*(3-t)
    rhs=scale(n,w)
    cap=isqrt(d)
    min_dot=t*n-2*isqrt(d*t)
    modes=[x for x in product(range(-cap,cap+1),repeat=3)
           if 0<dot(x,x)<=d and dot(x,w)>=min_dot]
    raw=velocity=False
    for p,q in combinations_with_replacement(modes,2):
        c=minus(rhs,add(p,q))
        if not(0<dot(c,c)<=d):
            continue
        raw=True
        if any(cross(p,q)) or any(cross(p,c)):
            velocity=True
            break
    return raw,velocity


def exact_thresholds():
    tests=0
    examples={}
    for n in range(12,49,2):
        for t in (1,2,3):
            raw=threshold(n,t)
            vel=threshold(n,t,True) if t<=2 else None
            scans={}
            for d in range(raw-1,raw+2):
                got=search(n,t,d)
                assert got[0]==(d>=raw)
                if vel is not None:
                    assert got[1]==(d>=vel)
                tests+=1
                scans[str(d)]=[int(v) for v in got]
            if n in (12,14,16,20):
                examples[str((n,t))]={'D_raw':raw,'D_velocity':vel,'search':scans}
    return {'N_even_inclusive':[12,48],'radius_and_type_tests':tests,'examples':examples}


def observe(k,r):
    h=Fraction(dot(k,r),dot(k,k)) if any(k) else Fraction()
    return minus(r,scale(h,k))+(h,)


def build_field(items):
    out={}
    for p,a in items:
        assert any(p) and dot(p,a)==0
        assert p not in out and scale(-1,p) not in out
        out[p]=a
        out[scale(-1,p)]=a
    return out


def mask_factor(w,count):
    return Fraction(sum((-1)**(dot(w,b)%2) for b in GRIDS[count]),count)


def budget_table():
    wraps=[w for w in product((-1,0,1),repeat=3) if 0<sum(bool(v) for v in w)<=2]
    # For the optimum two-point table take relative phase (1,2,3)/6.
    cos6=(Fraction(1),Fraction(1,2),Fraction(-1,2),Fraction(-1),Fraction(-1,2),Fraction(1,2))
    multipliers=[(1+cos6[dot(w,(1,2,3))%6])/2 for w in wraps]
    assert max(multipliers)==Fraction(3,4)
    assert {abs(mask_factor(w,3)) for w in wraps}=={Fraction(1,3)}
    assert {mask_factor(w,4) for w in wraps}=={0}
    return {'relevant_signed_wraps':len(wraps),'squared_optimal_worst_wrap_by_budget':
            ['1','3/4','1/9','0'],'two_node_relative_translation_in_grid_cells':['1/6','1/3','1/2'],
            'three_half_grid_numerators':GRIDS[3],'four_half_grid_numerators':GRIDS[4]}


def exact_groups(field,n,d):
    # All physical amplitudes are real with conjugate input partners. The stored
    # real vector is the coefficient of i at each source/output mode.
    zero=(0,)*4
    ledger=[]
    truth=defaultdict(lambda:zero)
    for p,q in combinations_with_replacement(field,2):
        P=add(p,q)
        k=tuple((v+n//2)%n-n//2 for v in P)
        if dot(k,k)>d:
            continue
        a,b=field[p],field[q]
        raw=minus(scale(dot(a,b),p if p==q else P),scale(dot(q,a),b))
        if p!=q:
            raw=minus(raw,scale(dot(p,b),a))
        joint=observe(k,raw)
        if not any(joint):
            continue
        w=tuple((v-h)//n for v,h in zip(P,k))
        if not any(w):
            truth[k]=add(truth[k],joint)
        else:
            ledger.append((k,w,joint))
    by_key=defaultdict(lambda:zero)
    for k,w,c in ledger:
        by_key[k,w]=add(by_key[k,w],c)
    rows={}
    for count in GRIDS:
        full=defaultdict(lambda:zero,truth)
        error=defaultdict(lambda:zero)
        term=sum(abs(mask_factor(w,count))*sum(map(abs,c)) for _,w,c in ledger)
        grouped=0
        for (k,w),c in by_key.items():
            v=scale(mask_factor(w,count),c)
            grouped+=sum(map(abs,v))
            error[k]=add(error[k],v)
            full[k]=add(full[k],v)
        actual=sum(sum(map(abs,v)) for v in error.values())
        assert actual<=grouped<=term
        velocities=sum(sum(map(abs,v[:3])) for v in error.values())
        rows[count]=({'term_l1':str(term),'same_output_wrap_l1':str(grouped),'true_l1':str(actual),
                      'velocity_l1':str(velocities),'pressure_l1':str(actual-velocities)},full)
    return truth,rows,(len(ledger),len(by_key))


def real_fft_test(repo,n,d,field):
    import numpy as np
    from scipy import fft
    # Avoid mutating the original Numba cache and preserve the frozen source exactly.
    native_path=repo/SOURCE
    assert sha256(native_path.read_bytes()).hexdigest()==DIGEST
    with TemporaryDirectory() as td:
        temp=Path(td)/"probe.py"
        temp.write_bytes(native_path.read_bytes())
        native=run_path(str(temp))
        frozen_cutoff,k,inv,frozen_keep=native['operators'](n)
        k2=np.sum(k*k,axis=0)
        keep=k2<=d
        h=np.zeros((3,n,n,n//2+1),dtype=np.complex128)
        for p,a in field.items():
            assert dot(p,p)<=d
            if p[2]>=0:
                h[:,p[0]%n,p[1]%n,p[2]]=a
        original_default=False
        if all(max(map(abs,p))<=frozen_cutoff for p in field):
            original=native['fft_rhs'](h,n,k,inv,frozen_keep)
            reference_sparse=native['sparse_rhs'](h,n,frozen_cutoff)
            assert np.max(np.abs(original-reference_sparse))<1e-9
            original_default=True
        truth,rows,cost=exact_groups(field,n,d)
        cutoff=isqrt(d)
        sparse=native['sparse_rhs'](h,n,cutoff)*keep
        def reference(table):
            result=np.zeros((4,n,n,n//2+1),dtype=np.complex128)
            for p,v in table.items():
                if p[2]>=0:
                    result[:,p[0]%n,p[1]%n,p[2]]=np.array(tuple(map(float,v)))*1j
            return result
        assert np.max(np.abs(sparse-reference(truth)[:3]))<1e-9
        out={}
        for count,shifts in GRIDS.items():
            averaged=np.zeros((4,n,n,n//2+1),dtype=np.complex128)
            worst_host=0.
            for b in shifts:
                phase=np.exp((1j*np.pi/n)*np.einsum("i,i...->...",b,k))
                shifted=h*phase
                velocity=native['fft_rhs'](shifted,n,k,inv,keep)
                u=fft.irfftn(shifted,s=(n,)*3,axes=(1,2,3),norm='forward')
                curl=1j*np.cross(k,shifted,axisa=0,axisb=0,axisc=0)
                vort=fft.irfftn(curl,s=(n,)*3,axes=(1,2,3),norm='forward')
                raw=fft.rfftn(np.cross(u,vort,axisa=0,axisb=0,axisc=0),axes=(1,2,3),norm='forward')
                pressure=np.sum(k*raw,axis=0)*inv
                projected=(raw-k*pressure)*keep
                worst_host=max(worst_host,float(np.max(np.abs(projected-velocity))))
                averaged+=np.concatenate((velocity,(pressure*keep)[None,...]))*phase.conjugate()/count
            err=np.max(np.abs(averaged-reference(rows[count][1])))
            assert worst_host<1e-9 and err<1e-9
            out[str(count)]=rows[count][0]
        return {'N':n,'D':d,'original_default_cube_replayed':original_default,'full_input_modes':len(field),'nonzero_unordered_aliased_branches':cost[0],
                'distinct_output_wrap_keys':cost[1],'absolute_tolerance_all_complex_host_components':'1e-9',
                'by_number_of_grids':out}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',required=True,type=Path)
    ap.add_argument('--out',type=Path)
    args=ap.parse_args()
    ey=(0,1,0);ez=(0,0,1)
    cases={
      'frozen_default_no_alias':(12,9,[((2,1,0),ez),((1,2,0),ez),((1,0,2),ey)]),
      'single_contact_pressure':(12,16,[((4,0,0),ez)]),
      'single_first_velocity':(12,17,[((4,0,1),ey),((4,0,0),ey)]),
      'double_contact_pressure':(12,32,[((4,4,0),ez)]),
      'double_first_velocity':(12,33,[((4,4,1),(1,-1,0)),((4,4,0),(1,-1,0))]),
    }
    data=[((4,4,0),(1,-1,0)),((4,4,1),(1,-1,0)),((4,4,-1),(-1,1,0)),
          ((5,1,0),ez),((5,-1,0),ez),((4,2,1),(1,-2,0)),((4,2,-1),(-1,2,0)),
          ((-1,5,0),ez),((1,5,0),scale(-1,ez)),((2,4,1),(2,-1,0)),((2,4,-1),(-2,1,0))]
    cases['mixed_real_field']=(12,33,data)
    result={'pinned_source_sha256':DIGEST,'integer_threshold_witnesses':exact_thresholds(),'grid_budget':budget_table(),
            'host_cases':{name:real_fft_test(args.repo,n,d,build_field(a)) for name,(n,d,a) in cases.items()}}
    mix=result['host_cases']['mixed_real_field']['by_number_of_grids']
    assert Fraction(mix['1']['true_l1'])<Fraction(mix['1']['same_output_wrap_l1'])<Fraction(mix['1']['term_l1'])
    assert Fraction(mix['2']['true_l1'])>0 and Fraction(mix['4']['true_l1'])==0
    report=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.out:args.out.write_text(report)
    else:print(report,end='')


if __name__=='__main__':
    main()
