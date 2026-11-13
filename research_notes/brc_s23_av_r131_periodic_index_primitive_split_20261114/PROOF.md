# R131 — Period-quotiented exact S23 index and a primitive event-sweep lower bound

Date: 2026-11-14 (Asia/Shanghai). Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Research type: independent author-side **S23 auxiliary observer**. Exact predecessors:
- R127 `72f6de415d45fbd9a0a3bfde7aae36ccc99d0b93`, gcd-period observation;
- R129 `ddef5881c7e9996fbc08c6f48cd0c387606d035d`, event completeness and circular period quotient;
- R130 `7040bd2b6f134ea105f75370f0e35f1294818b64`, sparse event log and immutable index.

## Definition and question

For arbitrary integers `A,d,E`, rational `x`, `m>=1`, and real phase `theta`, define the length-m binary word

`S_i(theta) = 1[ { x+(A+i*d)*theta } < { E*theta } ]` for `i=0,...,m-1`,

with fractional part `{z}=z-floor(z)`. This is the same directed-half-open-arc rotated auxiliary observer used in R126–R130. R129.4 proves a period `1/g` for `g=gcd(|A|,|d|,|E|)>0`. R130 constructs an exact sparse event trace and point-index on a bounded interval. This note composes these established operations and distinguishes its coefficient sensitivity from an unavoidable raw-event regime.

## Theorem R131.1 — exact normal-form oracle for arbitrary phase range

Suppose `g>0`, and put `a=A/g`, `b=d/g`, `e=E/g`. For every real theta, define `t={g*theta}`, with `0<=t<1`. Then, *coordinate by coordinate and at every endpoint*, one has

`S_i(theta) = 1[ { x+(a+i*b)*t } < { e*t } ] =: T_i(t)`.

Furthermore `T_i(0)=0` for all i. Let `C'` be R129's exact event set for the normalized coefficients `(a,b,e)` on the open interval `(0,1)`; build R130's sparse log and R130.2's persistent cut/right-index on this one interval. Store one additional all-zero singleton word for t=0.

Then an exact, immutable random-access oracle for `S_i(theta)` on *any* rational input theta, including negative phases, lifted cuts, and period endpoints, is:

1. calculate `t = g*theta - floor(g*theta)` with exact rational arithmetic;
2. if `t=0`, return zero;
3. otherwise, binary-search `C'`, choose the singleton root at equality, the immediately preceding right-open root between events, or the initial open root before the first cut;
4. descend the persistent binary word tree to bit i.

The R130 word-index proof applies without change to all `0<t<1`; the new component is an exact reduction of an arbitrarily long phase range to one primitive period *while preserving singleton events*. Given `Q=|C'|` and `U` actual sparse point replacements in the normalized log, additional persistent indexing requires `O(m+U log(m+1))` binary node operations and `O(m+Q+U log(m+1))` nodes/references. A point query needs `O(log(Q+1)+log(m+1))` index/comparison operations **plus exact modulo/floor and rational-arithmetic bit costs**. Root construction/sorting and the `m+2 J_total` normalized indicator evaluations remain those of R130, measured using `a,b,e`, rather than `A,d,E`. Outputting a full word costs at least `m` bits.

*Proof.* Since `g theta = floor(g theta)+t` and every `a+i b`, `e` is an integer,

`{x+(A+i d)theta}={x+(a+i b) t}`, `{E theta}={e t}`.

This preserves strict inequality at all phases, not merely away from cuts. At t=0 the right fractional part is zero and the strict inequality is false for every i. On (0,1), R129 gives precisely the event partition and R130 recovers each singleton/right interval state. Its persistent index is exact by structural induction over the cut order. Composition proves the oracle and the stated operation counts.

If `g=0`, all `A=d=E=0`, so every indicator is identically zero; a constant oracle handles this case.

## Corollary R131.1a — coefficient-scale invariance

