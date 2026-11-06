# PREFIX-530 — Exact 49-coordinate signed-linear lift of the 51-state BRC–aAc transducer

**Date**: 2026-11-06 (Asia/Shanghai). **Task line**: RS-X6-NATIVE-ROTATION-DYNAMICS.
**Frozen scientific input**: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
**Evidence state**: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Problem and model

PREFIX-529 proved that the 51-state controller is minimal among deterministic controllers that explicitly expose phase and preserve individual history's declared BRC visits and aAc gate count under every legal branch-labelled future. PREFIX-525 proved an exact 48-vector *second-order* aggregate recurrence. Here we give an exact **49-coordinate first-order linear realization** for the full six-axis, start/end-resolved weighted histograms.

Frozen four STARs are A={L1,L3,L6}, B={L1,L4,L5}, C={L2,L3,L5}, D={L2,L4,L6}; an admissible directed phase is (j,p,c), where p,c are distinct opposite-signed axes in STAR j. There are 48 phases, each with three incoming/outgoing phase edges. Each edge s→r has native branch words INNER=(-c_s,c_r), OUTER=(c_r,-c_s). T=(A,+L1,-L3) is the gate target: it has three incoming phase predecessors and no self-loop. Colors +L1=a, -L1=A, ±L3=c, others=_. A complete aAc gate at a macro step occurs exactly when the two most recent branches are INNER and the new phase is T.

Let R=Z[x1,...,x6,z]. Define W∈Mat_48(Z[x]) by W_(r,s)=x_|c_s|x_|c_r| if s→r and zero otherwise. Let e be the unit vector at T. For fixed initial phase s0, f_d(r) is the polynomial sum of x^K z^H over all *branch-labelled* length-d histories from s0 ending in phase r; K counts six unsigned-axis primitive visits and H counts complete aAc occurrences. Initial condition: f_0=e_(s0).

## Theorem 1 — a 49-coordinate exact first-order realization

Introduce one scalar polynomial g_d and initialize (f_0,g_0)=(e_(s0),0). For every integer d≥0, set

    f_(d+1) = 2W f_d + (z−1)e g_d
    g_(d+1) = e^T W² f_d.

Equivalently this is a single 49×49 first-order transfer

    M49 = [ 2W          (z−1)e ]
          [ e^T W²         0  ].

For all s0,d and all monomials x^K z^H, the first 48 coordinates exactly count the legal source-resolved histories. g is a *pending event credit*; it is not an individual path/Cell state.

**Proof.** Let b_d(r) count weighted histories whose last branch was INNER and whose final phase is r. For any r∈Pred(T), r≠T, so no gate can complete upon entering r. Thus for all d≥1, b_d(r)=(W f_(d−1))_r: every incoming phase edge has exactly one INNER realization, with no gate weight on arrival at this r. The normal extension from length d to d+1 contributes 2W f_d. The only modified histories are those whose new edge r→T is INNER and whose last branch was also INNER. Replacing their weight 1 by z contributes the correction (z−1)e·Σ_(r∈Pred(T)) W_(T,r)b_d(r). At d=0 there is no last INNER, so the correction is zero and g_0=0. For d≥1 the scalar is e^T W²f_(d−1). The second recurrence maintains precisely this identity, completing induction for all lengths. QED.

Eliminating g gives the PREFIX-525 48-vector order-two recurrence f_1=2Wf_0 and, d≥2,

    f_d = 2Wf_(d−1) + (z−1)ee^TW² f_(d−2).

The formal matrix determinant identity is

    det(I49−tM49) = det(I48−2tW−(z−1)t²ee^TW²).

Proof: Schur complement of the scalar bottom-right block of I49−tM49, which has constant term 1. This also shows exact equivalence of the two rational resolvents, without numerical approximation.

**Representation distinction.** The 51-state PREFIX-529 machine is a nonnegative deterministic controller for individual histories and their specified future operations. The 49-coordinate construction is a *signed linear realization* because it has z−1 entries: it aggregates and algebraically cancels weights. Its dimension 49 is a proved sufficient linear upper bound, not a proof of minimum Hankel rank or a replacement for ordered branch/Cell provenance.

## Theorem 2 — exact six-axis BRC readout

Let σ_a(c)=sgn(c) for |c|=a and zero otherwise. On an origin s0 / final r / visit vector K monomial of f_d(r), the signed primitive displacement telescopes to y_a=σ_a(c_r)−σ_a(c_s0). The exact native opposite-sign pair count is

    p_a = (K_a − |σ_a(c_r)−σ_a(c_s0)|)/2,  a=1,...,6.

Every occurring monomial has a nonnegative even numerator. Collecting these endpoint-corrected monomials yields the complete joint distribution (p1,...,p6,H) for every d. Different INNER/OUTER histories remain counted with correct multiplicities; if an observer asks for intermediate Cells or provenance, their raw ordered history is separately retained.

## Sparse arithmetic and exact evidence

W has 144 nonzero directed positions. On the frozen four-STAR graph e^TW² has *exactly nine* nonzero source positions, each of coefficient one (nine two-edge phase paths into T). Each 49-coordinate step therefore uses one sparse 48×48 multiply, a nine-term scalar accumulation and a single gate correction. This is an algebraic operation count, not a time benchmark; multivariate coefficient growth and integer bit costs remain to measure.

The attached Python exact-integer certificate independently reconstructs 48 phases and 3 successors each. It compares a direct 96-state nonnegative branch-labelled DP to the 49-coordinate signed-linear DP at **every origin, final phase, visit-vector and H coefficient**. The six-axis comparison covers all depths 0..5 (373,248 histories at d=5); the independent single-axis specialization covers depths 0..10 (2,902,376,448 histories at d=10), all computed by exact integer aggregation. Both pass at every depth with nonnegative resulting f coefficients and total count 48·6^d. This tests the implementation; the displayed induction proves the all-length claim.

At d=5 (six-axis) the direct DP has 18,191 keys; the linear lift has 9,182 f keys and 408 g keys. At d=10 (single-axis) the counts are 16,182 direct keys; 8,127 f keys and 162 g keys. These are actual reference-program key counts, not elapsed-time or minimum-space claims.

## Next experiment

Compute the reachability–observability/Hankel rank of M49 over Q(x1,...,x6,z), using every 48 origin and terminal phase observable, to decide whether the 49-coordinate *linear* realization can be further reduced without changing this joint observation. Benchmark end-to-end sparse arithmetic and memory for the 49-coordinate lift, the 51-state deterministic machine and the 48-vector second-order recurrence, including coefficient bit lengths and output recovery.

The four-STAR language is a frozen candidate subproblem. Mother objective: arbitrary native three-axis C6 generation, complete generated group, and physical native X6 rotation-selection dynamics. Sources: original PREFIX-525/529 notes, frozen native pin, current P000/ACTIVE worldview and portable research methods.