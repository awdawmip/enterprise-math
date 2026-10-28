# D25/LIFT GH-63/GH-64: resonant-gate syzygy and terminal-blind chart classification

Date 2026-10-29, Asia/Hong_Kong. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Own logical Research lane chatgpt-research-hourly-enterprise-math-20260923, not maintenance chatgpt-hourly-enterprise-math-20260921. These are PORTABLE author claims, not native Source checkpoint, CLAIM/run, Result or review.

## Input and GH-63 theorem

Let p=8m+3>=11 be prime, k=F_p, F(z)=sum_{r=0}^m (-m)_r² z^r/((2m+2)_r r!), and G(z)=16zF'(z)+5F(z). The inherited exact Gauss operator is L=A(z)∂²+B(z)∂-9/64, A=z(1-z), B=(5-7z)/4, with LF=0. At any a in k without {0,1}, set w=z-a. For any initial data (u,v), GH-61/62's degree-(p-1) jet J has LJ=-C_a w^(p-2)-D_a w^(p-1), with separate first and terminal resonant residuals. The joint kernel was proven to be the F solution line.

Define the new polynomial H(z)=4z(1-z)F'(z)+(1+z)F(z).

**Theorem GH-63.** For every eligible p, a and (u,v), including charts at roots of F,

\[
\boxed{H(a)C_a+4a(1-a)F(a)D_a=0.}\tag{63.1}
\]

**Proof.** Set q=z^(-2m-2)(1-z)^(4m+1), so q'/q=-B/A. For W=FJ'-F'J, exact reduction of order gives (W/q)'=F(LJ)/(Aq). Write K=F/(Aq), and inspect the coefficient of w^(p-1). Every formal derivative has zero coefficient there in characteristic p. The right-hand coefficient is -C_a K'(a)-D_a K(a). Since B-A'=(1+z)/4,
K(a)=F(a)/(A(a)q(a)) and K'(a)=H(a)/(4A(a)²q(a)).
Multiplying by 4A(a)²q(a), a unit, proves (63.1) without dividing by F(a).

At F(a)!=0 the inherited first gate C_a has rank one, so

\[
\boxed{D_a=-H(a)\,C_a/[4a(1-a)F(a)].}\tag{63.2}
\]

In particular the terminal gate is zero for **every** initial pair precisely when H(a)=0. At F(a)=0, GH-62 proves instead C_a=0 and D_a rank one. Thus the earlier GH-59 terminal-only selector requires a nonzero functional; the two-gate criterion remains uniform. The earlier p=43,a=6 counterexample is explained by H(6)=0, rather than being recredited as new.

## GH-64: global H derivative and exactly m+1 geometric blind charts

**Theorem.** In k[z],

\[
\boxed{H'(z)=25F(z)/16.}\tag{64.1}
\]

Indeed, differentiate H, use AF''=-BF'+9F/64, and observe -4B+4A'+1+z=0, leaving (1+9/16)F. This exact identity implies the following geometric count.

The leading coefficient of H is (1-4m)[z^m]F=(5/2)[z^m]F, a unit, hence deg H=m+1. Also H(0)=1 and H(1)=2F(1)!=0; here F(1)=(3m+2)_m/(2m+2)_m is a unit by the terminating Chu–Vandermonde identity. GH-61 proves that every root of F is simple and outside 0,1. At a root r of F, H(r)=4r(1-r)F'(r)!=0, so gcd(F,H)=1. Combining this with H'=25F/16 shows gcd(H,H')=1: **H has exactly m+1 distinct roots over an algebraic closure**. They are all outside 0,1 and F-roots. At each, D_a vanishes identically by (63.1). The first gate remains rank one over a scalar extension because the GH-61 Cartier obstruction coefficient becomes -D_m²/a^p, still nonzero. Some blind charts are not F_p-rational, and no full splitting assertion is made.

**Target-point corollary and falsifier.** At a=9, H(9)=2(10F(9)-G(9)), hence the division-free exact relation

\[
\boxed{144F(9)D_9=(10F(9)-G(9))C_9.}\tag{64.2}
\]

If the open target G(9)=0 holds, then F(9)!=0 (a zero would be simple with G(9)=144F'(9)!=0), and D_9=(10/144)C_9 as **nonzero** rank-one functionals. Conversely, **any** eligible p with D_9 identically zero as a functional is an exact counterexample to G(9)=0: the F-root case has nonzero D, while the nonroot case implies G(9)=10F(9)!=0. This is a new falsification condition, **not** the all-prime arithmetic proof.

## Exact checker, BRC and continuation

Companion independent integer finite-field program (same folder) was executed for all 76 primes 11<=p<2000 with p=3 mod8, 304 charts (a=2,9,-1,6) and three basis/test initial pairs each, 912 comparisons; coefficient-wise H'=25F/16 for all primes; 40 rational blind charts for primes p<1000 (each with rank-one first gate and identically zero terminal gate); and the exact inherited p=43,a=6 witness. All tests PASS. These finite computations corroborate the symbolic proof, not independent review or original native H0/B0 execution.

BRC COMPOSE_APPLIED: retain p, original indexed F/G provenance, observer chart a, two independent initial-data variables, separate first/terminal residues, full-jet vs formal-solution distinction and future differentiation. H precisely marks loss of terminal-only information. This auxiliary k[z] chart is NOT a native X6 three-dimensional slice, native Hasse/Green, W/S or physical observer; P000 unchanged.

Next exact science: independently evaluate G_m(9) for all primes p=11 mod24 by CM/Katz/finite-character source, or search for a target-chart terminal-blind counterexample. Preserve original GH-3, GH-20/21 next digit, six Hasse, W/S, R23/R36, eta/kappa and p=373 original native H0/B0. At 2026-10-29 00:20+08, the Sites gateway 0.6.11 returned research_authority_granted=false, executor_binding_configured=false, source_sync.control.state=CODE_REVIEW_REQUIRED, active_jobs=5/5; callable recovery_status was not exported by this connector. No session, CLAIM, open, Source checkpoint, Result, HANDOFF or Driver review was performed. Old session, request and staging untouched; responsible control issue enterprise-math#1558.