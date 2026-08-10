# P005 — Projective Precision Completion and Realization Boundary, Supplement 01

Status: `PROVED RESEARCH NOTE`  
Owner: A0 / P005 scale-refinement foundation, with a P023 task-precision bridge  
Depends on: P005 compatible finite refinement, P023 finite task quotients, P017 L077 split-profile example  
Discipline: inverse limits, product topology, density, compactness, and countability are standard mathematics. The project contribution is the explicit finite-precision realization boundary and its use inside Enterprise Math.

## 1. The missing question behind compatible finite refinement

P005 already treats compatible finite refinements without assuming a unique hidden fine state.

A stronger question appears whenever there are countably many compatible precision coordinates:

> if every finite set of coordinates is fully realizable, must every compatible infinite coordinate profile be an actual state?

The answer is no.

What finite surjectivity gives exactly is **density** in the projective completion. Global realization requires an additional closure principle.

## 2. Finite product system

Let the coordinate index set be countably infinite,

\[
I=\{1,2,3,\ldots\},
\]

and let every coordinate alphabet `A_i` be finite and nonempty.

For finite

\[
F\subset I,
\]

define

\[
Q_F=\prod_{i\in F}A_i.
\]

Whenever `F subseteq G`, let

\[
\pi_{G,F}:Q_G\to Q_F
\]

forget coordinates outside `F`.

These maps satisfy identity and path-independence:

\[
\pi_{H,F}=\pi_{G,F}\circ\pi_{H,G}.
\]

The inverse limit is naturally

\[
\boxed{
Q_\infty
=\varprojlim_FQ_F
\cong
\prod_{i\in I}A_i.
}
\]

## 3. Actual state image

Let `X` be the actual state space and let

\[
\Phi:X\to Q_\infty
\]

record all declared coordinates.

Write

\[
A=\Phi(X)
\subseteq Q_\infty
\]

for the actually realized profiles.

For every finite coordinate set `F`, the finite precision shadow is

\[
\Phi_F=\pi_F\circ\Phi:X\to Q_F.
\]

## 4. P005-S1-T01 — Full finite realization is equivalent to density

Status: `PROVED`.

The following are equivalent:

1. for every finite `F`, the finite projection `Phi_F` is surjective;
2. the actual image `A` is dense in the product topology on `Q_infty`.

### Proof

A basic open cylinder in the product topology fixes only finitely many coordinates, say those in `F`, to one pattern `a in Q_F`.

If every finite projection is surjective, some actual state realizes that pattern, so every nonempty cylinder meets `A`. Hence `A` is dense.

Conversely, if `A` is dense, every cylinder determined by a finite pattern meets `A`, so every pattern in every `Q_F` is realized. ∎

Thus

\[
\boxed{
\text{all finite shadows surjective}
\iff
\text{actual image dense in the completion}.
}
\]

The conclusion is density, not equality.

## 5. P005-S1-T02 — Countable finite-support counterexample

Status: `PROVED`.

Take binary alphabets

\[
A_i=\{0,1\}
\]

and let `X` be the set of all finite-support binary sequences:

