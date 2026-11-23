from itertools import combinations,product

def bit(p,i): return 0 if i==0 else (p>>(i-1))&1
def ell(p,i):
    for d in range(1,5):
        e=(i-d)%4
        if bit(p,e)!=bit(p,(e+1)%4):return e

def cuts(i,j):
    pairs=[(p,(1<<ell(p,i))|(1<<(4+ell(p,j)))) for p in range(1,8) if bit(p,i)!=bit(p,j)]
    out={}
    for U in range(1,256):
        P=tuple(p-1 for p,m in pairs if U&m==m)
        if P:out[P]=min(out.get(P,8),U.bit_count())
    return list(out.items())
C={(i,j):cuts(i,j) for i,j in combinations(range(4),2)}

def stable(x,q,u):
    return all(any(sum(x[p] for p in P)>q*m+2*u for P,m in cs) for cs in C.values())
def old(x,q,u):
    for i,j in C:
        D=sum(x[p-1] for p in range(1,8) if bit(p,i)!=bit(p,j))
        if D<2*q+2*u+1+(2*u if (j-i)%2 else 0):return False
    return True

def edges(x,q,u):
    for i in range(4):
        t=(i+1)%4
        N=[sum(x[p-1] for p in range(1,8) if bit(p,i)!=bit(p,t) and ell(p,i)==e) for e in range(4)]
        D=sum(N);B=sum(min(q,n) for n in N)
        if D<q+B+4*u+1:return False
    return True

def comp(k,n):
    if n==1:yield (k,);return
    for a in range(k+1):
        for t in comp(k-a,n-1):yield (a,)+t

if __name__=='__main__':
    for q in [5,6,7,10,100]:
        for k in [8,9]:
            a=[];b=[]
            for G in combinations([3,5,6],2):
                for z in comp(k-4,7):
                    x=tuple(z[p-1]+(2*q+2 if p in G else 0) for p in range(1,8))
                    if old(x,q,1) and stable(x,q,1):
                        a.append(x)
                        if edges(x,q,1):b.append(x)
            print(q,k,len(a),len(b),b[:10])

def direct_group_test():
    cases=0
    for n in range(7):
        universe=range(1<<n); full=(1<<n)-1
        for N in comp(n,3):
            masks=[];offset=0
            for m in N:
                masks.append(((1<<m)-1)<<offset);offset+=m
            for q in range(3):
                src=[w for w in universe if all((w&m).bit_count()<=q for m in masks)]
                dst=[w for w in universe if (w^full).bit_count()<=q]
                B=sum(min(q,m) for m in N)
                for u in range(3):
                    near0={w for w in universe if any((w^v).bit_count()<=2*u for v in src)}
                    near1={w for w in universe if any((w^v).bit_count()<=2*u for v in dst)}
                    both=near0&near1
                    for s in universe:
                        S=[(s&m).bit_count() for m in masks]
                        O=sum(max(0,v-q) for v in S)
                        P=sum(min(v,max(0,m-q)) for v,m in zip(S,N))
                        r=n-q-B-2*u
                        predicted=O<=2*u and P>=r and r<=2*u
                        actual=any((v|s) in both for v in src)
                        assert predicted==actual,(N,q,u,s,predicted,actual)
                        cases+=1
    print('joint prefix cases:',cases)

def reachability_test():
    from itertools import permutations
    from collections import deque
    cases=0
    for n in (2,3):
        for tail in permutations(range(1,1<<n),3):
            c=(0,)+tail
            for q in range(3):
                visited={(0,0)}; todo=deque(visited)
                while todo:
                    i,w=todo.popleft();t=(i+1)%4;change=c[i]^c[t];miss=change
                    while True:
                        if miss.bit_count()<=q:
                            s=change^miss;v=(t,(w&~s)|(c[t]&s))
                            if v not in visited:visited.add(v);todo.append(v)
                        if miss==0:break
                        miss=(miss-1)&change
                for i in range(4):
                    groups=[0]*4; const=0
                    for k in range(n):
                        p=sum(((c[j]>>k)&1)<<(j-1) for j in (1,2,3))
                        if p:groups[ell(p,i)]|=1<<k
                        else:const|=1<<k
                    actual={w for phase,w in visited if phase==i}
                    expected={c[i]^m for m in range(1<<n) if not m&const and all((m&g).bit_count()<=q for g in groups)}
                    assert actual==expected,(c,q,i,actual,expected)
                    cases+=1
    print('stable reachability phase cases:',cases)

if __name__=='__main__':
    direct_group_test();reachability_test()
