# PREFIX-541 — Exact gate periodicity and tropical BRC–gate support fibers

Date: 2026-11-06. Line: RS-X6-NATIVE-ROTATION-DYNAMICS.
Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessors: PREFIX-539 local BRC cocycle and PREFIX-540 rooted BRC maximum.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
This is independent author-side research material, not an authenticated CLAIM or Result.

## Domain and observable
The four STAR triples are (1,3,6),(1,4,5),(2,3,5),(2,4,6). They determine 48 directed phases (star, previous signed axis, current signed axis), 144 legal phase edges, and two independent INNER/OUTER labels on each transition. The gate target T is (A,+L1,-L3), represented as (0,1,-3). A gate event occurs precisely when the transition arrives at T with present and previous labels INNER. The first-axis BRC cancellation count p is defined by the frozen native endpoint formula, equivalently PREFIX-539's local cocycle. For root s and macro-depth d, let S_s(d) be the set of attainable ordered pairs (p,h) of BRC cancellation and gate count. This is an exact observer projection; native Cell, order, phase, branch identities and multiplicities stay in the underlying carrier.

## Theorem 1 — sharp rooted gate maximum has 4-periodic increments
Define the max-plus operator on all 96 phase/previous-label states (i,b):

(Gv)(i,b) = max_{j in NEXT(i), e in {0,1}} ( 1[b=e=1 and j=T] + v(j,e) ).

An exhaustive finite evaluation over the *entire* 96-state system proves

G^5(0_96) = G(0_96) + 1_96.

Since G(v+c 1)=G(v)+c 1, applying G^(d-1) to both sides proves

G^(d+4)(0_96) = G^d(0_96)+1_96, for every integer d>=1.

Set H_s(d)=(G^d 0)(s,0), the sharp maximum gate count of a rooted labeled length-d path. Thus H_s(0)=0. For d>=1 write d-1=4k+r, 0<=r<=3. Then

H_s(d) = k + a_s[r], where a_s=(H_s(1),H_s(2),H_s(3),H_s(4)).

The 48 roots have exactly four initial profiles:
- (0,0,0,0): 6 roots;
- (0,0,0,1): 15 roots;
- (0,0,1,1): 18 roots;
- (0,1,1,1): 9 roots.

The all-depth proof uses a checked finite identity and the algebraic max-plus translation law, not extrapolation from bounded depths.

## Theorem 2 — each fixed-BRC support fiber is a full gate interval
For every root s, integer d>=0, and attainable p, there exists H_s(d,p)>=0 with

{h : (p,h) in S_s(d)} = {0,1,...,H_s(d,p)}.

Proof: Choose an actual labeled native phase path with p and maximum H_s(d,p) gate events. The target phase T has no self-transition, so no two gate arrivals are consecutive. On an arbitrary selected gate occurrence, replace the INNER label *arriving at T* by OUTER. This removes exactly that event. Only an event at the next transition could otherwise depend on the changed label, but that next transition cannot also arrive at T. Thus distinct gate events can be independently disabled without changing any phase or the first-axis BRC count. Retaining any selected subset of the H events constructs every h from 0 through H. The empty path d=0 is included. QED.

## Theorem 3 — a three-seed tropical recurrence computes the exact all-depth joint support
For phase i, let sigma(i) in {-1,0,1} be the current first-axis sign and epsilon(i)=abs(sigma(i)). For an initial sign r=sigma(s), PREFIX-539 proves the exact BRC additive increment

tau_r(i,j) = [epsilon(i)+epsilon(j)-abs(sigma(j)-r)+abs(sigma(i)-r)]/2 in {0,1}.

For seed r and memory state (i,b), let W^r_d(i,b;p) be the maximum possible gate count with precisely p accumulated BRC units in the next d steps, with minus infinity when p is unattainable. Initialize W^r_0(i,b;0)=0 for every state. The max-plus recurrence is

W^r_(d+1)(i,b;p) = max_{j in NEXT(i),e in {0,1}}
      ( 1[b=e=1 and j=T] + W^r_d(j,e;p-tau_r(i,j)) ).

Path decomposition and the BRC cocycle identity prove by induction that W is exact. Together with Theorem 2,

S_s(d) = { (p,h): W^r_d(s,0;p) is finite and 0<=h<=W^r_d(s,0;p) }.

All 48 fixed roots are computed using only three shared seed recurrences, each with 96 phase/label states. The support can therefore be represented by a one-dimensional height profile in p; it does not reconstruct the full two-variable coefficient values or individual native branches.

## Support-allocation consequences
Let M_s(d) be PREFIX-540's exact rooted maximum BRC p. The previous candidate region used 0<=h<=floor((d+2)/4) and h<=p<=M_s(d). Replacing the uniform gate cap by Theorem 1 gives

C_s(d)=sum_{h=0}^{H_s(d)} max(0,M_s(d)-h+1).

Theorem 3 further gives the *exact occupied support size*

K_s(d)=sum_{p:W^r_d(s,0;p) finite} (W^r_d(s,0;p)+1).

A separate raw labeled-path integer counter was executed for all 48 roots, d=0,...,24 (1200 full support comparisons). It uses the original BRC endpoint formula, not the tropical cocycle, and checks every occupied (p,h) pair, all positive path multiplicities, and all length-d totals 6^d. All checks passed.

At d=20, summed over 48 roots: 1440 previous candidate slots, 1426 sharp-gate slots, 1352 exact occupied slots.
At d=23: 1848, 1801, 1709.
At d=24: 2016, 1998, 1876.
The independent full polynomial counter also finds exactly 1876 nonzero joint coefficients at depth 24, agreeing with PREFIX-537.

## Reproduction and next dependency
Run the adjacent PREFIX541_compact_exact_certificate.py using Python standard library. The exact finite max-plus identity, root profiles, tropical recurrence and 1200 independent raw endpoint BRC comparisons are asserted before the program emits PREFIX541_EXACT_EXECUTION.json and ALL_CHECKS_PASS.

These theorems concern supports of the pinned four-STAR BRC/gate observer. For a full dynamic native Cell or time operation, retain the phase, branch order, Cell identity and provenance in the original typed carrier.

Next PREFIX-542: allocate only the exact tropical profile's reachable coefficient positions in a full integer joint counter, then compare end-to-end wall time, peak memory, profile setup and coefficient recovery against the 49-coordinate sparse rank-one lift. Examine whether joint Cell/provenance observer fibers admit further exact descent certificates.
