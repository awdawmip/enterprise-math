#!/usr/bin/env python3
"""PREFIX-504 blocked V-prefix exact dense rank certificate on signed-X6 observer.

Scientific data: exact native signed-direction recurrence plus BRC cancellation V,W,
KMP terminal state and first B/C provenance. Validation K is built independently
from all native reachable states; the mathematical index uses PREFIX-500 oracle.
No floats, no numerical physical evolution, no general-X6 claims.
"""
from collections import defaultdict
from bisect import bisect_right
from time import perf_counter
import json, sys

LETTERS='aAbBcCdDeE'
GATES=('aab','aba')
CV=(0,1,0,2,1)
CW=(0,0,1,0,1)

def advance(x,ch,g):
    y=list(x[:5]);v,w,q,t=x[5:]
    i=LETTERS.index(ch)//2
    e=1 if ch.islower() else -1
    c=int(e*y[i]<0)
    y[i]+=e
    q=max(j for j in range(4) if (g[:q]+ch).endswith(g[:j]))
    if t=='N':
        if ch in 'bB':t='B'
        elif ch in 'cC':t='C'
    return tuple(y)+(v+CV[i]*c,w+CW[i]*c,q,t)

def row(pairs):
    vals=[];offs=[];weight=[];lookup={};total=0
    for val,k in pairs:
        if k:
            vals.append(val);offs.append(total);weight.append(k)
            lookup[val]=total;total+=k
    return vals,offs,weight,lookup,total

def choose(r,j):
    i=bisect_right(r[1],j)-1
    assert 0<=i<len(r[0]) and j<r[1][i]+r[2][i]
    return r[0][i],j-r[1][i]

def native_support(states):
    base=defaultdict(set)
    for x in states:base[x[:7]].add(x[7:])
    K={}
    for (u,v,c,d,e,V,W),ctrls in base.items():
        key=u,v,abs(c),abs(d)+abs(e),W,V
        if key in K:assert K[key]==ctrls
        else:K[key]=ctrls
    K={key:tuple(sorted(s)) for key,s in K.items()}
    return K

