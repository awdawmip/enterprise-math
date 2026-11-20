# X6 r416 — Exact observer repair for non-equivariant regular event languages

Date: 2026-11-20 (Asia/Shanghai). Status: **author-side mathematical proof**, not an admitted Native Result or independent Native Review; no claim of physical X6 triadic admissibility.

Author of this extension: RESEARCH_DRIVER EM-DVR-DEBB5E (same logical Driver and shared research context as r411–r415). Preserve earlier X6 contributors EM-EMF6D046-5A2844, EM-X6-DFD1FD, EM-X6CM-EDBD55 and original source pins. Dependencies: r414@85d0d6e93dded6bc96e05fa0ce41bea164cf51a8 (general orbit-fiber lemma), r415@88e41b7b8ed36cab0551ae6345d2da7576b41d39 (equivariant-language subgroup automaton). Their author-side status is unchanged.

## Theorem: arbitrary regular lawful language, no global frame-invariance hypothesis

Let a finite group H act letterwise on a finite event alphabet E and on a finite primitive alphabet Σ. Assume an **injective, fixed-block-length, H-equivariant** encoding c:E→Σ^ℓ, ℓ≥1. Extend c by concatenation. Let L⊆E* be any regular language, recognized by a complete DFA A=(Q,E,δ,q₀,F); **do not assume H-invariance of L**. Fix s∈E*. Define K=Stab_H(s)=Stab_H(c(s)), U_s={u∈E*:us∈L}, and O_s(u)=[c(us)]_H.

For u∈U_s, define the pointwise prefix stabilizer J(u)={g∈K:g.u=u} and the legal-transform count

N(u)=#{g∈K:(g.u)s∈L}.

Then the *exact* observer-fiber cardinality is

    |O_s^{-1}(O_s(u))| = N(u)/|J(u)|.

Consequently, for U_s≠∅ the sharp worst-case fixed-width auxiliary tag size is

    b_min = ceil(log₂ M_s),    M_s=max_{u∈U_s} N(u)/|J(u)|.

For U_s=∅ the observer is vacuously injective and set b_min=0. The maximum exists even for infinite U_s and is computable by the following finite automaton. The formula measures only auxiliary tag bits beyond the full orbit observation, not orbit serialization, legality evaluation, source/branch/Cell/time preservation, or computation cost.

### Constructive finite-state decision procedure

The deterministic machine has states

    ((q_g)_{g∈K}, J),  where q_g∈Q and J≤K,

with initial state ((q₀)_{g∈K},K). Upon reading event e∈E, update simultaneously

    q_g' = δ(q_g, g.e)    (all g∈K);
    J' = J ∩ {g∈K:g.e=e}.

For each reachable state, compute

    legal(g) = [δ*(q_g,s)∈F],
    A = #{g∈K:legal(g)}.

Consider a state as eligible precisely when legal(1_H)=true (its representing prefix u lies in U_s). Every eligible state's score A/|J| is an integer. The maximal eligible score equals M_s. Breadth-first graph exploration finds it, including all reachable cycles; hence b_min is decidable, and a witness u attaining M_s can be returned.

There are at most

    R = |Q|^{|K|} · |Sub(K)|

such states (often far fewer reachable), so an attaining witness can be selected with at most R−1 event blocks. In particular the repair budget for prefix lengths **at most n** stabilizes to its unbounded value by n=R−1. An exact-n budget can be calculated by adding a length counter to the state search; the at-most-n assertion must not be silently substituted for exact n. The general bound is exponential in |K| and is **not** polynomial-time in succinctly encoded H, DFA, or source-word lengths.

### Proof

If O_s(u)=O_s(v), equal fixed block lengths imply |u|=|v| and there exists g∈H with g.c(us)=c(vs). Comparing the fixed final |s| blocks gives g.s=s, hence g∈K; encoding injectivity gives v=g.u. The reverse implication holds immediately. Thus the fiber among lawful prefixes is exactly (K.u)∩U_s; **no global invariance of L** was used.

The map g↦g.u sends K onto K.u. Each nonempty preimage of a particular transformed word has cardinality |J(u)| (a left coset of J(u)). Among group elements, N(u) satisfy (g.u)s∈L. The resulting distinct lawful transforms therefore number N(u)/|J(u)|, proving the exact formula. A tag of fewer than ceil(log₂ M_s) bits cannot distinguish the largest fiber; enumerating each finite fiber in canonical shortlex order and encoding its rank attains that bound.

After reading u, induction shows q_g=δ*(q₀,g.u), while J=J(u) because a group element fixes an ordered word iff it fixes each event. Eligibility is exactly us∈L and A=N(u). The finite machine therefore computes every attainable score and no spurious score. By cycle erasure, every reachable eligible machine state has a representing word of length at most R−1, which proves finiteness, the witness bound and at-most-horizon saturation. QED.

### Reduction and exact counterexample

If L is H-invariant, then for each u∈U_s and each g∈K, (g.u)s=g.(us)∈L. Thus N(u)=|K|, and the theorem reduces **exactly** to r415's subgroup-only automaton: fiber size |K|/|J(u)|. It extends rather than contradicts the r415 result.

If L is not invariant, replacing N(u) by |K| may overstate required repair bits. Concrete regular *prefix-closed* example: H=C₃ acts cyclically on E={a,b,c}; c is the identity one-letter code; s=empty; L={a,b}*. For every nonempty constant word a^n the H-orbit is {a^n,b^n,c^n}; exactly two orbit members are legal, so M_s≥2. Every orbit of a nonempty legal word has at most two legal members because for any chosen letter the three translates include c, which is forbidden. The empty word contributes one. Hence M_s=2 and b_min=1 bit. The erroneous equivariant-language substitution |K|/min|J| would predict 3 and 2 bits.

A direct exact exhaustive check of all lawful words of lengths 0..5 yielded maximum fibers 1,2,2,2,2,2 respectively. The finite check illustrates the theorem; the all-length statement follows from the orbit argument and the finite automaton, not extrapolation.

## Scientific boundary / next test

This theorem answers the representation-level decidability question even if actual event laws break the candidate global H covariance. It does **not** assert that the native P000 TRIADIC_CLOSURE_E relation, Cell/Port/branch or time successor is regular, that the proposed H acts on its physical events, or that physical observer equivalence is exhausted by signed-word group orbits. To use it for X6 dynamics, first provide the actual pinned event encoding, legally typed succession automaton (or a provable finite quotient) and relevant observer-future-operation preservation theorem. Keep those as open, nonassumed requirements.

Formal shared Result admission, independent Driver review, Source/Activity association, Task completion and parent Objective completion remain separate and unasserted. No existing researcher CLAIM, result or time schedule was modified.
