"""Exact finite unitary quotients, twists and the characteristic-seven curve."""
import argparse
import json
from collections import deque
from itertools import product
from pathlib import Path


def local(n):
    m=2**n
    q=m*m
    ring=list(range(q))
    enc=lambda x,y:x%m+m*(y%m)
    conj=[enc(i%m-i//m,-(i//m)) for i in ring]
    norm=[((i%m)**2-(i%m)*(i//m)+(i//m)**2)%m for i in ring]
    add=[[enc(a%m+b%m,a//m+b//m) for b in ring] for a in ring]
    mul=[[enc((a%m)*(b%m)-(a//m)*(b//m),(a%m)*(b//m)+(a//m)*(b%m)-(a//m)*(b//m))
          for b in ring] for a in ring]
    neg2=[enc(-2*(a%m),-2*(a//m)) for a in ring]
    proper=set()
    naive=set()
    for c in ring:
        for a in ring:
            if (norm[a]+2*norm[c]-1)%m:
                continue
            for u in ring:
                if norm[u]%2==0 or (2*(norm[u]-1))%m:
                    continue
                g=(a,neg2[mul[u][conj[c]]],c,mul[u][conj[a]])
                naive.add(g)
                if norm[u]==1:
                    proper.add(g)
    if n<=2:
        direct=set()
        for a,b,c,d in product(ring,repeat=4):
            if (norm[a]+2*norm[c]-1)%m or (norm[b]+2*norm[d]-2)%m:
                continue
            if mul[conj[a]][b]!=neg2[mul[conj[c]][d]]:
                continue
            determinant=enc((mul[a][d]%m)-(mul[b][c]%m),(mul[a][d]//m)-(mul[b][c]//m))
            if norm[determinant]%2:
                direct.add((a,b,c,d))
        assert direct==naive
    assert len(proper)==9*2**(4*n-2)
    assert len(naive)==len(proper)*(1 if n==1 else 2)
    output=dict(n=n,liftable=len(proper),gram_invertible=len(naive),all_matrices_checked=n<=2)
    if n==3:
        def times(g,h):
            a,b,c,d=g;e,f,i,j=h
            return (add[mul[a][e]][mul[b][i]],add[mul[a][f]][mul[b][j]],
                    add[mul[c][e]][mul[d][i]],add[mul[c][f]][mul[d][j]])
        ident=(1,0,0,1)
        generated={ident}
        generators=[]
        sizes=[]
        for g in sorted(proper):
            if g in generated:
                continue
            generators.append(g)
            queue=deque(generated)
            while queue:
                current=queue.popleft()
                for h in generators:
                    new=times(current,h)
                    if new not in generated:
                        generated.add(new);queue.append(new)
            sizes.append(len(generated))
        assert generated==proper
        output['generators_mod8']=[[[z%m,z//m] for z in g] for g in generators]
        output['successive_generated_sizes']=sizes
    return output


def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def newton(power_sums):
    c=[1]
    for k in range(1,len(power_sums)+1):
        numerator=-sum(c[k-i]*power_sums[i-1] for i in range(1,k+1))
        assert numerator%k==0
        c.append(numerator//k)
    return c


def twists(nmax):
    # h(T) coefficients, high to low. Power sums include the four embeddings.
    h=[1,5,0,245,2401]
    p=[4]
    for j in range(1,8*nmax+1):
        if j<=4:
            p.append(-sum(h[i]*p[j-i] for i in range(1,j))-j*h[j])
        else:
            p.append(-sum(h[i]*p[j-i] for i in range(1,5)))
    hm=lambda m:newton([p[j*m] for j in (1,2,3,4)])
    rows=[]
    for n in range(1,nmax+1):
        polys=[]
        for k in range(4):
            # Trace of the j-th power of S^k J^n on E=B^2, using JSJ^-1=S^-1.
            traces=[]
            for j in range(1,9):
                if n%2:
                    value=0 if j%2 else 2*p[n*j//2]
                else:
                    value=(2,0,-2,0)[k*j%4]*p[n*j//2]
                traces.append(value)
            pol=newton(traces);polys.append(pol)
            if n%2:
                hcur=hm(n)
                expected=[hcur[i//2] if i%2==0 else 0 for i in range(9)]
            elif k in (0,2):
                hcur=hm(n//2)
                if k==2:
                    hcur=[v*(-1)**i for i,v in enumerate(hcur)]
                expected=poly_mul(hcur,hcur)
            else:
                hcur=hm(n)
                expected=[hcur[i//2]*(-1)**(i//2) if i%2==0 else 0 for i in range(9)]
            assert pol==expected
        assert len(set(map(tuple,polys)))==(1 if n%2 else 3)
        rows.append(dict(n=n,polynomials_high_first=polys,point_counts=[sum(a) for a in polys],
                         field_automorphisms=2 if n%2 else 4,quotients_defined=n%3==0))
    return rows


def curve_count(degree,lower):
    # F7[X]/(X^degree + sum lower_i X^i); certify field by nonzero unit inversion.
    q=7**degree
    coords=[[(a//7**i)%7 for i in range(degree)] for a in range(q)]
    def enc(a):
        return sum((v%7)*7**i for i,v in enumerate(a))
    def add(x,y):
        return enc([a+b for a,b in zip(coords[x],coords[y])])
    def mul(x,y):
        a=poly_mul(coords[x],coords[y])
        for j in reversed(range(degree,len(a))):
            for i,c in enumerate(lower):
                a[j-degree+i]-=a[j]*c
        return enc(a[:degree])
    def power(x,e):
        z=1
        while e:
            if e&1:z=mul(z,x)
            x=mul(x,x);e//=2
        return z
    roots=[[] for _ in range(q)]
    for y in range(q):
        assert not y or power(y,q-1)==1
        roots[mul(y,y)].append(y)
    E=C=1   # single rational point over infinity on each smooth model
    for x in range(q):
        x2=mul(x,x)
        ys=roots[add(add(mul(x2,x),x2),1)]
        E+=len(ys)
        for y in ys:
            C+=len(roots[mul(y,add(x2,2))])
    return dict(degree=degree,lower=lower,E_points=E,C_points=C,prym_trace=E-C)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--out',type=Path)
    a=p.parse_args()
    samples=twists(12)
    # Choose and certify a small monic degree-four field model by direct unit tests.
    models=[(1,[0]),(2,[1,0]),(3,[1,0,1])]
    for c in range(1,7):
        try:
            fourth=curve_count(4,[c,1,0,0])
            break
        except AssertionError:
            continue
    else: raise AssertionError('no degree-four model found')
    counts=[curve_count(d,l) for d,l in models]+[fourth]
    for d,row in enumerate(counts,1):
        assert row['prym_trace']==-samples[d-1]['polynomials_high_first'][0][1]
    docs=dict(local=[local(n) for n in range(1,4)],curve=counts,twists=samples,
              basis_order_for_mod8='matrix row-major; [a,b] means a+b*w, w^2+w+1=0')
    text=json.dumps(docs,sort_keys=True,indent=2)+'\n'
    if a.out:a.out.write_text(text)
    else:print(text,end='')


if __name__=='__main__':
    main()
