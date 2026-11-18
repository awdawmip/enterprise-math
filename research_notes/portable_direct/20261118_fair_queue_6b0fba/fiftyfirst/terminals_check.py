"""Positive terminal-only probes. Python 3.9+, no external packages."""
from fractions import Fraction as F
from itertools import combinations
import json

def coeffs(edges):
    # Entries are row-major. Left multiplication by L(t)U(r) puts one mass at
    # the new right endpoint; contiguous segments compose without extra mass.
    M=[(1,0,0,1)]+[(0,0,0,0)]*3
    for r in edges:
        U=[(a+r*c,b+r*d,c,d) for a,b,c,d in M]
        M=[(a,b,c+(U[i-1][0] if i else 0),d+(U[i-1][1] if i else 0))
           for i,(a,b,c,d) in enumerate(U)]
    return M

def coords(x,R):
    edges=[b-a for a,b in zip([0]+x,x+[R])]
    M=coeffs(edges)
    one,two,three=M[1:]
    return [one[0],one[1],two[2],two[0],two[1],three[2]]

def det(matrix):
    a=[list(map(F,row)) for row in matrix]
    ans=F(1)
    for i in range(len(a)):
        piv=next((j for j in range(i,len(a)) if a[j][i]),None)
        if piv is None:return F(0)
        if piv!=i:
            a[i],a[piv]=a[piv],a[i];ans=-ans
        g=a[i][i]; ans*=g
        for j in range(i+1,len(a)):
            t=a[j][i]/g
            a[j]=[v-t*w for v,w in zip(a[j],a[i])]
    return ans

def value(edges):
    M=coeffs(edges)
    c1,c2,c3=[a+d for a,b,c,d in M[1:]]
    n,S=len(edges),sum(edges)
    assert c1==n*S
    return F(8,n*n*S*S)*(F(c2,c1)**2-F(2*c3,c1))

def resistance_beta(edges):
    n,S=len(edges),sum(edges)
    pts=[sum(edges[:j]) for j in range(n)]
    R=[[F(abs(x-y)*(S-abs(x-y)),S) for x in pts] for y in pts]
    sums=[sum(row) for row in R]
    return F(2,n**4*S*S)*(n*n*sum(v*v for row in R for v in row)-
                            2*n*sum(v*v for v in sums)+sum(sums)**2)

def jacobian(pos,R):
    # Only two edge lengths vary: each coefficient is quadratic in one x_j.
    # The symmetric difference is its exact linear coefficient.
    D=[]
    step=F(1,3)
    for i in range(len(pos)):
        u=pos[:]; v=pos[:]
        u[i]+=step;v[i]-=step
        hi,lo=coords(u,R),coords(v,R)
        D.append([(a-b)/(2*step) for a,b in zip(hi,lo)])
    return [list(row) for row in zip(*D)]

def check_green(edges):
    pos=[sum(edges[:i]) for i in range(1,len(edges))]
    R=sum(edges)
    H=[[F(R-x,R),F(x,R)] for x in pos]
    G=[[F(min(x,y)*(R-max(x,y)),R) for y in pos] for x in pos]
    one=[[sum(h[i]*h[j] for h in H) for j in range(2)] for i in range(2)]
    two=[[sum(H[k][i]*g*H[l][j] for k,row in enumerate(G) for l,g in enumerate(row))
          for j in range(2)] for i in range(2)]
    sig=sum(sum(row)**2 for row in G)
    a,b,c,d=map(list,zip(*coeffs(edges)))
    def divide(num,den):
        q=[]
        for i,x in enumerate(num):
            q.append(F(x-sum(q[j]*den[i-j] for j in range(i)),den[0]))
        return q
    for i,j,symbol in [(0,0,a),(0,1,[-1,0,0,0]),(1,1,d)]:
        v=divide(symbol,b)
        assert v[1]-(1 if i==j==1 else 0)==one[i][j] and v[2]==-two[i][j]
    trace=[a[i]+d[i]-(2 if i==0 else 0) for i in range(4)]
    assert divide(trace,b)[3]==sig


def probes():
    # bars-and-stars over seven resistance increments and the unused budget
    for bars in combinations(range(10),7):
        seq=(-1,)+bars+(10,)
        yield [seq[j+1]-seq[j] for j in range(7)]

def add_boundaries(pos,R):
    return [b-a for a,b in zip([0]+pos,pos+[R])]

def main():
    base=[1,3,6,9,14,21];certs={}
    for h in range(1,7):
        m=jacobian(base[:h],27)
        found=None
        for rows in combinations(range(6),h):
            v=det([m[i] for i in rows])
            if v:
                found=(list(rows),str(v));break
        assert found
        certs[h]=dict(positions=base[:h],coordinate_indices=found[0],minor=found[1])
    tests=list(probes())
    assert len(tests)==120 and len(set(map(tuple,tests)))==120
    assert all(all(r>=1 for r in y) and sum(y)<=10 for y in tests)
    testpaths=[[2,3,7],[4,1,7],[1,2,3,3,5,7,6]]
    hashes=[]
    from hashlib import sha256
    for atoms in testpaths:
        check_green(atoms)
        vals=[]
        for ext in tests:
            a=value(atoms+ext)
            assert a==resistance_beta(atoms+ext)
            vals.append(str(a))
        hashes.append(sha256(json.dumps(vals,separators=(",",":")).encode()).hexdigest())
    # Six independent readouts at the normalized port; check with a polynomial
    # of degree <=4 (denominators fixed). Central finite differences cancel
    # the cubic term too. This is a certificate of rank, not a runtime query.
    us=[F(x,27) for x in base];E=F(1,270)
    refs=[(17,[]),(2,[1]),(8,[2,3,5]),(20,[5,7,14,19]),(11,[1]),(11,[5])]
    V=[]
    for S,v in refs:
        ext=add_boundaries(v,S); line=[]
        for i in range(6):
            ys=[]
            for j in (-2,-1,1,2):
                X=us[:];X[i]+=j*E
                ys.append(value(add_boundaries(X,F(1))+ext))
            line.append((ys[0]-8*ys[1]+8*ys[2]-ys[3])/(12*E))
        V.append(line)
    beta_det=det(V)
    assert beta_det==F(-1512681040853963720,3054632475346565685192903614224932699754941)
    print(json.dumps(dict(coordinates=["a","b","g","e","f","j"],chart_rank_certificates=certs,
                          exterior_mesh_count=len(tests),doubly_checked_beta=len(tests)*len(testpaths),
                          unknown_edges=testpaths,exact_beta_fingerprints=hashes,
                          normalized_open_rank=dict(position_numerators=base,denominator=27,
                                              exterior_length_and_interior_positions=refs,
                                              determinant=str(beta_det))),indent=2))

if __name__=="__main__":
    main()
