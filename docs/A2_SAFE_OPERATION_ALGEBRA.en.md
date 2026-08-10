# A2 — Safe-Operation Algebra and Complete-Growth Operation Spectrum

Status: `PROVED_WIP / EXECUTABLE_CHECKED / NOT CANONICAL_MAIN`  
Owner: A2 future-compatible quotient mother layer  
Consumes: canonical `EnterpriseMath/Quotient/OperationCongruence.lean`, P023 operation-family closure, P024 action-language precision, and stage-3 P008 complete-growth basin results frozen at `checkpoint/causal-absorption-20260809-stage3@d6944dad829c95c8e38022ab091c2d5c91087dfa`.

## 1. Why “precision” is no longer the primitive

Let

\[
q:X\to Q,
\qquad
\theta=\ker q.
\]

Canonical A2 already says that a `k`-ary operation `mu:X^k->X` survives the collapse exactly when coordinatewise `theta`-equivalence implies `theta`-equivalence of outputs. Equivalently, `mu` descends uniquely to an operation on `Q`.

The stage-3 P008 work suggests that the useful object is therefore not a scalar precision parameter but

\[
\boxed{
(\text{causal quotient }\theta,
\text{surviving operation algebra}).
}
\]

This note makes that statement exact and separates the classical absolute algebra from the project-specific natural-operation spectrum.

## 2. A2-SOA-T01 — absolute unary safe monoid

For a quotient `q:X->Q`, define

\[
\operatorname{Safe}_1(q)
=
\{f:X\to X:q(x)=q(y)\Rightarrow q(f(x))=q(f(y))\}.
\]

Then `Safe_1(q)` contains the identity and is closed under composition.

More strongly, every safe `f` is uniquely equivalent to the data

\[
\boxed{
\bar f:Q\to Q,
\qquad
f_a:q^{-1}(a)\to q^{-1}(\bar f(a))
\quad(a\in Q).
}
\]

Conversely, any such coarse map plus fiber maps defines a safe endomap.

This is exactly the classical transformation semigroup preserving/stabilizing the partition into `q`-fibers, commonly written `T(X,P)`. Enterprise Math does not claim that generic semigroup as new.

## 3. A2-SOA-T02 — all finitary safe operations form the equivalence polymorphism clone

For each arity `r>=1`, let `Safe_r(q)` be the operations

\[
\mu:X^r\to X
\]

such that

\[
x_i\mathrel\theta y_i\ \forall i
\Longrightarrow
\mu(x_1,\ldots,x_r)\mathrel\theta\mu(y_1,\ldots,y_r).
\]

The arity-sorted family

\[
\boxed{
\operatorname{Safe}(q)=\bigcup_{r\ge1}\operatorname{Safe}_r(q)
}
\]

contains every projection and is closed under superposition. It is precisely the classical polymorphism clone `Pol(theta)` of the equivalence relation `theta`.

Thus the **absolute** complete safe-operation algebra is already mature universal algebra. The Enterprise Math frontier is not to rename this clone; it is to intersect it with the operations that the causal model actually declares natural.

## 4. A2-SOA-T03 — exact fiber decomposition and finite census

Suppose `X` is finite and the quotient fibers have sizes

\[
m_a=|q^{-1}(a)|,
\qquad a\in Q.
\]

For a fixed coarse input tuple

\[
\mathbf a=(a_1,\ldots,a_r)\in Q^r,
\]

there are

\[
D_{\mathbf a}=\prod_i m_{a_i}
\]

fine input tuples over that coarse tuple. A safe fine operation first chooses one output coarse class `b`, then sends each of those `D_a` fine inputs arbitrarily into the fiber over `b`.

Hence

\[
\boxed{
|\operatorname{Safe}_r(q)|
=
\prod_{\mathbf a\in Q^r}
\left(
\sum_{b\in Q}m_b^{D_{\mathbf a}}
\right).
}
\]

For `k=|Q|` equal fibers of size `m`,

\[
\boxed{
|\operatorname{Safe}_r(q)|
=
k^{k^r}m^{k^r m^r}.
}
\]

The executable reference independently matches exhaustive enumeration for unary and binary operations on small nonuniform partitions.

This census is elementary/classical partition-preserving algebra; it is included to make the size of the absolute algebra explicit, not as a priority claim.

## 5. A2-SOA-D01 — natural operation spectrum

Let `A` be a declared ambient family of fine operations: arithmetic operations, causal updates, physically allowed transitions, or another typed operation algebra.

Define the **natural safe-operation spectrum**

\[
\boxed{
\operatorname{Spec}_{\mathcal A}(q)
=
\mathcal A\cap\operatorname{Pol}(\ker q).
}
\]

