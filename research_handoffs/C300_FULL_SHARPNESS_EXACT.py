#!/usr/bin/env python3
"""C300: exact reduced-denominator degree for 125 frozen C195/H168 paths.
(i) exact rational residue for cancelled linear factors;
(ii) certified-prime modular nonzero residue for every retained linear factor;
(iii) algebraic irreducibility/noncancellation of moving-base quadratics.
Author-only source; no native BRC transfer or Source claim.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter,defaultdict
import json,gzip,base64,hashlib
import C298_SHARED_DENOMINATOR_EXACT as base
import C300_RESIDUE_KERNEL as residues
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as src

P=residues.PRIMES[0]
assert P==2305843009213693951
assert all(61%d for d in range(2,8))
x=4
for _ in range(59): x=(x*x-2)%P
assert x==0, "Lucas-Lehmer Mersenne-prime witness failed"

def canonical(o): return json.dumps(o,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')

def run():
    ref=json.loads(Path('C293_125_REFINED_BRACKETS.json').read_text())
    paths,_=c288.build_paths()
    W,_=src.floor_fixed_masses()
    assert len(paths)==len(ref['records'])==125
    certrows=[];summaries=[]
    checks={'linear_nonzero_modular':0,'linear_zero_exact':0,'moving_base_irreducible_quadratics':0,'finite_fraction_spots':0,'exact_nonzero_residue_spots':0}
    for i,(p,rec) in enumerate(zip(paths,ref['records'])):
        assert rec[0]==i
        lo=Fraction(rec[1],1<<24);hi=Fraction(rec[1]+1,1<<24)
        g,occ,terms,scales=residues.prepare_terms(p,lo,hi,W)
        linear=sorted(q for q in g if len(q)==2)
        assert all(g[q]==1 for q in linear)
        nonlinear={q:e for q,e in g.items() if len(q)>2}
        active=sum(d!=0 for d in p['d'])
        assert len(nonlinear)==active
        assert all(len(q)==13 and e==1 for q,e in nonlinear.items())
        # Algebraic argument in proof: for nonconstant affine x(t),
        # 2-x(t)^2 and 3-x(t)^2 are irreducible quadratics.
        # Distinct moving x slots have no shared quadratic factors.
        for a,(w,d) in enumerate(zip(p['w'],p['d'])):
            if d==0:continue
            for b,(wm,dm) in enumerate(zip(p['w'],p['d'])):
                if a==b or dm==0:continue
                assert not (w==wm and d==dm)
                assert not (w==-wm and d==-dm)
            checks['moving_base_irreducible_quadratics']+=2
        witnesses=[]; cancel=[]
        for q in linear:
            obj=residues.witness(q,g,occ[q],terms,scales,P)
            assert obj is not None,(i,q,'bad modular witness')
            if obj['residue']:
                witnesses.append([q[0],q[1],int(obj['residue'])])
                checks['linear_nonzero_modular']+=1
            else:
                is_zero,rs=residues.exact_residue_zero(q,occ[q],terms)
                assert is_zero and rs==0,(i,q,rs)
                cancel.append([q[0],q[1],list(occ[q])])
                checks['linear_zero_exact']+=1
        assert len(cancel)==2 and sorted(tuple(z[2]) for z in cancel)==[(75,77),(76,78)]
        if i in (0,8,28,40,64,96,124):
            for q0,q1,rem in (witnesses[0],witnesses[-1]):
                q=(q0,q1)
                is_zero,R=residues.exact_residue_zero(q,occ[q],terms)
                assert not is_zero and R.denominator%P!=0
                assert R.numerator * pow(R.denominator,-1,P)%P==rem
                checks['exact_nonzero_residue_spots']+=1
        d0=sum((len(q)-1)*m for q,m in g.items())
        d_red=len(witnesses)+12*active
        scalar,base_groups=base.certificate_one(i,p,int(rec[1]),W)[1]
        assert base_groups==g
        cancelled={tuple(z[:2]) for z in cancel}
        M_red=scalar
        for q,exponent in g.items():
            if q in cancelled:
                assert exponent==1
                assert base.poly_eval(q,lo)>0 and base.poly_eval(q,hi)>0
                continue
            M_red*=sum(map(abs,q))**exponent
        H_red=M_red.bit_length()
        assert M_red < 1<<H_red
        assert d_red==d0-len(cancel)
        certrows.append([i,witnesses,[[z[0],z[1]] for z in cancel]])
        summaries.append({'index':i,'unreduced_degree':d0,'reduced_degree':d_red,
                          'linear_factors_retained':len(witnesses),
                          'linear_factors_cancelled_exact':len(cancel),
                          'reduced_denominator_l1_height_bound_bits':H_red,
                          'moving_base_quadratic_factors_retained_at_multiplicity_three':2*active})
    # Exact Fraction spot checks at selected regular rational midpoints.
    selected=(0,8,24,28,40,64,96,124)
    for i in selected:
        p=paths[i];k=int(ref['records'][i][1]);t=Fraction(2*k+1,1<<25)
        vec=tuple(w+t*d for w,d in zip(p['w'],p['d']))
        assert src.valid(vec)
        f=src.original_F(vec,W)/src.Q
        groups=base.certificate_one(i,p,k,W)[1]
        scalar,g=groups
        D=Fraction(scalar)
        for q,exponent in g.items():D*=base.poly_eval(q,t)**exponent
        assert D*f*(1<<(summaries[i]['unreduced_degree']*25))==int(D*f*(1<<(summaries[i]['unreduced_degree']*25)))
        checks['finite_fraction_spots']+=1
    summary={'schema':'EM_C300_FULL_REDUCED_DEGREE_CERT_V1',
             'model':'C195_H168_79_BRANCH_POSITIVE_RATIONAL_AUXILIARY',
             'count':len(certrows),'prime':str(P),
             'degree_distribution':dict(sorted(Counter(r['reduced_degree'] for r in summaries).items())),
             'unreduced_degree_distribution':dict(sorted(Counter(r['unreduced_degree'] for r in summaries).items())),
             'modular_noncancellation_witnesses':checks['linear_nonzero_modular'],
             'exact_linear_factor_cancellations':checks['linear_zero_exact'],
             'irreducible_base_quadratic_families':checks['moving_base_irreducible_quadratics'],
             'max_reduced_denominator_l1_height_bound_bits':max(r['reduced_denominator_l1_height_bound_bits'] for r in summaries),
             'uniform_sign_precision_formula':f"P={max(r['reduced_degree'] for r in summaries)}*b+{max(r['reduced_denominator_l1_height_bound_bits'] for r in summaries)}+134",
             'exact_nonzero_residue_spotchecks':checks['exact_nonzero_residue_spots'],
             'source_fraction_spotchecks':checks['finite_fraction_spots'],
             'scope':'AUTHOR_EXACT_NOT_CLAIMED_NOT_REVIEWED_NOT_ADMITTED'}
    compact={'schema':'EM_C300_FULL_125_LINEAR_POLE_CERT_V1','prime':str(P),'rows':certrows}
    contents=canonical(compact)
    z=gzip.compress(contents,compresslevel=9,mtime=0)
    encoded=base64.b64encode(z)
    Path('C300_125_LINEAR_POLE_CERTIFICATE.gz.b64').write_bytes(encoded+b'\n')
    summary['full_compact_json_sha256']=hashlib.sha256(contents).hexdigest()
    summary['compressed_blob_sha256']=hashlib.sha256(z).hexdigest()
    summary['compressed_blob_base64_bytes']=len(encoded)
    Path('C300_AUTHOR_AUDIT_20261025.json').write_text(json.dumps({'summary':summary,'path_rows':summaries},ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    assert len(encoded)<1024*1024
    print('C300_FULL_REDUCED_DENOMINATOR_DEGREE_EXACT_PASS',json.dumps(summary,ensure_ascii=False,sort_keys=True))
    return summary

if __name__=='__main__': run()
