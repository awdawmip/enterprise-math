# R5 — Exact observational fibre for labelled positive P/Q terminal kernels

2026-10-31. Portable author-side mathematical research, not independently reviewed or admitted.

## Frozen inputs, model type, and real authority

Global canonical snapshot: awdawmip/chatgpt-global-knowledge main@4e1e460209864a77964a9ff76e4caa99939081fd. Read both entry files, task-research router, ACTIVE worldview, math and code research policies and BRC priority.

Enterprise Math canonical snapshot: awdawmip/enterprise-math main@92ea1758627b6620538af4acadc1163fd56ef6d8. Read AGENTS.md, full P000, joint-observer preservation and Heartbeat World contracts, AUTONOMOUS_RESEARCH_OPERATIONS and PORTABLE_RESEARCH_PROTOCOL. Global P000_STARTUP projection refers to a different historical EM blob; full current EM P000 was therefore used. P000/ACTIVE worldview were not modified.

Predecessor research: commit 67bde21d6bff1859c3ced8158609b105c6b89c46, research_notes/brc_r5_two_gate_bypass_mccormick_20261031_t0540/RESEARCH.md and NEXT_TASK.md. This finite stopped P/Q experiment is an auxiliary observer model, not native X6 geometry or a physical Heartbeat theorem. The two time coordinates do not define a native 2D plane.

Native research context returned authority_granted=false. Owner inventory returned CONTROL_QUOTA. No verified canonical Owner, Source CLAIM, Result or independent Driver authority is asserted. This is author-side portable work, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

## Exact question

How much source-labelled positive terminal-kernel variation can remain invisible to every FULL and seedless likelihood-ratio (LR) four-observer behavioral strategy in the already verified two-shared-gate/bypass stopping model? Determine the complete positive parameter fibre, the BRC TV-residual range, and whether any of its points repair the predecessor's convex-hull inequality.

## Experiment and symbols

At time zero, Q masses for A0,A1,B,C0,C1 are (1/8,1/8,1/4,1/4,1/4), while P masses are (1/4,1/4,1/4,1/8,1/8). At time one A0/A1 share LR=2 STOP/CONTINUE gate x, and C0/C1 share LR=1/2 gate z. B bypasses time one and reaches time-two Y. Continued A paths can also reach Y (LR=1), a second shared STOP/CONTINUE gate. Y STOP terminates at time two; Y CONTINUE terminates at time three. All non-Y branches from A force termination at time three; C CONTINUE also terminates at three. STOP actions genuinely terminate paths. There is no persistent seed.

The terminal LR labels on continued A branches are R=(1,3/2,2,3) for Y,L,M,H. Each conditional Q kernel K_i must sum to one and have LR moment sum R_j K_i(j)=2; P_i(j)=R_j K_i(j)/2. K_i(Y)=1/4 is fixed. Errors are 1/8 everywhere except B STOP at Y and C STOP at time one (error 5/8). Every terminal error is interior to (0,1). Observers are v=(eP,eQ,TP,TQ).

FULL policies have seven independent real decision probabilities (x0,x1,u0,u1,uB,z0,z1), all in [0,1]. Here x,z mean CONTINUE at time one, while u means STOP at Y. Seedless LR policies obey x0=x1=x, u0=u1=uB=u, z0=z1=z. Histories are remembered only by FULL, not by an external seed supplied to LR.

## Theorem A: full positive kernel-fibre classification

For either source independently, every strictly positive kernel obeying the preceding constraints is uniquely of the form

    K(ell) = (1/4, ell, 1/2 - 3*ell/2, 1/4 + ell/2),
    0 < ell < 1/3.

Proof. Let L=ell. The sum and LR moment constraints, after subtracting the fixed Y contribution, read

    L+M+H=3/4;
    3L/2+2M+3H=7/4.

Solving gives M=1/2-3ell/2 and H=1/4+ell/2. Strict positivity is equivalent to 0<ell<1/3. Hence all Q and P chance transitions are strictly positive and individually normalized. In particular, Y conditional Q mass is 1/4, Y conditional P mass is 1/8, and the combined forced L/M/H masses are 3/4 under Q and 7/8 under P. QED.

## Theorem B: constant entire real behavioral images

For ANY ell0,ell1 in (0,1/3), the actual FULL four-observer image and actual seedless LR four-observer image are separately identical as sets to the predecessor's ell0=1/12, ell1=1/6 images. Consequently their convex hulls, support functions and affine ranks are identical over the entire continuous two-parameter fibre.

Proof. From any continued A origin, the only decision-bearing future label is Y, with fixed P/Q chance mass by Theorem A. Every other label L/M/H gives precisely the same time-three stopping reward and the same 1/8 terminal error; their TOTAL P and Q masses are fixed. Therefore each origin's P/Q expectations of each of the four observables are unchanged for EVERY real-valued behavioral choice. The LR collision equivalence classes and allowed decision keys are also unchanged. Taking images over the two fixed policy domains establishes equality of both actual images. Taking convex hulls or maximizing linear functionals preserves the equality. QED.

