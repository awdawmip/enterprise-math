# R157 — Exact extremal Sturmian absence family and certified Farey-cell window through m=32

Date: 2026-11-15 Asia/Shanghai. Status: **AUTHOR_PROVED (symbolic family), EXACT_FINITE_ENUMERATION (m<=32), NOT_REVIEWED**. Scope: external scalar tied-phase S23 integer-phase Sturmian observer; no native X6/BRC embedding is asserted. Scientific input retained from the established R146–R156 chain: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

Dependencies: R146 integer open-cut formula; R152B first-period reduction (branch `f6890b08b640bd8b0abea5c789e440ff63446fb2`); R156B exact length-20 alias-fiber check (branch `483affb888b713e9bc18652e4968c129602906ac`). Current protocol: `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context` and `docs/PORTABLE_RESEARCH_PROTOCOL.md`.

## 1. Precise model

For a binary length-m word w with prefix sums p_j, its open slope support is the intersection of `0<theta<1` and

```text
(q-1)/k < theta < (q+1)/k
```

for every nonempty contiguous factor of length k with q ones. Write its two reduced endpoints `alpha=a/b<beta=c/d`, and define absolute prefix cuts

```text
U = b + min_{0<=j<=m} (b*p_j-a*j),
V = max_{0<=j<=m} (d*p_j-c*j).
C_w(L+1) = ceil((L*c-V)/d) - floor((L*a-U)/b) - 1,   L>=1.
```

