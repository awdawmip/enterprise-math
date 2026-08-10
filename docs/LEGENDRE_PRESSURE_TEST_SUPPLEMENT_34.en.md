# Legendre Pressure Test — Supplement 34

Status: `PROVED RESEARCH NOTE`  
Scope: full finite split shadows versus the non-realized infinite Boolean completion  
Depends on: P017 L074–L076 and the finite-only precision discipline  
Discipline: product topology, inverse limits of finite Boolean cubes, countability and density are standard mathematics. The project-side result is a concrete P017 example where every finite precision projection is fully realized while the infinite completion contains non-realized ideal states.

## 1. Extend the split task to every prime

For every prime `p`, define

\[
I_p(k)\in\{0,1\}
\]

by the actual split-shell predicate when `p<=k`, and set

\[
I_p(k)=0
\qquad(p>k).
\]

Thus every basin index `k` determines an infinite binary split profile

\[
\boxed{
I(k)=(I_p(k))_{p\text{ prime}}.
}
\]

Because only primes `p<=k` can be active, every actual profile has finite support.

## 2. Every finite coordinate projection is surjective

Fix a finite prime set

\[
P=\{p_1,\ldots,p_m\}.
\]

L074 proves that every pattern

\[
\varepsilon\in\{0,1\}^{P}
\]

occurs with positive natural density among sufficiently large basin indices.

Therefore the coordinate projection

\[
\boxed{
I_P:k\mapsto(I_p(k))_{p\in P}
}
\]

is surjective onto the full Boolean cube

\[
\boxed{
\operatorname{im}I_P=\{0,1\}^{P}.
}
\]

This is exactly the L076 finite precision cube theorem.

## 3. The finite quotient system

For every finite prime set `P`, define the finite quotient

\[
Q_P=\{0,1\}^{P}.
\]

If

\[
P\subseteq Q,
\]

the forgetful projection

\[
\pi_{Q,P}:Q_Q\to Q_P
\]

simply drops coordinates outside `P`.

These maps are surjective and satisfy exact path independence:

\[
\pi_{R,P}
=
\pi_{Q,P}\circ\pi_{R,Q}
\qquad(P\subseteq Q\subseteq R).
\]

Thus the fixed-prime split tasks form a canonical finite projective system.

## 4. P017-L077-A — The inverse-limit completion is the full infinite Boolean product

Status: `PROVED / STANDARD STRUCTURE`.

The inverse limit over all finite prime sets is

\[
\boxed{
\varprojlim_P Q_P
\cong
\{0,1\}^{\mathbb P},
}
\]

where `P` denotes the countable set of all primes.

A compatible family of finite coordinate assignments is exactly one infinite binary assignment to all prime coordinates.

This completion is uncountable.

## 5. P017-L077-B — Actual basin profiles form only a countable subset

Status: `PROVED`.

The domain of actual basin indices

\[
\{1,2,3,\ldots\}
\]

is countable. Therefore its image

\[
\boxed{
\mathcal A
=
\{I(k):k\in\mathbb N\}
}
\]

inside the inverse-limit completion is countable.

Moreover every element of `A` has finite support, because `I_p(k)=0` for every prime `p>k`.

The full product

\[
\{0,1\}^{\mathbb P}
\]

contains uncountably many profiles, including every infinite-support binary sequence.

Hence

\[
\boxed{
\mathcal A
\subsetneq
\{0,1\}^{\mathbb P}.
}
\]

Most completion states are not the split profile of any actual square basin.

## 6. P017-L077-C — The actual image is dense in the completion

Status: `PROVED`.

A basic cylinder set in the product topology fixes only finitely many prime coordinates.

Let that finite set be `P` and let the prescribed pattern be

\[
\varepsilon\in\{0,1\}^{P}.
\]

By L074 the corresponding pattern occurs for a positive-density set of actual basin indices `k`.

Therefore every nonempty basic cylinder intersects `A`.

Hence

\[
\boxed{
\overline{\mathcal A}
=
\{0,1\}^{\mathbb P}.
}
\]

So the actual split profiles are a **countable dense proper subset** of the infinite Boolean completion.

## 7. P017-L077-D — Full finite realizability does not imply global realizability

Status: `PROVED` by L077-A–C.

For every finite prime set,

\[
\operatorname{im}I_P=Q_P.
\]

Every finite precision shadow is therefore fully realized.

Nevertheless

\[
\operatorname{im}I
\ne
\varprojlim_P Q_P.
\]

Thus

\[
\boxed{
\text{all finite projections surjective}
\not\Rightarrow
\text{actual state image equals the inverse-limit completion}.
}
\]

This is a concrete number-theoretic counterexample to the idea that a formally compatible infinite refinement space must be populated by actual states simply because every finite level is.

## 8. P017-L077-E — The infinite split-task family has no finite basis

Status: `PROVED`.

Take any finite set of prime split tasks `S` and choose a prime `q` outside it.

L076 applied to the finite family

\[
S\cup\{q\}
\]

shows that every Boolean pattern is realized. Therefore `I_q` takes both values inside every fixed context pattern on `S`.

Hence

\[
I_q\notin\operatorname{cl}(S).
\]

Because this holds for every finite `S`, no finite set of split coordinates generates the whole infinite task family.

Thus the S19 generator number is not finite for the all-prime split language.

This does not contradict the exact finite basis theorem for each finite prime subfamily.

## 9. Why this matters for the finite-only foundation

The example sharply separates three objects:

1. actual integer basin states `k`;
2. every finite precision quotient `Q_P`;
3. the formal inverse-limit completion over all finite prime coordinates.

The finite quotients are exact and mutually compatible. The completion is mathematically legitimate. But it contains ideal binary profiles not realized by any actual integer basin.

Therefore compatibility of all finite observations does not force the ontology to contain every completion point.

This directly supports the project's discipline:

\[
\boxed{
\text{finite exact consistency}
\neq
\text{ontological commitment to infinite completion}.
}
\]

The conclusion here is mathematical and does not depend on the physical interpretation of Enterprise Math.

## 10. Dense does not mean realized

Because `A` is dense, any finite experiment on split coordinates is compatible with some actual basin state.

But an infinite completion profile may fail to be realized globally.

Thus no finite observation can distinguish an arbitrary completion point from the closure of actual states, while the global state ontology still differs.

This is an exact finite/infinite boundary, not a numerical approximation statement.

## 11. Relation to P005 and inverse refinement

P005 already emphasizes that inverse refinement is generally nonunique and that finite scale compatibility does not supply a unique hidden fine state.

L077 gives a different but complementary phenomenon:

- every finite split-coordinate refinement is fully populated;
- the compatible inverse-limit space is still strictly larger than the actual state image.

So even **existence of all finite lifts** does not imply existence of a corresponding actual infinite state.

## 12. Research-tool rule

Whenever a project constructs a compatible tower of finite precision quotients:

1. distinguish the actual state image from the formal inverse limit;
2. test whether finite projection surjectivity survives globally;
3. do not infer actual realization from density or finite-cylinder consistency;
4. mark completion points as ideal/formal until an independent realization theorem exists;
5. preserve finite theorems even if no ontological infinite completion is assumed.

## 13. Foundation feedback

L077 supplies a concrete arithmetic model for one of the project's deepest methodological claims:

> one may use arbitrarily many compatible finite precision levels without treating the completed infinite object as primitive reality.

Here this is not philosophy: the actual integer system itself gives a countable dense proper subset of its natural infinite precision completion.
