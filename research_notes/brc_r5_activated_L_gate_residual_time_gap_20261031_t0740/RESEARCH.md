# R5 — Activating the L terminal class exposes a BRC residual in time support

2026-10-31; portable author-side proof, unreviewed/not admitted. This is a finite P/Q stop/continue auxiliary observer model, not native X6 or a physical Heartbeat theorem.

## Frozen sources and authority

GLOBAL_KNOWLEDGE_V1 main@09292cceaa714d59e1ddcb3d250509b4b87fd624; Enterprise Math main@f7f61aa61a5a5ee63061542ff3a5028bf1776c1c. Read global bootstrap/manual, P000_STARTUP and checked canonical P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview, TASK_RESEARCH, BRC, math/code policies and EM autonomous/portable protocols. Prior immutable research: commit 8a4e2fde8fcd7e81c3cf7d3241cfdead39c07131, research_notes/brc_r5_observer_fibre_20261031_t0640/RESEARCH.md. P000/ACTIVE worldview unchanged. Native status: research_authority_granted=false; executor_binding_configured=false; active jobs 5/5. Owner inventory returned CONTROL_QUOTA; own native session_start was rejected before submission with STATIC_READONLY_SCOPE_DENIED. No native owner/CLAIM/Result/review inferred.

## Exact extension

Keep Q origin masses A0,A1,B,C0,C1=(1/8,1/8,1/4,1/4,1/4), and P=(1/4,1/4,1/4,1/8,1/8). Time-one LR=2 A0/A1 gates CONTINUE with probabilities x0,x1; LR=1/2 C0/C1 gates CONTINUE with z0,z1. B bypasses. At time two Y, LR=1, STOP probabilities u0,u1,uB. Continued A has conditional Q next-label kernel over (Y,L,M,H), labels R=(1,3/2,2,3):

    K_i = (1/4, ell_i, 1/2-3*ell_i/2, 1/4+ell_i/2),   0<ell_i<1/3.

P conditional probability is R_j*K_i(j)/2. These natural probability rows are strictly positive and P/Q-normalized. Previously L/M/H terminated at t=3. NEW: L (time-three LR=3/2) has a genuine STOP(t=3)/CONTINUE(t=4) gate, with FULL origin-specific continue probabilities v0,v1 and single shared seedless LR probability v. Continuing ends at t=4 with unchanged LR=3/2; no new natural randomness. Both actions have error 1/8 at L. All other original interior error values and stopping gates are retained. This gate receives actual A_i-origin positive chance flows ell_i*x_i/8 under Q and 3*ell_i*x_i/16 under P; thus it is coupled, not a disjoint sidecar.

FULL behavior domain [0,1]^9 in variable order (x0,x1,u0,u1,uB,z0,z1,v0,v1). Seedless LR domain [0,1]^4 in (x,u,z,v), with both x_i=x, all u_i=uB=u, both z_i=z, both v_i=v. Observers O=(eP,eQ,TP,TQ). Define

    x=(x0+x1)/2; z=(z0+z1)/2;
    w=(x0*u0+x1*u1)/2; s=uB/4+w/16;
    E=ell0*x0*v0+ell1*x1*v1.

Since one extra time unit is contributed by exactly those L continue flows,

    eP=1/8+uB/8+(1-z)/8;
    eQ=1/8+uB/8+(1-z)/4;
    TP=3/2+x+z/2-s+3*E/16;
    TQ=3/2+x/2+z-s+E/8.

For LR: w=x*u, s=u*(1/4+x/16), E=(ell0+ell1)*x*v.

## Theorem 1 — full real time-image/hull classification

For every real ell0,ell1 in (0,1/3), FULL and LR have equal two-time convex hulls IF AND ONLY IF ell0=ell1. If equal, their ACTUAL real two-time images are also equal and are compact convex polytopes. If unequal, both time hulls and time images are distinct.

Proof (unequal). Let theta=(ell0+ell1)/2 and define

    H_theta=-(4+2*theta)*TP+(8+3*theta)*TQ.

Algebraic substitution gives

    H_theta = 6+3*theta/2 +(6+2*theta)*z
              -(4+theta)*s -(theta/2)*x +E/4.

