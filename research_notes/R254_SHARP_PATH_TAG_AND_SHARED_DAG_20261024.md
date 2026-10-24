# R254 — Sharp provenance-tag correction and exact shared BRC path DAG

**2026-10-24 · author-side exact mathematical result. Not a formally CLAIMed, independently reviewed, P000-heartbeat-admissible, or Foundation theorem.**

## Frozen authority and source

GLOBAL_KNOWLEDGE_V1 canonical main a52fe6f1ea886d219c9f4898c9a7cda48ef6134e; Enterprise Math Source canonical main 6f14c39fb618bf960c80c93345a7a7e2876a5256; P000 global file projects/enterprise-math/P000_REALITY_FOUNDATION.json, ACTIVE_LOCKED, blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Current protected ACTIVE worldview maintains six native spatial axes, one independent time dimension, no native plane and residual-faithful observers. The formal affine group below acts on all six signed coordinates relative to a chosen Cell, not on an independent lower-dimensional plane. This is an auxiliary finite BRC control model; neither a valid physical heartbeat update nor a valid final Cell address codec has been established.

Predecessor: R253 research note research_notes/R253_HOLONOMY_ONE_BIT_REPAIR_PROVENANCE_GROWTH_20261024.md at immutable commit b595842f59c9dcb9c16cae16a55d3070001c4069. Its previously established result was a coarse information bound \(b_m=m-O(\log m)\); R254 proves the sharp logarithmic *coefficient* and gives a serially closed, exact positive path-language representation.

## Precise positive BRC carrier

There are three NON-spatial control states \(Q=\{0,1,2\}\), two distinct unit-weight/multiplicity-one outgoing edges for each state, and all spatial effects act on the same six-axis relative chart:

$$
F_{\varepsilon,k}(z)=\operatorname{diag}(\varepsilon,\varepsilon,1,1,1,1)z+k e_1,\qquad
\varepsilon=\pm1,\quad k\in\mathbb Z.
$$

| source control | selector 0 (target, eta, b) | selector 1 (target, eta, b) |
|---:|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

Each edge carries effect \(F_{\eta,b}\). Source Affine.then(later) is chronological composition:

$$
(\varepsilon,k)\ {\rm then}\ (\eta,b)=(\eta\varepsilon,\eta k+b).
$$

Let \(p=-\varepsilon k\) be the first inverse-anchor coordinate. The declared *full-effect-and-terminal observer* of an ordered selector word \(w\in\{0,1\}^m\) from initial control \(s=0\) is

$$
O_m(w)=(q_m,\varepsilon_m,k_m)
\quad\Longleftrightarrow\quad(q_m,\varepsilon_m,p_m).
$$

The observer discards ordered source history. We are studying how much extra information is needed to reconstruct that word. The actual R193 source observer remains separately unverified.

## Theorem A — exact nonasymptotic bounds and sharp asymptotic order

Write \(M_m=\max_y |O_m^{-1}(y)|\), and \(C_m=\binom m{\lfloor m/2\rfloor}\). Then for every integer \(m\ge0\),

$$
\boxed{\left\lceil C_m/6\right\rceil\le M_m\le C_m.}
$$

If an extra fixed-width binary tag is attached to each full-effect/terminal atom and must allow recovery of its complete selector word at horizon \(m\), the *exact* minimum worst-fiber width is

$$
\boxed{b_m=\lceil\log_2 M_m\rceil.}
$$

Consequently, as \(m\rightarrow\infty\),

$$
\boxed{b_m=m-\frac12\log_2 m+O(1).}
$$

This sharpens the earlier \(m-O(\log m)\) statement: its logarithmic correction has coefficient \(1/2\). Observing terminal control plus complete affine holonomy, rather than only the inverse anchor, can save **at most three worst-fiber tag bits**, because it subdivides each anchor fiber into at most six subfibers.

### Full proof

For a chronological edge \(F_{\eta,b}\), the inverse anchor changes by

$$
p'=-\eta\varepsilon(\eta k+b)=p-\varepsilon'b,\qquad\varepsilon'=\eta\varepsilon.
$$

