import itertools, random, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'src'/'enterprise_math'
sys.path.insert(0,str(SOURCE if SOURCE.exists() else Path(__file__).resolve().parent))
import heartbeat_residual_holonomy as h

def block6(B):
    M=[list(row) for row in h.identity(6)]
    for i in range(2):
        for j in range(2):
            M[i][j]=B[i][j]
    return tuple(tuple(row) for row in M)

def test_phase_intertwining_random():
    rng=random.Random(20260920)
    checked=0
    for _ in range(60):
        # diagonal-permutation style integer matrices, all nonsingular
        steps=[]
        for t in range(3):
            perm=list(range(6)); rng.shuffle(perm)
            scales=[rng.choice((-3,-2,-1,1,2,3)) for _ in range(6)]
            A=[[0]*6 for _ in range(6)]
            for i,j in enumerate(perm): A[i][j]=scales[i]
            steps.append(tuple(tuple(r) for r in A))
        for t,A in enumerate(steps):
            Mt=h.monodromy(steps,start=t)
            Mnext=h.monodromy(steps,start=t+1)
            assert h.matmul(Mnext,A)==h.matmul(A,Mt)
            assert abs(h.determinant(Mt))==abs(h.determinant(Mnext))
            checked+=1
    return checked

def test_phase_carry_example():
    A0=block6(((1,0),(0,-2)))
    A1=block6(((-2,1),(2,-2)))
    p=h.phase_residual_profiles((A0,A1))
    assert p[0].invariant_factors==(1,1,1,1,2,2)
    assert p[1].invariant_factors==(1,1,1,1,1,4)
    assert p[0].cardinality==p[1].cardinality==4
    assert p[0].exponent==2 and p[1].exponent==4
    assert h.torsion_killed_count(p[0].invariant_factors,2)==4
    assert h.torsion_killed_count(p[1].invariant_factors,2)==2
    return p

def test_radix_staircase():
    cases=0
    for b in (2,3,5,7):
        A=h.cyclic_radix_heartbeat(b)
        assert h.matpow(A,6)==tuple(tuple(b if i==j else 0 for j in range(6)) for i in range(6))
        for k in range(1,25):
            actual=h.smith_invariant_factors(h.matpow(A,k))
            expected=h.radix_staircase_factors(b,k)
            assert actual==expected,(b,k,actual,expected)
            assert h.residual_branch_count(h.matpow(A,k))==b**k
            cases+=1
    return cases

def test_residual_cardinality_composition():
    rng=random.Random(92026)
    checked=0
    for _ in range(200):
        # block-diagonal 2x2 nonzero determinant plus identity4
        while True:
            a=tuple(tuple(rng.randint(-2,2) for _ in range(2)) for __ in range(2))
            if h.determinant(a): break
        while True:
            b=tuple(tuple(rng.randint(-2,2) for _ in range(2)) for __ in range(2))
            if h.determinant(b): break
        A=block6(a); B=block6(b); BA=h.matmul(B,A)
        assert h.residual_branch_count(BA)==h.residual_branch_count(A)*h.residual_branch_count(B)
        checked+=1
    return checked

def test_bounded_survey():
    vals=range(-2,3); mats=[]
    for e in itertools.product(vals,repeat=4):
        M=(e[:2],e[2:])
        if abs(h.determinant(M))==2: mats.append(M)
    diff=0
    for A in mats:
        for B in mats:
            if h.smith_invariant_factors(h.matmul(A,B))!=h.smith_invariant_factors(h.matmul(B,A)):
                diff+=1
    assert len(mats)==184 and len(mats)**2==33856 and diff==15488
    return len(mats),diff


