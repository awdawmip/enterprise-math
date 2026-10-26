#!/usr/bin/env python3
"""Author exact-rational Bellman/ordered-DFS check for external iid N=14 stages 157-158.
Only Python stdlib. Not a P000-native proof or independent Driver review.
"""
from fractions import Fraction as F
from functools import lru_cache
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
A=(3,1,20);B=(1,1,10);DP=24**N;DQ=12**N
S=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
assert len(S)==680

def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def verify(K,L,s1,z1,s2,z2,expected):
    # z1/z2 mean special action probabilities; other special action is baseline.
    @lru_cache(None)
    def bell(s):
        n,a,b=s;acts={'P':K*ratio(s),'Q':L}
        if n<N:
            kids=[bell((n+1,a+1,b))[0],bell((n+1,a,b+1))[0],bell((n+1,a,b))[0]]
            acts['C']=F(1)+sum(P[i]*kids[i] for i in range(3))
        v=min(acts.values());return v,tuple(z for z in acts if acts[z]==v),acts
    ties={s:bell(s)[1] for s in S if len(bell(s)[1])>1}
    assert set(ties)=={s1,s2},ties
    gaps=[v-bell(s)[0] for s in S for v in bell(s)[2].values() if v>bell(s)[0]]
    assert len(gaps)==1238 and min(gaps)==expected
    def choice(s,t1,t2):
        if s==s1:return z1 if t1 else next(x for x in ties[s] if x!=z1)
        if s==s2:return z2 if t2 else next(x for x in ties[s] if x!=z2)
        (a,)=bell(s)[1];return a
    @lru_cache(None)
    def obs(s,t1,t2):
        n,a,b=s;act=choice(s,t1,t2)
        if act=='P':return F(0),F(1),F(0),F(0)
        if act=='Q':return F(1),F(0),F(0),F(0)
        kid=[obs((n+1,a+1,b),t1,t2),obs((n+1,a,b+1),t1,t2),obs((n+1,a,b),t1,t2)]
        return sum(P[i]*kid[i][0] for i in range(3)),sum(Q[i]*kid[i][1] for i in range(3)),F(1)+sum(P[i]*kid[i][2] for i in range(3)),F(1)+sum(Q[i]*kid[i][3] for i in range(3))
    def ordered(t1,t2):
        hit={s1:[0,0,0],s2:[0,0,0]};tot=[0]*6;nodes=0
        def walk(n,a,b,p,q):
            nonlocal nodes
            nodes+=1;s=(n,a,b);act=choice(s,t1,t2)
            if s in hit:
                v=hit[s];v[0]+=1;v[1]+=p*24**(N-n);v[2]+=q*12**(N-n)
            if act=='C':
                assert n<N
                walk(n+1,a+1,b,p*A[0],q*B[0]);walk(n+1,a,b+1,p*A[1],q*B[1]);walk(n+1,a,b,p*A[2],q*B[2]);return
            pm=p*24**(N-n);qm=q*12**(N-n)
            tot[0]+=pm;tot[1]+=qm;tot[2 if act=='Q' else 3]+=(pm if act=='Q' else qm)
            tot[4]+=n*pm;tot[5]+=n*qm
        walk(0,0,0,1,1)
        assert tot[0]==DP and tot[1]==DQ
        v=(F(tot[2],DP),F(tot[3],DQ),F(tot[4],DP),F(tot[5],DQ))
        hits={str(s):[h[0],str(F(h[1],DP)),str(F(h[2],DQ))] for s,h in hit.items()}
        return v,hits,nodes
    out={};counts={};hits={}
    for t1,t2 in ((0,0),(1,0),(0,1),(1,1)):
        v,h,n=ordered(t1,t2)
        assert v==obs((0,0,0),t1,t2)
        out[(t1,t2)]=v;counts[f'{t1}{t2}']=n;hits[f'{t1}{t2}']=h
    assert len({str(v) for v in hits.values()})==1
    v=out[0,0];d1=tuple(out[1,0][i]-v[i] for i in range(4));d2=tuple(out[0,1][i]-v[i] for i in range(4))
    assert tuple(out[1,1][i]-v[i]-d1[i]-d2[i] for i in range(4))==(F(0),)*4
    x0=(v[1]-v[0])/(d2[0]-d2[1]);slope=-(d1[0]-d1[1])/(d2[0]-d2[1])
    xmax=min(F(1),-x0/slope) if slope<0 else min(F(1),(1-x0)/slope)
    assert 0<=x0<=1 and 0<xmax<=1
    def point(t):
        x=x0+slope*t
        assert 0<=x<=1
        return tuple(v[i]+t*d1[i]+x*d2[i] for i in range(4))
    start,end=point(F(0)),point(xmax);h=bell((0,0,0))[0]
    assert end[0]>start[0] and start[0]==start[1] and end[0]==end[1]
    assert all(o[2]>o[3] and o[2]+K*o[1]+L*o[0]==h for o in (start,end))
    assert start[2]-end[2]==(K+L)*(end[0]-start[0])
    return {'ties':ties,'dual':h,'min_gap':min(gaps),'first_hit':hits['00'], 'nodes':counts,
            'M00':v,'d1':d1,'d2':d2,'x0':x0,'dx_dt':slope,'tmax':xmax,'start':start,'end':end,
            'width':end[0]-start[0],'slope':K+L}

def fmt(x):return str(x) if not isinstance(x,(tuple,list,dict)) else str(x)
if __name__=='__main__':
    u=verify(F(3342600,10529),F(3342600,10529),(10,2,0),'P',(14,0,0),'P',F(232231247,11789784576))
    assert u['start'][0]==F(7319074368089652265,21035720123168587776)
    assert u['end'][0]==F(763084945158127578305,2192919042319171190784)
    assert u['end'][2]==F(3298586218925748578843,274114880289896398848)
    assert u['tmax']==F(660136987826389,4611571200000000)
    v=verify(F(26880449139504,86511167249),F(26463665283720,86511167249),(6,1,2),'Q',(10,2,0),'P',F(874625881143787,32290120153354752))
    assert v['start']==u['end']
    assert v['end'][0]==F(763167995878686618305,2192919042319171190784)
    assert v['end'][2]==F(3292184925194961698843,274114880289896398848)
    assert v['tmax']==1
    for stage,rec in ((157,u),(158,v)):
        print('STAGE',stage,'PASS states',len(S),'ties',rec['ties'],'min_gap',rec['min_gap'])
        for k in ('dual','first_hit','nodes','M00','d1','d2','x0','dx_dt','tmax','start','end','width','slope'):
            print(k,fmt(rec[k]))
