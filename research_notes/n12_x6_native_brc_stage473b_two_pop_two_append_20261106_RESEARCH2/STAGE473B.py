"""Stage473-B independent future-repair theorem and exact positive BRC DP.
Scientific model: ternary original words embedded into signed X6; all 12 signed future appends.
The polynomial support DP implemented here covers t>=m-1. The proof handles all t.
Python standard library only; all populations and DP counters are arbitrary-precision integers.
"""
from collections import defaultdict, Counter, deque
from functools import lru_cache
from itertools import product
import json

D=(0,1,2); A,B,C=D; Z=(0,)*9
ix=lambda a,b:3*a+b

def edge(w):
    z=list(Z)
    for a,b in zip(w,w[1:]):z[ix(a,b)]+=1
    return tuple(z)

def inc(e,a,b):
    z=list(e);z[ix(a,b)]+=1;return tuple(z)

def fits(e,b):return all(x<=y for x,y in zip(e,b))

def obs(p,q):return len(p),len(q),edge(p),edge(q),sum(a==b for a,b in zip(p,q))

def last(e):
    f=[sum(e[ix(x,y)] for y in D)-sum(e[ix(y,x)] for y in D) for x in D]
    r=[z for z in D if all(f[x]==(x==A)-(x==z) for x in D)]
    assert len(r)==1
    return r[0]

def repair469(p,q,t):
    m,n=len(p),len(q)
    v=(q[t-1],)
    v+=tuple((p[i-1],q[i-1]) for i in range(t+1,m+1))
    v+=tuple(q[i-1] for i in range(max(t+1,m+1),n+1))
    return (v,p[m-2],q[m-1] if t>m else None,q[m] if t>m+1 else None)

def repair473(p,q,t):
    m,n=len(p),len(q)
    return (repair469(p,q,t),p[m-3],q[m-2],q[m+1] if m+2<=n else None)

def key_dp(p,q,t):
    """Alternative class key for t>=m-1; equality equals repair473 on fixed observer fiber.
    Head records P_m-2, P_m-1, Q_m-1 and any Q_m..Q_m+2 inside prefix,
    then Q_t, followed by Q_(t+1)..Q_n. Q tail contains other Q tags.
    """
    m,n=len(p),len(q)
    assert m-1<=t<=n
    return (p[m-3],p[m-2],q[m-2])+tuple(q[j-1] for j in (m,m+1,m+2) if j<=t and j<=n)+(q[t-1],)+q[t:]

