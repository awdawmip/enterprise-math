"""Repair-state, octagon charge and integral membership certificates. Requires Regina 7.4.1."""
from collections import deque
from math import gcd, lcm, isqrt
from importlib.metadata import version
from pathlib import Path
import argparse
import json
import regina as R


def mat(M):
    return [[M.entry(i,j).pythonValue() for j in range(M.columns())] for i in range(M.rows())]


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def add(x,y,m=1):
    return [a+m*b for a,b in zip(x,y)]


def transpose(A):
    return list(zip(*A))


def eye(m):
    return [[int(j==i) for j in range(m)] for i in range(m)]


def matmul(A,B):
    return [[dot(row,col) for col in transpose(B)] for row in A]


def checked_smith(A):
    rows,cols=len(A),len(A[0])
    if not cols:
        return [],eye(rows),[]
    M=R.MatrixInt(A)
    S=R.MatrixInt(M)
    V,Vi,U,Ui=[R.MatrixInt(1) for _ in range(4)]
    R.smithNormalForm(S,V,Vi,U,Ui)
    assert U*M*V==S and (U*Ui).isIdentity() and (V*Vi).isIdentity()
    diag=[S.entry(i,i).pythonValue() for i in range(S.rank())]
    assert all(d>0 for d in diag) and all(b%a==0 for a,b in zip(diag,diag[1:]))
    return diag,mat(U),mat(V)


def field_solution(A,b,p,nvars):
    tab=[[x%p for x in row]+[z%p] for row,z in zip(A,b)]
    rr=0; pivots=[]
    for j in range(nvars):
        idx=next((i for i in range(rr,len(tab)) if tab[i][j]),None)
        if idx is None: continue
        tab[idx],tab[rr]=tab[rr],tab[idx]
        inv=pow(tab[rr][j],-1,p)
        tab[rr]=[(a*inv)%p for a in tab[rr]]
        for i in range(len(tab)):
            if i!=rr:
                tab[i]=[(a-tab[i][j]*s)%p for a,s in zip(tab[i],tab[rr])]
        pivots.append(j);rr+=1
    if any(not any(row[:-1]) and row[-1] for row in tab):return len(pivots),None
    x=[0]*nvars
    for i,j in enumerate(pivots): x[j]=tab[i][-1]
    assert all((dot(row,x)-z)%p==0 for row,z in zip(A,b))
    return len(pivots),x


def euler_standard(tri):
    n=tri.size(); e=[1]*(7*n)
    for face in tri.triangles():
        emb=face.front(); i,opp=emb.simplex().index(),emb.face()
        for k in range(7):
            if k!=opp:e[7*i+k]-=1
    for edge in tri.edges():
        emb=edge.front();i=emb.simplex().index()
        v,w=emb.vertices()[0],emb.vertices()[1]
        e[7*i+v]+=1;e[7*i+w]+=1
        for k in range(3):
            if (v in (0,k+1))!=(w in (0,k+1)):e[7*i+4+k]+=1
    return e


