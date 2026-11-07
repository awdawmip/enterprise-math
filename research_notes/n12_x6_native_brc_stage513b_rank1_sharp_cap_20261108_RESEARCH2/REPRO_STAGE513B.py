#!/usr/bin/env python3
"""Stage513-B: D_h-safe rank provenance cap for S containing 1 and K.
Native X6 alphabet is 0..11 and F includes all 144 ordered adjacency counts.
No external dependencies; proof is separate from these finite checks.
"""
from itertools import product
import json

A = 12

def F(w):
    ds = [0]*6
    e = [0]*(A*A)
    for i, a in enumerate(w):
        ds[a//2] += 1 if a % 2 == 0 else -1
        if i: e[w[i-1]*A+a] += 1
    return (len(w),tuple(ds),tuple(e),w[0] if w else None,w[-1] if w else None)

def join(x,y):
    if not x[0]: return y
    if not y[0]: return x
    E = [a+b for a,b in zip(x[2],y[2])]
    E[x[4]*A+y[3]] += 1
    return (x[0]+y[0],tuple(a+b for a,b in zip(x[1],y[1])),tuple(E),x[3],y[4])

def exposure(tags,h,R,S):
    front={tuple(range(len(tags)))}
    visited=set(front); touched=set(); states=0
    for depth in range(h):
        nxt=set()
        for w in front:
            states+=1
            n=len(w)
            def mark(j):
                if w[j]>=0: touched.add(w[j])
            if n:
                mark(n-1);nxt.add(w[:-1])
            if n>=3:
                mark(n-3);nxt.add(w[:-3]+w[-2:])
            if n>=2:nxt.add(w[:-2]+(-1,)+w[-2:])
            for r in R:
                if r<n:mark(n-1-r)
            ranked=[j for j in range(n-1,-1,-1) if w[j]<0 or tags[w[j]]]
            for k in S:
                if k<=len(ranked):
                    j=ranked[k-1];mark(j)
                    nxt.add(w[:j]+w[j+1:])
        front=nxt-visited;visited.update(front)
    return frozenset(touched),states

def compress(word,D,cap):
    out=[];hidden=[]
    def flush():
        if hidden:
            out.append(('G',F([x[1] for x in hidden]),min(cap,sum(x[2] for x in hidden))))
            hidden.clear()
    for tok in word:
        if tok[0]>=0 and tok[0] not in D:hidden.append(tok)
        else:
            flush();out.append(('T',tok))
    flush()
    return tuple(out)

def norm(parts,cap):
    out=[]
    for kind,obj,*tail in parts:
        if kind=='G' and out and out[-1][0]=='G':
            _,old,c=out[-1]
            out[-1]=('G',join(old,obj),min(cap,c+tail[0]))
        else:out.append((kind,obj,*tail))
    return tuple(out)

def piece_location(parts,j):
    p=0
    for z,part in enumerate(parts):
        length=1 if part[0]=='T' else part[1][0]
        if p<=j<p+length: return z,j-p
        p+=length
    raise IndexError(j)

def insert_location(parts,j):
    p=0
    for z,part in enumerate(parts):
        if j==p:return z
        length=1 if part[0]=='T' else part[1][0]
        if p<j<p+length:raise ValueError('INSERT would split hidden gap')
        p+=length
    if j==p:return len(parts)
    raise IndexError(j)

def public_target_comp(parts,k):
    for z in range(len(parts)-1,-1,-1):
        piece=parts[z]
        cnt=piece[1][2] if piece[0]=='T' else piece[2]
        if k<=cnt:
            if piece[0]=='G':raise ValueError('Ranked edit inside hidden gap')
            return z
        k-=cnt
    return None

def apply(word,parts,D,cap,act):
    typ=act[0];n=len(word)
    if typ=='POP': idx=n-1 if n else None
    elif typ=='DELETE2':idx=n-3 if n>=3 else None
    elif typ=='SET':idx=n-1-act[1] if act[1]<n else None
    elif typ=='KTH':
        pubs=[i for i in range(n-1,-1,-1) if word[i][2]]
        idx=pubs[act[1]-1] if act[1]<=len(pubs) else None
    else:idx=None
    if typ=='INSERT' and n<2:return None,None
    if typ!='INSERT' and idx is None:
        if typ=='KTH': assert public_target_comp(parts,act[1]) is None
        return None,None
    cp=list(parts)
    if typ=='INSERT':
        pos=n-2
        pi=insert_location(parts,pos)
        newid=min((t[0] for t in word),default=0)-1
        if newid>=0:newid=-1
        tok=(newid,act[1],1)
        nw=word[:pos]+(tok,)+word[pos:]
        cp.insert(pi,('T',tok))
    else:
        pi,off=piece_location(parts,idx)
        assert off==0 and cp[pi][0]=='T',('exposed target',act,idx)
        if typ=='KTH':assert pi==public_target_comp(parts,act[1])
        if typ=='SET':
            tok=word[idx];newtok=(tok[0],act[2],tok[2])
            nw=word[:idx]+(newtok,)+word[idx+1:]
            cp[pi]=('T',newtok)
        else:
            nw=word[:idx]+word[idx+1:]
            cp.pop(pi)
    return nw,norm(cp,cap)

def actions(n,R,S):
    ret=[('POP',),('DELETE2',),('INSERT',0),('INSERT',11)]
    ret.extend(('SET',r,d) for r in R for d in (0,11))
    ret.extend(('KTH',k) for k in S)
    return ret

def run_root(tags,h,R,S,stats,full=False):
    K=max(S); cap=max(0,K-2)
    D,scanned=exposure(tags,h,R,S)
    word=tuple((i,(7*i+3)%12,int(tags[i])) for i in range(len(tags)))
    root=compress(word,D,cap)
    queue=[(word,root,0)]
    while queue:
        w,c,d=queue.pop();stats['nodes']+=1
        assert c==compress(w,D,cap)
        f=F([t[1] for t in w]);fc=F([])
        for part in c:
            fc=join(fc,F([part[1][1]]) if part[0]=='T' else part[1])
        assert f==fc
        assert any(i for i in f[2]) or len(w)<2
        if d==h:continue
        for act in actions(len(w),R,S):
            ww,cc=apply(w,c,D,cap,act)
            stats['transitions']+=1
            if ww is not None:
                assert cc==compress(ww,D,cap)
                if d+1<h or full:queue.append((ww,cc,d+1))
    stats['roots']+=1;stats['states_preprocessing']+=scanned

def sharp(K):
    assert K>=3
    g=max(4,K);n=2+g+5
    tags_a=[1,1]+[1]*(K-3)+[0]*(g-(K-3))+[0,0,0,0,1]
    tags_b=[1,1]+[1]*(K-2)+[0]*(g-(K-2))+[0,0,0,0,1]
    assert len(tags_a)==n==len(tags_b)
    R={n-1,n-2};S={1,K};h=1
    D1,_=exposure(tags_a,h,R,S);D2,_=exposure(tags_b,h,R,S)
    assert D1==D2
    directions=[0,2]+[4]*g+[6,8,10,0,2]
    w1=tuple((i,directions[i],tags_a[i]) for i in range(n))
    w2=tuple((i,directions[i],tags_b[i]) for i in range(n))
    T=K-3
    assert compress(w1,D1,T)==compress(w2,D2,T)
    u1,_=apply(w1,compress(w1,D1,K-2),D1,K-2,('KTH',K))
    u2,_=apply(w2,compress(w2,D2,K-2),D2,K-2,('KTH',K))
    assert F([t[1] for t in u1])!=F([t[1] for t in u2])
    return {'K':K,'cap_sufficient':K-2,'cap_failed':K-3,'n':n,
    'same_exposure':sorted(D1),
    'lost_displacement':list(F([t[1] for t in u1])[1]),
    'other_displacement':list(F([t[1] for t in u2])[1])}

def main():
    stats={'roots':0,'nodes':0,'transitions':0,'states_preprocessing':0}
    for n in range(2,7):
        for tags in product((0,1),repeat=n):
            for h in (1,2):
                for K in (2,3,4):
                    R={2,max(0,n-1)}
                    run_root(tags,h,R,{1,K},stats)
    for n in (7,9,12):
        for j in range(12):
            tags=tuple(int(((i*17+j*3)%11)<5) for i in range(n))
            for K in (2,3,4):
                run_root(tags,3,{0,2,n-2},{1,K},stats)
    sharpness=[sharp(K) for K in (3,4,5,6,7)]
    result={'version':'STAGE513B',
    'statement':'Cap max(0,K-2) safe for S containing 1 and max S=K',
    'verified':stats,'sharpness':sharpness,
    'arithmetic':'Python exact signed integers; 12 X6 directions and 144 directed edges',
    'assertions':'PASS'}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