For every surviving operation, canonical A2 descent gives a unique induced coarse operation. Therefore the coarse causal state should be regarded as a quotient **together with its induced surviving algebra**, not as a quotient plus an externally assigned scalar precision.

This definition also explains why finer partitions need not have monotonically larger safe-operation sets. Equality and the universal relation are both preserved by every operation, while intermediate equivalences can impose genuine restrictions. Refinement order and safe-operation inclusion are therefore not the same order.

## 6. A2-SOA-T04 — safe translations do not identify the complete-growth quotient

Translation spectra can recover a natural period capacity without recovering the basin word.

Consider two P008 growth laws on `N_0`:

\[
V_1(k)=3k,
\]

with constant basin width `3`, and

\[
V_2(2m)=3m,
\qquad
V_2(2m+1)=3m+1,
\]

whose primitive width word is

\[
(1,2,1,2,\ldots).
\]

For both quotients the complete global safe-translation monoid is

\[
\boxed{3\mathbb N_0.}
\]

The quotients are different: one has one basin of width `3` per period, the other has two basins of widths `1,2`. Therefore

\[
\boxed{
\text{translation-safe monoid}\not\Rightarrow\text{unique quotient geometry}.
}
\]

The primitive positive generator `3` is a natural **period capacity**, but not a complete description of the causal partition.

This sharpens the stage-3 gcd result: in the uniform-block candidate family, `gcd(U)` is the largest exact block scale forced by the supplied translations; outside that candidate family, the same translation spectrum may support different periodic basin geometries.

## 7. A2-SOA-T05 — the full concrete safe unary monoid reconstructs every nondegenerate partition

Let `theta` be a nontrivial proper equivalence relation on `X`: it is neither equality nor the universal relation. Let

\[
M=\operatorname{Safe}_1(q)=T(X,P)
\]

be the **full concrete** partition-preserving transformation monoid acting on `X`.

Then the only equivalence relations on `X` preserved by every map in `M` are

\[
\boxed{\Delta_X,\ \theta,\ \nabla_X.}
\]

### Proof

If an invariant equivalence `E` relates two distinct points in one `theta`-block, a partition-preserving map can send those two points to arbitrary points inside any chosen target block. Hence `E` contains every within-block pair, so `theta subseteq E`.

If `E` relates points from two different `theta`-blocks, partition-preserving maps can send those source blocks to arbitrary target blocks and the two selected points to arbitrary target points. Hence every pair of points is `E`-related and `E=nabla_X`.

If neither event occurs, `E=Delta_X`. Therefore the only remaining nontrivial proper invariant equivalence is `theta` itself. ∎

So, except for the degenerate endpoints `theta=Delta_X` and `theta=nabla_X` (both of which have the full transformation monoid), the **entire concrete safe unary monoid does determine the quotient kernel**.

For an ordered P008 interval quotient, recovering the kernel recovers the ordered basin partition and hence the complete-growth boundary sequence once the level origin is fixed.

This theorem is a reverse-identifiability fact about the full partition-preserving monoid; novelty relative to the transformation-semigroup literature remains to be checked before any priority claim.

## 8. A2-SOA-T06 — successor rigidity for P008 complete-growth collapse

Let

\[
V(0)=0<V(1)<V(2)<\cdots
\]

and let `q_V` be the P008 level quotient with basin

\[
I_k=[V(k),V(k+1)-1].
\]

Then the unary successor

\[
s(n)=n+1
\]

is safe if and only if every basin is a singleton:

\[
\boxed{
+1\text{ safe}
\iff
V(k+1)-V(k)=1\ \forall k.
}
\]

Indeed, if one basin has width greater than one, its first state `x=V(k)` and last state `y=V(k+1)-1` satisfy `q_V(x)=q_V(y)=k`, but

\[
q_V(x+1)=k,
\qquad
q_V(y+1)=k+1.
\]

The converse is immediate because the quotient is then exact equality.

Thus the smallest positive ordinary additive step already forces all basin detail to be causally retained.

## 9. A2-SOA-T07 — ordinary binary addition has no nontrivial P008 quotient

Let

\[
\mu_+(x,y)=x+y.
\]

Then

\[
\boxed{
\mu_+\text{ descends through }q_V
\iff
q_V\text{ is the identity quotient}.
}
\]

If binary addition descends, fix the second input to `1`. Coordinatewise compatibility immediately makes `x->x+1` safe, so T06 forces every basin to be a singleton. Conversely, equality supports exact addition.

This strictly separates two notions that can otherwise be confused:

- a quotient may admit an **external unary translation submonoid**, e.g. `d N_0` for `q_d(n)=floor(n/d)`;
- the same quotient need not admit **internal binary addition of arbitrary represented states**.

For every nontrivial fixed block `d>1`, the first statement holds and the second fails.