Equivalently, C counts integers in the strict open interval `((La-U)/b,(Lc-V)/d)`. Define `T_w` as the least K>=2 for which C_w(K')>0 for all K'>=K. Global `T(m)=max_{|w|=m, admitted} T_w`.

## 2. R157A: exact all-n extremal family and *complete* absence set

**Theorem.** For every integer n>=2, the two different length-(n+2) words

```text
P_n = 0 1^n 0,       Q_n = 1 0^n 1
```

are finite Sturmian words. Their observer parameters are exactly

```text
                 alpha            beta           U     V
P_n              (n-1)/n          (n+1)/(n+2)     1     0
Q_n              1/(n+2)          1/n             n+2   n-1
```

and for every integer L>=1 their scalar counts are identical:

```text
C_{P_n}(L+1)=C_{Q_n}(L+1)
          = #{j in Z: L/(n+2)<j<(L+1)/n}
          = #{j>=1: n*j<=L<=(n+2)*j-1}.
```

Writing `h=ceil(n/2)`, the **entire** set of missing L>=1 is the following disjoint union of integer intervals:

```text
{1,...,n-1} union (union_{j=1}^{h-1} {(n+2)*j,...,n*(j+1)-1}).
```

Empty inner intervals are omitted. Its cardinality is `n*h - 1 - h*(h-1)`, its last member is `n*h-1`, and therefore

```text
T(P_n) = T(Q_n) = n*ceil(n/2)+1.
T(m) >= (m-2)*floor((m-1)/2)+1       for every m>=4.
```

This is a **general, proved lower bound** for the proposed global saturation formula. In particular it supplies an explicit missing mode at the last coefficient `K=T(m)-1` under that proposed formula, for every m>=5.

**Proof of support.** For P_n, a factor consisting entirely of ones has k<=n and contributes a lower bound at most `(n-1)/n`, attained by the length-n all-one block. A factor containing a zero has q<=k-1, so its lower bound is at most `(k-2)/k`, which is no greater than `(n-1)/n` for every possible such factor: a factor with one zero has k<=n+1, while the only factor with two zeros is the entire length-(n+2) word. The upper bound from a factor containing no zero or one zero is >=1; the only factor containing both zeros is the whole word and gives `(n+1)/(n+2)`. Thus P_n has the claimed endpoints. Direct substitution of its prefix sums `p_0=0`, `p_j=j-1` for `1<=j<=n+1`, `p_{n+2}=n` gives U=1,V=0.

For Q_n, complementary bits replace each slope theta with 1-theta. Consequently its endpoints are `1-(n+1)/(n+2)=1/(n+2)` and `1-(n-1)/n=1/n`; direct prefix sums `0,1,1,...,1,2` give U=n+2,V=n-1. Both supports are open and nonempty, proving admissibility.

**Proof of counts.** The integer interval for P_n is

```text
L-(L+1)/n < k < L-L/(n+2).
```

Apply integer change of variable `j=L-k`. For Q_n it is `L/(n+2)-1<k<(L+1)/n-1`, and apply `j=k+1`. Both yield the same open interval for j. Since j is integral, its inequalities are equivalent to `nj<=L<(n+2)j`.

For each j>=1 the covered coefficient integers form exactly `I_j=[nj,(n+2)j-1]∩Z`. Initially `1,...,n-1` are missing. Between `I_j` and `I_{j+1}`, the missing integer interval is `[(n+2)j,n(j+1)-1]`, and this interval is nonempty precisely for `2j<n`. With `h=ceil(n/2)` the gaps end at j=h-1, and the intervals I_h,I_{h+1},... touch or overlap because `2j>=n`. The final absent coefficient parameter is `L=nh-1`; hence T=nh+1. Summation of gap lengths gives the cardinality. QED.

## 3. R157B: complete, independently generated *finite* window m<=32

**Finite theorem.** For every `1<=m<=32`, (a) the exact maximum permanent-presence threshold agrees with the closed formula above for m>=5, and (b) at each `5<=m<=32` its **only two maximising words** are `0 1^(m-2) 0` and `1 0^(m-2) 1`. Moreover every observer fiber `w -> (alpha,beta,U,V)` has size at most two for the entire finite window. This is exhaustive finite evidence; the global upper bound and the all-length two-to-one claim are OPEN.

**Why the candidate enumeration is complete.** Every admitted word has the nonempty open slope support described in section 1; all its endpoint rational denominators are <=m because every defining inequality comes from a factor length k<=m. Partition (0,1) using the Farey fractions of order m. In each adjacent Farey gap choose its rational midpoint theta. Given any admitted word, at least one such midpoint belongs to its support. For that fixed theta, each word is encoded by a phase x via `w_j=floor((j+1)*theta+x)-floor(j*theta+x)`. Feasibility follows from the defining factor inequalities: `max_j(p_j-j*theta)-min_j(p_j-j*theta)<1` makes the intercept intersection nonempty. As x ranges over (0,1), these words change only at `x=(-j*theta) mod 1` for j=1..m, together with 0 and 1. One rational midpoint x in every open subinterval therefore enumerates every word possible at that theta. Taking the union across Farey cells is exhaustive for **all** admitted length-m words; duplicate words are discarded using exact tuples.

The checker `R157_check.py` uses Python `fractions.Fraction` and arbitrary-precision integer arithmetic only. It independently rebuilds all subfactor endpoints and U,V from every generated word, groups exact signature tuples, and for each signature scans `L=1,...,lcm(b,d)`. R152B gives `C(L+P+1)=C(L+1)+P(beta-alpha)` with a positive integer increment; thus the last zero is always in that first period. The script asserts (a) the global maximum, (b) precisely the two exhibited maximisers, and (c) maximum fiber cardinality <=2 at every tested length. There is no floating-point comparison.

Independent cross-check: a separate **direct enumeration of all 2^m binary strings**, filtered through the same exact signature definition, matches the Farey-generated word *sets* for every m=1..11; the length-20 counts `944 admissible / 868 signatures / 76 two-word fibers` also match previously committed R156B's different all-binary enumeration. For n=2..100, an independent j-interval test checks both extreme-family signatures, exact counts, last absence, and subsequent positive coefficients.

Selected exact outputs:

| m | admitted words | signatures | two-word fibers | T(m) | maximisers |
|---:|---:|---:|---:|---:|---|
| 20 | 944 | 868 | 76 | 163 | P_18,Q_18 |
| 24 | 1586 | 1456 | 130 | 243 | P_22,Q_22 |
| 28 | 2470 | 2246 | 224 | 339 | P_26,Q_26 |
| 30 | 3018 | 2754 | 264 | 393 | P_28,Q_28 |
| 32 | 3650 | 3358 | 292 | 451 | P_30,Q_30 |

Across all 32 lengths: 31,980 admitted words and 29,326 distinct signatures; every fiber size <=2. Exact per-length results and maximum-word identities are in `R157_verification.json`.

## 4. Status and next scientific questions

* R157A is a symbolic all-n theorem, with independently corroborated finite samples; **author-proved, not independently reviewed**.
* R157B is an exact finite theorem through m=32, with an explicit completeness proof and executable checker; **author-verified, not independently reviewed**.
* **OPEN:** prove for every m>=5 the matching universal upper bound `T(m)<=(m-2)*floor((m-1)/2)+1`; a useful route is to exploit the Farey endpoints and sharp intercept-cut constraints to rule out later absences.
* **OPEN:** prove the two-to-one signature bound for arbitrary m or construct a first longer triple collision; the present observations hold through m=32.
* Scalar observer coincidences do not identify the two original words. Preserve the word/source coordinate for any operation demanding that identity, consistent with the project's joint-observer preservation constraint.

Control provenance: exact S23 publication-directory lookup at Source `6b55443121d597e14540ce1b96cc5d63703be16c` returned `NO_CANONICAL_PUBLICATION_DIRECTORY` on 2026-11-15 02:01:55 +0800. This independent authored contribution asserts no formal TASK CLAIM/Result/Review. Historical own session `MCP-fa6cae44b88546f9a2079bdd4adcad23` is metadata only; current execution authority was not established. GitHub branch publication and activity checkpoint are separate operations.
