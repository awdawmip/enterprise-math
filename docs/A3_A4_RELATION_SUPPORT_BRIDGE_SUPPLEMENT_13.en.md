# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 13

Status: `ACTIVE RESEARCH NOTE`  
Scope: compositional projection from count semantics to existence semantics and Pareto budget semantics

## 1. Why this stage matters

The bridge has developed several state layers:

- exact witness identities;
- non-negative-integer count matrices/tensors;
- boolean support relations;
- Pareto budget frontiers;
- selected truth bits.

This note checks that the middle projections are not merely lossy summaries. For the declared future languages they are **compositional shadows**: project first or compose first gives the same answer.

The non-negative coefficient assumption is essential.

## 2. B53 — positive-support map is a semiring homomorphism

Define

\[
\sigma:\mathbb N\to\mathbb B
\]

by

\[
\sigma(n)=1[n>0].
\]

Then

\[
\boxed{
\sigma(a+b)=\sigma(a)\lor\sigma(b),
\qquad
\sigma(ab)=\sigma(a)\land\sigma(b).
}
\]

Also `sigma(0)=false` and `sigma(1)=true`.

Thus positive support is a homomorphism from the natural-number semiring to the Boolean semiring.

This is standard algebra; its importance here is that there is no coefficient cancellation in `N`.

## 3. B54 — count composition projects exactly to relation composition

Let `A,B` be non-negative-integer matrices and let `supp(A)` be their entrywise positive-support relations.

Then

\[
\boxed{
\operatorname{supp}(AB)
=
\operatorname{supp}(A)\circ\operatorname{supp}(B).
}
\]

Indeed,

\[
(AB)_{xz}>0
\iff
\sum_y A_{xy}B_{yz}>0
\iff
\exists y:A_{xy}>0\land B_{yz}>0.
\]

By induction, for every finite count-operation word,

\[
\boxed{
\operatorname{supp}(M_1\cdots M_k)
=
\operatorname{supp}(M_1)\circ\cdots\circ\operatorname{supp}(M_k).
}
\]

Therefore boolean A4 existence is an exact compositional shadow of the richer non-negative-integer witness-count algebra.

## 4. B55 — graded count support projects exactly to achievable cost sets

For a fixed stage depth, let the exact count tensor be

\[
H(\mathbf a)\in\mathbb N,
\]

where `a` is a stage-cost vector.

Define its positive coefficient support

\[
S(H)=\{\mathbf a:H(\mathbf a)>0\}.
\]

Under coefficient convolution, positive support obeys

\[
\boxed{
S(H^{(p)}\ast H^{(q)})
=
\bigcup_y
\{u\Vert v:u\in S(H^{(p)}_{xy}),\ v\in S(H^{(q)}_{yz})\}.
}
\]

because all convolution coefficients are sums of non-negative products. A coefficient is positive exactly when at least one represented prefix/suffix pair contributes.

So the path-cost support layer is also a compositional shadow of the count layer.

## 5. B56 — Pareto projection commutes with future composition

For a finite cost set `S subset N^k`, define

\[
\pi(S)=\operatorname{ParetoMin}(S).
\]

Stage 08 proved that if `u<=v`, then `u||w<=v||w` for every suffix `w`. Hence dominated costs never become nondominated after future concatenation.

Therefore

\[
\boxed{
\pi(S\star T)
=
\pi(\pi(S)\star\pi(T)),
}
\]

where `star` is path-cost concatenation through intermediate states followed by union.

At the matrix level this is exactly the antichain convolution theorem:

\[
\boxed{
F^{(p+q)}
=F^{(p)}\star F^{(q)}.
}
\]

Thus existence-budget state can be compressed online without first reconstructing the richer count tensor.

## 6. Commuting semantic-shadow diagram

For the generated staged-support language we now have a compositional chain

\[
\boxed{
\text{labeled paths}
\to
H^{(k)}\in\mathbb N^{(\mathbb N^k)}
\to
S^{(k)}
\to
F^{(k)}
\to
\text{budget truth}.
}
\]

The relevant operations commute with the projections:

- labeled-path concatenation → coefficient convolution;
- coefficient convolution → positive-support concatenation;
- positive-support concatenation → Pareto antichain convolution;
- antichain state → exact budget truth by dominance.

Each lower layer is therefore a mathematically closed machine for its own weaker observable language.

## 7. B57 — equitable count quotient automatically yields an existence quotient

Suppose a witness partition is equitable for a non-negative-integer count matrix `M`, with quotient matrix `Q_M`.

For every source coarse cell `a` and target coarse cell `b`:

\[
Q_M(a,b)>0
\]

iff every fine source state in `C_a` has at least one positive-weight transition into `C_b`.

Thus booleanizing the quotient count matrix gives the exact coarse block-existence relation.

For an equitable operation family,

\[
\operatorname{supp}(Q_{M_1}\cdots Q_{M_k})
\]

is therefore the exact block-existence relation after the operation word.

So once count-lumpability is proved, existence closure comes for free as a further homomorphic shadow.

## 8. Strict irreversibility of the shadow maps

The arrows generally cannot be inverted:

- boolean support does not recover positive count magnitudes;
- Pareto frontier does not recover dominated achievable costs;
- a truth bit does not recover the frontier;
- block quotient does not recover erased witness identities.

The explicit counterexamples from earlier stages witness these losses.

This is not a defect when the declared future language ignores the missing information. It is exactly the intended legal-collapse behavior.

## 9. B58 — non-negative coefficients are part of the contract

The positive-support homomorphism depends on absence of cancellation.

Over signed integer weights one can have nonzero contributing paths whose algebraic sum is zero. Then

\[
\operatorname{supp}(AB)
\]

need not equal boolean composition of entrywise nonzero supports.

Therefore the count→existence shadow theorem applies to **non-negative witness multiplicities/counts**, not arbitrary signed relation amplitudes.

This boundary is important because A3's weighted relation field `Z` is signed. One must not booleanize signed `Z`-algebra by analogy with count incidence.

## 10. Architecture consequence

The bridge now exposes two fundamentally different algebraic roles:

1. **signed A3 relation coordinates**: preserve cancellation/orientation information and require their own quotient rules;
2. **non-negative witness/count coefficients**: admit exact positive-support and Pareto semantic shadows.

This is another reason A3 and A4 should not be merged merely because both use relation-like matrices.

## 11. Prior-art discipline

Semiring homomorphisms, Booleanization of non-negative path algebras, weighted automata, provenance semirings and Pareto/idempotent path algebras are established prior art.

The current project value is the explicit commuting state-reduction chain inside the already-developed A3→A4→P023 bridge, plus the signed/non-negative boundary that prevents an invalid cross-algebra analogy.

## 12. Executable audit

The bridge test layer compares, on finite examples:

- positive support of natural-number matrix products versus Boolean relation composition;
- positive support of coefficient convolution versus achievable cost concatenation;
- Pareto projection after full composition versus antichain convolution of already-pruned states;
- equitable quotient count words versus their booleanized block-support shadows.
