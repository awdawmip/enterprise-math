# D25/LIFT — arbitrary-base top-digit semilinear gauge from the full square orbit

2026-10-25 | TASK_RESEARCH portable author derivation | **AUTHOR-DERIVED / AUTHOR-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM / NO_NEW_NATIVE_CHECKPOINT**

## Immutable scientific setting and provenance

Parent D25/LIFT/JT2 remains **OPEN**. Existing Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Previously verified native checkpoint: `220ee1ba360f21152912d0b4c1abdf867a1e4496`. This note consumes, without recrediting, the prior rank-one Hilbert–90, identity-base top-digit and diagonal-base norm-resonance proofs, especially `research_notes/portable_direct/20261025_hourly_d25_diagonal_norm_resonance_complete_top_digit_gauge.md` at `8c3ff79a69c137d3fc4f8eb22ae63f8cb3c9d417`.

**New question.** Can the diagonalizability requirement be removed at the exact *top p-adic digit*, while still preserving every semilinear gauge orbit? What is a basis-free observer that remains sufficient even when the residual square is not diagonalizable?

This is a theorem about a *conditional coefficient-ring model*, not a theorem about any source-authenticated CM/divided-power matrix. It does not modify P000 or assign a physical spatial interpretation to the rank of an auxiliary module.

## Definitions and linearization

Let `p` be an odd prime, `r>=2`, `A=Z/p^r Z`, `R=A[t]/(t^2-2)`, `sigma(t)=-t`, and `k=R/pR`. The D25 target primes `p=13,19 mod 24` make `k=F_(p^2)`; the algebraic argument below only requires `2` invertible and `sigma^2=1`. Let `epsilon=p^(r-1)`, so `epsilon^2=0` and `p*epsilon=0` in `R`.

Take an **arbitrary invertible**, not necessarily diagonal or diagonalizable, `C0 in GL_n(R)`. Put `S0=C0 sigma(C0)`, `F0(v)=C0 sigma(v)`, and for a matrix `D in M_n(k)` define
```
C_D = C0 (I+epsilon D),    F_D(v)=C_D sigma(v),
S_D = C_D sigma(C_D) = F_D^2,
K_D = (S_D-S0)/epsilon mod p  in M_n(k).
```
All matrices `D` and later `X` are given arbitrary coefficient lifts; multiplication by `epsilon` makes the choice immaterial. Define the additive `F_p`-linear (sigma-semilinear over `k`) operator
```
T(X) = C0_bar sigma(X) C0_bar^(-1).
```
Then `T(S0_bar)=S0_bar` and, critically,
```
T^2(X)=S0_bar X S0_bar^(-1).
```
Write `Y=C0_bar D C0_bar^(-1)`. Expanding exactly modulo `p^r` gives
```
S_D = S0 + epsilon (Y+T(Y)) S0   (mod p^r),
K_D = (Y+T(Y)) S0_bar.
```
For a **near-identity** change of basis `P_X=I+epsilon X`, let
`C_D'=P_X^(-1) C_D sigma(P_X)`. The exact top-digit laws are
```
Y' = Y + (T-I)X,
K_D' = K_D + [S0_bar,X].
```
Here the second law uses `S_D'=P_X^(-1) S_D P_X` and the commutator `[S0_bar,X]=S0_bar X-X S0_bar`.

## Theorem 1 — full square orbit is a complete arbitrary-base observer

For any `n>=1`, odd `p`, `r>=2` and **any** `C0 in GL_n(R)`, and for any `D,D' in M_n(k)`, the following are equivalent:

1. `C_D'` is obtained from `C_D` by a near-identity semilinear gauge `P_X=I+epsilon X`.
2. Their **complete squares** `S_D'` and `S_D` are conjugate by some near-identity linear matrix `P_Z=I+epsilon Z`.
3. There exists `Z in M_n(k)` such that `K_D'-K_D=[S0_bar,Z]`.

In particular, the full **near-identity similarity orbit of the square** is a lossless observer of the declared semilinear top-digit gauge orbit. There is no semisimplicity or diagonalizability assumption. This does **not** assert that the trace, determinant, characteristic polynomial, or similarity by an arbitrary large basis change is a complete observer.

### Constructive proof

