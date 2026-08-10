# P025 Supplement 99 — Action-Relative Dual Repairs for the Activation Potential

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-orbit-normal-stage91`  
Depends on: P025 Supplements 96–98  
Hard block: `NONE`

## 1. Threshold action repaired one directional failure

Stage 98 proves that the scalar activation area

\[
A
\]

is not future-safe under a declared threshold insertion.

For that action, the exact one-step repair is the new threshold crossing depth

\[
j_T,
\]

or equivalently the directional increment

\[
\Delta_TA.
\]

Stage 99 asks for the exact dual statement under the other primitive Stage-94 extension: appending one dyadic orbit node.

## 2. Reuse the same equal-area fiber

Keep the same current grid

\[
\left(\frac12,1\right)
\]

and horizon `h=1` from Stages 97–98.

The two exact states still satisfy

\[
\boxed{A^{\rm flat}=A^{\rm jump}=2.}
\]

### Flat state

\[
(q,p)=(3,5),
\qquad
(\rho_0,\rho_1)=\left(\frac12,\frac12\right).
\]

### Jump state

\[
(q,p)=(7,17),
\qquad
(\rho_0,\rho_1)=\left(\frac16,\frac{13}{6}\right).
\]

## 3. Apply the same orbit-extension action

Append one new dyadic difference node to each state.

For the flat orbit, the next tested pressure remains at the low-threshold level, so the new node reaches exactly one of the two old thresholds. Its rank is

\[
\boxed{r_{\rm new}^{\rm flat}=1.}
\]

By Stage 96,

\[
\boxed{A_{\rm next}^{\rm flat}=2+1=3.}
\]

For the jump orbit, monotonicity from Stage 86 already gives

\[
\rho_{\rm new}\ge\frac{13}{6}>1.
\]

So both old thresholds are reached:

\[
\boxed{r_{\rm new}^{\rm jump}=2,}
\]

and

\[
\boxed{A_{\rm next}^{\rm jump}=2+2=4.}
\]

## 4. P025-C39 — area is not future-safe under orbit extension either

The two current states lie in the same area fiber

\[
A=2,
\]

but the same orbit-node extension produces

\[
\boxed{3\ne4.}
\]

Therefore the scalar quotient

\[
q_A(B)=A(B)
\]

also fails P023 fiber constancy for the future map

\[
F_J(B):=A(E_J(B)),
\]

where `E_J` appends one dyadic orbit node.

Hence

\[
\boxed{
\text{activation area is not a Markov state for either primitive extension axis.}
}
\]

## 5. P025-T240 — exact orbit-action repair by new node rank

Stage 96 gives the exact orbit-axis derivative

\[
\Delta_JA=r_{\rm new}.
\]

Therefore

\[
\boxed{A_{\rm next}=A+r_{\rm new}.}
\]

So the exact one-step natural repair is

\[
\boxed{(A,r_{\rm new}).}
\]

This is the orbit-axis dual of Stage 98's

\[
(A,j_T).
\]

## 6. P025-T241 — threshold and orbit repairs are directional derivatives

For threshold insertion,

\[
\boxed{
\text{repair coordinate}=j_T
\leftrightarrow
\Delta_TA.
}
\]

For orbit-node append,

\[
\boxed{
\text{repair coordinate}=r_{\rm new}
=
\Delta_JA.
}
\]

Thus the two one-step repairs are exactly the two directional first derivatives of the Stage-96 scalar potential.

This gives a clean dictionary:

\[
\boxed{
\begin{array}{c|c|c}
\text{declared action}
&\text{natural response coordinate}
&\text{area increment}\\ \hline
+T&j_T&h+1-j_T\text{ or }0\\
+J&r_{\rm new}&r_{\rm new}
\end{array}}
\]

## 7. P025-D42 — action-relative repair compiler

Define a one-step repair compiler whose input is:

1. the current coarse scalar area;
2. the declared future action;
3. the action parameter when required.

Then:

- if the action is threshold insertion `+T`, reveal crossing depth `j_T`;
- if the action is orbit append `+J`, reveal new node rank `r_new`.

The repaired future area is reconstructed exactly from the chosen directional coordinate.

So the compiler is

\[
\boxed{
\text{action}
\longmapsto
\text{directional response coordinate}.
}
\]

It does not request both coordinates when only one action is declared.

## 8. P025-T242 — the repair vocabulary itself is action-relative

The two repairs do not merely carry different numerical values. They live in different coordinate vocabularies:

- `j_T` is threshold-centric and indexed by a future threshold;
- `r_new` is orbit-centric and indexed by a future node.

Therefore changing the action can change the **type** of additional precision required.

This is stronger than saying that one action needs a larger amount of precision than another.

The correct statement is:

\[
\boxed{
\text{future action can change the repair coordinate family itself.}
}
\]

## 9. One coarse state, two exact repairs

For the jump state with current area `2`:

### Threshold action

Insert

\[
T=\frac34.
\]

Then

\[
j_T=1,
\qquad
\Delta_TA=1,
\]

so

\[
A_{\rm next}=3.
\]

### Orbit action

Append one new node. Then

\[
r_{\rm new}=2,
\qquad
\Delta_JA=2,
\]

so

\[
A_{\rm next}=4.
\]

The same current scalar state therefore asks for different repair coordinates under different action languages.

## 10. P025-C40 — no action-independent one-coordinate claim is justified here

Stages 98–99 prove exact one-coordinate repairs **after the action is declared**.

They do not prove that one universal scalar repair coordinate exists that is simultaneously optimal for both primitive action families.

Any such stronger compression would require a separate factorization theorem.

Therefore the safe architectural conclusion is action-relative selection, not a new universal coordinate.

## 11. Relation to P023 operation families

P023 studies future-compatible operation families, not only one map.

Stages 98–99 provide the smallest nontrivial arithmetic example in which:

- one coarse state is unsafe for two distinct actions;
- each action has a simple one-step repair;
- the two repairs are different directional coordinates of one potential.

For a declared operation family containing both actions, the next question is whether the pair of directional responses, or a richer boundary chart, is the correct family-safe state.

That question is deliberately left for the next stage rather than silently answered.

## 12. Relation to P024 action-language precision

P024's central concern is that precision requirements depend on the action language.

Stage 99 supplies an exact number-theoretic witness:

\[
\boxed{
\text{same coarse state}
+
\text{different action}
\Longrightarrow
\text{different repair coordinate type}.
}
\]

This is a direct Relay candidate.

## 13. Prior-art / novelty discipline

Directional derivatives, action-dependent state augmentation and response coordinates are broad prior concepts.

P025 claims none of them in isolation.

The project-side result is the exact arithmetic dual-repair compiler induced by the Ferrers activation potential. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 14. Executable assets

Added:

- `src/enterprise_math/abc_activation_area_action_repair.py`;
- `tests/test_abc_activation_area_action_repair.py`.

The executable layer verifies the orbit-side future collision, new-rank repair, threshold/orbit action compiler, directional increments and action contract errors.

## 15. Next frontier

No hard block exists. Continue with a finite **operation family** rather than one action:

1. declare a finite set of candidate threshold insertions together with one orbit append;
2. derive the smallest natural response signature that predicts the next area for every action in the family;
3. exploit the threshold ordering to compress the threshold-response vector as a staircase;
4. compare the resulting family-safe state with the full Ferrers boundary;
5. use this to decide the exact common abstraction to Relay to P023/P024/A2.
