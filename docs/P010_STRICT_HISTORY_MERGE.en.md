# P010 — Exact criterion for strict growth of merged-history multiplicity

Status: `PROVED`  
Open problem: `P010`  
Scope: finite deterministic forward dynamics

## 1. Setup

Let \(X\) be finite. Use the project-wide canonical time convention

\[
F_0=\operatorname{id},
\qquad
F_t=T_{t-1}\circ\cdots\circ T_0\quad(t\ge1),
\]

so

\[
F_{t+1}=T_t\circ F_t.
\]

Here \(T_t\) is the transition from time \(t\) to time \(t+1\).

For \(x\in X\), define

\[
[x]_t=\{y\in X:F_t(y)=F_t(x)\},
\qquad
M_t(x)=|[x]_t|.
\]

T012 proves \([x]_t\subseteq[x]_{t+1}\), hence \(M_t(x)\) is nondecreasing. P010 asks exactly when the inequality is strict.

Write

\[
z_x=F_t(x),
\qquad T=T_t.
\]

Define the reachable collision set

\[
K_{t+1}(x)=\{z\in\operatorname{im}(F_t):T(z)=T(z_x)\}.
\]

It contains \(z_x\) automatically.

## 2. New history class as a union of old fibers

### P010-T01 — Fiber-union update law

Status: `PROVED`

\[
[x]_{t+1}
=
\bigsqcup_{z\in K_{t+1}(x)}F_t^{-1}(\{z\}),
\]

where the union is disjoint.

### Proof

A state \(y\) lies in \([x]_{t+1}\) exactly when

\[
T_t(F_t(y))=T_t(F_t(x)).
\]

Set \(z=F_t(y)\). Then \(z\in\operatorname{im}(F_t)\) and \(T_t(z)=T_t(z_x)\), so \(z\in K_{t+1}(x)\), and \(y\in F_t^{-1}(\{z\})\). The converse is immediate. Fibers over distinct values of a function are disjoint. ∎

Thus a new merged-history class is literally formed by gluing together the old \(F_t\)-fibers whose current reachable states collide under the transition \(T_t\).

## 3. Strict-growth criterion

### P010-T02 — Exact strict-merge criterion

Status: `PROVED`

The following are equivalent:

1. \(M_{t+1}(x)>M_t(x)\);
2. \([x]_t\subsetneq[x]_{t+1}\);
3. \(K_{t+1}(x)\) contains a reachable state other than \(F_t(x)\);
4. there exists \(y\in X\) such that

\[
F_t(y)\ne F_t(x)
\]

but

\[
T_t(F_t(y))=T_t(F_t(x)).
\]

### Proof

Because the classes are finite and T012 gives inclusion, strict cardinal growth is equivalent to strict set inclusion.

By P010-T01, the old class is exactly the fiber over \(z_x\), while the new class is the disjoint union of all fibers indexed by \(K_{t+1}(x)\). Every \(z\in\operatorname{im}(F_t)\) has a nonempty fiber. Therefore the union is strictly larger exactly when \(K_{t+1}(x)\) contains some \(z\ne z_x\). Choosing any \(y\) from that fiber gives condition 4, and conversely condition 4 supplies such a \(z\). ∎

So strict growth occurs exactly when the next transition \(T_t\) is noninjective **on the currently reachable image in the particular output fiber containing \(F_t(x)\)**.

Global noninjectivity of \(T_t\) outside \(\operatorname{im}(F_t)\) is irrelevant.

## 4. Exact integer increment

For a reachable state \(z\in\operatorname{im}(F_t)\), define its old fiber weight

\[
m_t(z)=|F_t^{-1}(\{z\})|.
\]

### P010-T03 — Exact merge-increment formula

Status: `PROVED`

\[
M_{t+1}(x)
=
\sum_{z\in K_{t+1}(x)}m_t(z),
\]

and therefore

\[
\boxed{
M_{t+1}(x)-M_t(x)
=
\sum_{\substack{z\in K_{t+1}(x)\\z\ne F_t(x)}}m_t(z).
}
\]

### Proof

P010-T01 is a finite disjoint union, so cardinalities add. The term indexed by \(z_x=F_t(x)\) is exactly

\[
m_t(z_x)=M_t(x).
\]

Subtract it from the total. ∎

This is a purely integer-valued update law. No logarithm, probability, or measure is required.

## 5. Layer-local injectivity criterion

### P010-T04 — No new merging iff the next map is injective on reachable collision fibers

Status: `PROVED`

For every \(x\in X\),

\[
M_{t+1}(x)=M_t(x)
\]

if and only if \(T_t\) is injective on \(\operatorname{im}(F_t)\).

### Proof

If the restriction is injective, every reachable collision set \(K_{t+1}(x)\) is the singleton \(\{F_t(x)\}\), so P010-T02 gives equality for all \(x\).

Conversely, if the restriction is not injective, choose distinct reachable states \(z,z'\) with equal \(T_t\)-image. Pick \(x\) with \(F_t(x)=z\). Then \(z'\in K_{t+1}(x)\), and P010-T02 gives strict growth. ∎

Hence a deterministic step can be globally many-to-one while creating **zero new history merging** if all of its collisions occur on states that are no longer reachable at time \(t\).

## 6. Example

Suppose the current reachable states have old fiber sizes

\[
m_t(a)=2,\qquad m_t(b)=3,\qquad m_t(c)=1,
\]

and the next map sends

\[
T(a)=T(b)\ne T(c).
\]

For any history currently at \(a\),

\[
M_t=2,
\qquad
M_{t+1}=2+3=5,
\]

so the strict increment is exactly the weight of the newly colliding old fiber:

\[
\Delta M=3.
\]

For a history at \(c\), no reachable state newly collides with \(c\), so its multiplicity remains \(1\).

## 7. P010 resolution

P010 is completely resolved by the reachable-collision criterion:

\[
\boxed{
M_{t+1}(x)>M_t(x)
\iff
\exists y:\ F_t(y)\ne F_t(x),\ 
T_t(F_t(y))=T_t(F_t(x)).
}
\]

The amount of strict growth is exactly the total old multiplicity carried by the other reachable states that join the same next-state fiber.

This identifies the local mechanism of irreversible history merging without introducing entropy as a primitive.

## 8. Consequence for P011

P010 shows that deterministic forward composition acts on the current fiber partition only by **merging blocks**. That immediately suggests many other integer observables besides the multiplicity of one selected history:

- number of lost reachable states;
- number of unordered pairs of histories already merged;
- sum of squares of fiber sizes;
- more generally, sums of superadditive integer functions of block sizes.

Those observables belong to P011 and should be proved there as a separate general family.

## 9. Prior-art discipline

Partition coarsening under deterministic postcomposition, function fibers, and additive cardinality of disjoint unions are standard mathematics; preimage-based noninvertibility measures also have established literature already recorded by the project. P010 does not claim those general ideas as inventions.

The exact project statement is an elementary theorem in the current finite forward-dynamics language. It is `PROVED`; historical novelty of this packaging remains `NOVELTY_UNVERIFIED`.
