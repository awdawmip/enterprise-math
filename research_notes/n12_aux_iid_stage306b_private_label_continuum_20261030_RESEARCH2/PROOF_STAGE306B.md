# Stage306-B — certified three-F continuum bound and joint-audit obstruction

**Scientific status, 2026-10-30:** PORTABLE_AUTHOR_PROOF / EXACT_DYADIC_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is an external positive-rational finite branch probability model; it is not a P000-X6 physical result or an accepted native Source Task Result.

**Immutable input context:** verified GLOBAL_KNOWLEDGE_V1 main@27a75c9f940402746b3aa78f62fb1cd8c4b60104; Enterprise Math main@816e145a36dede116cf5f42732c2cd19a7f81e5c. The global canonical entry/manual, ACTIVE protected worldview, project AGENTS.md, original P000 V5 (Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488), X6/time, BRC finite positive branch substrate, joint-observer fidelity, research persistence and portable research protocol were read. Predecessor: Stage305-B immutable 5c786240b76b62e3c0ceab302cb5e4cb2ce8f5c3, which constructed risk 63/6400 but did not prove sharpness.

## Model and allowed observers

Original hidden source S is fair on {0,1}. Conditional on S=s, sample J, W, and first immutable F-output Y1 independently with p0=1/4, p1=3/4; Pr(J=1|S=0)=1/8, Pr(J=1|S=1)=7/8; Pr(W=S)=3/4; Y1~Bern(pS). Each branch w(s,j,w,y)=(1/2)Pr(J=j|s)Pr(W=w|s)Pr(Y1=y|s) is strictly positive rational.

The compressed controller sees (J,W,Y1) but not S. It fixes one deterministic real rate t(j,w,y) in [0,1] per available private history and uses three future conditionally independent F bits at this SAME rate. No extra mixture over rates inside a label or action-dependent reset is allowed in this strategy class. The ideal system instead uses pS in each F visit. Public examiner sees W,Y1 and earlier ordered actions/outputs but not S or J, and chooses F or H on each of three rounds using any public-history causal randomized strategy. H returns an independent fair bit. The public terminal observation retains W,Y1 and the complete ordered action/output trace. Risk is supremum of total variation over these policies.

For g=(W,Y1)=00,01,10,11, exact positive-branch summation gives masses (5/16,3/16,3/16,5/16), posteriors Pr(S=1|g)=(1/10,1/2,1/2,9/10), and Pr(J=1|g)=(1/5,1/2,1/2,4/5).

## Lemma 306.1: simultaneous all-adaptive reduction

Presample three potential F bits and an independent sequence of H innovations. Every admissible public-history policy acts on this complete FFF experiment via a common stochastic kernel, identical for ideal and compressed processes. Total variation is contractive under a common kernel. The strategy FFF observes all potential F bits, so it attains the maximum. Thus risk for each fixed rate table equals its public FFF total variation, including randomized adaptive H/F policies.

Conditioned on g=00, let x=t(0,00), y=t(1,00), and b_k(z)=z^k(1-z)^(3-k). Every ordered three-bit word of Hamming weight k has ideal probability p_k, with (p0,p1,p2,p3)=(61,21,9,9)/160. The exact fiber risk is

d(x,y)=(1/2) sum_{k=0}^3 binom(3,k) abs[(4/5)b_k(x)+(1/5)b_k(y)-p_k].

For 01 and 10 the choice t(0,g)=1/4 and t(1,g)=3/4 matches all paths exactly. The 11 source/label-bit mirror of g=00 has the same minimum by taking t(0,11)=1-y and t(1,11)=1-x. The four observed g fibers admit independent rate choices. Consequently the EXACT full problem, without approximations, reduces to

R3*= (5/8) inf_{x,y in [0,1]} d(x,y).

This equation quantifies the precise permission boundary: a locked two-real-rate port with fixed conditional J weights, not arbitrary mixtures over that port class.

## Theorem 306.2: continuum minimax enclosure

Exact rational arithmetic proves the entire real-parameter infimum satisfies

604661379/80000000000
<= R3* <=
15116534475889766921898005231381567/2000000000000000000000000000000000000.

Thus 0.007558267237500000 <= R3* <= 0.007558267237944884; interval width < 4.45e-13. In particular Stage305-B's 63/6400 is STRICTLY improvable by >0.00228548. This is a sharp numerical enclosure with a reproducible exact certificate, NOT an exact algebraic formula for the minimizer.

For the upper bound, take x=231083940855/10^12, y=555508857277/10^12. Then exact arithmetic yields
d(x,y)=15116534475889766921898005231381567/1250000000000000000000000000000000000.
Take the mirrored rates for g=11 and exact original rates for g=01,10. Multiplying by 5/8 gives the displayed feasible upper bound.

