# PREFIX-850 — Projective order and logarithmic-width tracking of changing named BRC sources

**Date:** 2026-11-17  
**Status:** AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED  
**Frozen scientific input:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`, unchanged.  
**Dependencies:** PREFIX-847 (single named-source local-update difference obstruction), PREFIX-848 (autonomous unsynchronized stream), PREFIX-849 (five-source four-heartbeat threshold).  
**Scope:** abstract, declared, positive-integer Q-only named BRC scalar readout. This paper neither posits a native X6 event nor changes P000. It distinguishes a synchronized decoder holding the previous complete source state from the autonomous finite-window decoder of PREFIX-848/849.

## 1. Problem and exact state/readout types

Let `p>=1` and let each named weight be `w_i∈{1,2}`. Let `x_i=w_i-1∈{0,1}` and define the identity-preserving packed integer

`U(x)=∑_{i=0}^{p-1}2^i x_i`, with `0<=U<2^p`.

The physical labels `i` are retained, not quotiented by permutations. An allowed heartbeat updates **at most one named source** (a single bit flip), including the no-change transition. Write `H(x)={x}∪{x⊕2^i:0<=i<p}` for the `p+1` possible successors.

As in the earlier auxiliary BRC observer, the scalar at time `t>=1` is
`Y_t=c_t(S_0+U(x_t)) mod m`, `c_t=2^{floor(t/2)}`, with fixed known `S_0`, `a=2,b=1`. The receiver knows the preceding **full named state** `x_{t-1}`; this is a conditional local-update model. It cannot assume that state is known when first joining the stream.

For odd `q>1` define the *projective binary order*

`h(q)=min{d>=1 : 2^d≡1 or -1 (mod q)}`.

This exists for every odd `q>1`; it depends on the equivalence of powers under the sign action, and is not the ordinary multiplicative order (though `h(q)` divides it).

## 2. Exact local-update injectivity theorem

**Theorem 850-A.** For any odd `q>1`, the map `z↦U(z) mod q` is injective on every Hamming-radius-one successor set `H(x)`, uniformly over all binary named configurations `x∈{0,1}^p`, if and only if

`h(q)>=p`.

Equivalently, the `2p` residues `{+2^i,-2^i:0<=i<p}` are all distinct and nonzero modulo `q`.

*Proof.* The difference between no change and flipping bit `i` is `±2^i`, never divisible by odd `q>1`. The difference between flipping `i` and flipping `j`, `i<j`, is `s_i2^i-s_j2^j`, where `s_i,s_j∈{+1,-1}` depend on the two current bits. Each of the four sign choices occurs for some source state `x`. Because `2^i` is invertible modulo odd `q`, such a collision occurs for some `x` exactly if `2^{j-i}≡±1 (mod q)`. Distances `j-i` range over `1,...,p-1`. Their exclusion is exactly `h(q)>=p`, establishing both directions. The signed-residue statement is the same collision criterion, including distinctness from zero. QED.

**Corollary 850-B (minimum all-time raw modulus).** Under the specified `c_t=2^{floor(t/2)}` gain and a single fixed raw modulus `m`, the update can be decoded for every state and every future heartbeat from the known previous state if and only if the odd part `q=m/2^{v_2(m)}` has `h(q)>=p`.

*Proof.* The effective modulus of the readout is `m/gcd(m,c_t)`. Since `c_t` is a growing power of 2, its effective modulus eventually stabilizes at the odd part `q`. If `h(q)<p`, Theorem 850-A supplies a collision for some known previous source state at every sufficiently late heartbeat. Conversely, if `h(q)>=p`, reduction modulo `q` and inversion of the known odd-modulus gain recovers `U(x_t) mod q`, giving a unique successor for all times. Observing modulo a multiple `m` cannot reduce this discriminating information. QED.

It follows that the least fixed raw modulus is the **odd** number

`q_*(p)=min{q odd, q>=3 : h(q)>=p}`,

and the exact best fixed raw port width is `B_*(p)=ceil(log_2 q_*(p))`.

## 3. Universal linear modulus with a finite-memory synchronized decoder

**Lemma 850-C.** For every `k>=1`:

`h(3^k)=3^{k-1}`.

*Proof.* The familiar exact integer valuation `v_3(2^{2·3^r}-1)=r+1` follows by induction from `2^2-1=3` and the factorization `A^3-1=(A-1)(A^2+A+1)` for `A≡1 (mod 3)`: the second factor has 3-adic valuation exactly one. Thus the multiplicative order of 2 modulo `3^k` is precisely `2·3^{k-1}`: its order divides `phi(3^k)=2·3^{k-1}`, has a factor two because `2≡-1 (mod3)`, and cannot divide `2·3^{k-2}` (when `k>=2`) by the valuation. Any `2^d≡±1` implies `2^{2d}≡1`; therefore `3^{k-1}` divides `d`. Conversely `2^{3^{k-1}}≡-1 (mod 3^k)`: its square is one and its residue is `-1 (mod3)`, and equivalently this follows by the cubing induction `v_3(2^{3^r}+1)=r+1`. Hence the smallest such `d` is `3^{k-1}`. QED.

**Theorem 850-D (uniform logarithmic-width update).** Put `k=1+ceil(log_3 p)` interpreted as the least integer with `3^{k-1}>=p`, and set `m=3^k`. Then a synchronized decoder holding `x_{t-1}` recovers the complete named state `x_t` from **one modular BRC scalar every heartbeat**, for every permitted infinite update trajectory. Furthermore

`2p+1 <= q_*(p) <= 3^k < 9p`

and consequently `B_*(p)=log_2(p)+O(1)`. Explicitly,

`ceil(log_2(2p+1)) <= B_*(p) <= ceil(log_2(3^k)) <= ceil(log_2(9p))`.

*Proof.* Lemma 850-C gives `h(3^k)=3^{k-1}>=p`, so Theorem 850-A guarantees unique identification of each successor from its reduced residue. The receiver computes the modular inverse of `c_t` modulo odd `m` and subtracts the known offset `S_0`. It then enumerates the `p+1` successors of the stored old state and selects the unique matching residue; this updates the stored state. Induction over heartbeats proves perpetual exact recovery once synchronized.

For the lower bound, Theorem 850-A forces the `2p` signed powers to occupy distinct nonzero residue classes, so `q>=2p+1`. For the upper bound, by minimality of `k`, `3^{k-2}<p` when `k>=2`, whence `3^k<9p`; `k=1,p=1` has `3<9`. The bit bounds follow. QED.

**Resource-accounting qualification.** The decoder stores `p` named bits of the last recovered state, knows `S_0` and the heartbeat index, and receives `B_*(p)` bits per heartbeat after synchronization. This is a **per-message bandwidth** improvement, not compression of the entire persistent state into `O(log p)` bits. Starting with an unknown source state generally requires a separate full-state synchronization message of at least `p` bits (or an independently proved multi-heartbeat scheme); the autonomous model in PREFIX-848/849 does not receive this side information. A generic unrestricted encoding of the `p+1` possible updates needs at least `ceil(log_2(p+1))` bits; the stronger `2p+1` modulus bound applies only to this fixed modular observer family.

## 4. Sharp lower-bound equality criterion

**Proposition 850-E.** The exact minimum `q_*(p)=2p+1` holds if and only if `q=2p+1` is prime and the subgroup `<2,-1>` equals the entire multiplicative group of residues modulo `q`. Equivalently, for this prime `q`, the order of 2 is either `2p`, or `p` with `p` odd.

*Proof.* If `q=2p+1` works, its `2p=q-1` signed powers are all distinct units. Thus `phi(q)>=q-1`, forcing prime `q`; they exhaust its unit group and generate the claimed subgroup. Conversely if the subgroup generated by 2 and -1 is the full `q-1=2p` element group, its projective period is `p` and Theorem 850-A yields admissibility at the counting lower bound. For a cyclic group of order `2p`, adjoining -1 to the cyclic subgroup of 2 makes the full group precisely when its order is `2p` or it is the odd index-two order `p` subgroup, proving the final equivalence. QED.

This is an exact conditional arithmetic criterion; it makes no claim of an unproved infinitude of primes with any specified primitive-root property.

## 5. Exact computational certificates and scope

The accompanying standalone Node.js BigInt checker returns `ALL_EXACT_ASSERTIONS_PASSED` and records:
- `q_*(p)`, its exact bit width, and an explicit 3-power construction for every `1<=p<=64` (64 finite exact minima, exhausting all smaller odd raw moduli).
- 198 exhaustive comparisons between the signed-power criterion and **every binary predecessor state plus each of its `p` possible flips** for `1<=p<=9`, over a declared range of odd moduli.
- The exact identity `h(3^k)=3^{k-1}` for `k=1,...,8`.

Reproduce from the repository root:
`node research_notes/portable_direct/PREFIX850_R6_BINARY_LOCAL_PROJECTIVE_PERIOD_CHECK.js > /tmp/PREFIX850_R6_results.json`

Selected exact minima:

| p | q_*(p) | B_*(p) | h(q_*(p)) |
|--:|--:|--:|--:|
| 1 | 3 | 2 | 1 |
| 3 | 7 | 3 | 3 |
| 5 | 11 | 4 | 5 |
| 6 | 13 | 4 | 6 |
| 9 | 19 | 5 | 9 |
| 12 | 29 | 5 | 14 |
| 18 | 37 | 6 | 18 |
| 24 | 53 | 6 | 26 |
| 30 | 61 | 6 | 30 |
| 64 | 131 | 8 | 65 |

An independent Python integer implementation additionally checked the odd-modulus criterion against all binary predecessor neighborhoods for `1<=p<=9`. All enumeration claims are finite and do not replace the general proofs above.

## 6. Relevance, boundaries and next questions

This result refines PREFIX-847's general finite difference-divisibility criterion when `W=2` by a signed-power projective-order characterization and a uniform, explicit **linear-in-p** modulus bound. It precisely separates the initially synchronized local-update model from the autonomous no-baseline model of PREFIX-848/849. The source names remain distinguishable throughout, and only the readout's stated transition set has been compressed.

No X6 Cell/Link/Port event realization, native heartbeat law, physical calibration, or permitted observer is established. The positive-integer Q-only BRC modular observer is an auxiliary arithmetic interface, not a native-space proof. P000, the six-dimensional Cell ontology and three-dimensional slice constraints remain unchanged.

Useful next problems: (i) determine exact `q_*(p)` or effective closed-form families beyond 64, avoiding assumptions on Artin-type primitive-root distributions; (ii) quantify synchronization/resynchronization costs under partial or lossy observer memory; (iii) develop exact lower bounds for **autonomous** finite-window mod streams as `p` grows, where this theorem's prior-state assumption is unavailable; (iv) seek a genuinely licensed X6 typed readout while retaining source/port/event provenance.

**Publication/authority boundary:** Author-level proof and finite regression only. Not independent peer review, Source Result admission, live shared X6 CLAIM, or native observer permission.
