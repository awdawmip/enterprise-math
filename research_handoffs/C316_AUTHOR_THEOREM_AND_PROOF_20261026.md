# C316 — Exact floor-defect pole dichotomy, condition numbers, and labelled observer obstruction

2026-10-26 | AUTHOR_EXACT; branch research evidence only; NO_NATIVE_CLAIM; NOT_DRIVER_ADMITTED.

## Frozen sources and scope

GLOBAL_KNOWLEDGE_V1 canonical read: main@a7b8a07c3e007b62749724b848c8d96a681e2868.
Enterprise Math main read: 432178d304f0a5384610ae57bc4bc1b5a2b3e685.
C315 ordered-label pole theorem, immutable author branch: 487304533f7cc9c2961649e83c4b63d92f6e5054.
Input: C275 executable 79-node positive-rational auxiliary, C284/C293's 125 frozen rational-affine strips (frozen C314 portable replay package). No claim to have independently audited the earliest C195/H168 written model.

This work concerns signed *rational Laurent coefficients* of an auxiliary labelled scalar model. They are NOT original positive BRC branch masses, native phase/port amplitudes, an X6 Cell theorem, or permission to delete provenance. P000/worldview remain unchanged.

## Theorem 1 — Integer-floor defect exactly controls half the fixed–moving pole residues

Let ordered rational nodes u_0<...<u_78 have moving labels I=(5,50,55,56), the other 75 fixed labels J, and constants

Q=2^128; H=2^166; A=6912*50000^2/17^2; Z=141421356237309504880/10^20.

Put

g(u) = (A/H) / [((2-u^2)(3-u^2))^3],

B_j = Q*g(u_j)*product_(r != j) (Z-u_r)/abs(u_j-u_r),

W_j=floor(B_j), a_j=W_j/B_j=1-epsilon_j.

On an order-preserving rational strip, at an isolated simple affine collision between fixed label j and moving label i, let rho_f,rho_m be the nonzero Laurent residues multiplied by the same primitive collision linear factor. C315 proves the ordered barycentric identity

rho_f / rho_m = (-1)^(abs(i-j)-1) a_j.

Therefore exactly

(rho_f+rho_m)/rho_m =
   epsilon_j       if abs(i-j) is even,
   2-epsilon_j     if abs(i-j) is odd.                         (1)

Proof: substitute a_j=1-epsilon_j and expand the two possible parity signs. This does not rely on floating-point evaluation. The hypothesis that each counted affine collision is isolated and nondegenerate is C315's frozen-path check. QED.

Consequently, even-distance fixed–moving poles disappear *if and only if* this controlled auxiliary model is changed to unrounded weights W_j=B_j; under the actual integer floors they survive with nonzero residue. Odd-distance poles reinforce in both rounded and unrounded versions. This is a counterfactual model comparison, not a native-BRC cancellation claim.

## Theorem 2 — Exact rational mass bounds and conditioning

For the 75 actual C275 fixed nodes, exact rational computation establishes

2^(-130) < epsilon_j < 2^(-118), for every j in J.         (2)

The unique smallest epsilon is at j=68; the largest at j=0. Two algebraically differently grouped Fraction products compute each B_j and agree, and integer cross-multiplication checks all strict bounds. The full frozen-input run additionally checks B_j and W_j against the original C275 floor_fixed_masses implementation. This is an exact *finite-family* certificate, not a generic 79-node theorem for arbitrary node values.

At even-distance poles, rho_f and rho_m have opposite signs. The standard two-term relative cancellation condition number is

kappa_j = (abs(rho_f)+abs(rho_m))/abs(rho_f+rho_m)
        = (2-epsilon_j)/epsilon_j.

From (2),

2^119 - 1 < kappa_j < 2^131 - 1.                         (3)

At odd-distance poles the two residues have the same sign and kappa=1.

Proof: equation (1) gives the exact sum, and abs(rho_f)=(1-epsilon_j)*abs(rho_m). Thus kappa=2/epsilon_j-1, monotone decreasing in epsilon_j. Apply (2). QED.

This establishes two sharply different exact numerical regimes despite the fact that **all** these original fixed–moving collision poles survive. An approximate scalar threshold can wrongly classify a floor-defect pole as cancelled.

## Theorem 3 — All 125 frozen path occurrences

