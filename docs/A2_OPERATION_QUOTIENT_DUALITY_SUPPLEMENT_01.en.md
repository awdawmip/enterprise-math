# A2 — Operation–Quotient Duality, Supplement 01: Mixed-Context Refinement

Status: `PROVED_WIP / EXECUTABLE_WITNESSED / NOT CANONICAL_MAIN`  
Parent: `docs/A2_OPERATION_QUOTIENT_DUALITY.en.md`  
Scope: language growth, admissible congruences, mixed future contexts, and the fixed-block gcd witness

## 1. The abstract incidence relation

For a total operation family `A` on `X`, define its admissible quotient family

\[
\operatorname{Adm}(\mathcal A)
=
\operatorname{Con}(X,\mathcal A),
\]

the equivalence relations preserved by every operation in `A`.

For a quotient kernel `theta`, let `Pol(theta)` denote all finitary operations preserving `theta`.

Then the basic incidence relation is

\[
\boxed{
\mathcal A\subseteq\operatorname{Pol}(\theta)
\iff
\theta\in\operatorname{Adm}(\mathcal A).
}
\]

This is the classical operation–relation `Pol/Inv` viewpoint restricted to equivalence relations/congruences. Enterprise Math uses it as the bookkeeping skeleton for causal quotients; the Galois machinery itself is prior art.

## 2. A2-OQD-S1-T01 — adding required operations deletes admissible quotients

For any total operation families `A,B`,

\[
\boxed{
\operatorname{Adm}(\mathcal A\cup\mathcal B)
=
\operatorname{Adm}(\mathcal A)
\cap
\operatorname{Adm}(\mathcal B).
}
\]

A quotient is compatible with the union exactly when it is compatible with both families separately.

Therefore

\[
\mathcal A\subseteq\mathcal B
\Longrightarrow
\operatorname{Adm}(\mathcal B)
\subseteq
\operatorname{Adm}(\mathcal A).
\]

This is the non-scalar generalization of the Stage-3 fixed-block law

\[
\mathcal D(U\cup W)=\mathcal D(U)\cap\mathcal D(W).
\]

The fixed-block divisor sets are one parameterized slice of the general admissible-congruence family.

## 3. A2-OQD-S1-T02 — future-language growth monotonically refines the selected quotient

Fix an observation `O`. Let

\[
\Theta_{\mathcal A,O}
=
\max\{\rho\in\operatorname{Adm}(\mathcal A):\rho\subseteq\ker O\}
\]

be the observation-selected natural quotient kernel from the parent note.

If

\[
\mathcal A\subseteq\mathcal B,
\]

then every `B`-compatible relation is also `A`-compatible, hence

\[
\boxed{
\Theta_{\mathcal B,O}
\subseteq
\Theta_{\mathcal A,O}.
}
\]

So richer future capability monotonically preserves more present detail.

This does **not** contradict the Stage-3 negative result that two arbitrary quotient refinements need not have comparable safe-operation sets. The monotonicity lives on the **future-language axis with observation fixed**, not on the arbitrary partition-refinement axis.

This distinction resolves an important apparent tension:

- `partition finer => more/fewer safe operations` has no general monotone law;
- `required language larger => selected future-safe quotient finer` does have a monotone law.

## 4. A2-OQD-S1-T03 — mixed contexts can force strictly more refinement than separate minimizations

One might guess

\[
\Theta_{\mathcal A\cup\mathcal B,O}
=
\Theta_{\mathcal A,O}
\cap
\Theta_{\mathcal B,O}.
\]

That is false in general.

The correct universal relation is only

\[
\boxed{
\Theta_{\mathcal A\cup\mathcal B,O}
\subseteq
\Theta_{\mathcal A,O}
\cap
\Theta_{\mathcal B,O},
}
\]

and the inclusion can be strict.

The reason is causal: the union language permits **mixed contexts/compositions** alternating operations from both families. A relation obtained by intersecting two separately minimized quotients need not be compatible with either family after that intersection changes the classes.

Therefore the natural quotient must be computed from the **closed combined language**, not by minimizing each capability independently and intersecting the outputs afterward.

## 5. A2-OQD-S1-W01 — exact fixed-block witness: `+2` and `+3` create a new distinction together

Take

\[
O=q_6,
\qquad
q_6(n)=\left\lfloor\frac n6\right\rfloor.
\]

