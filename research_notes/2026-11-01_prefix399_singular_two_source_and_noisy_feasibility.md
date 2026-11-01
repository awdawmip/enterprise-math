# PREFIX-399 — Singular two-source fiber and exact joint feasibility in the auxiliary five-Port model

Date: 2026-11-01 (Asia/Shanghai). **AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING**. External static complex three-amplitude inverse problem only; neither native P000 X6 nor the three-dimensional slice nor typed BRC dynamics is proved.

## Frozen authority and scientific inputs
GLOBAL_KNOWLEDGE_V1 canonical `main@2dde259b7039962a5f02669e83f7ffc38081e01f` (bootstrap, operating manual, ACTIVE worldview, math policy, BRC method, TASK_RESEARCH startup, P000 projection; its canonical original blob matches `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`). Enterprise Math scientific input `main@42da097851a02b96f8ff2018f5c28096eec13866` (AGENTS, native P000, joint-observer preservation, Heartbeat X6 and portable research protocol, PREFIX-395/396/398). Contributor GitHub account: `awdawmip`. Native v0.6.11: `research_authority_granted=false`, `CODE_REVIEW_REQUIRED`, `UPSTREAM_CODE_REVIEW_REQUIRED`, five of five active jobs; Owner inventory fails with `CONTROL_QUOTA`. No claim of native Task owner, CLAIM, Result, review, or admission.

## Theorem A — necessary and sufficient *arbitrary rational noisy six-reading feasibility* specification

Let
```
A = [[4,4,0],[0,-4,4],[-5+3i,0,-3+i],
     [-2-2i,4+4i,2+2i],[-2,0,5+2i]]
```
and `A3` its first three rows; `det(A3)=-32+32i`. Then `B=A*A3^{-1}` has rows `(1,0,0),(0,1,0),(0,0,1)`, followed by
```
B4=(5/2+9i/2,3/2+7i/2,4i)
B5=(11/4+15i/8,11/4+15i/8,5/4+9i/4).
```
For arbitrary rational measured intensity centers `J1..J5`, nonnegative rational independent radii `xi1..xi5`, rational coherent reading `q` with nonnegative rational error `eta`, an actual source `Y in C^3` with `I1>0` satisfies the five intensity bands and `|Cu-q|<=eta`, where `Cu=|1+(A3Y)_2/(A3Y)_1|²`, **if and only if** the following *five real-variable degree-two polynomial system* is feasible:
```
h>0; W=(h,x+i*y,c+i*d)
for j=1..5: Jj-xij <= Pj(h,x,y,c,d) <= Jj+xij,
             Pj=|Bj W|²
(q-eta)*h² <= (h+x)²+y² <= (q+eta)*h².
```
Proof: any source is mapped to `W=A3Y`; its nonzero first Port permits a unique positive-real `h` gauge. All five intensities and the coherent ratio are unchanged. Conversely any feasible five-tuple gives the *explicit* complex lift `Y=A3^{-1}W`, reproducing all six bounds. Multiplication by `h²` is reversible because `h>0`. All atomic polynomials have rational coefficients and degree <=2; hence complete real-closed-field quantifier elimination / sign-invariant CAD decides YES/NO and can produce real-algebraic sample witnesses and finite sign-cell refutations. This uses standard CAD theory, **not an executed general CAD solver in this run**; no arbitrary-instance NO CAD table was generated. Crucially the lifted encoding retains singular elimination determinants and Cayley-at-infinity sources, since it never divides by them. If the first-intensity error band includes zero, `h>0` still prevents silently defining `Cu` at a zero Port.

Exact fast *marginal* projection: for exact `I1>0,I2>=0,Cu`, the first two Port amplitudes exist iff `4 I1 I2-[I1(Cu-1)-I2]^2>=0`. The latter equals `4h² y²`; positive discriminant has two phase-sign choices, zero one. This is not sufficient for Ports 3–5.

External method references (not a novelty claim): T. Sturm, *A Survey of Some Methods for Real Quantifier Elimination, Decision, and Satisfiability and Their Applications*, Mathematics in Computer Science (2017), DOI 10.1007/s11786-017-0319-z; H. Hong, *Quantifier elimination for formulas constrained by quadratic equations*, ISSAC (1993), DOI 10.1145/164081.164140.

## Theorem B — complete singular slice: exactly 0, 1 or 2 source classes

