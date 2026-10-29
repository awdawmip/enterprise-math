# D25/LIFT GH-104 and GH-105 — Alternating discriminant and an exact A5 Hasse-moment cover

2026-10-29 Asia/Hong_Kong · TASK_RESEARCH / author portable evidence · logical Research lane `chatgpt-research-hourly-enterprise-math-20260923`.

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION · D25/LIFT/JT2 OPEN. Exact task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Source and scope

Let `p=8m+3≥11` be prime; set `k=F_p`, `d=2m`, `N=(p−1)/2=4m+1`. Reuse the exact GH-102 Hasse finite-log moment theorem: there is a monic degree-m `G=z^m E(1−z^(-1))`, with `E(T²)=P_(2m)(T)`, for which `M(0)=0`, `deg M=N`, `lc(M)=2`, and

```text
M'(z) = −z^(2m) G(z)^2.
```

GH-100 defines the cubic Hasse provenance of E; GH-101–GH-103 define M. The GH-16 reflected source, its tail R, the original GH-3 truncation T_(p,9), and GH-83 Laurent residual remain distinct.

## GH-104 — exact discriminant-square theorem

Put `Q(z)=z^m G(z)` (monic, degree 2m), `F_t(z)=M(z)−t`, and define the monic degree-m critical-value polynomial

```text
K_p(t) = Res_z(G(z), t−M(z)) = ∏_(G(α)=0) (t−M(α))
```

(over the algebraic closure, preserving root multiplicities). Then **as a polynomial identity over F_p[t]**,

```text
Disc_z(M(z)−t) = −(1/2) t^(2m) K_p(t)^2.
```

Since `p ≡ 3 (mod 8)`, `(−2/p)=1`, so `−1/2` is a square in F_p. Therefore the arithmetic **and** geometric Galois groups of the generic degree-N polynomial `M(z)−t` are transitive subgroups of `A_N`, not just `S_N`.

**Proof.** The derivative relation gives `F_t' = −Q²`. The resultant is multiplicative in its second argument:

```text
Res(F_t,F_t') = (−1)^N Res(F_t,Q)^2 = −Res(F_t,Q)^2
```

because N is odd. The discriminant convention is `Disc(F)=(-1)^(N(N−1)/2)lc(F)^(-1)Res(F,F')`; here `N(N−1)/2=2m(4m+1)` is even and `lc(F_t)=2`. As `deg Q=2m` is even,

```text
Res(F_t,Q) = Res(Q,F_t) = (−t)^m ∏_(G(α)=0)(M(α)−t)
            = t^m K_p(t).
```

This yields the formula, including repeated critical values. The discriminant is nonzero over k(t), because `M'` is nonzero and transcendental t cannot equal a critical value algebraic over k. The generic polynomial `M(z)−t` is irreducible over k(t): `t−M(z)` is irreducible in k[z,t] (linear in t) and remains irreducible by Gauss's lemma. Quadratic reciprocity gives `(−1/p)=−1` and `(2/p)=−1`, hence `(−1/2/p)=+1`. A square discriminant places both permutation Galois groups in the alternating group. QED.

**BRC scope:** K retains unordered critical values (with multiplicity), but loses the map from a value back to its critical point and the sign of G. Preserve the full Hasse chart, original/reflected source tags and order of derivative/resultant/evaluation. No native X6 or original GH-3 theorem is inferred from an auxiliary classical chart.

## GH-105 — exact A5 specialization at p=11

For p=11, m=1, d=2, N=5,

```text
P_2(T)=(3T²−1)/2; E(y)=(3y−1)/2; G(z)=z+4
M(z)=2z^5+9z^4+2z^3; M'(z)=−z²(z+4)²  (mod 11)
M(z)=2z³(z²−z+1)
M(z)−7=2(z+4)³(z²−2z−1).
```

The two finite branch points are z=0 and z=7, with values 0 and 7 and ramification index 3. Infinity has index 5. Thus

```text
Disc_z(M(z)−t)=5t²(t−7)²  in F_11[t].
Gal(M(z)−t / F_11(t)) = Gal(M(z)−t / Fbar_11(t)) = A5.
```

**Proof of group assertion.** The generic cover is transitive/irreducible. All ramification is tame (the characteristic 11 does not divide |S5|). Finite index-3 ramification supplies a 3-cycle in geometric inertia. Transitivity of degree five implies the geometric group order is divisible by 5. GH-104 embeds it in A5. Its order must divide 60 and be divisible by 15, hence is 15, 30 or 60. An order-15 subgroup would be C15 (normal Sylow-5, trivial C3 action on Aut(C5)=C4), impossible in A5. An order-30 subgroup would be normal of index 2, impossible as A5 is simple. Hence geometric group is A5; arithmetic contains it and lies within A5, so equals A5. QED.

## Evidence, scope and continuation

Exact standalone Python standard-library check: `research_notes/portable_direct/d25_gh104_alternating_monodromy_check.py`. It constructs Legendre P_d by recurrence, independently reconstructs G and M from the GH-102 derivative, then compares two independent Sylvester-matrix resultants for each t in {0,…,6}, at the ten primes 11,19,43,59,67,83,107,131,139,163. All **70 exact specializations PASS**. The proof, not the finite check, establishes the all-prime identity. At p=11, direct factorization supplies the exact A5 assertion. No native Enterprise Math experiment performed.

**New discriminating next action:** seek an independent CM/Jacobi evaluation of K_p(t), and determine whether its critical-value data yields a noncircular criterion for the contact `C_p^*(9)−3M_p(9)=0`; note that `M'_(3347)(9)=2166≠0`, so a discriminant square by itself does not explain the 3347 reflected-tail anomaly. Preserve original GH-92 `T_(p,9)=0 (mod p)` as a separate target; retain GH-83, GH-20/GH-21, and native p=373 obligations. No CLAIM, OPEN, formal checkpoint, Result, independent review or mathematical admission is represented by this author publication.
