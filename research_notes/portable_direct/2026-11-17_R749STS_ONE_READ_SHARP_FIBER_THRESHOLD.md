# R749STS — Exact one-read fiber transition and partial optimal initial-horizon classification

Date: 2026-11-17. Evidence: `AUTHOR_EXACT_NOT_REVIEWED`.
Frozen five-source science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Predecessors: R749STQ and R749STR in Draft PR #2653. This concerns the auxiliary scalar observer, not a native X6/Port/Cell observer map.

## Complete one-read collision theorem

With five labeled nonnegative integer source coordinates weighted `(1,1,2,3,6)`, let `C_n` count source tuples of weighted sum at most `n-1` and `T_n` sum the first weight-one coordinate on the same population. Define

```
S(n)=18n^4+54n^3-345n^2+2070n-16315,
Y_n(e,d)=n^3*(T_n+e)/(C_n+d)-S(n)/108.
```

For every positive integer `h`, compare candidates `q=73` and `p=73+6h`, allowing an independent legal pair `(e,d),(E,D) in [-2,2]^2` fixed through the observation sequence.

**Theorem:** One initial exact scalar observation has a collision for **each integer 1<=h<=129**, whereas one read strictly separates the two candidates for **every integer h>=130**. The transition `h=129/130` is exact across all legal real nuisance pairs.

Because `Y_n` is continuous, strictly increasing in `e`, and strictly decreasing in `d` throughout the legal square, its one-read image is the full interval

```
I_n=[Y_n(-2,2),Y_n(2,-2)].
```

For `q=73`, the exact endpoints are

```
I_73=[-182118587/38196630, 962852177/38196414].
```

For the competing congruent family, its upper endpoint `M(h)=Y_(73+6h)(2,-2)` is **strictly decreasing for every integer h>=0**. The two exact adjacent threshold comparisons are

```
M(129)-Y_73(-2,2)
  = 27717700477367/1508935762911405 > 0,

M(130)-Y_73(-2,2)
  = -623634232392236/114862724731769385 < 0.
```

Furthermore, `Y_(73+6h)(-2,2)<0<Y_73(2,-2)` for every integer `h>=1`. Therefore the intervals overlap exactly for `1<=h<=129`; at `h>=130`, the whole competing interval lies strictly below the minimum of `I_73`.

## Full proof certificate and universal scope

Set `n=73+6k`. The exact quasi-polynomial identities established in R749STQ are

```
C_n=(k+13)(k+14)(54k^3+2097k^2+27103k+116595)/30,
T_n=(k+12)(k+13)(k+14)(216k^3+8532k^2+112161k+490715)/120.
```

Substitute these into `Y_n`. The difference `M(k)-M(k+1)` simplifies **exactly** to

```
5*(1732752k^8+184006164k^7+8542361534k^6
+226444999671k^5+3748957127828k^4+39694178452821k^3
+262492905003386k^2+991221043798044k+1636468758218520)
/
[6*(2916k^10+398520k^9+24498315k^8+892050120k^7
+21306988888k^6+348825539820k^5+3964074682360k^4
+30876499536180k^3+157758462118321k^2
+477443583597060k+649938085092900)].
```

Every numerator and denominator coefficient is strictly positive, so `M(k)>M(k+1)` for all real `k>=0`. Separately, `-Y_(79+6k)(-2,2)` has strictly positive numerator and denominator polynomial coefficients for `k>=0`, proving that the full lower candidate interval stays negative. The companion SymPy exact checker generates both full coefficient arrays and performs exact integer-count crosschecks for the threshold. No finite cutoff of `h` is used in the theorem.

## Combined initial-horizon consequence

Combining this theorem with R749STR's exact **two-read** collision witnesses for `h=1,2` and universal two-read separator for `h>=3`, the following table is now proven for the fixed-base congruent comparison family:

| Gap h | One-read collision? | Two-read collision? | Minimum initial reads |
|---|---|---|---|
| 1,2 | Yes | Yes (exact rational witnesses) | At least 3 |
| 3 through 129 | Yes | No | **Exactly 2** |
| At least 130 | No | No | **Exactly 1** |

The `h=1,2` exact optimal counts beyond two observations remain open. The all-unknown-q global bound `5<=m_*<=11` is unaffected.

Companion `R749STS_ONE_READ_SHARP_THRESHOLD_CERT.py` uses exact Fraction integer counts, symbolic polynomials and coefficient sign checks; author execution on 2026-11-17: **PASS**. It generates complete `R749STS_ONE_READ_SHARP_THRESHOLD_RESULTS.json`. These are author-exact calculations pending independent proof review.

Next: determine exact minimal consecutive initial observations for `(73,79)` and `(73,85)`, and test whether a typed source/branch/future-operation preserving BRC Port/Cell readout realizes this auxiliary scalar discrimination.