class Quintic:
    def __init__(self,n,K):
        self.n=n;self.K=K
        self.A=defaultdict(int)
        self.H={};self.B={};self.D={};self.C={};self.V={}
        byW=defaultdict(int)
        for (u,v,c,s,W,V),ctrls in K.items():
            self.A[u,v,c,s]+=len(ctrls)
            byW[u,v,c,s,W]+=len(ctrls)
        for u,v,c,s in self.A:
            m=(n-abs(u)-abs(v)-c-s)//2
            assert m>=0
            h=[0];running=0
            for W in range(m+1):
                running+=byW.get((u,v,c,s,W),0)
                h.append(running)
            assert running==self.A[u,v,c,s]
            self.H[u,v,c,s]=h
        for u,v,c in sorted(set(z[:3] for z in self.A)):
            L=n-abs(u)-abs(v)-c;P=[];acc=0
            for h in range(L+1):
                acc+=self.A.get((u,v,c,h),0);P.append(acc)
            self.B[u,v,c]=P
            E=lambda h:self.A.get((u,v,c,h),0)+2*(P[L]-P[h])
            drow=row((d,E(abs(d))) for d in range(-L,L+1))
            if drow[4]:self.D[u,v,c]=drow
        groups=defaultdict(set)
        for u,v,c in self.D:groups[u,v].add(c)
        byU=defaultdict(list)
        for u,v in sorted(groups):
            limit=n-abs(u)-abs(v)
            crow=row((w,self.D.get((u,v,abs(w)),([],[],[],{},0))[4]) for w in range(-limit,limit+1))
            if crow[4]:self.C[u,v]=crow;byU[u].append((v,crow[4]))
        self.V={u:row(pairs) for u,pairs in byU.items()}
        self.U=row((u,r[4]) for u,r in sorted(self.V.items()))
        self.S=self.U[4]
        self.nW=sum(len(h) for h in self.H.values())
        self.nquartic=len(self.A)+sum(len(p) for p in self.B.values())+sum(len(r[0]) for table in (self.D,self.C,self.V) for r in table.values())+len(self.U[0])
        self.calls=0
    def ep(self,u,v,c,d,e):
        p=self.B[u,v,c];L=len(p)-1;h=abs(d)
        if e<0:return p[L]-p[h+abs(e)]
        if e==0:return p[L]-p[h]
        return p[L]+self.A.get((u,v,c,h),0)+p[h+e-1]-2*p[h]
    def support(self,u,v,c,s,W,V):
        self.calls+=1
        return self.K.get((u,v,c,s,W,V),())
    def rank(self,x):
        u,v,c0,d,e,V,W,q,t=x;c=abs(c0);s=abs(d)+abs(e)
        z=self.U[3][u]+self.V[u][3][v]+self.C[u,v][3][c0]+self.D[u,v,c][3][d]+self.ep(u,v,c,d,e)
        z+=self.H[u,v,c,s][W]
        for vv in range(V):z+=len(self.support(u,v,c,s,W,vv))
        ctrls=self.support(u,v,c,s,W,V)
        return z+ctrls.index((q,t))
    def inverse(self,j):
        u,j=choose(self.U,j);v,j=choose(self.V[u],j);c0,j=choose(self.C[u,v],j)
        c=abs(c0);d,j=choose(self.D[u,v,c],j)
        R=self.n-abs(u)-abs(v)-c-abs(d)
        lo,hi=-R,R
        while lo<hi:
            mid=(lo+hi)//2
            if self.ep(u,v,c,d,mid+1)>j:hi=mid
            else:lo=mid+1
        e=lo
        assert self.ep(u,v,c,d,e)<=j<self.ep(u,v,c,d,e+1)
        j-=self.ep(u,v,c,d,e);s=abs(d)+abs(e)
        h=self.H[u,v,c,s]
        W=bisect_right(h,j)-1
        assert 0<=W<len(h)-1 and h[W]<=j<h[W+1]
        j-=h[W]
        m=(self.n-abs(u)-abs(v)-c-s)//2
        for V in range(2*m+1):
            cs=self.support(u,v,c,s,W,V)
            if j<len(cs):break
            j-=len(cs)
        else:raise AssertionError('V missing')
        return (u,v,c0,d,e,V,W)+cs[j]

