"""Stage480-B | Exact 2-Q-POP suffix BRC on a typed native X6 3-direction observer.
Scientific source pin: Stage477-B (Global bf84bd7c61a2444b59b1da96be57df0e9ae47e53;
EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419). Independent exact integer implementation.
"""
from itertools import product
from functools import lru_cache
from collections import defaultdict, Counter
from math import factorial
import json
A = 'ABC'
PAIRS = tuple(x+y for x in A for y in A)
IX={z:i for i,z in enumerate(PAIRS)}
ZERO=(0,)*9

def E(x,y):
    z=[0]*9;z[IX[x+y]]=1;return tuple(z)
def add(*x):return tuple(map(sum,zip(*x)))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def edges(s):
    c=[0]*9
    for x,y in zip(s,s[1:]):c[IX[x+y]]+=1
    return tuple(c)
def baseline(m):return (m-1,)+(0,)*8
def theta(m,w,h):
    return add(baseline(m),E('A',w[0]),edges(w),E(w[-1],'A'),E('A',h[0]),edges(h),E(h[-1],'A'))
def det2(z):
    if len(z)==0:return 1
    if len(z)==1:return z[0][0]
    if len(z)==2:return z[0][0]*z[1][1]-z[0][1]*z[1][0]
    raise AssertionError('3x3 minor maximum')
@lru_cache(None)
def N(l,s,t,e):
    """Directed Euler word count; counts original words, not labelled edges."""
    if l<1 or len(e)!=9 or min(e)<0 or sum(e)!=l-1:return 0
    if l==1:return int(s==t and e==ZERO)
    o=[sum(e[i*3:i*3+3]) for i in range(3)]
    inn=[sum(e[3*j+i] for j in range(3)) for i in range(3)]
    si=A.index(s);ti=A.index(t)
    if any(o[i]-inn[i]!=(i==si)-(i==ti) for i in range(3)):return 0
    active=[i for i in range(3) if o[i]+inn[i] or i==si or i==ti]
    rest=[i for i in active if i!=ti]
    if any(o[i]==0 for i in rest):return 0
    L=[[o[i]-e[3*i+i] if i==j else -e[3*i+j] for j in rest] for i in rest]
    tau=det2(L)
    if tau<=0:return 0
    v=tau*factorial(o[ti]);den=1
    for i in rest:v*=factorial(o[i]-1)
    for x in e:den*=factorial(x)
    assert v%den==0
    return v//den
@lru_cache(None)
def N_recur(s,t,e):
    if min(e)<0:return 0
    if sum(e)==0:return int(s==t)
    v=0
    for x in A:
        pos=IX[s+x]
        if e[pos]:
            z=list(e);z[pos]-=1
            v+=N_recur(x,t,tuple(z))
    return v

def compositions(bnd,tot,p=()):
    if len(p)==8:
        if 0<=tot<=bnd[8]:yield p+(tot,)
        return
    for x in range(min(tot,bnd[len(p)])+1):
        yield from compositions(bnd,tot-x,p+(x,))

@lru_cache(None)
def mass2(s,t,ew,T,u,m,d,c):
    """Number of original hidden words H with fixed last two letters (d,c).
    For u=1 only d='A' is a boundary marker before H; it is not an H letter.
    """
    if u==1:
        if d!='A':return 0
        residual=sub(T,add(baseline(m),E('A',s),ew,E(t,'A'),E('A',c),E(c,'A')))
        return int(residual==ZERO)
    residual=sub(T,add(baseline(m),E('A',s),ew,E(t,'A'),E(d,c),E(c,'A')))
    if min(residual)<0:return 0
    total=0
    for p in A:
        rest=sub(residual,E('A',p))
        if min(rest)>=0:total+=N(u-1,p,d,rest)
    return total

def summary(k,u,T):
    m=2*k+2;room=sub(T,baseline(m))
    if min(room)<0:return dict(classes=0,population=0,supported_types=0)
    num=pop=typ=0
    D='A' if u==1 else A
    for ew in compositions(room,k-1):
        for s in A:
            for t in A:
                nw=N(k,s,t,ew)
                if nw==0:continue
                for d in D:
                    for c in A:
                        mass=mass2(s,t,ew,T,u,m,d,c)
                        if mass:
                            num+=nw;pop+=nw*mass;typ+=1
    return dict(classes=num,population=pop,supported_types=typ)

