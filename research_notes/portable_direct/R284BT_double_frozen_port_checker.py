"""R284BT reproducible exact certificate (Python 3 stdlib, integers only).
Matrix index convention: mask bit (4*i+j) is C[i][j]-1.
The frozen controls are d1=5,d2=50; d0,d3,z1,z2,z3 are free.
The 10-tuple is (L0,L_delta,g0_1,g0_2,g0_3,gdelta_1,gdelta_2,gdelta_3,F0,Fdelta).
"""
from collections import Counter, defaultdict
from itertools import permutations
import json

def det3(v):
    a,b,c,d,e,f,g,h,i=v
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def adj3_v(v,w):
    a,b,c,d,e,f,g,h,i=v
    return ((e*i-f*h)*w[0]+(c*h-b*i)*w[1]+(b*f-c*e)*w[2],
            (f*g-d*i)*w[0]+(a*i-c*g)*w[1]+(c*d-a*f)*w[2],
            (d*h-e*g)*w[0]+(b*g-a*h)*w[1]+(a*e-b*d)*w[2])

def matrix(mask):
    return [[1+((mask>>(4*i+j)) & 1) for j in range(4)] for i in range(4)]

def signature(mask,t=5,s=50):
    c=[1+((mask>>i)&1) for i in range(16)]
    v=(c[4],c[8],c[12]); ls=[]; gs=[]; fs=[]
    for x in (0,1):
        B=(t-c[5],-c[6],-c[7],
           -c[9],s-c[10],-c[11],
           -c[13],-c[14],x-c[15])
        L=det3(B); g=adj3_v(B,v)
        ls.append(L); gs.append(g)
        fs.append(-c[0]*L-sum(c[j+1]*g[j] for j in range(3)))
    return (ls[0],ls[1]-ls[0],*gs[0],
            *(gs[1][j]-gs[0][j] for j in range(3)),
            fs[0],fs[1]-fs[0])

def det4(m):
    total=0
    for p in permutations(range(4)):
        inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        prod=1
        for i,j in enumerate(p):prod*=m[i][j]
        total+=(-1 if inversions%2 else 1)*prod
    return total

def direct(mask,t,s,d0,d3,z1,z2,z3):
    C=matrix(mask)
    B=[[(-C[i][j] + (d0 if i==j==0 else t if i==j==1 else s if i==j==2 else d3 if i==j==3 else 0))
         for j in range(4)] for i in range(4)]
    for j,z in zip((1,2,3),(z1,z2,z3)):B[0][j]-=z
    return det4(B)

def evaluate(k,d0,d3,z1,z2,z3):
    l=k[0]+k[1]*d3
    g=[k[2+i]+k[5+i]*d3 for i in range(3)]
    f=k[8]+k[9]*d3
    return d0*l-sum(z*g_i for z,g_i in zip((z1,z2,z3),g))+f

def main():
    t,s=5,50
    full=set(); groups=defaultdict(list)
    for mask in range(1<<16):
        k=signature(mask,t,s)
        if k in full:raise AssertionError('full polynomial collision')
        full.add(k)
        nonconst=k[:8]+k[9:]
        groups[nonconst].append((k[8],mask))
        if mask%257==0:
            d0,d3,z1,z2,z3=((mask//257+i)%3-1 for i in range(5))
            assert evaluate(k,d0,d3,z1,z2,z3)==direct(mask,t,s,d0,d3,z1,z2,z3)
    assert len(full)==65536 and len(groups)==32768
    gapmin=10**100; gapmax=0; witness=None; group_sizes=Counter()
    for rows in groups.values():
        group_sizes[len(rows)]+=1
        assert len(rows)==2
        (v1,m1),(v2,m2)=sorted(rows)
        assert (m1^m2)==(1<<3)
        gap=v2-v1
        assert gap>0
        if gap<gapmin:gapmin=gap;witness=(m1,m2)
        gapmax=max(gapmax,gap)
    assert gapmin==195 and gapmax==612
    out={'schema':'R284BT_EXACT_CENSUS_V1','date':'2026-11-20','model':'n=4 H=2, two frozen leaves d1=5,d2=50','mask_convention':'bit (4*i+j) = C[i,j]-1, row-major','candidate_count':65536,'full_signatures':len(full),'nonconstant_signatures':len(groups),
         'nonconstant_fibre_sizes':dict(group_sizes),'every_nonconstant_fibre_pair_differs_only_at_C03':True,
         'min_nonzero_constant_gap':gapmin,'max_constant_gap':gapmax,'gap_min_witness_masks':list(witness),
         'gap_min_witness_matrices':[matrix(witness[0]),matrix(witness[1])],
         'finite_noise_threshold':'rho < 195/2',
         'direct_formula_crosschecks':len(range(0,65536,257)),
         'independent_review':'NOT_REVIEWED'}
    print(json.dumps(out,indent=2,ensure_ascii=False,sort_keys=True))
if __name__=='__main__':main()
