"""Independent-reference checks for the six-axis derived foundation.

Deliberately does NOT import six_axis.py or vendor.atlas_brc.py.  It rebuilds
K4 incidence, S4 edge actions, tetrahedral rotations, gluing equations and the
quadratic metric classification from definitions to reduce correlated bugs.
"""
from itertools import combinations, permutations, product
import json, time
import sympy as s

V=range(4)
E=tuple(combinations(V,2))
EI={e:i for i,e in enumerate(E)}
STARS=tuple(tuple(i for i,e in enumerate(E) if v in e) for v in V)
G=tuple(permutations(V))
T=((1,-1,-1),(-1,1,-1),(-1,-1,1),(1,1,1))


def parity(g):
    return -1 if sum(g[i]>g[j] for i in V for j in range(i+1,4))%2 else 1

def edge_action(g):
    return tuple(EI[tuple(sorted((g[u],g[v])))] for u,v in E)

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def mt(A): return tuple(zip(*A))
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def rot(g):
    M=[]; p=parity(g)
    for i in range(3):
        row=[]
        for j in range(3):
            z=p*sum(T[g[v]][i]*T[v][j] for v in V)
            assert z%4==0
            row.append(z//4)
        M.append(tuple(row))
    return tuple(M)
def mv(A,x): return tuple(sum(A[i][j]*x[j] for j in range(3)) for i in range(3))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def ray(v,e):
    u,w=E[e]; o=w if u==v else u
    return tuple(-x//2 for x in cross(T[v],T[o]))
def local(n):
    out=[]
    for star in STARS:
        m=min(n[e] for e in star)
        out.append(tuple(n[e]-m for e in star))
    return tuple(out)
def reconstruct_three(charts):
    d={v:{e:x for e,x in zip(STARS[v],charts[v])} for v in charts}
    r=min(d); pot={r:0}
    for v in d:
        if v!=r:
            e=EI[tuple(sorted((r,v)))]
            pot[v]=d[r][e]-d[v][e]
    for u,v in combinations(sorted(d),2):
        e=EI[(u,v)]
        assert d[u][e]-d[v][e]==pot[v]-pot[u]
    raw=[]
    for e,(u,v) in enumerate(E):
        w=u if u in d else v
        raw.append(d[w][e]+pot[w])
    b=min(raw)
    return tuple(x-b for x in raw)


def main():
    t=time.time(); counts={}
    mats={g:rot(g) for g in G}; I=((1,0,0),(0,1,0),(0,0,1))
    for g in G:
        assert mm(mats[g],mt(mats[g]))==I and det3(mats[g])==1
        eg=edge_action(g)
        for v in V:
            for e in STARS[v]:
                assert mv(mats[g],ray(v,e))==ray(g[v],eg[e])
    for g in G:
        for h in G:
            gh=tuple(g[h[v]] for v in V)
            assert mm(mats[g],mats[h])==mats[gh]
    counts['independent_rotation_checks']=24*12+24*24

    k=0
    for n in product(range(4),repeat=6):
        ch=local(n); h=min(n); n0=tuple(x-h for x in n)
        for omit in V:
            use={v:ch[v] for v in V if v!=omit}
            assert reconstruct_three(use)==n0; k+=1
    counts['independent_three_chart_roundtrips']=k

    faces=((0,1,2),(0,1,3),(0,2,3),(1,2,3)); good=[]
    for tau in product((-1,1),repeat=6):
        prods=[]
        for a,b,c in faces:
            prods.append(tau[EI[tuple(sorted((a,b)))]]*tau[EI[tuple(sorted((b,c)))]]*tau[EI[tuple(sorted((a,c)))]] )
        if prods==[-1]*4: good.append(tau)
    assert len(good)==8
    orbit=set(); base=(-1,)*6
    for eps in product((-1,1),repeat=4):
        orbit.add(tuple(eps[u]*base[i]*eps[v] for i,(u,v) in enumerate(E)))
    assert set(good)==orbit and len(orbit)==8
    assert [tau for tau in good if len(set(tau))==1]==[base]
    counts['sign_connections_exhausted']=64

    a,b,c=s.symbols('a b c'); M=s.zeros(6)
    for i in range(6): M[i,i]=a
    for i,j in combinations(range(6),2):
        M[i,j]=M[j,i]=c if set(E[i]).isdisjoint(E[j]) else b
    for g in G:
        eg=edge_action(g); P=s.zeros(6)
        for old,new in enumerate(eg): P[new,old]=1
        assert s.simplify(P.T*M*P-M)==s.zeros(6)
    M=M.subs({a:1,b:0})
    for v in V:
        star=STARS[v]
        for i,j in combinations(star,2): assert M[i,j]==0
        for i in star: assert M[i,i]==1
    assert M.eigenvals()=={1-c:3,1+c:3}
    counts['metric_family_eigenvalues']='1-c (x3), 1+c (x3)'

    out={'status':'PASS_INDEPENDENT_REFERENCE_NO_IMPORT_OF_PRIMARY_IMPLEMENTATION','counts':counts,'seconds':round(time.time()-t,3)}
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__=='__main__': main()
