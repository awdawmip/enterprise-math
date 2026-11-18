"""Named-clock axis-pair variance checked against the sequential ordering law."""
from fractions import Fraction as F
from functools import cache
from itertools import combinations
from math import comb, factorial

EDGES = list(combinations(range(6), 2))


def cycles(*paths):
    L = [[0]*6 for _ in range(6)]
    for path in paths:
        for i,j in zip(path,path[1:]+path[:1]):
            L[i][j] += 1
            L[j][i] -= 1
    return L


def K(a,b,c):
    return F(a*b*c,(a+b+c)*(a+b)*(a+c))


def residual(a,b):
    return F(a*b*(a*a+a*b+b*b),(a+b)**2*(a+2*b)*(2*a+b))


def coefficients(a,w,L):
    first=sum(F(L[i][j]*L[i][k],w[i])*K(a[i],a[j],a[k])
              for i in range(6) for j in range(6) for k in range(6))
    second=sum(F(L[i][j]**2,w[i]*w[j])*residual(a[i],a[j]) for i,j in EDGES)
    return first,second


def sequential(a,m,L):
    """Moments of the uncentered statistic by conditioning on the next named axis."""
    @cache
    def moments(r):
        mass=sum(x*y for x,y in zip(a,r))
        if mass==0:
            return F(0),F(0)
        mean=square=F(0)
        for j,left in enumerate(r):
            if not left:
                continue
            chance=F(left*a[j],mass)
            increment=sum(F(L[i][j]*(m[i]-r[i]),m[i]*m[j]) for i in range(j))
            smaller=list(r)
            smaller[j]-=1
            avg,second=moments(tuple(smaller))
            mean+=chance*(increment+avg)
            square+=chance*(increment**2+2*increment*avg+second)
        return mean,square
    mean,square=moments(tuple(m))
    assert mean==sum(L[i][j]*F(a[i],a[i]+a[j]) for i,j in EDGES)
    return square-mean**2


def rank(rows):
    rows=[list(map(F,row)) for row in rows]
    pivot=0
    for c in range(len(rows[0])):
        chosen=next((k for k in range(pivot,len(rows)) if rows[k][c]),None)
        if chosen is None:
            continue
        rows[pivot],rows[chosen]=rows[chosen],rows[pivot]
        v=rows[pivot][c]
        rows[pivot]=[x/v for x in rows[pivot]]
        for k in range(pivot+1,len(rows)):
            w=rows[k][c]
            if w:
                rows[k]=[x-w*y for x,y in zip(rows[k],rows[pivot])]
        pivot+=1
    return pivot


def partitions(n,cap):
    if n==0:
        yield ()
    for k in range(min(n,cap),0,-1):
        for tail in partitions(n-k,k):
            yield (k,)+tail


def edge_constraints(vectors):
    return [[(v[j] if i==r else -v[i] if j==r else 0) for i,j in EDGES]
            for v in vectors for r in range(6)]


def mul(series,order):
    result=[F(1)]+[F(0)]*order
    for term in series:
        result=[sum(result[k-j]*term[j] for j in range(min(k+1,len(term))))
                for k in range(order+1)]
    return result


def K_series(i,j,k,order=8):
    # At epsilon=0 the rates are 1, slopes i,j,k respectively.
    num=mul([(1,i),(1,j),(1,k)],order)
    den=mul([(3,i+j+k),(2,i+j),(2,i+k)],order)
    coeff=[]
    for n in range(order+1):
        coeff.append((num[n]-sum(den[h]*coeff[n-h] for h in range(1,n+1)))/den[0])
    return coeff


def main():
    tri=cycles([0,1,2])
    rect=cycles([0,3,1,4])
    one=(1,)*6
    repeated=(1,1,1,2,2,2)
    partly=(1,1,2,3,4,5)
    distinct=(1,2,3,4,5,6)
    mixed=cycles([0,2,3,5],[1,5,2,4])
    for label,a,L in [('equal triangle',one,tri),('two groups triangle',repeated,tri),
                      ('two groups rectangle',repeated,rect),('split triangle',partly,tri),
                      ('all different triangle',distinct,tri)]:
        c,d=coefficients(a,one,L)
        for N in (1,2):
            assert sequential(a,(N,)*6,L)==c/N+d/N**2
        print(label, 'C1 =',c,'C2 =',d)
    for a,m,L in [(distinct,(1,2,1,2,1,1),mixed),(repeated,(2,1,1,2,2,1),rect),
                  ((F(2,3),1,2,F(7,4),3,5),(2,1,2,1,1,1),mixed)]:
        c,d=coefficients(a,m,L)
        assert sequential(a,m,L)==c+d
    assert coefficients(partly,one,tri)==(F(1,90),F(43,180))
    assert coefficients(distinct,one,tri)==(F(263,12600),F(5767,25200))
    count=0
    for partition in partitions(6,6):
        groups=[]
        start=0
        for size in partition:
            groups.append([int(start<=k<start+size) for k in range(6)])
            start+=size
        assert 15-rank(edge_constraints(groups))==comb(6-len(groups),2)
        count+=1
    assert count==11
    for d in range(6):
        vectors=[[i**k for i in range(6)] for k in range(d+1)]
        assert 15-rank(edge_constraints(vectors))==comb(5-d,2)
    U=[1,-4,6,-4,1,0]
    V=[0,1,-4,6,-4,1]
    L=[[U[i]*V[j]-V[i]*U[j] for j in range(6)] for i in range(6)]
    series=[F(0)]*9
    for i in range(6):
        for j in range(6):
            for k in range(6):
                w=L[i][j]*L[i][k]
                if w:
                    for h,v in enumerate(K_series(i,j,k)):
                        series[h]+=w*v
    expected=252*(F(factorial(8),3**9)-F(9,16))
    assert series==[0]*8+[expected]
    assert coefficients(one,one,L)==(0,147)
    eps=F(1,9)
    c,d=coefficients(tuple(1+eps*i for i in range(6)),one,L)
    assert sequential(tuple(1+eps*i for i in range(6)),one,L)==c+d and c>0
    print('11 rate partitions and 6 moment filtrations checked.')
    print('eighth order Taylor term:',series[-1],'; equal-rate residual:',147)


if __name__=='__main__':
    main()