def solve(phi,t):
    m,n,EP,EQ,K=phi
    assert 4<=m<n and m-1<=t<=n
    pm=last(EP)
    # p2,p1,q1,qm,qm1,qm2: -1 until that tagged index is observed.
    ini=(A,A,Z,Z,1,-1,-1,-1,-1,-1,-1)
    pre={ini:1}
    for j in range(2,t+1):
        nx=defaultdict(int)
        for (lp,lq,pe,qe,k,p2,p1,q1,qm,qm1,qm2),w in pre.items():
            for p in ((pm,) if j==m else D if j<m else (None,)):
                pp=inc(pe,lp,p) if p is not None else pe
                if not fits(pp,EP):continue
                for q in D:
                    qq=inc(qe,lq,q)
                    if not fits(qq,EQ):continue
                    kk=k+(int(p==q) if p is not None else 0)
                    if kk>K:continue
                    nx[(p if p is not None else lp,q,pp,qq,kk,
                        p if j==m-2 else p2,p if j==m-1 else p1,
                        q if j==m-1 else q1,q if j==m else qm,
                        q if j==m+1 else qm1,q if j==m+2 else qm2)]+=w
        pre=dict(nx)
    if t==m-1:
        nx=defaultdict(int)
        for (lp,lq,pe,qe,k,p2,p1,q1,qm,qm1,qm2),w in pre.items():
            if inc(pe,lp,pm)==EP:
                nx[(pm,lq,EP,qe,k,p2,p1,q1,qm,qm1,qm2)]+=w
        pre=dict(nx)
    hidden=defaultdict(lambda: defaultdict(int))
    for (_,lq,pe,qe,k,p2,p1,q1,qm,qm1,qm2),w in pre.items():
        if pe!=EP:continue
        head=(p2,p1,q1)+tuple(v for j,v in [(m,qm),(m+1,qm1),(m+2,qm2)] if j<=t and j<=n)+(lq,)
        assert -1 not in head
        hidden[head][(qe,k)]+=w
    heads=sorted(hidden)
    @lru_cache(None)
    def tail(head,j,q,used,extra):
        if j==n:
            need=tuple(EQ[z]-used[z] for z in range(9))
            pop=hidden[head].get((need,K-extra),0)
            return int(pop>0),pop
        support=mass=0
        for z in D:
            ee=inc(used,q,z)
            if not fits(ee,EQ):continue
            kk=extra+(int(z==pm) if t==m-1 and j+1==m else 0)
            if kk>K:continue
            a,b=tail(head,j+1,z,ee,kk)
            support+=a;mass+=b
        return support,mass
    roots={head:(head,t,head[-1],Z,0) for head in heads}
    totals={head:tail(*r) for head,r in roots.items()}
    qF=sum(s for s,mass in totals.values())
    total=sum(mass for s,mass in totals.values())
    def child(state,z):
        head,j,q,e,extra=state
        ee=inc(e,q,z)
        if not fits(ee,EQ):return None
        kk=extra+(int(z==pm) if t==m-1 and j+1==m else 0)
        if kk>K:return None
        return head,j+1,z,ee,kk
    def unrank(rank):
        if not 0<=rank<qF:raise IndexError(rank)
        for head in heads:
            if rank<totals[head][0]:break
            rank-=totals[head][0]
        st=roots[head];key=list(head)
        while st[1]<n:
            for z in D:
                c=child(st,z);cnt=tail(*c)[0] if c else 0
                if rank>=cnt:rank-=cnt
                else:key.append(z);st=c;break
            else:raise AssertionError('unrank')
        assert rank==0
        return tuple(key)
    def rankmass(key):
        head=tuple(key[:len(heads[0])]) if heads else ()
        if head not in roots:return None
        st=roots[head];rank=sum(totals[h][0] for h in heads if h<head)
        for z in key[len(head):]:
            for x in D:
                if x>=z:break
                c=child(st,x)
                if c:rank+=tail(*c)[0]
            st=child(st,z)
            if st is None:return None
        if st[1]!=n:return None
        a,mass=tail(*st)
        return (rank,mass) if a else None
    return {'support':qF,'population':total,'prefix_states':len(pre),'key_heads':len(heads),
            'suffix_states':tail.cache_info().currsize,'unrank':unrank,'rankmass':rankmass}

