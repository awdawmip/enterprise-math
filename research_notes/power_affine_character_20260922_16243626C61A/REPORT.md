# POWER feedback VI: nonuniform collision weights and certified character pruning

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`
Researcher-ID: `EM-DIRECT-16243626C61A`
Session: `local-power-review-16243626C61A` (continuing local key, not a platform identity)
Progress-Event-ID: `power-affine-character-20260922-16243626C61A`
Status: `PROVED_SCOPED_DERIVATIONS + EXECUTED_CHECKS / RESEARCH_CANDIDATE_NOT_ADMITTED`
Source snapshot: `awdawmip/enterprise-math@45921e618ee2a41678e5458c33e5f9bf8d9bee82`.

## Selected unit and reuse

The previous batch/window unit was complete. This unit specifies a genuinely different
observer: nonuniform positive integer exponent multiplicities. It also supplies a proven
constraint on the exponent matches, rather than another name for the same BSGS search.

The existing `group_ring_batch_response.py` (blob
`82c87f779a07b84de601d54ebd04d3bfb1856f92`) and its dependency
`group_ring_terminal_response.py` (`354633331b05f8c7f275e852ae04df85aad63004`)
were executed UNCHANGED. The new adapter explicitly consumes the former's local
first-hit/period data, including its private mapping fields. This is a pinned internal
extension, not a claim of a stable independently published external API.

The Jacobi function text is ported verbatim from
`awdawmip/power@6d784d3990afae602a03745173c3f2a16a076b0c:src/power/modular/arithmetic.py`
(source blob `b17dd3a61e83677f571649790ebe3ace3699d773`). Its results are independently
compared against SymPy. No other POWER arithmetic/primality claims are imported.

Classification: `T0_POSITIVE_BRC + T4_COLLISION + T6_OBSERVER_SAFE_SPECIALIZATION`,
`EXTEND_EXISTING_INTERFACE / REUSE_EXECUTED / EXACT_FUNCTION_PORT`.
No new top-level family, formal task CLAIM, Driver review, Working Truth or Foundation
promotion. P000 is unchanged; no geometrical/physical interpretation is required.

## 1. Weighted collisions: the right baseline is not the window length

Take a FULL exponent interval 0<=x<L, integer weights w_x>0, a unit a modulo n,
and r=ord_n(a). Define

    V = sum_x w_x [a^x],
    K_w(r) = [1](V V^-) = sum_u (sum_{x:a^x=u} w_x)^2,
    A(d) = sum_{x=0}^{L-1-d} w_x w_(x+d), 0<=d<L,
    A(d)=0 for d>=L.

Here V^- inverts group labels, not weights. The weights are multiplicities, not complex
amplitudes, normalized probabilities or stochastic errors. The diagonal baseline A(0)
includes different copies of the same exponent. Nontrivial EXPONENT collisions satisfy

    K_w(r) = A(0) + 2 sum_{j>=1} A(jr).

All sums are finite. Full strict positivity gives

    K_w(r) > A(0)  iff  r<L.

Thus positive reweighting does NOT advance the first detectable collision window relative
to uniform weights. It changes the observer, not that exact-information threshold.

### Positivity alone does NOT give unique order inversion

For L=4 and w=(2,1,1,2), A(0)=10, A(2)=A(3)=4. Consequently

    K_w(2)=18=K_w(3).

This occurs in the same ambient modular group: base6 modulo7 has order2, base2 has order3.
The previous uniform-weight integer binary inversion must not be applied blindly here.

If zero weights create holes, even the first-collision criterion can fail: w=(1,0,1,0),
L=4, base2 modulo7 has order3<L but K_w=A(0)=2. This is an information-loss witness,
not a reason to discard all sparse-weight models; their supported difference set needs
its own criterion.

### An unconditional partial-order law survives

For arbitrary nonnegative weights and r dividing s, multiples of s are a subset of
multiples of r, so K_w(r)>=K_w(s). With full positive support, r<s and r<L make this
strict. This is refinement monotonicity on the divisor order, NOT ordinary numerical
monotonicity between incomparable periods (the periods2 and3 above are incomparable).

## 2. Positive monotone weights restore exact injectivity

Suppose w is positive and nondecreasing. Reindex the correlation using y=x+d:

    A(d)-A(d+1)
      = w_0 w_d + sum_{y=d+1}^{L-1} (w_(y-d)-w_(y-d-1)) w_y > 0.

For d=L-1, A(L-1)>A(L)=0 directly. Thus A is strictly decreasing on 0..L.
When 1<=r1<r2<L, every A(j*r1)>=A(j*r2), with the j=1 term strictly larger.
Hence K_w(r) is strictly decreasing for 1<=r<L; exact K_w>A(0) uniquely determines r.
Reversing a nonincreasing profile leaves its autocorrelation unchanged, so positive
nonincreasing weights also qualify. Monotonicity of w is SUFFICIENT, not asserted necessary.
The more general sufficient property is a strictly decreasing positive lag correlation.

This is an elementary finite theorem for the declared observer. Historical novelty is
not claimed, and an externally supplied mass is not authenticated merely by inversion.

## 3. Executable affine family: a cubic response, no expanded weighted population

The implemented profile is w_x=alpha+beta*x, alpha>=1,beta>=0. Put k=L-d.
For 0<=d<L,

    A(d)=k*alpha*(alpha+beta*d)
        + beta*(2*alpha+beta*d)*k*(k-1)/2
        + beta^2*k*(k-1)*(2*k-1)/6.

Equivalently

    6*A(d)=c0+c1*d+c3*d^3,
    c0=6*alpha^2*L+6*alpha*beta*L*(L-1)+beta^2*L*(L-1)*(2*L-1),
    c1=-6*alpha^2-6*alpha*beta*(L-1)-beta^2*(3*L^2-3*L+1),
    c3=beta^2.

The d^2 coefficient cancels. Negative coefficients are exact algebraic readouts, NOT
negative BRC branch weights. Values outside |d|<L are zero; extrapolating the cubic is wrong.

The existing bounded compiler already provides first exponent e and, when found, period r.
For positive matches d=e+j*r, j=0..c-1, only the count, sum(d), and sum(d^3) are needed.
Closed integer progression sums evaluate the contribution without looping over c or L.
Without a found period, there is at most one match in the certified horizon; evaluate
that single correlation value. Combine the two signed targets and subtract A(0) once
for the identity. The previous all-future and atomwise information barriers still apply.

`affine_collision_from_order` evaluates the conditional mass in constant-many integer
operations; `invert_affine_collision` uses O(log L) evaluations. This is not a cheap
unknown-order oracle: `affine_index_responses` consumes actual bounded exponent evidence,
whose construction cost remains classical BSGS. Using the resulting mass to recover the
already-searched order is only a consistency test, not a second independent discovery.

The unchanged uniform API agrees at alpha=1,beta=0. Arbitrary positive profiles are not
silently admitted into this affine API. A profile with enormous coefficients has larger
bit costs even when the number of algebraic operations is constant.

## 4. Certified pruning: use a true character, not a coarse residue guess

For odd n the Jacobi symbol chi is a multiplicative map on units to {+1,-1}.
It can be evaluated by reciprocity without factoring n. If a^d=t, then

    chi(t)=chi(a)^d.

When chi(a)=-1, set epsilon(t)=0 for chi(t)=1 and1 for chi(t)=-1. Necessarily

    d=epsilon(t)+2k,
    (a^2)^k=t*a^(-epsilon(t)).

Thus for 0<=d<S only one parity progression needs searching, with at most ceil(S/2)
possible k. This is an exact equivalence, not probabilistic deletion. A first return
s of a^2 certifies ord(a)=2s, since chi(a)=-1 proves the order is even.

When chi(a)=1 but chi(t)=-1, ALL exponents are impossible. Positive characters alone
are not sufficient: modulo21, a=4 has subgroup{1,4,16}; t=5 has chi(5)=chi(4)=1 but
is not in it. The checker still searches rather than accepting this target.

The adapter executes the existing compiler unchanged on the transformed problem. Both
signed targets are registered, and the additional transformed inverse targets, input
inverses and Jacobi evaluations are explicitly costs. Identity is retained if necessary
so a reported period lower bound really was checked. Even moduli use the original path.

The one-bit gain CANNOT be iterated just by squaring: chi(a^2)=1. More generally, a genuine
computable character into a cyclic image could constrain d modulo the image order, but
computing that image/log is a cost, not an automatically available higher-bit oracle.
No new generic sub-BSGS, Shor or factorization complexity claim follows.

### Adapter defect found and fixed during this unit

For an odd master span S, learning a period through a^2 may certify r=S+1. Dropping a
canonical target exponent outside [0,S) then broke the inherited cut API's use of a
known period, even though two-sided weighted windows still agreed. The fix reconstructs
an inverse target exponent as -e modulo the PROVEN period; it does not invent a match.
For n=17,a=3,S=15, e(3)=1 and r=16 imply e(6)=15. Tests now include this evidence-lifting
boundary and check all inherited dyadic cut outputs against independent occupancy.
This was a new adapter defect fixed before publication, not a claim that the old
unmodified compiler had failed its original contract.

## 5. Executed validation and full-cost comparisons

Local sparse checkout from the preceding user bundle. 34 new tests and93 inherited tests:
127 PASS. Validation also checked2358 compilations,927315 weighted terminal observations,
17685 collision inversions and515175 dyadic-cut observations against independent direct
exponent occupancy. 1000 positive monotone profiles verified the monotonicity identity.
The ported Jacobi function matched6000 SymPy values in pytest. None of these counts is
a full EM/POWER test-suite claim or an independent-review/Lean certificate.

Same-output timings below are medians of seven complete calls after warmup. Every timed
call includes its own compilation and queries; no warm index is free. Common target
selection is outside every timing. Tracemalloc is a separate Python-allocation measurement,
not process RSS. The weight profile in all rows is alpha=3,beta=2.

| n,a; L; targets | direct weighted occupancy ms | unchanged bounded BSGS + affine ms | character + same backend ms | scans before -> after |
|---|---:|---:|---:|---:|
|100160063,5;262144;1|111.1424|0.093147|0.077885|1088 ->770|
|65537,3;65536;1|17.6249|0.050084|0.044876|545 ->386|
|100160063,5;16384;16|31.5653|0.132515|0.209498|1229 ->1083|
|10007,25;16384;32|18.3204|0.191932|0.171572|1554 ->928|
|100160063,2;32768;1|9.1347|0.038156|0.042031|386 ->386|

A sixth colliding identity sample n=65537,a=3,L=131072 was measured separately by the same
entrypoint: unchanged0.062722ms, character0.054420ms; scans642->455. Raw allocations and
all input targets are in results.json. Re-running validate.py reproduces every case,
although new timings naturally need not equal the archived host sample.

Interpretation: the exact profile readout avoids unnecessary weighted-population expansion;
this is not a generic order-search advance. Character pruning reduced single-target scan
counts by about29%, not50% (the square-root search balances table and giant costs). It
was faster in those measured single-target negative-character cases, but58% SLOWER in one
16-target case, despite fewer scans. Character-positive/no-exclusion setup also slowed a
case. Therefore retain it as an OPTIONAL strategy, never an unconditional speedup/default.
The right baseline is unchanged bounded BSGS with the SAME affine observer, not unweighted
output or a known-order oracle. Positive reweighting does not improve the collision horizon.

## 6. Literature, preservation and next unresolved unit

One actual dedicated Scholar job was submitted to KQB Issue187 and matched comment
5772200234. The job returned3 title/snippet records (PARTIAL); the wrapper state was FAILED.
No full paper was obtained. The matching query, request hash and observed payload are
preserved, and snippets are not theorem evidence. Primary public implementation context:
Sage arithmetic Jacobi documentation and generic bounded BSGS documentation. The arguments
above are explicit elementary derivations; no historical-priority claim is made.

This bounded unit closes the selected affine-observer and Jacobi-constraint tasks. A useful
next mathematics question is to characterize broader positive profiles whose lag correlation
is strictly decreasing, and/or which structured sparse profiles retain enough differences
to identify order. Neither arbitrary positivity nor character agreement suffices. Preserve
these failure witnesses instead of reclassifying unknown branches as absent.

Reproduce:

    PYTHONPATH=src pytest -q tests
    PYTHONPATH=src python research_notes/power_affine_character_20260922_16243626C61A/validate.py

Source, test, validator and result digests are in MANIFEST.json. Publication is candidate
provenance only. No RSA-270 execution, full-repository certification, independent reviewer,
Lean, Foundation promotion, new top-level tool family or external persistent executor.
