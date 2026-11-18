"""Exact integral bipyramid blocks, finite-field widths, and public Regina 7.4.1 controls."""
import argparse
from collections import defaultdict, deque
from functools import lru_cache
from itertools import combinations, product
from importlib.metadata import version
import json
from pathlib import Path

U, D, A, B, C, W = range(6)
RIM = (A, B, C)
PAIRS = ((A,B), (B,C), (C,A))
OLD = [(U,A,B,C),(D,A,B,C)]
NEW = [(U,D,i,j) for i,j in PAIRS]
EXTERIOR = [(v,W,i,j) for v in (U,D) for i,j in PAIRS]


def edge(x,y):
    return tuple(sorted((x,y)))


def oriented(tets):
    tets = [tuple(sorted(t)) for t in tets]
    faces = defaultdict(list)
    for k,t in enumerate(tets):
        for pos in range(4):
            faces[t[:pos]+t[pos+1:]].append((k,pos))
    signs = {0:1}
    queue = deque([0])
    while queue:
        k = queue.popleft()
        for j in range(4):
            face=tets[k][:j]+tets[k][j+1:]
            for l,h in faces[face]:
                if l!=k:
                    sign=-signs[k]*(-1)**(j+h)
                    if l in signs:
                        assert signs[l]==sign
                    else:
                        signs[l]=sign
                        queue.append(l)
    return [t if signs[i]==1 else (t[1],t[0],t[2],t[3]) for i,t in enumerate(tets)]


def blocks(tets):
    edges=sorted(set(e for t in tets for e in combinations(sorted(t),2)))
    rows=[[0]*(3*len(tets)) for _ in edges]
    for k,(a,b,c,d) in enumerate(tets):
        opposite=[(edge(a,b),edge(c,d)),(edge(a,c),edge(b,d)),(edge(a,d),edge(b,c))]
        for j in range(3):
            for sign,h in ((1,(j+1)%3),(-1,(j+2)%3)):
                for e in opposite[h]:
                    rows[edges.index(e)][3*k+j]=sign
    return edges,rows


def rank(matrix, p):
    basis={}
    for row in matrix:
        r=[x%p for x in row]
        for j in sorted(basis):
            if r[j]:
                f=r[j]
                r=[(x-f*y)%p for x,y in zip(r,basis[j])]
        nz=next((i for i,z in enumerate(r) if z),None)
        if nz is not None:
            f=pow(r[nz],-1,p)
            basis[nz]=[(x*f)%p for x in r]
    return len(basis)


def widths(tets, p):
    edges,rows=blocks(tets)
    n=len(tets); all_blocks=(1<<n)-1
    incidences=[sum(1<<k for k,t in enumerate(tets) if set(e)<=set(t)) for e in edges]
    ranks=[]
    for subset in range(1<<n):
        columns=[3*k+j for k in range(n) if subset>>k&1 for j in range(3)]
        ranks.append(rank([[r[j] for j in columns] for r in rows],p))
    linear=[ranks[s]+ranks[all_blocks^s]-ranks[-1] for s in range(1<<n)]
    raw=[sum(bool(s&e) and bool((all_blocks^s)&e) for e in incidences) for s in range(1<<n)]
    def optimal(cut):
        @lru_cache(None)
        def walk(s):
            if s & (s-1)==0:
                return cut[s]
            low=s & -s
            t=(s-1)&s
            best=10**9
            while t:
                if t & low:
                    best=min(best,max(walk(t),walk(s^t),cut[s]))
                t=(t-1)&s
            return best
        return walk(all_blocks)
    neighbors=[sum(1<<j for j,v in enumerate(tets) if j!=i and len(set(u)&set(v))==3)
               for i,u in enumerate(tets)]
    @lru_cache(None)
    def tw(removed):
        if removed==all_blocks:
            return 0
        best=n
        for k in range(n):
            if removed>>k&1:
                continue
            # Neighbors in the torso after eliminating the set removed.
            seen=0; front=neighbors[k]&removed; adj=neighbors[k]
            while front:
                seen|=front
                more=0
                for j in range(n):
                    if front>>j&1:
                        more|=neighbors[j]
                adj|=more;front=more&removed&~seen
            degree=(adj & ~removed & ~(1<<k)).bit_count()
            best=min(best,max(degree,tw(removed|(1<<k))))
        return best
    return {'row_rank':ranks[-1],'code_width':optimal(linear),'edge_width':optimal(raw),'dual_treewidth':tw(0)}


def matrix_entries(m):
    return [[m.entry(i,j).pythonValue() for j in range(m.columns())] for i in range(m.rows())]


