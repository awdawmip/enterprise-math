"""Exact coefficients and rank, cost and tensor checks for the marked [-3] family."""
import json
from fractions import Fraction as Q
from math import prod
from itertools import product


def dim_profiles(p,q,lower=(0,0)):
    if p+q==0:
        yield ()
        return
    for a in range(p+1):
        for b in range(q+1):
            if a+b==0 or (a,b)<lower:
                continue
            for rest in dim_profiles(p-a,q-b,(a,b)):
                yield ((a,b),)+rest


def gaussian_times(z,w):
    a,b=z
    c,d=w
    return a*c-b*d,a*d+b*c


def gaussian_power(z,n):
    w=(1,0)
    for _ in range(n):
        w=gaussian_times(z,w)
    return w


def matrix_times(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]


def tensor(A,B):
    return [[x*y for x in ar for y in br] for ar in A for br in B]


def main():
    profiles=list(dim_profiles(3,3))
    nontrivial=[r for r in profiles if len(r)>=2]
    dims=[sum(a*b for a,b in r) for r in nontrivial]
    maximizers=[r for r,d in zip(nontrivial,dims) if d==max(dims)]
    assert max(dims)==6 and set(maximizers)=={((0,1),(3,2)),((1,0),(2,3))}
    # Below or at chi=9 all positive integral polarizations are exhaustively listed.
    costs=[]
    for n in range(1,10):
        for m in range(1,10):
            v=3*m*n**5
            if v<=9:
                # 3*m*n <= 9 here. Gaussian norms 1..9 have rational norm iff
                # each inert prime valuation is even. Here the only obstruction is 3.
                x=3*m*n
                v3=0
                while x%3==0:
                    x//=3
                    v3+=1
                split=v3%2==0 and x in (1,2)
                costs.append([m,n,v,v*v,split])
    assert [c for c in costs if c[-1]]==[[3,1,9,81,True]]
    positive_line_split_weights=[3,1,1,1,1,3]
    negative_line_split_weights=[1,1,1,1,1,1]
    assert prod(positive_line_split_weights)==9 and prod(negative_line_split_weights)==1
    assert Q(1,3)*(-3)==-1
    # Integer coordinates for C* C = 3 I in the anisotropic residual pair.
    C=[[(1,0),(1,1)],[(-1,1),(1,0)]]
    gram=[]
    for j in range(2):
        row=[]
        for k in range(2):
            v=[gaussian_times((C[t][j][0],-C[t][j][1]),C[t][k]) for t in range(2)]
            row.append(tuple(map(sum,zip(*v))))
        gram.append(row)
    assert gram==[[(3,0),(0,0)],[(0,0),(3,0)]]
    U=(1,2)
    powers={str(d):gaussian_power(U,d) for d in (2,4,6,8)}
    assert powers['2']==(-3,4) and powers['6']==(117,44)
    # E^2 divisors, in the order Gamma_1,Gamma_i,H,V.
    intersection=[[0,2,1,1],[2,0,1,1],[1,1,0,1],[1,1,1,0]]
    divisors=[[1,0,-1,-1],[0,1,-1,-1]]
    pair=matrix_times(matrix_times(divisors,intersection),list(zip(*divisors)))
    assert pair==[[-2,0],[0,-2]]
    J=[[0,-1],[1,0]]
    UJ=tensor(J,J)
    projector=[[Q(int(i==j)-UJ[i][j],2) for j in range(4)] for i in range(4)]
    assert matrix_times(projector,projector)==projector
    # W6 basis w,Jw and W2 basis a,b. Embed x as x (tensor) a;
    # contraction by a uses the first row (-2,0) of the surface pairing.
    embed=[[1,0],[0,0],[0,1],[0,0]]
    contraction=[[-2,0,0,0],[0,0,-2,0]]
    composite=matrix_times(contraction,matrix_times(projector,embed))
    assert composite==[[-1,0],[0,-1]]
    assert sum(projector[i][i] for i in range(4))==2
    residues=sorted({(a*a+b*b)%3 for a,b in product(range(3),repeat=2) if a or b})
    assert residues==[1,2]
    print(json.dumps({"K":"Q(i)","hermitian_diagonal":[1,1,1,-1,-1,-3],
        "norm_mod_3_nonzero_vector":residues,
        "proper_signature_partitions":len(nontrivial),"max_locus_dimension":max(dims),
        "maximizing_signatures":maximizers,"all_chi_le_9_m_n_chi_degree_split":costs,
        "split_chi_degree_standard_positive_line":[9,81],
        "split_chi_degree_standard_negative_line":[1,1],"stabilization_gaussian_gram":gram,"u_powers_real_imag":powers,
        "surface_intersection":pair,"diagonal_projector_rank":2,
        "contraction_after_projection": [[int(x) for x in row] for row in composite]},indent=2))


if __name__=="__main__":
    main()