def suffixes(w,u,T):
    dset='A' if u==1 else A
    return [(d,c) for d in dset for c in A if mass2(w[0],w[-1],edges(w),T,u,2*len(w)+2,d,c)]

def prefix_support(pre,k,u,T):
    if len(pre)==k:return len(suffixes(pre,u,T))
    if not pre:return summary(k,u,T)['classes']
    m=2*k+2;ep=edges(pre);room=sub(T,add(baseline(m),ep))
    if min(room)<0:return 0
    result=0;remain=k-len(pre)
    for g in compositions(room,remain):
        for t in A:
            nw=N(remain+1,pre[-1],t,g)
            if nw:
                e=add(ep,g)
                masscount=sum(bool(mass2(pre[0],t,e,T,u,m,d,c)) for d in ('A' if u==1 else A) for c in A)
                result+=nw*masscount
    return result

def rank_key(w,d,c,u,T):
    if mass2(w[0],w[-1],edges(w),T,u,2*len(w)+2,d,c)==0:raise ValueError('unsupported')
    result=0;pre=''
    for x in w:
        for y in A:
            if y==x:break
            result+=prefix_support(pre+y,len(w),u,T)
        pre+=x
    for z in suffixes(w,u,T):
        if z==(d,c):break
        result+=1
    return result

def unrank_key(r,k,u,T):
    tot=summary(k,u,T)['classes']
    if r<0 or r>=tot:raise ValueError('rank outside support')
    pre=''
    for _ in range(k):
        for x in A:
            n=prefix_support(pre+x,k,u,T)
            if r<n:
                pre+=x;break
            r-=n
        else:raise AssertionError('unrank exhausted')
    return (pre,*suffixes(pre,u,T)[r])

def brute(k,u):
    m=2*k+2;fam=defaultdict(lambda:defaultdict(int)); histories=0
    for w in map(''.join,product(A,repeat=k)):
        for h in map(''.join,product(A,repeat=u)):
            d=h[-2] if u>=2 else 'A'
            fam[theta(m,w,h)][(w,d,h[-1])]+=1
            histories+=1
    class_checks=rank_checks=0
    for T,cs in fam.items():
        got=summary(k,u,T)
        assert got['classes']==len(cs),(k,u,T,got,len(cs))
        assert got['population']==sum(cs.values())
        for i,((w,d,c),mass) in enumerate(sorted(cs.items())):
            assert mass2(w[0],w[-1],edges(w),T,u,m,d,c)==mass
            class_checks+=1
            if k<=2:
                assert rank_key(w,d,c,u,T)==i
                assert unrank_key(i,k,u,T)==(w,d,c)
                rank_checks+=1
    return dict(k=k,u=u,fibers=len(fam),histories=histories,class_checks=class_checks,rank_checks=rank_checks)

def first_witness():
    for u in range(2,8):
        k=1;m=2*k+2
        d=defaultdict(list)
        for w in map(''.join,product(A,repeat=k)):
            for h in map(''.join,product(A,repeat=u)):
                d[(theta(m,w,h),w,h[-1])].append(h)
        for (T,w,c),v in d.items():
            for h1 in v:
                for h2 in v:
                    if h1[-2]!=h2[-2]:
                        q1='A'*m+w+'A'+h1+'A'
                        q2='A'*m+w+'A'+h2+'A'
                        first1=sub(T,E(c,'A'))
                        first2=sub(T,E(c,'A'))
                        second1=sub(first1,E(h1[-2],c))
                        second2=sub(first2,E(h2[-2],c))
                        assert first1==first2 and second1!=second2
                        return {'k':k,'u':u,'P':'A'*m,'Q1':q1,'Q2':q2,'W':w,'H1':h1,'H2':h2,'theta':T,'after_pop1':first1,'after_pop2_q1':second1,'after_pop2_q2':second2}
    return None

def mass0(s,t,ew,T,u,m):
    residual=sub(T,add(baseline(m),E('A',s),ew,E(t,'A')))
    if min(residual)<0:return 0
    acc=0
    for p in A:
        for c in A:
            h=sub(residual,add(E('A',p),E(c,'A')))
            if min(h)>=0:acc+=N(u,p,c,h)
    return acc

