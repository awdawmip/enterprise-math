# Shared-context review of the aggregate marked-section bridge

Status: PURE_SYMBOLIC_REVIEW / PASS / NOT_EXECUTED / NOT_ADMITTED. Reviewed the complete `AGGREGATE_HBW_SECTION_BRIDGE.md` at SHA-256 `d406650a2e90037d2c39f4f491f6f250773abd89f3af4f579b787648540b5b41`, together with the previously reviewed marked-section conjugacy. No scientific import, numerical example, arithmetic replay, external query or remote write was performed.

## Algebra checked

For a unit a with inverse b, `ell=(-b,1)` and `M=[[0,1],[-1,a+b]]`, direct multiplication gives `ell M=(-1,a)=a ell` in `Z/NZ`. This is a residue identity; it generally is not exact on unreduced integer lifts. The final draft correctly distinguishes the linear eigen-covector ell from the affine marker L: `L+delta=ell x` is the eigen-observer, while

`L -> t L + delta(t-1)`

for multiplier t. The earlier ambiguous eigen-covector sentence has been corrected in the reviewed hash.

For one parent value L, sum over the four microscopic multipliers `t in [1,1,c,c^-1]`. Their sums are `sum(t)=A1`, `sum(t^2)=A2`, and `sum(1)=4`. Expanding the affine update once and twice yields precisely

```
h0' = 4 h0,
h1' = A1 h1 + delta(A1-4) h0,
h2' = A2 h2 + 2 delta(A2-A1) h1
                  + delta^2(A2-2A1+4) h0.
```

These are polynomial identities over the integers and therefore valid after reduction in any residue ring, with no division by two or four. Substitution of the three translated coordinates gives exactly the claimed diagonal update with multipliers `4,A1,A2`. No hidden order, orbit table or factor enters this derivation.

Writing `m_j=sum(u^j)` over the same indexed microscopic population, substitution of `L=delta(u-1)` gives

`h0 h2-h1^2 = delta^2(m0 m2-m1^2)`.

For the more general affine readout `alpha u+beta`, all beta terms cancel and the determinant is multiplied by `alpha^2`. A certified unit alpha preserves the exact gcd with N, including prime powers. Also, collecting unordered index pairs gives the stated identity

`m0 m2-m1^2 = sum_(i<j)(u_i-u_j)^2`.

This is a division-free integer identity, including repeated microscopic indices. It does not use or justify a finite-field positivity argument. The reviewed source correctly refuses to infer coincident sections or a return/order certificate from a vanishing determinant.

## Required observation scope

The recurrences are for the **unstopped full microscopic population**, under one fixed public multiplier at each layer. They cannot silently consume a killed first-hit distribution or a history-dependent multiplier policy while retaining only one pair of coefficients A1,A2. The final source states the unstopped and public-schedule contract.

There is a further integration boundary: L itself is not invariant under the exchange S, although its gcd is. Consequently the three moments are not generally obtained by putting the entire weight of an S-orbit on its chosen canonical representative and evaluating L there. One must retain the relevant orientation multiplicities or compute the displayed full-population recurrences directly from their initial values. The latter route requires no orbit expansion and is the proposal reviewed here. A direct aggregate implementation should not import the previous folded histograms as if they already contained these moments.

The three residues therefore represent genuine compression for a specified degree-two observable. They preserve neither the full state distribution nor arbitrary future gcd events. In particular, the source correctly separates a sound final divisor certificate from a useful probability of obtaining such a certificate.

## Cost and completion boundary

The recurrence permits a constant number of residue registers per layer once its typed setup and multiplier coefficients are supplied. This avoids enumerating the microscopic histories for **these three statistics**. Every setup inverse/gcd, scalar square, moment operation, determinant operation and final gcd/divisibility check still needs actual typed receipts in an executed unit. A source-level algebraic shortcut is not evidence that the existing rational T0 implementation already performs the required modular arithmetic under the current execution contract.

A final `1<gcd(D_L,N)<N` is a verifiable factor witness. Values 1 or N supply no proper factor, and no repetition/success theorem or order-reconstruction procedure follows. An unlucky or structurally saturated probe remains a valid unsuccessful result. The full first-hit histogram, unknown period, residual native trajectory and general Shor simulator are not recovered from these three numbers.

No blocking mathematical issue remains in the reviewed draft. The result is a COMPOSE/domain-observer bridge using an existing degree-two transport pattern, with a precise weaker certificate target. It is neither a new classical moment theorem nor a completed native Shor algorithm.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
