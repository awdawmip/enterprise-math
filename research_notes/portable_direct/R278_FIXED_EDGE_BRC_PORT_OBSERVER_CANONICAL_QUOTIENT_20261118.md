# R278 — Fixed-edge BRC Port observer quotient and mixed-feedback witness

Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECK / NOT_REVIEWED.
Lineage: R275–R277 at fae3d3cf66a7bc294f9c5a854764bb14ab174030. Frozen scientific inputs: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Typed interface: native WBRC-T30/T31/T32, nonnegative rational weights and labeled visible Ports. This result is for a restricted future-observer language.

## 1. Model and permitted future

Let W be an n-by-n nonnegative rational visible-Port matrix, with every row sum strictly below 1. Let A=I-W, S=A^(-1), choose a visible readout Port r, and fix m labeled edge locations e_i=(u_i,v_i). A context adds nonnegative rational x_i at these locations, preserving strict stability. The only observable is

~~~text
F_W(x) = [A - sum_i x_i E_(u_i,v_i)]^(-1)_(r,r).
~~~

Any finite program may insert these edges repeatedly (increments aggregate), read F at intermediate steps and select further permitted edits adaptively from previous readouts. A sufficiently small positive rational box around the zero input always remains stable. The edge labels and observer are fixed; no unrestricted Port contexts are implied.

## 2. Theorem A: finite rational signature for all future observations

Set U=[e_(u_1),...,e_(u_m)], V=[e_(v_1),...,e_(v_m)], X=diag(x_1,...,x_m) and

~~~text
s=S_(r,r),   a_i=S_(r,u_i),   b_i=S_(v_i,r),   G_ij=S_(v_i,u_j).
~~~

Then on every permitted stable context:

~~~text
F_W(x) = s + a^T X (I-GX)^(-1) b = N_W(x)/D_W(x),
D_W(x) = det(I-GX) = det(A-U X V^T)/det(A),
N_W(x) = cofactor_(r,r)(A-U X V^T)/det(A).
~~~

Both N and D are multiaffine rational polynomials in m variables. D(0)=1, N(0)=s.

Proof: apply the matrix determinant lemma to the rank-m perturbation, and Woodbury (or direct multiplication) to its inverse. The scalar inverse-cofactor identity yields N/D. For fixed values of all other variables, varying x_i changes the matrix by a single rank-one update, so each determinant and principal cofactor is affine in x_i. This proves multiaffinity separately for every variable.

The coefficients of N and D can be reconstructed exactly using 2^m symbolic Boolean-subset determinant and cofactor evaluations. For each subset T of the m named edges let P_T=det(A-sum_(i in T) E_i)/det(A), Q_T=cofactor_(r,r)(A-sum_(i in T)E_i)/det(A). Then

~~~text
D_[H] = sum_(T subset H) (-1)^(|H|-|T|) P_T,
N_[H] = sum_(T subset H) (-1)^(|H|-|T|) Q_T.
~~~

These are algebraic coefficient evaluations; the Boolean-subset matrices need not be admissible stable physical contexts. The signature uses no more than 2^(m+1)-1 unconstrained rational coefficients (2^m N coefficients and 2^m-1 D coefficients), regardless of the size n of the Port matrix. This is a coefficient-count bound, not a bit-length bound.

## 3. Theorem B: canonical exact future-safe quotient

Cancel gcd(N_W,D_W) over Q[x_1,...,x_m] and normalize the resulting denominator to constant term 1. Denote the coprime pair by (N_red,D_red). It exists uniquely: D(0)=1, so any common polynomial factor has nonzero constant.

For two baseline-stable matrices W and W' with the same labeled edit alphabet and the same scalar observer, the following are equivalent:

1. All common stable admissible finite edit programs, including adaptive ones, produce identical intermediate scalar readouts.
2. F_W(x)=F_W'(x) for every sufficiently small nonnegative rational vector x.
3. N_W D_W' - N_W' D_W is identically zero as a rational polynomial.
4. Their normalized coprime polynomial pairs (N_red,D_red) are coefficientwise identical.

Proof: (1) implies (2) by inserting a specified vector through finitely many named edits. If (2) holds, the cross-product polynomial vanishes on a rational grid in an open box; hence every coefficient vanishes, proving (3). Uniqueness of reduced fractions in the UFD Q[x_1,...,x_m] and normalization gives (4). Conversely (3) makes scalar responses agree at every common stable context, and induction over steps gives identical adaptive readouts and choices. This equality is exactly the coarsest equivalence relation preserving all observations of the declared future language, not a claim of coordinatewise information-theoretic bit minimality.

For unrestricted WBRC-T32 future contexts, the full labeled effective Port matrix remains the canonical dynamic signature. The smaller polynomial pair is safe only for this fixed edge-edit alphabet and fixed scalar readout.

## 4. Theorem C: a minimal joint-feedback obstruction to singleton signatures

Consider two visible Ports 0,1 and observer r=0. Let the initial matrix W_c=diag(0,c), where c=0 or c=1/2. The allowed updates add a 0->1 edge x and a 1->0 edge y. Direct inverse calculation gives

~~~text
F_c(x,y) = 1 / (1 - xy/(1-c)).
~~~

The baseline and every single-edge readout agree between these models:

~~~text
F_0(0,0)=F_(1/2)(0,0)=1,
F_0(x,0)=F_(1/2)(x,0)=1,
F_0(0,y)=F_(1/2)(0,y)=1.
~~~

Yet for the same two-edge context x=y=1/4,

~~~text
F_0(1/4,1/4)=16/15,   F_(1/2)(1/4,1/4)=8/7.
~~~

Both final row sums are strictly below 1. Their mixed denominator coefficients are -1 and -2, respectively. This shows that the complete collection of baseline and arbitrary singleton-edit scalar responses fails to capture a necessary joint mixed-cycle residual. It is a concrete exact observer witness for the R273–R277 feedback program.

## 5. Reproducible exact evidence and scope

The accompanying R278_fixed_port_feedback_signature.py uses only fractions.Fraction, permutation determinants, principal cofactors and exact Boolean-subset Möbius inversion. It checks the two witnesses and all 81 direct inverse-versus-polynomial observations across three separate 3-Port matrices, each with three labeled additions and every edit vector in {0,1/8,1/4}^3. All tested row sums are strictly below 1 and the checks pass. The JSON certificate records every polynomial coefficient and the test counts. Theorems A and B hold for all finite n,m under their hypotheses by algebraic proof, rather than by extrapolation from the tests.

Existing P000, ACTIVE worldview, and frozen scientific input pins are unchanged. There has been no independent mathematical review or formal Result admission.

## 6. Next scientific questions

For a finite edit horizon k, classify the smallest safe signature by the mixed-cycle words of length at most k and compare with the all-horizon polynomial pair. Develop a prime-adic valuation and leading-residue signature for the reduced numerator/denominator under resonance, incorporating R270–R277. Test several specified star readouts and external edges with proven Port scope, then investigate a provenance-preserving map from R269 auxiliary-source classes to native labeled BRC Ports.
