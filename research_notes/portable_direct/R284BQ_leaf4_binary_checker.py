"""R284BQ exact exhaustive 4x4 binary star-Port frozen-leaf certificate.
Python 3 standard library. No floating point or third-party dependencies.
The signed-det Port is auxiliary; it does not assert native X6/BRC physical realization.
"""
import itertools
import json
from hashlib import sha256
from pathlib import Path

ALPHABET = (1, 2)
COUNT = 1 << 16
RANGE = range(-16, 17)


def det_adjv3(B, v):
    a,b,c,d,e,f,g,h,i = B
    adj = (e*i-f*h, c*h-b*i, b*f-c*e,
           f*g-d*i, a*i-c*g, c*d-a*f,
           d*h-e*g, b*g-a*h, a*e-b*d)
    D = a*adj[0]+b*adj[3]+c*adj[6]
    return D, tuple(sum(adj[3*k+j]*v[j] for j in range(3)) for k in range(3))


def signature(C,t):
    """Coefficients of F_C(d0,x2,x3,z), 20 entries grouped as:
    L, g1, g2, g3 (4 each), constant-in-d0,z baseline (4).
    Each group is [1,x2,x3,x2*x3]. z_i has coefficient -g_i.
    F_C = (d0-a)*L - sum_i (b_i+z_i)*g_i.
    """
    a=C[0]; b=C[1:4]; v=(C[4],C[8],C[12])
    A=[C[4*i+j] for i in range(1,4) for j in range(1,4)]
    measurements=[]; base=[]
    for x2,x3 in ((0,0),(1,0),(0,1),(1,1)):
        B=(t-A[0],-A[1],-A[2],-A[3],x2-A[4],-A[5],-A[6],-A[7],x3-A[8])
        L,g=det_adjv3(B,v)
        measurements.append((L,*g))
        base.append(-a*L-sum(bi*gi for bi,gi in zip(b,g)))
    result=[]
    for j in range(4):
        y00,y10,y01,y11=(row[j] for row in measurements)
        result.extend((y00,y10-y00,y01-y00,y11-y10-y01+y00))
    y00,y10,y01,y11=base
    result.extend((y00,y10-y00,y01-y00,y11-y10-y01+y00))
    return tuple(result)


def no_constant(coeff):
    # Baseline absolute constant is coefficient 16.
    return coeff[:16]+coeff[17:]


def det4_permutation(M):
    ans=0
    for perm in itertools.permutations(range(4)):
        parity=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term=1
        for i,j in enumerate(perm): term*=M[i][j]
        ans+=(-1 if parity%2 else 1)*term
    return ans


def direct_f(C,t,d0,x2,x3,z):
    M=[[(-C[4*i+j]) for j in range(4)] for i in range(4)]
    for i,x in enumerate((d0,t,x2,x3)):
        M[i][i]+=x
    for i in range(1,4): M[0][i]-=z[i-1]
    return det4_permutation(M)


def pred_f(coeff,d0,x2,x3,z):
    def p(part):return part[0]+part[1]*x2+part[2]*x3+part[3]*x2*x3
    return d0*p(coeff[:4])-sum(z[j]*p(coeff[4*(j+1):4*(j+2)]) for j in range(3))+p(coeff[16:20])


def run():
    matrices=list(itertools.product(ALPHABET,repeat=16))
    assert len(matrices)==COUNT
    max_q=0; joint=set(); crosschecks=0
    # Q = F(t=0), P = F(t=1)-F(t=0); omit only absolute constant.
    for i,C in enumerate(matrices):
        c0=signature(C,0); c1=signature(C,1)
        max_q=max(max_q,max(map(abs,c0)))
        pair=(no_constant(c0),no_constant(c1))
        assert pair not in joint, 'A t-independent nonconstant fibre detected'
        joint.add(pair)
        # Independent 4x4 Leibniz determinant (different implementation)
        # at spread-out reproducible matrices and signed controls.
        if i%2048==0:
            for t in (-3,0,5):
                coeff=signature(C,t)
                d0=(i//2048)%7-3
                x2=(i//128)%9-4
                x3=(i//32)%11-5
                z=(i%5-2,(i//8)%7-3,(i//16)%9-4)
                assert pred_f(coeff,d0,x2,x3,z)==direct_f(C,t,d0,x2,x3,z)
                crosschecks+=1
    assert max_q==8 and len(joint)==COUNT

    census={}; witnesses={}; nonconstant_gap={}
    for t in RANGE:
        full=set(); grouped={}
        equal_witness=None; constant_witness=None
        for C in matrices:
            co=signature(C,t); nc=no_constant(co)
            if co in full and equal_witness is None:
                equal_witness=(grouped[nc][0],C)
            full.add(co)
            if nc in grouped:
                oldC,oldk=grouped[nc]
                if oldk!=co[16] and constant_witness is None:
                    constant_witness=(oldC,C,co[16]-oldk)
            else:
                grouped[nc]=(C,co[16])
        census[str(t)]={'distinct_nonconstant':len(grouped),'distinct_full':len(full)}
        assert (len(grouped)==COUNT)==(t<=-4 or t>=5)
        assert (len(full)==COUNT)==(t<=-4 or t>=5)
        if equal_witness:
            witnesses[str(t)]=[''.join(map(str,x)) for x in equal_witness]
        if constant_witness:
            C,D,k=constant_witness
            nonconstant_gap[str(t)]={'C':''.join(map(str,C)),'D':''.join(map(str,D)),'signed_gap':k}
    assert len(witnesses)==8 and set(witnesses)==set(map(str,range(-3,5)))
    assert set(nonconstant_gap)==set(map(str,range(-3,2)))

    return {'schema':'EM_R284BQ_N4_H2_LEAF_FROZEN_EXACT_CERT_V1',
       'model':'F_C=det(diag(d0,t,x2,x3)-C-z1E01-z2E02-z3E03), C in {1,2}^{4x4}',
       'candidate_matrices':COUNT,'fixed_leaf_index':1,
       'tested_t_range':[-16,16],
       'independent_leibniz_checks':crosschecks,
       'max_abs_coefficient_Q_at_t0':max_q,
       'joint_noncst_signature_pairs_at_t0_t1':len(joint),
       'bound_logic':'For any collision at integer t with different t-slopes, |t|<=2*max_abs_Q=16; identical slopes/intercepts excluded by joint injectivity.',
       'census':census, 'exact_collision_witnesses':witnesses,
       'constant_nonzero_gap_witnesses':nonconstant_gap,
       'proven_injective_integer_t':'t<=-4 or t>=5',
       'proven_noninjective_integer_t':'-3<=t<=4',
       'review':'NOT_REVIEWED'}


if __name__=='__main__':
    result=run()
    outpath=Path(__file__).with_name('R284BQ_leaf4_binary_verification.json')
    with outpath.open('w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('census','exact_collision_witnesses','constant_nonzero_gap_witnesses')},indent=2))
    print('sha256_JSON',sha256(outpath.read_bytes()).hexdigest())
