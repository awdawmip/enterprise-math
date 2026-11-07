#!/usr/bin/env python3
"""Exact 0-gate e-basis sign scan, depth 0..256; native frozen pin f42f2906d77f24085c123f3ccfe9667d41caa96d."""
from collections import Counter
import json
from PREFIX565_positive_marginal_certificate import ZERO_ROOT, ROOTS, ACTIONS, edge
from PREFIX566_gate_quotient_certificate import (marginal_gate_rows,weighted_quotient,
    step_gate,native_involution,symmetric_to_uvz)

def verify(max_depth=256):
    rows=marginal_gate_rows(ZERO_ROOT)
    nedge=0
    for root in ROOTS:
        for i in range(96):
            for a in ACTIONS:
                j,w=edge(i,a,root)
                j0,w0=edge(i,a,ZERO_ROOT)
                assert j==j0 and w[4:]==w0[4:]
                nedge+=1
    nogate=[Counter({key:c for key,c in row.items() if key[3]==0}) for row in rows]
    ids,q,growth=weighted_quotient(nogate)
    assert len(q)==37
    fixed=sorted({ids[i] for i,j in enumerate(native_involution()) if i==j})
    assert len(fixed)==11
    cur=[{(0,0,0):1} for _ in q]
    total=0;witness=None;points=[]
    for d in range(max_depth+1):
        for c in fixed:
            uv=symmetric_to_uvz(cur[c])
            total+=len(uv)
            bad=next(((mon,val) for mon,val in uv.items() if val<0),None)
            if bad:
                witness={'depth':d,'class':c,'monomial':bad[0],'coefficient':bad[1]}
                break
        if witness:break
        if d in (64,128,192,256):
            points.append({'depth':d,'all_class_xy_terms':sum(map(len,cur)),
                 'fixed_class_uv_terms':sum(len(symmetric_to_uvz(cur[c])) for c in fixed)})
        if d<max_depth:cur=step_gate(cur,q)
    return {'status':'ALL_CHECKS_PASS' if witness is None else 'NEGATIVE_WITNESS',
            'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'observer':'q1=q2=q3=q4=1; x=q5,y=q6; z=0; roots r5=r6=0',
            'native_projection_edge_checks':nedge,'quotient_classes':len(q),
            'sigma_fixed_classes':len(fixed), 'checked_depth_range':[0,max_depth],
            'checked_e_basis_term_positions':total,'first_negative_witness':witness,
            'snapshots':points,'scope':'finite integer scan; all-depth nonnegativity remains open'}

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
