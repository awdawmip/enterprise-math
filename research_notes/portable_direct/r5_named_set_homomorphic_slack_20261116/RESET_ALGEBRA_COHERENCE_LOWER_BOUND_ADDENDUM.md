# R5 addendum — Reset-algebra-coherent controllers obey the exact projection lower bound

Date: 2026-11-16 (Asia/Shanghai). Frozen input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

This addendum strengthens NAMED_SET_CONGRUENCE_QUOTIENT_AND_HYPEREDGE_SLACK_THEOREM.md in the same folder. Its latter homomorphic-quotient hypothesis may appear restrictive when the inherited controller model permits overlapping belief states. The present theorem eliminates the need to assume a global abstraction map at the outset: the map can be constructed from the internal Set algebra.

## Theorem: internal reset identities force the homomorphic lower bound

Let X={0,1}^n. A deterministic controller has finite nonempty internal state set Q, total transitions δ_i^b:Q→Q for each named overwrite Set_i(b), and for each q∈Q a nonempty raw belief B(q)⊆X. Assume:
1. Raw coverage: every raw u occurs in at least one allowed initial state.
2. Transition soundness: Set_i(b)(B(q))⊆B(δ_i^b(q)) for every q,i,b.
3. Source-labelled output in q serves every raw u∈B(q) at additive penalty at most s over its individual optimum, under the positive hyperedge source-cost model stated in the companion theorem.
4. On the reachable controller states, the transition operators obey the **concrete reset identities**
   
       δ_i^b ∘ δ_i^c = δ_i^b             for every i,b,c,
       δ_i^b ∘ δ_j^c = δ_j^c ∘ δ_i^b   for i≠j.          (R)

Then for nonnegative rational hyperedge costs h, every such controller has at least

    2^(n−d_h(s)),  where d_h(s)=max{|F|:c_h(F)≤s},          (A)

internal states. This lower bound is attained by the projection controller from the companion theorem. For the R5 unit cycle (k≥3, s=2) **every reset-algebra-coherent controller has at least 2^(k−1) states**, even if its beliefs overlap and its initial-state selection is not a function of the raw mask.

**Proof.** Choose any initial controller state q₀ with nonempty B(q₀). For each raw mask u define f(u) by applying, in a fixed order, one internal reset δ_i^{u_i} for every i to q₀. The reset identities make the order immaterial and give

    f(Set_i(b)u)=δ_i^b(f(u)).                                  (B)

Every concrete raw mask x∈B(q₀), after that same complete reset word, becomes u. Iterating transition soundness therefore gives u∈B(f(u)). Thus f:X→f(X)⊆Q is an explicit surjective homomorphic abstraction of the full concrete reset algebra. The kernel of f is reset-invariant, hence by companion Theorem A there exists a fixed forgotten coordinate set F and f has exactly 2^(n−|F|) distinct values. For each q∈f(X), the entire fiber f⁻¹(q) lies in B(q). Source costs for B(q) must therefore also meet the budget on that fiber; companion Theorem B gives c_h(F)≤s. Hence |F|≤d_h(s), yielding (A). The projected controller realizes equality. QED.

The proof requires the reset identities only on a forward-invariant state subset containing an allowed start state, since all f(u) then lie in that subset. Consequently any proposed controller with fewer states than (A) must fail at least one identity (R) on the reachable transitions of **every** available start-state subautomaton. That failure is a precise *path-order or repeated-update internal residual* to preserve and study; it is not a claim about native spatial coordinates.

## Identity hypothesis is substantive

Take any exact-state controller storing the raw mask u plus an auxiliary parity label t. Every Set command updates raw u correctly but flips t. Its belief remains the singleton {u}; its source output remains exactly optimal. Repeating the same concrete overwrite leaves raw u unchanged but flips the label twice, so the internal identity δ_i^b∘δ_i^b=δ_i^b fails. Thus transition soundness and source safety alone do not impose (R).

## Evidence, model boundary and next question

The companion executable VERIFY_R5_RESET_ALGEBRA_RIGIDITY.js checks all coordinate-projection quotients for k=3..8, verifies the internal absorption and commutation laws on each raw state, checks source slack, and checks the parity-labelled counterexample. The attached JSON records the exact finite count. The universal proof is the algebraic argument above; its contribution is the extension from predeclared homomorphic maps to all reset-algebra-coherent controllers.

The remaining unrestricted problem is now more focused: can a finite transition-closed, future-safe radius-one-star belief controller violate the internal reset algebra and actually use fewer than 2^(k−1) states? A finite compression witness must expose its concrete noncommuting or nonabsorbing transitions and preserve named-source fidelity; alternatively prove such transition residuals never improve the state count.

Scientific source: the unchanged R5 input pin, the preceding saved source-labelled common library L(r), and the companion theorem. This is portable author-side research rather than a formal Task claim, Result, review or native P000 promotion.
