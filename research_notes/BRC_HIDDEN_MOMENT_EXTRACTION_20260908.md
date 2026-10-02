# BRC Hidden Moment Extraction: cubic audit and observer boundary

Status: `RESEARCH NOTE / EXACT DERIVATIONS + SMALL FINITE CERTIFICATE / NO N-ONLY EXTRACTION ESTABLISHED`
Date: `2026-09-08`
Researcher-ID: `EM-HME-0CE4FD / TASK_RESEARCH`
Scope: Direct user-selected arithmetic question; no official task claim, Driver verdict, Foundation promotion, or change to P000 is asserted.
Global read snapshot: `dde41a0cf844b545f7490995264aff6d4980adc0`.
Parent durable frontier: `awdawmip/enterprise-math@c5d6e6ed4aa4c899706e2a895f55733dc2eb3cb8:research_notes/BRC_MULTIPLIER_BOUNDARY_COLLISION_SPECTRUM_20260908.md`.
The additional earlier claim about an `E3 mod 1152` facade was supplied by the user; its underlying implementation was not retrieved or independently revalidated here.

## 1. Result and selected question

The selected research direction is **N-only extraction of a hidden moment**, with cubic central moments as a probe. The present work completes the algebra audit, a natural modular shadow falsification, and a test of local information beyond an even observer. It does not construct an extractor.

Three corrections determine the frontier:

1. For `{0,p,q}`, the correct cubic is `9 M3 = 2 S^3 - 9 N S`, not `2 S^3 - 6 N S`.
2. Every exchange-symmetric polynomial moment at every fixed horizon belongs to `Q[S,N]`. Increasing the degree does not create another algebraically independent hidden coordinate.
3. Cubic residues can distinguish sign branches of `S mod m` that `S^2 mod m` does not distinguish. This is a possible output advantage, not evidence that an N-only observer produces it.

The remaining issue is an explicitly defined N-visible observer that preserves information about the actual branch and has a proved cost. A higher-degree expression alone does not supply that observer.

## 2. Carrier, observer, and actual BRC reuse

Let `p,q` be positive integers, `N=pq`, `S=p+q`, and

`C_K = {(r,s) in Z_{>=0}^2 : (2r+1)(2s+1) <= K}`.

For `K>=1`, retain a branch for every coefficient pair, with multiplicity even when projected coordinates coincide. Set `Y_(r,s)=rp+sq`, `n=|C_K|`, `mu=(sum Y)/n`, and

`M_d(K)=sum_(r,s) (Y_(r,s)-mu)^d`.

These are **sums**, not moments normalized by `1/n`. The formal coefficients depend only on K. Branch exchange `(r,s)<->(s,r)` makes the aggregate symmetric in p,q. A common translation of every boundary is irrelevant for these central moments. Reflection is not irrelevant for odd central moments.

The parent BRC carrier is labeled boundary support, not positive branch mass. For independent numerical validation only, the existing `moment_transition_matrix` in `src/enterprise_math/brc_moment_transfer.py` was executed unchanged: one state, parallel edges of positive weights `1+rp+sq`, and orders 0 through d. Its law is `W^(j)[0,0]=sum_edges weight^j`. Binomial centering recovers the same central moment because the common shift by 1 cancels.

Reuse classification: `REUSE_EXECUTED` for explicit-weight finite moment evaluation. Exact module source agrees between local HEAD and project read snapshot `ef1893382eb1dcfcd773e19882569e9ff072a8ee`; the certificate records the actual file SHA256. This API requires explicit weights. Supplying `rp+sq` uses p,q, so it is **not** an N-only extraction interface. Centered cubic values may be negative; no signed cancellation theorem is inferred from positive BRC mass.

## 3. Complete cubic formula for every K

Define coefficient-domain sums

`R1=sum r=sum s`, `R2=sum r^2=sum s^2`, `R11=sum rs`,

`R3=sum r^3=sum s^3`, `R21=sum r^2 s=sum r s^2`, `t=R1/n`.

The mean is `mu=tS`. Direct binomial expansion yields

`M3 = A(p^3+q^3) + B(p^2q+pq^2)`,

where

`A = R3 - 3 t R2 + 2 R1^3/n^2`,

`B = 3 [R21 - t(R2+2R11) + 2 R1^3/n^2]`.

Therefore

`M3(K) = a_K S^3 + b_K N S`,

`a_K = R3 - 3 R1 R2/n + 2 R1^3/n^2`,

`b_K = 3(R21-R3) + 6 R1(R2-R11)/n`.

This is an identity for all K, not a fit to examples. Its proof is expansion plus exchange symmetry.

For modular questions define the integral target `H_K=n^2 M3(K)`:

`H_K = [n^2 R3 - 3n R1 R2 + 2R1^3] S^3`

