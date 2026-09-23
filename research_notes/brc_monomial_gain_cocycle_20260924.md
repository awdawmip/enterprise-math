# BRC monomial branch-gain cocycle

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note does not allocate a new Researcher identity and does not change formal D24/UR ownership. Control issue #1511 remains the gate for lawful successor-session `continuation_prepare -> CLAIM -> OPEN`. The present unit is portable auxiliary BRC research only.

## 1. Consumed singleton carrier

For target primes `p == 13 or 19 (mod 24)`, define

`beta_infty(j)=2j+1`,

`beta_p(j)=2j+epsilon_p(j)+v_p((1+4^j)/j)`.

The preceding singleton-event theorem introduced the signed local displacement

`Delta_p(j):=beta_infty(j)-beta_p(j)`

and the typed local ports

`H_p(j)=1_((p-1)|2j)`,

`D_p(j)=v_p(j)`,

`C_p(j)=v_p(1+4^j)`,

so that

`Delta_p(j)=H_p(j)+D_p(j)-C_p(j)`.

The remaining question was how these local threshold events compose once a monomial uses several ports and multiplicities large enough for factorial denominators to matter.

## 2. Exact branch-gain cocycle

Let `m=(m_1,m_2,...)` be a finite exponent vector. The exact branch weight is

`W_p(m)=sum_j m_j beta_p(j)-sum_j v_p(m_j!)`,

while the conservative generic weight is

`W_infty(m)=sum_j m_j (2j+1)`.

Define the total signed branch gain

`Gamma_p(m):=W_infty(m)-W_p(m)`.

Then, by direct substitution,

`Gamma_p(m)=sum_j m_j Delta_p(j)+sum_j v_p(m_j!)`.

Expanding the typed singleton carrier gives the exact four-port balance law

`Gamma_p(m)=E_p(m)+D_p(m)-C_p(m)+F_p(m)`,

where

`E_p(m)=sum_j m_j H_p(j)`  (harmonic-endpoint credit),

`D_p(m)=sum_j m_j v_p(j)`  (denominator credit),

`C_p(m)=sum_j m_j v_p(1+4^j)`  (coefficient-cancellation debit),

`F_p(m)=sum_j v_p(m_j!)`  (factorial credit).

This identity is exact; it is not an asymptotic estimate and does not require a horizon bound.

## 3. Exact visibility interval for every monomial

The generic first-visible horizon is

`G_p(m)=W_infty(m)+1`,

and the branch first-visible horizon is

`B_p(m)=W_p(m)+1=G_p(m)-Gamma_p(m)`.

Therefore every finite exponent vector has one exact signed threshold interval:

- if `Gamma_p(m)>0`, the monomial is branch-only for exactly `Gamma_p(m)` horizons
  `B_p(m) <= N <= G_p(m)-1`;
- if `Gamma_p(m)=0`, branch and generic first visibility coincide;
- if `Gamma_p(m)<0`, the monomial is generic-only for exactly `-Gamma_p(m)` horizons
  `G_p(m) <= N <= B_p(m)-1`.

Thus the full branch/generic support difference is controlled by an additive gain cocycle plus the local nonlinear factorial credits. No separate horizon-by-horizon case table is needed to decide first visibility once the typed port data are known.

## 4. Global monotonicity for class `19 mod 24`

For `p == 19 (mod 24)`, the preceding order-parity theorem gives

`v_p(1+4^j)=0`

for every `j`. Hence

`C_p(m)=0`

for every monomial, and all remaining terms in the gain law are nonnegative:

`Gamma_p(m)=E_p(m)+D_p(m)+F_p(m) >= 0`.

Therefore

`W_p(m) <= W_infty(m)`

for every exponent vector `m`, with the exact consequence

`M_infty(N) subseteq M_p(N)`

for every integer horizon `N`.

This is a global statement, not just a singleton theorem. Class `19 mod 24` branches can add support relative to the generic observer but can never prune generic support.

This is compatible with the earlier large-prime theorem `M_p(N) subseteq M_infty(N)` for `p>N`: in that regime both inclusions hold, so the two carriers are exactly equal at that fixed horizon.

## 5. Class `13 mod 24`: exact credit/debit law

For `p == 13 (mod 24)`, write

`ord_p(4)=2s_p`,

`kappa_p=v_p(1+4^(s_p))`.

Let

`CANCEL_p={j: j=s_p*u, u odd}`.

The singleton theorem proves:

- if `j in CANCEL_p`, then `Delta_p(j)=-kappa_p`;
- otherwise `Delta_p(j)=H_p(j)+v_p(j)>=0`.

Therefore the monomial gain can be regrouped without losing mechanism provenance as

`Gamma_p(m)=A_p(m)-kappa_p Q_p(m)`,

where

`Q_p(m)=sum_(j in CANCEL_p) m_j`

is the total cancellation-fiber multiplicity and

