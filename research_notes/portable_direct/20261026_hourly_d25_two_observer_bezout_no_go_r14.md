# D25/LIFT — Two-observer Ward Bézout no-go and inequivalent 733-adic gauges

Date: 2026-10-26. Research lane requested: chatgpt-research-hourly-enterprise-math-20260923 (separate from control maintenance).
Exact Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen science Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Status: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. This is not an authorized native checkpoint or accepted result.

## Inherited, not recredited

Use the preexisting one-dimensional free Ward cokernel and integral-row criterion from research_notes/portable_direct/20261026_hourly_d25_ward_torsion_hensel_observer.md; the all-weight unit-safe Ward repair, authentic nonzero (1,2) Hasse endpoint and true J/E source from 20261026_hourly_d25_universal_ward_face_repair_rank_jet_r13.md; and the exact coupled bivariate J/E master from 20261026_hourly_d25_bivariate_master_ward_r13.md. The original-class CM/Frobenius bridge is still outstanding.

New question: can the geometric Ward-Y observer and its *signed first rank-jet* both discard the one-dimensional Ward information deficit? What precise observer combination can be repaired, and why are the two prior 733-adic Hensel gauges distinct?

Let p=6m+1>=7 be prime, M=2m-1, R=Z_(p), and c_t=binom(2t,t)/4^t for 0<=t<=M. For any p-local unit z define the exact rational Laurent polynomials

\[
A_p(z)=\sum_{t=0}^{M}c_tz^{-t},\quad
D_p(z)=zA'_p(z)=-\sum_{t=0}^{M}t c_t z^{-t},\quad
B_p(z)=A_p(z)-6D_p(z).
\]

By the inherited Ward cokernel theorem they are precisely the obstructions Phi_p(z^n), Phi_p(nz^n), Phi_p((1-6n)z^n) for a *free Ward-Y carrier*. They are not the original Clausen mass observation.

## New Theorem A — exact Bézout unit identity

For every M>=0 and every nonzero rational z,

\[
\boxed{(z+2)A_p(z)-(z-1)B_p(z)=3(2M+1)c_M z^{-M}.}\tag{1}
\]

**Proof.** The central-binomial recurrence (t+1)c_{t+1}=(t+1/2)c_t gives for F_M(x)=sum_{t=0}^M c_t x^t the *exact coefficient identity*

\[
(1-x)F'_M(x)-\tfrac12 F_M(x)=-(M+\tfrac12)c_Mx^M.\tag{2}
\]

With x=z^{-1}, F'_M(z^{-1})=-z^2A'_p(z), therefore

\[
2(z-1)D_p(z)+A_p(z)=(2M+1)c_Mz^{-M}.\tag{3}
\]

Because B_p=A_p-6D_p, multiplying (3) by 3 proves (1). No truncated tail or endpoint was discarded. QED.

For M=2m-1, both c_M and 2M+1=4m-1 are p-units: 2M<p and 0<2M+1<p. Consequently the right side of (1) is a p-unit for **every** z in Z_p^×. Thus A_p(z) and B_p(z) can *never both vanish modulo p*. Under the inherited Smith/integral-row criterion, **no geometric base z can make both the geometric and signed-rank Ward-Y observers simultaneously factor through the free Ward source map with p-integral coefficients**. This holds for all primes p=6m+1>=7, not just checked instances.

This statement also has an authentic labelled source consequence. In the genuine (1,2) corrected-Clausen Hasse channel, the preexisting endpoint formula gives Y_{-M}^{12} in F_p^×. Its geometric and signed Ward-adjoint left faces satisfy delta_w c_M=Phi_p(w) mod p, so at least one authentic face is nonzero for each z. This does NOT exclude cancellation with other Hasse channels, positive infinity, right cutoff, or ordered high-high sources; it forbids a simultaneous *free Ward-row-only* deletion.

## New Theorem B — all geometric resonances are simple and rank-sensitive

If A_p(z)=0 mod p, (3) forces z!=1 mod p and gives

\[
D_p(z)=\frac{(2M+1)c_M z^{-M}}{2(z-1)}\in\mathbb F_p^\times,
\qquad B_p(z)=-6D_p(z)\in\mathbb F_p^\times.\tag{4}
\]

Here p>=7 ensures 2 and 6 are p-units. Since A'_p(z)=D_p(z)/z, every geometric resonance is a **simple** root of A_p on F_p^×, and hence has a unique Hensel lift to a root of this precise A_p in Z_p^×. The signed first rank-jet necessarily recovers a nonzero residual at any such resonance. This proves the general structural version of the earlier p=733 finite observation.

