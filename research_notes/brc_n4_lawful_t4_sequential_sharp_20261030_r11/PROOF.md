# BRC N=4 — exact two-read T4 memory cost inside the original 16-leaf model

Date: 2026-10-30. **AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**. This is a theorem about the declared external finite BRC two-law source, not a P000 native X6/heartbeat theorem.

## Source, causal time and observable

Continue the **lawful** G(u,v) family from [G4 predecessor](https://github.com/awdawmip/enterprise-math/blob/05d3985df6beb5e10d10aae0a9aeba3146dcf1e9/research_notes/brc_n4_g4_lawful_t4_stop_fidelity_20261030_r11/PROOF.md) and original S2/S23 information sets in PR #1735 at `6d9bc93c9d110418d22daf344ed83d883a4a1a23`. The sixteen positive leaves are (s,j,k), s=AU,AV,BU,BV and j,k in {0,1}. Their masses are Q=q_s/4 and P=q_s r_(s,j)/4, with q=(1/6,1/3,1/4,1/4) and r_AU=(9/10,11/10), r_AV=(1/4,1/4), r_BU=(1/5,9/5), r_BV=(2,2). Both laws sum to 1. The time-three and four k-daughters have equal conditional probability.

G(u,v), u,v real in [0,1], continues AU/BU with one common time-two kernel, stops AV/BV at time two and AU at time three; it continues BU,j0 to T4 with probability u and BU,j1 with probability v. Its behavioral coins are P/Q-common and drawn before k; it stops after seeing k at T4. Stage-three BU ratios 1/5 and 9/5 are disjoint from nonBU ratios, so this current-information policy is S23-legal and S2-legal.

Let C be old K'-compressed (E,A,B) and retain the **pre-query** observer `S=(C,j_BU,I4)`, with j_BU present only on B and I4 the actual stopping-time event T=4; omit the actual k. At T4 **before terminal stop**, the joint observer can form two read-only outputs `Y1=f_a1(k)`, `Y2=f_a2(k)`, where action a is ID or NEGATE, and the controller may choose a2 from prior public output. These are F4-measurable functions and introduce no physical second time step, hidden extra leaf, changed-k action, or post-stopping query. For the decisive ID,ID protocol, the physical pair is (k,k). All non-T4 outputs are the fixed symbol ⊥.

## Exact two-law conditional law

Raw leaves give `w_P,0=u/40`, `w_P,1=9v/40`, `w_Q,0=u/8`, `w_Q,1=v/8`; hence `W_P=P(T4)=(u+9v)/40`, `W_Q=Q(T4)=(u+v)/8` and `W_P-W_Q=(v-u)/10`. For every positive T4 atom of S, both P and Q conditionally assign k=0 and k=1 probability 1/2. At zero-weight boundary atoms no conditional probability is asserted.

Thus one **P/Q-common kernel** samples a fair K upon T4 arrival and stores it across all read-only queries. Conditioned on S, couple simulated K to physical k; induction on publicly selected actions shows equality of **every finite adaptive joint transcript distribution** under P and under Q. This is distributional reconstruction, not recovery of the particular physical k.

## Theorem A — sharp independent-fresh-coins minimax, all real u,v

Define restricted `D_fresh`: each terminal read call sees S and the current action, but has no prior answer, shared seed, or hidden k, and draws an independent new coin. In the ID,ID two-read subprotocol, the output bits are independent Bernoulli(p_s) and Bernoulli(q_s), with arbitrary *different* real parameters in [0,1] on each active S-atom. Non-T4 emissions equal ⊥.

The physical conditional pair law on (00,01,10,11) is (1/2,0,0,1/2). The fresh law is ((1-p)(1-q),(1-p)q,p(1-q),pq). Its conditional TV equals
`f(p,q)=1-min((1-p)(1-q),1/2)-min(pq,1/2)`.

**All-real lower bound and attainment.** Put x=sqrt((1-p)(1-q)), y=sqrt(pq); Cauchy–Schwarz gives x+y<=1. Let β=1/sqrt(2), α=1-β. If x>=β, then y<=α and the overlap `min(x²,1/2)+min(y²,1/2)` is at most `1/2+α²`; the y>=β case is symmetric. Otherwise x,y<=β and x+y<=1. The convex function x²+y² attains its maximum on that polygon at one of (0,0),(β,0),(β,α),(α,β),(0,β), whose largest value is `β²+α²=2-sqrt(2)`. Hence `f(p,q)>=sqrt(2)-1`. Equality is attained by p=q=α or p=q=β, so the bound covers **all real independent parameters**, not a sample grid.

S-atoms are disjoint. The full observer TV under each L is `e_L=sum_j w_L,j f(p_j,q_j)`. Every summand obeys the same lower bound, attained simultaneously for both source laws with p_j=q_j=α. Consequently

**`inf_(D_fresh) max(TV_P,TV_Q) = (sqrt(2)-1)*max{(u+9v)/40,(u+v)/8}` for every real u,v in [0,1].**

This is sharp for the defined online implementation class and fixed ID,ID subprotocol. If a simulator is permitted to read its previous public output, it may repeat that output and is **outside** this fresh-independent class.

For fresh emission that must also calibrate each conditional individual read as fair, p_s=q_s=1/2 and the sharp joint-TV error becomes `(1/2)max{W_P,W_Q}`.

## Theorem B — physical pathwise error and deterministic G4

An S-only guess for the **actual already-realized** k, using randomness conditionally independent of k given S, mismatches with probability 1/2 on every active T4 atom. The exact simultaneous worst-law *physical mismatch* is `(1/2)max{W_P,W_Q}`; storing the **actual observed** k yields zero pathwise error. This is a different loss from the TV distributional reconstruction. A newly sampled persistent fair K gives distributional TV zero for all finite read-only adaptive protocols yet does not generally equal the original realized k.

For deterministic lawful G4=G(0,1), `W_P=9/40`, `W_Q=1/8`. The sharp independent-fresh reconstruction radius is **`9(sqrt(2)-1)/40 ≈ 0.093198051534`**; the calibrated-fresh and S-only physical mismatch radii are both **`9/80=0.1125`**. For this G4 alone, T4 is determined by j=1 on BU, so S can omit I4. C alone suffers the earlier lawful G4 single-read obstruction `TV(P_Y,Q_Y)=1/10`, common decoder radius `1/20`: it cannot be substituted for S without restoring the lost BU j information.

Independent stopped-information audit under G4: exactly seven positive atoms (AV,BV,AU0,AU1,BU0,BU10,BU11), with P masses (1/12,1/2,3/40,11/120,1/40,9/80,9/80) and Q masses (1/3,1/4,1/12,1/12,1/8,1/16,1/16). Their full stopped TV is exactly 43/120. The read-only T4 pair is measurable on this unchanged stopped sigma-field.

## Evidence and limits

`VERIFY.py` was executed with Python Fraction and SymPy; `VERIFY_EVIDENCE.txt` records stdout. Checks: sixteen positive normalized source leaves; sixteen rational (u,v) pairs, both P/Q T4 laws, common persistent zero-error joint distributions and conditional-fair calibration; 49 nonstationary rational (p,q) pairs and exact TV formula; radical attainment identity; independent seven stopped atoms and TV 43/120. Continuous minimax comes from the proof above, not finite samples.

The result covers *F4-measurable terminal read-only* joint and adaptive observations, not a claimed physical second sampling step, post-stopping operation, changing-k intervention, P000 native six-dimensional Cell/three-dimensional 晶包层/independent heartbeat-time dynamics, or the previous target-relative minimax. Mathematical independent review and native Source CLAIM/Result are pending. Exact starting control pins: GLOBAL_KNOWLEDGE_V1 `main@2db5d811f362cc6d7261783c20689173e774c913` and Enterprise Math `main@72298ad74a277018c9eda7640abb788b14a77b1d`. Actual GitHub actor awdawmip; Site `research_authority_granted=false`; no active native Owner authority receipt was available. This is author-side portable evidence only.