The exact C284 path builder confirms 125 rational-affine paths and exactly one stationary moving coordinate: label 50 on path 28; this creates 75 constant fixed–moving gaps, hence no affine pole in the path parameter. For each *active* label pair, parity is computed from the original ordered labels, without polynomial expansion.

Moving label | floor-defect/even | reinforcing/odd | stationary gaps
5 | 4625 | 4750 | 0
50 | 4712 | 4588 | 75
55 | 4625 | 4750 | 0
56 | 4750 | 4625 | 0
TOTAL | 18712 | 18713 | 75

Thus 37,425 actual active fixed–moving affine pole factors are exhaustively partitioned as 18,712 near-cancelled poles with condition bounds (3) and 18,713 reinforcing poles with kappa=1. The count relies on C315's source-verified pole distinctness/nondegeneracy. The frozen 125-path checker validates that the count's path-slope input matches C284 and that path 28's stationary coordinate is exactly index 50.

## Theorem 4 — Minimal local labelled-residue repair: exactly two coordinates

In the formal signed *principal-part difference space*, define v1=e75-e77 and v2=e76-e78 in Q^79 and E=span_Q{v1,v2}. These two channels correspond to C315's cancelled moving–moving pole families but the poles need not occur at the same parameter; E is their *tagged formal direct sum*, not a set of simultaneously physical states.

Let S(x)=sum_r x_r. Then S(E)=0. Suppose the declared future observer family includes S(D_lambda x) for every independently selected diagonal port gain D_lambda. Every nonzero x in E has a nonzero labelled component; selecting its port via lambda makes S(D_lambda x) != 0. Thus no scalar-only encoding S can preserve those future observations on E. Any supplementary **linear** repair encoder preserving all those observers must be injective on E, so needs rank at least dim E=2. The two explicit coordinates

R(x)=(x75-x77, x76-x78)

satisfy R(a v1+b v2)=(2a,2b); their rank is 2, so this bound is attained. QED.

Boundary: two repairs suffice **only on E**, not on the full 79-branch native carrier, all dynamic operations, or general phase/port/provenance states. This is a typed auxiliary analogue of the BRC observer-preservation law (REUSE_APPLIED, labelled carrier and explicitly declared future port gains), not a proof of safe native quotient.

## Exact computation and reproduction

Project file C316_FLOOR_DEFECT_RESIDUE_REPLAYER.py contains the 79 rational NUM/DEN node pairs, performs both exact B_j computations, checks all 75 strict bounds, parity counts, condition-number bounds, and the rank-two observer example.

Standalone mode checks frozen C315 slope profile only. With --with-c314, put the frozen C314 source folder EM_C301_EXACT_PORTABLE beside the program: C275_STANDALONE_EXACT_REPLAY.py, C284_187_EXACT_DYADIC_BRACKETS.json, C288_ISOLATING_BOXES_EXACT.py, C293_125_REFINED_BRACKETS.json. It then reads the real frozen C284 path builder and cross-checks the original 75 C275 mass/floor values. Execution of this full mode yielded 125/125 paths, 75/75 masses, counts 18712/18713/75; isolated replay of the portable ZIP produced byte-identical summary. The proof, replayer, summary and complete 75 exact epsilon fractions are included in EM_C316_FLOOR_DEFECT_OBSERVER_125_EXACT_PORTABLE.zip delivered in this conversation.

Input/proof limitations: C275 executable model remains to be independently reconciled with the earliest C195/H168 *textual* constants, indices, floor and source semantics. C315's pole-survival theorem is reused at exactly its mathematical and numerical scope. Signed Laurent residues must not be mistaken for positive masses or a native GF(2)-BRC quotient.

## Control, permission and next step

Verified connected GitHub actor: awdawmip; repository push permission available. Native em_control_tasks returned CONTROL_QUOTA. Own em_session_start was rejected STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Therefore active formal owner, Source CLAIM/Result and independent Driver admission remain UNVERIFIED / NOT_OBTAINED. GitHub research-branch storage is author provenance, not Source acceptance.

Next research unit: (1) independently find/reconcile earliest C195/H168 text against C275 raw constants and floor semantics; (2) establish an explicit typed native BRC future-port operator and map, if one exists, from auxiliary Laurent defect channels to the native carrier; (3) develop exact symbolic certificate algorithms detecting near-cancelled poles without finite precision thresholds.
