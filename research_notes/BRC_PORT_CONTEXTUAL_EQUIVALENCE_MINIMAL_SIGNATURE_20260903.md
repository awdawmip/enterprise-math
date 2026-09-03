# BRC Port Contextual Equivalence and Minimal Module Signatures

Status: `RESEARCH CANDIDATE / EXACT FINITE-RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parent result: recurrent Schur operation-safe collapse, PR #1152 / merge `40d3ec9e7786bafddb6e10694e2d60137a65850b`

## 1. Purpose

PR #1152 proved that a stable internal block can be Schur-eliminated to an exact effective boundary matrix and that every future positive update supported only on retained boundary edges commutes with that collapse.

This note enlarges the context language and asks for **minimal black-box module signatures**.

A module has internal states `I` and labeled ports `B`, with rows=source and columns=target:

\[
M=
\begin{pmatrix}
A & X\\
Y & B
\end{pmatrix},
\qquad
S_I=(I-A)^{-1},
\qquad
W_{\rm eff}=B+YS_IX.
\]

Assume the internal block `A` is stable. Generic Schur complements, boundary response maps, stochastic complements, Dirichlet-to-Neumann/Poincare-Steklov maps, and network black-box reductions are classical prior art. The project-specific question is the exact positive-recurrent BRC contextual contract and its minimal rational signature.

## 2. General positive rational port context

Let `E` be any finite set of newly supplied external states. A context may add:

- arbitrary non-negative rational port-to-port mass `C`;
- arbitrary port-to-external mass `U`;
- arbitrary external-to-port mass `V`;
- arbitrary external-to-external mass `R`.

The context is forbidden to connect directly to the hidden internal states `I`.

The full composite matrix, ordered `(I,B,E)`, is

\[
\boxed{
\mathcal C(M)
=
\begin{pmatrix}
A & X & 0\\
Y & B+C & U\\
0 & V & R
\end{pmatrix}.
}
\]

Eliminating `I` gives the **ported reduced composite**

\[
\boxed{
\mathcal C_{\rm eff}(M)
=
\begin{pmatrix}
W_{\rm eff}+C & U\\
V & R
\end{pmatrix}.
}
\]

This is the same external context with the hidden module replaced by one exact weighted port block.

## 3. Port-context theorem

### Candidate BRC-PC1

For every finite non-negative rational port context as above:

\[
\boxed{
\mathcal C(M)\text{ stable}
\iff
\mathcal C_{\rm eff}(M)\text{ stable}.
}
\]

When stable, the full star restricted to visible states `B union E` is exactly

\[
\boxed{
(I-\mathcal C(M))^{-1}[B\cup E,B\cup E]
=
(I-\mathcal C_{\rm eff}(M))^{-1}.
}
\]

**Reason.** This is PR #1152 applied after treating `B union E` as the retained boundary. The hidden internal block and hidden/port couplings are unchanged, and there are no hidden/external direct edges.

Thus `W_eff` is a complete exact black-box state for all visible positive total-mass dynamics under arbitrary finite port contexts.

## 4. Contextual equivalence

For two modules `M_1,M_2` with the same labeled port set, call them **port-dynamically equivalent** when every finite non-negative rational context produces:

1. the same stable/unstable outcome;
2. whenever stable, the same star on the visible states `B union E`.

### Candidate BRC-PC2 — complete classification on stable modules

For modules whose no-extra-context composites are stable,

\[
\boxed{
M_1\equiv_{\rm port}M_2
\iff
W_{\rm eff}(M_1)=W_{\rm eff}(M_2).
}
\]

**Sufficiency** is BRC-PC1: every reduced composite is literally identical.

**Necessity.** Choose the empty external context (`E=empty`, `C=0`). Port-dynamic equivalence gives equal boundary stars

\[
(I-W_{{\rm eff},1})^{-1}
=(I-W_{{\rm eff},2})^{-1}.
\]

Both are invertible on the stable phase, hence

\[
W_{{\rm eff},1}=W_{{\rm eff},2}.
\]

Therefore `W_eff` is not merely sufficient; under this observation contract it is a **minimal complete exact port signature up to bijective re-encoding**.

## 5. Loop-zeta-enhanced context

The hidden internal recurrent scalar is

\[
\boxed{
Z_{\rm int}(M)=Z_{\rm loop}(A)=\frac1{\det(I-A)}\in\mathbb Q_{\ge1}.
}
\]

For every stable context,

\[
\det(I-\mathcal C(M))
=\det(I-A)\det(I-\mathcal C_{\rm eff}(M)),
\]

so

\[
\boxed{
Z_{\rm loop}(\mathcal C(M))
=Z_{\rm int}(M)\,
Z_{\rm loop}(\mathcal C_{\rm eff}(M)).
}
\]

and

\[
\Gamma(\mathcal C(M))
=\Gamma(A)+\Gamma(\mathcal C_{\rm eff}(M)).
\]

## 6. Minimal zeta signature

Call two stable modules **zeta-contextually equivalent** if they are port-dynamically equivalent and every stable finite port context also gives the same full global `Z_loop`.

### Candidate BRC-PC3

\[
\boxed{
M_1\equiv_{\rm port+zeta}M_2
\iff
\bigl(W_{{\rm eff},1},Z_{{\rm int},1}\bigr)
=
\bigl(W_{{\rm eff},2},Z_{{\rm int},2}\bigr).
}
\]

Sufficiency follows from the factorization above.

For necessity, dynamic equivalence first recovers `W_eff`. In the empty context,

\[
Z_{\rm int}
=
\frac{Z_{\rm loop}(M)}{Z_{\rm loop}(W_{\rm eff})},
\]

so equal total zeta forces equal hidden zeta.

Thus the exact rational signature ladder is:

\[
\boxed{W_{\rm eff}}
\quad\text{for visible recurrent dynamics},
\]

\[
\boxed{(W_{\rm eff},Z_{\rm int})}
\quad\text{for visible dynamics + global loop-zeta/Gamma}.
\]

The log scalar `Gamma(A)` is only a derived readout of the exact rational `Z_int`.

## 7. Necessity witness: same port dynamics, different hidden recurrence

Use one labeled port `b` and one hidden state.

### Module M1

\[
A_1=[0],
\quad X_1=[1/4],
\quad Y_1=[1/4],
\quad B_1=[1/10].
\]

Then

\[
W_{{\rm eff},1}
=1/10+(1/4)(1)(1/4)
=13/80,
\]

and

\[
Z_{{\rm int},1}=1.
\]

### Module M2

\[
A_2=[1/2],
\quad X_2=[1/8],
\quad Y_2=[1/4],
\quad B_2=[1/10].
\]

Since `(I-A_2)^-1=2`,

\[
W_{{\rm eff},2}
=1/10+(1/4)(2)(1/8)
=13/80,
\]

but

\[
Z_{{\rm int},2}=2.
\]

Hence the two modules are exactly port-dynamically interchangeable in every allowed context but their full loop-zeta values differ by the constant factor `2` in every stable context.

This proves `W_eff` alone is insufficient once global recurrent scalar observation is added.

## 8. External feedback and interaction compatibility

Any declared future feedback event whose endpoints lie in `B union E` is computed from visible star entries only. By BRC-PC1 those star entries are identical in the full and reduced composites.

Therefore every already-Foundation feedback observable commutes with module substitution:

- `WBRC-T25` feedback-event condensation;
- `WBRC-T26` exact additive/multiplicative robustness;
- `WBRC-T27` conditional feedback chain;
- `WBRC-T28` subset zeta / all-orders Mobius interactions;
- `WBRC-T29` interaction girth / circuit atoms.

So `W_eff` is a complete port signature not merely for static star queries but for the current full finite positive feedback operation language applied outside the hidden internal states.

## 9. Hierarchical composition

Suppose an external context itself contains another hidden module and is later Schur-collapsed. Because Schur elimination is transitive, replacing the first module by `W_eff` before or after eliminating other disjoint hidden blocks gives the same final visible matrix whenever the required internal blocks are stable.

Therefore exact module black-boxing composes hierarchically:

```text
leaf recurrent modules
-> exact W_eff port signatures
-> connect signatures through ports
-> eliminate higher-level hidden modules
-> repeat.
```

For global zeta, multiply the hidden rational factors `Z_int` along the elimination tree. The product is order independent although the stagewise factor assignment depends on the chosen hierarchy.

## 10. Port relabeling

If two modules use different port names but a declared bijection `P` identifies them, the effective matrices transform by permutation similarity. Thus contextual equivalence with relabeled ports is

\[
W_{{\rm eff},2}=P^{-1}W_{{\rm eff},1}P.
\]

Without an explicit port bijection, labels are semantic and may not be silently quotient-identified.

## 11. Boundary of the minimality claim

The minimality statements are relative to the declared observation/context language.

- If only a weaker scalar such as final stability is observed, `W_eff` may contain more information than necessary.
- If internal state reconstruction is required, `(W_eff,Z_int)` is insufficient; retain additional port-to-internal transfer data such as `(S_I,X,Y)`.
- If future contexts may connect directly to hidden internal states, the port signature lease is violated.
- CWM count/dominant/provenance is not preserved by total-mass Schur collapse.
- Signed/amplitude or complex contexts are outside the current positive-rational theorem.

Therefore “minimal” here means **coarsest exact signature for the specified visible star/stability context semantics**, not universal minimal information for every possible observer.

## 12. Prior-art boundary

Schur-complement black-boxing, boundary response maps, stochastic complements, Dirichlet-to-Neumann/Poincare-Steklov operators, Kron reductions and exact aggregation are classical/general mathematics.

Enterprise Math does not claim novelty for those generic ideas.

The project-specific reusable synthesis proposed here is:

\[
\boxed{
\text{finite positive recurrent BRC module}
\to W_{\rm eff}
\to\text{exact contextual equivalence under all positive rational port contexts}
}
\]

with the additional exact rational hidden-zeta coordinate when global loop surplus is observed.

## 13. Validation plan

Use exact `Fraction` arithmetic only.

1. Use the explicit `M1/M2` witness above and exhaust all one-external-state contexts with `C,U,V,R` in `{0,1/6,1/4}` (`3^4=81` contexts). Verify identical stability and visible star for every context, while every stable full zeta ratio is exactly `2`.
2. Construct a third module with different `W_eff` but the same `Z_int` and verify the empty context already distinguishes its visible star.
3. On a nontrivial two-port / two-hidden-state module, compare the full composite against the reduced composite over an exact corpus of 2-external-state contexts; verify visible star and determinant factorization.
4. Add external feedback events involving ports and external states and verify full versus reduced feedback kernels, interaction factors and critical radii are identical.
5. Verify hierarchical two-module substitution and elimination order on a selected exact network.
6. Verify a port permutation produces permutation-similar effective matrices and identical contextual behavior after relabeling.

A dedicated research CI gate must pass before any Foundation backflow.