`      + [3n^2(R21-R3) + 6nR1(R2-R11)] N S`.

Do not divide by `n^2 mod m` unless it is invertible. When `gcd(n,m)>1`, a residue of `H_K` is a different output contract and can lose information about the rational moment.

| K | n | a_K | b_K | M3(K) |
|---|---:|---:|---:|---|
| 3 | 3 | 2/9 | -1 | `(2/9)S^3-NS` |
| 5 | 5 | 54/25 | -9 | `(54/25)S^3-9NS` |
| 7 | 7 | 432/49 | -36 | `(432/49)S^3-36NS` |
| 9 | 10 | 633/25 | -102 | `(633/25)S^3-102NS` |

K=9 is a cross-check that includes the first mixed point `(1,1)`; it is not a resumed multiplier scan.

## 4. The three-point correction and all-order collapse

For K=3 the deviations are `-S/3`, `(2p-q)/3`, `(2q-p)/3`. Their sum is zero, so their cube sum is three times their product. Hence

`H_3 := 9 M3(3) = S(2p-q)(p-2q) = 2S^3-9NS`.

For p=3,q=5, this gives `M3=-56/9`; the proposed formula would give `304/9`, so the discrepancy is substantive, including the sign.

Let `E3=p^2+q^2+(p-q)^2=2S^2-6N`. Then

`M2(3)=E3/3`,

`M4(3)=M2(3)^2/2=E3^2/18`.

The fourth identity follows for any three centered numbers z1,z2,z3: from their sum being zero, `sum z^4=(sum z^2)^2/2`. Their characteristic polynomial is

`x^3-(M2/2)x-M3/3`.

Consequently, with `M0=3`, `M1=0`, all subsequent centered moments satisfy

`M_d=(M2/2)M_(d-2)+(M3/3)M_(d-3)` for `d>=4`.

At every fixed K, the fundamental theorem of symmetric polynomials gives

`Q[p,q]^(p<->q) = Q[S,N]`.

Because M_d is homogeneous of degree d,

`M_d(K)=sum_(j=0)^floor(d/2) c_(K,d,j) S^(d-2j) N^j`.

An elementary two-variable proof avoids any extra hypothesis: pair a monomial with its swap and factor off `(pq)^min(a,b)`; the remaining power sums obey `P_d=S P_(d-1)-N P_(d-2)`, with `P0=2`, `P1=S`.

Writing `U=S^2`, all even-degree moments belong to `Q[U,N]`, and all odd-degree moments belong to `S Q[U,N]`. In particular,

`H_3^2 = U(2U-9N)^2`.

Thus the cubic probe remains within the same quadratic extension of the even observer algebra. The equation being cubic in S does not imply a stronger algebraic information source. The suggested raw fourth power sum also reduces to `p^4+q^4=U^2-4NU+2N^2`.

For positive factors, exact U already determines S by its positive square root. Conversely, for fixed positive N, `2S^3-9NS` is strictly increasing on the physical domain `S>=2 sqrt(N)` since its derivative is at least `15N`. Exact cubic and exact quadratic targets both identify S on that domain.

This is an algebraic scope result, not a computational lower bound. Different moduli or precisions of the same hidden variable may still add information. In particular, the linear span of second-order energies does not rule out all accumulation strategies for that variable.

