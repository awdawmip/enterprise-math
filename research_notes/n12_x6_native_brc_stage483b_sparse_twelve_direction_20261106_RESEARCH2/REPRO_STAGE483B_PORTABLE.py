"""Stage483-B sparse directed Euler-BRC counting, all 12 signed native X6 steps.
Reproduces the large sparse table with exact positive integers; full finite-fiber
and future-operation-tree verifier is REPRO_STAGE483B.py in the stage handoff.
"""
from collections import Counter,defaultdict
from functools import lru_cache
from math import factorial
from itertools import product
import json

D='ABCDEFGHIJKL'  # +E1..+E6,-E1..-E6, six native spatial axes
A='A'
def edges(word):return tuple(sorted((x,y,n) for (x,y),n in Counter(zip(word,word[1:])).items()))
def subtract(e,f):
    z=Counter({(x,y):n for x,y,n in e})
    for x,y,n in f:z[x,y]-=n
    if min(z.values(),default=0)<0:return None
    return tuple(sorted((x,y,n) for (x,y),n in z.items() if n>0))
def combine(*sets):
    z=Counter()
    for e in sets:
        for x,y,n in e:z[x,y]+=n
    return tuple(sorted((x,y,n) for (x,y),n in z.items() if n>0))
def determinant(mat):
    n=len(mat)
    if not n:return 1
    a=[list(row) for row in mat];sgn=1;prev=1
    for j in range(n-1):
        if a[j][j]==0:
            p=next((i for i in range(j+1,n) if a[i][j]!=0),None)
            if p is None:return 0
            a[j],a[p]=a[p],a[j];sgn=-sgn
        pivot=a[j][j]
        for i in range(j+1,n):
            for k in range(j+1,n):
                num=pivot*a[i][k]-a[i][j]*a[j][k]
                assert num%prev==0
                a[i][k]=num//prev
            a[i][j]=0
        prev=pivot
    return sgn*a[-1][-1]
@lru_cache(None)
def N(n,s,t,e):
    if n<1 or sum(v for _,_,v in e)!=n-1:return 0
    if n==1:return int(s==t and not e)
    out=Counter();inc=Counter();E={}
    for x,y,v in e:
        if v<0:return 0
        out[x]+=v;inc[y]+=v;E[x,y]=v
    V=sorted(set(out)|set(inc)|{s,t})
    if any(out[x]-inc[x]!=int(x==s)-int(x==t) for x in V):return 0
    W=[x for x in V if x!=t]
    if any(out[x]==0 for x in W):return 0
    tau=determinant([[out[x]-E.get((x,x),0) if x==y else -E.get((x,y),0)
                      for y in W] for x in W])
    if tau<=0:return 0
    num=tau*factorial(out[t]);den=1
    for x in W:num*=factorial(out[x]-1)
    for _,_,v in e:den*=factorial(v)
    assert num%den==0
    return num//den
@lru_cache(None)
def suffix(R,u,r):
    assert 0<=r<=u
    pairs=tuple((x,y) for x,y,v in R);start=tuple(v for x,y,v in R)
    back=defaultdict(list)
    for i,(x,y) in enumerate(pairs):back[y].append((x,i))
    state={(A,start):1};trans=0
    for _ in range(r):
        next_=defaultdict(int)
        for (tip,rest),ways in state.items():
            for x,j in back[tip]:
                if rest[j]:
                    v=list(rest);v[j]-=1;next_[(x,tuple(v))]+=ways;trans+=1
        state=dict(next_)
    support=mass=0
    for (tip,rest),ways in state.items():
        rem=tuple((x,y,v) for (x,y),v in zip(pairs,rest) if v)
        n=N(u-r+2,A,tip,rem)
        support+=ways*(n>0);mass+=ways*n
    assert mass==N(u+2,A,A,R)
    return support,mass,trans

def distribute(bds,total,i=0,p=()):
    if i==len(bds):
        if total==0:yield p
        return
    for x in range(min(bds[i],total)+1):
        yield from distribute(bds,total-x,i+1,p+(x,))

def fiber(k,u,r,Theta):
    m=2*k+2;starter=edges(A*m);budget=subtract(Theta,starter)
    if budget is None:return None
    pairs=tuple((x,y) for x,y,v in budget)
    letters=sorted({A}|{v for x,y,n in budget for v in (x,y)})
    types=0;values=defaultdict(int);q=mass=0
    for seq in distribute([v for x,y,v in budget],k-1):
        eW=tuple((x,y,v) for (x,y),v in zip(pairs,seq) if v)
        for s in letters:
            for t in letters:
                count=N(k,s,t,eW)
                if count==0:continue
                base=combine(starter,((A,s,1),),eW,((t,A,1),))
                R=subtract(Theta,base)
                if R is None or suffix(R,u,r)[0]==0:continue
                types+=1;values[R]+=count
    transitions=0
    for R,mult in values.items():
        a,b,steps=suffix(R,u,r)
        q+=mult*a;mass+=mult*b;transitions+=steps
    return dict(r=r,classes=q,population=mass,w_types=types,distinct_R=len(values),unique_R_transitions=transitions)

def run():
    k=16;u=13;W=('ABGA'*4)[:k];H=('AGBA'*4)[:u]
    theta=edges(A*(2*k+2)+W+A+H+A)
    answer=[fiber(k,u,r,theta) for r in (0,1,3,6,9,13)]
    assert [v['classes'] for v in answer]==[880898,2184817,8293813,47641484,175874227,333915624]
    assert all(v['population']==333915624 for v in answer)
    assert all(v['w_types']==1154 and v['distinct_R']==162 for v in answer)
    assert [v['unique_R_transitions'] for v in answer]==[0,411,2788,13558,28630,37903]
    # Exercise all signed axes as a legal primitive word, including reversal pairs.
    for c in D:assert N(3,A,A,edges(A+c+A))==1
    # Verify the directed Euler formula by exhaustive signed-word counting.
    total=0;classes=set()
    for n in range(1,6):
        bucket=Counter()
        for seq in product('ABG',repeat=n):
            w=''.join(seq);bucket[(w[0],w[-1],edges(w))]+=1;total+=1
        for (s,t,e),v in bucket.items():assert N(n,s,t,e)==v
        classes.update(bucket)
    assert total==363 and len(classes)==300
    return {'status':'ALL_ASSERTIONS_PASSED','signed_directions':12,'large_k':k,'large_u':u,
            'theta':theta,'support_edges':len(theta),'exact_table':answer,
            'euler_brute_words':total,'euler_types':len(classes)}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))