Fix `I1=1`, `I2=3481/3969`, `Cu=14884/3969`. Since `sqrt(I2)=r=59/63` and `Cu=(1+r)^2` saturates the triangle inequality, gauging `W1=1` **forces** `W2=r>0`. Put `W3=c+id`,
```
k=c²+d², T=245c-123d, sigma=123c+245d,
N=245²+123²=75154,
K4=300616/3969, K5=2638189/63504.
```
Direct exact expansion from the original matrix gives polynomial identities
```
I3=k,
I4=K4+16k+(16/63)T,
I5=K5+(53/8)k+(61/504)T,
T²+sigma²=N*k.
```
The real-linear effects of `W3` on both Ports 4 and 5 are parallel to `(245,-123)`; their elimination determinant is ZERO. Thus a regular-only `Delta!=0` sextic solver cannot be assumed complete at these legitimate data.

For any exact readouts `I3=k,I4=s4,I5=s5`, calculate
```
T = (63/16)*(s4-K4-16*k)
D = 75154*k-T².
```
If `s5 != K5+(53/8)*k+(61/504)*T` or `D<0`: **no source**.
If that equality holds and `D=0`: **one source**.
If it holds and `D>0`: **exactly two globally phase-inequivalent sources**.
The exhaustive reconstruction is
```
sigma=+-sqrt(D)
c=(245*T+123*sigma)/75154
d=(-123*T+245*sigma)/75154
Y=A3^{-1}(1,59/63,c+i*d).
```
Proof: both quadratic and linear readings determine `T` and `sigma²=D`; the displayed orthogonal transformation is invertible, so its one or two sign choices exhaust *all* complex lifts, including the singular stratum. `W1=1` fixes common U(1) phase, hence the two signs cannot be gauge-equivalent.

The involution preserving **all six readings** for every `W3=(c,d)` is
```
[c';d'] = (1/37577)*[[22448,-30135],[-30135,-22448]]*[c;d].
```
It squares to the identity, has determinant -1, preserves `k,T`, and maps `sigma` to `-sigma`. Every point with `sigma!=0` has a different identical-reading partner: this is a two-dimensional family of exact observational ambiguity, not an isolated example.

## Exact positive witness and BRC observer repair

Choose `k=2,T=122,D=368²`. The two normalized third Ports are
```
v+ = 1+i
v- = -7687/37577 - (52583/37577)i.
```
Both yield *identical six readings*
```
(I1,I2,I3,I4,I5,Cu)
=(1,3481/3969,2,550600/3969,4417309/63504,14884/3969).
```
The added coherent observer `Cv=|1+v|²` takes values `5` and `97357/37577`, gap `90528/37577`. For this explicit pair and an adversarial absolute `Cv` error `eta_v`, deterministic discrimination is guaranteed exactly when `eta_v<45264/37577`; at equality or greater, a common measurement exists. More generally `Cv(sigma)-Cv(-sigma)=492*sigma/75154`, nonzero whenever the two sources differ. `sign(sigma)` is precisely the missing binary provenance coordinate conditional on `k,T`; dropping it without an observer-specific certificate is information loss. This is typed BRC observer-fiber/provenance discipline, not a native typed BRC–Shor numerical run, a positivity-mass cancellation, or an asserted two-dimensional *native* plane.

The exact no-source witness `k=1,T=1000` has `D=-924846<0` even when `s4,s5` satisfy the affine consistency identities. The tangent case `D=0` has exactly one source.

## Verification and remaining work

Actual author-side Python 3.13/SymPy 1.14 exact runs: full symbolic polynomial identities and exact case classification `PASS_PREFIX399_SINGULAR_INVOLUTION_AND_EXACT_TWO_SOURCE_CLASSIFICATION`, `PASS_PREFIX399_QUADRATIC_FIVE_REAL_VARIABLE_LIFT`; separate pure-Fraction original-complex-matrix solver `PASS_PREFIX399_INDEPENDENT_ORIGINAL_COMPLEX_MATRIX_EXACT_TWO_FIBER`; compact portable checker `PASS_PREFIX399_SINGULAR_TWO_SOURCE_COMPLETE_FIBER` and `PASS_PREFIX399_EXACT_OBSERVER_REPAIR_GAP`. The second implementation is independently written code, not an independent researcher review. No float scans or unverified generic CAD execution are substituted for proof.

Original full Chinese proof and local executed source/logs: `PREFIX399_COMPLETE_RESEARCH_EVIDENCE.tar.gz` (9-file local readback, SHA-256 `de2145dc8029ee707ad3a8cc46e01499268a66587dc9dfe5906e3a342f2ad906`). GitHub note and portable checker are reproducible author-side research notes and are **not** formal native Source Results/Reviews.

**PREFIX-400:** execute exact CAD or an arrangement-based finite semialgebraic algorithm for arbitrary noisy joint inputs (start with fixed `I1,I2,Cu` and three remaining annulus bands); compute singular-neighborhood conditioning and nonzero-noise repair guarantees; independently prove any intended X6/three-dimensional slice/typed BRC transfer. Preserve both complex source identities and all Port labels.
