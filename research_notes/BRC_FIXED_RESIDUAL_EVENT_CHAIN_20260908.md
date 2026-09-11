# Fixed-residual completion events form a reusable factor chain

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Status: elementary derivation, bounded positive certificates and indexed-batch timing; noncanonical research checkpoint.  
Global snapshot: `e76fdc883f9f4a3a93c1284340e38c55aeba0a6a`.  
Parent project frontier: `3b6d58809e1ec8af7f6fff25800dfe07315a4541`.

## Question, supplied information and reuse

The user asks for occasional inexpensive successes and for BRC states to be studied separately. The preceding [fixed-residual positive family](BRC_OCCASIONAL_HIT_STATE_REGIMES_20260908.md) supplies the starting identity. This continuation determines the exact event locations, retains the D/U split, and identifies a factor that can be reused between consecutive events.

For a prescribed residual `r >= 1`, the source integers are `N=J²+r`, with `J >= max(3,ceil(r/2))`. This ensures a canonical nonsquare state and proper factors at every completion event. The mathematical fiber is selected by r; an executing batch also receives its **complete ordered root interval**. The runtime carrier is not r alone. An arbitrary sparse input list would additionally require acquisition, grouping and membership operations that are outside this experiment.

The existing `point_cost_state` and `ceiling_completion_square_witness` are executed unchanged for validation. Their exact source hashes are in the certificate, with bytes checked against the previously pinned source identities. Reuse status is `REUSE_APPLIED` for the prior parametrization and `REUSE_EXECUTED` for those two BRC interfaces. The event recurrence extends the existing completion family; it is not claimed to be a new factorization principle.

The only data used in the executable are fixed small constructions below `2^19`. There is no external-integer input option or production dispatch change.

## Exact event positions and direction

Put

\[
A=2J+1-r.
\]

Immediate completion means `A=b²`, so the positive events are exactly

\[
\boxed{J_b=\frac{b^2+r-1}{2},\qquad b\equiv1-r\pmod2.}
\]

The prior note established this parametrization. Its additional ordered structure is

\[
\boxed{J_{b+2}-J_b=2b+2,\qquad
(J_{b+4}-J_{b+2})-(J_{b+2}-J_b)=4.}
\]

Thus one parity-adjusted square root locates the first event of a prescribed interval; subsequent event positions require integer additions. No square test is needed at the intervening root positions when the requested output is the complete event list for that interval.

For any `L <= H` inside the canonical range, define `b_-` as the smallest integer of parity `1-r` with `b_-² >= 2L+1-r`, and `b_+` as the largest integer of that parity with `b_+² <= 2H+1-r`. Then the exact positive count is

\[
\boxed{Q_r(L,H)=\max\left(0,1+\frac{b_+-b_-}{2}\right).}
\]

An empty root interval has count zero. All displayed quotients are integers after the parity adjustment.

The edit-cost directions have an especially simple event description:

\[
D:\ J_b\ge r\iff b^2\ge r+1,
\qquad
U:\ J_b\le r-1\iff b^2\le r-1.
\]

Consequently the separate counts are `Q_r(max(L,r),H)` and `Q_r(L,min(H,r-1))`, respectively. For each fixed r, the U segment is finite and the D segment contains infinitely many integer constructions. Canonical collapse remains downward in both cost populations. This is not a claim about prime density or the distribution of cryptographic inputs.

## Consecutive events share a factor

At an event write

\[
u_b=J_b+1-b=\frac{(b-1)^2+r}{2},\qquad
v_b=J_b+1+b=\frac{(b+1)^2+r}{2}.
\]

Then `N_b=u_b v_b`, and the next event satisfies

\[
\boxed{u_{b+2}=v_b,\qquad v_{b+2}=v_b+2b+4.}
\]

The factor chain is therefore

\[
N_b=u_bv_b,\qquad N_{b+2}=v_bw_b,
\quad w_b=u_b+4(b+1).
\]

The executable uses these additions to carry the factors between event outputs, and checks every product. A concrete positive pair in the downward population is

\[
r=10:\quad
299=17^2+10=13\cdot23,\qquad
851=29^2+10=23\cdot37.
\]

Here `b=5,7`, and the shared factor is 23. Both inputs are known semiprimes by construction.

For odd constructions, select `r mod 4` equal to 1 or 2, with the required b parity. The exact gcd is also controlled by the residual:

