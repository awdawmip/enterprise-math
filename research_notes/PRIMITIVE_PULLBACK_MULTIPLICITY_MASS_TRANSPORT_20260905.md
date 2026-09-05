# Primitive pullback: multiplicity scaling versus endpoint prime-mass transport

Status: `FREE_RESEARCH / EXACT FINITE-TYPED THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive pullback semigroup law;
- `deg Psi_d=phi(d)`;
- primitive endpoint mass `P_d=|Psi_d(0)|`.

## 1. Pullback branch family

For phase multiplication `R_n`, the primitive factor pullback is

\[
\operatorname{Monic}(\Psi_d\circ R_n)
=\prod_{\substack{g\mid n\\(d,n/g)=1}}\Psi_{dg}.
\]

Call the divisor fiber

\[
\mathcal F_n(d)
:=\{dg:g\mid n,\ (d,n/g)=1\}.
\]

The factors in this family are distinct primitive spectral channels.

## 2. Primitive spectral multiplicity scales by n

Since

\[
\deg\Psi_e=\varphi(e),
\]

degree comparison gives

\[
\boxed{
\sum_{e\in\mathcal F_n(d)}\varphi(e)
=n\varphi(d).
}
\tag{PMT-1}
\]

Thus the total primitive mode count in an `n`-fold phase pullback is exactly `n` times the source primitive mode count.

This is a support/multiplicity statement.

## 3. Primitive endpoint prime mass is conserved

Define the positive integer endpoint mass

\[
P_d:=|\Psi_d(0)|
=\begin{cases}p,&d=p^a,\\1,&\omega(d)\ge2.
\end{cases}
\]

Because

\[
R_n(0)=0,
\]

evaluation of the pullback identity at zero gives

\[
\boxed{
P_d
=\prod_{e\in\mathcal F_n(d)}P_e.
}
\tag{PMT-2}

Thus the multiplicative endpoint prime mass is exactly conserved across the pullback branch family.

Taking the later logarithmic readout gives

\[
\boxed{
\Lambda(d)
=\sum_{e\in\mathcal F_n(d)}\Lambda(e).
}
\tag{PMT-3}

So `phi` is an `n`-scaling multiplicity functional on the pullback semigroup, while `Lambda` is an invariant additive mass functional.

## 4. Prime-local transport rule

For one prime `p`,

\[
\mathcal A_p[d]
=\begin{cases}[d]+[pd],&p\nmid d,\\[pd],&p\mid d.
\end{cases}
\]

### p already present

If `d=p^a`, then

\[
\mathcal A_p[p^a]=[p^{a+1}].
\]

The unique descendant has

\[
P_{p^{a+1}}=P_{p^a}=p.
\]

Thus the prime mass moves one step deeper along its own `p`-adic ray without splitting.

### new prime q != p

If `d=p^a` and `q!=p`, then

\[
\mathcal A_q[p^a]=[p^a]+[p^a q].
\]

The endpoint masses are

\[
P_{p^a}=p,
\qquad
P_{p^a q}=1.
\]

Therefore the newly created mixed channel is positive-mass neutral; the old ancestral channel retains the full prime mass.

At the same time the degrees split as

\[
\varphi(p^a)+\varphi(p^a q)
=\varphi(p^a)+(q-1)\varphi(p^a)
=q\varphi(p^a).
\]

So a foreign prime creates `(q-1)phi(p^a)` genuinely new primitive spectral dimensions with no new endpoint prime mass.

## 5. General support/mass separation

For arbitrary `d`, each new prime factor absent from `d` can create mixed descendant channels.  Any descendant containing at least two distinct primes has endpoint mass one, even though its primitive mode count is positive.

Hence under phase pullback:

\[
\boxed{
\text{TOTAL PRIMITIVE MODE COUNT}
\text{ scales by }n,
}
\]

while

\[
\boxed{
\text{MULTIPLICATIVE ENDPOINT PRIME MASS}
\text{ is conserved}.
}
\]

These are different observers and must not be recoalesced.

## 6. Relation to mixed join defects

The higher join-defect theory found that pure mixed denominator factors satisfy

\[
P_d=1
\]

while carrying nonzero support and reciprocal moments.

The present pullback law shows the local generation mechanism for exactly those factors:

```text
introduce a prime absent from the source denominator
 -> preserve ancestral primitive channel
 -> create mixed descendants
 -> descendants add spectral multiplicity
 -> descendants contribute endpoint mass 1
```

Thus `mixed mass = 1` is a structural consequence of prime-extension branching, not an isolated cancellation at the join level.

## 7. Typing consequence

The same finite branch family carries at least two independent exact summaries:

- `phi`: primitive supported-mode multiplicity, scaling by phase degree;
- `P` / derived `Lambda`: prime endpoint mass, conserved under pullback.

So

`MODE_MULTIPLICITY_GROWTH != ENDPOINT_PRIME_MASS_GROWTH`.

Freeze:

`PHASE_PULLBACK_MULTIPLICITY_SCALE = n`.

`PHASE_PULLBACK_ENDPOINT_PRIME_MASS = CONSERVED`.

`FOREIGN_PRIME_BRANCH_CREATION = MASS_NEUTRAL_BUT_SUPPORT_NONTRIVIAL`.
