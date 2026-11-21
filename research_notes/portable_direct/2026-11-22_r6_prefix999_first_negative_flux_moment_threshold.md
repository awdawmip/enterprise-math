# PREFIX-999 — Exact first-negative BRC flux, collision decrement, and sharp moment threshold

Date: 2026-11-22 (+08). Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Independent portable continuation of PREFIX-996/997/998. No shared CLAIM, native PROGRESS, Result, independent Review, physical-time calibration, or P000 modification.

## Frozen inputs and observer

P000 V5: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Native space is the affine X6 Cell torsor with six axes and twelve signed primitive neighbour ports (not twelve axes). The Stage46 typed BRC candidate uses the real signed local scattering matrix on twelve ports

C_{h,j} = 1/6 - 1_{h=j},

and routed directed-port amplitudes, from research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md. Initial state is a unit amplitude on one incoming arc from x0-e_i to x0. Time below means ordered integer update count; it has no physical clock calibration. The raw Cell displacement and terminal directed port remain part of the observer, and amplitudes are summed within each Cell/port fibre before squaring. Positive and negative amplitudes are not converted to independent mass before this sum.

Let M_n be the total norm-squared at the outer spatial grade (six-coordinate sum n) after n steps. Then exactly all n steps must be positive. Let F_n be the norm-squared of paths whose FIRST negative step occurs exactly on step n, keeping only the terminal negative port on that step. These are mutually exclusive first-exit events in the declared *absorbing/monitored outer-grade continuation*; they are not a physical-time detection protocol or an unconditional claim about probabilities of unmeasured trajectory histories.

## Theorem 999.1 — Exact flux conservation and collision decrement

Set M_0=1 and for m>=0 define the six-label multinomial collision integer

A_6(m) = sum_{h_1+...+h_6=m, all h_r>=0} [m!/(h_1!...h_6!)]^2.

Then for every n>=1,

M_n = A_6(n-1)/(6*36^(n-1)),
F_n = M_(n-1) - M_n.                                           (1)

In particular F_1=5/6. For n>=2 the integer numerator of F_n over 36^n is exactly

36^n F_n = 216 A_6(n-2) - 6 A_6(n-1).                         (2)

The signed BRC local operator and its routing preserve the total directed-port norm. Immediately before update n, the outer-grade grade-(n-1) component contains only positive-step histories. At update n, this component splits into terminal-positive paths, reaching grade n, and terminal-negative paths, reaching grade n-2. The two sectors occupy disjoint directed ports. An output Cell/terminal-port has a unique predecessor Cell, so no unaccounted merging occurs across source vertices when summing norms. The norm of the first sector is M_n, that of the second is F_n, and the incoming norm is M_(n-1). Since C=(1/6)J-I is orthogonal (C^2=I), (1) follows. For an all-positive word every local branch numerator is 1; with initial positive-entry port fixed the positive n-word amplitude is 6^(-n). Group by final Cell composition and final positive port to obtain M_n from A_6(n-1) as in PREFIX-996. Substitution proves (2).

An independent combinatorial check for n>=2 uses m=n-1 and N(h)=m!/(prod h_r!). The terminal-negative fibre at (h-e_r,+r), after coherent addition, has integer numerator N(h)*(m-6h_r)/m. Consequently

36^n F_n = sum_h sum_r [N(h)*(m-6h_r)/m]^2
          = (36/m^2) sum_h N(h)^2 sum_r (h_r-m/6)^2.           (3)

Alternatively, put N_r(h)=h_r N(h)/m. Expanding sum_r (N(h)-6 N_r(h))^2 and using
sum_r N_r(h)=N(h), as well as
sum_h N_r(h)^2=A_6(m-1),
gives 216 A_6(m-1)-6 A_6(m), identical to (2). This calculation retains the signed negative-step interference before squaring.

## Corollary 999.2 — Exact first-exit law

M_n is strictly decreasing and tends to zero. Strict decrease follows by the exact sum-of-squares expression (3) (at n=1 directly) or strict ell2 contraction of repeated convolution by the six-symbol step distribution. Decay follows from PREFIX-996:

M_n ~ [9/(8*pi^(5/2))] n^(-5/2).

Therefore F_n>0, and for every N>=1,

