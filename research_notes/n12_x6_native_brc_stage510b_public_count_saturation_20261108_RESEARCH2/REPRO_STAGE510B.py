"""Stage510-B: verified BRC provenance-count saturation (exact integer model)."""
import itertools, json
from collections import deque
AXES = tuple((i,s) for i in range(6) for s in (-1,1))
def vec(a):
    i,s=AXES[a]; return tuple(s if j==i else 0 for j in range(6))
def F(toks):
    d=[0]*6; e=[0]*144
    for pos,(_,a,_) in enumerate(toks):
        v=vec(a)
        for j in range(6): d[j]+=v[j]
        if pos: e[toks[pos-1][1]*12+a]+=1
    return (len(toks),tuple(d),tuple(e))
def summary(toks):
    z=F(toks)
    return (z[0],z[1],z[2],toks[0][1] if toks else None,toks[-1][1] if toks else None)
def join(x,y):
    if x[0]==0:return y
    if y[0]==0:return x
    d=tuple(a+b for a,b in zip(x[1],y[1]))
    e=[a+b for a,b in zip(x[2],y[2])]
    e[x[4]*12+y[3]]+=1
    return (x[0]+y[0],d,tuple(e),x[3],y[4])
def tokens(tags,dirs=None):
    if dirs is None: dirs=tuple(i%12 for i in range(len(tags)))
    return tuple((i,dirs[i],t) for i,t in enumerate(tags))
def ops(toks,R,S):
    n=len(toks); out=[]
    if n:out.append(('POP',0))
    if n>=3:out.append(('DELETE2',0))
    if n>=2:out.append(('INSERT2',0))
    for r in R:
        if r<n:out.append(('SET',r))
    for k in S:
        if sum(t[2]=='P' for t in toks)>=k:out.append(('RANK',k))
    return out
def target(toks,op):
    kind,val=op
    if kind=='POP':return len(toks)-1
    if kind=='DELETE2':return len(toks)-3
    if kind=='SET':return len(toks)-1-val
    if kind=='RANK':
        positions=[i for i,t in enumerate(toks) if t[2]=='P']
        return positions[-val]
    return None
def apply(toks,op):
    kind,val=op; j=target(toks,op); a=list(toks)
    if kind in ('POP','DELETE2','RANK'):a.pop(j)
    elif kind=='SET':
        old=a[j];a[j]=(old[0],(old[1]+1)%12,old[2])
    elif kind=='INSERT2':
        next_id=min((t[0] for t in a),default=0)-1
        a.insert(len(a)-2,(next_id,7,'P'))
    else:raise ValueError(op)
    return tuple(a)
def exposed(original,R,S,h):
    q=deque([(original,0)]);seen=set();touched=set();states=0
    while q:
        w,depth=q.popleft()
        key=(tuple((t[0],t[2]) for t in w),depth)
        if key in seen:continue
        seen.add(key);states+=1
        if depth>=h:continue
        for op in ops(w,R,S):
            j=target(w,op)
            if j is not None and w[j][0]>=0:touched.add(w[j][0])
            q.append((apply(w,op),depth+1))
    return touched,states
def compress(raw,touched,cap):
    pieces=[];run=[]
    def flush():
        if run:
            pieces.append(('G',summary(run),min(cap,sum(t[2]=='P' for t in run))))
            run.clear()
    for t in raw:
        if t[0] in touched:
            flush();pieces.append(('T',t))
        else:run.append(t)
    flush()
    return tuple(pieces)
def Fcomp(pieces):
    z=(0,(0,)*6,(0,)*144,None,None)
    for p in pieces:z=join(z,summary((p[1],)) if p[0]=='T' else p[1])
    return z[:3]
def legal_comp(pieces,op):
    kind,val=op
    n=sum(p[1][0] if p[0]=='G' else 1 for p in pieces)
    if kind=='POP':return n>=1
    if kind=='DELETE2':return n>=3
    if kind=='INSERT2':return n>=2
    if kind=='SET':return val<n
    if kind=='RANK':
        r=val
        for p in reversed(pieces):
            c=(1 if p[1][2]=='P' else 0) if p[0]=='T' else p[2]
            r-=c
            if r<=0:return True
        return False
    raise ValueError(op)
