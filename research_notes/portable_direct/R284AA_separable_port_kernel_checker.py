#!/usr/bin/env python3
"""R284AA exact checks: independently unit-edited Port pencil, full match but no fixed kernels.
Uses fractions.Fraction only; finite checks are tests, theorem in accompanying note.
"""
from fractions import Fraction as F
from itertools import product, permutations
from json import dumps

P=(0,1); A=(2,3); B=(4,5); Q=(6,7)
S=A+B
c=F(1,16)
loops=(F(1,16),F(1,32),F(1,24),F(1,20))
base=F(1,8)

def mat(x=F(0), y=F(0), u=F(0), v=F(0), eta=F(0)):
    W=[[F(0) for _ in range(8)] for _ in range(8)]
    g=[base+x,base+y]; h=[base+u,base+v]
    for i in range(2):
        W[P[i]][A[i]]=g[i]
        W[B[i]][Q[i]]=h[i]
    for i in range(2):
        for j in range(2): W[A[i]][B[j]]=c+(eta if i==j==0 else F(0))
    for i,k in enumerate(S): W[k][k]=loops[i]
    assert all(F(0)<=t<1 for row in W for t in row)
    assert all(sum(row)<1 for row in W)
    M=[[(F(1) if i==j else F(0))-W[i][j] for j in range(8)] for i in range(8)]
    subrows=list(S+P); subcols=list(S+Q)
    D=[[M[i][j] for j in subcols] for i in subrows]
    return W,M,D,g,h

def det(M):
    A=[row[:] for row in M]; n=len(A)
    if not n: return F(1)
    d=F(1)
    for j in range(n):
        piv=next((k for k in range(j,n) if A[k][j]),None)
        if piv is None: return F(0)
        if piv!=j: A[piv],A[j]=A[j],A[piv]; d=-d
        t=A[j][j]; d*=t
        for k in range(j+1,n):
            if not A[k][j]: continue
            f=A[k][j]/t
            for l in range(j+1,n): A[k][l]-=f*A[j][l]
            A[k][j]=0
    return d

def rank(M):
    A=[row[:] for row in M]
    if not A:return 0
    n=len(A);m=len(A[0]);k=0
    for j in range(m):
        q=next((i for i in range(k,n) if A[i][j]),None)
        if q is None:continue
        A[k],A[q]=A[q],A[k]; piv=A[k][j]
        for l in range(j,m):A[k][l]/=piv
        for i in range(n):
            if i!=k and A[i][j]:
                v=A[i][j]
                for l in range(j,m):A[i][l]-=v*A[k][l]
        k+=1
        if k==n:break
    return k