def summary0(k,u,T):
    m=2*k+2;room=sub(T,baseline(m))
    if min(room)<0:return 0,0
    cats=pop=0
    for ew in compositions(room,k-1):
        for s in A:
            for t in A:
                nw=N(k,s,t,ew)
                if nw:
                    h=mass0(s,t,ew,T,u,m)
                    cats+=nw*bool(h)
                    pop+=nw*h
    return cats,pop

# The entire 12-direction native alphabet: +E1,...,+E6,-E1,...,-E6.
X12='ABCDEFGHIJKL'
def observation(p,q):
    def obs(w):
        z=[0]*6;edges12=[0]*144
        for ch in w:
            j=X12.index(ch)
            z[j%6]+=1 if j<6 else -1
        for a,b in zip(w,w[1:]):edges12[12*X12.index(a)+X12.index(b)]+=1
        return len(w),tuple(z),tuple(edges12)
    return obs(p),obs(q),sum(a==b for a,b in zip(p,q))

def full_future_equiv(p,q1,q2,k):
    """Compare every legal APPEND/POP interleaving, all 12 directions, every step."""
    seen=set();tested=0
    def visit(p,q1,q2,pc,pa,qc,qa):
        nonlocal tested
        key=(p,q1,q2,pc,pa,qc,qa)
        if key in seen:return True
        seen.add(key);tested+=1
        if observation(p,q1)!=observation(p,q2):return False
        ops=[]
        if pc<k and len(p)>1:ops.append(('PPOP',None))
        if qc<2 and len(q1)>1:ops.append(('QPOP',None))
        if pa<k:ops.extend(('PAPP',x) for x in X12)
        if qa<1:ops.extend(('QAPP',x) for x in X12)
        for op,x in ops:
            if op=='PPOP':v=(p[:-1],q1,q2,pc+1,pa,qc,qa)
            elif op=='QPOP':v=(p,q1[:-1],q2[:-1],pc,pa,qc+1,qa)
            elif op=='PAPP':v=(p+x,q1,q2,pc,pa+1,qc,qa)
            else:v=(p,q1+x,q2+x,pc,pa,qc,qa+1)
            if not visit(*v):return False
        return True
    eq=visit(p,q1,q2,0,0,0,0)
    return {'equal':eq,'states':tested,'future_append_direction_count':12}

def same_key_witness():
    k=1;u=4;m=2*k+2;w='A';x='ABAA';y='BAAA'
    assert x!=y and x[-2:]==y[-2:] and theta(m,w,x)==theta(m,w,y)
    return {'k':k,'u':u,'P':'A'*m,'W':w,'H1':x,'H2':y,
      'future_check':full_future_equiv('A'*m,'A'*m+w+'A'+x+'A','A'*m+w+'A'+y+'A',k)}

def run():
    by_type=Counter()
    for n in range(1,7):
        for w in map(''.join,product(A,repeat=n)):
            by_type[(n,w[0],w[-1],edges(w))]+=1
    for (n,s,t,e),cnt in by_type.items():
        assert cnt==N(n,s,t,e)==N_recur(s,t,e)
    results=[brute(k,u) for k in (1,2,3) for u in (1,2,3)]
    cert=first_witness();assert cert
    k,u=12,9;m=2*k+2
    w=('ABCCABCAAB'*4)[:k];h=('BCAACBBC'*4)[:u]
    T=theta(m,w,h)
    large=summary(k,u,T)
    assert 0 < large['classes']<=large['population']<=3**(k+u)
    old_classes,old_population=summary0(k,u,T)
    assert large['population']==old_population and old_classes<=large['classes']
    strong_same=same_key_witness();assert strong_same['future_check']['equal']
    different=full_future_equiv(cert['P'],cert['Q1'],cert['Q2'],1)
    assert not different['equal']
    return {'status':'ALL_ASSERTIONS_PASSED','model':'P=A^m; Q=A^m W A H A; X6 A/B/C restricted directions; k,u>=1; P POP,APPEND <=k, Q POP<=2 APPEND<=1; 12 signed append directions','repair_key':'(W,H[-2:], u>=2); (W,H[-1], boundary A), u=1','euler_types_checked':len(by_type),'small':results,'strict_pop2_witness':cert,'strict_future_check':different,'same_key_distinct_histories':strong_same,'medium':{'k':k,'u':u,'m':m,'n':m+k+u+2,'theta':T,**large,'old_pop0_classes':old_classes,'old_pop0_population':old_population},'arithmetic':'Python arbitrary-precision exact integers'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
