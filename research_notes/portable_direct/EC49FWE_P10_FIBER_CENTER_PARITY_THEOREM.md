# EC49FWE — Projective-fiber model and parity-resolved minimizing reflections for frozen P10

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_FIBER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
Mode: independent portable research on an unpublished topic; no shared CLAIM, formal Result, or Review.
Scientific input pin: BRC16943 (unchanged).
Immediate predecessor: awdawmip/enterprise-math@425997bc02b242d2c51d7057817279a507397d9b:research_notes/portable_direct/EC49FWD_CRT_PROJECTIVE_CENTER_MULTIPLICITY_THEOREM.md.
This is the auxiliary nonconfluent mod-10 factor P10, **not** the complete Bernoulli/mod-11 certificate or native X6 geometry.

## New result

Let P10 be the same 44-element set of pairs (h,n) in (Z/10Z)^2, obtained from the exact frozen BRC16943 modular constants and ten nonconfluent z tests (z != 3) plus the confluent nonzero test, as implemented by the attached verifier and the predecessor. Use CRT to identify h=(h2,h5), n=(n2,n5). For nonzero (h5,n5) let q=[h5:n5] be represented by the slope n5/h5 in F5, with infinity when h5=0. The point (0,0) in F5^2 is never accepted.

**Theorem A (four projective fibers).** P10 membership depends only on the parity pair (h2,n2) and q. Exactly the following slope sets are allowed:

| (h2,n2) | Allowed q in P1(F5) | Number of P10 cells in this parity fiber |
|---|---|---:|
| (0,0) | {3} | 4 |
| (0,1) | {0,3,4,infinity} | 16 |
| (1,0) | {2,3,4,infinity} | 16 |
| (1,1) | {2,3} | 8 |

This is a complete exact finite identification: the source predicate and these four fibers agree on all 100 possible (h,n). Every allowed projective slope has four nonzero F5 vectors, so 4+16+16+8=44. This replaces 44 unstructured cells by four short slope selectors and makes the unit homothety invariance immediate.

For any primitive mod-10 direction (a,b), choose an affine point x0=(h0,n0) with
(b-a)h0-a n0=-1 (mod 10), and define
S(a,b)={t mod 10 : x0+t(a,b-a) belongs to P10}.
Let D=min_c |S triangle (c-S)|; let E be the number of *even* minimizing reflection centers c, and O the number of *odd* minimizing centers. Thus N=E+O is the unsigned count in EC49FWD.

Write epsilon=(a mod 2,b mod 2) and lambda=b/a in P1(F5). For lambda=infinity take a=0 mod 5. Then (D,E,O) depends only on (epsilon,lambda) and is exactly:

| epsilon / lambda | 0 | 1 | 2 | 3 | 4 | infinity |
|---|---|---|---|---|---|---|
| (1,0) | (2,1,0) | (2,2,2) | (0,0,1) | (2,2,2) | (2,1,0) | (0,0,1) |
| (0,1) | (2,2,2) | (2,1,0) | (2,1,0) | (2,1,0) | (2,1,0) | (2,2,2) |
| (1,1) | (2,1,1) | (2,1,1) | (2,2,0) | (2,2,0) | (2,2,0) | (2,0,2) |

**Theorem B (parity refinement).** The table is exact for every primitive direction and any valid affine base point. It refines the earlier four-valued (D,N) observation: the 72 original directions distribute as
(D,E,O)=(0,0,1):8; (2,1,0):24; (2,2,2):16; (2,2,0):12; (2,1,1):8; (2,0,2):4.
Summing E+O reproduces the predecessor's (D,N) histogram [(0,1):8,(2,1):24,(2,2):24,(2,4):16].
In particular, **all perfect symmetries have an odd minimizing center**, whereas some near symmetries admit only even minimizing centers and some only odd centers. These are genuine differences lost by the unsigned multiplicity N.

## Proof and compact finite certificate

1. Theorem A is a **verified finite lemma**, not an asserted symbolic factorization of the upstream Bernoulli model. Evaluate the frozen modular predicate on h,n in 0..9 and compare it to the four projective slope selectors. The attached executable checks each of the 100 possible pairs with exact mod-11 arithmetic and also verifies the 400 unit-covariance cases. This is exhaustive, with no floating-point arithmetic and no undocumented testing assumption.

