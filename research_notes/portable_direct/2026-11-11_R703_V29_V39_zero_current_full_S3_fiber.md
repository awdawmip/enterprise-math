# R703 — Three-way zero-current holonomy fiber over an identical complete V29 event ledger

Date: 2026-11-11 (Asia/Shanghai). Mother task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`. Classification: author-side exact theorem + finite exact verification, **UNREVIEWED**. No formal native CLAIM, Result, Working Truth, Foundation or real-world dynamical calibration asserted. The scientific task's original source pins (including `a72226e2430ffa4786321ac86e7f0c599d5f0389`) remain unchanged.

## Sources and exact BRC carrier

- V29 exact additive PASS/TRANSFER ledger: `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md`, blob `6849ebd3fc776fb7da3b46627376490aba3dad99`.
- V38 two genuine based active-triad X6 bow-tie loop packets A,B, their inverses and commutator: `research_notes/X6_ZERO_CURRENT_NONABELIAN_COMMUTATOR_MEMORY_V38_20260906.md`, blob `b627dd6265744669c438417bb19e896814a94be1`. Those packets start and finish at support 012 and have transposition holonomies A=(0,2,1) and B=(1,0,2), with noncommuting composition; inverse packets have inverse transfer chains and inverse holonomies.
- V39 operation-safe `(j,h)` based-loop port, with `h(gamma;r)=h(r) o h(gamma)`: `research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md`, blob `8151d0b6a4b65225b93d858bbc8a5d7037bf9cef`.
- R701 exact V29 count-ledger fibers at `bd3449ee630dee0cacbdedccbc7990bc55e01017`; R702 joint divergence/PASS fibers at `e843d70bb7e43532449bb924a3408550b61a2f2c`. This unit studies an *additional temporal/S3 fiber that survives even when the full V29 count ledger and packet multiset are retained*, rather than repeating those count-fiber formulas.
- P000 V5 native X6 spatial and triadic state are retained. The loop packets are composite native paths, with label, direction and sequential order as part of the typed BRC carrier. Group transport is derived from V38/V39, not a replacement for typed native Cell steps.

## Theorem 1: exact S3 holonomy-support classification of two based packets

Let A,B be two distinct noncommuting transpositions in S3. For nonnegative integers a,b, define `W_(a,b)(g)` to be the number of words of length a+b with exactly a copies of A and b copies of B and resulting ordered holonomy g, using the V39 composition convention. Let `S_(a,b)={g:W_(a,b)(g)>0}`.

Then **for every a,b>=0**:

```
|S_(a,b)| = 1, if a*b=0;
          = 2, if min(a,b)=1 and a*b>0;
          = 3, if min(a,b)>=2.