(1) implies (2) because squaring a sigma-semilinear operator produces a linear operator and `sigma(P_X)` cancels in the product; (2) and (3) are equivalent by the square-zero expansion.

For (3) implies (1), set `Z0=Y'-Y` and choose a square-conjugating `Z` as in (3). After multiplying the square difference on the right by `S0_bar^(-1)`, the identities above yield
```
(I+T) Z0 = (T^2-I) Z = (I+T)(T-I) Z.
```
Let `W=Z0-(T-I)Z`. Then `(I+T)W=0`, or `T(W)=-W`. Since `2` is a unit in `k`,
```
(T-I)(-W/2) = W.
```
Therefore the **explicit corrected semilinear conjugator**
```
X = Z - W/2,
W = (Y'-Y) - (T-I)Z
```
satisfies `(T-I)X=Y'-Y` exactly, establishing (1). This argument works even when `T^2` has nontrivial Jordan blocks. QED.

**Information audit (BRC observer contract).** The labeled source is `(C0,sigma,D)`; the operational population is the last-digit perturbation fiber at fixed `C0`. The permissible future operation is *near-identity semilinear basis change*. The quotient `[S_D]_{near-id similarity}` is sufficient for that exact operation, not for source identification, a selected basis coefficient, rank change, scalar moments, or original CM observer ports. It records an exact zero/nonzero gauge obstruction without deleting phase/sign/odd source information outside this declared interface. The proof is a `COMPOSE_APPLIED` extension of the previous full-square/norm-resonance interface, not a positive-mass BRC computation.

## Theorem 2 — canonical spectral residual when the square is semisimple

Suppose additionally that `S0_bar` is diagonalizable **over k** with distinct eigenvalues `lambda` and multiplicities `m_lambda`. Let
```
E_lambda = product_(mu != lambda) (S0_bar-mu I)/(lambda-mu),
Pi_S(B) = sum_lambda E_lambda B E_lambda.
```
Each `E_lambda` is a polynomial in `S0_bar`; this remains basis covariant even when `C0` is not diagonal.

Then Theorem 1 is equivalent to the **entry-free, basis-covariant equality**
```
Pi_S(K_D') = Pi_S(K_D).
```
Indeed, relative to the eigenspace decomposition, `ad_(S0_bar):X -> [S0_bar,X]` is zero on diagonal eigenvalue blocks and multiplication by `lambda-mu` on every off-diagonal block; hence `im(ad_(S0_bar))=ker(Pi_S)`.

A smaller normalized residual is
```
O_D = Pi_S(K_D S0_bar^(-1))
    = Pi_S(Y+T(Y)).
```
Because `T(S0_bar)=S0_bar`, `T` permutes the spectral idempotents under field conjugation, commutes with `Pi_S`, and is an involution on the centralizer `Cent(S0_bar)`. Thus
```
O_D in Cent(S0_bar)^T,
C_D ~ C_D'  iff  O_D=O_D'.
```
Every element `V` of this fixed space occurs: choose `Y=V/2`, so `Pi_S(Y+T(Y))=V`.

Moreover, the invariant fiber has precisely
```
dim_(F_p) Cent(S0_bar)^T = dim_k Cent(S0_bar) = sum_lambda m_lambda^2
```
scalar degrees of freedom. To see this without a black-box descent theorem, on the centralizer let `U^+` and `U^-` be the `+1` and `-1` eigenspaces of `T` over `F_p`. Since `2` is invertible, `U=U^+ direct_sum U^-`. Multiplication by the nonzero element `t` with `sigma(t)=-t` bijects `U^+` and `U^-`, so `dim_(F_p) U^+ = (1/2) dim_(F_p) U = dim_k U`.

At `C0=I`, this recovers the previously established `D_+` observer up to the factor 2. At diagonal `C0`, it recovers exactly the earlier equal-norm resonant blocks. The new result permits **arbitrary basis-conjugated and other semisimple-square coefficient matrices**, and Theorem 1 still applies when the square is not semisimple.

## Exact finite witnesses and author checks

