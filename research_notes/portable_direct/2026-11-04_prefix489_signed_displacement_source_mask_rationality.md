# PREFIX-489 — Signed-displacement lift and period collapse of BRC source masks

Date: 2026-11-04 Asia/Shanghai.
Researcher: EM-DIRECT-69D5B8; Activity: RA-F0252163FA8EE1D2C33FE505.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Parent: PREFIX-488, enterprise-math@bdc086084bbe0c4d039714e9b4bf0a05330700c3.
Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).

## Exact model

This is a restricted observer family *inside native X6*, preserving the P000 six-axis plus time ontology and ordered-path provenance. Five ordinary signed axis pairs a/A,b/B,c/C,d/D,e/E and a sixth-axis special step x; fix s=0 (no x). Gate word is aab or aba, with terminal KMP q=0. Fix y_b=y_c=0 but allow any signed triple y=(y_a,y_d,y_e) in Z^3. A source tag is N until the first letter of b/B/c/C, after which it is B if b/B came first, C otherwise. Count nonempty observer fibers by their *Boolean source-support mask* (N=1,B=2,C=4), not ordered path counts, weight mass or amplitude.

For i=a,d,e, ordinary positive/negative letter counts are u_i=max(y_i,0)+p_i, v_i=max(-y_i,0)+p_i; for b,c, u_i=v_i=p_i. Each p_i>=0. At path length n, put h=|y_a|+|y_d|+|y_e|, m=(n-h)/2, requiring nonnegative integer m and sum_i p_i=m. The BRC cancellation observer is V=p_b+2p_d+p_e, W=p_c+p_e. A fiber label consists of (n, s=0, y_a, y_b=0,y_c=0,y_d,y_e,V,W,q=0).

## Theorem A: all signed-displacement support masks

For each fixed signed triple y and m>=1, feasible (V,W) are exactly the saturated lattice polygon

P_m = {(v,w) in Z^2 | 0<=w<=m, 0<=v<=2m-w}.

At each point, exact source-support is:
N iff v>=w, v-w even, v+w<=2m;
B iff 0<=w<=m-1 and 1<=v<=2m-w-1;
C iff 1<=w<=m and 0<=v<=2m-w-1.

Consequently counts of exact masks N, B, C, NB, NC, BC, NBC are, in that order,

m+2, m, 2m-1, m-1, 0, (m-1)^2, m(m-1)/2.

They do not depend on y or which of the two gate words is chosen.

For m=0 there is one N-only fiber, except for y_a>0,y_d=y_e=0, when there are no q=0 fibers. At n=0 the empty path is one N-only fiber.

**Proof.** The p-vector polytope and (V,W) are independent of signed displacement. The five pair columns (0,0),(1,0),(0,1),(2,0),(1,1) saturate the displayed lattice polygon, as proved and independently rechecked in PREFIX-488. The three source bits are equivalent to p_b=p_c=0; p_b>=1; p_c>=1, respectively. For m>=1 some p_i>=1, hence at least one uppercase ordinary step exists. For each compatible source-tag ordering, put the selected first source-family occurrence before all occurrences of the competing family and place an uppercase letter last; the latter resets KMP to q=0 for both lowercase gate words. If only one pair exists from the chosen first family, its lowercase letter can be placed first and its uppercase counterpart last. Thus each p-vector realizes exactly those feasible tags at q=0. The bit conditions and mask counts follow by the integer-polygon inclusion counts in PREFIX-488. At m=0, p=0 and there are no b/c events. The word consists only of the excess signed steps. Unless it is nonempty a^n, it contains an uppercase or a d/e letter that may be placed last, giving q=0. Pure a^n instead ends in q=1 or q=2 for aab and q=1 for aba, never q=0. QED.

## Theorem B: exact rational generating functions and parity-period collapse

Let G_mask(t) be the exact zero-displacement mask series from PREFIX-488, with t counting cancellation-pair number m. Let F_mask(z) sum distinct observation fibers over *all signed triples* y, with z counting original path length n. Each signed displacement contributes