The z coefficient is positive, the s coefficient negative; both policy classes maximize at z=1 and uB=u0=u1=0 (LR u=0). The remaining FULL decisions are independent x_i and v_i, and LR decisions are shared x,v. Exhausting their real intervals algebraically, using q_+=max(q,0), yields

    sup_FULL H_theta =
        12+7*theta/2 +[(ell0-theta)_+ +(ell1-theta)_+]/4
      = 12+7*theta/2 +abs(ell1-ell0)/8;
    sup_LR H_theta =
        12+7*theta/2 +(ell0+ell1-2*theta)_+/4
      = 12+7*theta/2.

Hence exact all-real signed support gap abs(ell1-ell0)/8>0 for unequal ell. This proves both non-equalities, without sampling.

Proof (equal). If ell0=ell1=ell, any FULL aggregate (x,z,s,E) satisfies

    0<=x,z<=1, 0<=s<=1/4+x/16, 0<=E<=2*ell*x.

For any such FULL aggregate choose LR x,z unchanged; u=s/(1/4+x/16), and when x>0 choose v=E/(2*ell*x), else v arbitrary since E=0. These LR values are in [0,1] and reproduce both times exactly. LR is already a FULL subclass. Conversely every point in the displayed convex polytope is LR-realizable by these formulas. Because (TP,TQ) is affine in (x,z,s,E), the actual common time image is convex. QED.

## Theorem 2 — BRC residual becomes observable

The exact origin-labelled conditional kernel Q-total-variation is

    TV(K0,K1)=3*abs(ell1-ell0)/2.

The new time-only support gap therefore obeys the exact model-specific conversion

    Delta_theta=TV(K0,K1)/12.

For ell0<ell1 a legal FULL deterministic witness takes x0=0,x1=1,z0=z1=1,v1=1 and all other decision variables 0. It has O=(1/8,1/8,5/2+3*ell1/16,11/4+ell1/8). Reverse source labels when ell0>ell1. By the signed separator and the triangle inequality, its distance to ALL real LR four-observer points is at least

    d_infty >= abs(ell1-ell0)/[8*(12+5*theta)].

At (ell0,ell1)=(1/12,1/6), theta=1/8, the integer direction -34TP+67TQ has sup_FULL=1195/12, sup_LR=199/2, gap=1/12. Witness O=(1/8,1/8,81/32,133/48); d_infty>=1/1212. The normalized functional gap is 1/96. These relations require the specified L stop gate and do not extend automatically to arbitrary operations or native physics.

## Theorem 3 — this entire new gate family still fails the four-observer mother target

The inherited four-observer signed direction

    J=14eP-19eQ+2TP-4TQ

simplifies EXACTLY to

    J=(-53-uB+w-E)/8.

In FULL, 0<=w<=1, uB>=0,E>=0, and maximum -13/2 is achieved by x0=x1=u0=u1=1, uB=v0=v1=0. In LR, w=xu, uB=u, E=(ell0+ell1)*x*v>=0; therefore J<=-53/8, attained with u=v=0. Consequently, for ALL ell0,ell1 in the entire strictly positive open square,

    sup_FULL J - sup_LR J = 1/8 > 0.

Thus 4D convex hull equality fails everywhere, including ell0=ell1 where two-time actual images do coincide. This is a complete no-go for the stated activated L single-gate model, not for other transition/reward/topology choices. The original mother question remains open.

## Validation, provenance, reusable insight

Executed sibling Python standard-library Fraction VERIFY.py. Four rational pairs; each exhausts 512 FULL and 16 LR deterministic strategies (2048+64 observations total), checks Q/P kernel positivity/moments, two exact support formulas, time hull equality condition by rational polygon hull, the independent four-observer support gap, and a concrete signed separator. EXACT_OUTPUT.txt is actual output. Finite regression tests four instances; all-real theorems follow from the written algebra. No Lean or independent review.

BRC use: REUSE_APPLIED to prior origin-labelled positive Q/P branch carrier K(ell). Previously the forced-terminal fibre erased differences in ell; a new permitted downstream shared stop decision multiplies labelled positive L flow by v_i and exposes a TV-proportional residual. This is an observer/future-operation-specific insufficiency certificate, not an interpretation of positive weights as signed amplitudes, nor a native X6 proof. Protected P000/worldview remained unchanged.

Next exact research question: introduce genuinely interactive downstream chance routing or source-sensitive interior rewards to compensate the new gate while preserving positive two-law paths, full four-dimensional rank and ALL-signed convex-hull equality. Enumerate rational FULL/LR deterministic images, demand exact <=5-vertex LR convex combinations for EVERY FULL point or rational Farkas rejection; if equality survives, prove actual real LR-image nonmembership semialgebraically. This current family requires no repeat search.

Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
