#!/usr/bin/env python3
"""Independent polynomial convolution cross-check of C313 factorwise multiplicity."""
import json,time
from collections import Counter
import C310_JOINT_BRANCH_PRIME_CERT as b
import C313_BRANCHWISE_F7_STRUCTURE as q
import C311_COMPOSITE_CERTIFICATE as c

def poly_root_multiplicity_exact(coeffs,a,p=7):
    v=[int(x)%p for x in coeffs]
    while len(v)>1 and v[-1]==0:v.pop()
    if not any(v):return None
    n=0
    while len(v)>1:
        res=[0]*(len(v)-1)
        res[-1]=v[-1]
        for k in range(len(v)-2,0,-1):res[k-1]=(v[k]+a*res[k])%p
        remainder=(v[0]+a*res[0])%p
        if remainder: break
        v=res;n+=1
    return n

def main():
    paths,_=b.c305.c288.build_paths();rr=json.loads(c.FROZEN.read_text());W,_=b.c305.src.floor_fixed_masses()
    bound={r['index']:r for r in json.load(open('C313_BRANCHWISE_F7_AUDIT_125.json'))['rows']}
    start=time.monotonic();rows=[]
    for i in range(125):
        s,groups,prepared,cancels,d=b.c305.prepare(i,paths[i],int(rr['records'][i][1]),W)
        L=b.term_content_lower(s,prepared)
        full,_,_,_=b.poly_branch_mod(7,groups,prepared,L)
        vals=[poly_root_multiplicity_exact(full,a) for a in range(7)]
        assert all(v is not None for v in vals),(i,'zero polynomial')
        m=min(vals)
        assert m>=bound[i]['guaranteed_P7_multiplicity'],(i,m,bound[i])
        row={'index':i,'R_degree_mod7':len(full)-1,'all_residue_multiplicities':vals,'exact_P7_power_in_R_mod7':m,
             'termwise_guaranteed_power':bound[i]['guaranteed_P7_multiplicity'],
             'excess_from_interbranch_cancellation':m-bound[i]['guaranteed_P7_multiplicity'],
             'R_mod7_nonzero':True}
        rows.append(row)
        if i%25==0:print('C313_POLY',i,m,'bound',bound[i]['guaranteed_P7_multiplicity'],flush=True)
    print('C313_POLY_DONE',len(rows),'minimum',min(r['exact_P7_power_in_R_mod7'] for r in rows),'max',max(r['exact_P7_power_in_R_mod7'] for r in rows),
          'excess_positive',sum(r['excess_from_interbranch_cancellation']>0 for r in rows),'elapsed',round(time.monotonic()-start,2),flush=True)
    with open('C313_F7_FULL_POLYNOMIAL_125.json','w') as f:json.dump({'schema':'C313_F7_FULL_NUMERATOR_POLYNOMIAL_CHECK_V1','model':'conditional on C300/C305 shared factorized auxiliary numerator','prime':7,'rows':rows},f,indent=2)

if __name__=='__main__':main()
