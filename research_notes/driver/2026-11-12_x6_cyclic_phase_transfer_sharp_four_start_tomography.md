# X6 / Weighted-BRC C6 — four consecutive phase origins suffice, and three do not

Status: DRIVER_MATHEMATICAL_AUDIT / EXACT_SCOPED_THEOREM / NOT_NATIVE_RESULT_ADMISSION
Date: 2026-11-12 (+08)
Parent: RS-X6-NATIVE-ROTATION-DYNAMICS / PO-X6-UPPER-STRUCTURE-20260906
Context: shared, non-clean-blind X6 review context. Original C6/C12 signed Cell and Path-formal sources retain their authorship; this note is a new scoped Driver extension of the existing phase-weight transfer proof. It makes no native research CLAIM, Result admission, or physical rotation assertion.

## 1. Problem and exact model

In the previously published six-phase candidate Weighted-BRC model with no adjacent INNER choices, let `t_j > 0` be the INNER phase activity (OUTER activity 1), and define

```text
T(t) = [[1,t],[1,0]]
P_j = T(t_j)T(t_{j+1})...T(t_{j+5}),  phase indices modulo 6.
```

The complete labelled two-branch start/end matrix `P_j` is observed for **consecutive registered start phases** `j=1,...,k`, each with the same actual phase order and start O/I boundary convention. This is not the weaker trace/open aggregate observation.

**Sharp tomography theorem.** Among positive rational (indeed positive real) phase activities, four consecutive registered whole-turn transfer matrices `P_1,P_2,P_3,P_4` determine all six ordered activities `(t_1,...,t_6)` uniquely by explicit algebra. Three consecutive registered matrices are insufficient, even with all four matrix entries and arbitrarily many repeated-turn observations for those same three origins.

More generally, for any periodic `n>=4` with the identical `T(t)` transition law, **exactly `n-2` consecutive phase-origin matrices** are sufficient and necessary for uniform injective recovery over positive activities. For `n<=3`, one full-origin matrix already suffices. This is a minimum **number of complete consecutive-origin matrices**, not an information-bit bound or a bound for arbitrary other observer designs.

## 2. Constructive inverse: four origins

Each `T(t)` is invertible for `t>0`, and all entries of a six-factor `P_j` are strictly positive. The cyclic relation

```text
P_j T(t_j) = T(t_j) P_{j+1}
```

gives, from the (2,2) entry,

```text
t_j = (P_{j+1})[1,2] / (P_j)[2,1]     (j=1,2,3).
```

Thus four measured matrices yield `t_1,t_2,t_3`. Strip their known right-hand product from the last matrix:

```text
R = P_4 [T(t_1)T(t_2)T(t_3)]^(-1)
  = T(t_4)T(t_5)T(t_6)
  = [[A,B],[C,D]].
```

The three-factor identity is

```text
T(a)T(b)T(c) = [[1+a+b, c(1+a)],
                [1+b,       c     ]].
```

Consequently,

```text
t_4 = B/D - 1,    t_5 = C - 1,    t_6 = D.
```

Here `D=t_6>0`. All six activities are therefore explicitly determined. This also supplies a consistency certificate: every measured positive-law matrix satisfies `A=B/D+C-1` after stripping its known prefix.

For general `n>=4`, `P_1,...,P_{n-2}` recover `t_1,...,t_{n-3}` by the same cyclic relation; stripping that known right-hand prefix from `P_{n-2}` leaves precisely three factors, reconstructed with the formula above. For `n=1,2,3`, direct multiplication of one, two, or three `T` factors is injective over positive `t` (for two factors the matrix is `[[1+a,b],[1,b]]`).

## 3. Sharpness: explicit three-origin indistinguishability

From the previously established exact four-factor collision,

```text
T(1/2)T(1/2)T(2)T(2) = [[5,4],[7/2,3]]
                        = T(1)T(2)T(1/2)T(1),
```

take the two inequivalent six-phase laws

```text
U = (1/2,1/2,1/2,1/2,2,2)
V = (1/2,1/2,1,2,1/2,1).
```

They have the same first two activities and the same full-period product. Their cyclic starting transfers agree for `j=1,2,3`, exactly:

```text
P_1(U)=P_1(V)=[[37/4,15/2],[27/4,11/2]]
P_2(U)=P_2(V)=[[49/4,27/8],[9,5/2]]
P_3(U)=P_3(V)=[[23/2,9/2],[33/4,13/4]].
```

But the fourth matrices differ:

```text
P_4(U)=[[23/2,33/8],[9,13/4]]
P_4(V)=[[23/2,33/4],[9/2,13/4]].
```

Any repeated-turn readouts `P_j^m` for origins `j<=3`, all boundary states and any integer `m>=1`, agree under `U,V`. Thus three consecutive origins are not enough. The same collision, preceded by `n-4` identical positive factors, yields a collision in `P_1,...,P_{n-3}` for every `n>=4`: equal full products plus equal first `n-4` phase factors imply equal corresponding successive cyclic conjugates. It proves the claimed lower bound `n-2` for all `n>=4`.

## 4. Exact independent arithmetic check

The preceding identities constitute an algebraic proof. As additional validation, the following rational-arithmetic procedure reconstructs the sequence from the proposed minimal measurements; one can test arbitrary positive rational input tuples.

```python
from fractions import Fraction as F

I=((F(1),F(0)),(F(0),F(1)))
def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                 for j in range(2)) for i in range(2))
def T(x): return ((F(1),x),(F(1),F(0)))
def product(v):
    r=I
    for x in v: r=mul(r,T(x))
    return r
def inverse(M):
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return ((M[1][1]/det,-M[0][1]/det),
            (-M[1][0]/det,M[0][0]/det))
def phase_origin(v,j): return product(v[j:]+v[:j])
def recover(v):
    n=len(v)
    assert n>=4
    obs=[phase_origin(v,j) for j in range(n-2)]
    prefix=[obs[j+1][0][1]/obs[j][1][0] for j in range(n-3)]
    R=mul(obs[-1],inverse(product(prefix)))
    return prefix+[R[0][1]/R[1][1]-1,R[1][0]-1,R[1][1]]

U=[F(1,2),F(1,2),F(1,2),F(1,2),F(2),F(2)]
V=[F(1,2),F(1,2),F(1),F(2),F(1,2),F(1)]
assert U!=V
assert all(phase_origin(U,j)==phase_origin(V,j) for j in range(3))
assert phase_origin(U,3)!=phase_origin(V,3)
assert recover(U)==U and recover(V)==V
```

Using exact rational arithmetic, independently checked 30 positive-rational samples for each `n=4,...,10` (210 inputs), all reconstructed exactly. Finite tests supplement the universal proof.

## 5. Scientific interpretation and provenance

This result improves the earlier six-origin cyclic tomography sufficiency theorem to a **sharp four-origin criterion** in the six-phase candidate model. It identifies a concrete memory/observation tradeoff for future signed Cell/path successor design: complete whole-period boundary transfer from only three consecutive phase origins can collapse inequivalent internal branch laws, whereas retaining a fourth registered phase origin recovers their individual activities.

It does not equate this NB transfer law with a full native X6 physical rotation. Relative observer quotients, phase clock, branch provenance, frame, and future composition are typed separately under current P000 and the joint-relation preservation requirement.

Exact source ancestry:
- `research_notes/driver/2026-11-12_x6_weighted_brc_full_period_transfer_matrix_nonidentifiability.md`, GitHub commit `0d5e4cacb6b9d79f1977b83f88f23b192ae58a2f`, blob `ffa02e6ea275c0331ac672308f2f718c11e9be12`.
- `research_notes/driver/2026-11-12_x6_phase_weighted_brc_c6_loop_identifiability.md` and `research_notes/driver/2026-11-12_x6_weighted_brc_c6_loop_and_star_atlas_invariants.md`.
- Original X6 signed spatial and C6/C12 microtrace materials at frozen Task input refs and their recorded authors. Shared-context Driver contribution; decisive independent formal review remains a separate native step.

Next useful unit: define which registered boundary states and phase-origin readouts are physically observable in a native X6 successor, then test whether the four-origin candidate tomography survives branch-level BRC composition with a nontrivial incoming phase and time state.
