#!/usr/bin/env python3
"""C290 author-level exact, reproducible padded-chart certificate for 125 roots.

Input: frozen C275 rational auxiliary model, C284 dyadic root brackets,
C288 path identities / rational isolating boxes. No Source admission.
All theorem-decisive tests use stdlib Fraction and exhaustive 79-branch
interval calculations; floating point appears only in optional reporting.
"""
from fractions import Fraction as R
from itertools import combinations
import hashlib
import json

import C275_STANDALONE_EXACT_REPLAY as s
import C288_ISOLATING_BOXES_EXACT as c288

Z=R(0)
O=R(1)
Q=R(s.Q)
PAD=R(1,2**26)
E_LEVEL=R(1,2**28)

def box(a,b=None):
    if b is None:b=a
    assert R(a)<=R(b)
    return (R(a),R(b))

def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def minus(a,b):return plus(a,neg(b))
def scale(a,k):return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
def reciprocal(a):
    assert a[0]*a[1]>0,('pole',a)
    return 1/a[1],1/a[0]
def mm(a):return max(abs(a[0]),abs(a[1]))

def moving_kernel(p):
    """6p[(2-p^2)^-1+(3-p^2)^-1] is increasing for 0<p<1."""
    assert 0<p[0]<=p[1]<1
    def f(x):return 6*x*(1/(2-x*x)+1/(3-x*x))
    return box(f(p[0]),f(p[1]))

def log_grad_bounds(j,B):
    """Four exact rational enclosures of every partial of log M_j.

    Fixed j: ∂k log M_j=-1/(Z-v_k)+1/(U_j-v_k).
    Moving active i: ∂i log M_i=6p[(2-p²)^-1+(3-p²)^-1]
                 -sum_fixed 1/(p-U_j)-sum_(k!=i) 1/(p-v_k)
    and ∂k log M_i=-1/(Z-v_k)+1/(p-v_k), k!=i.
    """
    out=[box(Z) for _ in range(4)]
    if j in s.J:
        for k in range(4):
            out[k]=plus(neg(reciprocal(minus(box(s.Z),B[k]))),
                        reciprocal(minus(box(s.U[j]),B[k])))
    else:
        i=s.I.index(j)
        p=B[i]
        out[i]=moving_kernel(p)
        for h in s.J:
            out[i]=minus(out[i],reciprocal(minus(p,box(s.U[h]))))
        for k in range(4):
            if k==i:continue
            d=reciprocal(minus(p,B[k]))
            out[i]=minus(out[i],d)
            out[k]=plus(neg(reciprocal(minus(box(s.Z),B[k]))),d)
    return tuple(out)

def branch_at_midpoint(j,mid,W):
    if j in s.J:return R(W[j])*s.fixed_multiplier(j,mid)
    return s.moving_mass(j,mid)

def partial_interval(B,W):
    """Enclose 4D ∇F on an entire convex box via rational log derivative.

    The mass enclosure uses exp(-rho)>=1-rho and
    exp(rho)<=1/(1-rho) for 0<=rho<1. Each rho controls
    log M_j(v)-log M_j(mid) on every straight segment in B.
    """
    c=tuple((a+b)/2 for a,b in B)
    hw=tuple((b-a)/2 for a,b in B)
    dl=[Z]*4; du=[Z]*4
    maxrho=Z
    for j in range(79):
        lg=log_grad_bounds(j,B)
        rho=sum(mm(lg[k])*hw[k] for k in range(4))
        assert Z<=rho<O,(j,'rho greater than 1',rho)
        maxrho=max(maxrho,rho)
        m=branch_at_midpoint(j,c,W)
        assert m>0
        masslo=m*(O-rho)
        masshi=m/(O-rho)
        for k,(lo,hi) in enumerate(lg):
            dl[k]+= (masslo if lo>=0 else masshi)*lo
            du[k]+= (masshi if hi>=0 else masslo)*hi
    return tuple(zip(dl,du)),maxrho

def pair_gap(B,C):
    return max(max(Z,lo-hi2,lo2-hi) for (lo,hi),(lo2,hi2) in zip(B,C))