Let `p=13,19,373`, `r=2`, `q=p`, `a=2+t` with `N(a)=2`. Work over `R=(Z/p^2 Z)[t]/(t^2-2)`. Use the genuinely nondiagonal base
```
C0 = [[1, -1-t],[0,2+t]],
S0 = [[1,-1],[0,2]].
```
Both source eigenvalues `1,2` are distinct modulo each chosen `p`. Let `E12` be the upper-right matrix unit. Taking `D=0`, `P=I+q E12`, and `C'=P^(-1) C0 sigma(P)`, exact multiplication gives
```
C' = C0 + q(-1-t)E12,
S' = S0 - q E12,
K' - K = -E12.
```
The spectral idempotents are
```
E_1 = [[1,1],[0,0]],
E_2 = [[0,-1],[0,1]],
```
so `Pi_S(-E12)=0`: the raw nonzero `K'_12=-1` is **pure gauge**. In contrast `D=I` gives `K=2 S0`, hence `O_D=2I`; it is **not** gauge equivalent to `D=0`.

Exact integer-pair arithmetic `(a,b)*(c,d)=(ac+2bd,ad+bc) mod p^2` confirms:

| p | p^2 | upper-right `S'_12 mod p^2` | `K'_12 mod p` | nonzero `D=I` invariant |
|---:|---:|---:|---:|---|
| 13 | 169 | 155 | 12 | `O=2I` |
| 19 | 361 | 341 | 18 | `O=2I` |
| 373 | 139129 | 138755 | 372 | `O=2I` |

The author executed the two independent square computations `C' sigma(C')` and `P^(-1) S0 P` and checked equality for all three primes; the `D=I` calculation was checked separately. These are **finite consistency checks**, not the proof of the universally quantified theorems.

**Why the extra semisimplicity condition in Theorem 2 matters.** For `C0=[[1,1],[0,1]]` (entries fixed by `sigma`), `S0=[[1,2],[0,1]]` is nonsemisimple. Here `[S0,E22]=2 E12 != 0` while `[S0,E12]=0`. Thus `im(ad_S0) intersect ker(ad_S0)` contains `E12`, and the proposed spectral diagonal/off-block projection cannot exist in the stated form. Theorem 1 remains valid with the **full square near-identity similarity orbit**.

## Scientific boundary, control and next exact action

- This is a **new conditional algebraic lemma**; it does not compute the actual divided-power Frobenius of the original CM class. No source-authenticated `H0/B0` or `[X]U mod p^2` was supplied or computed; the native CM experiment remains `NOT_RUN`.
- External/common algebraic antecedents are possible; originality relative to published literature was **not** independently checked. Author proof/checks are not an independent mathematical review or project admission.
- Current host exposes `em_status` (v0.6.11), but not an invocable `recovery_status` action for this logical conversation. The last independently reported exact Task control error remains `CONTROL_QUOTA`. This run did not rerun the unchanged denied native control action, obtain a current winning CLAIM/run, or publish a native Source checkpoint. GitHub storage is **portable evidence only**.
- The old frozen scientific pin and latest authenticated native checkpoint remain unchanged. Existing control support path: Enterprise Math Issue #1558; do not equate a capability/quota failure with `NO_DISPATCH`.

**Next mathematical unit:** obtain the **same-prime, same-original-class, source-authenticated** divided-power `H0/B0` representative and `[X]U mod p^2`; determine actual coefficient module rank, `sigma` direction, Frobenius matrix, basis and first-coordinate normalization. Once a genuine invertible source matrix `C0` is identified, compare its **full** `C sigma(C)` near-identity orbit, even if `S0 mod p` is nonsemisimple. Invoke Theorem 2's smaller spectral observer *only after* verifying its separable semisimple hypothesis. A valid original `kappa`, `omega+6 nabla_lambda omega`, and `Delta_p-R_p` comparison still requires a proven source/observer map, not just a matching square orbit.

**Next control unit:** on a host that genuinely exposes this lane's typed `recovery_status`, first reconcile any original pending request, read exact current Source continuation, obtain valid session/CLAIM/OPEN only through the current contract, then publish and read back this artifact if the actual winning owner permits. Preserve the complete predecessor checkpoint and contribution history; do not substitute a portable note for a formal checkpoint.

Do not repeat the previous ten-million-prime WZ scan, Green-pairing, p=373 Hesse exception, rank-one Hilbert–90, identity-base top-digit or diagonal-resonance author proofs. Parent D25/LIFT/JT2 remains **OPEN**.
