# R284BV — Radix-separated double-frozen star-Port: complete observer fibres, sharp noise radius, and deterministic decoding

Date: 2026-11-20 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. This is a portable, independent auxiliary algebraic Port result, **not** native BRC/X6 arithmetic, a CLAIM, an accepted Result, a Review or a change to P000.

## Frozen source and question

Continue R284BU_SHARP_ROOT_FREE_LEAF_CONSTANT_GAP_20261120.md, immutable proof source `9ebf0c5dc3b59c58a06ea7e0ae36081175917d58`, with its R284BT predecessor. Keep the same frozen 4×4 star-Port determinant model and circle-residue measurement semantics. Unknown `C ∈ {1,...,H}^{4×4}`, `H≥2`; freeze `d1=t,d2=s`; vary `d0,d3,z1,z2,z3`. Define
```
F_C = det(diag(d0,t,s,d3)-C-z1 E01-z2 E02-z3 E03).
```
R284BU established the sharp constant single-entry gap
`m_H(t,s)=ts-(H-1)(t+s)` for `t,s≥H²+1`, but not whether other multi-entry pairs could create smaller or zero constant gaps. We now construct settings where these are the *only* possible constant-response pairs and provide an arithmetic decoder with no exponential candidate table.

## Theorem (all H≥2; exact if-and-only-if noise radius)

Set `B=48 H^4+1`, `s=B`, `t=B²` and `m=ts-(H-1)(t+s)>0`. For two admissible matrices C and D, the difference `F_C-F_D` is independent of the five free controls **if and only if** C and D agree in all 15 entries other than `C03`. In that case
```
F_C-F_D = (D03-C03) q3(C),
q3(C) = [adj(diag(t,s,d3)-C_leaf) (C10,C20,C30)^T]_3,
m ≤ q3(C) ≤ H(t+H-1)(s+H-1).
```
In particular there is no exact alias `F_C≡F_D` for distinct C,D, and the minimum nonzero constant gap among all pairs is exactly `m`.

With a single nonadaptive read of the determinant modulo a sufficiently large prime, using circular real-valued adversarial error radius `rho≥0`, uniform recovery of all `H^16` candidates is possible **if and only if**
```
                         2 rho < m.
```
The sufficient direction admits a **deterministic choice** of all five free controls and a **direct arithmetic decoder** (no H^16 table). The prime is any prime above the explicit finite bound given below; a particular prime is not required for this existence theorem. Bit complexity of decoding is polynomial in the input/output integer bit lengths at fixed dimension four; this is not a near-optimal bit-length or small-modulus scheme.

## Proof, part I: exact signature and integer coefficient separation

Write
```
C = [[a,b1,b2,b3],
     [u1,A11,x,y],
     [u2,w,A22,z],
     [u3,g,h,r]]
T=t-A11; S=s-A22;
U=T*S-x*w;
V=-r*U-z*(T*h+x*g)-y*(w*h+S*g);
p1=S*u1+x*u2; p2=T*u2+w*u1;
q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+S*u3);
q2=-r*p2+T*z*u3+u1*z*g+y*(w*u3-u2*g);
q3=U*u3+p1*g+p2*h;
J=-a*U-b1*p1-b2*p2;
K=-a*V-b1*q1-b2*q2-b3*q3.
```
Schur/block determinant expansion gives the exact identity
```
F_C=d0*(U*d3+V)-z1*(p1*d3+q1)-z2*(p2*d3+q2)-z3*q3+J*d3+K.      (1)
```
Its complete nonconstant signature is `S(C)=(U,V,p1,p2,q1,q2,q3,J)`. The only occurrence of b3 is in the constant term K, so equal matrices away from b3 always have equal signatures.

Each coefficient of each component of S(C), viewed as a polynomial in independent t,s, has bidegree at most (1,1). Moreover every such coefficient has absolute value ≤24H⁴: in the original 4×4 Leibniz determinant, each of at most 4!=24 permutation products supplies at most one term for each fixed monomial in t,s and the five free controls, and its remaining C-entry product has absolute value ≤H⁴. Thus the base-B substitution (t,s)=(B²,B) is injective on these coefficient arrays. Indeed, the difference of two evaluations has the form `c0+c1 B+c2 B²+c3 B³`, `|ci|≤48H⁴<B`; reduction modulo B followed by division proves each ci=0. Individual coefficient arrays can be recovered by balanced base-B digits, since B is odd and all original digits lie in [-24H⁴,24H⁴].