def test_invalid_boundaries():
    try:
        h.matpow(h.identity(2), -1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative exponent was accepted")
    for args in [((2,3,5,7,11,13),4,-1), ((2,3,5,7,11,13),4,1)]:
        factors, prime, beats = args
        try:
            h.cyclic_valuation_depths(factors, prime, beats)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid valuation arguments were accepted")
    return 3


def test_weighted_valuation_balance():
    rng=random.Random(20260921)
    checked=0
    for _ in range(80):
        factors=tuple(rng.randint(1,6) for _ in range(6))
        A=h.cyclic_weighted_heartbeat(factors)
        B=1
        for value in factors:
            B*=value
        assert h.matpow(A,6)==tuple(tuple(B if i==j else 0 for j in range(6)) for i in range(6))
        for k in range(1,19):
            smith=h.smith_invariant_factors(h.matpow(A,k))
            for prime in (2,3,5):
                actual=tuple(sorted(h.prime_valuation(d,prime) for d in smith))
                expected=h.cyclic_valuation_depths(factors,prime,k)
                assert actual==expected,(factors,k,prime,smith,actual,expected)
                checked+=1
    return checked


def test_monomial_valuation_drift_criterion():
    rng=random.Random(20260922)
    comparisons=0
    classifications=0
    for _ in range(40):
        perm=list(range(6)); rng.shuffle(perm)
        weights=[rng.randint(1,12) for _ in range(6)]
        M=[[0]*6 for _ in range(6)]
        for j,i in enumerate(perm):
            M[i][j]=weights[j]
        M=tuple(tuple(row) for row in M)
        for prime in (2,3,5):
            for k in range(1,13):
                smith=h.smith_invariant_factors(h.matpow(M,k))
                actual=tuple(sorted(h.prime_valuation(d,prime) for d in smith))
                expected=h.monomial_valuation_depths(M,prime,k)
                assert actual==expected,(perm,weights,prime,k,actual,expected)
                comparisons+=1
            data=h.monomial_cycle_valuation_data(M,prime)
            balanced=h.monomial_valuation_balance(M,prime)
            direct=all(data[i][1]*data[0][2]==data[0][1]*data[i][2] for i in range(1,len(data)))
            assert balanced==direct
            classifications+=1
    M=h.cyclic_weighted_heartbeat((2,3,4,5,6,7))
    for prime in (2,3,5,7):
        assert h.monomial_valuation_balance(M,prime)
        spreads=[max(h.monomial_valuation_depths(M,prime,k))-min(h.monomial_valuation_depths(M,prime,k)) for k in range(121)]
        assert max(spreads)==max(spreads[:6])
    D=((2,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),(0,0,0,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
    assert not h.monomial_valuation_balance(D,2)
    assert h.monomial_valuation_depths(D,2,20)==(0,0,0,0,0,20)
    return comparisons,classifications


def test_periodic_monomial_phase_balance():
    rng=random.Random(20260923)
    checked=0
    for _ in range(40):
        steps=[]
        for _beat in range(3):
            perm=list(range(6)); rng.shuffle(perm)
            weights=[rng.randint(1,8) for _ in range(6)]
            A=[[0]*6 for _ in range(6)]
            for j,i in enumerate(perm):
                A[i][j]=weights[j]
            steps.append(tuple(tuple(row) for row in A))
        for prime in (2,3,5):
            verdict=h.periodic_monomial_valuation_balance(steps,prime)
            phase_verdicts=tuple(h.monomial_valuation_balance(h.monodromy(steps,start=t),prime) for t in range(3))
            assert phase_verdicts==(verdict,)*3
            checked+=1
    return checked



def _blockdiag3(two):
    out=[[0]*6 for _ in range(6)]
    for block in range(3):
        for i in range(2):
            for j in range(2):
                out[2*block+i][2*block+j]=two[i][j]
    return tuple(tuple(row) for row in out)


def _poly_eval_zero(coefficients, matrix):
    n=len(matrix)
    power=h.identity(n)
    out=[[0]*n for _ in range(n)]
    for coefficient in coefficients:
        for i in range(n):
            for j in range(n):
                out[i][j]+=coefficient*power[i][j]
        power=h.matmul(power,matrix)
    return tuple(tuple(row) for row in out)


def test_general_newton_carry_spectrum():
    rng=random.Random(20260924)
    cayley=0
    for n in range(1,5):
        for _ in range(40):
            M=tuple(tuple(rng.randint(-3,3) for _ in range(n)) for __ in range(n))
            coeff=h.characteristic_coefficients(M)
            assert _poly_eval_zero(coeff,M)==tuple(tuple(0 for _ in range(n)) for __ in range(n))
            assert coeff[0]==((-1)**n)*h.determinant(M)
            cayley+=1

    A2=((0,2),(1,0))
    B2=((1,1),(1,-1))
    P2=h.matmul(B2,A2)
    C2=((0,-2),(1,6))
    A6=_blockdiag3(A2); B6=_blockdiag3(B2); P6=h.matmul(B6,A6); C6=_blockdiag3(C2)
    half=(Fraction(1,2),)*6
    assert h.carry_slope_spectrum(A6,2)==half
    assert h.carry_slope_spectrum(B6,2)==half
    assert h.carry_slope_spectrum(P6,2)==(Fraction(0),)*3+(Fraction(2),)*3
    assert h.carry_slope_spectrum(C6,2)==half
    assert h.carry_balanced(A6,2) and h.carry_balanced(B6,2) and h.carry_balanced(C6,2)
    assert not h.carry_balanced(P6,2)
    for n in range(1,9):
        assert h.smith_p_depths(P6,2,n)==(0,0,0,2*n,2*n,2*n)
    return cayley,8


def test_general_phase_carry_slope_invariance():
    rng=random.Random(20260925)
    checked=0
    for _ in range(60):
        steps=[]
        for _beat in range(3):
            while True:
                B=tuple(tuple(rng.randint(-3,3) for _ in range(2)) for __ in range(2))
                if h.determinant(B):
                    break
            M=[list(row) for row in h.identity(6)]
            for i in range(2):
                for j in range(2):
                    M[i][j]=B[i][j]
            steps.append(tuple(tuple(row) for row in M))
        spectra=h.phase_carry_spectra(steps,2)
        assert spectra==(spectra[0],)*3
        checked+=3
    return checked



def test_eventual_carry_controller_examples():
    A=h.cyclic_radix_heartbeat(2)
    trace=h.smith_increment_trace(A,1,12)
    assert trace[:6]==trace[6:]
    assert all(__import__('math').prod(row)==2 for row in trace)

    A2=((0,2),(1,0)); B2=((1,1),(1,-1))
    P2=h.matmul(B2,A2)
    P6=_blockdiag3(P2)
    for n in range(1,7):
        assert h.smith_factor_ratio(P6,n)==(1,1,1,4,4,4)
    return 18


if __name__=='__main__':
    results={
      'phase_intertwining':test_phase_intertwining_random(),
      'phase_carry_example':str(test_phase_carry_example()),
      'radix_staircase_cases':test_radix_staircase(),
      'composition_cardinality':test_residual_cardinality_composition(),
      'bounded_survey':test_bounded_survey(),
      'weighted_valuation_balance':test_weighted_valuation_balance(),
      'invalid_boundaries':test_invalid_boundaries(),
      'monomial_valuation_drift':test_monomial_valuation_drift_criterion(),
      'periodic_monomial_phase_balance':test_periodic_monomial_phase_balance(),
      'general_newton_carry_spectrum':test_general_newton_carry_spectrum(),
      'general_phase_carry_slope_invariance':test_general_phase_carry_slope_invariance(),
      'eventual_carry_controller_examples':test_eventual_carry_controller_examples(),
    }
    print('PASS',results)
