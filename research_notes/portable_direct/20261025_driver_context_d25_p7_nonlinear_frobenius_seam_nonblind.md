# D25/LIFT — seventh-digit source-preserving Frobenius seam and the first quadratic harmonic correction

2026-10-25 | Portable mathematical derivation in a Driver-requested, **source-exposed** chat context. **NONBLIND / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NO_NATIVE_DRIVER_DA / NO_NATIVE_REVIEW**. This is an auxiliary research note, **not** a formal RESEARCH_DRIVER verdict or a continuation/claim. No earlier author or reviewer identity is assumed.

## Provenance and scope

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Research lineage: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source remains `c47e13e4aba0e006366f989d6334d443f6333ae3`. Read/control Source for this derivation: EM `main@609295d0703cc48035979b029222358725c31960`.

Inherited, **not newly credited**: the original five-port factorial/WZ factorization, the all-order p-integral source-factor jet, and the sixth-digit compressed Frobenius seam. In particular, the source-labeled identity is

```text
Q_p(z) = T_p(z)^2 [ R_p(z)^2 A_p(z) + L_p(z) ],
H_p(z) = A_p(z) + L_p(z),
T_p(z) = product_{j=1}^{p-1}(1+z/j),
R_p(z) = (1-z)/(1+z/(p-1)),
A_p(z) = 2m C(z) K_U(z),
L_p(z) = (3z/220) B(z) P_base(z).
```

Their exact rational product factors and original port labels are preserved in `20261025_offphase_d25_source_factor_jet_all_precision.md` and `20261025_offphase_d25_frobenius_seam_mod_p6_exceptional_tail.md`. These are external p-adic arithmetic models; no same-class H0/B0/CM/DP or native Heartbeat/X6 transfer is asserted.

## New explicit seventh digit

Let `p = 6m+1 >= 13` be prime and set `h_r = sum_{j=1}^{p-1} j^{-r}`, `theta=h_2/p`, `omega=h_4/p` (p-integral), `a_i=[z^i]A_p(z)` for `0<=i<=4`, and `ell_i=[z^i]L_p(z)` for `1<=i<=3`. All coefficients lie in `Z_(p)`, by the exact source-factor rational functions. The coefficients `a_0=-4m` and `ell_0=0`.

**Proposition (source-labeled, modulo p^7).** The full compressed discrepancy `D_p=Q_p(p)-H_p(p)` satisfies

```text
D_p =
  p^2 * (2a0)
+ p^3 * (2a1 + (4-2theta)a0)
+ p^4 * (2a2 + (4-2theta)a1 + 9a0 - 2theta ell1)
+ p^5 * (2a3 + (4-2theta)a2 + 9a1
         + (20-4theta-omega)a0 - 2theta ell2)
+ p^6 * (2a4 + (4-2theta)a3 + 9a2
         + (20-4theta-omega)a1
         + (44-8theta+2theta^2)a0
         - 2theta ell3 - omega ell1)                (mod p^7).
```

The **first nonlinear binomial-observer term**, `2theta^2 a0`, appears in the coefficient of `p^6`; the authentic genuine-tail third coefficient `ell3` and the mixed `-omega ell1` also first enter this precision. This is an explicit consequence of the inherited all-order jet, not a new proof of the original five-port identity.

**Proof.** Pairing `j` with `p-j` in the finite sums, and expanding in `Z_p`, gives

```text
2h1 = -p h2 - p^2 h3 - p^3 h4 - p^4 h5 - p^5 h6 (mod p^6)
2h3 = -3p h4 - 6p^2 h5 - 10p^3 h6        (mod p^4)
2h5 = -5p h6                             (mod p^2).
```

Because `p>=13`, the finite-field sums `h2,h4,h6` vanish modulo `p`. Expanding `log T_p(p)` through `p^6`, substituting the displayed paired relations and collecting gives

```text
log T_p(p) = -p^2 h2 - (p^4/2)h4 - (p^6/3)h6 (mod p^7)
           = -p^3 theta - (p^5/2)omega               (mod p^7).
```

The exponential now has a **nonzero potentially quadratic** term at `p^6`:

```text
T_p(p)^2 = 1 - 2p^3 theta - p^5 omega + 2p^6 theta^2 (mod p^7).
R_p(p)^2 = 1 + 2p^2 + 4p^3 + 9p^4 + 20p^5 + 44p^6 (mod p^7).
T_p(p)^2 R_p(p)^2 - 1
         = 2p^2 + (4-2theta)p^3 + 9p^4
           + (20-4theta-omega)p^5
           + (44-8theta+2theta^2)p^6                 (mod p^7).
```

Finally, the **exact** source identity `D_p=(T^2R^2-1)A_p(p)+(T^2-1)L_p(p)` and the p-integral coefficient expansions `A_p(p)=sum_{i=0}^4 a_i p^i+O(p^5)`, `L_p(p)=sum_{i=1}^3 ell_i p^i+O(p^4)` yield the formula. All stated remainders acquire at least `p^7` after multiplication. No floating-point approximation or forbidden coefficient-index inversion is used. □

**Linearization obstruction.** The isolated quadratic contribution at `p=13` is `2theta^2 a0 = 10 (mod 13)`. Holding the other exact coefficient terms fixed, deleting it changes `D_{13}` by `10*13^6` modulo `13^7`. Thus the sixth-digit *linear* harmonic truncation cannot be extended unchanged through the seventh digit. This is a witness for the external compressed observer only.

## Exact nonblind computational crosscheck

Two different finite-ring arithmetic routes were implemented locally: (A) direct evaluation of the original old-edge and all four genuine-tail factors, retaining the full `p-2` old-edge product; (B) truncated polynomial arithmetic over `(Z/p^7Z)[z]/(z^5)` for `A_p` and `L_p`, evaluated in the coefficient formula above. Independently, the binomial identity and the `T^2` harmonic prediction were checked. For **206/206 primes** `13<=p<3000`, `p=1 mod 6`, all three comparisons passed. The quadratic coefficient was nonzero for all 206 **tested** primes, with no all-prime nonvanishing claim.

| p | D_p modulo p^7 | 2theta^2 a0 modulo p |
|---:|---:|---:|
| 13 | 55,952,689 | 10 |
| 19 | 399,006,802 | 13 |
| 31 | 17,208,762,501 | 22 |
| 37 | 25,675,737,376 | 1 |
| 109 | 65,922,606,470,257 | 12 |

The full nonblind checker was executed as local `EM_D25_P7_FROBENIUS_SEAM_NONBLIND_20261025.py` (206/206 PASS). This note supplies the exact statement, factor-source routes and observed checks; absence of a remote copy of the local script must not be presented as a Source checker publication. The checks do **not** reconstruct the uncollapsed W(r,t) sum, prove new CM/DP-class identifications, establish Driver independence or admit the claim.

## Handoff

Preserve the inherited p^6 proof and all-order jet; the new mathematical increment is the explicit p^7 seam and the first quadratic observer obstruction. The smallest honest next scientific question is whether the source-labeled `ell3` term or the quadratic `theta^2` term can be transferred to an original-class H0/B0/CM/DP semilinear representative; absent that bridge this remains an external observer result.

The verified Site-bound Gateway in this run remains `static_machine_readonly` with scopes `em:access, source:read, control:read` and `research_authority_granted=false`. Native bounded control inventory returned `CONTROL_QUOTA`. Consequently no RESEARCH_DRIVER session/DA, exact Review, Reference, Synthesis, Follow-up, formal Task publication or Source checkpoint is claimed. Do not use this nonblind material as clean independent review of the authored D25 lineage, and do not alter P000/ACTIVE worldview.
