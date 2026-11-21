"""Extract and check exact rational covers for the type/point LP relaxation."""
import argparse,json,struct,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
import sympy as sp
from type_separator import points

def main(work,source,output):
    previous=json.loads(source.read_text());tag=previous['tag']
    counts={tuple(map(int,t.split('-')[:2])):int(t.split('-')[2])for t in tag.split('_')}
    counts.pop((12,1104),None);counts.pop((13,1296),None)
    types=sorted(counts);rows=[]
    for lo,hi,c,s in struct.iter_unpack('<QQII',(work/'bank').read_bytes()):
        t=(s%256,c)
        if t in counts:rows.append((lo+(hi<<64),types.index(t)))
    results=[]
    for entry in previous['frames']:
        if 'integer_certificate' in entry:continue
        start=time.monotonic();free=int(entry['free'])
        allowed=[(m,j)for m,j in rows if m&free==m]
        ri=[];ci=[]
        for i,(m,j)in enumerate(allowed):
            support=list(points(m))+[125+j]
            ri.extend(support);ci.extend([i]*len(support))
        design=coo_matrix((np.ones(len(ri),dtype=int),(ri,ci)),shape=(125+len(types),len(allowed))).tocsc()
        target=np.zeros(125+len(types),dtype=int);target[list(points(free))]=1
        for j,t in enumerate(types):target[125+j]=counts[t]
        fit=linprog(np.zeros(len(allowed)),A_eq=design,b_eq=target,bounds=(0,None),method='highs')
        assert fit.status==0,fit.message
        support=np.flatnonzero(fit.x>1e-8)
        exact=sp.Matrix(design[:,support].toarray());right=sp.Matrix(target)
        solution,parameters=exact.gauss_jordan_solve(right)
        assert not parameters.rows
        rational=[Fraction(int(x.p),int(x.q))for x in solution]
        assert all(v>0 for v in rational)
        sums=[Fraction(0)]*(125+len(types));items=[]
        for q,v in zip(support,rational):
            mask,j=allowed[q]
            for p in points(mask):sums[p]+=v
            sums[125+j]+=v
            items.append({'mask':str(mask),'type':types[j],'numerator':v.numerator,'denominator':v.denominator})
        assert sums==list(target)
        result={'frame':entry['frame'],'free':str(free),'positive_classes':len(items),'weights':items,'seconds':time.monotonic()-start}
        results.append(result)
        output.write_text(json.dumps({'tag':tag,'types':types,'frames':results},sort_keys=True,indent=2)+'\n')
        print(json.dumps({'frame':entry['frame'],'positive_classes':len(items),'seconds':result['seconds'],'verified':True}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--work',type=Path,required=True);p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();main(a.work,a.source,a.output)
