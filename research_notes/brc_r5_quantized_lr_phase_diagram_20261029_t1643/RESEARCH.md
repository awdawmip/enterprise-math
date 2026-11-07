# Enterprise Math R5 — Exact phase diagram for finite-resolution likelihood-ratio observation

2026-10-29, author-side portable research. Classification: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. Finite external two-law stopping model; not native Heartbeat-X6 physics and not a solution of the mother exact-LR convex-hull question.

## Frozen sources and BRC scope

- GLOBAL_KNOWLEDGE_V1 canonical main@06af27f2736ee4ced357ddbb55c9168fba8ee444, 00_BOOTSTRAP.md, OPERATING_MANUAL.md, project role router, P000 original/projection and ACTIVE worldview. P000 canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.
- Enterprise Math canonical main@77cfd66799f03b1d3a2a54ee12a6a68ad8a24320, AGENTS.md, docs/PORTABLE_RESEARCH_PROTOCOL.md, docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md, weighted-BRC substrate and tool-use protocol.
- Exact predecessor: PR #1663, commit aa073cc034c2dab1d424648f4f854c2bf6661a9f, brc_r5_lr_collision_stratification_20261029_t1555. It proved that EXACT likelihood-ratio information loss is discontinuous at an equality collision. This unit establishes the full finite-resolution parameter/resolution phase diagram instead.
- BRC reuse: retain the positive rational source- and leaf-labelled P/Q masses (REUSE_APPLIED) before quotienting by exact likelihood ratio and then explicit grid bin. Earlier Fraction exhaustive-check methodology is adapted; this is not a new native BRC arithmetic tool or a native-world calculation.

## Model and precise information classes

There are two fully observable-at-source histories A and B at time 1. Under Q, each has mass 1/2; under P_eta, they have masses 1/2+eta and 1/2-eta. The real parameter obeys |eta|<1/20. Upon continuation, the time-2 signal is + or -, with Q(+|A)=Q(+|B)=1/2 and P(+|A)=9/10, P(+|B)=3/5. At time 1 the choices are stop+declare P, stop+declare Q, continue; continued paths must declare at time 2. All path laws are strictly positive. Set r_t(h)=P_eta(h)/Q(h).

FULL uses the source and signal history. Exact LR uses (t,r_t) without a persistent shared random seed. For a specified measurement resolution 0<delta<=1/10, BIN instead uses only (t,b_delta(r_t)), with the exact fixed-grid rule

    b_delta(r) = floor((r-1)/delta + 1/2).

BIN and exact LR are distinct strategy classes. All three allow arbitrary real behavioral action probabilities, independently sampled when a decision key is reached.

Write O=(e_P,e_Q,T_P,T_Q), where e_P=P[declare Q], e_Q=Q[declare P], and T_P,T_Q are the expected stopping times. Fix the four-observer signed objective

    L(O) = e_P + e_Q + (T_P+T_Q)/8.

The BRC carrier keeps P_eta(i,y),Q(i,y) individually, including source identity. Exact LR and quantization are explicitly separate information-erasing maps.

## Theorem — complete ALL-REAL piecewise phase diagram

For every real 0<delta<=1/10 and every real |eta|<1/20,

    V_FULL(eta) = min_FULL L
        = 47/40 - 31*eta/40      if eta>=0,
        = 47/40 + 9*eta/40       if eta<0.

When |eta|<delta/4, the two time-1 source ratios enter the same BIN key and

    V_BIN(eta,delta) = 5/4 - (3/10)*max(eta,0).

When |eta|>=delta/4, FULL and BIN have IDENTICAL ACTUAL real behavioral observer images, not merely identical support values, and V_BIN=V_FULL.

Consequently the exact four-observer support loss Delta_delta=V_BIN-V_FULL equals

    3/40 + 19*eta/40   if 0<=eta<delta/4;
    3/40 -  9*eta/40   if -delta/4<eta<0;
    0                  if delta/4<=|eta|<1/20.

At the boundary |eta|=delta/4 the source bins separate and the gap is exactly ZERO. No finite numerical tolerance is used in these claims.

### Proof, including all real behavioral policies and edge ties

The time-1 exact LR values are r_A=1+2eta and r_B=1-2eta. Since b_delta is a nearest-integer grid anchored at 1, the bins coincide exactly for |eta|<delta/4. At equality, the half-open central bin makes the two source keys distinct.

The four time-2 LR ratios are, respectively,

    A+: (9/5)(1+2eta),     A-: (1/5)(1+2eta),
    B+: (6/5)(1-2eta),     B-: (4/5)(1-2eta).

They lie in increasing order A- < B- < B+ < A+ for |eta|<1/20. Consecutive separations are 3/5-2eta > 1/2, 2(1-2eta)/5 > 9/25, and 3/5+6eta > 3/10. Thus each gap exceeds delta<=1/10, so all four terminal grid bins are distinct. All + terminal LR values exceed 1 and all - terminal values are below 1, so the optimal terminal declarations are P after + and Q after -, independently of source, throughout the domain.