For fixed primitive coefficients `(a,b,e)`, x and m, the family `(A,d,E)=(g a,g b,g e)` has *exactly the same normalized event index* for every positive integer g. The number of stored cuts, transition deltas and tree nodes is independent of g, while the exact integer arithmetic to compute `{g theta}` scales with its binary representation.

For instance, take `x=A=0,d=E=g,m=32`. The index has exactly 307 interior normalized event cuts and 1,800 recorded replacement entries for each tested `g` in `{1,10^3,10^12,10^90}`. Over the unnormalized interval `(0,1)`, the `g-1` distinct residues `j/g` alone are event points of `E theta` and include actual singleton word changes (already at bit i=0, whose value is 1 away from these cuts and 0 at them). Thus the unnormalized event materialization has at least `g-1` genuine cut points; the quotient index avoids enumerating them when answering phase queries.

## Theorem R131.2 — primitive coefficient counter-regime

For every integer `K>=2`, set

`x=0, A=K, d=1, E=1, m=3, I=(0,1)`.

Then `gcd(|A|,|d|,|E|)=1`, and at each `theta_j=j/K`, `1<=j<K`, the first bit has a genuine discontinuity of its exact strict-indicator value:

`S_0(theta_j-epsilon)=0,quad S_0(theta_j)=S_0(theta_j+epsilon)=1`

for all sufficiently small positive epsilon. Consequently any R129/R130-type event trace explicitly storing all genuine chronological signature-change phases on I needs at least `K-1` such cuts, despite at most `2^3=8` distinct length-three signatures. Taking `K=2^n` shows that the event-trace size can grow exponentially in the bit length `n+O(1)` of the coefficients even for fixed m and primitive gcd 1.

*Proof.* At the named crossing `K theta_j=j`, so `{K theta_j}=0 < {theta_j}=j/K` and `S_0(theta_j)=1`. Just to the left, `{K theta}` approaches 1 while `{theta}` approaches `j/K<1`, hence `S_0=0`. Just to the right, `{K theta}` approaches 0 while `{theta}` is positive, hence `S_0=1`. These `K-1` rational phases are distinct and lie strictly within I. The gcd and word-count claims follow immediately.

**Scope of this lower bound:** chronological explicit cut-index methods, including R130's unmodified event list. It is not a lower bound for all possible symbolic/compressed representations, nor for the decision problem “does any phase realize a given word?” The coefficient-independent R126/R127 feasibility routes and R128 rotation-word candidate routes remain alternatives for such questions.

## Computation, provenance and unresolved question

Companion `check_r131.py` is self-contained: exact Python `Fraction` phase evaluation, normalized R130 sparse cut construction, persistent copy-on-path tree, and quotient query. It tests 140 seeded signed/rational cases, 6 edge cases, 225,642 exact bit comparisons against independent direct evaluation, including negative phases and lifted event/boundary points. All tested word queries match. For the scale family `g=1,10^3,10^12,10^90`, the indexed cut/delta counts remain 307/1,800; for primitive K=11,101,1001, all K-1 proposed genuine jumps passed direct exact left/at/right checks.

Exact execution returned `R131_PERIODIC_PRIMITIVE_SPLIT_PASS`. The script writes `verification_r131.json`. Uncontrolled CPython wall times are diagnostic, not an asymptotic certificate; all displayed arithmetic identities and strict-boundary assertions are checked exactly.

Next: implement a hybrid *word-set feasibility* engine which selects between normalized event enumeration and fixed-dimensional 2/3-integer feasibility using a sufficient coefficient-sensitive cost inequality. Compare total preprocessing, bit costs, deduplication, memory, and recovered rational witnesses on primitive large-K examples. Any transfer from this auxiliary phase observer to named X6 Cell/Link/Port events requires its own joint-state observer bridge under P000.

No formal task publication, native CLAIM, independent acceptance, or physical dynamics claim is created by this note.