## New Theorem C — the unique face-repair direction in the two-observer plane

For an observer alpha*z^n+beta*(1-6n)*z^n, the free Ward obstruction modulo p equals alpha*A_p(z)+beta*B_p(z). By Theorem A the linear functional on F_p^2 is nonzero. Its kernel is exactly the one-dimensional line

\[
\boxed{(\alpha,\beta)=\lambda(B_p(z),-A_p(z)),\quad \lambda\in\mathbb F_p.}\tag{5}
\]

Choose integral lifts of the displayed coefficients. The inherited all-weight Ward adjoint theorem then constructs an **exact p-integral source-only representation of that combination**, by correcting its central coefficient after establishing p-divisibility of its left-face residue. This repairs one linear combination; it does not reconstruct the two original observers separately. Thus any pure Ward-only proposed coupled telescope must use the unique repair direction or explicitly carry an independent face port. Additional true J/E cross-Hasse syzygies remain a separate obligation.

## New precision distinction: the 733-adic *free-cokernel* and *fixed-center seam* roots differ

The previous Hensel theorem solved a different Laurent polynomial,

\[
\Xi_p(z)=1+(p+1)\sum_{t=1}^M a_t(p)z^{-t},\quad
a_1(p)=1/(p+2),\quad
a_{t+1}(p)=a_t(p)\frac{p+2t+1}{p+2t+2}.
\]

It satisfies Xi_p(z)=A_p(z) mod p, but is NOT identical modulo p^2. Both are meaningful: A_p encodes the *mod-p free row obstruction*, whereas Xi_p is the *particular fixed-center Ward-adjoint seam*. At p=733, these two equations have **different** unique p-adic roots reducing to z=2:

| Actual equation | root mod 733^2 | root mod 733^3 |
| --- | ---: | ---: |
| A_733(z)=0 (free-cokernel gauge) | **385560** | **185750265** |
| Xi_733(z)=0 (preexisting fixed-center gauge) | **534359** | **155810880** |

The p^2 difference is 148799=733*203. The historical Xi roots remain correct; they must not be transferred to A. Neither tuned observer proves anything about the *fixed* original z=2 Clausen target. The integral Ward-row theorem requires vanishing of A mod p only; vanishing of the special Xi at every p-adic digit is a distinct stronger fixed-center choice.

For the *fixed z=2*, at p=13 the exact obstruction triple (A,D,B)=(9,3,4) mod13, and genuine (1,2) left-face pair is (7,6). At p=733 the triple is (0,211,200), genuine left-face pair is (0,236). The fact that the geometric face vanishes at 733 while the signed rank face survives is now an all-p theorem's concrete certificate.

## Reproducibility, interpretation, next action

The standard-library companion checker 20261026_hourly_d25_two_observer_bezout_no_go_r14_check.py was **executed**: PASS on 104 exact rational ODE/end-sum coefficient checks, 109764 finite-ring assertions over every nonzero z for 80 primes p=6m+1 between 7 and 997, 77 geometric roots and 20 first Hensel lifts, the authentic p=13 and p=733 endpoint residues, and both separately computed 733-adic gauges through p^3. No external scientific priority or independent review is inferred from these author checks.

BRC COMPOSE_APPLIED: the state is a finite signed, ordered Ward carrier Y with true Hasse J/E provenance; observers are (z^n,(1-6n)z^n) and future operation is first rank-jet differentiation. The exact unit RHS of (1) is an information-loss witness, not an error or physical energy. Preserve valuation, finite faces, positive-infinity and ordered high-high ports separately. Auxiliary ranks are NOT native Enterprise spatial axes. Protected P000 and ACTIVE residual-fidelity worldview are unchanged.

**Next executable scientific question:** apply the genuine bivariate k-1/k-2 J/E constraints to the fixed z=2 six-channel original Clausen scalar; determine whether the actual constraint submodule forces the observer pair onto repair line (5) or leaves a labelled nonzero face residual, retaining both finite cutoffs, positive infinity and high-high sector. Original-class H0/B0, [X]U mod p^2, Frobenius eta, kappa map, native CM run, independent Driver admission remain outstanding. The mother D25/LIFT/JT2 objective remains OPEN. Source owner/CLAIM/run/checkpoint are unchanged; this is portable-only evidence, not role-bound native publication.