#!/usr/bin/env python3
"""PREFIX-557 exact structural checks; frozen X6 native BRC science pin
f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires the already-published PREFIX550, PREFIX553, PREFIX556 source companions.
"""
import json
from collections import Counter
import PREFIX550_shared_gauge_compact_certificate as x
import PREFIX553_batched_depth_stream_certificate as p
import PREFIX556_compact_exact_certificate as b

PRIME=1000000007; Q=(2,3,5,7,11,13)
roots=(x.ZERO_ROOT,)+x.ROOTS

def mv(rows,v):
    return [sum(a*v[j] for j,a in row.items())%PRIME for row in rows]

def calc(root):
    # Each path action contributes a native BRC six-axis monomial and gate flag.
    rows=[{} for _ in range(96)];u=[0]*96
    for i in range(96):
        for act in x.A:
            j,w=x.edge(i,act,root)
            a=1
            for q,e in zip(Q,w[:6]):a=a*pow(q,e,PRIME)%PRIME
            if w[6]:
                assert j==9;u[i]=(u[i]+a)%PRIME
            else:rows[i][j]=(rows[i].get(j,0)+a)%PRIME
    assert {i for i,v in enumerate(u) if v}=={7,29,31}
    return rows,u

def gate_gap():
    gate_sources={7,29,31}; frontier={9};sizes=[]
    for d in range(4):
        sizes.append((len(frontier),sorted(frontier & gate_sources)))
        if d<3:
            frontier={j for i in frontier for act in x.A
                      for j,w in [x.edge(i,act,x.ZERO_ROOT)] if not w[6]}
    assert sizes==[(1,[]),(6,[]),(18,[]),(36,[7,29,31])]
    loop=[9,22,82,29,9]
    for h,(i,j) in enumerate(zip(loop,loop[1:])):
        assert any(x.edge(i,a,x.ZERO_ROOT)[0]==j and
                   x.edge(i,a,x.ZERO_ROOT)[1][6]==int(h==3) for a in x.A)
    # Each of the three sources has exactly one gate action to port 9.
    gates=[(i,j) for i in range(96) for a in x.A
           for j,w in [x.edge(i,a,x.ZERO_ROOT)] if w[6]]
    assert sorted(gates)==[(7,9),(29,9),(31,9)]
    return {'native_actions':576,'gate_edges':gates,
            'reachable_port_counts_and_gate_sources_at_0_to_3':sizes,
            'shortest_gate_separation':4,'repeatable_gate_loop':loop,
            'sharp_bound':'max_gate_count(d)=ceil(d/4) for d>=1'}

def zero_modes_and_rankone():
    prep=p.prepare();ids,ph,sig,rows,roots=prep
    neg=[c for c in range(51) if x.P[ph[c]][2]<0]
    pos=[c for c in range(51) if x.P[ph[c]][2]>0]
    ineg={c:i for i,c in enumerate(neg)};ipos={c:i for i,c in enumerate(pos)}
    A=[Counter() for _ in neg];B=[Counter() for _ in pos]
    for ii,c in enumerate(neg):
        for (j,g),n in rows[c].items():
            m=[0]*6;axis=abs(x.P[ph[c]][2])-1
            if axis<5:m[axis]=1
            m[5]=g;A[ii][(ipos[j],tuple(m))]+=n
    for ii,c in enumerate(pos):
        for (j,g),n in rows[c].items():
            m=[0]*6;axis=abs(x.P[ph[c]][2])-1
            if axis<5:m[axis]=1
            m[5]=g;B[ii][(ineg[j],tuple(m))]+=n
    pairs=[(1,2),(7,8),(9,10)]
    for lo,hi in pairs:
        for row in A:
            assert Counter({m:n for (j,m),n in row.items() if j==lo})==Counter(
                {m:n for (j,m),n in row.items() if j==hi})
    assert all(w[5]==0 for r in A for (j,w) in r)
    gates=[(i,j) for i,row in enumerate(B) for (j,w),n in row.items() if w[5]]
    assert gates==[(2,2),(8,2),(10,2)]
    cert=b.main(0)
    assert cert['AB_24_determinant_mod']==641735106
    return {'Q0_exact_nullspace_basis_global_indices':[[pos[hi],pos[lo]] for lo,hi in pairs],
            'nullspace_dimension':3,'rank_Q0':48,
            '24_core_gated_component':'H(z)=H(0)+z*u*e_2^T; u=A*b',
             'gated_B_entries':gates,
            'finite_field_AB_determinant':641735106}

def renewal():
    check=0
    for root in roots:
        rows,u=calc(root)
        base=[[1]*96]; kernel=[u]
        for d in range(24):
            base.append(mv(rows,base[-1]));kernel.append(mv(rows,kernel[-1]))
        for z in (0,3,17):
            f=[[1]*96];g=[[1]*96]
            for d in range(1,25):
                nxt=mv(rows,f[-1]);f.append([(nxt[i]+z*u[i]*f[-1][9])%PRIME for i in range(96)])
                t=[(base[d][i]+z*sum(kernel[s][i]*g[d-1-s][9] for s in range(d)))%PRIE
                   for i in range(96)]
                assert t==f[-1]
                g.append(t);check+=96
    assert check==89856
    return {'roots':13,'z_specializations':[0,3,17], 'depth_inclusive':24,
            'coefficient_comparisons_mod_prime':check,'all_equal':True}

def main():
    result={'status':'ALL_CHECKS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'gate_gap':gate_gap(),'zero_modes_and_rankone':zero_modes_and_rankone(),
            'finite_field_renewal_check':renewal()}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()