## 10. A2-SOA-T08 — ordinary binary multiplication also has no nontrivial unbounded P008 quotient

Assume the boundary sequence `V(k)` is unbounded and let

\[
\mu_\times(x,y)=xy.
\]

Then

\[
\boxed{
\mu_\times\text{ descends through }q_V
\iff
q_V\text{ is the identity quotient}.
}
\]

Suppose a basin contains distinct `x<y`.

If `x=0`, choose a positive boundary `B` and a multiplier `a` with `ay>=B`; then `ax=0` remains below that boundary while `ay` crosses it.

If `x>0`, choose a boundary

\[
B>\frac{xy}{y-x}
\]

and put

\[
a=\left\lceil\frac By\right\rceil.
\]

Then `ay>=B`, while the displayed bound gives `ax<B`. Thus the scalar map `n->an` separates `x,y`. But binary multiplication descent would make every fixed-scalar map safe, contradiction.

Hence no non-singleton basin exists.

Therefore any complete-growth coarse world that insists on ordinary internal semiring operations `(+ , ×)` has no nontrivial information-losing P008 quotient at all.

## 11. Reverse reconstruction has three distinct strengths

The results above give a clean hierarchy.

### Restricted natural language

A small operation language may determine only a scale invariant. Stage-3 periodic translations determine primitive period capacity, not the complete basin word.

### Full concrete safe algebra

The entire concrete partition-preserving unary monoid reconstructs every nondegenerate quotient kernel. This is mathematically complete but usually far larger than a physically or arithmetically natural dynamics.

### Declared operations plus observation/context

For a declared future language and current observation, P023/P024 compute the coarsest compatible refinement by future distinguishability / boundary pullback. This is the operational route to a **natural quotient**: not “which partition happens to have many safe maps?”, but “which distinctions are forced by the actual future tasks and observations?”.

Accordingly, the current causal chain is better written as

\[
\boxed{
\text{causal law}
\to
\text{declared future/context language}
\to
\text{future-safe quotient}
\to
\text{complete-growth basin geometry}
\to
\text{surviving natural operation spectrum}.
}
\]

“Precision” is then a coordinate or complexity measure on this structure, not the primitive object.

## 12. Prior-art boundary

The following generic structures are established mathematics and are not Enterprise Math novelty claims:

- partition-preserving/stabilizing full transformation semigroups `T(X,P)`;
- operations preserving an equivalence relation and the clone `Pol(theta)`;
- congruences, quotient algebras, clone superposition and partition refinement;
- Myhill–Nerode/future distinguishability and related finite-state minimization ideas.

Relevant direct literature includes:

- J. Araújo, W. Bentz, J. D. Mitchell, C. Schneider, *The rank of the semigroup of transformations stabilising a partition of a finite set*, arXiv:1404.1598;
- M. Sarkar, S. N. Singh, *On certain Semigroups of Transformations that preserve a partition*, arXiv:2006.04242;
- L. E. F. Diekouam, E. R. A. Temgoua, M. Tonga, *Meet-reducible submaximal clones determined by nontrivial equivalence relations*, arXiv:1611.06574, as one direct `Pol(theta)` reference.

The project-specific claims under pressure test are the P008 complete-growth specialization, the translation-spectrum non-identifiability boundary, the addition/multiplication no-go theorems, and the causal interpretation of natural operation spectra as the replacement for an externally primitive precision scalar.

## 13. Executable evidence

New exact reference layer:

- `src/enterprise_math/safe_operation_algebra.py`;
- `tests/test_safe_operation_algebra.py`.

Current bounded regressions verify:

1. the unary finite census against exhaustive enumeration on a nonuniform `(2,1)` partition;
2. the binary finite census against all `3^9` binary operation tables on the same partition;
3. the local `+1` obstruction on fixed-width complete growth;
4. the non-identifiability example `width 3` versus periodic `widths (1,2)`;
5. small finite instances of the full-safe-monoid reconstruction theorem.

These tests are executable evidence, not a substitute for the proofs above.

## 14. Next frontier

The next genuinely new classification problem is no longer “what is the full safe clone?” That answer is classical.

It is:

\[
\boxed{
\text{Given a complete-growth law }V
\text{ and a natural ambient operation class }\mathcal A,
\text{ classify }\operatorname{Spec}_{\mathcal A}(q_V).
}
\]

High-value next ambient classes are:

1. monotone integer endomaps with exact P008 boundary-pullback constraints;
2. affine/polynomial integer maps, where degree growth should create strong no-go regimes;
3. typed multi-input causal operations that are not ordinary semiring operations;
4. operations generated by LEGO redistribution/fiber composition, where hidden relation rank may survive even when ordinary arithmetic does not.

That is the point at which number, dimension, quotient, scale, and operation can begin to close into one system without turning classical universal algebra into a novelty claim.
