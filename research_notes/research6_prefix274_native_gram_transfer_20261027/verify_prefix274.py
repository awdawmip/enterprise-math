"""Exact tagged ordered-source-pair BRC Gram transfer; author-side only."""
from fractions import Fraction as Q
from itertools import product, combinations

def gram(v):
    return [[sum((x*y for x,y in zip(a,b)),Q(0)) for b in v] for a in v]

def brc_intensity(g,m,s):
    n=len(m)
    return sum((Q(s[i]*s[j])*m[i]*m[j]*g[i][j]
                for i in range(n) for j in range(n)),Q(0))

def phase_coeff_gram(c):
    return [[x*y for y in c] for x in c]

def check_case(k):
    m=[Q(i+1,i+2) for i in range(k)]
    c=[Q(i+2,i+1) for i in range(k)]
    vecs=[(Q(i+1,i+2),Q((i%3)-1,i+3),Q(1,i+1)) for i in range(k)]
    g=gram(vecs)
    gc=phase_coeff_gram(c)
    signs=list(product((-1,1),repeat=k))
    d=sum((m[i]**2*(g[i][i]-gc[i][i]) for i in range(k)),Q(0))
    off={(i,j):g[i][j]-gc[i][j] for i in range(k) for j in range(i+1,k)}
    diffs=[]
    for s in signs:
        a=brc_intensity(g,m,s)
        b=brc_intensity(gc,m,s)
        assert b==sum((m[i]*c[i]*s[i] for i in range(k)),Q(0))**2
        diff=a-b
        expected=d+2*sum((m[i]*m[j]*s[i]*s[j]*off[i,j] for i,j in off),Q(0))
        assert diff==expected
        diffs.append(diff)
    assert sum(diffs,Q(0))/len(diffs)==d
    for i,j in off:
        recovered=sum((diff*s[i]*s[j] for diff,s in zip(diffs,signs)),Q(0))/(len(signs)*2*m[i]*m[j])
        assert recovered==off[i,j]
    empirical=sum((diff*diff for diff in diffs),Q(0))/len(signs)
    analytic=d*d+4*sum((m[i]**2*m[j]**2*r*r for (i,j),r in off.items()),Q(0))
    assert empirical==analytic

    # Sparse degree-2 Boolean Mobius inversion: zero, singleton, pair flips.
    def delta_flips(indices):
        s=tuple(-1 if i in indices else 1 for i in range(k))
        return brc_intensity(g,m,s)-brc_intensity(gc,m,s)
    base=delta_flips(())
    singles={i:delta_flips((i,)) for i in range(k-1)}
    pairs={(i,j):delta_flips((i,j)) for i,j in combinations(range(k-1),2)}
    b_rec={}
    for (i,j),value in pairs.items():
        b_rec[i,j]=(value-singles[i]-singles[j]+base)/4
    for i in range(k-1):
        b_rec[i,k-1]=-(singles[i]-base)/2-sum(
            (b_rec[min(i,j),max(i,j)] for j in range(k-1) if i!=j),Q(0))
    assert all(b_rec[i,j]==2*m[i]*m[j]*off[i,j] for i,j in off)
    assert base-sum(b_rec.values(),Q(0))==d
    sparse=1+(k-1)+(k-1)*(k-2)//2
    assert sparse==1+k*(k-1)//2
    for s in signs:
        assert brc_intensity(gc,m,s)==sum((m[i]*c[i]*s[i] for i in range(k)),Q(0))**2
    return len(signs),len(off),sparse

def gauss_mul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def gauss_conj(a):
    return (a[0],-a[1])

def c4_ordered_pair_intensity(g,amplitudes):
    total=(Q(0),Q(0))
    for i,ai in enumerate(amplitudes):
        for j,aj in enumerate(amplitudes):
            term=gauss_mul(gauss_mul(gauss_conj(ai),g[i][j]),aj)
            total=(total[0]+term[0],total[1]+term[1])
    assert total[1]==0
    return total[0]

def main():
    total_signs=total_pairs=total_sparse=0
    for k in range(2,7):
        signs,pairs,sparse=check_case(k)
        total_signs+=signs
        total_pairs+=pairs
        total_sparse+=sparse
        print(f"k={k}: signs={signs}; sparse_probes={sparse}; reconstructed_pair_coefficients={pairs}; EXACT_PASS")
    coherent=[[Q(1),Q(1)],[Q(1),Q(1)]]
    separate=[[Q(1),Q(0)],[Q(0),Q(1)]]
    for s,want_coh,want_sep in [((1,1),Q(4),Q(2)),((1,-1),Q(0),Q(2))]:
        assert brc_intensity(coherent,[Q(1),Q(1)],s)==want_coh
        assert brc_intensity(separate,[Q(1),Q(1)],s)==want_sep
        print(f"witness phase={s}: coherent={want_coh}; tagged_separate={want_sep}")
    one=(Q(1),Q(0)); imag=(Q(0),Q(1))
    plus_half_i=(Q(0),Q(1,2)); minus_half_i=(Q(0),Q(-1,2))
    gamma_pos=[[one,plus_half_i],[minus_half_i,one]]
    gamma_neg=[[one,minus_half_i],[plus_half_i,one]]
    for s0,s1 in product((-1,1),repeat=2):
        amp=[(Q(s0),Q(0)),(Q(s1),Q(0))]
        assert c4_ordered_pair_intensity(gamma_pos,amp)==Q(2)
        assert c4_ordered_pair_intensity(gamma_neg,amp)==Q(2)
    assert c4_ordered_pair_intensity(gamma_pos,[one,imag])==Q(1)
    assert c4_ordered_pair_intensity(gamma_neg,[one,imag])==Q(3)
    assert Q(1)-Q(1,4)==Q(3,4)>0
    print("C4_IMAGINARY_OBSTRUCTION_PASS: sign_probes_equal=2; relative_i_effects=(1,3)")
    print(f"PREFIX274_FORMAL_GRAM_TRANSFER_PASS signs={total_signs} sparse_probes={total_sparse} pair_coefficients={total_pairs}")

if __name__=="__main__":
    main()
