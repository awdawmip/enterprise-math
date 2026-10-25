#!/usr/bin/env python3
"""C294: exact 125-point perturbed Newton certificate over C293 frozen inputs.

The unconditional finite statements here are rational arithmetic on 125 fully
specified perturbed inputs. Uniform continuum claims in the companion proof are
conditional on the pinned C290 and C292 author-level full-box certificates.
"""
from fractions import Fraction as R
import json, hashlib
import C293_AUTHOR_VERIFY_EXACT as c293
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as src
import C290_PADDED_CHART_EXACT as c290

H=R(1,2**32)
R0=R(1,2**29)
R_PERT=R(1,2**28)
PAD=R(1,2**26)
M=R(6,5)
MM=R(21,10)
C=R(2125,6)

class Dual:
    __slots__=("v","d")
    def __init__(self,v,d=0):self.v=R(v);self.d=R(d)
    @staticmethod
    def cv(x):return x if isinstance(x,Dual) else Dual(x)
    def __add__(self,o):
        o=self.cv(o);return Dual(self.v+o.v,self.d+o.d)
    __radd__=__add__
    def __neg__(self):return Dual(-self.v,-self.d)
    def __sub__(self,o):return self+-self.cv(o)
    def __rsub__(self,o):return self.cv(o)+-self
    def __mul__(self,o):
        o=self.cv(o);return Dual(self.v*o.v,self.d*o.v+self.v*o.d)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.cv(o);assert o.v
        return Dual(self.v/o.v,(self.d*o.v-self.v*o.d)/(o.v*o.v))
    def __rtruediv__(self,o):return self.cv(o)/self
    def __pow__(self,k):
        assert isinstance(k,int)
        if k<0:return Dual(1)/self**(-k)
        if k==0:return Dual(1)
        return Dual(self.v**k,k*self.v**(k-1)*self.d)
    def __abs__(self):
        assert self.v!=0
        return self if self.v>0 else -self

def direction(i):
    # Exercise all 16 sign corners in successive 16 paths. Order: x5,x50,x56,tau.
    return tuple(1 if i & (1<<j) else -1 for j in range(4))

def point(i,p,k):
    mid=R(2*k+1,2**25)
    v0=c293.at(p,mid)
    bits=direction(i)
    v=(v0[0]+bits[0]*H,v0[1]+bits[1]*H,v0[2],v0[3]+bits[2]*H)
    target=R(1)+bits[3]*H
    return v0,v,target

