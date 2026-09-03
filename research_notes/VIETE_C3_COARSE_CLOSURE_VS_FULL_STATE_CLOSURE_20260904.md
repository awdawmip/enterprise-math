# Viète nontrivial C3<-C6 cover forces coarse closure != full-state closure

Status: `FREE_RESEARCH / EXACT SEMANTIC CONSEQUENCE OF NONTRIVIAL COVER / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`

## 1. Why this distinction is necessary

The #1158 winding/deck route uses a nontrivial connected double cover

\[
p:C_6\to C_3.
\]

The coarse `C3` variable records a three-class orientation/ray/slice quotient, while the lifted state retains one additional binary deck/history coordinate.

It is tempting to say that because the coarse transition has order three, one full physical rotation is already completed after three coarse steps. That interpretation is incompatible with the nontrivial cover.

This note states the exact consequence.

## 2. Coarse and refined generators

Let

\[
X=C_3,
\qquad
Y=C_6.
\]

Let

\[
r:X\to X
\]

be the coarse generator and

\[
R:Y\to Y
\]

its connected lift, with

\[
p\circ R=r\circ p.
\]

Then

\[
r^3=\mathrm{id}_X.
\]

But in the nontrivial six-state lift,

\[
\boxed{R^3=H}
\]

where `H` is the nontrivial deck involution, and

\[
H\neq\mathrm{id}_Y,
\qquad
H^2=\mathrm{id}_Y.
\]

Hence

\[
\boxed{R^6=\mathrm{id}_Y.}
\]

## 3. Three-step equality survives only after projection

Because `H` lies in the kernel/deck group of the cover,

\[
p\circ H=p.
\]

Therefore

\[
\begin{aligned}
p\circ R^3
&=p\circ H\\
&=p.
\end{aligned}
\]

So after three refined transitions the coarse observation has returned:

\[
\boxed{p(R^3y)=p(y).}
\]

But the full refined state has not:

\[
\boxed{R^3y=Hy\neq y.}
\]

Thus the same event is simultaneously:

- closed at coarse quotient strength;
- open/nonclosed at full precision-state strength.

This is the exact meaning of hidden deck/history information.

## 4. Full-state order-three semantics would kill the nontrivial cover

Suppose instead one demanded that the coarse equation

\[
r^3=\mathrm{id}
\]

be preserved as an exact law of every refined full orientation state:

\[
R^3=\mathrm{id}_Y.
\]

Then the deck transformation would satisfy

\[
H=R^3=\mathrm{id},
\]

so the nontrivial connected cover is impossible.

Therefore:

\[
\boxed{
\text{NONTRIVIAL }C_3\leftarrow C_6\text{ REFINEMENT}
\Longrightarrow
C_3\text{ IS NOT A COMPLETE ORIENTED FULL-STATE ONTOLOGY}.
}
\]

It is necessarily a quotient/readout that forgets at least the deck/history distinction.

## 5. Winding-memory interpretation

In the winding-parity model write a refined state as

\[
(k,\beta),
\qquad
k\in C_3,
\quad
\beta\in\mathbf F_2.
\]

One positive coarse circuit gives

\[
(k,\beta)\longmapsto(k,\beta\oplus1).
\]

Thus the coarse position `k` returns while the loop-history memory changes.

Only after a second coarse circuit does

\[
\beta\mapsto\beta\oplus1\oplus1=\beta.
\]

This is precisely the six-state closure.

Hence the cover does not claim that a complete direction physically fails to return after a declared full turn. It says that the **coarse three-class observation did not contain enough state to decide full return in the first place**.

## 6. Character consequence

Let a primitive six-state character read the lifted generator as

\[
\chi(R)=\zeta_6.
\]

Then

\[
\chi(R^3)=-1.
\]

The coarse `C3` character pulled back along `p`, by contrast, has order three and cannot detect `H`.

Therefore the primitive six-state character is not merely the pullback of the coarse character. It is a richer observer that couples the coarse class to the hidden deck/history coordinate.

Freeze:

`PRIMITIVE_C6_CHARACTER != PULLBACK_OF_C3_CHARACTER`.

`NEW_CHARACTER_PHASE_USES_NEW_PRECISION_STATE`.

This prevents a hidden assumption that the finer 60-degree-looking phase values were already encoded by the coarse C3 character.

## 7. What “binary precision refinement” means here

The cover

\[
C_3\leftarrow C_6
\]

is therefore not best understood as simply inserting one geometric midpoint between every pair of already-known real angles.

It is a **state refinement**:

\[
\boxed{
\text{coarse class}
\to
(\text{coarse class},\text{one hidden loop/deck bit}).
}
\]

Only after a primitive character is placed on the refined state does the additional binary information receive a half-period phase interpretation.

This is compatible with the wider #1158 principle:

`FINITE STATE REFINEMENT PRECEDES CONTINUOUS ANGLE CALIBRATION`.

## 8. Relation to the three positive native rays

Current three-axis slice Foundation has three positive native rays and no required primitive negative axes.

The present theorem does not alter that native fact.

It says only that if one uses the **three ray/slice labels as a coarse cyclic rotation quotient** and then chooses a nontrivial binary precision cover, equality of those three labels after one coarse circuit is not equality of the full refined orientation/process state.

No current Foundation theorem was found that declares the candidate `C3` ray-label cycle itself to be the complete exact native rotation state with order exactly three. Indeed the broader P000 rotation-law program leaves the exact native rotation law underdetermined.

Therefore the quotient interpretation is allowed as a research architecture, but not automatically promoted to G0.

## 9. Generalization to every binary layer

For

\[
p_m:C_{3\cdot2^{m+1}}\to C_{3\cdot2^m},
\]

let `R_{m+1}` be the fine generator and `R_m` the coarse generator.

The nontrivial deck involution is

\[
H_{m+1}=R_{m+1}^{3\cdot2^m}.
\]

Then one complete coarse cycle returns the level-`m` state after projection but flips the new binary sheet at level `m+1`.

Thus every extra precision bit refines a former equality into two possible full states.

The coherent inverse limit

\[
C_3\times\mathbf Z_2
\]

can therefore be read as an infinite hierarchy of progressively resolved equalities: two histories that coincide at precision `m` may separate at precision `m+1`.

## 10. Precision ontology consequence

This gives a particularly sharp form of finite-resolution ontology:

\[
\boxed{
\text{EQUALITY AT FINITE PRECISION IS QUOTIENT-RELATIVE}.
}
\]

At level `m`, two infinite precision addresses are observationally identical exactly when their projections to

\[
C_{3\cdot2^m}
\]

coincide.

A later precision refinement may split that equality without contradicting the earlier finite observation.

This is more precise than treating finite precision as an approximate real number with an external error bar.

## 11. Boundary

The theorem is conditional on the nontrivial connected binary cover architecture.

It does not prove that actual Cell rotation must use that architecture. Rather, it states an unavoidable semantic commitment of the architecture:

> if the six-gate state is a nontrivial refinement of a three-class coarse rotation quotient, then the three-class closure must be interpreted as coarse observational closure, not full-state identity.

Any future native promotion must respect this distinction explicitly.