sum_{n=1}^N F_n = 1-M_N,  and  sum_{n>=1} F_n = 1.           (4)

Under the explicitly monitored absorbing outer-sector experiment, F_n is the probability that the first negative step is detected at step n, with survival P(T>n)=M_n. This interpretation requires the declared measurement/absorption scheme. The identities remain valid as statements about the Stage46 coherent amplitude and its terminal-port readout without invoking physical-time calibration.

## Theorem 999.3 — Sharp first-exit tail and moment transition

For collision-biased compositions h of m with weights N(h)^2/A_6(m), the squared-multinomial local central limit with fourth-moment control proved in PREFIX-998 yields

E[sum_r (h_r-m/6)^2] ~ 5m/12.

Using (3), dividing by the outer numerator 6A_6(m), with m=n-1, shows

F_n/M_n ~ 5/[2(n-1)] ~ 5/(2n).                                (5)

Together with PREFIX-996 this proves

F_n ~ [45/(16*pi^(5/2))] n^(-7/2).                           (6)

Thus for every real p>=0, the monitored first-negative exit count T satisfies

E[T^p] < infinity  if and only if  0<=p<5/2.                 (7)

At p=5/2 the moment series diverges logarithmically; moments of larger order diverge. The mean and variance are finite, while the third moment is infinite. This is a native model-internal update-count assertion, not a statement about a calibrated physical waiting time or the still-open B_fix,odd(32) objective.

The exponent and constant in (6) follow from the exact Stage46 typed BRC flux and the previously demonstrated collision asymptotic; a finite fit alone does not establish (6). No ordinary matrix exponential, Taylor/Pade/Cayley, trigonometric calculation, or independent classical propagator is substituted for the typed BRC model.

## Exact scalar algorithm and reproducibility

The recurrence A_1(m)=1 and

A_d(m)=sum_{r=0}^m binom(m,r)^2 A_(d-1)(m-r),  d=2,...,6,   (8)

computes the scalar outer and first-negative flux through any prescribed finite n using exact integers. It avoids storing endpoint/port amplitude fibres for this single scalar observable; it is NOT an observer-safe replacement for the full BRC state when later operations or future interference require that state. Equation (1) is precisely the scoped compression certificate for this scalar.

Companion executable PREFIX999_R6_FLUX_CERTIFICATE.py independently propagates the twelve signed Stage46 BRC ports, preserving raw Cell displacement, last incoming port and up to one negative step, and compares its outer and first-exit squared fibre sums for all n=1..7. It also checks the collision recurrence, equation (2), strict positivity for n<=60 and the finite telescoping identity through n=60, all by Python integers and Fraction, with no rounding in the checks. Companion PREFIX999_R6_EXACT_RESULTS.json records the inputs, formula, integer numerators and rational samples. Example: (n,M_n,F_n)=(1,1/6,5/6),(2,1/36,5/36),(3,11/1296,25/1296),(4,83/23328,115/23328).

## Provenance, limitations, next objective

Science pins: frozen P000 V5 at f42f2906d77f24085c123f3ccfe9667d41caa96d; Stage46 typed BRC local rule at research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md. Continuation sources: PREFIX-996 proof 0bfb06f7e3118bed106b730ec0daf00ab5786adb, PREFIX-997 proof 436902ad6606be55f596a228f9419b0573502ff0, PREFIX-998 proof 6a348719b9c36eae638b528d017f92cb64ad5489. Previously generated exact source has been reused; no theorem admission or independent review is asserted.

Research provenance is the historical EM-DIRECT-FBEA5D; this turn has no newly authenticated possession of its private execution capability. Current owner read request r6-20261122-0752-leased-owner-read-v1 failed SOURCE_TREE_TRUNCATED / EVENT_ISSUE_GUARD_CHANGED while assembling source events. It does not grant a shared owner or CLAIM. This portable source work is independent of that permission; no formal PROGRESS or Activity backfill is claimed.

Next: find a similarly scalar, observer-safe identity for the *positive-terminal* part of the first-interior grade, which carries the leading n^(-5/2) term and retains interference between different negative axes. Test whether X6 Link/Port occupancy or triadic field feedback preserves the flux identity, or derive the exact correction flux at the declared boundary. Shared mother objective B_fix,odd(32) in {19,20} remains open.