Let

\[
\mathcal A=\langle+2\rangle,
\qquad
\mathcal B=\langle+3\rangle.
\]

The Stage-3 gcd refinement gives

\[
\Theta_{\mathcal A,q_6}=\ker q_2,
\qquad
\Theta_{\mathcal B,q_6}=\ker q_3.
\]

The states `0` and `1` remain equivalent in both relations:

\[
q_2(0)=q_2(1),
\qquad
q_3(0)=q_3(1).
\]

Hence

\[
(0,1)\in
\ker q_2\cap\ker q_3.
\]

But the combined language contains the mixed future word

\[
+2\ ;\ +3,
\]

which is the actual translation `+5`. Then

\[
q_6(0+5)=0,
\qquad
q_6(1+5)=1.
\]

So `0` and `1` are future-distinguishable only after both capabilities are available.

Since

\[
\gcd(6,2,3)=1,
\]

Stage 3 gives

\[
\boxed{
\Theta_{\mathcal A\cup\mathcal B,q_6}
=\ker q_1
=\Delta_{\mathbb N_0}.
}
\]

Therefore

\[
\boxed{
\Theta_{\mathcal A\cup\mathcal B,q_6}
\subsetneq
\Theta_{\mathcal A,q_6}
\cap
\Theta_{\mathcal B,q_6}.
}
\]

This is an exact causal witness for **mixed-context refinement synergy**.

## 6. Why the admissible-family intersection law and the selected-kernel failure are compatible

There is no contradiction between T01 and T03.

T01 says the **set of quotients** compatible with the union is exactly the intersection of the two admissible sets:

\[
\operatorname{Adm}(\mathcal A\cup\mathcal B)
=
\operatorname{Adm}(\mathcal A)\cap\operatorname{Adm}(\mathcal B).
\]

T03 concerns the **largest selected element below a fixed observation**.

The relation

\[
\Theta_{\mathcal A,O}\cap\Theta_{\mathcal B,O}
\]

need not itself belong to either admissible family. Intersecting equivalence relations can destroy operation compatibility because the output classes become finer while the operation images stay unchanged.

In the `q_6` witness, `ker q_2 cap ker q_3` still identifies `0` and `1`, but it is not stable under the combined translation language. The mixed `+5` context exposes the missing distinction.

Thus “intersect the valid-scale sets” and “intersect the separately selected quotient kernels” are different operations.

## 7. A2-OQD-S1-C01 — composition closure is causally substantive

The result gives a precise reason P023 closes the future language under operation words.

A state representation is not safe merely because every generator looks harmless when audited in isolation. The generated algebra/monoid can contain contexts that are absent from every one-generator sublanguage.

Therefore the real object is

\[
\boxed{
\langle\mathcal A\rangle_{\mathrm{context/composition}},
}
\]

not the unordered list of primitive operations.

This also sharpens the meaning of the user-facing Stage-3 rule “new future capability deletes unsafe scales”: new generators may create **new mixed words**, so the information cost of the union can be strictly greater than the naïve meet of the individually repaired state representations.

## 8. P008 language hierarchy revisited

The current hierarchy can now be read as a sequence of restrictions on admissible quotient geometry:

\[
\{\min,\max\}
\Rightarrow
\text{convex interval congruences},
\]

\[
\{\min,\max,+t\}
\Rightarrow
\text{periodically transported interval geometry}
\]

under the Stage-3 fixed-translation hypotheses,

and

\[
\{\min,\max,+\}
\Rightarrow
\Delta
\]

because binary addition contributes all elementary translations, including `+1`.

When several restricted translations are introduced, their **generated** additive monoid—not the generators viewed separately—is what determines the future-safe refinement. The gcd formula is exactly the closed form of that generated-language effect in the fixed-block regime.

## 9. Prior-art boundary

The `Pol/Inv` operation–relation Galois viewpoint, congruence lattices, semigroup/action closure, and context minimization are classical mathematics.

The Enterprise Math content under pressure test is the causal specialization:

- distinguishing admissible-quotient-set intersection from selected-kernel intersection;
- the explicit P008/fixed-block `(+2,+3)` mixed-context witness;
- the interpretation that capability composition can force detail not required by any isolated capability;
- the placement of the Stage-3 gcd law inside that general operation-language closure.

No generic clone/Galois/automata novelty is claimed.