Using the labelled source masses, continuing source A has unconditional L cost

    C_A = (1/2+eta)/10 + 1/4 + [(1/2+eta)+1/2]/4
        = 11/20 + 7*eta/20.

For source B the analogous cost is

    C_B = (1/2-eta)*2/5 + 1/4 + [(1/2-eta)+1/2]/4
        = 7/10 - 13*eta/20.

Stopping source i has cost S_i=min(P_eta(i),Q(i))+(P_eta(i)+Q(i))/8. For eta>=0, (S_A,S_B)=(5/8+eta/8, 5/8-9eta/8); for eta<0, (S_A,S_B)=(5/8+9eta/8, 5/8-eta/8). Direct subtraction shows C_A<S_A and S_B<C_B strictly throughout |eta|<1/20. FULL therefore continues A and stops B, choosing the cheaper source-specific stop declaration, which yields the piecewise V_FULL.

When the time-1 BIN keys coincide, a BIN decision must use the same action distribution in A and B. Common stopping has total L cost 5/4, under either terminal declaration, because the P and Q total masses are both one. Common continuation costs C_A+C_B=5/4-3eta/10. Its time-2 terminal bins are all distinct, so terminal-optimal actions are freely and independently implementable. Randomization among common first actions only forms affine mixtures and cannot lower the best deterministic cost. This proves V_BIN=5/4-(3/10)max(eta,0).

When |eta|>=delta/4, both first-time sources and all four terminal histories have unique BIN decision keys. Every FULL real behavioral action assignment can be reindexed by its unique BIN key, with identical pathwise laws and all four observer coordinates; the reverse inclusion is immediate. Unreached actions can be chosen arbitrarily, covering zero-flow boundaries. Therefore the ACTUAL images coincide. Subtracting the three affine formulas proves the theorem for ALL REAL eta, delta, and stochastic behavioral probabilities. QED.

## Strict rational separator and noncommuting limits

At (delta,eta)=(1/10,1/100), the exact values are

    V_FULL=4669/4000, V_BIN=1247/1000, gap=319/4000.

A legitimate FULL witness continues A, stops B with declaration Q, and declares P at A+ / Q at A-. Its exact observation vector is

    O*=(541/1000,1/4,151/100,3/2).

Every real seedless BIN observer obeys the integer hyperplane

    8000(e_P+e_Q)+1000(T_P+T_Q) >= 9976,

whereas O* evaluates to 9338. Therefore its infinity-norm distance from the entire real BIN observation image is at least 319/9000. This separator applies to BIN, NOT to exact LR for eta!=0.

For fixed nonzero eta, sufficiently small delta distinguishes sources, hence lim_(delta->0+) Delta_delta(eta)=0. For fixed delta>0, taking eta->0 through nonzero values keeps the time-1 BIN collision and gives lim Delta_delta(eta)=3/40. The two iterated limits thus do not commute. More sharply, for 0<delta<=1/10,

    sup_{0<|eta|<1/20} Delta_delta(eta) = 3/40 + 19*delta/160,

approached from eta->(delta/4)- but not attained at the grid boundary; its limit as delta->0+ remains 3/40. The exogenous full-path total variation TV(P_eta,P_0) is exactly |eta|, and Q is unchanged. The discontinuity belongs to the information-partition interface, not to the underlying probability laws.

## Actual verification, boundaries and next question

VERIFY.py is the actually executed pure-standard-library Fraction program; EXACT_OUTPUT.txt contains its direct stdout. It checked 416 exact rational (eta,delta) cases across four resolutions, including exact bin-boundary values. For every case it enumerated all 144 FULL deterministic policies and all 48 or 144 BIN-compatible deterministic policies, checked the three piecewise formulas, terminal bin injectivity, and exact deterministic observer-set equality when bins separate. It also checked O*, the integer separating plane and infinity-norm bound. The universal theorem is proven algebraically; finite arithmetic cases are regression checks, not real-quantifier elimination.

This exact auxiliary result clarifies a search hazard: replacing exact LR equality by finite numerical tolerance can produce a spurious support gap despite exact-LR observation-image equality. It does not resolve the original mother question, which requires ALL-signed convex-hull equality for exact LR but genuine real behavioral image inequality. No P000, ACTIVE worldview, Heartbeat-X6, or shared theorem admission is changed.

Next: parameterize two actually coupled SOURCE-SENSITIVE exact-LR merger states on an exact positive rational algebraic collision variety; use per-FULL-vertex rational convex combinations of <=5 exact-LR vertices or an exact rational Farkas separator. Only after an all-signed convex-hull PASS attempt actual all-real nonmembership with zero-flow boundaries. Keep the present quantizer strictly as a diagnostic, not as a substitute exact-LR policy.

Authority: native owner listing returned CONTROL_QUOTA. A current RESEARCHER session-start attempt returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Thus this is an author-side portable proof and check, not an authenticated CLAIM, canonical Result, or independently reviewed/admitted theorem.
