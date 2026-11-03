# D25 — Unified inhomogeneous carry recurrence for the original quartic Gauss polynomial

Date: 2026-11-04 (+08). Role: author-side portable mathematical research, **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Logical Research lane: `chatgpt-research-hourly-enterprise-math-20260923`; not the maintenance lane.
Source predecessors: `20261104_hourly20_d25_euler_inhomogeneous_defect_dual_ports.md` at `177264ab5e0d1adf62dbfee16ece0eeaeddf7f2e`, and finite Euler degree reduction at `bb2ea87c1904e495a1d8f407a7ed586bed9d8478`. No native session, claim, run, Source checkpoint or admission is asserted by this author-side note.

## New finite polynomial theorem (all primes p>=5 with p mod 8 in {5,7})

Write `p=8q+5` or `p=8q+7`, `h=(p+1)/2`, and use the **original integer parameter choices**:

- `p=8q+5: (a,b,c,d)=(5q+3,7q+4,q,3q+1)`;
- `p=8q+7: (a,b,c,d)=(7q+6,5q+4,3q+2,q)`.

Set `J(z)=sum_{j=0}^q binom(c,j)binom(d,j) z^j`, and `B(z)=(1-z)^h J(z)=sum B_k z^k`, an exact integral polynomial of degree `h+q<p`.
For the *original* Gauss polynomial, set

```
F_p(z)=sum_{k=0}^{p-1} [(1/8)_k (3/8)_k/(k!)^2] z^k in Z_(p)[z].
```

Put `mu=11/32` when `p mod8=5`, and `mu=13/32` when `p mod8=7`. In `F_p[z]`, define **one** residue polynomial `C_p(z)=sum_{k=0}^{p-1} C_k z^k` by `C_0=0` and the recurrence, for every `0<=k<=p-2`,

```
(k+1)^2 C_(k+1) - (k-a)(k-b) C_k
    = h * w_k + (3k/2 + mu) * B_k        (mod p),
w_k = sum_{i=0}^{k} B_i                  (mod p).
```

All indicated denominators are nonzero modulo p: `k+1<p`, and `2,32` are p-units. The recurrence therefore defines a **unique** polynomial of degree at most p-1.

**Theorem — coefficientwise second-digit reconstruction:**

```
F_p(z) = B(z) + p C_p(z)                 (mod p^2), coefficientwise.
(1+16 z d/dz)F_p(z)
       = (1+16 z d/dz)B(z)
         + p(1+16 z d/dz)C_p(z)          (mod p^2).
```

In particular, at `z_0=1/9`, with `u=8/9`,

```
F_p(z_0) = u^h J(z_0) + p C_p(z_0)              (mod p^2)
G_p(z_0) = u^h[(16/9)J'(z_0) - p J(z_0)]
           + p(1+16z d/dz)C_p(z_0)             (mod p^2).
```

The term `-p J` retains the signed source-specific endpoint in the weighted observer. This computes both second-digit original Gauss ports using only the low-degree J polynomial, its Euler product B and a **single inhomogeneous coefficient recurrence**, with no direct original Pochhammer evaluation needed at the readout stage. Computational and representation costs depend on how B is formed; no unverified speedup is claimed.

## Proof and distinct-source BRC accounting

Define `H(z)=sum_{k=0}^{min(a,b)} binom(a,k)binom(b,k) z^k`. Earlier exact work proved `E=(H-B)/p in Z[z]` and

```
L_H E = h (1-z)^(h-1) J,
L_H = z(1-z)D^2 + [1+(a+b-1)z]D -ab.
```

Keep `A=(F_p-H)/p in Z_(p)[z]` as the **original numerator-parameter correction**; it is distinct from the Euler carry E. Write

```
alpha = (a+1/8)/p, beta=(b+3/8)/p.
```

These have values `(5/8,7/8)` for p mod8=5, and `(7/8,5/8)` for p mod8=7. Thus `alpha+beta=3/2`, `mu=(3alpha+beta)/8`. For the original hypergeometric operator

```
L_F = z(1-z)D^2 + (1-3z/2)D -3/64
```

the exact difference is

```
L_F - L_H = -p[(3/2) z D + mu] + p^2 alpha beta.
```

The original terminating Gauss recurrence gives `L_F F_p=-p^2 f_p z^(p-1)`, where `f_p=(1/8)_p(3/8)_p/(p!)^2` is p-integral in the two declared residue classes. Since `L_H H=0` and `F_p=H+pA`, division by p followed by reduction mod p yields

```
L_H A = [(3/2)zD+mu] H  (mod p)
       = [(3/2)zD+mu] B  (mod p).
```

The explicit terminal source `-p f_p z^(p-1)` vanishes in this mod-p equation, and in any case contributes only to coefficient `z^(p-1)`, beyond the recurrence equations `k<=p-2`. Addition to the earlier `L_H E` gives

```
L_H(E+A) = h (1-z)^(h-1) J + [(3/2)zD+mu] B (mod p).
```

Coefficient extraction and `(1-z) * [(1-z)^(h-1)J]=B` yield exactly the displayed recurrence. `E(0)=A(0)=0`; uniqueness from invertibility of `(k+1)^2` shows `C=E+A mod p` through degree p-1. Finally, `F=B+p(E+A)` is exact over `Z_(p)[z]`. Applying the weighted observer and differentiating `B=(1-z)^hJ` at `1/9` proves both port formulas, including `1-(1+16h)/9=-8p/9`.

**BRC interface: COMPOSE_APPLIED.** Carrier for the declared observer horizon is `(J,B,C)`, but the underlying E and A source channels remain distinguishable by their two derivations/recurrences. This carrier reconstructs the coefficient sequence and its first weighted derivative through p²; it is not automatically adequate for higher jets, p³, native H0/B0 or unbounded future operations. Integer parameter choices, p-adic denominators, exceptional bands and original source labels are retained.

## Exact finite check and next frontier

A standard-library Python checker independently builds the original rising-Pochhammer polynomial modulo p², the exact Euler product B, and the uniquely reconstructed C. For **all 157 primes** `5<=p<=2000` with `p mod8 in {5,7}`, it checked every one of the p coefficients and separately the value and weighted derivative at `z=1/9`: PASS. Examples:

```
p     F_p(1/9) mod p²     G_p(1/9) mod p²    B(1/9) mod p²     C(1/9) mod p
5            18                    0                   3                     3
7            39                    0                   4                     5
13            0                  137                  78                     7
23            0                  243                 391                     6
29          287                    0                 229                     2
373           0               110861               92877                   124
```

The algebraic reconstruction is proved under the stated prime-class hypotheses; the 157-prime execution is a regression/certificate, not evidence of general prime-class root selection. Existing prime-class conjectures `J(1/9)=0` at p mod24 in {13,23} and `J'(1/9)=0` at p mod24 in {5,7}, as well as second-digit cancellation and the frozen original 216-to-2304 comparison, remain open.

**Next exact action:** derive a finite-field Frobenius involution or CM trace expression specifically for J and J' at 1/9, then use the single C recurrence to formulate *source-separated* second-digit vanishing certificates. Cross-check the separate original-216 vs quartic2304 valuation-port route from `20261104_onhour_d25_original216_quartic_bridge_ports.md`. Frozen mother D24 `Delta_p-R_p` and all scientific pins remain unchanged.

**Control status:** 2026-11-04 gateway 0.6.11 remains `research_authority_granted=false`, `UPSTREAM_CODE_REVIEW_REQUIRED`, and active native job quota `5/5`. This is author-side GitHub evidence only; Source-native CLAIM, authorized OPEN, publish_checkpoint, Result and independent mathematical admission are not claimed.