def check():
    paths,_=c288.build_paths()
    records,source_cert=c293.load_certificate()
    W,_=src.floor_fixed_masses()
    assert len(paths)==len(records)==125
    # All domain-independent constants are checked by exact rational arithmetic.
    assert R(19,3)*H<R0
    assert 2*R0==R_PERT and 2*R_PERT==PAD/2
    assert C*R_PERT<R(1,2**19)
    assert R(16630,3)*R0**2<R(1,2**45)
    assert R(6,5)*R0>R(38,5)*H
    assert R(670)>0 and R(3326)>0
    patterns=set()
    rows=[]
    normalized_residual_max=R(0)
    normal_slope_min=None
    normal_slope_max=None
    for i,(p,(idx,k)) in enumerate(zip(paths,records)):
        assert idx==i
        v0,v,target=point(i,p,k)
        assert src.valid(v) and src.valid(v0)
        assert all(p['box'][t][0]-PAD<v[t]<p['box'][t][1]+PAD for t in range(4))
        assert abs(target-1)==H
        pattern=direction(i);patterns.add(pattern)
        vv=tuple(Dual(x,1 if j==2 else 0) for j,x in enumerate(v))
        yd=src.original_F(vv,W)
        assert isinstance(yd,Dual)
        f=yd.v/src.Q; fy=yd.d/src.Q
        assert fy>M and fy<MM
        # Compare independent product-rule dual differentiation against the
        # exact positive-branch log-gradient identity at one degenerate box.
        singleton=tuple((x,x) for x in v)
        df_check=sum((c290.branch_at_midpoint(j,v,W)*
                      c290.log_grad_bounds(j,singleton)[2][0]
                      for j in range(79)),R(0))/src.Q
        assert df_check==fy
        residual=f-target
        assert abs(residual)<M*R_PERT
        y0=v[2]
        n1=y0-residual/fy
        assert abs(n1-y0)<R_PERT
        v1=(v[0],v[1],n1,v[3])
        assert src.valid(v1)
        assert all(p['box'][t][0]-PAD<v1[t]<p['box'][t][1]+PAD for t in range(4))
        # The full-box convexity theorem (C292) implies N1 is strictly to the
        # right of the unique root, except when the rational initial value is
        # already exact. We do not claim direct evaluation of F(N1) here:
        # the rational first Newton iterate can have enormous coefficients.
        # The following are exact new finite computations at the initial point.
        normal_slope_min=fy if normal_slope_min is None else min(normal_slope_min,fy)
        normal_slope_max=fy if normal_slope_max is None else max(normal_slope_max,fy)
        normalized_residual_max=max(normalized_residual_max,abs(residual))
        body=f'{i}|{k}|{pattern}|{residual.numerator:x}/{residual.denominator:x}|{fy.numerator:x}/{fy.denominator:x}|{n1.numerator:x}/{n1.denominator:x}'
        rows.append({'index':i,'K':k,'signs':list(pattern),
                     'initial_residual_sign':'POSITIVE' if residual>0 else ('NEGATIVE' if residual<0 else 'ZERO'),
                     'exact_initial_residual_lt_m_over_2_to_28':True,
                     'normal_derivative_within_6over5_and_21over10':True,
                     'normal_Newton_first_step_within_2_to_minus_28':True,
                     'exact_record_sha256':hashlib.sha256(body.encode()).hexdigest()})
    assert len(patterns)==16
    audit={
        'schema':'EM_C294_AUTHOR_PARAMETRIC_NEWTON_V1',
        'statement_kind':'FINITE_EXACT_PLUS_CONDITIONAL_FULL_BOX_THEOREM',
        'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
        'upstream_sources':['C293_125_REFINED_BRACKETS.json',
                            'C288_ISOLATING_BOXES_EXACT.py',
                            'C275_STANDALONE_EXACT_REPLAY.py',
                            'C290_PADDED_CHART_EXACT.py',
                            'C292_AUTHOR_THEOREM_AND_PROOF_20261025.md'],
        'path_count':len(rows),'distinct_sign_patterns':len(patterns),
        'perturbation_bound_per_coordinate':'1/4294967296',
        'level_perturbation_bound':'1/4294967296',
        'normal_base_root_error_lt':'2^-29',
        'perturbed_normal_root_shift_lt':'2^-29',
        'rational_start_root_error_lt':'2^-28',
        'newton_error_n_bound':'2^-28 * (2^-19)^(2^n-1)',
        'hessian_upper_2norm_conditional':'3326',
        'linear_response_second_order_error_lt':'2^-45',
        'exact_perturbed_normal_derivative_checks':len(rows),
        'independent_dual_vs_log_identity_checks':len(rows),
        'exact_first_Newton_iterates_constructed':len(rows),
        'post_Newton_overshoot':'CONDITIONAL_ON_C292_STRICT_CONVEXITY_NOT_DIRECT_F_AT_NEWTON',
        'C292_entire_box_hypotheses_replayed_this_run':False,
        'formal_Source_result':False,'independent_Driver_review':False,
        'record_count':len(rows),
        'initial_residual_sign_counts':{t:sum(r['initial_residual_sign']==t for r in rows) for t in ('POSITIVE','NEGATIVE','ZERO')},
        'record_digest':hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        'records':rows
    }
    with open('C294_AUTHOR_EXACT_AUDIT_20261025.json','w',encoding='utf-8') as fh:
        json.dump(audit,fh,indent=2,ensure_ascii=False,sort_keys=True);fh.write('\n')
    print('C294_AUTHOR_PARAMETRIC_NEWTON_EXACT_PASS',len(rows),'patterns',len(patterns),
          'max_initial_residual<2^-28*m:',normalized_residual_max<M*R_PERT,
          'slopes in',float(normal_slope_min),float(normal_slope_max),flush=True)
    return audit

if __name__=='__main__':check()
