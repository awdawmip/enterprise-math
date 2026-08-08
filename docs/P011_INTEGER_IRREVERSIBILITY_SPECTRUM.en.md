# P011 — Integer irreversibility observables from fiber coarsening

Status: `PROVED`  
Open problem: `P011`  
Scope: finite deterministic forward maps and postcomposition

## 1. Setup

Let \(X\) be a finite set with \(|X|=N\), let

\[
F:X\to Y,
\]

and write the nonempty fiber size over a reachable value \(y\in\operatorname{im}(F)\) as

\[
m_F(y)=|F^{-1}(\{y\})|.
\]

If a later deterministic step is

\[
G:Y\to Z,
\]

then \(G\circ F\) can only merge existing \(F\)-fibers. It cannot split one.

P010 identified the local strict-merging criterion for one selected history. P011 asks for other integer-valued observables that are monotone under broad many-to-one forward maps without assuming logarithms.

The answer is a general family indexed by superadditive integer functions, together with a canonical collision spectrum that completely determines the fiber-size distribution.

## 2. General superadditive fiber functional

Let

\[
\varphi:\mathbb N_{>0}\to\mathbb Z
\]

satisfy

\[
\varphi(a+b)\ge\varphi(a)+\varphi(b)
\qquad(a,b\ge1).
\]

Define

\[
I_\varphi(F)
=
\sum_{y\in\operatorname{im}(F)}\varphi(m_F(y)).
\]

### P011-T01 — Superadditive fiber monotonicity

Status: `PROVED`

For every finite \(F:X\to Y\) and every map \(G:Y\to Z\),

\[
\boxed{I_\varphi(G\circ F)\ge I_\varphi(F).}
\]

### Proof

Fix \(z\in\operatorname{im}(G\circ F)\). The new fiber over \(z\) is the disjoint union of the old \(F\)-fibers indexed by reachable \(y\) with \(G(y)=z\):

\[
(G\circ F)^{-1}(\{z\})
=
\bigsqcup_{\substack{y\in\operatorname{im}(F)\\G(y)=z}}
F^{-1}(\{y\}).
\]

Hence

\[
m_{G\circ F}(z)
=
\sum_{\substack{y\in\operatorname{im}(F)\\G(y)=z}}m_F(y).
\]

Repeated superadditivity gives

\[
\varphi(m_{G\circ F}(z))
\ge
\sum_{\substack{y\in\operatorname{im}(F)\\G(y)=z}}
\varphi(m_F(y)).
\]

Summing over new reachable outputs \(z\) partitions all old reachable \(y\), giving the claim. ∎

Thus every superadditive integer weight on fiber size generates a forward-monotone integer irreversibility observable.

## 3. Exact defect decomposition

### P011-T02 — Exact superadditivity-defect formula

Status: `PROVED`

For each new reachable output \(z\), define its group of old reachable states

\[
A_z=\{y\in\operatorname{im}(F):G(y)=z\}.
\]

Then

\[
\boxed{
I_\varphi(G\circ F)-I_\varphi(F)
=
\sum_{z\in\operatorname{im}(G\circ F)}
\left[
\varphi\left(\sum_{y\in A_z}m_F(y)\right)
-
\sum_{y\in A_z}\varphi(m_F(y))
\right].
}
\]

Every bracket is a nonnegative integer.

This formula separates the total irreversible increment into independent collision groups of currently reachable states.

## 4. Strictness

Call \(\varphi\) strictly superadditive when

\[
\varphi(a+b)>\varphi(a)+\varphi(b)
\qquad(a,b\ge1).
\]

### P011-T03 — Strict monotonicity criterion

Status: `PROVED`

If \(\varphi\) is strictly superadditive, then

\[
I_\varphi(G\circ F)>I_\varphi(F)
\]

if and only if \(G\) is noninjective on \(\operatorname{im}(F)\).

### Proof

If the restriction is injective, every set \(A_z\) is a singleton, so every defect in P011-T02 is zero.

If it is noninjective, some \(A_z\) contains at least two reachable states with positive fiber sizes. Repeated strict superadditivity makes that group's defect positive. ∎

This is the global analogue of P010's pointwise reachable-collision criterion.

## 5. Canonical collision spectrum

For \(1\le k\le N\), define

\[
J_k(F)
=
\sum_{y\in\operatorname{im}(F)}\binom{m_F(y)}{k}.
\]

Combinatorially, \(J_k(F)\) is exactly the number of \(k\)-element subsets of histories whose members all have the same \(F\)-image.

In particular,

\[
J_1(F)=N
\]

for every \(F\), while \(J_2\) counts unordered pairs of histories already merged.

### P011-T04 — Collision-spectrum monotonicity

Status: `PROVED`

For every \(k\ge2\),

\[
\boxed{J_k(G\circ F)\ge J_k(F).}
\]

### Proof