def check():
    paths,_=c288.build_paths() # same C284 immutable certificate digest
    W,_=s.floor_fixed_masses()
    assert len(paths)==125
    margins=[]; padded=[]; stats=[]
    minsep=None; maxrho=Z
    for idx,p in enumerate(paths):
        base=p['box'];B=tuple((lo-PAD,hi+PAD) for lo,hi in base)
        for k in range(4):
            assert s.U[s.I[k]-1]<B[k][0]<B[k][1]<s.U[s.I[k]+1]
            assert B[k][1]<s.Z
        for k in range(3):
            sep=B[k+1][0]-B[k][1]
            assert sep>0
            minsep=sep if minsep is None else min(sep,minsep)
        # Endpoint witnesses for full C289 level band, no reliance on floating point.
        a,b=R(p['k'],4096),R(p['k']+1,4096)
        v0=tuple(w+a*d for w,d in zip(p['w'],p['d']))
        v1=tuple(w+b*d for w,d in zip(p['w'],p['d']))
        assert all(base[k][0]<=v0[k]<=base[k][1] and
                   base[k][0]<=v1[k]<=base[k][1] for k in range(4))
        left=(Q-s.original_F(v0,W))/Q
        right=(s.original_F(v1,W)-Q)/Q
        assert left>E_LEVEL and right>E_LEVEL
        margins.extend([left,right])
        L,rho=partial_interval(B,W)
        maxrho=max(maxrho,rho)
        # Full *four-dimensional* padded box, not just the root line.
        assert L[2][0]>R(6,5)*Q,('v55 normal lower',idx)
        assert Z<L[2][0]<=L[2][1]<R(21,10)*Q
        assert R(1,3)*Q<L[0][0]<=L[0][1]<3*Q
        assert -2*Q<L[1][0]<=L[1][1]<2*Q
        assert -R(8,5)*Q<L[3][0]<=L[3][1]<-R(1,16)*Q
        # Even independent coordinate extrema enclose the line derivative.
        D=sum((L[k][0] if d>=0 else L[k][1])*d for k,d in enumerate(p['d']))
        assert D>Q/56,('directional lower',idx)
        stats.append({'i':idx,'rho':rho,'d_lower':D/Q,
                      'dv5_lower':L[0][0]/Q,'dv5_upper':L[0][1]/Q,
                      'dv50_lower':L[1][0]/Q,'dv50_upper':L[1][1]/Q,
                      'dv55_lower':L[2][0]/Q,'dv55_upper':L[2][1]/Q,
                      'dv56_lower':L[3][0]/Q,'dv56_upper':L[3][1]/Q})
        padded.append(B)
    assert len(stats)==125
    min_gap=None; winner=None
    for i,j in combinations(range(125),2):
        g=pair_gap(padded[i],padded[j])
        assert g>R(1,2**23)
        if min_gap is None or g<min_gap:min_gap=g;winner=(i,j)
    assert winner==(34,59)
    expected=R(518383,3360752136192)-2*PAD
    assert min_gap==expected
    assert maxrho<R(1,1000)
    # Stronger coordinate-wise estimates give quantitative local charts:
    # |Δv55| < (5/6)(|Δq|/Q +3|Δv5|+2|Δv50|+8/5|Δv56|).
    # Choose independent parameter perturbations |Δx_k|<=PAD/20,
    # |Δq|<=Q*PAD/5. Then normal displacement <= 53 PAD / 120 < PAD/2.
    assert (R(5,6)*(R(1,5)+(3+2+R(8,5))/20))<R(1,2)
    # Extra width: each original box including any degenerate coordinate is
    # strictly PAD-separated from all boundary facets of the padded box.
    out={
      'schema':'EM_C290_PADDED_FULL_4D_RATIONAL_CHARTS_AUTHOR_EXACT_V1',
      'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
      'n_node_branches':79,'n_paths_and_padded_boxes':len(stats),
      'n_endpoint_checks':len(margins), 'n_padded_pair_checks':7750,
      'uniform_pad':str(PAD),
      'normal_v55_full_padded_box':'dF/dv55 > (6/5)*Q (exact)',
      'other_derivative_full_padded_box':{
        'v5':'Q/3 < dF/dv5 < 3Q','v50':'-2Q < dF/dv50 < 2Q',
        'v56':'-8Q/5 < dF/dv56 < -Q/16'},
      'uniform_transverse_line_derivative':'grad F dot d > Q/56',
      'minimum_padded_pair_gap':str(min_gap),
      'gap_gt':'1/8388608',
      'max_log_mass_radius_lt':'1/1000',
      'min_dv55_lower_gt_6Q_5':True,
      'min_dv5_lower_gt_Q_3':True,
      'max_dv56_upper_lt_negative_Q_16':True,
      'local_base_perturbation_inf_radius':str(PAD/20),
      'local_threshold_change_radius_in_Q_units':str(PAD/5),
      'local_normal_search_radius':str(PAD/2),
      'local_unique_normal_coordinate':'v55 (third entry of four-dimensional auxiliary)',
      'local_lipschitz_v55_bound':'(5/6)*(|delta_q|/Q+3|delta_v5|+2|delta_v50|+(8/5)|delta_v56|)',
      'minimum_end_margin_approx_info_only':format(float(min(margins)),'.15g'),
      'minimum_dv55_lower_over_Q_approx_info_only':format(float(min(a['dv55_lower'] for a in stats)),'.15g'),
      'maximum_rho_approx_info_only':format(float(maxrho),'.15g'),
      'all_decisive_inequalities_exact':True,
      'formal_Source_claim':False,'driver_accepted':False,'native_X6_BRC_transfer':False,
      'upstream':'C275 frozen source and C284 certificate from C289 portable package, C288 paths',
    }
    with open('C290_AUTHOR_EXACT_AUDIT_20261025.json','w',encoding='utf-8') as f:
        json.dump(out,f,ensure_ascii=False,indent=2,sort_keys=True)
        f.write('\n')
    print('C290_PADDED_FULL_4D_CHARTS_EXACT_PASS 125 boxes 250 endpoint checks 7750 pair checks')
    print('min padded gap:',min_gap,' vs 2^-23:',min_gap>R(1,2**23))
    print('min dF/dv55 lower/Q ~',out['minimum_dv55_lower_over_Q_approx_info_only'],'maxrho ~',out['maximum_rho_approx_info_only'])
    print('local chart radii triple',PAD/20, 'q/Q',PAD/5,'normal',PAD/2)
    return out

if __name__=='__main__':check()