Independent of ell0 and ell1, the exact all-real observer map is

    x=(x0+x1)/2; z=(z0+z1)/2;
    w=(x0*u0+x1*u1)/2; s=uB/4+w/16;
    eP=1/8+uB/8+(1-z)/8;
    eQ=1/8+uB/8+(1-z)/4;
    TP=3/2+x+z/2-s;
    TQ=3/2+x/2+z-s.

LR has the extra exact nonlinear relation w=x*uB=x*u. The affine four-observer coefficient columns for x,uB,z,w have determinant 1/2048 (see VERIFY.py), so rank remains FOUR. The seedless LR actual image is nonconvex: the FULL-reachable midpoint

    M=(5/16,7/16,59/32,51/32)

lies in conv(LR_actual) but not in LR_actual, with the inherited valid all-real distance lower bound 1/1520. The exact signed observable

    H=14eP-19eQ+2TP-4TQ

still has sup_FULL H=-13/2 and sup_LR H=-53/8, hence Δ=1/8>0 for ALL ell0,ell1 in the positive fibre. Therefore no kernel-only adjustment in this complete family can meet the mother problem's four-dimensional hull-equality requirement, although the LR image is nonconvex and has full affine rank.

## Theorem C: large hidden BRC residual with identical outputs

The precise source-labelled conditional Q total variation is

    TV(K(ell0),K(ell1)) = 3*abs(ell0-ell1)/2.

With strict positivity its attainable range is exactly [0,1/2), and each such value occurs with ALL four-observer FULL and LR images exactly unchanged.

Proof. The signed difference is (0,d,-3d/2,d/2), d=ell0-ell1. Sum the four absolute entries and divide by two. For any real v in [0,1/2), the explicit positive choice

    ell0=1/6-v/3; ell1=1/6+v/3

has TV=v. Theorem B supplies unchanged observer images; none of this is an asymptotic or floating-point inference. QED.

Zero transition-kernel residual (ell0=ell1) does NOT alone imply FULL/LR four-observer equality: the source-sensitive STOP reward at Y (B versus continued A) persists, and the support gap remains 1/8. Do not confuse a vanishing *one component* of BRC residual with full Markov sufficiency.

Information-loss witness: the origin-labelled terminal-event readout E={L,H} has conditional Q contrast 3(ell0-ell1)/2 (up to sign). Its magnitude is exactly the TV residual. Thus the invisible distinction is recoverable under a different future observer; no universal equivalence or safe deletion of origin provenance is claimed.

## General forced-terminal fibre lemma

For any fixed source prior LR r, suppose probabilities of every decision-bearing successor are fixed. The remaining m forced terminal classes all have the SAME terminal time and observable reward, and their Q probabilities k_f must satisfy sum k_f=q and sum R_f*k_f=p*r for fixed q,p. The positive fibre is the intersection of the strictly positive orthant with the affine kernel of the 2-by-m matrix with rows (1,...,1) and (R_f). Its affine dimension (when nonempty) is

    m - rank([1;R_f]),

which equals m-2 when the forced classes include at least two distinct LR values. Such perturbations preserve the declared current four-observer P/Q expectations *only while there is no other permitted terminal-label access, downstream decision or distinguishing reward*. This is a direct finite linear-algebra theorem, not a claim of novelty for generic kernel nullspaces.

BRC use: REUSE_APPLIED to positive rational labelled branch mass, full source provenance and exact observer factorization. The signed difference of two positive kernels is an analytical contrast, not a signed probability measure used as primitive branch mass. The residual remains available for an extended future operation. This is not a native X6 coordinate theorem.

## Verification coverage

The sibling VERIFY.py was EXECUTED with Python standard-library Fraction. For FOUR explicit rational kernel pairs it independently constructs every P/Q stop path and enumerates 128 FULL and 8 seedless LR DETERMINISTIC strategies each (512 FULL plus 32 LR evaluations total). It checks strict chance positivity and normalized P/Q rows, the observer formula on every enumerated strategy, identical vectors for all pairs, exact signed support maxima -13/2 and -53/8, total-variation values 0,1/8,3/8,497/1000, rank determinant 1/2048 and a real FULL midpoint witness. EXACT_OUTPUT.txt records the run ending

    PASS_EXACT_R5_OBSERVER_FIBRE_RESIDUAL_RANGE_AND_FIXED_GAP

The general all-real theorems follow from the proofs above, not from four samples. The verifier does not independently reprove the previously established 1/1520 distance bound; that reference is explicitly inherited. No Lean checker, independent audit or native Result admission was performed.

## Scientific consequence and next question

Kernel reweighting inside the three forced terminal classes is a complete observational null direction, not a promising optimization lever for the still-open mother question. Next turn at least one forced class into a genuinely decision-bearing shared LR gate with physical cross-origin flow coupling (not an independent unrelated sidecar). First prove two-time image/hull equality. Then prove complete FOUR-dimensional convex-hull equality via exact rational convex combinations for every FULL deterministic observer (or provide a rational Farkas separator), verify rank four, and only then attempt genuine real LR image nonmembership by a polynomial/semialgebraic certificate. Preserve each source label and the newly observable BRC kernel contrast.

STATUS: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