class BlockedV(Quintic):
    """Exact V-block rank index, directly reusable PREFIX-503 spatial & W index.

    K is the independent native-test oracle in this certificate; production may
    supply the existing exact PREFIX-500 BRC source-support oracle. Full K is NOT
    counted as part of the sparse shared index.
    """
    def __init__(self,n,K,b):
        assert isinstance(b,int) and b>=1
        super().__init__(n,K)
        self.b=b;self.Vblocks={};self.block_words=0
        self.build_calls=0
        for u,v,c,s in sorted(self.A):
            m=(n-abs(u)-abs(v)-c-s)//2
            h=self.H[u,v,c,s]
            for W in range(m+1):
                p=[0];run=0
                for start in range(0,2*m+1,b):
                    for V in range(start,min(start+b,2*m+1)):
                        run+=len(self.K.get((u,v,c,s,W,V),()))
                        self.build_calls+=1
                    p.append(run)
                assert run==h[W+1]-h[W]
                self.Vblocks[u,v,c,s,W]=p
                self.block_words+=len(p)
        self.total_words=self.nquartic+self.nW+self.block_words

    def rank(self,x):
        u,v,c0,d,e,V,W,q,t=x;c=abs(c0);s=abs(d)+abs(e)
        z=self.U[3][u]+self.V[u][3][v]+self.C[u,v][3][c0]+self.D[u,v,c][3][d]
        z+=self.ep(u,v,c,d,e)+self.H[u,v,c,s][W]
        start=V//self.b*self.b
        z+=self.Vblocks[u,v,c,s,W][V//self.b]
        for vv in range(start,V): z+=len(self.support(u,v,c,s,W,vv))
        return z+self.support(u,v,c,s,W,V).index((q,t))

    def inverse(self,j):
        u,j=choose(self.U,j);v,j=choose(self.V[u],j);c0,j=choose(self.C[u,v],j)
        c=abs(c0);d,j=choose(self.D[u,v,c],j)
        R=self.n-abs(u)-abs(v)-c-abs(d)
        lo,hi=-R,R
        while lo<hi:
            mid=(lo+hi)//2
            if self.ep(u,v,c,d,mid+1)>j: hi=mid
            else: lo=mid+1
        e=lo
        assert self.ep(u,v,c,d,e)<=j<self.ep(u,v,c,d,e+1)
        j-=self.ep(u,v,c,d,e);s=abs(d)+abs(e)
        h=self.H[u,v,c,s]
        W=bisect_right(h,j)-1
        assert 0<=W<len(h)-1 and h[W]<=j<h[W+1]
        j-=h[W]
        p=self.Vblocks[u,v,c,s,W]
        block=bisect_right(p,j)-1
        assert 0<=block<len(p)-1 and p[block]<=j<p[block+1]
        j-=p[block]
        m=(self.n-abs(u)-abs(v)-c-s)//2
        for V in range(block*self.b,min((block+1)*self.b,2*m+1)):
            cs=self.support(u,v,c,s,W,V)
            if j<len(cs):break
            j-=len(cs)
        else:raise AssertionError('V missing within selected block')
        return (u,v,c0,d,e,V,W)+cs[j]


def verify(N=9, selected_widths=(1,2,3,4,8)):
    result={
        'status':'ALL_CHECKS_PASS',
        'research':'PREFIX-504',
        'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'scope':'signed native X6, five-axis restricted BRC-KMP-first-source observer',
        'arithmetic':'exact Python integers; no floating point scientific computation',
        'method':'independently computed native-state oracle; reusable PREFIX-503 spatial/W rank',
        'widths':list(selected_widths), 'gates':{}
    }
    for g in GATES:
        states={(0,0,0,0,0,0,0,0,'N')};out=[]
        for n in range(N+1):
            K=native_support(states)
            ordered=sorted(states,key=lambda x:(x[:5],x[6],x[5],x[7],x[8]))
            baseline=Quintic(n,K)
            assert baseline.S==len(ordered)
            vals=[]
            for b in sorted(set(list(selected_widths)+[n+1])):
                tm=perf_counter()
                idx=BlockedV(n,K,b)
                preprocessing_seconds=perf_counter()-tm
                assert idx.S==len(ordered)
                max_rank=max_inv=0
                tm=perf_counter()
                for j,x in enumerate(ordered):
                    idx.calls=0
                    r=idx.rank(x)
                    assert r==j,(g,n,b,'rank',j,r,x)
                    max_rank=max(max_rank,idx.calls)
                    idx.calls=0
                    inv=idx.inverse(j)
                    assert inv==x,(g,n,b,'inverse',j,inv,x)
                    max_inv=max(max_inv,idx.calls)
                query_seconds=perf_counter()-tm
                assert max_rank<=b and max_inv<=b,(g,n,b,max_rank,max_inv)
                vals.append({
                    'b':b,'shared_integer_words':idx.total_words,
                    'base_quintic_words':idx.nquartic+idx.nW,
                    'block_prefix_words':idx.block_words,
                    'preprocess_oracle_calls_Vblocks':idx.build_calls,
                    'max_rank_oracle_calls':max_rank,
                    'max_inverse_oracle_calls':max_inv,
                    'all_rank_inverse_states_checked':len(ordered),
                    # Non-evidentiary diagnostic measured on this host:
                    'build_seconds_diagnostic':round(preprocessing_seconds,4),
                    'rank_and_inverse_seconds_diagnostic':round(query_seconds,4)
                })
            out.append({'n':n,'total_joint_states':len(states),
                        'BRC_base_fibers':len({x[:7] for x in states}),
                        'quotient_spatial_keys':len(baseline.A),'widths':vals})
            if n<N:states={advance(x,a,g) for x in states for a in LETTERS}
        result['gates'][g]=out
    return result

if __name__=='__main__':
    print(json.dumps(verify(int(sys.argv[1]) if len(sys.argv)>1 else 9),sort_keys=True,separators=(',',':')))
