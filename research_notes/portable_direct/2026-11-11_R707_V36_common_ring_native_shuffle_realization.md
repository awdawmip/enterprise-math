# R707 — Common native V36 ring realizes the full R706 BRC packet-shuffle histogram

Date: 2026-11-11 (Asia/Shanghai).
Researcher-ID: EM-X6-7D75EC.
Research-Activity-ID: RA-DD67F86B87BABC853E154219.
Mother task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Classification: author-side exact model theorem, finite independent checker; UNREVIEWED, no formal CLAIM, Result, or Foundation admission.
Frozen task science pin: a72226e2430ffa4786321ac86e7f0c599d5f0389 (unchanged).

## Research question and existing exact sources

R703 and R706 counted based active-triad packet shuffles by the S3 word product. Their next open question was whether those **intermediate event words** can actually occur under an X6 network triad-update rule. This note proves a constructive YES for the exact V36 directed-copy V20 ring model, on one *fixed ring topology per packet count*, with explicit distinct initial active-triad configurations. This is stronger than formal concatenability of loop packets.

Immutable sources:
- V17 canonical axis-slot replacement holonomy: `research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`, blob 42b810a8f82c504833027da17884cc4fb2943e5b.
- V20 canonical one-hot pure-triadic coupling: `research_notes/X6_PURE_TRIADIC_FIELD_COUPLING_V20_20260906.md`, blob 057fd80774200581886022c2e2cbbc9753e5380b.
- V29 nonnegative PASS/TRANSFER event ledger: `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md`, blob 6849ebd3fc776fb7da3b46627376490aba3dad99.
- V36 universal directed-ring realization: `research_notes/X6_ACTIVE_LOOP_TO_DIRECTED_RING_REALIZATION_V36_20260906.md`, blob b104e09cdb7479d0d981492ddfb20b713cc817d9.
- V38 two bow-tie based loops: `research_notes/X6_ZERO_CURRENT_NONABELIAN_COMMUTATOR_MEMORY_V38_20260906.md`, blob b627dd6265744669c438417bb19e896814a94be1.
- V39 operation-safe (j,h) observation: `research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md`, blob 8151d0b6a4b65225b93d858bbc8a5d7037bf9cef.
- R706: `research_notes/portable_direct/2026-11-11_R706_S3_shuffle_closed_form_and_bias.md`, commit 16fd003aaaa88d221db442c9e048f9af6878487d.

Typed BRC population: **oriented, labeled packet orderings** of the multiset with k copies each of A,A^{-1} and l copies each of B,B^{-1}. An ordering is not a uniformly random physical history. The observer is the V17 holonomy at the base Cell after one full ring period. The V29 ledger below is an explicitly specified *compatible count-event overlay*, not a derived rate/scheduler coupling.

## Theorem 1 — common fixed-topology native realization for every packet shuffle

Let the base active triad be 012 and define the four V38 cyclic active-triad packets:

```text
A:   012 -> 013 -> 023 -> 012
A^-: 012 -> 023 -> 013 -> 012
B:   012 -> 023 -> 123 -> 012
B^-: 012 -> 123 -> 023 -> 012
```

Let k,l be nonnegative integers with q=2k+2l >= 1. For every oriented ordering w of these q packets, form the closed active-triad walk W(w) by concatenating the q three-step packets, taking the shared 012 endpoints only once. It has length m=3q=6(k+l) in native J(6,3) transitions. Every step replaces exactly one of the six native axes.

**Claim.** On one directed m-Cell context ring with edges i -> i+1 (mod m), one fixed V20 pure-triadic coupling and one fixed synchronous update law, there exists an initial triad state field (depending on w) for which Cell 0 follows exactly W(w), returns to 012 after m layers, and has holonomy equal to the V38/V39 ordered packet product h(w). The **graph and update law are identical across all w for the fixed k,l**.

**Proof.** Write the cyclic word W(w)=(S_0,...,S_{m-1}) with S_0=012 and S_m=S_0. Each S_i ~ S_{i+1} in the Johnson adjacency J(6,3), including packet boundaries. Initialize Cell i in state S_i. The V36 one-hot V20 coupling satisfies K(T,T)=6, K(U,T)<6 for U != T. Since S_{i+1} is among the allowed J(6,3) next states of S_i, it is the unique score maximizer at Cell i when the context is its clockwise neighbor. Thus each synchronous layer implements X_i(t+1)=X_{i+1}(t). By induction X_i(t)=S_{i+t mod m}. Hence Cell 0 traverses the prescribed walk and returns after m layers. Its canonical V17 slot replacement is precisely the sequential V38 packet holonomy, using the V39 composition convention. Nothing in the ring topology or transition rule depends on the ordering. QED.