For fixed \(k\), the integer function

\[
\varphi_k(n)=\binom nk
\]

is superadditive on positive integers. Indeed, Vandermonde's identity gives

\[
\binom{a+b}{k}
=
\binom ak+\binom bk
+
\sum_{j=1}^{k-1}\binom aj\binom b{k-j},
\]

and all cross terms are nonnegative integers. Apply P011-T01. ∎

For \(k=2\), every merge of two nonempty old fibers creates new cross pairs, so

\[
J_2(G\circ F)>J_2(F)
\]

if and only if \(G\) is noninjective on \(\operatorname{im}(F)\).

Thus \(J_2\) is a globally strict integer detector of new reachable merging.

## 6. Exact increment for collision counts

Suppose one new output \(z\) merges old fibers of sizes

\[
a_1,\ldots,a_r.
\]

Then its contribution to the \(k\)-collision increment is

\[
\Delta J_k(z)
=
\binom{a_1+\cdots+a_r}{k}
-
\sum_{i=1}^r\binom{a_i}{k}.
\]

By the multinomial form of Vandermonde, this counts exactly the newly merged \(k\)-subsets whose elements came from at least two different old fibers.

For \(k=2\),

\[
\boxed{
\Delta J_2(z)=\sum_{1\le i<j\le r}a_i a_j.
}
\]

So pair irreversibility weights a merge by the number of cross-history pairs that become indistinguishable at that step.

## 7. The spectrum is complete for fiber-size statistics

Let

\[
c_r(F)
=
|\{y\in\operatorname{im}(F):m_F(y)=r\}|
\]

be the number of reachable fibers of size exactly \(r\).

Then

\[
J_k(F)
=
\sum_{r=k}^N c_r(F)\binom rk.
\]

### P011-T05 — Integer binomial inversion

Status: `PROVED`

The fiber-size multiplicities are recovered exactly from the collision spectrum by

\[
\boxed{
c_r(F)
=
\sum_{k=r}^N(-1)^{k-r}\binom kr J_k(F).}
\]

### Proof

This is the finite upper-triangular binomial inversion of

\[
J_k=\sum_{r\ge k}\binom rk c_r.
\]

Substituting the proposed inverse and using the standard alternating binomial identity leaves coefficient \(1\) on \(c_r\) and \(0\) on every \(c_s\) with \(s>r\). ∎

Therefore

\[
\boxed{(J_1,J_2,\ldots,J_N)}
\]

uniquely determines the multiset of nonempty fiber sizes.

Because \(J_1=N\) is constant, the irreversibility spectrum

\[
\mathcal J(F)=(J_2(F),\ldots,J_N(F))
\]

together with the known domain size \(N\) is a complete integer encoding of the fiber-size distribution.

It does not recover which specific histories belong to which fiber; it recovers the complete block-size profile of the current history partition.

## 8. Useful special observables

### Lost reachable states

Choose

\[
\varphi(n)=n-1.
\]

Then

\[
I_\varphi(F)
=
\sum_y(m_F(y)-1)
=
N-|\operatorname{im}(F)|.
\]

This counts how many reachable labels have been lost relative to an injective map on \(N\) histories.

### Merged history pairs

\[
J_2(F)=\sum_y\binom{m_F(y)}2.
\]

This counts unordered history pairs already identified by the current map.

### Square fiber energy

\[
Q(F)=\sum_y m_F(y)^2.
\]

Since

\[
n^2=n+2\binom n2,
\]

we have the exact identity

\[
Q(F)=N+2J_2(F).
\]

Thus the square moment is monotone but carries no information beyond \(J_2\) once \(N\) is fixed.

### Higher collision counts

For \(k\ge3\), \(J_k\) records higher-order history coincidences invisible to pair counts alone. The full hierarchy reconstructs the entire fiber-size profile by P011-T05.

## 9. P011 resolution

P011 is resolved at the finite deterministic level by two nested answers:

1. every superadditive integer function of fiber size generates a monotone observable \(I_\varphi\);
2. the canonical binomial family \(J_k\) gives a componentwise monotone integer spectrum that completely determines the fiber-size distribution.

No logarithm, probability distribution, real-valued entropy, or measure is primitive in these constructions.

This does **not** imply that the collision spectrum is thermodynamic entropy. Any relation to Shannon entropy, folding entropy, thermodynamic entropy, or physical entropy production remains a separate comparison problem.

## 10. Prior-art discipline

Function fibers, partition coarsening, Vandermonde identities, binomial inversion, and convex/superadditive block statistics are established mathematics. Preimage-based quantification of noninvertibility is also established prior work already recorded in the project source registry.

Enterprise Math therefore does not claim invention of these ingredients. The project-specific contribution here is to organize them as a primitive integer-first irreversibility layer before introducing logarithmic entropy. Historical novelty of that packaging remains `NOVELTY_UNVERIFIED`.
