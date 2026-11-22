# R5: all-positive-threshold 41-primary coefficient-period classification via an 82-step rational identity

Date: 2026-11-23 (Asia/Shanghai). Mathematical status: **AUTHOR_EXACT_PROOF / REUSED_EXACT_INTEGER_ZEROS / NEW_FINITE_FIELD_NONZERO_WITNESS / NOT_REVIEWED**. Independent informed portable research; no shared CLAIM/Result, P000 theorem or native X6/BRC promotion. Scientific model frozen at `awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15`.

Predecessor: `2f93df67adc3731aa7f0c93028f66b641d964ed1:research_notes/portable_direct/r5_d41_exact_window_20261123/RESEARCH.md`. Its exact integer cyclic computation establishes the five characteristic-zero zeros at thresholds 78,79,80,81,82. This note extends that finite window to infinitely many thresholds, and obtains the exact converse using a new modular witness.

## Statement

Let the frozen prices be `214..314`, with multiplicities `a_p>=0`. Let the failure events `E_i(m)` be that the sum on support `S_i` is less than integer threshold `m>=1`:
- `S0=214..218`;
- `S1={214,216,217,218,219,220,221}`;
- `S2={215,216,217,218,219,220,221}`;
- `S3=223..290`;
- `S4=296..312`.

Put `F_m(q)=R_m(q)/D(q)`, where `D(q)=product_{p=214}^{314}(1-q^p)` and `F_m` counts the union of these five failures. Let `z` be any primitive 41st root of unity. Then **for every integer m>=1**:

```
R_m(z)=0   if and only if   m mod 82 is in {0,78,79,80,81}.
```

In particular, for the strictly least period `M_m^(>=1)` of all positive-degree quasipolynomial coefficients, we obtain the exact 41-primary valuation classification

```
v_41(M_m^(>=1)) = 0  if m mod 82 in {0,78,79,80,81};
v_41(M_m^(>=1)) = 1  otherwise.
```

This settles the 41-order disappearance/return for *all positive thresholds*, not just 78..83. It explains the old counterexample `78≡119 (mod 41)`: the threshold dependence is instead exactly 82-periodic for this primitive-order-41 component.

## Proof of exact 82-periodicity in characteristic zero

Partition the first three overlapping events as follows: `a=a_214`, `b=a_215`, `c=a_216+a_217+a_218`, and `d=a_219+a_220+a_221`. The three event loads are `a+b+c`, `a+c+d` and `b+c+d`. Their minimum equals

```
c + a+b+d - max(a,b,d).
```

Let `A_m(q)` be the normalized numerator for the union of these first three failures on their eight-price support, `B_m(q)` for `S3`, and `C_m(q)` for `S4`. The supports of the three groups are pairwise disjoint. Thus the complete numerator factors by Boolean union:

```
R_m=A_m+B_m+C_m-A_m B_m-A_m C_m-B_m C_m+A_m B_m C_m.
```

At a primitive 41st root, `B_m(z)=0` for **all m**: its normalized numerator is a finite truncated complete-homogeneous sum multiplied by `product_{p=223}^{290}(1-z^p)`, which contains the zero factors for `p=246,287`. Therefore `R_m(z)=A_m(z)+C_m(z)-A_m(z)C_m(z)`.

We now derive a complete finite threshold recurrence for `A_m(z)`. Set `alpha=z^214`, `beta=z^215`, `gamma_j=z^j` (`j=219,220,221`), `K=product_{p=214}^{221}(1-z^p)`, and `H_c(t)=product_{p=216}^{218}(1-t z^p)^(-1)`. The three-price complete homogeneous polynomial for the `d` group has a partial-fraction decomposition

```
h_d(gamma_219,gamma_220,gamma_221) = sum_j kappa_j gamma_j^d,
kappa_j = gamma_j^2 / product_{k!=j}(gamma_j-gamma_k).
```

All denominators here are nonzero at a primitive 41st root. For the ordered variables `(a,b,d)`, sort descending with tie priority `a,b,d`. For each of the six permutations `pi=(top,middle,bottom)`, let `u1,u2,u3` be the corresponding weights drawn from `(alpha,beta,gamma_j)`. Put `e1=1` if `top` has lower tie priority than `middle` (else 0), and `e2=1` if `middle` has lower tie priority than `bottom` (else 0). The three nonnegative gap variables give the *exact* rational cone sum:

```
sum_{a,b,d in cone(pi)} alpha^a beta^b gamma_j^d t^(a+b+d-max(a,b,d))
= u1^e1 (u1*u2*t)^e2 /
  ((1-u1)*(1-u1*u2*t)*(1-u1*u2*u3*t^2)).
```

