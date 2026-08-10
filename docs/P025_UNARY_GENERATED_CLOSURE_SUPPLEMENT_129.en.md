# P025 Supplement 129 — Unary-Generated Closure Boundary

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-nonideal-boundary-stage125`  
Depends on: P025 Supplements 126–128  
Hard block: `NONE`

## 1. When is the semantic implication poset already complete?

Supplement 126 derives the largest unary implication preorder. Supplement 127 shows that higher-order conjunction laws can make the full closure strictly coarser. Supplement 128 defines the exact generator horizon.

Stage 129 characterizes the boundary between the unary and genuinely higher-order regimes.

## 2. P025-D52 — mandatory core and unary-generated closure

Define the always-active / mandatory core

\[
\boxed{
M:=\operatorname{cl}_\Omega(\varnothing)
=
\bigcap_{X\in\Omega}X.
}
\]

For a required set \(S\), define the closure generated only by unary consequences:

\[
\boxed{
\operatorname{cl}_1(S)
:=
M
\cup
\bigcup_{s\in S}
\operatorname{cl}_\Omega(\{s\}).
}
\]

By monotonicity of the exact closure,

\[
\boxed{
\operatorname{cl}_1(S)
\subseteq
\operatorname{cl}_\Omega(S).
}
\]

The difference

\[
\boxed{
D(S):=
\operatorname{cl}_\Omega(S)
\setminus
\operatorname{cl}_1(S)
}
\]

is the set of genuinely higher-order consequences of \(S\) not implied by any individual member.

## 3. P025-T282 — exact unary-generated criterion

The following are equivalent:

1. every conjunction closure is determined by the mandatory core and singleton closures;
2. for every \(S\subseteq P\),
   \[
   \boxed{
   \operatorname{cl}_\Omega(S)
   =
   \operatorname{cl}_1(S);
   }
   \]
3. every higher-order defect vanishes:
   \[
   D(S)=\varnothing
   \quad\forall S.
   \]

When these conditions hold, the full conjunctive future is completely described by the semantic implication preorder plus the mandatory core.

When they fail, any \(S\) with

\[
D(S)\ne\varnothing
\]

is an exact certificate that unary relation geometry is insufficient.

## 4. Minimal higher-order defect example

For

\[
\Omega
=
\{\{a\},\{b\},\{a,b,c\}\},
\]

we have

\[
M=\varnothing,
\]

\[
\operatorname{cl}(\{a\})=\{a\},
\qquad
\operatorname{cl}(\{b\})=\{b\},
\]

but

\[
\operatorname{cl}(\{a,b\})=\{a,b,c\}.
\]

Hence

\[
\boxed{D(\{a,b\})=\{c\}.}
\]

This is an irreducible binary implication: `c` is forced by `a AND b` but by neither label alone.

## 5. P025-T283 — exact horizon in the unary-generated regime

Let

\[
P_\Omega=P/{\sim_\Omega}
\]

be the semantic implication quotient poset. All mandatory labels have the all-ones membership column, so if \(M\ne\varnothing\) they form one semantic equivalence class.

Delete that mandatory class and call the remaining induced poset

\[
P_\Omega^{\rm opt}.
\]

If the closure is unary-generated, then every closed query state has the form

\[
\boxed{
M\cup\downarrow A
}
\]

for some antichain \(A\) of optional semantic classes.

The minimum generator of that closed set is exactly its maximal optional antichain. Therefore

\[
\boxed{
g(\Omega)
=
\operatorname{width}(P_\Omega^{\rm opt}).}
\]

If there are no optional semantic classes, the width is interpreted as zero and

\[
\boxed{g(\Omega)=0.}
\]

## 6. Recovery of ordinary poset width

For the all-ideal universe

\[
\Omega=J(P),
\]

there is no mandatory core except labels forced by the original poset universe itself, and

\[
\operatorname{cl}(S)=\downarrow S
\]

is unary-generated.

Hence Stage 129 reduces exactly to the earlier width theorem:

\[
\boxed{g(J(P))=\operatorname{width}(P).}
\]

Thus the P025 width-saturation theorem is not arbitrary: it is the special case of a more general unary-generated closure criterion.

## 7. Mandatory-core correction

Suppose

\[
\Omega
=
\{\{m\},\{m,a\},\{m,a,b\}\}.
\]

Then

\[
M=\{m\}
\]

is always present and should never be paid for as a query generator. The optional semantic poset is the chain

\[
a<b,
\]

so

\[
\boxed{g(\Omega)=1.}
\]

If the only exact state is the full label universe, every semantic class is mandatory and

\[
\boxed{g(\Omega)=0.}
\]

This is why the exact formula uses **optional** semantic width rather than the uncorrected preorder width.

## 8. Architectural consequence

Stages 125–129 now identify four distinct relation layers:

\[
\boxed{
\begin{array}{ccl}
\text{external relation} &:& \text{may be unsafe};\\
\text{semantic unary preorder} &:& \text{largest safe unary relation};\\
\text{full conjunctive closure} &:& \text{exact operation quotient};\\
\text{minimum closure generators} &:& \text{exact semantic arity cost}.
\end{array}}
\]

The unary preorder is complete precisely when the closure is singleton-generated up to the mandatory core.

This gives a precise rule for when a poset-width representation is justified and when higher-order relation state must appear.

## 9. Relation to A2/A4

A2 owns generic future quotients; A4 owns arbitrary correspondence/witness structure. Stage 129 is a Boolean conjunction specialization that supplies an exact criterion for when unary relation geometry suffices.

It should be used as a pressure test for foundation language, not promoted as a competing generic Horn/FCA theory.

## 10. Prior-art discipline

Unary implication systems, closure operators, Horn-style higher-order implications and formal concept analysis are classical. No generic novelty claim is made.

Project-side contribution is the exact P025 boundary between width-governed unary precision and genuinely higher-order closure precision. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/unary_generated_closure.py`;
- `tests/test_unary_generated_closure.py`.

The executable layer checks all-ideal width recovery, higher-order synergy defects, mandatory-core removal, the zero-horizon all-mandatory case and independent optional width-two states.

## 12. Natural generation boundary

Stages 125–129 form one coherent hypothesis-repair generation:

\[
\boxed{
\text{external width failure}
\to
\text{ideal-law iff boundary}
\to
\text{endogenous semantic preorder}
\to
\text{full conjunction closure}
\to
\text{exact generator horizon}
\to
\text{unary-generated iff boundary}.
}
\]

A next generation should no longer ask whether width is correct. It should study the genuinely higher-order closure regime: minimal implication bases, closure-circuit size, composition of closure systems, or the relation between closure generators and A4 multivalued witness correspondences.
