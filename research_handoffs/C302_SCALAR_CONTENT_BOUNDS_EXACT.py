#!/usr/bin/env python3
"""C302: certified common INTEGER scalar cancellation for the 79-branch auxiliary model.

Author-level exact arithmetic. Unlike a formal primitive-pair certificate, this
computes a proved common scalar divisor, not the full numerator content.
Input: frozen C275/C288/C293/C298/C300/C301 source materials. Stdlib only.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
import json, hashlib
import C300_RESIDUE_KERNEL as residue
import C298_SHARED_DENOMINATOR_EXACT as base
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as src
from C301_STRIP_ADAPTIVE_HEIGHT_EXACT import bound_bit_length

def exact_monotone_bound(path,k24,scalar,group,cancel):
    lo,hi=F(k24,1<<24),F(k24+1,1<<24)
    U=F(scalar)
    for q,m in group.items():
        if q in cancel:continue
        assert len(q) in (1,2,13)
        a,b=base.poly_eval(q,lo),base.poly_eval(q,hi)
        assert a>0 and b>0
        # linear or frozen C301 positive-base-factor monotonicity.
        U*=max(a,b)**m
    return U

def perform():
    paths,_=c288.build_paths(); W,_=src.floor_fixed_masses()
    raw=json.loads(Path('C293_125_REFINED_BRACKETS.json').read_text())['records']
    old=json.loads(Path('C301_AUTHOR_EXACT_AUDIT_20261025.json').read_text())['paths']
    c300=json.loads(Path('C300_AUTHOR_AUDIT_20261025.json').read_text())['path_rows']
    assert len(paths)==len(raw)==len(old)==len(c300)==125
    rows=[]
    for i,(path,row,prior,pr300) in enumerate(zip(paths,raw,old,c300)):
        assert i==row[0]==prior['index']==pr300['index']
        k=int(row[1]);lo=F(k,1<<24);hi=F(k+1,1<<24)
        groups,occ,terms,scales=residue.prepare_terms(path,lo,hi,W)
        scalar=lcm(*scales)
        assert scalar.bit_length()==prior['shared_denominator_scalar_content_bits']
        # C300's exact cancellation criterion, not modular-zero-only evidence.
        cancel={q for q in groups if len(q)==2 and set(occ[q]) in ({75,77},{76,78})}
        assert len(cancel)==2 and all(groups[q]==1 for q in cancel)
        deg=sum((len(q)-1)*e for q,e in groups.items())-2
        assert deg==pr300['reduced_degree']==prior['degree']
        # Structural Gauss-lemma bound: content(prod f) = prod content(f).
        each=[]
        for (num,den,nums,facs),d in zip(terms,scales):
            assert den==d
            t=abs((scalar//d)*num)
            for n in nums:
                assert all(isinstance(c,int) for c in n)
                t*=gcd(*(abs(z) for z in n))
            each.append(t)
        L=gcd(scalar,*each)
        assert L>1 and scalar%L==0
        # Exactly compute A_full(0) mod s, an upper bound on true content gcd.
        a0=0
        for (num,_,nums,facs),d in zip(terms,scales):
            val=((scalar//d)*num)%scalar
            if not val:continue
            for n in nums:val=val*n[0]%scalar
            if not val:continue
            exp=Counter(facs)
            for q,e in groups.items():
                r=e-exp[q]
                if r:val=val*pow(q[0],r,scalar)%scalar
                if not val:break
            a0=(a0+val)%scalar
        coeffs=[a0]
        upper=gcd(scalar,a0)
        assert upper%L==0,(i,upper,L)
        # Strict continuous upper denominator bound, inherited factor monotonicity.
        U=exact_monotone_bound(path,k,scalar,groups,cancel)
        assert bound_bit_length(U)==prior['adaptive_strip_height_bits']
        Hnew=bound_bit_length(U/L)
        assert Hnew < prior['adaptive_strip_height_bits']
        rows.append({
            'index':i,'degree':deg,'scalar_bits':scalar.bit_length(),
            'certified_common_scalar_divisor_decimal':str(L),
            'certified_scalar_divisor_bits':L.bit_length(),
            'upper_content_gcd_from_constant_term_decimal':str(upper),
            'upper_content_gcd_bits':upper.bit_length(),
            'content_divisor_relation_checked':upper%L==0,
            'old_strip_height_bits':prior['adaptive_strip_height_bits'],
            'certified_new_strip_height_bits':Hnew,
            'saved_sufficient_precision_bits':prior['adaptive_strip_height_bits']-Hnew,
            'constant_numerator_residue_mod_scalar_sha256':hashlib.sha256(('\n'.join(map(str,coeffs))+'\n').encode()).hexdigest(),
        })
        if i%25==0:print('C302_PATH',i,'L bits',L.bit_length(),'new H',Hnew,'gain',prior['adaptive_strip_height_bits']-Hnew,flush=True)
    global_old=max(r['old_strip_height_bits'] for r in rows)
    global_new=max(r['certified_new_strip_height_bits'] for r in rows)
    special=next(r for r in rows if r['index']==28)
    summary={
      'schema':'EM_C302_CERTIFIED_SCALAR_NORMALIZATION_V1',
      'scope':'125 frozen C293 positive-rational 79-branch auxiliary paths; NOT native GF(2)-BRC or X6',
      'paths':len(rows),'all_common_scalar_divisors_verified':True,
      'minimum_common_divisor_bitwidth':min(r['certified_scalar_divisor_bits'] for r in rows),
      'maximum_common_divisor_bitwidth':max(r['certified_scalar_divisor_bits'] for r in rows),
      'min_per_path_strip_precision_gain':min(r['saved_sufficient_precision_bits'] for r in rows),
      'max_per_path_strip_precision_gain':max(r['saved_sufficient_precision_bits'] for r in rows),
      'old_global_strip_height_bits':global_old,'new_global_strip_height_bits':global_new,
      'max_new_height_paths':[r['index'] for r in rows if r['certified_new_strip_height_bits']==global_new],
      'old_global_precision_at_b512':352*512+global_old+134,
      'new_global_precision_at_b512':352*512+global_new+134,
      'special_28_precision_at_b512':265*512+special['certified_new_strip_height_bits']+134,
      'scalar_gcd_exactness':'lower divisor proved; full shared scalar gcd not yet determined',
      'upper_content_gcd_semantics':'gcd(s,A_full(0)), so true gcd divides this; exact over Z',
      'dependency':'C300 primitive double-linear cancellation; C301 monotonic-factor strip bound; C297 outward width < 2^(134-P)',
      'author_validation_only':True,'formal_claim':False,'native_transfer':False,
    }
    out={'summary':summary,'rows':rows}
    Path('C302_125_SCALAR_NORMALIZATION_CERTIFICATE.json').write_text(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
    Path('C302_AUTHOR_EXACT_AUDIT_20261025.json').write_text(json.dumps(summary,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
    print('C302_CERTIFIED_SCALAR_NORMALIZATION_PASS',json.dumps(summary,sort_keys=True),flush=True)
    return out

if __name__=='__main__':perform()