For either entering sign and each of the three control states, inspection of the two explicit edges shows that their \(p'-p\) increments form **exactly the multiset \(\{-1,+1\}\)**. Each edge has positive unit weight and multiplicity one. Therefore after forgetting control and holonomy the exact aggregate anchor histogram obeys

$$
A_0(p)={\bf1}_{p=0},\qquad
A_{m+1}(p)=A_m(p-1)+A_m(p+1).
$$

Induction/Pascal's rule gives

$$
A_m(p)=
\begin{cases}
\binom m{(m+p)/2}, & |p|\le m,\ p\equiv m\pmod2,\\
0,&\text{otherwise}.
\end{cases}
$$

The maximum anchor-only fiber is \(C_m\). For any given anchor, the refined observer has only three possible terminal controls times two holonomy signs, hence at most six atoms. By pigeonhole its largest refined atom has multiplicity at least \(\lceil C_m/6\rceil\). Every refined atom is a subset of an anchor fiber, so it has multiplicity at most \(C_m\). This proves the first displayed bound.

An injective source tag is required only within each observed fiber: at least \(M_m\) symbols are necessary; numbering its words \(0,\ldots,|\text{fiber}|-1\), with label reuse across different fibers, achieves that bound. The exact bit width is \(\lceil\log_2 M_m\rceil\), including the \(M_m=1\) zero-bit case. Finally the central-binomial asymptotic

$$
C_m=2^m\sqrt{\frac2{\pi m}}\,(1+O(1/m))
$$

implies \(\log_2 C_m=m-\tfrac12\log_2m+O(1)\). Taking \(\log_2\) of the six-factor inequalities and applying ceilings changes the result by a bounded amount. QED.

**Information-cost scope.** The theorem gives the size of *individual recoverable history tags conditioned on the effect/terminal observation*. It is NOT a lower bound on total bytes in a shared directed acyclic expression describing many histories simultaneously.

## Theorem B — exact source language, chronological composition and linear-size shared syntax

Let \(A\) be a finite alphabet of uniquely identified **physical directed edges**. Let \(G\) be the exact affine-effect monoid under chronological then, and \(W\) the multiplicative positive rational weight monoid. Set

$$
\mathcal M=W\times G\times A^*,
$$

with product

$$
(w,F,u)(v,H,vword)=(wv,F\ {\rm then}\ H,uvword).
$$

The positive integer monoid algebra \(\mathbb N[\mathcal M]\) retains ordered source histories, exact weights and noncommuting affine effects. Addition merges identical triples by **positive integer path multiplicity**, not by signed cancellation. Define the state-indexed one-step matrix

$$
K_{q,t}=\sum_{e:q\to t}[w_e,F_e,e]\in\mathbb N[\mathcal M].
$$

Then the matrix power \((K^m)_{s,t}\) is exactly the formal sum of all *ordered* length-\(m\) paths from \(s\) to \(t\). Proof is induction using matrix multiplication: every length-\(m+1\) path has a unique last edge and the preceding path's terminal control agrees with that edge's source. Weights multiply, affine effects compose with correct temporal order, and history words concatenate. Thus for time-port-aligned packets

$$
\boxed{K^{a+b}=K^aK^b}
$$

is a lossless serial-composition identity of source-annotated BRC. Summation over intermediate states preserves positive counts.

The coefficientwise erasure of the history word,

$$
\rho:[w,F,u]\mapsto[w,F],
$$

preserves the sum and chronological product and therefore induces the exact terminal-indexed original EffectHistogram/ControlPacket semantics on this finite edge model. But the map is NOT injective: the length-three selector histories **000** and **101** from initial control 0 both end in terminal 0 with effect \((\varepsilon,k)=(+1,-1)\), and are merged as a single positive-multiplicity-two terminal/effect atom.

A shared DAG realizes this formal algebra without enumerating every history. For fixed initial control \(s\) let \(D_0(s)=1\), \(D_0(q)=0\) otherwise. For each physical source-labeled edge \(e:q\to t\), retain the expression \(D_j(q)[w_e,F_e,e]\) and share earlier nodes. The exact recurrence is

$$
\boxed{D_{j+1}(t)=\sum_{e:q\to t}D_j(q)[w_e,F_e,e].}
$$

Each of the \(m\) layers uses at most \(|E|\) appended-product nodes and \(|Q|\) sum nodes. Therefore the entire expression for a fixed start has **\(O(m(|E|+|Q|))\)** syntax nodes; for this example \(|E|=6, |Q|=3\). Every edge-ID word is recovered by expanding the relevant DAG path; its source and destination compatibility, precise affine composition and positive path multiplicity are inherited by induction. One may concatenate two compatible DAG expressions using the displayed monoid product and sum over intermediate controls to obtain future-aligned serial composition.

This is an exact representational **upper bound**, not a minimum circuit-size theorem or a bound on the time needed to explicitly print \(2^m\) words. The exponential information demand for identifying an *individual* hidden source word and the linear syntax of a *shared generative expression* address different storage questions. QED.

## Independent finite evidence (not the basis for the infinite proof)

The author's Python exact dynamic program checked initial states 0 and 1, horizons 0..96 and the full binomial marginal/fiber inequalities; its independent DAG representation expanded through depth 11, checked syntax node counts through depth 64, checked explicit histories to depth 12 and 2,883 serial splits. A separate C++17 checker using boost::multiprecision::cpp_int checked the same counts 0..96 and independently enumerated paths through depth 12. Eleven selected heights were matched exactly across the two implementations.

| depth m | full ordered paths | largest effect/terminal fiber | exact tag bits |
|---:|---:|---:|---:|
| 3 | 8 | 2 | 1 |
| 12 | 4,096 | 250 | 8 |
| 24 | 16,777,216 | 705,854 | 20 |
| 48 | 281,474,976,710,656 | 8,233,429,852,978 | 43 |
| 64 | 18,446,744,073,709,551,616 | 465,428,353,188,420,746 | 59 |
| 96 | 79,228,162,514,264,337,593,543,950,336 | 1,625,701,140,345,181,560,104,470,766 | 91 |

At depth 64 the shared DAG has **564 syntax nodes** for start control 0, representing \(2^{64}\) histories. It was **not** explicitly expanded to \(2^{64}\) words; expansion was checked through depth 11. The 96-step counts are exact integer dynamic programming, not exhaustive word listing. Infinite-horizon assertions rest on the displayed proofs.

## Precise remaining obligations

This work uses the Source methods src/enterprise_math/brc_transport.py (Affine.then/inverse, EffectHistogram) and src/enterprise_math/brc_control_port.py (ControlPacket.from_edges/then, typed time ports) as **read and applied interface laws**. The original enterprise_math Python package was NOT installed or executed on this host. The source's EffectHistogram loses edge histories; the decorated free-monoid/DAG carrier above is a mathematically specified **proposed extension**, not claimed to exist in the current Source code.

The actual R193 observer, original source-token grammar and contract have not been directly verified; no R193 fidelity bridge, legal native heartbeat update, six-axis final-address realization, verified active Owner/CLAIM, formal Result or independent Driver review is claimed. Native task query returned CONTROL_QUOTA; direct native session creation received STATIC_READONLY_SCOPE_DENIED with operation_sent=false. A separate lightweight research activity was registered through managed GitHub without granting task authority.

## Next independent research step (R255)

Resolve R193's exact ordered source-path observer and its time/port contract, then establish or reject a word-preserving map from R193 source tokens to the decorated physical-edge alphabet. Derive the *smallest sufficient carrier for that actual observer*: it may require less than full words. Also execute the already prepared R253_NATIVE_INTEGRATION_PENDING.py on a genuine, pin-matched enterprise_math installation, reading its real ControlPacket.blocks through depth three. Test prefix/suffix provenance queries on the shared DAG with declared output-sensitive resource bounds. Keep formal mathematical review and P000 dynamical admissibility separate from this author-side finite result.
