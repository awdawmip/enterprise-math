from R284GE_exact_adjacent_rollback_checker import bit, ell, stable, old, edges, comp
from itertools import combinations, product
def distance(x,s,i,j,q):
    t=(i+1)%4
    demand=[]
    for p in range(1,8):
        m=x[p-1];v=s[p-1]
        if bit(p,i)!=bit(p,j):
            demand.append((m-v,(1<<ell(p,i))|(1<<(4+ell(p,j)))))
        if bit(p,t)!=bit(p,j):
            demand.append((v,1<<(4+ell(p,j))))
    return max(sum(w for w,M in demand if U&M==M)-q*U.bit_count() for U in range(256))


def verify(q,u,k):
    stable_count=survivors=checks=0
    for G in combinations((3,5,6),2):
        for z in comp(k-4*u,7):
            x=tuple(z[p-1]+(2*q+2*u if p in G else 0) for p in range(1,8))
            if not (old(x,q,u) and stable(x,q,u)):continue
            stable_count+=1
            if not edges(x,q,u):continue
            survivors+=1
            assert G in ((3,5),(5,6))
            i=0 if G==(3,5) else 1
            t=(i+1)%4
            R=sum(x[p-1] for p in range(1,8) if p not in G)
            assert R<=min(q,4*u-2)
            for g in G:
                h=next(p for p in G if p!=g)
                j=next(j for j in range(4) if j not in (i,t) and bit(g,j)!=bit(g,i) and bit(h,j)==bit(h,i))
                v=x[g-1]-2*q+R-2*u
                w=x[h-1]-2*q+R-2*u
                assert 1<=v<=q+1 and 1<=w<=q+1
                ranges=[range(x[p-1]+1) if p not in G and bit(p,i)!=bit(p,t) else (0,) for p in range(1,8)]
                ranges[g-1]=(v,)
                for s in product(*ranges):
                    d=distance(x,s,i,j,q)
                    assert d<=2*u,(q,u,k,x,G,g,s,d)
                    checks+=1
    print(f'q={q} u={u} k={k}: stable={stable_count} GE1 survivors={survivors} third-phase checks={checks}; all blocked')
    return checks

if __name__=='__main__':
    params=[(q,1,k) for q in (5,6,7,10,100) for k in (8,9)]
    params += [(9,2,k) for k in (16,17)] + [(13,3,k) for k in (24,25)]
    total=sum(verify(*p) for p in params)
    print('all explicit threshold witness comparisons:',total)
