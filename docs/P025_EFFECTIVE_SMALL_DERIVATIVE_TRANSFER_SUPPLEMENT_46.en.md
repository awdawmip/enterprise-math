# P025 Supplement 46 — Effective Small Derivatives Preserve Pasten's Exponent-Transfer Diagram

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplement 42; Pasten `SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES`  
Hard block: `NONE`
Novelty status: `NOVELTY_UNVERIFIED / PRIORITY SEARCH INCOMPLETE`

## 1. Exact scope of Pasten's published implication diagram

Pasten's Small Derivatives Conjecture excludes, up to order, triples of the form

\[
(1,N,q),
\qquad q\text{ prime},
\]

and asks for an absolute exponent

\[
0<\eta<1
\]

such that, outside finitely many remaining primitive triples, there is a relation-adapted nondegenerate arithmetic derivative with

\[
\|\psi\|_\infty<c^\eta.
\]

In P025 notation this is exactly

\[
\boxed{\mu<c^\eta.}
\]

The numerical minimization itself is therefore **Pasten prior art**; P025 only interprets `mu` as a certificate-access precision horizon and compiles it through block-value access.

Pasten proves two exponent-dependent directions:

1. if Small Derivatives holds at exponent `eta`, then Oesterle's weaker abc conjecture holds for every
   \[
   \boxed{M>1/(1-\eta)};
   \]
2. if Oesterle-abc holds for some
   \[
   1<M<2,
   \]
   then Small Derivatives holds for every
   \[
   \boxed{
   \eta>
   1-
   \frac{2-M}{4M}.
   }
   \]

P025 does not claim either published implication.

## 2. P025-C05 — Effective Small Derivatives Conjecture

Retain exactly Pasten's exceptional family and finite-exception convention, but replace the norm by the intrinsic-image normalized quantity from Supplement 42:

\[
\boxed{
\mu_{\rm eff}
=
\frac{\mu}{\eta_{\min}}.
}
\]

For a fixed `0<eta<1`, define `ESD_eta` to mean that for all but finitely many nonexceptional primitive triples,

\[
\boxed{
\frac{\mu}{\eta_{\min}}<c^\eta.
}
\]

Because

\[
\eta_{\min}\ge1,
\]

ordinary Small Derivatives at the same exponent implies ESD pointwise.

The converse is false pointwise: Supplement 42 gives explicit triples where ESD holds at an exponent for which the ordinary norm bound fails.

## 3. P025-T103 — ESD gives Pasten's Lemma-4.1 conclusion with the same exponent

Supplement 42 proves the refined Wronskian-capacity inequality

\[
\eta_{\min}c
\le
\mu\operatorname{rad}(abc)
\left(
\sum_{p\mid a}\frac{v_p(a)}p
+
\sum_{p\mid b}\frac{v_p(b)}p
\right).
\]

Divide by `eta_min`:

\[
 c
\le
\mu_{\rm eff}\operatorname{rad}(abc)S_{ab},
\]

where

\[
S_{ab}
=
\sum_{p\mid a}\frac{v_p(a)}p
+
\sum_{p\mid b}\frac{v_p(b)}p.
\]

For positive `a,b<c`, elementary estimates give

\[
S_{ab}
\le
\frac12
\left(
\sum_{p\mid a}v_p(a)
+
\sum_{p\mid b}v_p(b)
\right)
\le
\frac{\log a+\log b}{2\log2}
<
\frac{\log c}{\log2}.
\]

Assume ESD at exponent `eta`. Then, outside the same finite/exceptional set,

\[
\boxed{
\frac{c}{\log c}
<
\operatorname{rad}(abc)
\frac{c^\eta}{\log2}.
}
\]

This is the same inequality used in Pasten's Lemma 4.1 after imposing ordinary Small Derivatives.

Consequently the same elementary final step gives:

\[
\boxed{
\mathrm{ESD}_\eta
\Longrightarrow
\text{Oesterle-abc}_M
\quad\text{for every }M>\frac1{1-\eta}.
}
\]

Thus the Wronskian-to-abc direction survives after replacing the ordinary derivative norm by the strictly weaker effective norm.

## 4. P025-T104 — the reverse exponent arrow is inherited from Pasten

Suppose Oesterle's abc conjecture holds for some

\[
1<M<2.
\]

Pasten's Theorem 4.5 gives ordinary Small Derivatives for every

\[
\eta>
1-
\frac{2-M}{4M}.
\]

Since

\[
\mu/\eta_{\min}\le\mu,
\]

we immediately obtain ESD for the same allowed exponent range:

\[
\boxed{
\text{Oesterle-abc}_M
\Longrightarrow
\mathrm{ESD}_\eta
\quad
\forall\eta>
1-
\frac{2-M}{4M}.
}
\]

This reverse arrow is not a new proof of Pasten's theorem; it is a direct weakening of his conclusion.

## 5. The proven diagram

At matched definitions/exceptions, the current rigorous implication diagram is

\[
\boxed{
\text{Oesterle-abc}_M
\Longrightarrow
\mathrm{SD}_\eta
\Longrightarrow
\mathrm{ESD}_\eta
\Longrightarrow
\text{Oesterle-abc}_{M'}
}
\]

where Pasten supplies the first arrow for

\[
\eta>1-(2-M)/(4M),
\]

and P025-T103 supplies the last arrow for every

\[
M'>1/(1-\eta).
\]

The middle arrow is pointwise trivial but generally strict.

The Masser-Oesterle abc conjecture, through Pasten's Corollary 4.6, therefore implies the existence of an ESD exponent. Conversely, one ESD exponent implies an Oesterle-type abc exponent exactly as above.

This is the correct sense in which ESD preserves the published exponent-transfer architecture. It is **not** a claim that a single fixed ESD exponent by itself proves the full `1+epsilon` Masser-Oesterle statement.

## 6. Why this is a genuine weakening rather than notation

For

\[
1+242=243,
\]

P025 computes

\[
\mu=27,
\qquad
\eta_{\min}=5.
\]

At exponent `eta=1/3`,

\[
\mu<c^{1/3}
\]

fails, but

\[
\mu/\eta_{\min}<c^{1/3}
\]

holds.

Thus the middle implication

\[
\mathrm{SD}_\eta\Rightarrow\mathrm{ESD}_\eta
\]

cannot be reversed pointwise at fixed exponent.

## 7. Research consequence

The derivative route can now target the weaker conjectural resource

\[
\boxed{
\mu/\eta_{\min}
}
\]

instead of `mu` itself without losing Pasten's Lemma-4.1 implication to Oesterle-abc.

Supplement 43 further decomposes this resource into projective capacity, integer alignment, and absorption-level factors. Hence future attacks can be divided rather than treating small derivatives as one undifferentiated shortest-vector problem.

## 8. Prior-art / novelty discipline

Pasten owns the arithmetic-derivative construction, the Small Derivatives Conjecture, and both published exponent-transfer theorems used here.

P025's candidate addition is only the insertion of the complete normalized Wronskian-image index `eta_min` into the norm resource, together with the proof that the weaker effective condition still supplies the same Lemma-4.1 inequality.

A focused search has not located this exact normalization; that absence is not evidence of originality. Status remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_effective_exponent_transfer.py`;
- `tests/test_abc_effective_exponent_transfer.py`.

All threshold maps are stored as exact rational numbers.

## 10. Next frontier

No hard block exists. Continue with:

1. direct bounds on `mu/eta_min` rather than on `mu`;
2. projective/alignment/absorption decomposition from Supplement 43;
3. exact hard-family analysis when `eta_min=1`;
4. priority audit of effective normalization;
5. no canonical abc claim without a uniform ESD exponent theorem.