def inverse(M):
    n=len(M)
    A=[M[i][:]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        assert k is not None
        A[j],A[k]=A[k],A[j]
        v=A[j][j]
        A[j]=[x/v for x in A[j]]
        for i in range(n):
            if i!=j:
                t=A[i][j]
                A[i]=[a-t*b for a,b in zip(A[i],A[j])]
    return [row[n:] for row in A]

def mmul(X,Y):
    return [[sum((X[i][k]*Y[k][j] for k in range(len(Y))),F(0)) for j in range(len(Y[0]))] for i in range(len(X))]

def schur_transfer(W):
    G=[[(F(i==j)-W[S[i]][S[j]]) for j in range(4)] for i in range(4)]
    PS=[[W[p][s] for s in S] for p in P]
    SQ=[[W[s][q] for q in Q] for s in S]
    direct=[[W[p][q] for q in Q] for p in P]
    z=mmul(mmul(PS,inverse(G)),SQ)
    return [[z[i][j]+direct[i][j] for j in range(2)] for i in range(2)]

def has_perfect_support(M):
    return any(all(M[i][p[i]] != 0 for i in range(len(M))) for p in permutations(range(len(M))))

def T_formula(g,h,eta=F(0)):
    return [[g[i]*(c + (eta if i==j==0 else F(0)))*h[j]/((1-loops[i])*(1-loops[2+j])) for j in range(2)] for i in range(2)]

lo=F(0); hi=F(1,16)
checkpoints=0
for vals in product((lo,F(1,64),hi),repeat=4):
    W,M,D,g,h=mat(*vals)
    expected=F(0)
    assert det(D)==expected
    assert has_perfect_support(D)
    assert rank(D)==5
    assert schur_transfer(W)==T_formula(g,h)
    assert rank(T_formula(g,h))==1
    assert det(T_formula(g,h))==0
    checkpoints+=1

# A common right kernel would survive all 2 selected h-values, left all 2 selected g-values.
r1=mat(u=0,v=0)[2];r2=mat(u=F(1,16),v=0)[2]
l1=mat(x=0,y=0)[2];l2=mat(x=F(1,16),y=0)[2]
right_stacked_rank=rank(r1+r2)
left_stacked_rank=rank([[l1[i][j] for i in range(6)] for j in range(6)]+[[l2[i][j] for i in range(6)] for j in range(6)])
assert right_stacked_rank==6
assert left_stacked_rank==6

# Independent unit edits in x,y,u,v: a multiaffine polynomial is uniquely defined by its {0,1/16}^4 values.
corner_checks=0
for vals in product((F(0),F(1,16)),repeat=4):
    _,_,D,_,_=mat(*vals)
    assert det(D)==0
    corner_checks+=1

# Perturb a *single* mixing edge a1->b1 by eta; prediction det A = g1*g2*h1*h2 * eta*c, independent of internal loops.
perturb_checks=0
for vals in product((F(0),F(1,64)),repeat=4):
    W,M,D,g,h=mat(*vals,eta=F(1,32))
    target=g[0]*g[1]*h[0]*h[1]*c*F(1,32)
    assert det(D)==target and target>0
    assert rank(D)==6
    perturb_checks+=1

# Prove coefficient in the observation cofactor N_(0,6) for target edge 7->1 vanishes:
# F_(0,6) = (-1)^(0+6)*det M[delete row 6, col 0]/det M.
# x_target appears at (row7,col1), its coefficient is - times a signed complementary 6x6 minor D,
# therefore exactly zero (with row/col ordering caveat); verify numerator difference equals zero.
cofactor_checks=0
for vals in product((F(0),F(1,32)),repeat=4):
    W,M,D,g,h=mat(*vals)
    N0=det([[M[i][j] for j in range(8) if j!=0] for i in range(8) if i!=6])
    M[7][1]-=F(1,32)
    Nx=det([[M[i][j] for j in range(8) if j!=0] for i in range(8) if i!=6])
    assert N0==Nx
    cofactor_checks+=1

out={
 "schema":"ENTERPRISE_MATH_R284AA_EXACT_VERIFICATION_V1", "status":"PASS",
 "arithmetic":"Python fractions.Fraction; exact Gaussian elimination",
 "named_ports":{"P":[0,1],"A":[2,3],"B":[4,5],"Q":[6,7]},
 "base_gate":"1/8", "gate_edit_box":"0<=x,y,u,v<=1/16", "mixing_entry":"1/16",
 "internal_loops":[str(t) for t in loops],
 "sample_checks":{"3^4_exact_parameter_grid_and_independent_schur_inversion":checkpoints,"2^4_multiaffine_corners":corner_checks,"single_mixer_edit_16_corners":perturb_checks,"observer_target_cofactor_16_pairs":cofactor_checks},
 "baseline_complement_rank":rank(mat()[2]),"baseline_complement_det":str(det(mat()[2])),
 "perfect_support_matching":has_perfect_support(mat()[2]),
 "right_kernel_intersection_stacked_rank":right_stacked_rank,
 "left_kernel_intersection_stacked_rank":left_stacked_rank,
 "mixer_edge_perturbation":{"eta":"1/32","det_at_base":str(det(mat(eta=F(1,32))[2])),"closed_form":"g1*g2*h1*h2*eta/16"},
 "theorem_not_equivalent_to_finite_test":True,
 "source_input":"R284Y (eb197ee78efb59a38657c0f9ae4fbf7ed0a8950c); R284Z (1df6634e10467fef49504c0455bd73402dd815ad)"
}
print(dumps(out,indent=2,ensure_ascii=False))
