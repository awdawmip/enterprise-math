"""Exact finite-ring minimal labelled observer basis for the frozen R258 auxiliary model.

No floating point operations. All reconstruction is modulo p**a. A uniform
monic annihilator of degree sum(d_m)=249 makes a 249-tap window sufficient
for all future times k>=3.
"""
import json
from pathlib import Path
from fractions import Fraction
from R260_labelled_modular_quotient import reconstruct, sequence

N=249
P=13

def independent_rows_mod_p(rows,p):
    echelon=[]
    indices=[]
    pivots=[]
    for idx,row in enumerate(rows):
        v=[x%p for x in row]
        for j,piv in enumerate(pivots):
            c=v[piv]
            if c: v=[(a-c*b)%p for a,b in zip(v,echelon[j])]
        if any(v):
            pivot=next(j for j,a in enumerate(v) if a)
            inv=pow(v[pivot],-1,p)
            v=[x*inv%p for x in v]
            pivots.append(pivot)
            indices.append(idx)
            echelon.append(v)
    return indices,pivots

def inverse_mod_unit_matrix(a,n,p):
    d=len(a)
    if not d:return []
    v=[[x%n for x in row]+[int(j==i) for j in range(d)] for i,row in enumerate(a)]
    for i in range(d):
        k=next(k for k in range(i,d) if v[k][i]%p)
        v[i],v[k]=v[k],v[i]
        inv=pow(v[i][i],-1,n)
        v[i]=[w*inv%n for w in v[i]]
        for k in range(d):
            if k==i:continue
            t=v[k][i]
            if t:v[k]=[(x-t*y)%n for x,y in zip(v[k],v[i])]
    return [row[d:] for row in v]

def multiply_row_matrix(row,mat,n):
    return [sum(x*mat[i][j] for i,x in enumerate(row))%n for j in range(len(mat))]

def recurse_basis(rows,p,a):
    n=p**a
    total=len(rows)
    width=len(rows[0])
    ids,pivots=independent_rows_mod_p(rows,p)
    rank=len(ids)
    selected=[rows[i] for i in ids]
    if rank:
        pivot_matrix=[[r[j]%n for j in pivots] for r in selected]
        inverse=inverse_mod_unit_matrix(pivot_matrix,n,p)
        coeff0=[multiply_row_matrix([v[j]%n for j in pivots],inverse,n) for v in rows]
    else: coeff0=[[] for v in rows]
    residuals=[]
    for i,v in enumerate(rows):
        r=[(v[k]-sum(coeff0[i][j]*selected[j][k] for j in range(rank)))%n for k in range(width)]
        assert all(x%p==0 for x in r)
        residuals.append([x//p for x in r])
    if a==1:
        assert all(not any(r) for r in residuals)
        assert len(ids)==len(set(ids))
        return ids,coeff0,[rank],pivots
    ids_extra,coeff_extra,levels,deep_pivots=recurse_basis(residuals,p,a-1)
    assert not set(ids)&set(ids_extra)
    coeff=[]
    for i in range(total):
        e=coeff_extra[i]
        unit=[(coeff0[i][j]-sum(e[h]*coeff0[idx][j] for h,idx in enumerate(ids_extra)))%n for j in range(rank)]
        coeff.append(unit+[z%n for z in e])
    allids=ids+ids_extra
    assert len(allids)==len(set(allids))
    for i,row in enumerate(rows):
        for k in range(width):
            assert (sum(coeff[i][j]*rows[idx][k] for j,idx in enumerate(allids))-row[k])%n==0,(p,a,i,k)
    return allids,coeff,[rank]+levels,pivots

def run():
    s=Fraction(866,2197)
    J,T,K=3327364117,3975468120,36933000
    cs,qs=reconstruct(s,J,T,K)
    # Each q_(m,k) follows its own exact integer characteristic recurrence.
    # The product of the 63 monic polynomials has degree 249 and annihilates all masks.
    reports=[]
    for exp in range(1,11):
        mod=P**exp
        rows=[sequence(c,q,mod,N) for c,q in zip(cs,qs)]
        ids,coeff,levels,pivots=recurse_basis(rows,P,exp)
        assert len(ids)==sum(levels)
        # Extra 249-tap recurrence verification beyond the theorem window.
        expanded=[sequence(c,q,mod,N*2) for c,q in zip(cs,qs)]
        for m in range(63):
            for j in range(N,N*2):
                assert (sum(coeff[m][b]*expanded[mask][j] for b,mask in enumerate(ids))-expanded[m][j])%mod==0,(exp,m,j)
        reports.append({
            'modulus':mod,'p':P,'exponent':exp,
            'smith_layer_generator_counts':levels,
            'minimal_original_label_count':len(ids),
            'selected_masks':ids,'field_pivot_columns':pivots,
            'all_label_coefficient_vectors':coeff,
            'checked_masks':63,'proved_all_k_ge_3':True,
            'theorem_window_length':N,'cross_checked_total_initial_taps':2*N,
        })
        print('p^a',mod,'layers',levels,'basis',len(ids),'masks',ids,flush=True)
    out={
        'schema':'EM_R261_10_LAYER_LABELLED_OBSERVER_V1',
        'source':'R260 code and R260A proof at enterprise-math@6bbb4062b54094d2fdea30df1d31891659d9fdb1',
        'frozen_science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'model':'R258 auxiliary positive rational 63-mask model',
        'parameter_s':'866/2197','normalization':{'J':J,'T':T,'K':K},
        'R261_computations':reports
    }
    dest=Path(__file__).with_name('R261_full_verification.json')
    dest.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('PASS output',dest,'size',dest.stat().st_size)
    import hashlib
    digest=hashlib.sha256(dest.read_bytes()).hexdigest()
    short={'schema':'EM_R261_10_LAYER_DIGEST_V1','frozen_pin':out['frozen_science_pin'],
        'full_json_sha256':digest,'full_json_size':dest.stat().st_size,
        'cases':[{'modulus':x['modulus'],'p_power':x['exponent'],
          'smith_layer_generator_counts':x['smith_layer_generator_counts'],
          'minimal_original_label_count':x['minimal_original_label_count'],
          'selected_masks':x['selected_masks'],'checked_taps':x['cross_checked_total_initial_taps']}
          for x in reports]}
    digestpath=Path(__file__).with_name('R261_verification_digest.json')
    digestpath.write_text(json.dumps(short,sort_keys=True,indent=2)+'\n')
    print('DIGEST',digest,'summary',digestpath)

if __name__=='__main__':run()
