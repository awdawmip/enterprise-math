# R5 — Named-Set source controller: idempotent reset normal form

Date: 2026-11-16. Frozen scientific pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551 (unchanged). Inherited frontier: Draft PR #2427, R5_SINGLE_RESET_PAIRED_LOOP_THEOREM.md at fdca33bd777759d4162a71e8f9cc920fd1b70281. Author-side independent portable derivation; NOT_REVIEWED. No formal Task, CLAIM or protected Activity write is asserted.

## Precise question

In the inherited, genuine source-labelled cycle-of-triangles auxiliary repair model, k=9, slack s=2 and the only raw commands are named Set_0(0), Set_0(1). The saved computational result is a 43-library static cover and a 44-state reset-coherent (paired-loop) optimum, leaving general dynamic minimum 43 or 44. The integer-program lower bounds are currently solver-based. If general control could improve the 44-state coherent bound, would it need to remember *repetitions of the same Set command*?

**Result: no.** Every finite valid source-labelled controller can be transformed without extra states or changes to its labelled outputs so that each named reset is internally idempotent. The remaining possible advantage is cross-command order residual, not same-command repetition.

## Theorem A — Finite reset-power normalization

Let X be raw states, A a finite alphabet of operations, and R_a:X→X a physically idempotent update for every a∈A, i.e. R_a^2=R_a. Let Q be a finite deterministic Moore controller (m=|Q|≥1), with output o:Q→Y, transitions f_a:Q→Q and a total initialization relation I⊆X×Q. The output-correctness relation Good(x,y) may require exact source identity, typed provenance and an additive resource budget.

Assume every (x,q)∈I is correct for *every finite input word*, including the empty word. Put L=lcm(1,...,m) and replace each internal transition with g_a=f_a^L, keeping Q, I and o unchanged.

Then:

1. g_a^2=g_a for all a.
2. The modified controller remains correct for every finite command word.
3. No labelled output/library changes, no extra state is introduced.

**Proof.** Every orbit of a self-map on m elements enters a cycle before m iterations, and every cycle length d≤m divides L. Since L≥m for m≥2 (m=1 is trivial), f_a^L maps each orbit to a cyclic point and another L iterations return that same point. Therefore g_a is idempotent. For a word w, expand each occurrence of a into L repetitions to form Φ(w). The new controller's state after w equals the original controller's state after Φ(w). Since R_a^L=R_a for each a, the corresponding physical raw states are identical after w and Φ(w). Correctness of the original controller on all words thus proves correctness of the new one. Every output is literally its former labelled output. QED.

This proof requires only individual physical idempotency. It does not assume the different operations commute or satisfy cross-absorption.

## Theorem B — Every retained state can be fixed by a command

Assume also that every raw x admits at least one command a with R_a(x)=x. This holds for any named Set coordinate: select a coordinate and Set it to its existing value.

After Theorem A, put Q'=⋃_{a∈A} image(g_a), restrict all transitions and the output map to Q', and initialize x at g_a(q), where (x,q)∈I and R_a(x)=x. Then the restricted controller is correct and has no more than m states; furthermore

- g_a^2=g_a on Q';
- Q'=⋃_a image(g_a)=⋃_a Fix(g_a);
- every retained state is fixed under at least one named reset;
- all output libraries and their actual provenance remain unchanged.

**Proof.** Q' is transition-closed because g_b(z)∈image(g_b)⊆Q' for every z∈Q'. The prefix a^L leaves x physically unchanged, so the original controller's correctness after that prefix and every expanded suffix proves that g_a(q) can initialize x. Idempotency gives image(g_a)=Fix(g_a). QED.

Consequently any optimal finite controller for the R5 named single-bit Set system has a witness with idempotent internal Set_0(0), Set_0(1), and every state fixed by one or both operations. **This does not imply the cross-command absorption identity** g_b(g_c(q))=g_b(q), which is the stronger hypothesis of the previous paired-loop theorem.

## Corollary C — Exact transition template enumeration