\[
\boxed{\gcd(N_b,N_{b+2})
=v_b\,\operatorname{oddpart}(\gcd(r+4,b+1)).}
\]

Proof: factor out `v_b`. Since `u_b` is odd,
`gcd(u_b,w_b)=gcd(u_b,4(b+1))=gcd(u_b,b+1)`.
The identity `2u_b=(b+1)(b-3)+(r+4)` identifies this last gcd with the odd part displayed above.

In particular, a unit correction gives exactly the shared factor. There are explicit infinite positive classes with this property: for `r=1 mod 4`, choose `b=2(r+4)h`; for `r=2 mod 4`, choose `b=(r+4)h+1`, with integer `h>=1`. These choices preserve parity and make the correction one. They construct integer pairs, not an asserted infinite family of prime triples.

This explains what the residual alone can retain: the possible gcd correction divides `oddpart(r+4)`. Locating a particular event still uses its index b or J. Once an event factor is certified, the next event reuses it; this does not provide the first event factor of an arbitrary supplied number for free.

## Bounded positive evidence

The fixed population consists of all odd `N=J²+r` in 32 complete fibers: `1<=r<=64`, `r mod 4 in {1,2}`, and `max(3,ceil(r/2))<=J<=512`.

| Initial direction | Prescribed odd states | Verified completion events | Known prime-pair events |
|---|---:|---:|---:|
| D | 7,695 | 418 | 68 |
| U | 255 | 77 | 22 |
| Total | 7,950 | 495 | 90 |

The direct finite enumeration and the recurrence return identical complete event lists. The run verifies 96 closed-form counts, 7,950 unchanged BRC point states and 495 unchanged completion-witness outputs. All 463 adjacent event pairs satisfy the shared-factor and exact gcd formulas; 373 have a unit correction. Among the adjacent pairs, 50 have three certified prime factors. These are overlapping pairs, not 100 independent input examples.

For all 90 known prime-pair events, an independent exact `Fraction` centered-sum check verifies the conditional hidden coordinate and earlier corrected moment identity:

\[
S=2(J+1),\qquad 9M_3=2S^3-9NS.
\]

The certificate includes every prime-pair event and all per-fiber counts. This population differs from the earlier 406-input cohort; its hits must not be added to that cohort's denominator or coverage total.

## Measured cost in complete indexed intervals

Both paths receive the same implicit complete fiber descriptions and return identical event lists. The direct path examines the odd root positions and square-tests each completion gap. The event path computes an initial seed per fiber and advances the position/factor recurrence. Both allocate outputs and verify every proposed factor product, sum and difference. Setup of the event seeds is inside the timed region; no stored event lookup table is supplied.

Final recorded run: CPython 3.14.6 on the host Windows runtime, seven shuffled-order rounds, 16 complete batches per method per round.

| Fiber interval view | Direct batch, microseconds | Recurrence batch, microseconds | Ratio of medians | Faster recurrence rounds |
|---|---:|---:|---:|---:|
| D only | 1,299.619 | 206.513 | 6.29x | 7/7 |
| U only | 65.838 | 42.231 | 1.56x | 7/7 |
| Complete combined interval | 1,368.769 | 240.956 | 5.68x | 7/7 |

The combined batch replaces 7,950 square-root calls with 32 seed calls and still verifies all 495 output products. Independent D/U runs use 32 and 30 seed calls, respectively; those separate runs are not the execution path of the combined batch.

These measurements establish a local advantage for enumerating completion events over **complete supplied indexed intervals**. Creating such an index from unrelated input integers, determining membership of a sparse list, imports and external data acquisition are not timed. Their costs are unmeasured; neither arbitrary-input factorization performance nor full-portfolio savings follows from this table. This restriction is part of the method contract, not a reason to discard the measured specialist.

## Artifacts and retained direction

```powershell
python experiments/brc_fixed_residual_event_chain_20260908.py --enterprise-root . --output-dir experiments
```

The companion JSON preserves source hashes, observer/cost contracts, exact counts, positive examples and all raw timing rounds. A final metadata-only clarification makes the complete-interval prerequisite explicit; it does not change the measured kernels. The mathematical and timing run completed in about 1.2 seconds on this host.

Retain this as a specialist for prepared complete residual fibers. Its new reusable facts are the event-spacing recurrence, shared-factor chain and residual-controlled gcd correction, with distinct D/U costs. Effectiveness on public RSA tasks remains unestablished. The full research goal stays active; this note does not promote a theorem, alter a production solver, or complete that broader request.