For the lower bound, on any interval I=[l,r], b_k has extrema at its endpoints and, when inside I, its stationary point z=k/3. For every rectangle I×J the residual r_k=(4/5)b_k(x)+(1/5)b_k(y)-p_k lies in an EXACT rational range [A_k,B_k] obtained by combining those four one-dimensional extrema. Hence throughout the rectangle,

d(x,y) >= (1/2)sum_{k=0}^3 binom(3,k) max(0,A_k,-B_k).

Start with [0,1]^2. Repeatedly split the longer side at its dyadic midpoint, tie toward x. Accept a leaf only if the displayed rational lower bound is at least 604661379/50000000000; otherwise split. The actual exact run exhaustively covered the square with 1249 accepted leaves, 2497 visited nodes, maximum dyadic depth 81. Separate checker independently verified the leaf set is prefix-free and satisfies exact binary Kraft sum 1 (no gaps), reconstructed each dyadic rectangle, and checked every rational leaf inequality. The continuum lower bound therefore covers EVERY real x,y, not a finite sample. The generated certificate file CERT_STAGE306B_DYADIC.json has 59870 bytes and SHA256 7a048d9bbe3502b5f6a1589bc8426638521d8401305bc0e68f45457193763466.

The executable program REPRO_STAGE306B.py generates the full certificate deterministically. VERIFY_STAGE306B_CERT.py reads the generated JSON and independently verifies its complete cover and all bounds. Actual stdout files record STAGE306B_EXACT_PASS and INDEPENDENT_STAGE306B_DYADIC_CERT_VERIFY_PASS. The generated plain JSON can be recreated from the archived source and does not require a numerical solver.

## Lemma 306.3: strict third-moment no-go

If a two-atom mixture (1-u)δ_a+uδ_b with nonzero variance and another (1-α)δ_x+αδ_y have the same first three raw moments, their standardized third centered moment must coincide. In an oriented two-atom distribution it is (1-2u)sign(b-a)/sqrt(u(1-u)), strictly monotone in u for a fixed orientation. Therefore either α=u (preserving atom order) or α=1-u (reversing it). The outer fibers require u=1/10 but α=1/5, so there cannot be EXACT three-visit public equality for any real locked rates. Compactness of [0,1]^2 separately proves the minimum is positive. The dyadic computation supplies its tight quantitative bounds.

## Theorem 306.4: original source/J joint audit

When the terminal observer can additionally read both original S and persistent J, the risk for ONE future F visit is the weighted absolute-deviation sum over original strictly positive branches,

sum_{s,j,w,y} w(s,j,w,y) abs[p_s-t(j,w,y)].

For each fixed h=(j,w,y), its independent minimizer is p0 or p1 according to the larger source weight. The weighted median identity gives minimum (p1-p0)min(w0h,w1h). Exact summation over eight h gives sum_h min(w0h,w1h)=7/64. The exact one-F joint-audit minimax is therefore 7/128. Projection from three F visits onto the first F establishes every locked-rate three-visit implementation has joint-(S,J)-audit risk at least 7/128. This is NOT an assertion that the three-visit tagged optimum equals 7/128; that larger-horizon value and the joint/public Pareto tradeoff remain open.

These two observer scopes differ mathematically: public three-F risk can reach approximately 0.007558267238, while a terminal examiner who reopens original S and J necessarily detects at least 0.0546875 risk. Public pooling alone cannot certify preservation of the hidden source-label relation.

## BRC applicability, evidence and next problem

The relevant BRC typed interface is finite positive rational branch accumulation with retained provenance/multiplicity before a declared observer quotient (definition blob f375a059fa4af8c6eefaddb4d4a8689a0c063674). The existing positive CWM implementation src/enterprise_math/brc_weighted.py (blob 3f205696709e847909958a153f8fe10d3f6b70f0) is useful for exact positive-mass semantics but its total-only CWM is not sufficient for the present (S,J) or three-moment observers. Reuse: REUSE_APPLIED to the finite BRC branch/observer law; the exact dyadic minimax verifier is external rational RESEARCH_TOOLING, not a native BRC physical execution or a newly accepted reusable tool. No signed phase cancellation, pi, trig, native X6 state update or physics is evaluated.

P000 remains unchanged, including six signed chart-relative native axes, independent time, primitive one-axis steps, triadic E closure, explicit three-dimensional slice and lossless six-field final Cell addressing. A typed native X6/BRC commuting map has not been proved. Site configuration observed research_authority_granted=false; control owner list returned CONTROL_QUOTA; no live CLAIM, native Result, independent Driver review or admission is asserted.

**Stage307-B handoff:** Find a rigorous real-algebraic global minimizer, checking whether both k=0 and k=1 residuals vanish at it; provide a Sturm/resultant isolating certificate or a counterexample. Separately compute the exact three-visit (S,J) terminal-audit minimax and the public/joint Pareto frontier under the SAME locked-rate class. Pursue X6/BRC correspondence only with its explicit native carrier, operations and observers.