def build_regina(tets, R):
    t=R.Triangulation3()
    for _ in tets:
        t.newTetrahedron()
    pending={}
    for k, labels in enumerate(tets):
        for i in range(4):
            face=tuple(sorted(x for j,x in enumerate(labels) if j!=i))
            if face not in pending:
                pending[face]=(k,i)
                continue
            l,j=pending.pop(face)
            perm=[j if h==i else tets[l].index(x) for h,x in enumerate(labels)]
            t.tetrahedron(k).join(i,t.tetrahedron(l),R.Perm4(*perm))
    assert not pending and t.isValid() and t.isClosed() and t.isOrientable() and t.countVertices()==6
    assert t.isSphere()
    edges,rows=blocks(tets)
    actual=matrix_entries(R.makeMatchingEquations(t,R.NS_QUAD))
    for ge in t.edges():
        em=ge.front()
        tet=tets[em.simplex().index()]
        key=edge(tet[em.vertices()[0]],tet[em.vertices()[1]])
        theoretical=rows[edges.index(key)]
        assert actual[ge.index()] in (theoretical,[-x for x in theoretical])
    return t


def surface_vector(tets, old, k, j):
    vector=[]
    for tet in tets:
        values=[0]*7
        if W in tet:
            cut={W, U if U in tet else D}
            amount=k
        elif old:
            values[tet.index(U if U in tet else D)]=k
            cut=None
            amount=0
        else:
            values[tet.index(U)]=values[tet.index(D)]=k-j
            cut={U,D}
            amount=j
        if cut:
            partition=cut if tet[0] in cut else set(tet)-cut
            typ=next(i for i in range(1,4) if tet[i] in partition)
            values[3+typ]=amount
        vector+=values
    return vector


