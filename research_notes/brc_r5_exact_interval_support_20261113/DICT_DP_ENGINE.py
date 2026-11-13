#!/usr/bin/env python3
"""Pruned dictionary baseline for the frozen original R5 interval-array cold comparison."""
from VERIFY_R5_INTERVAL_ARRAY_DP import frozen_events,graph,IntervalDP,R,K,ORIGINAL_RANK,EXPECTED_J,EXPECTED_T,original_centers
x=frozen_events();g=graph(x,R);original=original_centers()

class DictDP:
    def __init__(self,x,r,k,g):
        n=len(x)
        tail=lambda p:sum(x[b]-x[p] for b in range(p+1,n))
        row={p:(tail(p),1) for p in range(n) if x[-1]-x[p]<=r}
        allrows=[None,row]
        for t in range(2,k+1):
            nxt={}
            for p in range(max(0,min(row)-(2*r+1)),max(row)):
                best=10**30;ways=0
                for q,w in g[p]:
                    old,nways=row.get(q,(10**30,0))
                    if not nways:continue
                    y=w+old
                    if y<best:best,ways=y,nways
                    elif y==best:ways+=nways
                if ways:nxt[p]=(best,ways)
            row=nxt;allrows.append(row)
        self.rows=allrows
    def value(self,t,p):return self.rows[t].get(p,(10**30,0))
    def summary(self):
        head=lambda p:sum(x[p]-x[b] for b in range(p))
        starts=[p for p in range(len(x)) if x[p]-x[0]<=R]
        best=min(head(p)+self.value(K,p)[0] for p in starts)
        return best,sum(self.value(K,p)[1] for p in starts if head(p)+self.value(K,p)[0]==best)
    def unrank(self,rank):
        best,total=self.summary();assert 0<=rank<total
        head=lambda p:sum(x[p]-x[b] for b in range(p))
        starts=[p for p in range(len(x)) if x[p]-x[0]<=R]
        out=[]
        for p in starts:
            c,z=self.value(K,p)
            if head(p)+c!=best:continue
            if rank<z:out=[p];break
            rank-=z
        for t in range(K,1,-1):
            p=out[-1];base=self.value(t,p)[0]
            for q,w in g[p]:
                c,z=self.value(t-1,q)
                if w+c!=base:continue
                if rank<z:out.append(q);break
                rank-=z
            else:raise AssertionError('bad path')
        assert rank==0
        return out
