"""Exact finite checks for truncated integral matrices and their minor denominators."""
from fractions import Fraction
from itertools import combinations, permutations, product
import json
from math import factorial, gcd, lcm, prod


def identity(d):
    return [[int(r == j) for j in range(d)] for r in range(d)]


def powers_entry(i, r, j):
    if r <= j:
        return 0
    return Fraction((-1) ** (r - j - 1), r * i ** (r - j))


def matrix(i, d):
    return [[powers_entry(i, r, j) for j in range(d)] for r in range(d)]


def multiply(A, B):
    return [[sum(a*b for a,b in zip(row, col)) for col in zip(*B)] for row in A]


def minor(A, rows, cols):
    t = len(rows)
    out = 0
    for perm in permutations(range(t)):
        inv = sum(perm[i] > perm[j] for i in range(t) for j in range(i+1,t))
        out += (-1)**inv * prod(A[r][cols[h]] for r,h in zip(rows,perm))
    return out


def diagonal(d, M):
    return [factorial(r)*M**r for r in range(d)]


def word_denominators():
    I, d = (2,3), 7
    D = diagonal(d, lcm(*I))
    basis = [matrix(i,d) for i in I]
    den = [[1]*d for _ in range(d)]
    translated = {}
    word_count = 0
    stage = [identity(d)]
    for length in range(d):
        for A in stage:
            word_count += 1
            for r in range(d):
                for j in range(r+1):
                    den[r][j] = lcm(den[r][j], A[r][j].denominator)
        for t in (1,2,3):
            for J in combinations(range(d-length),t):
                R = tuple(j+length for j in J)
                pure = []
                for base in basis:
                    B = identity(d)
                    for _ in range(length):
                        B = multiply(base,B)
                    pure.append(minor(B,R,J).denominator)
                bound = prod(D[r] for r in R)//prod(D[j] for j in J)
                assert lcm(*pure) == bound
                translated[t] = translated.get(t,0)+1
        if length+1 < d:
            stage = [multiply(B,A) for A in stage for B in basis]
    assert all(den[r][j]==(D[r]//D[j] if r>=j else 1)
               for r in range(d) for j in range(d))
    R, J = (1,3), (0,1)
    l_word=lcm(*(minor(A,R,J).denominator for A in basis))
    polynomial=[]
    for A in basis:
        A2=multiply(A,A)
        polynomial.append([[x+y for x,y in zip(row1,row2)] for row1,row2 in zip(A,A2)])
    l_poly=lcm(*(minor(A,R,J).denominator for A in polynomial))
    assert (l_word,l_poly)==(3*6**3,6*6**3)
    return {"alphabet":I,"dimension":d,"words_including_empty":word_count,
            "entry_positions":d*d,"entry_row6_col2":den[6][2],
            "translated_minor_shapes_by_order":translated,
            "example_rows_1_3_cols_0_1":{"word_lcm":l_word,"polynomial_lcm":l_poly}}


def modular_minor(A,R,J,p):
    B=[[A[r][j]%p for j in J] for r in R]
    for j in range(len(R)):
        pivot=next((h for h in range(j,len(R)) if B[h][j]),None)
        if pivot is None:
            return False
        B[j],B[pivot]=B[pivot],B[j]
        r_inv=pow(B[j][j],-1,p)
        for h in range(j+1,len(R)):
            w=B[h][j]*r_inv%p
            B[h]=[(u-w*v)%p for u,v in zip(B[h],B[j])]
    return True


def good_prime_checks():
    d, I = 5, (2,3,5)
    D=diagonal(d,lcm(*I))
    result=[]
    for p in I:
        T=matrix(p,d)
        S=[[int(T[r][j]*D[r]/D[j]) if T[r][j] else 0 for j in range(d)] for r in range(d)]
        powers=[identity(d)]
        for _ in range(1,d):
            powers.append(multiply(S,powers[-1]))
        shapes=set()
        for t in range(1,min(p,d)+1):
            for R in combinations(range(d),t):
                for J in combinations(range(d),t):
                    if all(r>=j for r,j in zip(R,J)):
                        shapes.add((R,J))
        pending=shapes.copy()
        trials=0
        for c in product(range(p),repeat=d):
            A=[[sum(h*P[r][j] for h,P in zip(c,powers))%p for j in range(d)] for r in range(d)]
            pending={rs for rs in pending if not modular_minor(A,*rs,p)}
            trials+=1
            if not pending:
                break
        assert not pending
        result.append({"prime":p,"dimension":d,"shapes":len(shapes),
                       "coefficient_tuples_until_all_witnessed":trials})
    return result


def bad_prime_checks():
    rows=[]
    for p in (2,3,5,7,11,13):
        js=[(2*p+1)*h for h in range(1,p+1)]
        def value(c1,c2):
            return c1*prod(c2-(j+1)*c1 for j in js)
        assert all(value(a,b)%p==0 for a,b in product(range(p),repeat=2))
        val=value(1,js[0]+1+p)
        assert val%p==0 and val%(p*p)!=0
        rows.append({"prime":p,"minor_order":p+1,"tested_residue_pairs":p*p,
                     "least_universal_normalized_valuation":1})
    # Actual original rational matrices for the smallest displayed obstruction.
    d=9
    A=matrix(1,d)
    A2=multiply(A,A)
    J,R=(0,3,6),(1,5,8)
    D=diagonal(d,1)
    bound=prod(D[r] for r in R)//prod(D[j] for j in J)
    for c1,c2 in product(range(-5,7),repeat=2):
        F=[[c1*u+c2*v for u,v in zip(r,s)] for r,s in zip(A,A2)]
        assert bound*minor(F,R,J)==c1*(c2-4*c1)*(c2-7*c1)
    sample_gcd=0
    for a in range(4):
        for b in range(4-a):
            sample_gcd=gcd(sample_gcd,a*(b-4*a)*(b-7*a))
    assert sample_gcd==2
    assert bound==1120 and Fraction(1*(5-4)*(5-7),bound)==Fraction(-1,560)
    return {"family":rows,"example":{"rows":R,"columns":J,"lattice_bound":bound,
           "attained_reduced_denominator":560,"simplex_sample_gcd":sample_gcd,
           "pairs_of_integer_coefficients":144}}


def progression_fixed_divisor(u,k,step):
    fixed=1
    for prime in range(2,k+1):
        if any(prime%q==0 for q in range(2,prime)) or step%prime==0:
            continue
        value=factorial(k)
        exponent=0
        while value%prime==0:
            value//=prime
            exponent+=1
        fixed*=prime**min(u,exponent)
    return fixed


def progression_checks():
    cases=0
    for u,k,step,offset in product(range(1,5),range(1,9),range(3,13),(0,1,4)):
        start=2*u+1+offset
        degree=u+k
        g=0
        for a in range(degree+1):
            for b in range(degree+1-a):
                v=a**u*prod(b-(start+j*step)*a for j in range(k))
                g=gcd(g,v)
        assert g==progression_fixed_divisor(u,k,step)
        cases+=1
    J,R=(0,2,4,7,10,13),(1,3,6,9,12,15)
    D=prod(factorial(r)//factorial(j) for r,j in zip(R,J))
    T=matrix(1,16)
    T2=multiply(T,T)
    values=[]
    for a,b in [(a,b) for a in range(7) for b in range(7-a)]+[(26,17)]:
        poly=[[a*entry+b*other for entry,other in zip(row,row2)] for row,row2 in zip(T,T2)]
        determinant=minor(poly,R,J)
        normalized=a*a*prod(b-v*a for v in (5,8,11,14))
        assert D*determinant==normalized
        values.append(normalized)
    g=gcd(*values[:-1])
    assert cases==960 and g==4 and D==179625600
    assert determinant.denominator==D//g==44906400
    return {"simplex_formulas_checked":cases,"example":{"rows":R,"columns":J,
            "simplex_points":len(values)-1,"lattice_bound":D,
            "normalized_fixed_divisor":g,"attaining_coefficients":[26,17],
            "attaining_minor":str(determinant),"reduced_denominator":determinant.denominator}}


def dag_check():
    edges=[
        (0,1,None,Fraction(2,3)),(0,1,2,Fraction(-1,2)),
        (0,2,3,Fraction(5,7)),(0,4,None,Fraction(-2,5)),
        (1,3,2,Fraction(1)),(1,4,3,Fraction(1,6)),
        (2,3,None,Fraction(4,9)),(2,4,2,Fraction(1)),
        (3,4,3,Fraction(-3,4)),(3,5,None,Fraction(2)),
        (4,5,2,Fraction(1,10)),(4,5,None,Fraction(7,11))]
    n,d,M=6,7,6
    D=diagonal(d,M)
    P=[1]*n
    b=[1]*n
    outgoing=[[] for _ in range(n)]
    for i,j,a,c in edges:
        outgoing[i].append((j,a,c))
        b[i]=lcm(b[i],c.denominator)
    for v in reversed(range(n-1)):
        P[v]=P[v+1]*b[v]
    Q=[1]*n
    for v in reversed(range(n-1)):
        for w,label,c in outgoing[v]:
            effective=c*(M//label if label else 1)
            need=effective.denominator*Q[w]//gcd(abs(effective.numerator),Q[w])
            Q[v]=lcm(Q[v],need)
        assert P[v]%Q[v]==0
    paths=[]
    def visit(v,seq,c):
        if v==n-1:
            paths.append((seq,c))
        for w,label,coef in outgoing[v]:
            visit(w,seq+(label,) if label else seq,c*coef)
    visit(0,(),Fraction(1))
    frozen={i:matrix(i,d) for i in (2,3)}
    expected=[[Fraction(0) for _ in range(d)] for _ in range(d)]
    for seq,c in paths:
        prodmat=identity(d)
        for label in seq:
            prodmat=multiply(prodmat,frozen[label])
        for r in range(d):
            for j in range(d):
                expected[r][j]+=c*prodmat[r][j]
    for col in range(d):
        Y=[[0]*d for _ in range(n)]
        Y[-1][col]=D[col]
        for v in reversed(range(n-1)):
            for w,label,c in outgoing[v]:
                wt=c*(M//label if label else 1)*Q[v]/Q[w]
                assert wt.denominator==1
                wt=wt.numerator
                values=Y[w]
                if label:
                    tmp=[0]*d
                    for r in range(1,d):
                        tmp[r]=values[r-1]-(r-1)*(M//label)*tmp[r-1]
                    values=tmp
                Y[v]=[u+wt*a for u,a in zip(Y[v],values)]
        assert all(Fraction(Y[0][r],Q[0]*D[r])==expected[r][col] for r in range(d))
    assert multiply(frozen[2],frozen[3]) != multiply(frozen[3],frozen[2])
    # The (signed) bound here is for stored vertex coefficients in any one source column.
    numer_product=prod(max(1,abs(c.numerator)) for _,_,_,c in edges)
    state_bound=max(Q)*max(D)*(1 << (len(edges)+d))*numer_product
    return {"vertices":n,"expanded_edge_records":len(edges),"source_sink_paths":len(paths),
            "stored_state_magnitude_upper_bound_bits":state_bound.bit_length(),
            "checked_source_entries":d*d,"first_column":[str(row[0]) for row in expected],
            "sharp_vertex_multipliers":Q,"naive_vertex_product":P[0]}


if __name__=="__main__":
    print(json.dumps({"word_and_shifted_minor_checks":word_denominators(),
                      "good_prime_minors":good_prime_checks(),
                      "bad_prime_minors":bad_prime_checks(),"progression_blocks":progression_checks(),
                      "ordered_dag_check":dag_check()},
                     indent=2,sort_keys=True))