def normal_from_edges(tet, weights):
    # Unique admissible tetrahedral filling, or None.
    a,b,c,d=tet
    w=lambda i,j: weights[edge(i,j)]
    def defect(i,j,k): return w(i,j)+w(i,k)-w(j,k)
    for i,j,k in combinations(tet,3):
        arcs=[defect(i,j,k),defect(j,i,k),defect(k,i,j)]
        if any(z<0 or z%2 for z in arcs): return None
    sums=[w(a,b)+w(c,d),w(a,c)+w(b,d),w(a,d)+w(b,c)]
    lo,mid,hi=sorted(sums)
    if mid!=hi or (hi-lo)%2: return None
    tri=[min(defect(i,j,k) for j,k in combinations([v for v in tet if v!=i],2))//2 for i in tet]
    quad=[0]*3
    quad[sums.index(lo)]=(hi-lo)//2
    return tri+quad


def geometric_check():
    distinct=0
    for qtype in range(3):
        for coords in product(range(3),repeat=5):
            tri=list(coords[:4]);q=coords[-1]
            w={edge(i,j):tri[i]+tri[j]+q*((i in (0,1+qtype))!=(j in (0,1+qtype)))
               for i,j in combinations(range(4),2)}
            vals=tri+[q if z==qtype else 0 for z in range(3)]
            assert normal_from_edges((0,1,2,3),w)==vals
            distinct+=1
    p={edge(v,i):2 for i in RIM for v in (U,D)}
    p.update({edge(A,B):2,edge(B,C):2,edge(A,C):4,edge(U,D):0})
    assert all(normal_from_edges(t,p) is None for t in OLD)
    assert all(normal_from_edges(t,p) is not None for t in NEW)
    for k in range(1,9):
        w={edge(v,i):k for i in RIM for v in (U,D)}
        w.update({edge(i,j):0 for i,j in PAIRS})
        assert all(normal_from_edges(t,w) is not None for t in OLD)
        observed=[]
        for x in range(2*k+1):
            w[edge(U,D)]=x
            fillings=[normal_from_edges(t,w) for t in NEW]
            if all(y is not None for y in fillings):
                observed.append(x)
                assert all(y==[x//2,x//2,0,0,k-x//2,0,0] for y in fillings)
        assert observed==list(range(0,2*k+1,2))
    return {'tetra_small_reconstructions':distinct,'geometric_fibres_checked_through_k':8,
            'nonextendible_new_tetra_standard':[normal_from_edges(t,p) for t in NEW]}


def puncture_control():
    traces={}
    for name,core in [('two',OLD),('three',NEW)]:
        tets=oriented(core+EXTERIOR)
        edges,rows=blocks(tets)
        column=[]
        for k,tet in enumerate(tets):
            if W in tet:
                side={U,A} if U in tet and A in tet else set(tet[:2])
            elif name=='two':
                side={A,(U if U in tet else D)}
            else:
                side={U,D}
            if tet[0] not in side: side=set(tet)-side
            column.append(3*k+next(j for j in range(3) if tet[j+1] in side))
        at=rows[edges.index(edge(U,A))]
        traces[name]=[at[j] for j in column]
        if name=='three':
            center=rows[edges.index(edge(U,D))]
            assert all(center[j]==0 for j in column)
    assert not any(traces['two']) and any(traces['three'][:3]) and not any(traces['three'][3:])
    return traces


def integral_section():
    # A homogeneous integral identity is verified here on the ten standard basis vectors.
    oe,orr=blocks(oriented(OLD))
    ne,nrr=blocks(oriented(NEW))
    def apply(keys,rows,weights):
        return [sum(weights[e]*r[j] for e,r in zip(keys,rows)) for j in range(len(rows[0]))]
    for idx in range(len(ne)):
        m={e:int(i==idx) for i,e in enumerate(ne)}
        w=lambda x,y:m[edge(x,y)]
        reduced={e:0 for e in ne}
        for v in (U,D):
            reduced[edge(v,B)]=w(v,B)+w(A,C)-w(v,A)-w(B,C)
            reduced[edge(v,C)]=w(v,C)+w(A,B)-w(v,A)-w(B,C)
        section=w(U,A)+w(D,A)+w(B,C)-w(A,B)-w(A,C)
        reduced[edge(U,D)]=w(U,D)-section
        assert apply(oe,orr,m)==apply(oe,orr,reduced)
        assert apply(ne,nrr,m)==apply(ne,nrr,reduced)
    return len(ne)


def main():
    import regina as R
    parser=argparse.ArgumentParser(__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result={'regina_version':R.versionString(),'regina_package':version('regina'),'closed':{},'local':{},
            'geometric':geometric_check(),'punctured_old_to_new':puncture_control(),
            'integral_section_basis_columns':integral_section()}
    controls={}
    for name,core in [('two',OLD),('three',NEW)]:
        result['local'][name]={p:widths(oriented(core),p) for p in (2,3,5)}
        tets=oriented(core+EXTERIOR)
        t=build_regina(tets,R)
        controls[name]=(t,tets)
        standard=matrix_entries(R.makeMatchingEquations(t,R.NS_STANDARD))
        zero_gauges={x:next((i,tet.index(x)) for i,tet in enumerate(tets) if W in tet and x in tet)
                     for x in range(6)}
        readings=[]
        for k in range(1,6):
            values=[]
            for j in (range(k+1) if name=='three' else (0,)):
                v=surface_vector(tets,name=='two',k,j)
                assert all(sum(x*y for x,y in zip(row,v))==0 for row in standard)
                assert all(v[7*i+h]==0 for i,h in zero_gauges.values())
                surface=R.NormalSurface(t,R.NS_STANDARD,v)
                assert surface.embedded() and surface.isOrientable()
                chi=surface.eulerChar().pythonValue()
                assert chi==2*(k-j)
                if k==1:
                    assert surface.isConnected()
                values.append(chi)
            readings.append(values)
        relative=None
        if name=='three':
            caps=surface_vector(tets,False,1,0)
            annulus=surface_vector(tets,False,1,1)
            diff=[b-a for a,b in zip(caps,annulus)]
            assert all(z==0 for z in diff[21:])
            assert all(sum(x*y for x,y in zip(row,diff))==0 for row in standard)
            quads=[diff[7*i+4+j] for i in range(len(tets)) for j in range(3)]
            bmat=matrix_entries(R.makeMatchingEquations(t,R.NS_QUAD))
            assert all(sum(x*y for x,y in zip(row,quads))==0 for row in bmat)
            relative={'interior_q_by_block':[quads[i:i+3] for i in (0,3,6)],
                      'euler_difference':readings[0][1]-readings[0][0]}
        result['closed'][name]={'isoSig':t.isoSig(),'relative_kernel_witness':relative,'vertices':t.countVertices(),'tetrahedra':t.size(),
                'repairs_outside':zero_gauges,'actual_euler_by_k':readings,
                'widths':{p:widths(tets,p) for p in (2,3,5)}}
    old,tets=controls['two']
    face=old.tetrahedron(0).triangle(tets[0].index(U))
    assert old.pachner(face)
    assert old.isoSig()==controls['three'][0].isoSig()
    result['regina_legal_2_to_3']=True
    content=json.dumps(result,indent=2,sort_keys=True)+'\n'
    print(content,end='')
    if args.output: args.output.write_text(content)


if __name__=='__main__':
    main()