It remains to prove that formal equality of S determines 15 entries. Let `[t]`, `[s]`, `[ts]` mean coefficients in the formal t,s polynomial, after the preceding base inversion. Recover successively:
- `A22=-[t]U; A11=-[s]U`;
- `u1=[s]p1; u2=[t]p2`, both strictly positive;
- `x=([1]p1+A22*u1)/u2; w=([1]p2+A11*u2)/u1`;
- `u3=[ts]q3`;
- from `q3-U*u3=g*p1+h*p2`, `g=[s](q3-U*u3)/u1`, `h=[t](q3-U*u3)/u2`, with g,h≥1;
- `r=-[ts]V`; from `V+r*U=-z*(T*h+x*g)-y*(w*h+S*g)`, `z=-[t](V+r*U)/h`, `y=-[s](V+r*U)/g`;
- `a=-[ts]J`; from `J+a*U=-b1*p1-b2*p2`, `b1=-[s](J+a*U)/u1`, `b2=-[t](J+a*U)/u2`.

This recovers exactly every entry except b3 and proves the equivalence in the theorem. As q3>0 for these t,s, distinct values of b3 differ by nonzero constant multiples of q3. R284BU's cofactor extremal theorem gives exactly `m≤q3≤H(t+H-1)(s+H-1)` with attainable endpoints; a b3 increment of 1 is admissible since H≥2. The sharp lower gap is therefore m.

## Proof, part II: explicit one-scalar encoder and table-free decoder

Fix an arbitrary finite `rho≥0`; put `R=ceil(rho)`,
`A=24*(t+s+H+1)^4` and `Q=4*(A+R+1)`. Every coefficient of F_C as a polynomial in the five free controls, evaluated at frozen t,s, has absolute value ≤A (a deliberately loose Leibniz bound).

Choose the **integer** free controls
```
d3=Q, d0=Q^3, z1=Q^5, z2=Q^7, z3=Q^9.
```
Then equation (1) becomes
```
F_C=Q P_C+K,
P_C=J+V Q²+U Q³-q1 Q⁴-p1 Q⁵-q2 Q⁶-p2 Q⁷-q3 Q⁸.            (2)
```
Choose any prime satisfying
```
p > 4*(A+R+1)*Q^9.                                                (3)
```
The bound `|F_C|<2A Q^9` puts every value and its rho-neighborhood within the centered interval (-p/2,p/2). Hence the noisy circle-residue observation can be centered-lifted to a real `y=F_C+epsilon`, `|epsilon|≤rho` without wrap ambiguity.

Because `|K|≤A` and `Q>2(A+rho)`, rounding `y/Q` to the nearest integer recovers `P_C` exactly. Balanced base-Q digits (each coefficient magnitude ≤A<Q/2) recover all eight signed entries of `S(C)` from (2). Apply the balanced base-B extraction and reconstruction of part I to recover the first 15 matrix entries and then compute `K_base=-aV-b1q1-b2q2`. The final residual obeys
```
(P_C Q+K_base-y)/q3 = b3 - epsilon/q3.
```
Since `q3≥m>2rho`, nearest-integer rounding uniquely recovers `b3∈{1,...,H}`. Every division is exact on the noiseless recovered coefficients. The decoder uses a bounded number of big-integer arithmetic operations; it requires no candidate table. This proves sufficiency.

For necessity, use the R284BU minimizing witness (all entries admissible, b3 increment 1): its response difference is identically m for all remaining controls. Modulo any prime its circular distance is at most m. If 2rho≥m, the two closed circular error balls overlap at every possible measurement, including adaptive repetitions; exact worst-case recovery is impossible. QED.

## Exact computation and independent checks

Companion `R284BV_radix_double_leaf_checker.py` exhaustively enumerates the 65,536 matrices at H=2, independently computes 384 direct Leibniz determinants, and executes the table-free arithmetic decoder on every matrix at three adversarial integer errors. The JSON records the exact data:
```
H=2; B=769; s=769; t=591361;
all candidate matrices=65536;
nonconstant signature classes=32768, each of size 2 (only b3 differs);
min constant gap m=454164479;
max constant gap=910697480;
largest guaranteed integer error=227082239;
decoder scenarios=196608; direct determinant crosschecks=384.
```
The saved `Q=11801801187046420106734176` has 84 bits. A prime above (3) needs at least ~833 bits under this deliberately loose construction. For general H, the preceding argument is symbolic/algebraic; the exhaustive experiment is only H=2. Formal proof assistant checking: not performed. Independent scientific review: NOT_REVIEWED.

## Relation to P000, observer residuals, and next unit

This finite integer determinant is an *auxiliary* 4×4 scalar observation, not native X6/BRC rotation or a complete native three-dimensional slice; no native transfer is asserted. The fibre before recovering K retains the unobserved directed edge b3. The final constant-slot measurement restores that residual only for the frozen observer and the proved noise range. General native edge provenance, history and branch types must be retained separately.

Next: improve the 833-bit upper construction towards the information bound while retaining deterministic table-free decoding; classify other (t,s) where the same 15-entry injectivity holds (without huge radix separation); extend to n≥5 with multiple frozen leaves and typed observer-composition guarantees.

Historical portable source attribution: EM-DIRECT-E6B1DD (unverified as current native session); this note makes no current CLAIM, Activity checkpoint, Result/Review or foundation-promotion assertion.