def apply_comp(pieces,op):
    kind,val=op;ps=list(pieces)
    n=sum(p[1][0] if p[0]=='G' else 1 for p in ps)
    if kind=='RANK':
        rem=val;j=None
        for ix in range(len(ps)-1,-1,-1):
            p=ps[ix]
            c=(1 if p[1][2]=='P' else 0) if p[0]=='T' else p[2]
            if rem<=c:
                assert p[0]=='T','rank inside opaque gap'
                j=ix;break
            rem-=c
        assert j is not None
    elif kind=='INSERT2':
        pos=n-2;k=0;j=None
        for ix,p in enumerate(ps):
            if k==pos:j=ix;break
            k+=p[1][0] if p[0]=='G' else 1
        if j is None and k==pos:j=len(ps)
        assert j is not None,'insertion split opaque gap'
        new_id=min((p[1][0] for p in ps if p[0]=='T'),default=0)-1
        ps.insert(j,('T',(new_id,7,'P')))
        return tuple(ps)
    else:
        pos={'POP':n-1,'DELETE2':n-3,'SET':n-1-val}[kind]
        k=0;j=None
        for ix,p in enumerate(ps):
            m=p[1][0] if p[0]=='G' else 1
            if k<=pos<k+m:
                assert p[0]=='T','direct edit inside opaque gap'
                j=ix;break
            k+=m
        assert j is not None
    if kind=='SET':
        old=ps[j][1];ps[j]=('T',(old[0],(old[1]+1)%12,old[2]))
    else:ps.pop(j)
    return tuple(ps)
def verify(raw,R,S,h,cap,stats):
    touched,count=exposed(raw,R,S,h)
    stats['skeleton_states']+=count
    comp=compress(raw,touched,cap)
    assert F(raw)==Fcomp(comp)
    q=[(raw,comp,0)]
    while q:
        w,ps,dep=q.pop()
        stats['future_nodes']+=1
        assert F(w)==Fcomp(ps)
        if dep>=h:continue
        possible=[('POP',0),('DELETE2',0),('INSERT2',0)]
        possible += [('SET',r) for r in R]
        possible += [('RANK',k) for k in S]
        legal=set(ops(w,R,S))
        for op in possible:
            stats['legality_checks']+=1
            assert legal_comp(ps,op)==(op in legal),(op,w,ps)
            if op in legal:
                a,b=apply(w,op),apply_comp(ps,op)
                assert F(a)==Fcomp(b)
                stats['transitions']+=1
                q.append((a,b,dep+1))
    return touched,comp
def run():
    stats=dict(roots=0,skeleton_states=0,future_nodes=0,
               legality_checks=0,transitions=0,cap_boundary_collisions=0)
    for n in range(5):
        for xs in itertools.product(range(4),repeat=n):
            raw=tokens(tuple('P' if a//2 else 'O' for a in xs),
                       tuple(a%2 for a in xs))
            for R,S,h in [((2,),(1,),1),((2,),(1,2),2),((0,3),(1,3),2)]:
                verify(raw,R,S,h,max(S)-1,stats);stats['roots']+=1
    for n in (19,28):
        for z in range(10):
            tag=tuple('P' if (i*7+z*3)%11 in (0,1,3,4) else 'O' for i in range(n))
            dirs=tuple((i*7+z*5)%12 for i in range(n))
            raw=tokens(tag,dirs)
            R,S,h=((2,11),(1,3),3) if n==19 else ((2,18),(1,3),2)
            verify(raw,R,S,h,max(S)-1,stats);stats['roots']+=1
    witnesses=[]
    for K in range(2,8):
        n=K+5
        x=tokens(tuple('P' if i in range(K) else 'O' for i in range(n)))
        y=tokens(tuple('P' if i in range(K-1) else 'O' for i in range(n)))
        R,S,h=(n-1,),(K,),1
        dx,_=exposed(x,R,S,h);dy,_=exposed(y,R,S,h)
        assert dx==dy
        assert compress(x,dx,K-2)==compress(y,dy,K-2)
        assert ('RANK',K) in ops(x,R,S)
        assert ('RANK',K) not in ops(y,R,S)
        assert compress(x,dx,K-1)!=compress(y,dy,K-1)
        witnesses.append(dict(K=K,n=n,D=sorted(dx),gap_P_x=K-1,
                              gap_P_y=K-2,cap_wrong=K-2))
        stats['cap_boundary_collisions']+=1
    return dict(stage='510-B',status='ALL_ASSERTIONS_PASS',
      theorem='GAP_PUBLIC_COUNTS_SATURATE_AT_MAX_RANK_MINUS_ONE',
      tests=stats,strict_smaller_cap_witnesses=witnesses,
      frozen_science=dict(global_='bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
                          em='2af3fc484eb11060b69e0afc1b562bcaf5ad1419'),
      observer='n + signed Z6 displacement + 144 directed adjacency counts')
if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
