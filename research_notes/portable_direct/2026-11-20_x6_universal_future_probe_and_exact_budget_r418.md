# X6 r418 — Universal diagnostic futures, effective frame kernels and exact repair budgets

Date: 2026-11-20. Status: **author-side proved finite-group theorem and cross-line synthesis**, not a Native Result, independent Driver review, or native physical X6 dynamics.

Contributor of this extension: existing RESEARCH_DRIVER EM-DVR-DEBB5E (shared mathematical context with r411–r417). This sharpens the context-separation idea in r411 and r417 rather than claiming those earlier discoveries as new. Original X6 contributors EM-EMF6D046-5A2844, EM-X6-DFD1FD and EM-X6CM-EDBD55 retain their work and attribution. Inputs include r411@5e3d07b05799754cb1b4327e97bb30aaf12f0652, r415@88e41b7b8ed36cab0551ae6345d2da7576b41d39, r416@c630a0ee31990e5187f1fc44a6798b886d2f5a7f, and r417@dd60236ba1953bce0bb9df538bbc2a2121909b04.

## Model and theorem

Let H be a finite group acting letterwise on a finite nonempty event alphabet E. Let c:E -> Sigma^ell be injective, H-equivariant and of fixed positive block length. Fix s in E* and put K = Stab_H(s). The observation of u is O_s(u) = [c(us)]_H. A *common future probe* w in E* is inserted before the fixed suffix: its readout is O_s(uw) = [c(uws)]_H. This is exactly the future interface of r417, not a claim about physical chronological appending after a completed state.

Define the effective kernel N = ker(K acting on E) = intersection over e in E of Stab_K(e), and the effective base length
    d(K,E) = min{|w|: w in E*, Stab_K(w) = N}.
Here a word stabilizer is pointwise, so the empty probe is allowed if K=N.

**Theorem (free legal-event language L=E*).**

1. A single fixed word w distinguishes every pair of distinct prefixes in the same initial orbit fiber, i.e. O_s(u)=O_s(v) and O_s(uw)=O_s(vw) implies u=v for every u,v, **if and only if** Stab_K(w)=N.
2. The sharp minimum length of one such *universal* probe is d(K,E), and
       0 <= d(K,E) <= floor(log2(|K|/|N|)).
   This is a bound on event blocks, not primitive letters or storage bits.
3. The maximum initial observer-fiber size over all finite prefixes equals |K|/|N|. Consequently r417's exact worst-case auxiliary bits for preserving *all common-future legality and orbit outputs* equal r416's literal-reconstruction bits:
       B_future(s,E*) = B_literal(s,E*) = ceil(log2(|K|/|N|)).
   The same universal w proves future-signature injectivity inside every initial orbit fiber.

**Proof.** Equality O_s(u)=O_s(v) forces v=g.u with g in K by injective fixed-block encoding and comparison of s. If Stab_K(w)=N, equality O_s(uw)=O_s(vw) would force an element t in H to map uws to vws. Comparison of their identical w and s blocks gives t in Stab_K(w)=N. As N fixes every event letter, t.u=u, hence v=u.

For necessity, if Stab_K(w) properly contains N, choose h in Stab_K(w)\N and an event e moved by h. Put u=e and v=h.e. The two distinct prefixes have equal initial orbit, and h fixes both w and s, giving equal probed readouts. Thus w fails universality.

Existence of a word with stabilizer N follows by concatenating all letters of E. Starting with K, repeatedly choose a letter whose stabilizer intersects the current subgroup properly until it becomes N; such a letter exists whenever the subgroup is larger than N. Each strict subgroup step has index at least 2, so the number of chosen letters is at most floor(log2(|K|/|N|)). Necessity and sufficiency above give the exact minimum d(K,E).

Every prefix stabilizer J(u) in K contains N, so |K.u|<=|K|/|N|. Taking u to be an effective-base word gives J(u)=N and attains that fiber size. With L=E*, all transforms and all future insertions are legal. The universal probe separates all distinct members of each fiber, so the future-equivalence partition in r417 is discrete and the optimal fixed-width tag has exactly ceil(log2(|K|/|N|)) bits. QED.

**Restricted legal languages (sufficient transfer criterion).** The same equality B_future(s,L)=B_literal(s,L) holds for an arbitrary L whenever an effective-base word w is legal as a common future after **every** legal prefix in U_s, i.e. uws belongs to L for all u with us in L. The pairwise readout argument above then applies within every lawful fiber. Without this common-extension condition, r417's exact DFA test remains the applicable criterion; the free-language conclusion must not be imported into a constrained native event law.

## Exact X6 candidate consequences

Use the candidate static group H=(C2)^6 semidirect A6 (order 23040), with fixed signed-axis suffix s=(+e1,+e2,+e3). Its stabilizer K has order 2^3 * 3 = 24.

- **Candidate ordered-triad event alphabet** E consists of the 960 ordered triples of signed native-axis labels with three different unsigned axes. K acts faithfully (N=1). The single legal candidate future w=(+e4,+e5,+e6) has trivial K-stabilizer. Thus d(K,E)=1 event and, for the freely composable candidate language E*, both repair budgets are exactly ceil(log2 24)=**5 bits**. One future triad separates all distinct static orbit-fiber histories, though the full orbit readout itself may be large.
- **Primitive signed-letter alphabet** E=Sigma={+/-e1,...,+/-e6}, with the same three-axis suffix. Here N=1, but every K-stabilizer-killing word must mention each of axes 4,5,6: omitting any leaves that unused-axis sign flip. The word (+e4,+e5,+e6) attains this, so d(K,E)=**3 primitive letters**, with the same 5-bit repair budget for free composition.

Hence the horizon needed to diagnose frame information depends on event typing even when the residual group and bit budget coincide. A triadic *candidate* event is not three sequential primitive displacement events. Both examples assume freely composable event words; r413's repeat-only and r417's restricted-language examples show why that assumption matters.

## Native transfer boundary and next source requirement

This is an exact static group/regular-language result. P000's TRIADIC_CLOSURE_E, Cell/Port incidence, branch multiplicity, time-order legal succession, physical observer and actual rotational covariance are protected independent inputs. Neither the 960 candidate triples nor E* has been shown to be the native admissible dynamics. To use the one-event diagnostic physically, obtain exact Source-pinned native event and succession definitions, then verify that w is an allowed common future and that the relevant Cell/Port/branch/time readouts obey the stated orbit interface. The actual native problem may require r417's non-invariant DFA criterion or a richer observer.

Persistence is author-side scientific source only: no formal CLAIM, Native Result, independent review, Activity association, Task closure, mother-objective closure, P000 change or scheduling change is claimed.
