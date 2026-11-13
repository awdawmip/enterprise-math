#!/usr/bin/env python3
"""Exact adaptive dual BRC positive split; source is frozen native PREFIX589/591."""
from pathlib import Path
import runpy,json
s=runpy.run_path(str(Path(__file__).with_name('PREFIX591_R2_integer_lattice_core.py')))
A,T,H,W,blocks,steps=s['A'],s['T'],s['H'],s['W'],s['blocks'],s['steps']
N=96

def mv(C,c,v):
    out=[0]*N; terms=0
    for k in range(7):
        if c[k]==0:continue
        for i in range(N):
            for j in range(N):
                if C[k][i][j] and v[j]!=0:
                    out[i]+=c[k]*C[k][i][j]*v[j]
                    terms+=1
    return out,terms

cases={'singleton_port_0':[int(i==0) for i in range(N)],
       'uniform_all_ports':[1]*N,
       'block_balanced_4_ports':[int(i in blocks[0]) for i in range(N)],
       'sparse_native_endpoints':[int(i in (0,1,4,5,9,16,71)) for i in range(N)],
       'two_heavy_in_one_block':[int(i in blocks[0][:2]) for i in range(N)]}
results={}
for name,r in cases.items():
    v=H(r)
    p=[max(x,0) for x in v];q=[max(-x,0) for x in v]
    fp=W(r);fq=[2*x for x in r];native=r[:]
    assert [p[i]-q[i] for i in range(N)]==v
    assert all(p[i]<=fp[i] and q[i]<=fq[i] for i in range(N))
    count={'native':0,'signed':0,'fixed_two_positive':0,'adaptive_two_positive':0}
    for d in range(12):
        x=steps[d%4];c=list(x[:6])+[x[0]*x[6]]
        native,n=mv(A,c,native)
        v,sgn=mv(T,c,v)
        p,np=mv(T,c,p);q,nq=mv(T,c,q)
        fp,nfp=mv(T,c,fp);fq,nfq=mv(T,c,fq)
        assert all(y>=0 for y in p+q+fp+fq+native)
        assert [p[i]-q[i] for i in range(N)]==v
        assert W(v)==[3*x for x in native]
        assert all(p[i]<=fp[i] and q[i]<=fq[i] for i in range(N))
        for key,val in (('native',n),('signed',sgn),('fixed_two_positive',nfp+nfq),('adaptive_two_positive',np+nq)):
            count[key]+=val
    assert count['adaptive_two_positive']<=count['fixed_two_positive']
    results[name]=count
assert results['uniform_all_ports']['adaptive_two_positive']==6912
print('ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED')
print(json.dumps(results,sort_keys=True))