\[
X
=
\{x\in\{0,1\}^{\mathbb N}:\#\{i:x_i=1\}<\infty\}.
\]

Then:

1. `X` is countable;
2. every finite binary pattern is realized by a finite-support sequence;
3. therefore `X` is dense in the full Boolean product;
4. but the full product
   \[
   \{0,1\}^{\mathbb N}
   \]
   is uncountable, so `X` is a proper subset.

Hence

\[
\boxed{
\text{every finite precision level fully realized}
\not\Rightarrow
\text{every inverse-limit point realized}.
}
\]

This is an abstract version of the P017 L077 split-profile phenomenon.

## 6. P005-S1-T03 — Closed-image realization theorem

Status: `PROVED`.

Assume every finite shadow is surjective and the actual image

\[
A\subseteq Q_\infty
\]

is closed in the product topology.

T01 gives that `A` is dense. A subset that is both dense and closed equals the whole space. Therefore

\[
\boxed{
A=Q_\infty.
}
\]

So **closedness is an exact sufficient global realization principle** missing from finite shadow data alone.

Within the finite-shadow-surjective regime, it is also necessary: if `A=Q_infty`, then `A` is obviously closed.

Thus

\[
\boxed{
\text{finite shadow surjectivity}
+
\text{closed actual image}
\iff
\text{full completion realization}.
}
\]

## 7. P005-S1-T04 — Compact-source corollary

Status: `PROVED / STANDARD TOPOLOGY`.

Suppose `X` is a compact topological state space, each coordinate alphabet is finite discrete, and

\[
\Phi:X\to Q_\infty
\]

is continuous.

The product `Q_infty` is Hausdorff. Therefore the compact image `Phi(X)` is compact and hence closed.

If all finite shadows are also surjective, T03 gives

\[
\boxed{
\Phi(X)=Q_\infty.
}
\]

Thus compactness plus continuity is one concrete route by which finite realizability *does* force projective realization.

This is a positive boundary complementary to the finite-support counterexample.

## 8. P005-S1-T05 — Finite precision data cannot distinguish dense proper image from full completion

Status: `PROVED`.

Let `A` be any dense proper subset of `Q_infty`.

For every finite coordinate set `F`,

\[
\pi_F(A)=Q_F.
\]

Therefore every statement depending only on finitely many coordinate values sees exactly the same set of possible finite patterns whether the allowed global state space is `A` or the full completion `Q_infty`.

Yet the global state spaces are different.

Hence

\[
\boxed{
\text{finite observational completeness}
\not\Rightarrow
\text{global ontological equality}.
}
\]

This is a mathematical indistinguishability statement, not an empirical claim about nature.

## 9. P005-S1-T06 — No finite basis in the free finite-shadow model

In the finite-support Boolean counterexample, take all coordinate tasks as the task language.

No finite coordinate set determines any omitted coordinate: after fixing finitely many bits, one may choose an omitted bit to be zero or one while keeping support finite.

Therefore for every finite task subset `S`,

\[
\boxed{
\operatorname{cl}(S)=S.
}
\]

and the infinite task language has no finite basis.

So finite generation of each finite precision level does not imply finite generation of the entire projective task language.

## 10. Relation to P017 L077

P017 supplies an arithmetic realization of exactly this structure.

Its all-prime split profile

\[
I(k)=(I_p(k))_p
\]

has finite support for every actual basin index `k`; every finite prime projection is the full Boolean cube by L074/L076; and the actual image is countable dense but proper inside the infinite Boolean completion.

Thus P017 is not merely an analogy to T02. It is a genuine number-theoretic specialization of the P005 projective-realization boundary.

## 11. Relation to P023 future-safe precision

P023 asks which distinctions a declared finite future language requires.

P005-S1 says that even if **every** finite language has a fully populated exact quotient, the formal limit over all finite languages may contain ideal profiles not produced by any actual state.

Therefore the passage

\[
\boxed{
\text{all finite task quotients}
\longrightarrow
\text{infinite completed task state}
}
\]

is an extra mathematical construction, not a theorem of finite future compatibility.

A realization theorem needs a separate global hypothesis such as closedness/compactness.

## 12. Foundation consequence

Enterprise Math can now separate three statements rigorously:

1. **finite compatibility** — projections commute and every finite quotient is exact;
2. **finite realizability** — every state of every finite quotient is produced by an actual state;
3. **completion realizability** — every compatible infinite profile is produced by an actual state.

The first two do not imply the third.

Hence a theory may consistently use arbitrarily many compatible finite precision levels without making the completed infinite object part of its primitive ontology.

This is not a ban on completions. It is a requirement that a completion be labeled **formal/ideal** until a global realization theorem is supplied.

## 13. Executable specification

- `src/enterprise_math/projective_precision_completion.py`
- `tests/test_projective_precision_completion.py`

The executable model realizes every pattern on each tested finite binary coordinate set using a canonical finite-support profile. Countability, density, properness, and the closed-image theorem are mathematical arguments in this document rather than finite computational claims.

## 14. Prior-art and novelty discipline

Inverse limits, product topology, cylinder sets, dense subsets, compact-image closedness, and the finite-support dense subset of a Boolean product are established mathematics.

The project-specific contribution is the explicit realization taxonomy

\[
\boxed{
\text{finite compatibility}
\to
\text{finite realizability}
\to
\text{completion realizability},
}

with the exact missing closedness principle and the P017 arithmetic specialization.
