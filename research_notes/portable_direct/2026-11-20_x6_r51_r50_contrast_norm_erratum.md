# X6 R51 — R50 correlated-noise contrast correction and exact counterexample to the claimed radius

Date: 2026-11-20 (Asia/Shanghai). Task: RS-X6-NATIVE-TIME-DYNAMICS. Researcher provenance: EM-X6-214D9C, Activity RA-545183ADD4EF71C3E4698AEE. Status: AUTHOR_PROOF / EXACT_RATIONAL_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.

## 1. Object and scope

This is a **scientific correction** to the immutable historical R50 proof (2026-11-20_x6_r50_correlated_error_common_offset_brc.md @ ae0ca414659c48c1a88b0cc10fabb75f8103ba35). It keeps R44–R50's conditional, positive-weight, two-named-source, once-only whole-triad BRC transition grammar; it does not assert a native P000 admission map for candidate release R / reoccupation T.

Let p>=1 be an integer, alpha,beta>0, S=alpha+beta, P=alpha*beta with 4P<=S^2. The four BRC root masses (F,FT,FF,FRF) are
  A_p(S,P) = (pS, (p-1)S, 2(p^2-1)P, 2pP).
An observation z=A_p(S,P)+b(1,1,1,1)+epsilon has arbitrary common real b and |epsilon_i|<=eta.

R50.1 (exact common-bias elimination by the range of four residuals) and R50.4 (finite candidate bound when x-y>2eta) are unaffected. The R50.2 coefficient norm and R50.3 uniform radius are **incorrect**, as shown below. R50's earlier PASS covered a limited test family and did not prove those statements.

## 2. R51.1 — correct exact contrast and sharp noise envelope

For any candidate q>=1, put C_q=q^2-q-1 and
  L_q(z)=(d-h)-C_q[(x-y)-(x-h)/q].
For z in order (x,y,d,h), direct expansion gives coefficients
  (-C_q(1-1/q), C_q, 1, -1-C_q/q).
In particular, the h coefficient is **-1-C_q/q**, not the R50.2 paper's C_q/q-1. The R50 verification script likewise took abs(C_q/q-1) instead of abs(-1-C_q/q).

The exact l1 coefficient norm is
  N_q = 2                            if q=1,
        2q(q-1)=2(C_q+1)             if q>=2.
Every feasible q has |L_q(z)|<=eta*N_q, and this bound is sharp for independent errors in [-eta,eta]^4: choose each error sign to match its coefficient. The common additive bias cancels because the four coefficients sum to zero. The exact model satisfies L_q(A_q(S,P))=0.

A concrete refutation of the previous bound is q=2, eta=1, with epsilon=(-1,+1,+1,-1). Then L_2(epsilon)=4, whereas R50.2 asserted N_2=3. At q=3 the true norm is 12, not 10. This is an implementation and algebraic coefficient error, not a physical residual.

The exact identity from R50 remains valid:
  L_q(A_p(S,P)) = (p-q)/q * [S*C_q + 2P*(pq+1)].
For q>=2, C_q>0; it is nonzero for q!=p.

## 3. R51.2 — exact positive-weight counterexample to the old R50.3 radius

The R50.3 hypothesis for p>=2 claimed eta<min{S/[4(p+1)], C_p P/2} rules out every competing integer q. It does not.

Take the true model
  p=4, alpha=99/100, beta=1/100,
  S=1, P=99/10000,
  A_4=(4,3,297/1000,99/1250), b=0.
The R50.3 claimed threshold equals min{1/20, (11*99/10000)/2}=1/20.

Take a competing q=5 model with
  S'=161/200, P'=1/100, A_5=(161/40,161/50,12/25,1/10),
  b'=-301/2500.
Its source weights are the two positive real roots of u^2-(161/200)u+1/100=0; the discriminant is positive.

Choose the same measured vector for both models:
  z=(39523/10000, 15249/5000, 3283/10000, 147/5000).
For the true model the four measurement errors are
  (-477/10000, +249/5000, +313/10000, -249/5000);
for the rival with bias b', the errors are the opposite four values.
All eight errors have magnitude <=eta=249/5000=0.0498<0.05=1/20.
Thus distinct Port counts 4 and 5 are both exactly compatible *inside* the claimed R50.3 radius. This refutes that universal assertion under its own hypotheses. No floating-point reasoning is involved.

## 4. R51.3 — a valid uniform sufficient identification radius

**Theorem.** For the same conditional four-channel model and all positive alpha,beta and arbitrary b, every eta-accurate observation admits no other integer Port count if
  p=1: eta<P/2;
  p>=2: eta<min{ S/[8(p+1)], (p^2-p-1)P/2 }.

**Proof.** For p=1 the exact e=D-H=-2P<0, whereas every q>=2 has e_q=2C_q P_q>0. Two error boxes of radius eta produce e intervals of radius 2eta; eta<P/2 strictly separates them.

For p>=2, actual e=2C_pP>0; the second bound strictly separates q=1's negative e from every allowed actual observation.

It remains to exclude each q>=2, q!=p. From the identity above,
  |L_q(A_p)|=|p-q|/q*[S C_q+2P(pq+1)] >= S*C_q/(p+1),
since |p-q|/q>=1/(p+1). If some observation z were within eta of both the true p model and a q model (each allowing its own common bias), then by the exact linear norm,
  |L_q(A_p)|<=2eta*N_q=4eta(C_q+1).
But eta<S/[8(p+1)] makes the RHS strictly less than S(C_q+1)/[2(p+1)] <= S*C_q/(p+1), since C_q>=1. Contradiction. QED.

This is a **sufficient** corrected radius, not claimed optimal. The R50.1 exact semialgebraic feasibility test remains the reference when the larger instance-dependent range matters. The old S/[4(p+1)] radius must not be cited as a theorem.

## 5. Reproducible verification and future work

Companion source: research_notes/portable_direct/x6_r51_correlated_error_erratum_verify.py.
Companion exact output: research_notes/portable_direct/x6_r51_correlated_error_erratum_results.json.
The Fraction verifier checks the corrected coefficient identities/norm and sharpness at all 16 noise-box vertices for q=1..30, validates both positive-weight models and their single shared measured vector exactly, and checks 1,404 rival-Port contrast exclusions in p=1..9, four positive weight pairs and q=1..40 at one-third of the new stated sufficient radius. General validity is proved symbolically above.

Further questions: the **optimal** simultaneous-error identifiability radius for each actual (p,S,P), including ties at the boundary; short finite q elimination when x-y<=2eta; and whether the R/T conditional graph embeds as a genuine frozen-P000 TRIADIC_CLOSURE_E Cell/Link/Port trace system. Native physical correspondence and independent review remain open. Preserve earlier immutable R50 evidence as a historical author result and mark the affected claims explicitly rather than silently altering their original content.
