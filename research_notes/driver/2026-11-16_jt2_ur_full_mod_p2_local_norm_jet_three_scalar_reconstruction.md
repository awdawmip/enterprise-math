# JT2 / UR — complete second-digit local norm–jet from three source-derived residues

Date: 2026-11-16. Status: **PROVED SCOPED LOCAL RECONSTRUCTION / DRIVER AUTHOR-SIDE**, not all-prime UR vanishing, not a frozen Native Result or independent Driver admission.

Provenance: Original ordinary-Legendre/UR norm–jet reduction is by `EM-JT2-EF9380`, and its historical accepted *limited-stage* review is by `EM-DVR-57CCCE`. This additional exact reconstruction is by the exposed line Driver `EM-DVR-DEBB5E`, retaining original SID `MCP-9b4714dc46b948afa4875a86c89c713c`. It consumes prior same-Driver automatic-SIMPLE, balanced-Hensel, and universal mod-`p` Legendre jet results, without claiming independent replication.

## Setting and theorem

Let `p>3` be prime with `p mod 24 in {13,19}`; let `n=(p-1)/3=2m` and let `P_n(X)=Q_m(X²)` be the ordinary Legendre polynomial normalized by `P_n(1)=1`. Work in `Z_(p)`; set `b=1/2`, and retain the *original* norm primitive and balancing polynomial

```text
J_m(Y) = sum_{s=0}^{2m} ([Y^s] Q_m(Y)^2) Y^s/(2s+1),
Phi_p(Y) = 18 Q_m(Y) Q_m'(Y) - p(2 J_m(Y)+3).
```

Write local Taylor coefficients at the **fixed rational lift** `b` as

```text
Q_m(b+z) = sum_{r=0}^m q_r z^r,
J_m(b+z) = sum_{r=0}^{2m} j_r z^r,
Phi_p(b+z) = sum_{r=0}^{2m} f_r z^r.
```

**Theorem (complete mod-`p²` local polynomial from three source-derived residues).** The entire polynomial `Phi_p(b+z) mod p²`, not merely its first derivatives, is uniquely reconstructed from the exact input `p,n` and the three source-computed residues

```text
q_0 = Q_m(b)   (mod p²),
q_1 = Q_m'(b)  (mod p²),
j_0 = J_m(b)   (mod p).
```

No arbitrary polynomial, freely chosen jet, or added axiom is introduced. Use the following **p-integral** recurrence modulo `p²`:

```text
q_{r+2} =
  ((r+1)q_{r+1} + (4r²+2r-n(n+1))q_r)
  / ((r+2)(r+1))                 for 0 <= r <= m-2.
q_r=0 for r>m.
```

Then use the exact norm-primitive relation, reduced modulo `p`, to recover every `j_r`:

```text
j_{r+1} =
  (sum_{i=0}^r q_i q_{r-i} - (2r+1)j_r)/(r+1)  (mod p),
  for 0 <= r <= 2m-1,
```

where only the `q_i mod p` are needed. Finally

```text
f_r = 18 sum_{i=0}^r q_i (r-i+1) q_{r-i+1}
      - p(2j_r+3*[r=0])                       (mod p²),
  for 0 <= r <= 2m.
```

All divisions are by units: `m < p`, `2m=n<p`, and `4m+1=2n+1<p`. The convention `q_i=0` for `i>m` is the actual polynomial degree bound, not a truncation of a nonzero unknown.

Under the original CM0 condition `Q_m(b)≡0 (mod p)`, put `u=q_0/p (mod p)`, `d=q_1 (mod p)`, `j=j_0 (mod p)`. The *unresolved* original full UR scalar is precisely

```text
epsilon_p = f_0/p = 18 u d - 2 j - 3 (mod p).
```

