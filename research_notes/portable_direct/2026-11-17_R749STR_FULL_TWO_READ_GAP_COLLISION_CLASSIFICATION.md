# R749STR — Complete two-initial-read classification for the fixed-base six-step family

Date: 2026-11-17 · Mathematical status: `AUTHOR_EXACT_NOT_REVIEWED`.
Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Predecessors: R749STP (73/265, initial two reads) and R749STQ (all-gap difference-of-reads separator), Draft PR #2653. This is a **labeled five-source auxiliary scalar observer**, not a native X6/Port/Cell equivalence. No shared Task CLAIM is asserted.

## Exact setting and theorem

For five distinct labeled nonnegative integer source coordinates with weights `(1,1,2,3,6)`, let `C_n` count weighted sums at most `n-1` and `T_n` sum the first weight-one coordinate over that population. Define

```
S(n)=18n^4+54n^3-345n^2+2070n-16315
Y_n(e,d)=n^3*(T_n+e)/(C_n+d)-S(n)/108.
```

For every integer `h>=1`, compare candidate `q=73` with `p=73+6h`. Each candidate has an independent pair of nuisance parameters, `(e,d),(E,D) in [-2,2]^2`, constant across consecutive observations `j=0,1`.

**Theorem (complete first-two-read collision/noncollision classification).**

1. For `h=1` and `h=2`, there are explicit **legal rational** nuisance quadruples with **both** initial scalar reads identical:
   ```
   h=1, p=79:
     E=-2/5, D=19/10,
     e=-251839066287820157213308556/126987724119296300884285527,
     d=156633484697374856671338713/84658482746197533922857018.

   h=2, p=85:
     E=7/5, D=2,
     e=-3017722237060578733161/1527694442423074582592,
     d=1445925897017416432877/763847221211537291296.
   ```
   In each case, `Y_73(e,d)=Y_p(E,D)` and `Y_79(e,d)=Y_(p+6)(E,D)` exactly.
2. For **every integer h>=3 and every allowed real nuisance quadruple**, define the nontrivial two-read linear separator
   ```
   L_n(e,d) = Y_n(e,d) - (21/20)*Y_(n+6)(e,d).
   ```
   Then the **sharp attained uniform separation** is
   ```
   L_73(e,d) - L_(73+6h)(E,D)
       >= delta
       = 148157200542443986379/5091802077550505078161
       > 0.
   ```
   Equality holds at `h=3, (e,d,E,D)=(-2,2,2,2)`. Thus initial two readings separate the candidates for all `h>=3`.
3. For all `h>=3`, if each of the four scalar readings is independently perturbed by any additive error of magnitude at most `eta`, the separator remains strictly positive when
   ```
   0<=eta<delta / [2*(1+21/20)]
       = 1481572005424439863790/208763885179570708204601
       ≈ 0.007096878869398547.
   ```

Quantifiers: the two legal nuisance pairs are fixed *within* each two-read sequence, while all real values in the four-dimensional cube are allowed. No probability assumptions.

## Constructive proof for h=1,2

For any given right-side candidate `p` and legal rational `E,D`, put `y_i=Y_(p+6i)(E,D)` for `i=0,1` and

```
x_i = [y_i + S(73+6i)/108] / (73+6i)^3,
v_i = C_(73+6i) * x_i - T_(73+6i).
d = (v_0-v_1)/(x_1-x_0),
e = v_0 + x_0*d.
```

For the two supplied rational choices, exact arithmetic establishes `x_0!=x_1`, each of the resulting `e,d` lies strictly between `-2` and `2`, and both desired observation equalities hold identically. The attached executable certificate calculates and checks those identities using Python `fractions.Fraction` from independently regenerated five-source integer counts.

## Uniform sharp-separation proof for all h>=3

**The q=73 minimum.** For `L_73(e,d)`, differentiation and interval-wise bounds on the separate positive terms give

```
partial_e L_73 >=
73^3/(C_73+2) - (21/20)*79^3/(C_79-2)
= 123909199877/2888630046580 > 0,

-partial_d L_73 >=
73^3*(T_73-2)/(C_73+2)^2
  - (21/20)*79^3*(T_79+2)/(C_79-2)^2
= 17230872095203588080407/521511471625298310606025 > 0.
```

Thus the attained minimum is `L_73(-2,2)=33210791290663/51995544553800`.

**All larger-gap maxima.** Write `h=3+t`, `t>=0`, `n=73+6h`, and represent the full legal nuisance square by `E=2-4u`, `D=-2+4v` with `u,v in [0,1]`. R749STQ established the exact six-phase counting polynomials (for `k=h`):

```
C_(73+6k)=(k+13)(k+14)(54k^3+2097k^2+27103k+116595)/30
T_(73+6k)=(k+12)(k+13)(k+14)(216k^3+8532k^2+112161k+490715)/120.
```

Set `U=L_91(2,2)=1740831760941127/2855570604280200`. Both `C_n+D` and `C_(n+6)+D` are positive. Consider the exact polynomial

```
P(t,u,v)=(U + [S(n)-(21/20)S(n+6)]/108)
          *(C_n+D)*(C_(n+6)+D)
        - n^3*(T_n+E)*(C_(n+6)+D)
        + (21/20)*(n+6)^3*(T_(n+6)+E)*(C_n+D).
```

It equals `[U-L_n(E,D)]*(C_n+D)*(C_(n+6)+D)`; it is polynomial of degree 10 in `t`, at most 1 in `u` and at most 2 in `v`.

Expand `P` in the tensor Bernstein basis of degree `(1,2)` in `u,v`. Each of its six coefficient polynomials in `t` has degree 10 and **all 66 monomial coefficients are nonnegative**: **65 strictly positive and one zero**, the constant term at `u=0,v=1`. Therefore `P>=0` on `t>=0, u,v in [0,1]`, with equality only `t=0,u=0,v=1`, that is `h=3,E=2,D=2`. The exact SymPy verification constructs all coefficients from the displayed formula; its JSON output includes the entire set (six arrays, 11 coefficients each).

Consequently

```
L_(73+6h)(E,D) <= L_91(2,2)
```

for every integer `h>=3` and legal nuisance pair. Subtracting yields the exact attained uniform gap

```
delta=L_73(-2,2)-L_91(2,2)
=148157200542443986379/5091802077550505078161>0.
```

The coefficient norm of the four-read difference is `1+21/20+1+21/20=41/10`, proving the noise tolerance.

## Reproducibility and research frontier

Companion Python/SymPy code `R749STR_FULL_TWO_READ_GAP_CLASSIFICATION_CERT.py` constructs the original five-source integer counts, the two exact rational collision witnesses, both q=73 derivative bounds and all six Bernstein polynomials. A complete JSON results file is produced by the checker. Author execution on 2026-11-17: **PASS**. Evidence: exact rational/symbolic author check, awaiting independent proof review.

This fully classifies simultaneous collision at the first two reads for the fixed base `q=73` and all positive **congruent** gaps `p-q=6h`. It does not classify one-read minimality for `h>=3` or the unknown-q global horizon `5<=m_*<=11`. A next useful unit is the exact one-read overlap transition for this infinite family, then a typed source/provenance/future-operation preserving BRC Port/Cell observer lift.
