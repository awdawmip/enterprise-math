"""R037 independent R033/R034 replication runner.

Researcher-ID: EM-R037-A7C2D1
Source base: enterprise-math main 092c8ced3b3a5808d8669946a830db73b129a126
Frozen claims are NOT imported.  This file rebuilds the graphs from definitions.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations, permutations, product
import json
import math

TRI = ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))
SA = ((0,0),(-1,0),(0,-1))
SB = ((0,0),(1,0),(0,1))

def _fcc_steps():
    out=set()
    for zero in range(3):
        ij=[i for i in range(3) if i != zero]
        for a,b in product((-1,1), repeat=2):
            v=[0,0,0]; v[ij[0]]=a; v[ij[1]]=b
            out.add(tuple(v))
    return tuple(sorted(out))
FCC_STEPS=_fcc_steps()

def fcc_neighbors(v):
    x,y,z=v
    return [(x+a,y+b,z+c) for a,b,c in FCC_STEPS]

def hcp_neighbors(v):
    m,n,l=v
    out=[(m+a,n+b,l) for a,b in TRI]
    shifts=SA if l%2==0 else SB
    for dl in (-1,1):
        out += [(m+a,n+b,l+dl) for a,b in shifts]
    return out

def bfs(neighbor,R,root=(0,0,0)):
    dist={root:0}; q=deque([root])
    while q:
        v=q.popleft()
        if dist[v] >= R: continue
        for w in neighbor(v):
            if w not in dist:
                dist[w]=dist[v]+1; q.append(w)
    return dist

def tri_norm(m,n): return max(abs(m),abs(n),abs(m+n))

def fcc_distance(v):
    x,y,z=v
    return max(max(abs(x),abs(y),abs(z)), (abs(x)+abs(y)+abs(z))//2)

def hcp_distance(v):
    m,n,l=v
    L=abs(l); q=L//2
    if L%2==0:
        rem=tri_norm(m,n)
    else:
        rem=min(tri_norm(m-a,n-b) for a,b in SA)
    return L + max(0, rem-q)

def fcc_A(r): return 1 if r==0 else 10*r*r+2
def fcc_V(r): return (10*r**3+15*r*r+11*r+3)//3
def hcp_A(r): return 1 if r==0 else (21*r*r)//2+2
def hcp_V(r): return (14*r**3+21*r*r+14*r+(4 if r%2==0 else 3))//4
def exposed_faces(r): return 12*(3*r*r+3*r+1)

def shell_edge_count(neighbor,dist,r):
    s={v for v,d in dist.items() if d==r}
    return sum(w in s for v in s for w in neighbor(v))//2

def outside_edge_count(neighbor,dist,r):
    ball={v for v,d in dist.items() if d<=r}
    shell=[v for v,d in dist.items() if d==r]
    return sum(w not in ball for v in shell for w in neighbor(v))

def hcp_position(v):
    m,n,l=v; p=l&1
    return (Fraction(m)+Fraction(n,2)+Fraction(p,2),
            Fraction(n,2)+Fraction(p,6), Fraction(l))

def fcc_norm2(v): return Fraction(v[0]*v[0]+v[1]*v[1]+v[2]*v[2],2)
def hcp_norm2(v):
    x,y,z=hcp_position(v)
    return x*x+3*y*y+Fraction(2,3)*z*z

def path_counts(neighbor,n):
    c={(0,0,0):1}
    for _ in range(n):
        nc=defaultdict(int)
        for v,k in c.items():
            for w in neighbor(v): nc[w]+=k
        c=dict(nc)
    return c

def radial_moment(counts,norm2,p,n):
    return sum(Fraction(c)*norm2(v)**p for v,c in counts.items())/Fraction(12**n)

def shell_four_cycles(neighbor):
    d=bfs(neighbor,1); S=[v for v,x in d.items() if x==1]; SS=set(S)
    adj={v:set(w for w in neighbor(v) if w in SS) for v in S}
    cyc=set()
    for a,c in combinations(S,2):
        common=adj[a]&adj[c]
        for b,d0 in combinations(common,2):
            cyc.add(tuple(sorted((a,b,c,d0))))
    return len(cyc)

# Exact rational Voronoi boundary complex, independent of frozen topology code.
def _det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def _solve3(A,b):
    D=_det3(A)
    if D==0: return None
    cols=[]
    for j in range(3):
        B=[list(row) for row in A]
        for i in range(3): B[i][j]=b[i]
        cols.append(_det3(B)/D)
    return tuple(cols)
def _voronoi_faces(steps,G):
    normals=[tuple(G[i]*d[i] for i in range(3)) for d in steps]
    verts={}
    for ids in combinations(range(12),3):
        sol=_solve3([normals[i] for i in ids],[Fraction(1,2)]*3)
        if sol is None: continue
        if all(sum(n[j]*sol[j] for j in range(3))<=Fraction(1,2) for n in normals):
            active=tuple(i for i,n in enumerate(normals)
                         if sum(n[j]*sol[j] for j in range(3))==Fraction(1,2))
            verts[sol]=active
    faces={}
    for fi in range(12):
        fvs=[v for v,a in verts.items() if fi in a]
        edges=[]
        for a,b in combinations(fvs,2):
            if len(set(verts[a])&set(verts[b]))>=2:
                edges.append((a,b))
        faces[fi]=(fvs,edges)
    return faces

FCC_STEP_FRAC=[tuple(Fraction(q) for q in v) for v in FCC_STEPS]
FCC_FACES=_voronoi_faces(FCC_STEP_FRAC,(Fraction(1,2),)*3)
def _hcp_local_steps(v):
    p=hcp_position(v)
    return [tuple(a-b for a,b in zip(hcp_position(w),p)) for w in hcp_neighbors(v)]
HCPA_STEPS=_hcp_local_steps((0,0,0))
HCPB_STEPS=_hcp_local_steps((0,0,1))
HCPA_FACES=_voronoi_faces(HCPA_STEPS,(Fraction(1),Fraction(3),Fraction(2,3)))
HCPB_FACES=_voronoi_faces(HCPB_STEPS,(Fraction(1),Fraction(3),Fraction(2,3)))
_SCALE=12
def _scale(v): return tuple(int(x*_SCALE) for x in v)
def _face_int(face_map):
    return {i:([_scale(v) for v in vs],
               [(_scale(a),_scale(b)) for a,b in es])
            for i,(vs,es) in face_map.items()}
_FFI=_face_int(FCC_FACES); _HAI=_face_int(HCPA_FACES); _HBI=_face_int(HCPB_FACES)
def _center_int(v,kind):
    if kind=="fcc": return tuple(_SCALE*x for x in v)
    return _scale(hcp_position(v))
def _add(a,b): return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

def boundary_complex(kind,r):
    neighbor=fcc_neighbors if kind=="fcc" else hcp_neighbors
    dist=bfs(neighbor,r+1); ball={v for v,d in dist.items() if d<=r}
    shell=[v for v,d in dist.items() if d==r]
    vf=defaultdict(list); ef=defaultdict(list); F=0
    for v in shell:
        center=_center_int(v,kind)
        if kind=="fcc":
            fmap=_FFI; neigh=fcc_neighbors(v)
        else:
            fmap=_HAI if v[2]%2==0 else _HBI; neigh=hcp_neighbors(v)
        for fi,w in enumerate(neigh):
            if w in ball: continue
            idx=F; F+=1
            vs,es=fmap[fi]
            for q in vs: vf[_add(center,q)].append(idx)
            for a,b in es: ef[frozenset((_add(center,a),_add(center,b)))].append(idx)
    V=len(vf); E=len(ef)
    edge_inc=Counter(len(fs) for fs in ef.values())
    vedges=defaultdict(list); adj=defaultdict(set)
    for e,fs in ef.items():
        a,b=tuple(e); adj[a].add(b); adj[b].add(a)
        vedges[a].append(fs); vedges[b].append(fs)
    connected=True
    if vf:
        start=next(iter(vf)); seen={start}; st=[start]
        while st:
            a=st.pop()
            for b in adj[a]:
                if b not in seen: seen.add(b); st.append(b)
        connected=len(seen)==V
    links=True
    for v,inc in vf.items():
        la=defaultdict(set)
        for fs in vedges[v]:
            if len(fs)==2:
                a,b=fs; la[a].add(b); la[b].add(a)
        if any(len(la[i])!=2 for i in inc): links=False; break
        seen={inc[0]}; st=[inc[0]]
        while st:
            a=st.pop()
            for b in la[a]:
                if b not in seen: seen.add(b); st.append(b)
        if len(seen)!=len(inc): links=False; break
    return {"V":V,"E":E,"F":F,"chi":V-E+F,
            "connected":connected,"edge_incidence":dict(edge_inc),"vertex_links_cycles":links}

def run_reference(full_topology=False):
    fd=bfs(fcc_neighbors,20); hd=bfs(hcp_neighbors,20)
    assert all(fcc_distance(v)==d for v,d in fd.items())
    assert all(hcp_distance(v)==d for v,d in hd.items())
    shells_f=Counter(fd.values()); shells_h=Counter(hd.values())
    for r in range(21):
        assert shells_f[r]==fcc_A(r); assert shells_h[r]==hcp_A(r)
    assert shell_four_cycles(fcc_neighbors)==6
    assert shell_four_cycles(hcp_neighbors)==9
    for r in range(1,21):
        assert shell_edge_count(fcc_neighbors,fd,r)==24*r*r
        assert shell_edge_count(hcp_neighbors,hd,r)==27*r*r-(3 if r%2 else 0)
        assert outside_edge_count(fcc_neighbors,fd,r)==exposed_faces(r)
        assert outside_edge_count(hcp_neighbors,hd,r)==exposed_faces(r)
    topology_radii=range(21) if full_topology else (0,1,2,10,20)
    topo={}
    for kind in ("fcc","hcp"):
        topo[kind]={}
        for r in topology_radii:
            bc=boundary_complex(kind,r); F=exposed_faces(r)
            assert (bc["V"],bc["E"],bc["F"],bc["chi"])==(F+2,2*F,F,2)
            assert bc["connected"] and bc["edge_incidence"]=={2:2*F} and bc["vertex_links_cycles"]
            topo[kind][r]=bc
    paths={}
    for n in range(13):
        cf=path_counts(fcc_neighbors,n); ch=path_counts(hcp_neighbors,n)
        paths[n]={"fcc_support":len(cf),"hcp_support":len(ch),
                  "fcc_return":cf.get((0,0,0),0),"hcp_return":ch.get((0,0,0),0)}
        assert radial_moment(cf,fcc_norm2,1,n)==n
        assert radial_moment(ch,hcp_norm2,1,n)==n
        assert radial_moment(cf,fcc_norm2,2,n)==Fraction(5*n*n-2*n,3)
        assert radial_moment(ch,hcp_norm2,2,n)==Fraction(5*n*n-2*n,3)
        f6=Fraction(n*(35*n*n-42*n+16),9)
        assert radial_moment(cf,fcc_norm2,3,n)==f6
        if n>=1:
            h6=Fraction(210*n**3-252*n*n+95*n+1,54)
            assert radial_moment(ch,hcp_norm2,3,n)==h6
    assert (len(path_counts(fcc_neighbors,2)),len(path_counts(hcp_neighbors,2)))==(55,57)
    return {
      "schema":"R037_INDEPENDENT_REFERENCE_V1",
      "researcher_id":"EM-R037-A7C2D1",
      "growth":{"fcc_r100":{"A":fcc_A(100),"V":fcc_V(100)},
                "hcp_r100":{"A":hcp_A(100),"V":hcp_V(100)}},
      "first_differences":{"rooted_r1_shell_four_cycles":{"fcc":6,"hcp":9},
                           "shell_cardinality_r2":{"fcc":42,"hcp":44}},
      "topology":topo,
      "paths":paths,
      "spectral_certificate":{
        "fcc_log2":"-(x^2+y^2+z^2)/6",
        "fcc_log4":"-(x^4+x^2*y^2+x^2*z^2+y^4+y^2*z^2+z^4)/144",
        "hcp_log2":"-(x^2+y^2+z^2)/6",
        "hcp_log4":"-(9*x^4+18*x^2*y^2+24*x^2*z^2+9*y^4+24*y^2*z^2+8*z^4)/1728",
        "stacking_aligned_fcc_minus_hcp_log4":"-sqrt(2)*y*z*(3*x^2-y^2)/432"
      }
    }

if __name__=="__main__":
    print(json.dumps(run_reference(full_topology=False),sort_keys=True,indent=2,default=str))
