# R173 — Exact one-sided context quotients and sharp cost of future-operation scope

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.
Frozen science: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Dependencies: R171 context identity and R172 all-modulus image theorem, both in this portable research branch.
Population: all finite words in signed unit X6 directions (or d>=1 axes for the abstract theorem).
Observation: J(P)=sum of relative signed-coordinate prefix displacements. Modulus q>=2, with b=D(P) mod q, c=J(P) mod q and a=|P| mod q. This does not identify the complete native path, BRC amplitude, or event-time history.

## R173A. Exact directional-context equivalences

Define right-only (future suffix) observational equivalence by

    P ~R Q iff J(PY)=J(QY) mod q for every signed-path suffix Y.

Define left-only equivalence by

    P ~L Q iff J(XP)=J(XQ) mod q for every signed-path prefix X.

Then, for all P,Q and all q>=2,

    P ~R Q  iff  (D(P), J(P))=(D(Q), J(Q)) mod q;
    P ~L Q  iff  (|P|, J(P))=(|Q|, J(Q)) mod q.       (1)

**Proof.** R171's exact cocycle gives

    J(PY)-J(QY) = J(P)-J(Q)+|Y|(D(P)-D(Q)),
    J(XP)-J(XQ) = J(P)-J(Q)+(|P|-|Q|)D(X),

all modulo q. Empty contexts first force equal J. A single appended +E_1 (right test) forces D equality, while a single prepended +E_1 (left test) forces length equality. Conversely those equalities make every allowed context readout equal. Thus the empty and one-letter context probes are already a complete finite separating basis, and (1) is exact for arbitrary future context length. QED.

This is a distinction between **allowed operation families**, not an approximate finite-horizon result. Under two-sided concatenation, even a length-one context already attains R171's full K_q quotient, so a smaller state count requires a narrower permitted operation or observation scope.

## R173B. Sharp minimal numbers of contextual states

Let R_{q,d}, L_{q,d}, T_{q,d} be the minimal right-only, left-only and two-sided context quotients for J mod q on all signed primitive direction words in d>=1 axes.

For every q>=2:

    |R_{q,d}| = q^(2d),                               (2)
    |L_{q,d}| = q^(d+1) / (2 if 4 divides q else 1),  (3)
    |T_{q,d}| = q^(2d+1) / gcd(q,4).                  (4)

Here (4) is R172's theorem; (2) and (3) are new.

**Proof.** By R173A, the right quotient is the realized projection (b,c) of the full R172 image M_{q,d}. Every pair (b,c) is realized:

- For odd q, R172 allows every a.
- For q≡2 mod4, choose any a with a≡sum b_i mod2.
- For 4|q, choose a of parity sum b_i. Among the two residues 0,2 mod4 when a is even, or 1,3 mod4 when a is odd, the triangular parity a(a+1)/2 assumes both values 0 and 1. Choose it equal to sum c_i mod2, then use R172's exact sufficiency.

Thus every q^(2d) pair (b,c) appears, proving (2).

Similarly the left quotient is the realized projection (a,c). When 4 does not divide q, choose a b whose sum parity agrees with a for even q, or any b for odd q; R172 allows every (a,c). Hence |L|=q^(d+1). When 4|q, R172 requires sum c_i≡a(a+1)/2 mod2, which excludes exactly half of the q^d choices of c for each a. For every compatible (a,c), choose any b with sum b_i≡a mod2; R172 guarantees realization. Hence |L|=q^(d+1)/2. R171 and R172 prove (4). Finally the quotient maps (b,c), (a,c), and (a,b,c) are sufficient by (1) and R171 and necessary by their separating context witnesses, so each number is minimal. QED.

## R173C. Quantified price of admitting left contexts

The two-sided quotient has exactly

    |T_{q,d}|/|R_{q,d}|=q/gcd(q,4)                  (5)

times as many states as the right-only future-suffix quotient. For the six-dimensional native-axis instance:

| q | right-only | two-sided | extra factor |
|---|------------|-----------|--------------|
| 2 | 4,096 | 4,096 | 1 |
| 3 | 531,441 | 1,594,323 | 3 |
| 4 | 16,777,216 | 16,777,216 | 1 |
| 6 | 2,176,782,336 | 6,530,347,008 | 3 |

For q=2, length parity is reconstructible from D parity. For q=4, the two R172 parity constraints reconstruct length modulo 4 from (D,J). For other moduli, adding left contexts genuinely distinguishes more states. These are exact minimal-state differences in the declared observer, not speculative performance claims for an implementation.

## Exact verification

Executable: research_notes/portable_direct/R173_context_scope_check.py.
Result data: research_notes/portable_direct/R173_context_scope_verification.json.

The verifier constructs reachable modular signed-step image sets, takes full right/left projections, and checks each count against (2)–(4) in nine cases, including q=2,d=6. It separately checks 7,225 ordered word pairs (lengths 0..3 over a two-axis signed alphabet) with empty and one-letter contexts at q=4,d=2. All exact integer checks passed. Marker R173_DIRECTIONAL_CONTEXT_QUOTIENT_EXACT_PASS. Proof applies to all q,d; independent review and formal checker have not run.

## Next scientific question

Choose a concrete native BRC signed-port observer with explicit branch weights, signed cancellation and allowed operation family. Test whether its right-only evolution factors through a finite signed-path cocycle, or provide a branch/provenance counterexample and the minimal additional repair coordinate. The quotient formulas here identify the mathematical cost of enlarging from future right updates to bidirectional contexts; they do not equate this J readout to full BRC port dynamics.

No claim, review or Foundation admission is implied by this portable research submission.