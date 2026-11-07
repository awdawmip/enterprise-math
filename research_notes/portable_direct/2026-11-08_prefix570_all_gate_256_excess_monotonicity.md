# PREFIX-570 — 257-layer gate e-positivity and coefficientwise gate-count growth

Research date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Previous source: PREFIX-557–569, especially PREFIX-566's 37-class observer and PREFIX-569's 128-excess theorem.

## Model and scope

The underlying frozen four-STAR X6 BRC system retains 96 ordered native ports with six distinguishable actions per port. This note considers the precise observer q1=q2=q3=q4=1, x=q5, y=q6, gate marker z, for the nine permitted roots r5=r6=0. Put u=x+y and v=xy. This is an observer-level result; original native edge identity and multiplicity remain in the frozen input.

The exactly checked weighted 37-class transition matrix has the rank-one form M=N+z U e_5^T, with U_4=U_15=U_17=1 and all other U_i=0. Gated edges have zero x,y exponent. The native axis-swap involution fixes 32 original ports. Their observer classes form I={0,2,5,7,14,15,18,25,27,31,33}; equality of their readouts follows from the weighted transition descent.

Let F_(i,d)(x,y,z) be the complete length-d joint path-count polynomial with F_(i,0)=1. The minimal length containing a gate is delta_i, with classes:
0:4, 2:5, 5:4, 7:3, 14:5, 15:1, 18:4, 25:3, 27:4, 31:3, 33:2.

For k>=1 and s>=0 define the matched-excess slice
H_(i,k,s)(u,v) = [z^k] F_(i,delta_i+4(k-1)+s)(x,y,z), written in the unique integer elementary-symmetric basis u,v.

## Theorem A — all gate counts, excess 0..256

For each of the 32 exchange-fixed native ports (equivalently its class i in I), for EVERY integer k>=1 and EVERY integer 0<=s<=256,

H_(i,k,s)(u,v) belongs to Z_{>=0}[u,v].

The excess bound is 257 consecutive lengths, versus 129 for PREFIX-569. The gate count k is unrestricted.

## Theorem B — coefficientwise monotonicity between gate counts

Under the SAME quantifiers and observer,

H_(i,k+1,s) - (4+8u) H_(i,k,s) belongs to Z_{>=0}[u,v].

Thus H_(i,k,s) >=_coeff (4+8u)^(k-1) H_(i,1,s). The lengths being compared differ by four native actions; s is their common excess above their respective sharp minima. Coefficientwise means coefficientwise in the algebraically independent variables u and v.

## Proof

Work over the formal power-series ring Z[x,y,z][[t]], and let R(t)=(I-tN)^(-1). Define A_i(t)=[R(t)U]_i, K(t)=[R(t)U]_5 and B(t)=[R(t)1]_5. Expanding the resolvent of M=N+z U e_5^T in the number of gate insertions gives the exact identity, for any k>=1,

[z^k] sum_(d>=0) F_(i,d) t^d = t^k A_i(t) K(t)^(k-1) B(t). (1)

This may equivalently be proved by unique cutting of an ordered path at its gate actions. Each cut retains every native step, path multiplicity and observer weight.

The observed minimal t degrees are ord A_i=delta_i-1, ord K=3, ord B=0. Define a_i=t^(-(delta_i-1))A_i, c=t^(-3)K and b=B. Exact shortest return enumeration gives c(0)=4+8u, and b(0)=1. Shifting the exponent in (1) yields

H_(i,k,s) = [t^s] a_i(t)c(t)^(k-1)b(t). (2)

The executable exhaustive certificate checks that EVERY coefficient of a_i, c and b through t^256 lies in Z_{>=0}[u,v], for all i in I, using exact integer arithmetic on the complete 37-state transition rows. A degree-s coefficient of a product of formal power series only uses factor coefficients of degrees <=s. Therefore (2) proves Theorem A for all k, even though the supporting factor scan has a finite depth bound.

Subtract (4+8u) times (2) at k from (2) at k+1:

H_(i,k+1,s)-(4+8u)H_(i,k,s)
= [t^s] a_i(t)c(t)^(k-1)(c(t)-c(0))b(t). (3)

The factor c(t)-c(0) has zero constant term; its coefficients through t^256 are nonnegative, and so are the coefficients of the other factors on that window. This proves Theorem B for every k and s in scope. Repetition yields the final lower bound. No analytical convergence, approximation or floating-point check is involved.

## Exact finite certificate and reproducibility

Run python3 PREFIX570_compact_certificate.py alongside the existing, unchanged PREFIX565_positive_marginal_certificate.py and PREFIX566_gate_quotient_certificate.py, all in the research_notes/portable_direct directory. It rechecks the nine roots (5,184 native weighted projected edges), the complete 37-state row quotient, 576 native exchange edges, the exact three gated source rows and common target, and the integer polynomial evolution of A_i/K/B through depth 260.

Elementary-basis conversion is exact: pair the x^a y^b and x^b y^a monomials; p_0=x^0+y^0=2, p_1=x+y=u, p_n=u p_(n-1)-v p_(n-2). The diagonal x^a y^a contributes v^a. The conversion checks x-y exchange symmetry first. Across A_i, K and B the factor scan checks 1,428,455 + 129,033 + 259,842 = 1,817,330 nonzero integer coefficient positions, finding no negative values.

A separate extended execution, preserved in PREFIX570_FULL_RESEARCH_EVIDENCE.zip, checked direct gate-aware propagation depths 0..19 against (1)/(2), comparing 231 complete gate-slice polynomials and 1,455 nonzero integer positions, plus 154 direct instances of inequality (3). Both exact programs returned ALL_CHECKS_PASS.

## Research boundary and next discriminating experiment

The exact theorem has unrestricted k and excess 0..256. The open mother question is arbitrary excess s>=257, not merely another larger finite scan. Next test: search for an invariant nonnegative coefficient cone, a positive rational generating-function representation of the factors, or a verified first negative elementary-basis factor witness beyond the present bound. If a factor turns negative, test the complete product before inferring that the joint gated count also turns negative. A second branch should benchmark a_i/c/b convolution against direct 37-state gate-truncated propagation with output recovery.

Native control session_start failed with OSError and task listing reached WAITING_RESOURCE / EVENT_COLLECTION_IO in this turn, so active Owner and authentic native Researcher-ID were not confirmed. This document is an independent author proof and source evidence, not a formal CLAIM, Result, Review or promoted theorem. Current P000 V5, ACTIVE Heartbeat World and portable research rules were read separately from the frozen scientific input.