2. The determinant constraint on the chosen affine line is
v_n h - v_h n = -1, where v=(v_h,v_n)=(a,b-a).
Thus mod 5 the affine line avoids the origin and meets each projective direction q in P1(F5) **exactly once except** q=s=[v_h:v_n], the direction of the line, which it never meets. If a!=0 mod 5, write s=v_n/v_h=lambda-1 and define
phi_s(q)=(q-s)^(-1) for finite q != s, phi_s(infinity)=0.
The determinant implies n-s h=1/v_h, hence phi_s(q)=v_h h=v_h h0+(v_h)^2 t (mod 5), including the q=infinity case. If a=0 mod 5, then s=infinity and h=-1/v_n is fixed; use phi_infinity(q)=q=n/h, an affine nonconstant function of t. Consequently the projective-to-phase map phi_s is a bijection from P1(F5)\{s} to F5 and differs from t5 by an invertible affine transformation.

3. Mod 2, the affine determinant condition selects the following two parity fibers as t2 varies:
epsilon (1,0): (1,0) and (0,1);
epsilon (0,1): (1,0) and (1,1);
epsilon (1,1): (0,1) and (1,1).
Let F_i,F_j be the corresponding two slope selectors from Theorem A. For s=lambda-1, or s=infinity, set A=phi_s(F_i\{s}) and B=phi_s(F_j\{s}), two subsets of F5. A reflection c in Z/10Z factors into its parity c2 and its F5 coordinate c5. When c2=0 it preserves the two parity layers; when c2=1 it exchanges them. Therefore its exact mismatch is

D_even(k)=|A triangle (k-A)|+|B triangle (k-B)|,
D_odd(k)=2|A triangle (k-B)|,  k in F5.

The invertible affine change between phi_s and t5 sends each reflection center to a unique reflection center and does not change its mod-2 parity. Thus the minimizing center counts E,O can be computed entirely from these two 5-element subsets. Inserting the four explicit F_i and computing five pair sums in each parity case gives the displayed 3 by 6 table. The attached verifier independently evaluates these exact set formulas for all 18 classes, then re-evaluates the **original 10-residue affine mask** for all 72 primitive directions and checks equality.

The proof replaces a raw 72-direction examination by an explicit projective-fiber decomposition and universal two-layer correlation identities. The last step uses a complete 18-class finite F5 certificate; a case-free closed-form evaluation of the table remains open. No claimed infinity-family conclusion depends on an unbounded numerical experiment: CRT and the exact finite 10/5-residue case partitions exhaust the specified direction domain.

## Interpretation / observer boundary

Parity of the minimizing center is invariant under changing affine base points, because t -> t+k sends c -> c+2k; unit homothety changes t by an odd-unit affine bijection and also preserves center parity. This makes (D,E,O) a well-defined observer of the direction's CRT class.

The observer still discards the actual minimizing centers, orientation, signed mismatch sites, CRT unit representative, and mod-11 confluent component. It is not lossless for downstream computations requiring those quantities. A later application to moving Farey gaps must retain its exact input and show the corresponding observer-preservation law. No BRC-native six-axis or physical claim follows from the auxiliary two-coordinate predicate.

## Verification, next question

Executable: EC49FWE_P10_FIBER_CENTER_PARITY_VERIFY.js.
Captured output: EC49FWE_P10_FIBER_CENTER_PARITY_OUTPUT.json.
Independent cross-check: separate Python reconstruction of the original frozen predicate, four fibers, 18 phase computations, and all 72 affine masks produced the same (D,E,O) table.
Status: AUTHOR_PROVED / EXACT_FINITE_FIBER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.

Next: derive the E/O formulas without the 18 finite F5 cases, or determine the complete signed locations of the two minimizing mismatches using the projective phase coordinate. Then check which such information survives coupling to the full mod-11 factor and helps the mobile Farey maximum-gap objective. Keep BRC16943, P000 and all inherited source pins fixed.