Since `sum_{m>=minload+1} t^m=t^(minload+1)/(1-t)`, the threshold series is

```
G_A(t)=sum_{m>=0} A_m(z)t^m
      = K*t/(1-t) * H_c(t) *
        sum_{j=219}^{221} kappa_j * sum_{pi in S_3}
          [u1^e1 (u1*u2*t)^e2 /
           ((1-u1)*(1-u1*u2*t)*(1-u1*u2*u3*t^2))].
```

Its possible t-poles (using `z` as the primitive generator) are:

```
1;
z^(-11),z^(-12),z^(-13)                 [c-group];
z^(-19),z^(-23),z^(-24),z^(-25),z^(-26) [top-pair];
+/-z^3, +/-z^4, +/-z^24                 [three-variable].
```

These are all distinct (the negative roots are outside the 41st roots, as 41 is odd). Consequently every pole is simple and is an 82nd root of unity. Each summand is proper in t (decays at infinity); therefore `G_A(t)=P(t)/(1-t^82)` for a polynomial `P` of degree less than 82. It follows coefficient by coefficient that

```
A_{m+82}(z)=A_m(z) for every m>=0.
```

Similarly, `G_C(t)=sum_{m>=0}C_m(z)t^m = t K_C / ((1-t)*product_{p=296}^{312}(1-t z^p))`; since 296..312 have distinct nonzero residues 9..25 mod41, all its t-poles are simple 41st roots. Thus `C_{m+41}(z)=C_m(z)` for all m>=0. Therefore **R_{m+82}(z)=R_m(z) for every m>=0**.

## Five zeros and the exact converse

In characteristic zero, the predecessor's exact cyclic-ring integer proof establishes `A_m(z)=0` for m=78,79,80,81,82. For C, the complement-residue argument independently gives its zeros. The 17 residues 9..25 are complemented to the full 41-residue set by 24 residues, including zero. Thus

```
product_{r=9}^{25}(1-t z^r)^(-1)
 = product_{r not in [9,25]}(1-t z^r)/(1-t^41).
```

The numerator has degree 24 and vanishes at t=1. Its complete homogeneous coefficients are zero for indices 25..40 and repeat modulo 41, and their one-period total sum is zero. It follows `C_m(z)=0` for `m mod41 in {0,25,26,...,40}`, including m=78..82. Hence `R_m(z)=0` at those five exact thresholds, and by proved periodicity on *all* their congruence classes mod82.

For every other residue m=1..77, use the accompanying independent `VERIFY_D41_MOD82.py`, which works exactly in F_821 with primitive 41st root `z=28`. It computes the same cone series for A and complete-homogeneous series for C, assembles `R=A+C-AC`, and prints all 82 residues. Its output has *exactly* five zero residues: 78..82. The other 77 modular residues are nonzero, hence their characteristic-zero values are nonzero. This supplies the converse without treating any finite-field zero as proof of integer/cyclotomic vanishing.

Evidence from the executed script:

```
p=821; z=28; z^41=1, z!=1; p prime
R mod 821 zero residues in [1,82] = [78,79,80,81,82]
77 other residues are nonzero
R_9 mod821=66; R_50 mod821=130 (both were coincidental zeros mod83)
R_83 mod821=320; R_119 mod821=527
sha256('m,R_mod821\\n' + 82 rows) =
407b860a6b6a0ea68c9716b0c6bd86ed2d66644ecfc7cbccbe49916f50b81da0
```

Finally, there are exactly two prices divisible by 41, namely 246 and 287; no multiple d>41 of 41 has two prices in [214,314]. Hence the only denominator root order carrying a 41-factor that can contribute to positive-degree quasipolynomial coefficients is d=41, and it has pole order exactly two before numerator cancellation. The root-of-unity/quasipolynomial correspondence yields the asserted exact 41-adic period valuation.

## Reproducibility, origin and remaining research

The analytic cone decomposition is new this run and valid at every primitive 41st root in characteristic zero; the full 82-residue nonzero witness was computed locally with Python's exact modular integer arithmetic. The five integer-cyclotomic zero cases are reused verbatim at their pinned source and are not relabeled an independent rerun. The modular algorithm is a characteristic-zero *nonzero witness*, not an upper-bound/zero certificate. Source may carry the separate `FINFIELD_RESULTS.txt` with the printed residue table.

This theorem classifies **only the 41-primary part** of `M_m^(>=1)`. The remaining prime-primary factors and complete all-threshold least coefficient period are still open. Next: test whether the same threshold generating-series/rational-pole method classifies other covering orders (e.g. 47,59,61,73) with reduced reliance on large finite threshold scans; retain exact source and observer map before making any native X6/BRC claim. Formal independent review remains `NOT_REVIEWED`.
