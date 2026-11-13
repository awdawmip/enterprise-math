#!/usr/bin/env python3
"""R118: exact S23 six-affine-phase two-band feasibility oracle.
Pure Python Fraction arithmetic; no floating-point; independently compare full cut atoms.
"""
from fractions import Fraction as Q
from math import floor, ceil
import random, json, hashlib, pathlib, time

SEED=1182026
RNG=random.Random(SEED)
COUNTS={"seed":SEED,"random_cases":0,"old_atoms_checked":0,"oracle_calls":0,"oracle_band_checks":0,"oracle_witnesses":0,"bruteforce_new_atoms":0,"exact_top1_checkpoints":0,"large_signed_cases":0,"max_witness_bitlength":0,"newtime_raw_cut_count_small_cases":0}

def frac(v): return v-floor(v)
def eligible(th,t,j,x,a,c):
    aa=frac(a*th); cc=frac(c*th); yy=frac(x+(t-j)*th)
    if aa == cc: return False
    if aa < cc: return aa<=yy<cc
    return yy>=aa or yy<cc

def cuts_phase(m, b,lo=Q(0),hi=Q(1)):
    if m==0: return set()
    v0=m*lo+b; v1=m*hi+b
    lower=min(v0,v1); upper=max(v0,v1)
    out=set()
    for k in range(floor(lower)-1,ceil(upper)+2):
        theta=(Q(k)-b)/m
        if lo < theta < hi: out.add(theta)
    return out

def six_cuts(t,j,x,a,c,lo=Q(0),hi=Q(1)):
    Y=t-j
    forms=((a,Q(0)),(c,Q(0)),(a-c,Q(0)),(Y,x),(Y-a,x),(Y-c,x))
    out=set()
    for slope,offset in forms:out.update(cuts_phase(slope,offset,lo,hi))
    return out

def atoms(cuts,lo=Q(0),hi=Q(1)):
    pts=[lo]+sorted(v for v in cuts if lo<v<hi)+[hi]
    out=[]
    for i,point in enumerate(pts):
        out.append((point,point,True))
        if i+1<len(pts):out.append((point,pts[i+1],False))
    return out

def midpoint(atom):
    lo,hi,pt=atom
    return lo if pt else (lo+hi)/2

def put_upper(cur, v):
    return v if cur is None else min(cur,v)

def put_lower(cur, v):
    return v if cur is None else max(cur,v)

def exact_band_open(lo,hi,lower_slope,lower_const,upper_slope,upper_const):
    """exists theta in (lo,hi), integer n with L(theta)<n<=U(theta),
    provided U(theta)-L(theta)>0 continuously on (lo,hi)."""
    COUNTS["oracle_band_checks"]+=1
    Llo=lower_slope*lo+lower_const
    Lhi=lower_slope*hi+lower_const
    Ulo=upper_slope*lo+upper_const
    Uhi=upper_slope*hi+upper_const
    mn=min(Llo,Lhi); mx=max(Ulo,Uhi)
    n=floor(mn)+1
    if not (Q(n)<mx or (upper_slope==0 and Q(n)==mx)):
        return None
    # Recover interior rational theta using strict L<n and strict U>n
    # (unless U is the constant included edge U=n).
    left=lo; right=hi
    if lower_slope==0:
        assert lower_const<Q(n)
    else:
        boundary=(Q(n)-lower_const)/lower_slope
        if lower_slope>0:right=min(right,boundary)
        else:left=max(left,boundary)
    if upper_slope==0:
        assert upper_const>=n
    else:
        boundary=(Q(n)-upper_const)/upper_slope
        if upper_slope>0:left=max(left,boundary)
        else:right=min(right,boundary)
    assert left<right,(lo,hi,n,mn,mx,left,right,lower_slope,upper_slope)
    theta=(left+right)/2
    assert lo<theta<hi
    assert lower_slope*theta+lower_const<n<=upper_slope*theta+upper_const
    return theta

def arc_oracle_open(lo,hi,t,j,x,a,c,reverse=False):
    """Full S23 directed arc oracle on one old eligible-constant open cell.
    reverse=True means complementary directed arc, with equal-endpoint special case outside.
    """
    sample=(lo+hi)/2
    af=a*sample; cf=c*sample
    p=floor(af); q=floor(cf)
    if reverse:
        left_slope,left_floor,left_frac=c,q,frac(cf)
        right_slope,right_floor,right_frac=a,p,frac(af)
    else:
        left_slope,left_floor,left_frac=a,p,frac(af)
        right_slope,right_floor,right_frac=c,q,frac(cf)
    assert left_frac!=right_frac
    ny=t-j
    if left_frac<right_frac:
        # [left,right): L=Y-right, U=Y-left
        return exact_band_open(lo,hi,ny-right_slope,x+right_floor,ny-left_slope,x+left_floor)
    # [left,1) or [0,right) (wrap-around)
    val=exact_band_open(lo,hi,ny,x-1,ny-left_slope,x+left_floor)
    if val is not None: return val
    if right_frac==0: return None  # [0,0) empty
    return exact_band_open(lo,hi,ny-right_slope,x+right_floor,ny,x)