This construction works simultaneously for all oriented shuffles on the same physical **directed cycle topology**, but requires potentially different complete initial active-triad fields. It does not claim two distinct deterministic outcomes from one fully identical initial microstate. For q=0 the empty history is the identity; no positive-length ring is needed.

## Corollary 2 — all R706 histogram classes are dynamically attainable in the V36 model

The ordering-to-holonomy map on native ring initializations has exactly the multiset histogram R706 computed at packet level, since every ordering is realized and its frame product is unchanged. Put C=binom(2k+2l,2k), D=sum_{r=0}^{min(k,l)} (k+l)!/((k-r)!(l-r)!(2r)!), and z=binom(2k,k)binom(2l,l). For k,l>0, the V36 realizations cover the three distinct even holonomies with exact oriented word multiplicities:

```text
identity: z*(C+2D)/3
AB:       z*(C-D)/3
BA:       z*(C-D)/3
```

This is an exact count of *initially specified word configurations* in the constructed deterministic ring model, not a physical probability or an invariant measure on the ring's full state space.

For k=l=1 there are 24 oriented words, histogram (16,4,4), with m=12 Cells. For k=l=2 there are 2520 words, histogram (1296,612,612), with m=24 Cells.

## Proposition 3 — an identical legal V29 TRANSFER ledger can be overlaid

Fix one context ring of m Cells as in Theorem 1 and a permitted interface port p at each Cell. Declare the same V29 transfer event schedule, independent of w: for each of the m synchronous relation layers, serialize in a fixed order precisely one matched `TRANSFER(i:p -> i+1:p)` for every ring edge i, then execute the synchronous V36 triad update. The V29 event grammar admits each such matched transfer along a declared connection; its additive counts stay nonnegative. Starting at zero, every Cell has final M=0, Rin[p]=Rout[p]=m, all other entries zero. Every edge has m positive oriented transfer occurrences. Hence complete V29 count ledgers and net cycle chains are equal for every w. The common net cycle chain is m times the directed ring cycle (in general nonzero).

This is a legitimate **explicit combined trace under the declared product schedule** because V29 transfers do not modify the V20 active-triad state and V20 ring selection does not read cumulative transfer counts. However, V29 itself does not derive the chosen schedule from an autonomous flow law, nor certify a unique coupled scheduler when additional port-state dependencies are imposed. The result establishes **existence under the current V20/V29 compatible trace grammar**, not a universal classification of every future native event scheduler. In particular, it does not replace R703's *zero-net-current packet-accounting* witness by a zero-net-current physical ring witness.

## Exact counterexample on one 12-Cell ring

With the same 12-Cell directed context graph, the same V20 update, the same Cell-0 start/end triad 012 and the same V29 overlay ledger M=0, Rin=Rout=12 at every Cell, the following distinct global initial fields give three different final S3 holonomies:

```text
H0 = A ; A^- ; B ; B^- :  (0,1,2)
H1 = A ; B ; A^- ; B^- :  (2,0,1)
H2 = B ; A ; B^- ; A^- :  (1,2,0)
```

Therefore the coarsened observer retaining Cell-0 endpoint, ring topology, full V29 counts and fixed update law loses a three-element holonomy fiber. At least ceil(log2(3))=2 bits of extra history information are needed to answer the V39 exact h-query for this finite family. Full initial triad configurations distinguish these histories; this is an observer-specific repair claim, not a claim about identical full initial physical states.

## Exact finite executable check

`R707_NATIVE_RING_SHUFFLE_VERIFY.py` independently implements the canonical slot replacement, validates J(6,3) adjacency of every constituent step and cross-packet join, simulates m synchronous copy-ring layers for each distinct oriented packet ordering, and accumulates the resulting Cell-0 frame tuple. It checks the R706 binomial/factorial closed histogram for (k,l)=(1,1),(1,2),(2,1),(2,2): respectively 24, 180, 180, 2520 full oriented words, 2904 total checked realizations. It also verifies the three displayed 12-Cell witnesses. All integer assertions passed: `R707_NATIVE_RING_BRC_SHUFFLES_EXACT_PASS`.

The checker performs the V36 consequence X_i(t+1)=X_{i+1}(t) and uses V36's published K unique-max lemma as an imported exact model premise. The V29 overlay counts are derived symbolically from its explicit schedule, with no continuous/arbitrary-precision approximation.

## Remaining exact research unit

Determine which event-driven V29 PASS/TRANSFER schedulers can themselves enforce (rather than merely permit) the V36 context shift with matched port/stock and source constraints. Then intersect the set of legal initial full Cell fields with one fixed shared initial macrostate or reset/seed protocol; enumerate resulting reachable S3 histogram and seek a zero-net-current realization under genuine coupled native event updates. Preserve full BRC word provenance until the relevant future-operation quotient has been proved.
