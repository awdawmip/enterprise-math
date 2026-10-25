#!/usr/bin/env python3
"""C299 exact 125-strip structural pole-cancellation proof, stdlib only.
Run beside frozen C275/C284/C288/C293 and C298 factorization helper.
Model: positive 79-node rational auxiliary, not native signed BRC.
"""
from collections import Counter
from fractions import Fraction as F
from math import lcm
from pathlib import Path
import hashlib, json
from C298_SHARED_DENOMINATOR_EXACT import make_terms, primitive_factor
from C297_UNIFORM_WIDTH_AND_HEIGHT_EXACT import poly_eval
import C275_STANDALONE_EXACT_REPLAY as original
import C288_ISOLATING_BOXES_EXACT as paths_source

BASE=Path(__file__).resolve().parent
def make_certificate():
    raw=json.loads((BASE/'C293_125_REFINED_BRACKETS.json').read_text())
    canon=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    assert hashlib.sha256(canon(raw['records'])).hexdigest()==raw['records_sha256']
    paths,_=paths_source.build_paths()
    W,_=original.floor_fixed_masses()
    assert len(paths)==len(raw['records'])==125
    out=[];residue_tests=0
    for i,(r,path) in enumerate(zip(raw['records'],paths)):
        assert r[0]==i
        a=F(int(r[1]),1<<24);b=a+F(1,1<<24)
        terms=make_terms(path,a,b,W)
        assert len(terms)==79
        groups=Counter();scalars=[];own_counts=[]
        for coeff,factors in terms:
            own=Counter();scalar=coeff.denominator
            for n,d in factors:
                content,q=primitive_factor(d)
                scalar*=content;own[q]+=1
            for q,e in own.items():groups[q]=max(groups[q],e)
            scalars.append(scalar);own_counts.append(own)
        S=lcm(*scalars);degree=sum((len(q)-1)*e for q,e in groups.items())
        M=S
        for q,e in groups.items():M*=sum(abs(x) for x in q)**e
        oldH=M.bit_length()
        qs={}
        for k,m,label in ((0,2,'02'),(1,3,'13')):
            gap_idx=1+75+[x for x in range(4) if x!=k].index(m)
            _,gap_denom=terms[75+k][1][gap_idx]
            _,q=primitive_factor(gap_denom)
            assert len(q)==2 and q[1]!=0 and groups[q]==1
            qs[label]=q
            t0=-F(q[0],q[1])
            contributors=[j for j,c in enumerate(own_counts) if c[q]]
            assert contributors==[75+k,75+m],(i,label,contributors)
            for key in groups:
                if key!=q:assert poly_eval(key,t0)!=0,(i,label,key)
            residues=[]
            for j in contributors:
                coeff,factors=terms[j]
                value=coeff
                for num,den in factors:
                    c,key=primitive_factor(den)
                    value*=poly_eval(num,t0)
                    if key==q:value/=c
                    else:
                        denvalue=poly_eval(den,t0)
                        assert denvalue!=0
                        value/=denvalue
                assert value!=0
                residues.append(value)
            assert residues[0]+residues[1]==0,(i,label)
            residue_tests+=1
        q02=qs['02'];q13=qs['13']
        assert q02!=q13
        divided_norm=sum(map(abs,q02))*sum(map(abs,q13))
        assert M%divided_norm==0
        Mred=M//divided_norm
        newdeg=degree-2;newH=Mred.bit_length()
        assert newdeg>=0 and newH<=13713
        out.append({'path':i,'shared_D_degree':degree,
            'cancelled_pole_factors':{'pair_02':list(q02),'pair_13':list(q13)},
            'certified_integral_denominator_degree':newdeg,
            'shared_height_bit_bound':oldH,'reduced_height_bit_bound':newH,
            'exact_residue_cancellations':2})
    degrees=Counter(str(x['certified_integral_denominator_degree']) for x in out)
    assert degrees==Counter({'352':124,'265':1})
    assert max(x['reduced_height_bit_bound'] for x in out)==13713
    audit={'schema':'EM_C299_TWO_MOVING_POLE_CANCELLATIONS_V1',
      'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
      'source_C293_records_sha256':raw['records_sha256'],
      'source_C284_records_sha256':paths_source.SOURCE_CERT_SHA,
      'path_count':125,'exact_rational_residue_checks':residue_tests,
      'distinct_nonconstant_coprime_linear_factors_per_path':2,
      'certified_integral_denominator_degree_histogram':dict(sorted(degrees.items())),
      'uniform_degree_upper_bound':352,
      'uniform_reduced_denominator_height_bit_bound':13713,
      'uniform_nonroot_dyadic_sign_precision':'P=352*b+13713+134',
      'precision_at_b512':352*512+13713+134,
      'old_C298_precision_at_b512':354*512+13799+134,
      'source_semantics':'AUTHOR EXACT; C297 continuous width inherited; NOT native BRC; NOT admitted'}
    (BASE/'C299_125_TWO_POLE_PATHWISE.json').write_text(json.dumps({'audit':audit,'rows':out},indent=2,sort_keys=True,ensure_ascii=False)+'\n')
    (BASE/'C299_AUTHOR_EXACT_AUDIT_20261025.json').write_text(json.dumps(audit,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
    print('C299_125_TWO_POLE_CANCELLATIONS_EXACT_PASS',json.dumps(audit,sort_keys=True))
if __name__=='__main__':make_certificate()
