# T6 p19 order 9: recovered exact lattice and the independent (4,5) block

Task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND` / `TP2-34B106D2512A298C9647`.
Researcher: `EM-T6SM-B134BD`; execution record `ER-120BCED768F86DA406CC`.
Status: `EXACT_INPUT_RECOVERED / (4,5) COMPLETE_RESEARCHER_CERTIFICATE / GLOBAL_T6_OPEN`.

## Reconciled source frontier

The frozen September-9 dossier still names (3,6) as first unfinished. Current
source also contains `research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_6E0914_20260917/`
with `PROOF.md`, `order9_36_certificate.json`, and `verification.txt`. These report
335,374 primitive (3,6) cosets cleared and name (4,5) next. The claimed builder
`check_order9_36.py` (SHA256 4974d37f506f54812189d1bae4b9bd71dbc326a6c9214bdf8e623ed2610952c2)
and generated C++ (f6557d770faa22ff9088b95fbd372abc15f01e8039e76009d0187cea2ea5e8a9)
are absent from that current artifact directory; a bounded exact-name source
search returned no code result. That is a reproducibility gap, not a refutation.
The prior (3,6) result remains **an authored clearance claim awaiting recovery or
independent verification**. Its 335,374 cosets were not replayed here. This work
recovers mathematical inputs and starts the separate (4,5) block.

## Carrier and elementary guards

Retain denominator a=e+1, its prime valuations, signed multiplicity z_a, and
the separate positive/negative exponent-mass budgets 2331. The original BRC
shape observer is H_k=sum(e/(e+1))^k for k=0,...,6. By the binomial triangular
change of coordinates, equality of these seven observers implies equality of
the reciprocal moments sum a^(-k), k=0,...,6. No prime-only or logarithmic
compression is used.

The 18-dimensional lattice here is an auxiliary space of arithmetic
coefficients, not an 18-axis native physical space. Its weighted quadratic
form is a proof bound, not an additional native metric axiom. P000 is preserved.
Choose the maximal prime only after cancelling common exponent atoms; removing
such atoms preserves every H_k equality and weakens both side budgets.

For maximal prime 19, a denominator with valuation at least 3 exceeds 2332.
At valuation 2, a=361m has 1<=m<=6. Multiplying the six reciprocal equations by
19^(2k) and reducing mod19 gives the six checks sum z_m m^(-k)=0. The six
nonzero distinct residues 1,...,6 give an invertible Vandermonde-type matrix.
Thus z_m is divisible by19. But each side can contain at most six such atoms
(7*360>2331), so after common cancellation |z_m|<=6 and every z_m=0. Therefore
the nonzero 19 layer has valuation exactly one, a=19m with 19 not dividing m.

Write m=r+19q, 1<=r<=18, q>=0. The q0 weight is w_r=19r-1. A vertical atom
(q,r), q>=1, costs 361q+w_r and carries vertical order q. The implementation
lists every atom fitting one side and enumerates its nondecreasing finite
multisets with exact order and exact side cost. It obtains 8124 order-4 states
and 8506 order-5 states. Identical atoms on opposite sides are cancelled: this
reduces total vertical order below9, already excluded by the frozen order0--8
input. Global sign reversal exchanges (4,5) with (5,4), so one orientation suffices.

## Exact homogeneous and affine inputs

The homogeneous lattice is

    L = {u in Z^18 : sum u_r r^(-k) = 0 mod 19^k, k=1,...,6}.

Six sequential kernel updates with a unit pivot give index factors 19^k. The
weighted LLL routine in python-flint is only a basis proposal. Native integer
verification checks the proposed transform product and determinant +/-1, all
six congruences, and determinant of the unweighted basis of absolute value
19^21. An independent saturation argument is available: the first six residue
columns have unit determinant mod19; hence they are invertible mod19^6 and
surject onto the six mixed moduli. Their product has cardinality19^21. Inclusion
plus the checked equal index therefore proves that the recovered lattice is
the entire kernel, not a sublattice selected for convenience.

For each vertical atom the recorded particular q0 representative solves

    sum u_r r^(-k) = -(r+19q)^(-k) mod19^k.

For two states the positive representative minus the negative representative
has exactly the required affine congruence. Replacing a representative by a
lattice translate changes neither this affine class nor its potential completions.
`verify_input` reconstructs the congruences and Gram-Schmidt data from integers;
the run path does not import FLINT or trust an LLL approximation.

These mixed congruences are a necessary relaxation of the complete seven BRC
observer equalities, not an equivalent replacement for them. Empty affine
classes exclude full collisions. A surviving local class would still need
the lower-prime and H0 completion and would be retained rather than discarded.

## Stronger separate-side sphere bound

Let B+=2331-cost(V+) and B-=2331-cost(V-). Any feasible q0 completion satisfies

    ||Wu||_2^2 <= B+^2 + B-^2.

Indeed its positive weighted entries sum to at most B+ and its negative
absolute weighted entries sum to at most B-. For nonnegative entries the sum
of squares is at most the square of their sum, separately on the disjoint
positive and negative supports. For order4 the minimum vertical cost is1462;
for order5 it is1823. Consequently B+<=869, B-<=508, and

    R^2 <= 869^2+508^2 = 1,013,225.

This is stronger than the total-l1 bound 1377^2. It does not erase either side
budget: the final candidate also undergoes both original signed cost checks.
The displayed number is an a priori upper bound on the squared norm of any
feasible completion. It is not a claim that a feasible completion attains that
norm. The maximal budget expression itself is obtained from the distinct
single vertical atoms (q,r)=(4,1) and (5,1); their existence as vertical states
does not assert that their affine class has a feasible q0 point.

## Flatness and exhaustive coordinate rejection

The recovered weighted row basis b_i has exact rational Gram-Schmidt squared
lengths D_i. All are checked to exceed 4*1,013,225. For an affine representative
w, write its orthogonal coordinates h_i and upper coefficients mu_ji. Any
point w+sum n_i b_i inside radius R must, descending from i=17, satisfy

    |h_i + sum_(j>i) n_j mu_ji + n_i| <= R/sqrt(D_i) < 1/2.

There is at most one possible integer n_i, namely the exact nearest integer
to the negative center. Ties cannot be feasible because the inequality is
strict. Inductively there is at most one full candidate in the affine ball.
No heuristic rounding or alternate branch is silently discarded.

The code uses integer projector numerators over positive common denominators.
Each materialized quotient/remainder enters `brc_evaluate_division`. At every
coordinate it adds the floor of the exact nonnegative squared orthogonal
component. This sum of floors is a lower bound on the partial squared norm;
if it exceeds the integer R^2, the coset is empty. Flooring here can only make
the rejection weaker, never invalidate it. Surviving full candidates are
checked by the integer weighted norm and both original side budgets. A genuine
modular kernel is returned and stops the run; it is not declared a full shape
collision before lower-prime completion.

## Complete exact (4,5) census

Three completed, disjoint, contiguous half-open intervals cover all8124
order-4 rows against every one of the8506 order-5 states:

| Order-4 rows | Primitive affine cosets checked | Shared-atom pairs |
| --- | ---: | ---: |
| [0,25) | 117474 | 95176 |
| [25,2025) | 8737150 | 8274850 |
| [2025,8124) | 36432451 | 15445643 |
| Total | 45287075 | 23815669 |

The total is69102744=8124*8506. All45287075 primitive cosets were rejected,
with no modular kernel. Each complete run reports the same input SHA256
`2c6be9c821faf2480e101bafbda191a0d334430e2fffc5bcf0dcaa0f3c726c27`
and frozen core source SHA256
`14f531a16ad338aee9fdd6d697cba64442e047570706ad2adaa6b460622382d1`.
`verify_coverage.py` validates file hashes, exact ranges, pair counts and rejection
counts and produces `coverage_4_5.json`. This metadata verifier does not replace
independent execution of the mathematical checker. Researcher computation and
the preceding proof yield the bounded conclusion:

    No primitive maximal-p19 order9 split(4,5) kernel meets both side budgets2331.

This closes the new (4,5) block at researcher-proof/census strength, not the
separate prior (3,6) independent-review gap and not the entire T6 target.

The input is durable as `input.json`, including the full basis, exact rational
orthogonal data, atom representatives and saturation construction. Source
`p19_order9.py` uses the existing BRC arithmetic facade for actual division;
its task-specific signed rational bookkeeping retains explicit numerators and
denominators and only reduces them through that facade. The trace object is
validated at every call. Output retains sample traces and an exact call count,
not a complete archived transcript of millions of calls; the source and input
permit their exact replay. This is standard exact lattice methodology applied
to the existing BRC shape observer, not a new general tool family or a claim
of global mathematical novelty.

## Reproduction and limits

Python3.12.14 is the actual local interpreter. Building alone uses the existing
isolated python-flint0.9.0 as an external proposal provider. Verify/run need
only the standard library and this snapshot's `src/enterprise_math` BRC facade.
With that source directory on PYTHONPATH:

    python p19_order9.py verify
    python verify_candidate_transport.py
    python p19_order9.py run --start 0 --stop 25 --max-seconds 120 --output replay.json
    python p19_order9.py run --start 25 --stop 2025 --max-seconds 300 --output replay2.json
    python p19_order9.py run --start 2025 --stop 8124 --max-seconds 660 --output replay3.json
    python verify_coverage.py

A time budget stops only at a completed row boundary. The returned half-open
completed-row interval is authoritative; resource exhaustion is never encoded
as an empty unvisited interval. Future intervals must be disjoint and contiguous
before their union is called complete. The separately retained (3,6) review gap,
orders10--12, lower maximal primes and global T6 all remain outside this initial
block certificate. No CI, persistence, source branch or self-check confers
Driver acceptance, Working Truth, Foundation promotion or global T6=2332.

## Independent higher-block reuse

One side cannot have order7: even its cheapest nonempty vertical state costs
7*361+18>2331. Thus, after order9, the only primitive blocks up to sign are
10:(4,6),(5,5);11:(5,6);12:(6,6). Their respective squared-radius upper bounds
are776770,516128,279673,43218. All are below the already checked(4,5) flatness
envelope. `higher_orders.py` reuses the frozen lattice verifier, state generator
and exact candidate function unchanged. Equal-order blocks use j>i to remove
only overall sign duplication. Shared atoms are absent from the normalized
primitive carrier; excluding them in an individual primitive block does not
assert that the lower order after cancellation has already been independently
reviewed. Higher-block certificates are separate and cannot resolve the old
(3,6) source gap by themselves.

Researcher-ID: EM-T6SM-B134BD / RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND
Global-Knowledge-Sync: main@6043a5a / GLOBAL_KNOWLEDGE_V1