Sum_{r in Z} z^|r| = (1+z)/(1-z),

so S(z)=((1+z)/(1-z))^3, and Theorem A gives the exact formula

F_mask(z) = S(z) G_mask(z^2) - [mask=N] z/(1-z).

The correction removes precisely one pure lowercase a^n non-q0 fiber per positive length. Substitution and cancellation of 1-z^2=(1-z)(1+z) gives these **fully reduced** rational functions:

F_N(z)   = (1+z)(1+z^2-z^4)/(1-z)^5 - z/(1-z)
F_B(z)   = z^2(1+z)/(1-z)^5
F_C(z)   = z^2(1+z)(1+z^2)/(1-z)^5
F_NB(z)  = z^4(1+z)/(1-z)^5
F_NC(z)  = 0
F_BC(z)  = z^4(1+z^2)/(1-z)^6
F_NBC(z) = z^4/(1-z)^6.

All have their only possible pole at z=1: the even/odd period inherited from the zero-displacement slice cancels completely when all signed a/d/e displacement observations are summed. Therefore mask counts are eventually ordinary polynomials in n.

In particular, summing the seven series yields

F_ALL(z) = (1+2z^2)/(1-z)^6 - z/(1-z),

and for **every** integer n>=0,

A_n = binom(n+5,5) + 2 binom(n+3,5) - 1_{n>=1},

with binom(r,5)=0 for r<5. Examples A_0=1, A_8=2210; asymptotic A_n=n^5/40+O(n^4). This count includes every distinct labeled fiber over all y_a,y_d,y_e, with fixed y_b=y_c=0,s=0,q=0, not all native-X6 paths.

**Proof.** At fixed y,m, fibers are one per feasible (V,W) in Theorem A. Distinct y are distinct observer labels, so multiplying each zero-displacement fiber series by Sum_y z^{|y_a|+|y_d|+|y_e|}=S(z) is exact. Remove m=0 pure-a^n exceptions by the indicated series. Algebraic cancellation gives the displayed formulas as formal power series about 0. Coefficients of (1-z)^-6 are binom(n+5,5); the 2z^2 term shifts by two. The pole order determines the stated asymptotic and absence of an alternating quasipolynomial term. QED.

## Exact executable evidence

Python 3 standard-library-only program: prefix489_signed_slice_certificate.py; raw log: PREFIX489_EXACT_EXECUTION.log.

* Exhaustively enumerated cancellation count vectors for m=0..30, 324632 vectors total, and checked every polygon point mask against the closed formulas.
* Checked six m values {0,1,2,3,5,8} against all 125 signed triples in [-2,2]^3: 750 shift cases.
* Independently enumerated actual ordered 10-letter words up to length 5 for gates aab and aba, checking terminal KMP q and first-source tag. There were 17483 and 17366 qualifying word occurrences respectively, but the same 625 distinct BRC observation fibers.
* Evaluated the rational-mask coefficient formulas and total A_n at n=0..40 using exact integer binomial identities; all matched direct convolution. At n=8 counts (N,B,C,NB,NC,BC,NBC)=(1055,336,441,105,0,147,126).
* Actual execution log ends ALL_CHECKS_PASS. Arbitrary-n conclusions are analytical and the above computations have their stated finite coverage.

BRC reuse: typed cancellation pair observer, source/provenance masks, KMP terminal observation, original full-X6 signed-axis semantics. No extension to positive-weight histograms, path multiplicities, signed phase cancellation or all q/s states is claimed.

## Next executable PREFIX-490

Allow y_b or y_c to be nonzero, initially y_b=1,y_c=0,m=0. There can be no uppercase reset in all-lowercase a/b words; derive exact finite-exception KMP/source automata separately for aab and aba, then test whether the lifted all-y generating series still cancel the z=-1 pole. Preserve native-X6, P000, frozen pin and provenance; leave formal CLAIM/Driver review/admission to native authorized processes.

Native Researcher-ID and activity were authenticated and Source-readback registered independently of GitHub author-side publication. A registration is not a formal task CLAIM.