For m labelled internal states under two named resets, the normalized transition pairs are precisely the idempotent map pairs (g_0,g_1) for which image(g_0)∪image(g_1)=Q.

Partition Q as A (fixed only by g_0), B (fixed only by g_1), C (fixed by both), with a=|A|, b=|B|, c=|C|, a+b+c=m. g_0 fixes A∪C, and each element of B maps arbitrarily into A∪C. Analogously g_1 fixes B∪C, and each element of A maps into B∪C. Both images are nonempty.

Therefore the exact number of labelled transition templates is

T_m = Σ_{a+b+c=m, a+c≥1, b+c≥1} [m!/(a!b!c!)] (a+c)^b (b+c)^a.

The exact values at m=1,2,3,4 are 1, 7, 55, 597. These count *algebraic transition templates*, not source-feasible controllers or minimum states.

A three-state counterexample demonstrates that cross-order residual survives normalization. Let g_0=(0,1,1) and g_1=(2,2,2) denote output images on Q={0,1,2}. Both maps are idempotent, their image union is Q, but g_0(g_1(0))=1 differs from g_0(0)=0. This is an algebraic counterexample to automatic absorption, not a claimed 43-state k=9 witness.

## Corollary D — Exact finite 43-state decision kernel

Use the previously frozen source-centre coverage law C_k(r)={u:u≤r coordinatewise and q(r)-q(u)≤2}, where q(u)=Σ_{i modulo k}u_i u_{i+1}. For k=9 and raw R_b(2y+c)=2y+b, an unrestricted deterministic source-labelled controller with at most m states exists **if and only if** the following finite objects exist:

1. Q of cardinality at most m and idempotent maps g_0,g_1:Q→Q, with image(g_0)∪image(g_1)=Q.
2. One genuine source centre r(q) for each q∈Q.
3. A total relation S⊆{0,...,511}×Q satisfying both:
   - (u,q)∈S implies u∈C_9(r(q)).
   - (u,q)∈S implies (R_b(u),g_b(q))∈S for b=0 and b=1.

**Proof.** Necessity is obtained by Theorems A–B and taking the relation of all safe raw-state/controller-state pairs. Sufficiency follows by initializing each raw u in any q with (u,q)∈S and inducting on word length using the closure condition. QED.

This is an exact finite constraint characterization that excludes internal non-idempotent transition maps from the 43-state search. The prior 44-state construction is still an upper certificate. The prior k=9 lower bound M_static=43 and coherent minimum W_9=44 keep their actual recorded solver-dependent certification status; this theorem does not independently close the 43/44 gap.

If 43 states are feasible while W_9=44 holds, a witness can be chosen with individually idempotent resets and must violate some cross-absorption identity. Thus a possible 43-state advantage must encode order of **different** commands rather than repeat-count of an identical Set command.

## Exact local checks and evidence scope

Companion program VERIFY_R5_RESET_IDEMPOTENT_NORMAL_FORM.py (Python standard library) tests idempotent powers for every self-map of m=1..4, exhausts all idempotent map pairs for the T_m counts, and tests a 16-state k=3 two-copy toggling source-labelled controller (original resets non-idempotent, outputs exact source centres) on every word of length 0..7. The 2,040 raw-state/word cases contain 12,304 checked transitions. Also checks the three-state non-absorption example. The recorded result is PASS_R5_RESET_IDEMPOTENT_NORMAL_FORM.

Universal mathematics: AUTHOR_PROVED. Finite checks: EXACT_FINITE_CHECKED. Independent review: NOT_REVIEWED. This is a typed *auxiliary integer/source controller* result, not native X6 or BRC arithmetic; P000, ACTIVE worldview, and the frozen scientific input are unchanged.

## Next question

Apply the normalized finite relation kernel at k=9,m=43 with symmetry breaking and reproducible SAT/CP/branch search. Save either a complete 43-state source witness (all 512 raw initialization cases and full reset closure independently checked), or an auditable no-go certificate. Do not infer an impossibility merely from a failed/timeout search.