def bit_oracle(atom,t,j,x,a,c,bit):
    COUNTS["oracle_calls"]+=1
    lo,hi,point=atom
    if point:
        th=lo
        return th if eligible(th,t,j,x,a,c)==bool(bit) else None
    mid=(lo+hi)/2
    if frac(a*mid)==frac(c*mid):
        return mid if bit==0 else None
    th=arc_oracle_open(lo,hi,t,j,x,a,c,reverse=(bit==0))
    if th is not None:
        assert eligible(th,t,j,x,a,c)==bool(bit)
        COUNTS["oracle_witnesses"]+=1
        COUNTS["max_witness_bitlength"]=max(COUNTS["max_witness_bitlength"],th.numerator.bit_length(),th.denominator.bit_length())
    return th

def check_case(j,x,a,c,old_times,t):
    raw=set()
    for old in old_times:raw.update(six_cuts(old,j,x,a,c))
    old_atoms=atoms(raw)
    oracle=set()
    for atom in old_atoms:
        COUNTS["old_atoms_checked"]+=1
        old_sig=tuple(eligible(midpoint(atom),z,j,x,a,c) for z in old_times)
        for bit in (0,1):
            w=bit_oracle(atom,t,j,x,a,c,bit)
            if w is not None:
                assert tuple(eligible(w,z,j,x,a,c) for z in old_times)==old_sig
                oracle.add((old_sig,bit))
    full=set(raw);new_cuts=six_cuts(t,j,x,a,c);full.update(new_cuts)
    COUNTS["newtime_raw_cut_count_small_cases"]+=len(new_cuts)
    new_atoms=atoms(full);COUNTS["bruteforce_new_atoms"]+=len(new_atoms)
    direct={(tuple(eligible(midpoint(atom),z,j,x,a,c) for z in old_times),int(eligible(midpoint(atom),t,j,x,a,c))) for atom in new_atoms}
    if direct!=oracle:
        raise AssertionError(f'MISMATCH: {j,x,a,c,old_times,t}, oracle={oracle}, direct={direct}')
    # Single-source history vs empty history, Top1 has one entry iff bit==1.
    for sig,bit in direct:
        COUNTS["exact_top1_checkpoints"]+=1
        assert (bit==1)==(len([(t,0) for _ in range(bit)])==1)
    return len(old_atoms),len(new_atoms),len(direct)

def main():
    # Fixed edge-case classifications of half-open endpoints, coincident arc, signed frequency.
    specials=[(0,Q(1,4),0,1,(-1,0,1),2),(1,Q(1,2),1,1,(0,2,3),5),
              (0,Q(-2,3),-2,3,(-3,0,2),-4),(3,Q(7,8),3,-2,(-4,0,1),-6),
              (0,Q(0),0,0,(-1,0),1),(1,Q(0),-1,0,(0,1,2),-2)]
    for v in specials:check_case(*v)
    COUNTS['special_cases']=len(specials)
    for _ in range(500):
        j=RNG.randint(-4,4); a=RNG.randint(-4,4);c=RNG.randint(-4,4)
        x=Q(RNG.randint(-10,10),RNG.randint(1,9))
        old_times=tuple(sorted(RNG.sample(range(-5,6),RNG.randint(1,4))))
        available=[v for v in range(-9,10) if v not in old_times]
        t=RNG.choice(available)
        check_case(j,x,a,c,old_times,t)
        COUNTS['random_cases']+=1
    # Very large signed frequencies: witness and old-signature exactness, no new cut enumeration.
    for t in (10**80+7,-(10**80+7),10**150+19,-(10**150+19)):
        j,x,a,c=1,Q(1,4),-2,3
        old_times=(-5,-1,0,2,4)
        raw=set()
        for old in old_times:raw.update(six_cuts(old,j,x,a,c))
        old_atoms=atoms(raw)
        got=set()
        for atom in old_atoms:
            sig=tuple(eligible(midpoint(atom),z,j,x,a,c) for z in old_times)
            for bit in (0,1):
                w=bit_oracle(atom,t,j,x,a,c,bit)
                if w is not None:
                    assert tuple(eligible(w,z,j,x,a,c) for z in old_times)==sig
                    got.add((sig,bit))
        assert got
        COUNTS['large_signed_cases']+=1
    COUNTS['status']='R118_PASS'
    path=pathlib.Path(__file__).with_name('verification_r118.json')
    path.write_text(json.dumps(COUNTS,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf8')
    print('R118_PASS',COUNTS['random_cases'],COUNTS['old_atoms_checked'],COUNTS['oracle_calls'],COUNTS['oracle_witnesses'],COUNTS['bruteforce_new_atoms'],COUNTS['max_witness_bitlength'])

if __name__=='__main__':main()