Primary reference for the standard invariant-ring theorem: [NPTEL, Lecture 6, Theorem 6.4](https://archive.nptel.ac.in/content/storage2/courses/111101001/modules/lec6/6.3.html). The specialized identities and proofs above are derived in this audit.

## 5. Odd collision sums and the autocorrelation boundary

The proposed complete ordered sum

`sum_(i,j,k) (X_i-X_j)(X_j-X_k)(X_k-X_i)`

vanishes identically: swapping i and k changes the sign; repeated-index terms are zero. Restricting to ordered labels would introduce a different observer whose labeling must be supplied.

Likewise, if `R(h)=sum_t A(t)A(t+h)` is the ordered difference autocorrelation, then `R(h)=R(-h)`, so every odd signed difference moment, including `sum h^3 R(h)`, is zero.

A generic support and its reflection have the same autocorrelation and opposite third central moments. Hence no universal function of autocorrelation alone returns the signed third central moment over arbitrary finite supports. This is a precise observer-loss statement. It is **not** a proof that N plus a full autocorrelation cannot determine the moment on this restricted arithmetic family: the parent note already shows that such a full hidden spectrum determines factors. It also does not preclude nonlinear statistics of an actually accessible richer observer.

The relevant next interface must specify whether original oriented support, a higher joint statistic, or only the already symmetric difference observer is accessible.

## 6. Experiment 2: a natural N-only cubic shadow cancels

For m>=2 and a unit product residue n, consider the completely N-visible local carrier

`F_m(n)={(a,b) in (Z/mZ)^* x (Z/mZ)^* : ab=n}`.

Define the natural complete-branch shadow

`Phi_m(n)=sum_(a,b in F_m(n)) [(a+b)(2a-b)(a-2b)] mod m`.

The involution `(a,b)->(-a,-b)` preserves the carrier and negates every summand. For m>2 it has no fixed unit pair; for m=2 every summand is zero. Therefore

`Phi_m(n)=0 mod m` for every unit n and m>=2.

This is a genuine N-only computable statistic, but it does not reproduce the actual branch's `H_3`. More generally, on odd moduli, any weighting invariant under simultaneous sign reversal cancels in the same way. Breaking that summation symmetry using only n can change the output but cannot make the statistic distinguish two actual inputs with the same n.

There is a stronger local impossibility classification. A function `g_m(ab)` equal to `H_3(a,b)` on **all unit pairs** exists exactly when `m` divides 4:

- Pairs `(1,1)` and `(-1,-1)` have product 1, the same `(a+b)^2=4`, and targets -2 and +2. Equality would require `m|4`.
- For m=2 or 4, direct odd-residue calculation gives `H_3(a,b)=ab+1 mod m` on all unit pairs.

For every m not dividing 4, even the observer `(ab,(a+b)^2) mod m` cannot universally return the cubic target. This theorem is over unit residue pairs. Its extension to an arbitrary restricted prime population is not presumed; the next section supplies an actual distinct-odd-prime example.

## 7. Experiment 3: genuine local distinction, no CRT extraction claim

An exact small semiprime witness at m=5 is:

| p,q | N | S | N mod 5 | S^2 mod 5 | E3 mod 5 | H_3 mod 5 |
|---|---:|---:|---:|---:|---:|---:|
| 3,13 | 39 | 16 | 4 | 1 | 3 | 1 |
| 7,17 | 119 | 24 | 4 | 1 | 3 | 4 |

So an authentic cubic residue would distinguish a branch that this quadratic residue misses. It does not follow that the cubic residue has been obtained, nor that different such observations would be independent.

Correct tests for any proposed observer O(N) are:

1. **Faithfulness:** prove the claimed output equals the declared integral target modulo m on the stated population.
2. **Coarse-observer factorization:** to refute `target mod m = f(O(N))`, find equal O outputs but unequal target residues modulo the same m. Unequal exact moments alone are insufficient: any finite residue output admits collisions of exact values.
3. **Computational input audit:** identify which N-visible operations produced O; supplying p,q, hidden boundaries, or already known raw moment weights is an oracle validation, not extraction.
4. **Accumulation:** only after a faithful extractor exists, ask what information remains after conditioning on the entire existing observation vector. `N mod m` nonconstancy alone is not CRT independence.

If all available observers depend only on `N mod L`, arbitrary deterministic nonlinear postprocessing also depends only on `N mod L`. For several finite moduli, replace L by their least common multiple. This follows by composition and cannot be evaded merely by taking higher powers. It is restricted to the stipulated observers: no impossibility of arbitrary full-N computation is claimed. For a semiprime, its factor pair and S are already functions of the complete integer N; the distinction at issue is efficient computation.

## 8. Validation and continuation

The task-local certificate uses exact Python fractions throughout:

- 7,168 evaluations: K in {3,5,7,9}, degrees 2 through 8, p,q from 1 through 16; polynomial reduction versus direct centered sums.
- 36 independent checks through the unchanged existing BRC moment API, with explicit input weights.
- 256 three-point cases verifying the corrected cubic, factorized form, fourth-moment identity, ordered-triple cancellation, and Newton recurrence through degree 10.
- Complete unit-residue checks for m=2 through 32 verifying the product-only classification and the vanishing complete-branch shadow.
- The two distinct-odd-prime rows above checked exactly.

The algebraic identities and involution arguments supply proofs; the finite checks supply an implementation certificate, not asymptotic or novelty claims.

Reproduction after placing the companion script under `experiments/`:

`python experiments/brc_hidden_moment_extraction_20260908.py --enterprise-root . --output-dir <scratch-directory>`

Expected terminal verdict:

`PASS_EXACT_ALGEBRA_AND_FINITE_CHECKS; NONLY_EXTRACTION_NOT_ESTABLISHED`.

The proposed cubic probe is now sharply specified. The next unresolved mathematical input is an N-visible observer definition with its carrier, operations, preserved branch/orientation information, output contract and bit cost. The supplied `BRC(N)` notation does not specify such an operator; the retrieved parent note explicitly leaves it open. Repeating higher-degree expansions, summing over all local product branches, or starting CRT accumulation cannot supply that missing input.

Priority remains **BRC Hidden Moment Extraction**, focused on that observer question. The verified algebra and negative shadows should be consumed as completed prerequisites.