def build(tri):
    assert tri.isValid() and tri.isClosed() and tri.isOrientable() and tri.countVertices()==1
    n=tri.size()
    A=mat(R.makeMatchingEquations(tri,R.NS_STANDARD))
    AO=mat(R.makeMatchingEquations(tri,R.NS_AN_STANDARD))
    B=mat(R.makeMatchingEquations(tri,R.NS_QUAD))
    BO=mat(R.makeMatchingEquations(tri,R.NS_AN_QUAD_OCT))
    triangles=[7*i+t for i in range(n) for t in range(4)]
    quads=[7*i+j for i in range(n) for j in (4,5,6)]
    for an,ao in zip(A,AO):
        for i in range(n):
            assert ao[10*i:10*i+7]==an[7*i:7*i+7]
            for k in range(3):
                assert ao[10*i+7+k]==sum(an[7*i+4+j] for j in range(3) if j!=k)
    for bn,bo in zip(B,BO):
        for i in range(n):
            assert bo[6*i:6*i+3]==bn[3*i:3*i+3]
            assert bo[6*i+3:6*i+6]==[-z for z in bn[3*i:3*i+3]]
    T=[[row[t] for t in triangles] for row in A]
    Q=[[row[t] for t in quads] for row in A]
    E=euler_standard(tri); et=[E[t] for t in triangles];eq=[E[t] for t in quads]
    assert sum(et)==2
    paths=[None]*(4*n); paths[0]=[0]*(3*n)
    edges=[[] for _ in paths]
    for i,row in enumerate(T):
        pos=[j for j,x in enumerate(row) if x==1];neg=[j for j,x in enumerate(row) if x==-1]
        assert sum(abs(x) for x in row)==2*len(pos) and len(pos)==len(neg)<=1
        if pos:
            a,b=pos[0],neg[0];edges[a].append((b,i,1));edges[b].append((a,i,-1))
    wait=deque([0])
    while wait:
        a=wait.popleft()
        for b,i,sign in edges[a]:
            if paths[b] is None:
                paths[b]=add(paths[a],Q[i],sign);wait.append(b)
    assert all(row is not None for row in paths)
    residual=[add(qr,p) for qr,p in zip(Q,matmul(T,paths))]
    assert R.MatrixInt(B+residual).rank()==R.MatrixInt(B).rank()==R.MatrixInt(residual).rank()
    d0=eq
    for a,t in zip(paths,et):d0=add(d0,a,t)
    d=[add(d0,a,-2) for a in paths]
    for tau,row in enumerate(d):
        assert all(sum(row[3*i:3*i+3])==-1+2*(tau//4==i) for i in range(n))
    return T,Q,et,eq,B,d


def prime_euler(T,Q,et,eq,tau,p):
    if p<3 or any(p%j==0 for j in range(2,isqrt(p)+1)):return None
    G=[int(i==tau) for i in range(len(et))]
    H=T+[G]
    rank,_=field_solution(H,[0]*len(H),p,len(et))
    if rank!=len(et):return None
    _,weights=field_solution(transpose(H),et,p,len(H))
    assert weights is not None
    d=[(v-dot(weights[:-1],c))%p for v,c in zip(eq,transpose(Q))]
    return d,weights


def charge(B,d,J,exc,tau):
    # Bq=hb, chi=d_J q+h*delta. H=0 encodes that h=0 is the only match.
    A=[[row[j] for j in J] for row in B]; b=[row[exc] for row in B]
    D=[d[j] for j in J]
    zeros=(tau,) if isinstance(tau,int) else tau
    delta=-d[exc]-2+2*sum(i//4==exc//3 for i in zeros)
    diag,U,V=checked_smith(A)
    y=[dot(row,b) for row in U];rank=len(diag)
    w=[dot(D,c) for c in transpose(V)]
    g=gcd(*w[rank:]);H=0 if any(y[rank:]) else lcm(*(s//gcd(s,v) for s,v in zip(diag,y)))
    eta=None;witness=None
    if H:
        z=[H*v//s for s,v in zip(diag,y)]+[0]*(len(J)-rank)
        witness=[dot(row,z) for row in V]
        assert all(dot(row,witness)==H*v for row,v in zip(A,b))
        eta=dot(D,witness)+H*delta
    return dict(H=H,g=g,representative_eta=eta,match_lift=witness,
                s=diag,U_rhs=y,delta=delta), (A,D,b,delta,U,y)


def first_local(A,b,p):
    diag,U,V=checked_smith(A)
    y=[dot(row,b) for row in U]
    best=None
    for i,(v,s) in enumerate(zip(y,diag+[0]*(len(A)-len(diag)))):
        if v==0:continue
        power=p;k=1
        while v%power==0:power*=p;k+=1
        if s%power==0 and (best is None or k<best[0]):
            row=[a%power for a in U[i]]
            assert all(dot(row,col)%power==0 for col in transpose(A))
            assert dot(row,b)%power
            best=(k,power,row,dot(row,b)%power)
    return best


def in_charge(data,h,chi):
    H,g,eta=data['H'],data['g'],data['representative_eta']
    if H==0:
        if h:return False
        target=chi
    else:
        if h%H:return False
        target=chi-h//H*eta
    return target%g==0 if g else target==0


def determinant_certificate(A,D):
    S,_,V=checked_smith(A)
    Saug,_,_=checked_smith(A+[D])
    w=[dot(D,c) for c in transpose(V)]
    g=gcd(*w[len(S):])
    if len(Saug)==len(S):
        assert g==0
    else:
        from math import prod
        assert prod(Saug)==g*prod(S)
    return [S,Saug,g]


def geometries():
    summary=[]
    for name,tri in (('S3',R.Example3.threeSphere()),('Bing',R.Example3.bingsHouse()),
                     ('L(3,1)',R.Example3.lens(3,1)),('Poincare',R.Example3.poincare())):
        T,Q,et,eq,B,d=build(tri); n=tri.size()
        actual=0; positive=[]
        for s in R.NormalSurfaces(tri,R.NS_AN_QUAD_OCT):
            o=[s.octs(i,k).pythonValue() for i in range(n) for k in range(3)]
            if sum(o)!=1:continue
            exc=o.index(1)
            q=[s.quads(i,k).pythonValue() for i in range(n) for k in range(3)]
            t=[s.triangles(i,k).pythonValue() for i in range(n) for k in range(4)]
            J=[i for i,v in enumerate(q) if v]
            assert all(i//3!=exc//3 for i in J)
            Z=[i for i,v in enumerate(t) if v==0]
            assert Z
            chi=s.eulerChar().pythonValue()
            for tau in Z:
                cert,_=charge(B,d[tau],J,exc,tau)
                assert in_charge(cert,1,chi)
                assert dot(d[tau],q)+cert['delta']==chi
            if chi==2:
                positive.append(dict(exc=exc,repair_states=Z,triangles=t,quads=q,
                                     matching_connected=s.isConnected(),orientable=s.isOrientable()))
            actual+=1
        summary.append(dict(control=name,isosig=tri.isoSig(),vertex_surfaces_with_one_octagon=actual,
                            euler_two=positive))
    return summary


def multivertex():
    tri=R.Example3.threeSphere()
    assert tri.pachner(tri.tetrahedron(0))
    n=tri.size()
    vertices=[[4*i+j for i in range(n) for j in range(4)
               if tri.tetrahedron(i).vertex(j).index()==v] for v in range(tri.countVertices())]
    A=mat(R.makeMatchingEquations(tri,R.NS_STANDARD))
    B=mat(R.makeMatchingEquations(tri,R.NS_QUAD))
    tj=[7*i+j for i in range(n) for j in range(4)]
    qj=[7*i+4+j for i in range(n) for j in range(3)]
    eq0=euler_standard(tri); et=[eq0[j] for j in tj];eq=[eq0[j] for j in qj]
    assert [sum(et[j] for j in corners) for corners in vertices]==[2]*len(vertices)
    T=[[row[j] for j in tj] for row in A]; Q=[[row[j] for j in qj] for row in A]
    edges=[[] for _ in tj]
    for i,row in enumerate(T):
        if 1 in row:
            u,w=row.index(1),row.index(-1)
            edges[u].append((w,i,1));edges[w].append((u,i,-1))
    from itertools import product
    surfaces=[]
    for surf in R.NormalSurfaces(tri,R.NS_AN_QUAD_OCT):
        o=[surf.octs(i,j).pythonValue() for i in range(n) for j in range(3)]
        if sum(o)==1:
            surfaces.append((o.index(1),
                             [surf.quads(i,j).pythonValue() for i in range(n) for j in range(3)],
                             [surf.triangles(i,j).pythonValue() for i in range(n) for j in range(4)],
                             surf.eulerChar().pythonValue()))
    gauges=physical_checks=0; sharp=None
    for tau in product(*vertices):
        gauges+=1
        paths=[None]*len(tj)
        for z in tau:paths[z]=[0]*len(qj)
        todo=deque(tau)
        while todo:
            u=todo.popleft()
            for w,i,sgn in edges[u]:
                if paths[w] is None:
                    paths[w]=add(paths[u],Q[i],sgn);todo.append(w)
        assert None not in paths
        d=eq
        for x,row in zip(et,paths):d=add(d,row,x)
        counts=[sum(i//4==t for i in tau) for t in range(n)]
        assert all(sum(d[3*t:3*t+3])==2*counts[t]-1 for t in range(n))
        for exc,q,tv,chi in surfaces:
            if all(tv[j]==0 for j in tau):
                assert dot(d,q)-d[exc]-2+2*counts[exc//3]==chi
                physical_checks+=1
        if sharp is None and max(counts)==2:
            free=counts.index(2)
            for omitted in range(n):
                if omitted==free:continue
                other=[i for i in range(n) if i not in (omitted,free)]
                for types in product(range(3),repeat=len(other)):
                    J=sorted([3*free+j for j in range(3)]+[3*i+j for i,j in zip(other,types)])
                    M=[[row[j] for j in J] for row in B];D=[d[j] for j in J]
                    ss,sa,g=determinant_certificate(M,D)
                    if g==3:
                        sharp=dict(tau=tau,free_tetrahedron=free,exceptional_tetrahedron=omitted,J=J,
                                   homogeneous_g=g,smith=ss,augmented_smith=sa,
                                   exceptional_types=[charge(B,d,J,3*omitted+j,tau)[0]
                                                      for j in range(3)])
                        break
                if sharp is not None:break
    assert sharp and physical_checks
    return dict(isosig=tri.isoSig(),n=n,vertices=len(vertices),gauges=gauges,
                octagonal_vertex_surfaces=len(surfaces),surface_gauge_checks=physical_checks,
                sharp_half_vertex_example=sharp)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",type=Path)
    args=parser.parse_args()
    controls=[
        ('S3',R.Example3.threeSphere(),0,0,[],2),
        ('Poincare',R.Example3.poincare(),0,0,[3,6,10,14],0),
        ('Weeks9',R.Example3.weeks(),3,0,[0,3,4,5,7,13,17,20,21,25],31),
        ('Weeks8',R.Example3.weeks(),3,1,[1,3,6,7,8,12,17,20,23,26],33),
    ]
    records=[]
    for name,tri,ex,k,J,tau in controls:
        T,Q,et,eq,B,d=build(tri); exc=3*ex+k
        state,parts=charge(B,d[tau],J,exc,tau)
        A,D,b,delta,U,y=parts
        rhs=b+[2-delta]; C=A+[D]
        row=dict(name=name,isosig=tri.isoSig(),exceptional_tetrahedron=ex,octagon_type=k,
                 repair=tau,allowed_quad_columns=J,arithmetic=state,
                 determinant_divisors_smith_factors=determinant_certificate(A,D),
                 residue_detection={},full_target_in_image=in_charge(state,1,2))
        for p in (2,3,5):
            z=first_local(C,rhs,p)
            if z:
                lev,power,lam,res=z
                row['residue_detection'][p]=dict(first=lev,modulus=power,left=lam,rhs_residue=res)
            else:row['residue_detection'][p]=None
        if name=='S3':
            assert state['H']==1 and state['g']==0 and state['representative_eta']==2
            local=[]
            for it in range(4):
                dp,alpha=prime_euler(T,Q,et,eq,it,3)
                delta_p=-dp[exc]-2+2*(it//4==ex)
                den=(2-delta_p)%3
                assert den==(2 if it in (0,1) else 0)
                local.append(dict(repair=it,prime=3,alpha=alpha[:-1],mu=alpha[-1],d=dp,
                                  lambda_B=[0]*len(B),target_minus_lambda_rhs=den,killed=bool(den)))
            row['all_prime_repair_states']=local
        if name in ('Weeks9','Weeks8'):
            p=3 if name=='Weeks9' else 2
            kfirst=2 if name=='Weeks9' else 3
            assert row['residue_detection'][p]['first']==kfirst
            case=first_local(A,b,p)
            assert case is not None
            lev,power,lam,res=case
            assert lev==kfirst
            assert all(dot(lam,col)%power==0 for col in transpose([a[1:] for a in A]))
            row['bare_matching_inherited']=dict(prime=p,first=lev,modulus=power,left=lam,
                                                rhs_residue=res,delete_column=J[0])
            # The free tetrahedron has g=1 for every repair. Verify full branch death.
            assert any(all(3*i+j in J for j in range(3)) for i in range(tri.size()))
            for it in range(4*tri.size()):
                cert,_=charge(B,d[it],J,exc,it)
                assert cert['g']==1 and not in_charge(cert,1,2)
            row['dead_repairs']=4*tri.size()
        records.append(row)
    # An intentionally non-incidence triangle matrix: the bad-prime guard must reject.
    assert prime_euler([[1,0],[0,3]],[[0],[0]],[1,1],[0],0,3) is None
    assert prime_euler([[1,0],[0,3]],[[0],[0]],[1,1],[0],0,5) is not None
    assert prime_euler([[1,0],[0,3]],[[0],[0]],[1,1],[0],0,2) is None
    T,Q,et,eq,B,d=build(R.Example3.threeSphere())
    J=[0];A=[[r[j] for j in J] for r in B]
    normal=[]
    for tau in range(4):
        dp,w=prime_euler(T,Q,et,eq,tau,3)
        D=[dp[j] for j in J]
        _,lam=field_solution(transpose(A),D,3,len(B))
        val=determinant_certificate(A,[d[tau][j] for j in J])[-1]
        normal.append(dict(tau=tau,g=val,field_row=lam,killed=lam is not None))
    assert [u['killed'] for u in normal]==[True,True,False,False]
    result=dict(regina_package=version("regina"),controls=records,normal_Q_partial=normal,
                actual_QO_vertices=geometries(),multiple_vertices=multivertex(),synthetic_rank_drop=dict(mod3='rejected',mod5='full_rank'))
    output=json.dumps(result,ensure_ascii=False,indent=2)
    if args.verify:
        if json.loads(output)!=json.loads(args.verify.read_text()):
            raise ValueError("certificate disagrees with reconstructed controls")
        print("PASS")
    else: print(output)


if __name__=='__main__':
    main()