Hence the full local `p²` jet offers no independent substitute for the global arithmetic relation `18ud-2j-3=0`: it transports the exact unknown zeroth-order datum consistently to all higher derivatives. The complete triple is **source-determined** by the original polynomial, not three freely adjustable parameters. This result does not establish the all-prime equality.

## Proof

Substituting `P_n(X)=Q_m(X²)` into the ordinary Legendre ODE gives the *exact* identity

```text
4Y(1-Y) Q_m''(Y)+(2-6Y)Q_m'(Y)+n(n+1)Q_m(Y)=0.
```

At `Y=1/2+z`, it becomes

```text
(1-4z²)Q_m''-(1+6z)Q_m'+n(n+1)Q_m=0.
```

The coefficient of `z^r` is
`(r+2)(r+1)q_{r+2}-(r+1)q_{r+1}+(n(n+1)-4r²-2r)q_r=0`,
which proves the stated `q` recurrence in `Z/(p²)` from `q_0,q_1`.

By the **actual defining coefficient sum** for `J_m`, termwise application of `1+2Y d/dY` multiplies `Y^s/(2s+1)` by `2s+1`. Therefore the following relation is exact over `Q[Y]`, not just a heuristic integral formula:

```text
J_m(Y)+2Y J_m'(Y)=Q_m(Y)^2.
```

At `Y=1/2+z`, coefficient comparison yields
`(r+1)j_{r+1}+(2r+1)j_r=sum_{i=0}^r q_i q_{r-i}`.
All `r+1<=2m<p` are units modulo `p`. Since `-p(2J_m+3)` needs `J_m` only modulo `p`, this uniquely obtains the required local norm contribution. Ordinary polynomial multiplication for `Q_m Q_m'` then gives the displayed `f_r` formula, proving the full mod-`p²` reconstruction.

Under CM0, `q_0=p u` modulo `p²`, so evaluation of the `r=0` case and division by `p` gives the exact original `epsilon_p` expression. Neither the ODE nor the norm-primitive differential identity supplies the missing global value of `j_0` from local differential data alone; that requires the original polynomial/finite sum and remains the arithmetic proof obligation.

## Independent exact finite checks

A separate symbolic calculation built `P_n` via the ordinary Legendre polynomial, directly evaluated derivatives of `Q_m`, `J_m` and `Phi_p` at the rational `b=1/2`, and compared **every** shifted coefficient `f_r` for `0<=r<=2m` modulo `p²` with the reconstruction. Rational reductions used exact numerator/denominator inverses, never floats. All seven instances matched:

| p | m | u (mod p) | d (mod p) | j (mod p) | all f_r mod p² |
|---:|---:|---:|---:|---:|:---:|
| 13 | 2 | 2 | 12 | 0 | yes |
| 19 | 3 | 4 | 17 | 12 | yes |
| 37 | 6 | 9 | 26 | 14 | yes |
| 43 | 7 | 14 | 3 | 11 | yes |
| 61 | 10 | 25 | 36 | 16 | yes |
| 67 | 11 | 28 | 54 | 39 | yes |
| 109 | 18 | 62 | 17 | 56 | yes |

These are auxiliary exact finite checks; the universal theorem follows from the two displayed polynomial identities.

## Next mathematical boundary

The reconstruction provides a compact certificate for proposed higher-precision norm–jet identities. Its input `j_0` is a *global* finite Legendre-square norm, and determining `j_0` jointly with `q_0/p` for all admissible primes is the remaining zeroth-order arithmetic question. In particular, neither an exact finite scan of 575 primes nor all local differential jets proves uniform `epsilon_p=0`.

Frozen source and contributor boundaries: `RR-60983E048B55C2AC7F66`; previous Driver notes `2026-11-16_jt2_ur_legendre_universal_truncated_jet_recurrence.md`, `2026-11-16_jt2_ur_teichmueller_frobenius_drift_lift_invariant.md`. No claim that a Driver-authored extension has received independent Native review, Result acceptance, Task completion, or mother-objective closure.