```

Moreover every g in this support has sign (-1)^(a+b); when a,b>=2, the support is *the entire three-element parity coset* of S3.

**Proof.** Every word has a+b transpositions, so parity is fixed. Each parity coset in S3 contains exactly three elements, proving |S|<=3. If either count is zero, only one group word exists. If a=1 and b>=1, every shuffle is `B^i A B^(b-i)`, where its group value depends only on i modulo 2, since B²=e. Both parities occur (i=0,1) and yield distinct products because AB!=BA. The case b=1 is symmetric. If a=b=2, the three words `AABB`, `ABAB`, `BABA` evaluate to e and the two distinct nonidentity 3-cycles: AB has order three, and (AB)² and (BA)²=(AB) are distinct. For any a,b>=2, append the same fixed suffix `A^(a-2)B^(b-2)` to each of these three words. This preserves word counts and multiplies all three holonomies on the same side by the same group element, hence preserves their distinctness. Fixed parity supplies the matching upper bound. QED.

This statement is a *closed symbolic theorem*; its exact dynamic-programming checker below is independent finite regression evidence.

## Theorem 2: full three-value frame ambiguity with zero transfer current and identical V29 full ledger

Fix positive integers k,l. Take the actual V38 based X6 packets A, A^{-1}, B, B^{-1} and consider *every sequential permutation* of the same packet multiset with exactly k copies of A and k of A^{-1}, and l of B and l of B^{-1}. All packets return to the common based support, so their sequential composition belongs to the V39 based-loop language used by V38.

For **every** such permutation:
1. The exact net transfer chain is `j=k alpha(A)-k alpha(A)+l alpha(B)-l alpha(B)=0`.
2. The complete final nonnegative V29 `(M,Rin,Rout)` and full directional primitive event histogram are identical, because each packet's finite sequence of PASS/TRANSFER events is used with exactly the same multiplicity. V29 final ledger addition is independent of serialization, although its native time trace is not.
3. Since an S3 transposition is its own inverse, `h(A^{-1})=h(A)=A` and `h(B^{-1})=h(B)=B`. Thus the possible total transports are precisely `S_(2k,2l)=A3={e,c,c^{-1}}`, a **three-element** set by Theorem 1.

Consequently, even the complete nonnegative V29 count ledger, the fixed packet multiset and `j=0` leave an *exact three-value* V39 holonomy ambiguity. A direct `h` query distinguishes every value; the optimal fixed-length repair is exactly `ceil(log2 3)=2` bits. Retaining the actual S3 element h is sufficient for the V39 `L_JH` continuation language and is compositional under appended based-loop packets.

**Explicit four-packet witnesses (k=l=1).** The following are *packet identities*, not new primitive directions:

```
H0 = A ; A^{-1} ; B ; B^{-1}       -> h=e
H+ = A ; B ; A^{-1} ; B^{-1}       -> h=c
H- = B ; A ; B^{-1} ; A^{-1}       -> h=c^{-1}
```

The two nontrivial 3-cycles may exchange the labels c/c^{-1} under the alternative permutation-action convention; with this note's V39 left-composition convention and A=(0,2,1), B=(1,0,2), the explicit images are H+=(2,0,1), H-=(1,2,0). The invariant result is the full even coset, regardless of notation. This *strengthens* V38's two-history witness to three pairwise-distinct future-holonomy outputs at identical exact zero current and event multiplicities.

**Proof of optimality.** With the full count ledger and the exact multiset fixed, the three proven histories remain distinct under V39's direct h query. One bit has at most two codes; two bits code three outcomes. Sufficiency follows from keeping their exact h value and V39 compositionality. QED.

## Theorem 3: exact number of shuffles realizing each holonomy

For labeled packet *types* A and B, define `W_(a,b)(g)` as in Theorem 1. For a,b>=0 the finite recursion is

```
W_(0,0)(e)=1; all other W_(0,0)(g)=0;
W_(a,b)(g) = W_(a-1,b)(A^{-1} o g) + W_(a,b-1)(B^{-1} o g)
```

with invalid negative-count terms interpreted as zero, and left multiplication convention. This follows by the unique last packet of each word and is equivalent in formal group algebra to

```
sum_(a,b>=0) sum_(g in S3) W_(a,b)(g) g x^a y^b
       = (1-x A-y B)^(-1).
```

The total is `sum_g W_(a,b)(g)=binomial(a+b,a)`.

When A and A^{-1}, B and B^{-1} are distinguished *packet orientations* but have identical respective transposition holonomies, every coarse A/B word with counts (2k,2l) admits exactly `binomial(2k,k)*binomial(2l,l)` assignments of forward/reverse names. Hence the exact histogram of the fixed zero-current packet multiset is

```
H_(k,l)(g) = binomial(2k,k) binomial(2l,l) W_(2k,2l)(g).
```

For k=l=1, the six binary packet-type shuffles have holonomy counts `(e,c,c^{-1})=(4,1,1)`; the 24 permutations of four distinguishable directed packets have the **exact multiplicities (16,4,4)**. These are history counts, not probability assertions.

## Exact computation and scope

The accompanying JavaScript checker performs big-integer DP over every `0<=a,b<=24` (625 complete count pairs), checks support classification and parity at each count pair, verifies `sum_g W_(a,b)(g)=binomial(a+b,a)`, and checks the exact three four-packet witnesses and selected distributions. Output: `R703_S3_TWO_PACKET_SUPPORT_EXACT_PASS`. It stores a JSON summary with generator convention and selected exact distributions. This is an exact regression check; the three theorems above stand on their group-theoretic proofs.

The construction uses genuine V38 native-X6 *based closed packets* and V29's declared additive event grammar. It preserves ordered packet sequences and the V39 operation language; a separately coupled scheduler acting on intermediate states would require its own admissibility proof and may constrain the available shuffles.

## Next precise unit

Examine X6 native Link/Port and active-triad update legality **at intermediate event time** to determine which permutations remain reachable when the scheduler/Cell state is allowed to constrain packet composition. If every based V38 packet composition remains admissible, the R703 three-value fiber is already a constructive minimal holonomy-repair witness for the native event stream; otherwise calculate the reachable sublanguage and its exact holonomy support by a product-state automaton rather than assuming unconstrained permutations. Preserve the frozen Task pin and parent triadic closure/rotation-covariance objective.
