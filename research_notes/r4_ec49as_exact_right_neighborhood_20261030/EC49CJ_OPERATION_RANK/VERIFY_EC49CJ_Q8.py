"""Independent exact-rational rank of all real 8-step path observations.
Uses an integer 3-vector basis at each typed state; no finite-field span
heuristic used to establish the Q upper bound at n=8.
"""
from collections import defaultdict
from fractions import Fraction
from VERIFY_EC49CJ import S,W,Z,suffixes,row_system,advance,reach_back,row_values

def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))

def indep3(bas,v):
    if len(bas)==0:return True
    if len(bas)==1:
        a=bas[0][0]
        return any(a[i]*v[j]!=a[j]*v[i] for i,j in ((0,1),(0,2),(1,2)))
    if len(bas)==2:return det3(bas[0][0],bas[1][0],v)!=0
    return False

class QBasis:
    def __init__(self):self.b=[]
    def add(self,v):
        v=[Fraction(x) for x in v]
        for p,row in self.b:
            if v[p]:
                k=v[p];v=[x-k*y for x,y in zip(v,row)]
        p=next((i for i,x in enumerate(v) if x),None)
        if p is None:return False
        factor=v[p];v=[x/factor for x in v]
        self.b.append((p,v));self.b.sort(key=lambda x:x[0])
        return True
    def rank(self):return len(self.b)

def all_real_paths_basis(n,ds):
    state={(Z,0):[((1,1,1),())]}
    for t in range(n):
        out={};rem=n-t-1
        for (z,q),samples in state.items():
            for sg in (1,-1):
                for i in range(6):
                    zz=list(z);zz[i]+=sg;zz=tuple(zz)
                    if not reach_back(zz,rem,ds):continue
                    key=(zz,advance(q,sg*(i+1)))
                    bs=out.setdefault(key,[])
                    a=W[0][i] if sg>0 else 1;b=W[1][i] if sg>0 else 1
                    for w,path in samples:
                        nw=(w[0]*a,w[1]*b,1)
                        if indep3(bs,nw):bs.append((nw,path+(sg*(i+1),)))
        state=out
    return state

if __name__=='__main__':
    n=8
    sufs=suffixes(3,True);rs=row_system(sufs)
    states=all_real_paths_basis(n,rs)
    for flag in (False,True):
        suf=suffixes(3,flag);rows=row_system(suf)
        total=0;fibers=[]
        for d,selected in rows.items():
            bs=QBasis()
            for q in range(9):
                for w,path in states.get((d,q),[]):
                    bs.add(row_values(path,suf,selected))
            total+=bs.rank();fibers.append((d[:2],bs.rank()))
        assert total==(135 if flag else 120),(flag,total)
        print('exact rational n8', 'S_leq3' if flag else 'S3',total,'fibers',fibers,flush=True)
