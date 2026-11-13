# R758P4 — Eight-step counterexample to area-only future sufficiency in the candidate X6 / S3 transport

Date: 2026-11-13 (Asia/Shanghai). Scientific classification: exact counterexample, algebraic theorem, exhaustive finite theorem. Research scope: an explicitly declared *candidate* axis-involution transport on three selected X6 axes; not a newly admitted native TRIADIC_CLOSURE_E or a V39 based-loop assertion.

## Lineage and fixed inputs

R758P3 [PR #2204], immutable commit `9e010eb25d64205dfc2ea3b94e88602d53f45656`, proved an area-conjugacy criterion for the very specific 720 six-step words in which every one of three axes appears with exactly one positive and one negative step. The present question is whether area alone stays a sufficient observer for **concatenated closed loops**. Scientific reference is the previously frozen `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; current P000 and ACTIVE world constraints are kept unchanged.

Let `e0,e1,e2` denote three selected native directions of the three-dimensional research slice inside native X6. No two-dimensional native plane is posited. A closed word `w` records signed unit steps and path provenance. Define the three signed integer projected-area observations:
```
A_ab(w) = sum_{step j along axis b} x_a(j-1) * delta_x_b(j), a<b
A(w) = (A_01,A_02,A_12)
```
For closed loops rooted at the same Cell, `A(uv)=A(u)+A(v)`.

Fix the *candidate* S3 transport from R758P3: `T_a=s*r^a` for `a=0,1,2`, with `s^2=r^3=e`, `srs=r^(-1)`; signed positive/negative motion along axis a has the same involutive frame increment. Later steps multiply on the left, hence `H(w)=T_last ... T_first`. Set `p(w)=len(w) mod 2` and `q(w)=sum_j (-1)^(j-1)*a_j mod 3`, where positions j begin at 1. Then `H(w)=s^p*r^q` in the declared convention. Every closed unit-step path has even length, so `H(w)=r^q` and `q(uv)=q(u)+q(v) mod 3` for closed loops.

## Theorem 1: exact eight-step failure of area-to-frame conjugacy

Consider two rooted closed words:
```
W0 = (+0,+1,-0,-1, +0,+2,-0,-2)
W2 = (+0,+1,-0,-1, +2,-0,-2,+0)
```
Each is a composition of two four-step spatially closed commutator circuits. Both traverse the same signed total area:
```
A(W0) = A(W2) = (1,1,0).
```
But their alternating axis charges are respectively `q(W0)=0` and `q(W2)=2`. Consequently
```
H(W0)=e,     H(W2)=r^2.
```
The results belong to different S3 conjugacy classes. Thus **no function of the signed area vector alone can recover even the final S3 frame conjugacy class on the family of all closed three-axis paths**. In particular, the R758P3 six-step area-conjugacy conclusion does not extend to this eight-step concatenation family.

*Proof.* Both words have signed displacement zero. Their first four steps are `+0,+1,-0,-1`, of area `A01=1` and alternating charge `q=1`. The last four steps of W0 and W2 both have `A02=1` and all other area components zero, but their axis strings are `0202` and `2020`, of alternating charges 2 and 1 respectively. Since both parts have even length, their q's add modulo 3. This gives `q(W0)=1+2=0` and `q(W2)=1+1=2`. The exact group readout gives the claimed distinct conjugacy classes. QED.

## Theorem 2: full finite classification of a balanced eight-step family

Define `D8` to be all distinct orderings of the multiset
`{+0,+0,-0,-0,+1,-1,+2,-2}`; its size is `8!/(2!*2!)=10,080`. Every member is a closed X6-slice path. The accompanying exact Python verifier enumerates every distinct word, computes integer areas and actual permutation-product frames, and crosschecks the explicit `q` formula.

The enumeration establishes:

| Property | Exact value |
|---|---:|
| Words in D8 | 10,080 |
| Distinct signed-area vectors | 75 |
| Area fibers allowing precisely one final frame | 17 |
| Area fibers allowing precisely two final frames | 44 |
| Area fibers allowing all three final frames | 14 |
| Word counts by H=e, r, r^2 | 3,744; 3,168; 3,168 |
| Frames in the A=(1,1,0) fiber | e:48; r:96; r^2:96 |

The finite covering is exhaustive because `set(permutations(multiset))` covers each word exactly once. A full run of the companion script reproduced all tabulated counts using exact integer arithmetic and S3 permutations.

## Theorem 3: a minimal future-composable frame residual

For the declared observer consisting of signed area plus future frame under arbitrary concatenations of **closed loops**, `(A,q)` is a deterministic sufficient carrier:
```
(A,q)(uv) = (A(u)+A(v), q(u)+q(v) mod 3).
```
Three q states are reachable. They yield distinct present frames `e,r,r^2`, and therefore any exact deterministic future-frame quotient must distinguish all three. Hence q is a minimal three-state frame register on the closed-loop monoid.

Even conditional on one specific eight-step area vector `A=(1,1,0)`, all three frame states occur; consequently a *uniform fixed-width* repair code for this D8 observer needs at least `ceil(log2(3))=2` bits in the worst fiber. A 2-bit encoding of `q in {0,1,2}` attains that lower bound. This is a scoped strengthening of R758P3's conditional 1-bit repair on its original six-step, once-per-signed-axis domain.

The q-register does not replace the path's spatial provenance or every native joint observer: it is exactly sufficient for the declared final frame and concatenations of closed words. The pair `(A,q)` preserves the declared signed-area and frame readings in this candidate model.

## Verification status and recovery

Companion files contain reproducible standard-library Python verification and JSON evidence. Exact domain: D8; full symbolic argument for the two words and the q-monoid law. No floating-point operations, randomness, or extrapolation beyond the specified model.

Next discriminating step: Find a Source-admitted TRIADIC_CLOSURE_E Cell/Link/Port incidence and the authorized V39 increment for its actual update. Then test whether its legal closed-loop output admits the same frame monoid quotient, or derive an alternate minimal residual on the admitted event domain. Preserve P000 arity and the three-dimensional slice's full coordinate meaning.
