"""Compare conditioned GAK intervals with exact path-weight supports."""
from functools import lru_cache
from collections import Counter
import json
from gal_path_hall import Bound,bitlist
from verify_gak import intervals

class FiberBound(Bound):
    def __init__(self,st):
        super().__init__(st);self.st=st
    @lru_cache(None)
    def opts(self,s,k):
        bits=list(bitlist(s));st=[self.st[b.bit_length()-1] for b in bits]
        return tuple((b,sum(1<<j for j in range(k+1) if lo<=j<=hi)) for b,(lo,hi) in zip(bits,intervals(st,k)))

def main():
    data=json.load(open('gal_path_hall.json'))['rows'];tot=Counter();rows=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));b=FiberBound(st);f=b.full;out=[];hits=Counter()
        for r in data[i]['budgets']:
            d,exact,old,*path=r;u=[b.upper(f,d,f,l) for l in range(3)]
            assert u[0]==old and all(x>=y for x,y in zip(u,path))
            for l,(x,y) in enumerate(zip(u,path)):
                if x>y:tot['strict_path_'+str(l)]+=1
                if x<n:tot['fiber_reject_'+str(d-k)+'_'+str(l)]+=1
            out.append([d,*u]);tot['budgets']+=1
        for t,old,*path in data[i]['obstacles']:
            u=[b.upper(f,k,t,l) for l in range(3)]
            assert all(x>=y for x,y in zip(u,path)) and u[0]==old
            for l,(x,y) in enumerate(zip(u,path)):
                if x>y:tot['strict_target_'+str(l)]+=1
                if x<t.bit_count():hits[l]+=1;tot['fiber_obstruction_'+str(l)]+=1
            tot['obstacles']+=1
        rows.append([i,out,dict(hits)]);b.clear()
    print(json.dumps({'totals':dict(tot),'rows':rows},sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
