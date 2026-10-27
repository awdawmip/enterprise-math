#!/usr/bin/env python3
"""R033 exact FCC/HCP intrinsic graph-ball laboratory.

No floating point is used for graph membership, growth, boundary spectra, or
Voronoi-boundary topology. The only physical embedding data are exact rational
Gram matrices, used after the graph balls are frozen.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations, product
from typing import Dict, List, Sequence, Set, Tuple

P3 = Tuple[int, int, int]
Q3 = Tuple[F, F, F]

FCC_DIRS = (
    (0,-1,-1),(0,-1,1),(0,1,-1),(0,1,1),
    (-1,0,-1),(-1,0,1),(1,0,-1),(1,0,1),
    (-1,-1,0),(-1,1,0),(1,-1,0),(1,1,0),
)
TRI_DIRS = ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))


def fcc_neighbors(p: P3) -> Tuple[P3, ...]:
    x,y,z=p
    return tuple((x+a,y+b,z+c) for a,b,c in FCC_DIRS)


def hcp_neighbors(p: P3) -> Tuple[P3, ...]:
    i,j,k=p
    same=[(i+a,j+b,k) for a,b in TRI_DIRS]
    shifts=((0,0),(1,0),(0,1)) if (k & 1) else ((0,0),(-1,0),(0,-1))
    lower=[(i+a,j+b,k-1) for a,b in shifts]
    upper=[(i+a,j+b,k+1) for a,b in shifts]
    return tuple(same+lower+upper)


def fcc_distance(p: P3) -> int:
    x,y,z=p
    if (x+y+z) & 1:
        raise ValueError("not an FCC D3 vertex")
    a,b,c=abs(x),abs(y),abs(z)
    return max(a,b,c,(a+b+c)//2)


def tri_radius(i:int,j:int)->int:
    return max(abs(i),abs(j),abs(i+j))


def hcp_shift_radius(i:int,j:int)->int:
    return max(i,j,i+j,-i-1,-j-1,-i-j-1)


def hcp_distance(p:P3)->int:
    i,j,k=p
    a=abs(k)
    if not (k & 1):
        return max(a, a//2 + tri_radius(i,j))
    return max(a, (a+1)//2 + hcp_shift_radius(i,j))


def bfs_layers(neighbors, max_r:int, origin:P3=(0,0,0)) -> List[Set[P3]]:
    seen={origin}; layers=[{origin}]; frontier={origin}
    for _ in range(max_r):
        nxt=set()
        for p in frontier:
            for q in neighbors(p):
                if q not in seen:
                    seen.add(q); nxt.add(q)
        layers.append(nxt); frontier=nxt
    return layers


def fcc_A(r:int)->int:
    return 1 if r==0 else 10*r*r+2


def fcc_V(r:int)->int:
    return (10*r**3+15*r*r+11*r+3)//3


def hcp_A(r:int)->int:
    if r==0: return 1
    return (21*r*r + (4 if r%2==0 else 3))//2


def hcp_V(r:int)->int:
    return (14*r**3+21*r*r+14*r+(4 if r%2==0 else 3))//4


def exposed_faces(r:int)->int:
    return 12*(3*r*r+3*r+1)


def fcc_shell_edges(r:int)->int:
    return 0 if r==0 else 24*r*r


def hcp_shell_edges(r:int)->int:
    if r==0: return 0
    return 27*r*r if r%2==0 else 27*r*r-3


def fcc_boundary_orbits(r:int)->Dict[str,int]:
    if r==0: return {"single_cell_out12":1}
    return {
        "F7_vertex_out7":12,
        "F5_edge_out5":24*(r-1),
        "F4_square_face_out4":6*(r-1)**2,
        "F3_triangular_face_out3":4*(r-1)*(r-2),
    }


def hcp_boundary_orbits(r:int)->Dict[str,int]:
    if r==0: return {"single_cell_out12":1}
    if r<4: raise ValueError("stable HCP orbit formulas require r>=4")
    if r%2==0:
        return {
            "H69_out3":3*(3*r*r-6*r+4)//2,
            "H228_out4":3*(r-2)*(3*r-2)//2,
            "H229_out5":12*(r-1),
            "H448_out3":(3*r*r-6*r+4)//2,
            "H453_out5":3*(r-2),
            "H458_out5":3*(r-2),
            "H469_out6":12,
            "H581_out4":3*(r-1),
            "H1764_out6":3*(r-1),
            "H1765_out7":6,
        }
    return {
        "H69_out3":9*(r-1)**2//2,
        "H228_out4":3*(r-1)*(3*r-5)//2,
        "H229_out5":12*(r-1),
        "H448_out3":3*(r-1)**2//2,
        "H453_out5":3*(r-1),
        "H458_out5":3*(r-3),
        "H469_out6":12,
        "H581_out4":3*(r-1),
        "H1764_out6":3*(r-1),
        "H1765_out7":6,
    }


def fcc_shell_points(r:int)->Set[P3]:
    if r==0:return {(0,0,0)}
    pts=set()
    for x in range(-r,r+1):
        for y in range(-r,r+1):
            for z in range(-r,r+1):
                if ((x+y+z)&1)==0 and fcc_distance((x,y,z))==r:
                    pts.add((x,y,z))
    return pts


def hcp_shell_points(r:int)->Set[P3]:
    if r==0:return {(0,0,0)}
    pts=set()
    for k in range(-r,r+1):
        for i in range(-r-1,r+2):
            for j in range(-r-1,r+2):
                if hcp_distance((i,j,k))==r:
                    pts.add((i,j,k))
    return pts

# Exact diagnostic embeddings for Voronoi topology.
FCC_G=((F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)))
HCP_G=((F(1),F(1,2),F(0)),(F(1,2),F(1),F(0)),(F(0),F(0),F(2,3)))


def fcc_center(p:P3)->Q3:
    return tuple(F(x) for x in p)  # type: ignore


def hcp_center(p:P3)->Q3:
    i,j,k=p
    s=F(1,3) if (k&1) else F(0)
    return F(i)+s,F(j)+s,F(k)


def mat_vec(G, d:Q3)->Q3:
    return tuple(sum(G[i][j]*d[j] for j in range(3)) for i in range(3))  # type: ignore


def qdot(G,a:Q3,b:Q3)->F:
    return sum(a[i]*sum(G[i][j]*b[j] for j in range(3)) for i in range(3))


def sub(a:Q3,b:Q3)->Q3:
    return tuple(a[i]-b[i] for i in range(3))  # type: ignore


def add(a:Q3,b:Q3)->Q3:
    return tuple(a[i]+b[i] for i in range(3))  # type: ignore


def det3(M)->F:
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))


def solve3(M,b)->Q3 | None:
    d=det3(M)
    if d==0:return None
    cols=[]
    for c in range(3):
        N=[list(row) for row in M]
        for i in range(3):N[i][c]=b[i]
        cols.append(det3(N)/d)
    return tuple(cols)  # type: ignore


@dataclass(frozen=True)
class LocalCell:
    vertices: Tuple[Q3,...]
    active: Tuple[frozenset[int],...]
    face_vertices: Tuple[Tuple[int,...],...]
    face_edges: Tuple[Tuple[Tuple[int,int],...],...]


def local_voronoi_cell(world:str, parity:int=0)->LocalCell:
    if world=="fcc":
        origin=(0,0,0); neigh=fcc_neighbors; center=fcc_center; G=FCC_G
    else:
        origin=(0,0,parity); neigh=hcp_neighbors; center=hcp_center; G=HCP_G
    c0=center(origin)
    ds=[sub(center(q),c0) for q in neigh(origin)]
    normals=[mat_vec(G,d) for d in ds]
    rhs=[qdot(G,d,d)/2 for d in ds]
    verts={}
    for inds in combinations(range(12),3):
        M=[normals[i] for i in inds]; b=[rhs[i] for i in inds]
        x=solve3(M,b)
        if x is None:continue
        if all(sum(normals[j][t]*x[t] for t in range(3)) <= rhs[j] for j in range(12)):
            act=frozenset(j for j in range(12) if sum(normals[j][t]*x[t] for t in range(3))==rhs[j])
            verts[x]=act
    vs=tuple(sorted(verts)); active=tuple(verts[x] for x in vs)
    face_vertices=[]; face_edges=[]
    for f in range(12):
        ids=tuple(i for i,a in enumerate(active) if f in a)
        edges=[]
        for i,j in combinations(ids,2):
            if len(active[i].intersection(active[j]))>=2:
                edges.append((i,j))
        face_vertices.append(ids); face_edges.append(tuple(edges))
    return LocalCell(vs,active,tuple(face_vertices),tuple(face_edges))


_LOCAL={
    ("fcc",0):local_voronoi_cell("fcc",0),
    ("hcp",0):local_voronoi_cell("hcp",0),
    ("hcp",1):local_voronoi_cell("hcp",1),
}


def boundary_complex(world:str, ball:Set[P3]):
    if world=="fcc": neigh=fcc_neighbors; center=fcc_center
    else: neigh=hcp_neighbors; center=hcp_center
    face_records=[]; all_edges=Counter(); all_vertices=set()
    for p in ball:
        ns=neigh(p); c=center(p)
        cell=_LOCAL[(world,0 if world=="fcc" else (p[2]&1))]
        for f,q in enumerate(ns):
            if q in ball: continue
            verts=[add(c,cell.vertices[i]) for i in cell.face_vertices[f]]
            ids={local_i:v for local_i,v in zip(cell.face_vertices[f],verts)}
            fedges=[]
            for a,b in cell.face_edges[f]:
                e=tuple(sorted((ids[a],ids[b])))
                all_edges[e]+=1; fedges.append(e)
            all_vertices.update(verts)
            face_records.append((frozenset(verts),tuple(fedges)))
    adj=defaultdict(set)
    for a,b in all_edges:
        adj[a].add(b);adj[b].add(a)
    comps=0; unseen=set(all_vertices)
    while unseen:
        comps+=1; root=unseen.pop(); stack=[root]
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if w in unseen: unseen.remove(w); stack.append(w)
    bad_edge_inc=sum(n!=2 for n in all_edges.values())
    bad_links=0; incidence_by_vertex=defaultdict(list)
    for fi,(fverts,fedges) in enumerate(face_records):
        for v in fverts: incidence_by_vertex[v].append((fi,fedges))
    for v,recs in incidence_by_vertex.items():
        link=defaultdict(set)
        for _,fedges in recs:
            vedges=[e for e in fedges if v in e]
            if len(vedges)!=2:
                bad_links+=1; break
            e1,e2=vedges; link[e1].add(e2);link[e2].add(e1)
        else:
            if not link or any(len(x)!=2 for x in link.values()):
                bad_links+=1; continue
            root=next(iter(link)); seen={root}; stack=[root]
            while stack:
                e=stack.pop()
                for q in link[e]:
                    if q not in seen: seen.add(q);stack.append(q)
            if len(seen)!=len(link):bad_links+=1
    V=len(all_vertices);E=len(all_edges);Fcount=len(face_records)
    return {"V":V,"E":E,"F":Fcount,"chi":V-E+Fcount,
            "components":comps,"bad_edge_incidence":bad_edge_inc,"bad_vertex_links":bad_links}

# Directional-mask / symmetry-orbit enumeration.
def _mask_permute(mask:int, perm:Sequence[int])->int:
    out=0
    for i,j in enumerate(perm):
        if mask>>i & 1: out |= 1<<j
    return out


def _fcc_sym_perms():
    idx={d:i for i,d in enumerate(FCC_DIRS)}; out=set()
    for ax in permutations(range(3)):
        for s in product((-1,1), repeat=3):
            p=[]
            for d in FCC_DIRS:
                t=tuple(s[k]*d[ax[k]] for k in range(3)); p.append(idx[t])
            out.add(tuple(p))
    assert len(out)==48
    return tuple(sorted(out))

FCC_SYM_PERMS=_fcc_sym_perms()


def fcc_orbit_mask(mask:int)->int:
    return min(_mask_permute(mask,p) for p in FCC_SYM_PERMS)


def _hcp_A_displacements():
    p=(0,0,0); c=hcp_center(p)
    return tuple(sub(hcp_center(q),c) for q in hcp_neighbors(p))

HCP_A_DISP=_hcp_A_displacements()


def _r120(v:Q3)->Q3:
    u,w,z=v; return -u-w,u,z

def _reflect(v:Q3)->Q3:
    u,w,z=v; return w,u,z

def _zflip(v:Q3)->Q3:
    u,w,z=v; return u,w,-z


def _hcp_A_sym_perms():
    idx={v:i for i,v in enumerate(HCP_A_DISP)}; perms=set()
    for rot in range(3):
        for refl in (False,True):
            for zf in (False,True):
                def tr(v,rot=rot,refl=refl,zf=zf):
                    x=v
                    for _ in range(rot): x=_r120(x)
                    if refl:x=_reflect(x)
                    if zf:x=_zflip(x)
                    return x
                perms.add(tuple(idx[tr(v)] for v in HCP_A_DISP))
    assert len(perms)==12
    return tuple(sorted(perms))

HCP_A_SYM_PERMS=_hcp_A_sym_perms()


def _hcp_B_to_A_perm():
    p=(0,0,1); pp=(0,0,2); idx={q:i for i,q in enumerate(hcp_neighbors(pp))}; out=[]
    for q in hcp_neighbors(p):
        qp=(-q[0],-q[1],q[2]+1); out.append(idx[qp])
    return tuple(out)

HCP_B_TO_A=_hcp_B_to_A_perm()


def hcp_orbit_mask(mask:int, parity:int)->int:
    if parity&1: mask=_mask_permute(mask,HCP_B_TO_A)
    return min(_mask_permute(mask,p) for p in HCP_A_SYM_PERMS)


def boundary_orbit_counts(world:str, shell:Set[P3], ball:Set[P3])->Counter:
    out=Counter()
    if world=="fcc":
        for p in shell:
            mask=sum(1<<i for i,q in enumerate(fcc_neighbors(p)) if q not in ball)
            out[fcc_orbit_mask(mask)] += 1
    else:
        for p in shell:
            mask=sum(1<<i for i,q in enumerate(hcp_neighbors(p)) if q not in ball)
            out[hcp_orbit_mask(mask,p[2]&1)] += 1
    return out


def macro_record(r:int)->dict:
    Af,Vf=fcc_A(r),fcc_V(r); Ah,Vh=hcp_A(r),hcp_V(r)
    kf=F(Af**3,Vf**2); kh=F(Ah**3,Vh**2)
    return {
        "r":str(r),
        "fcc":{"A":str(Af),"V":str(Vf),"K":{"num":str(kf.numerator),"den":str(kf.denominator)}},
        "hcp":{"A":str(Ah),"V":str(Vh),"K":{"num":str(kh.numerator),"den":str(kh.denominator)}},
    }


if __name__=="__main__":
    for world,neighbors,A,V,dist in [
        ("fcc",fcc_neighbors,fcc_A,fcc_V,fcc_distance),
        ("hcp",hcp_neighbors,hcp_A,hcp_V,hcp_distance),
    ]:
        layers=bfs_layers(neighbors,20); seen=set()
        for r,shell in enumerate(layers):
            seen|=shell
            assert len(shell)==A(r) and len(seen)==V(r)
            assert all(dist(p)==r for p in shell)
        print(world,"BFS r=0..20 exact: PASS")