def x6(w):
    out=[0]*6;ee=[0]*144
    for u in w:out[u//2]+=1 if u%2==0 else -1
    for a,b in zip(w,w[1:]):ee[12*a+b]+=1
    return len(w),tuple(out),tuple(ee)

def signed_obs(p,q):return x6(p),x6(q),sum(a==b for a,b in zip(p,q))

def diff_future(p,q,pp,qq,h,ap=2,pop=2,aq=1,limit=220000):
    """Exhaustive synchronized future tree across all twelve signed append directions.
    Returns witness path or None, visited count; raises if caller's finite budget exceeded.
    """
    conv=lambda s:tuple(2*z for z in s)
    p,q,pp,qq=map(conv,(p,q,pp,qq))
    queue=deque([(p,q,pp,qq,0,0,0,0,())]);seen=set()
    while queue:
        a,b,c,d,ip,ia,jp,ja,path=queue.popleft()
        state=(a,b,c,d,ip,ia,jp,ja)
        if state in seen:continue
        seen.add(state)
        if len(seen)>limit:raise RuntimeError(f'future capacity exceeded {limit}')
        if signed_obs(a,b)!=signed_obs(c,d):return path,len(seen)
        if ip<pop and len(a)>1 and len(c)>1:
            queue.append((a[:-1],b,c[:-1],d,ip+1,ia,jp,ja,path+('POP_P',)))
        if jp<h and len(b)>1 and len(d)>1:
            queue.append((a,b[:-1],c,d[:-1],ip,ia,jp+1,ja,path+('POP_Q',)))
        if ia<ap:
            for z in range(12):queue.append((a+(z,),b,c+(z,),d,ip,ia+1,jp,ja,path+(f'APPEND_P_{z}',)))
        if ja<aq:
            for z in range(12):queue.append((a,b+(z,),c,d+(z,),ip,ia,jp,ja+1,path+(f'APPEND_Q_{z}',)))
    return None,len(seen)

def validate_small():
    stats=Counter(); examples=[]
    cfg=[(4,5,3),(4,5,4),(4,5,5),(4,6,3),(4,6,4),(4,6,5),(4,6,6),
         (5,6,4),(5,6,5),(5,6,6),(5,7,4),(5,7,5),(5,7,6),(5,7,7)]
    cache={}
    for m,n,t in cfg:
        if (m,n) not in cache:
            fibers=defaultdict(list)
            for p1 in product(D,repeat=m-1):
                for q1 in product(D,repeat=n-1):
                    p=(A,)+p1;q=(A,)+q1
                    fibers[obs(p,q)].append((p,q))
            cache[(m,n)]=fibers
        for phi,hist in sorted(cache[(m,n)].items(),key=lambda r:(-len(r[1]),repr(r[0])))[:35]:
            orig=Counter(key_dp(p,q,t) for p,q in hist)
            assert len(orig)==len({repair473(p,q,t) for p,q in hist})
            mapping=defaultdict(set);inverse=defaultdict(set)
            for p,q in hist:
                mapping[key_dp(p,q,t)].add(repair473(p,q,t))
                inverse[repair473(p,q,t)].add(key_dp(p,q,t))
            assert all(len(x)==1 for x in mapping.values())
            assert all(len(x)==1 for x in inverse.values())
            r=solve(phi,t)
            assert r['support']==len(orig) and r['population']==len(hist),(m,n,t,phi,r)
            for i,k in enumerate(sorted(orig)):
                assert r['rankmass'](k)==(i,orig[k])
                assert r['unrank'](i)==k
                stats['classes']+=1
            stats['fibers']+=1
            stats['suffix_states']+=r['suffix_states']
            stats['max_class_mass']=max(stats['max_class_mass'],max(orig.values()))
        stats['configs']+=1
    return dict(stats)

def witnesses():
    # All members of each witness pair have identical full initial X6 observer and R469(t=n).
    m1=6;p1=(A,)*m1
    q1=(A,)*7+(B,)+(A,)*2+(C,)+(A,)*3
    q2=(A,)*7+(C,)+(A,)*2+(B,)+(A,)*3
    m2=11;q3=(A,)*13
    p3=(A,)*3+(C,)+(A,)*4+(B,)+(A,)*2
    p4=(A,)*3+(B,)+(A,)*4+(C,)+(A,)*2
    m3=6;p5=(A,)*m3
    q5=(A,)*4+(B,)+(A,)*3+(C,)+(A,)*4
    q6=(A,)*4+(C,)+(A,)*3+(B,)+(A,)*4
    cases=[('Q_m_plus_2',p1,q1,p1,q2,('APPEND_P_0','APPEND_P_2')),
           ('P_m_minus_2',p3,q3,p4,q3,('POP_P','POP_P')),
           ('Q_m_minus_1',p5,q5,p5,q6,('POP_P','POP_P','APPEND_P_2'))]
    results=[]
    for name,p,q,pp,qq,path in cases:
        assert obs(p,q)==obs(pp,qq)
        assert repair469(p,q,len(q))==repair469(pp,qq,len(qq))
        assert repair473(p,q,len(q))!=repair473(pp,qq,len(qq))
        # Confirm exact displayed witness and full initial observer.
        a,b,c,d=map(lambda w:tuple(2*z for z in w),(p,q,pp,qq)); obs_list=[signed_obs(a,b)]
        for s in path:
            if s=='POP_P':a=a[:-1];c=c[:-1]
            elif s.startswith('APPEND_P_'):
                z=int(s.rsplit('_',1)[-1]);a=a+(z,);c=c+(z,)
            else:raise AssertionError(s)
            obs_list.append(signed_obs(a,b))
        assert obs_list[-1]!=signed_obs(c,d)
        results.append({'name':name,'m':len(p),'n':len(q),'P1':''.join('ABC'[z] for z in p),
                        'Q1':''.join('ABC'[z] for z in q),'P2':''.join('ABC'[z] for z in pp),
                        'Q2':''.join('ABC'[z] for z in qq),'same_phi_and_R469':True,
                        'witness_path':list(path),'initial_K':obs(p,q)[-1],
                        'final_K':[signed_obs(a,b)[-1],signed_obs(c,d)[-1]]})
    return results

def future_audit():
    stats=Counter();record=[]
    # Small configs: complete legal future action tree comparisons from selected full-observer fibers.
    for m,n,t in [(4,5,5),(4,5,4),(4,5,3),(4,6,6),(4,6,5),(5,6,6)]:
        fibers=defaultdict(list)
        for pw in product(D,repeat=m-1):
            for qw in product(D,repeat=n-1):
                p=(A,)+pw;q=(A,)+qw
                fibers[obs(p,q)].append((p,q))
        eq_local=0;diff_local=0
        for his in fibers.values():
            if len(his)<2:continue
            for i in range(len(his)):
                for j in range(i+1,len(his)):
                    p,q=his[i];pp,qq=his[j]
                    equal=repair473(p,q,t)==repair473(pp,qq,t)
                    if equal and eq_local>=1:continue
                    if not equal and diff_local>=3:continue
                    # Full tree may have many states; limit is high enough for these small examples.
                    path,states=diff_future(p,q,pp,qq,n-t)
                    assert (path is None)==equal,(m,n,t,p,q,pp,qq,path)
                    stats['equal_pairs' if equal else 'distinct_pairs']+=1
                    if equal:eq_local+=1
                    else:diff_local+=1
                    stats['future_states']+=states
                    if len(record)<5:record.append({'m':m,'n':n,'t':t,'equal':equal,'states':states,'path':path})
                    if eq_local>=1 and diff_local>=3:break
                if eq_local>=1 and diff_local>=3:break
            if eq_local>=1 and diff_local>=3:break
        stats['configs']+=1
    return dict(stats),record

def large_case():
    m=35;n=56;p=(A,)*m
    q=(A,)
    for z in (B,)*14+(C,)*12:q+=(z,A)
    q+=(A,)*3
    assert len(q)==n
    out=[]
    for t in (m-1,m,m+1,m+2,n):
        z=solve(obs(p,q),t)
        assert z['population']==11154643500
        for i in (0,1,10,100,1000):
            if i<z['support']:assert z['rankmass'](z['unrank'](i))[0]==i
        out.append({'t':t,'support':z['support'],'population':z['population'],
                    'prefix_states':z['prefix_states'],'suffix_states':z['suffix_states']})
    return out

if __name__=='__main__':
    result={'stage':'473-B','scope':'ternary original directions in signed X6; all 12 future APPEND directions',
            'small_dp':validate_small(),'strict_witnesses':witnesses(),
            'future_audit':None,'large':None,'success':False}
    result['future_audit']=future_audit()
    result['large']=large_case()
    result['success']=True
    print(json.dumps(result,ensure_ascii=False,indent=2))