`A_p(m)=sum_(j notin CANCEL_p) m_j (H_p(j)+v_p(j)) + sum_j v_p(m_j!)`.

Thus:

- `Gamma>0` iff endpoint/denominator/factorial credits strictly exceed the cancellation debit;
- `Gamma=0` iff the two sides balance exactly;
- `Gamma<0` iff the cancellation debit wins.

This is the exact multiport composition law sought after the singleton skeleton.

### Denominator valuation on cancellation fibers does not reappear

A cancellation port divisible by `p^d` does not contribute an additional `d` to `A_p`: its denominator lowering was already neutralized exactly by the LTE increase in the numerator valuation. The only residual singleton contribution of that port is `-kappa_p` per occurrence. Factorial credit remains separate because it belongs to multiplicity, not to the source coefficient.

## 6. Pure cancellation cone is permanently pruning

Suppose `m` is nonzero and supported entirely on `CANCEL_p` for a class-13 target prime. Put

`Q=sum_j m_j > 0`.

Then

`Gamma_p(m)=-kappa_p Q + sum_j v_p(m_j!)`.

Since `kappa_p>=1` and Legendre gives

`v_p(n!) <= n/(p-1)`,

we have

`sum_j v_p(m_j!) <= Q/(p-1) < Q <= kappa_p Q`.

Hence

`Gamma_p(m)<0`.

Therefore every nonzero monomial supported only on class-13 cancellation ports is always delayed relative to the generic observer; factorial denominators can never reverse it into a branch-added monomial.

Equivalently, on this entire cone

`W_p(m)>W_infty(m)`.

This is a useful safe pruning rule for the compiler.

Example `p=13`, cancellation port `j=3`:

- one copy has `Gamma=-1`;
- thirteen copies have `Gamma=-13+v_13(13!)=-12`;
- no multiplicity can make the pure `j=3` direction branch-novel.

## 7. Exact balancing examples

The gain law exposes collisions that are difficult to see from horizon enumeration alone.

For `p=13`:

- `m=e_3`: one cancellation debit, `Gamma=-1`;
- `m=e_6`: one endpoint credit, `Gamma=+1`;
- `m=e_3+e_6`: the two mechanisms balance, `Gamma=0`, so generic and branch first visibility coincide exactly.

For `p=19`:

- `m=e_9`: endpoint credit gives `Gamma=1`;
- `m=e_19`: denominator credit gives `Gamma=1`;
- `m=e_171`: endpoint and denominator collide, giving `Gamma=2`;
- `m=19 e_1`: the only gain is factorial, `Gamma=v_19(19!)=1`.

These examples are manifestations of one balance law, not separate compiler exceptions.

## 8. BRC safe quotient

Before an observer is fixed, keep the provenance-resolved carrier

`(E_p, D_p, C_p, F_p)`

or, when reconstruction of individual ports is required, the full per-port contributions.

For the observer

`MONOMIAL_FIRST_VISIBILITY_RELATIVE_TO_GENERIC`,

the quotient

`(E,D,C,F) -> Gamma=E+D-C+F`

is safe because the exact first-visible interval depends only on `W_infty(m)` and `Gamma`.

For any observer that must explain *why* a monomial moved, or must reconstruct source-coefficient/denominator/factorial origin, collapsing to `Gamma` alone is not safe. In particular, a denominator gain neutralized on a class-13 cancellation fiber must remain distinguishable from an ordinary denominator gain off that fiber.

## 9. Exact falsification

Checker:

`research_checks/check_brc_monomial_gain_cocycle_20260924.py`

Checker commit:

`7c363f029ae9b9b4e3aa8ede26b0f4e3218c513e`.

The checker was executed locally before publication. It tests:

- exact equality between direct branch/generic weights and the four-port gain formula;
- exact first-visibility threshold displacement;
- global nonnegative gain on class `19 mod 24` samples;
- strict negative gain on pure class-13 cancellation-cone samples.

Regression summary:

- target primes below `500`: `23`;
- mixed monomials checked: `46000`;
- pure cancellation-cone monomials checked: `6000`;
- failures: `0`.

Finite computation is falsification/regression only. The theorem is the exact algebraic identity plus the already proved order/LTE structure and Legendre's factorial bound.

## 10. Do not repeat / next

Do not return to treating endpoint, denominator, cancellation, and factorial phenomena as unrelated branch exceptions. Their composition is now exactly the branch-gain cocycle.

If formal D24 control remains blocked, the next information-gain question is no longer “what happens at the next horizon?” It is to exploit the cocycle for a **uniform-union redundancy criterion**: given an exponent vector and a target branch `p`, determine whether an earlier target branch already has at least as much gain at the same generic carrier, preferably reducing branch-set generation to a finite dominance problem rather than enumerating every target prime separately.

If #1511 gains a deployed lossless rollover/disposition operation, stop auxiliary compiler work and resume the Source-native D24 frontier through the lawful successor identity, preserving the existing Source checkpoint and native frontier exactly.
