# R160 — Sharp minimum slope-support width for every finite Sturmian length

Date: 2026-11-15 (Asia/Shanghai). Scientific status: **AUTHOR_PROVED**, exact finite exhaustive checker for lengths 1–18, **NOT_REVIEWED**.

Continuity: R159 (immutable GitHub commit 014bc02903e83d7aad4b4bc18713afeee1c1ad96), R158 residue certificate (c96a9e24905566bba302ed82b45590f3c3812668). Frozen external S23 scalar observer scientific input pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. This mathematical result concerns an external one-dimensional slope parameter and does not claim a native X6 embedding, new BRC method, project Foundation admission, or formal Task claim.

## 1. Definitions and theorem

For a binary word $w=w_1\cdots w_m$, set $p_0=0$ and $p_j=\sum_{k=1}^{j}w_k$. Its *open admissible slope support* $I_w=(\alpha_w,\beta_w)\subseteq(0,1)$ is defined by existence of a real intercept $x$ such that all $m$ successive floor differences have the pattern $w$; equivalently

$$
\frac{q-1}{k}<\theta<\frac{q+1}{k}
$$

for every contiguous factor of length $k$ having $q$ ones, intersected with $(0,1)$. The word is admitted when this interval is nonempty.

**Theorem R160 (all lengths, sharp and unique).** For every integer $m\ge5$ and every admitted binary Sturmian word $w$ of length $m$,

$$
\boxed{\beta_w-\alpha_w\ge\frac{2}{m(m-2)}.}
$$

Equality holds **if and only if**

$$
\boxed{w=1\,0^{m-2}1 \quad\text{or}\quad w=0\,1^{m-2}0.}
$$

The exact exceptional small-length minima are: $m=1$: $1$ (two constant one-bit words); $m=2$: $1/2$ (00,11); $m=3$: $1/3$ (000,111); $m=4$: $1/4$ (0000,0110,1001,1111).

In particular, for $m\ge5$ the two extremal patterns of R157, R158 and R159 also uniquely **minimize** admissible slope-support width. This is a separate slope-geometry extremal result; it does not itself prove their unique maximization of eventual absence across all lengths.

## 2. Piecewise-affine range lemma

Define the affine prefix-discrepancy lines

$$
x_j(\theta)=p_j-j\theta,\quad 0\le j\le m,\qquad
R(\theta)=\max_j x_j(\theta)-\min_j x_j(\theta).
$$

The existence of a common intercept is precisely $R(\theta)<1$: each constraint requires a common point in the half-open unit intervals from the prefix discrepancies, and their intersection is nonempty exactly when their overall range is strictly less than one. Hence $I_w=\{\theta\in(0,1):R(\theta)<1\}$; $R$ is continuous, convex and piecewise affine. Every crossing of two distinct lines occurs at

$$
\theta=\frac{p_j-p_i}{j-i}\quad(i<j),
$$

a rational with denominator at most $m$ after reduction.

**Lemma.** If $w$ is nonconstant, the interior of $I_w$ contains at least one rational whose reduced denominator is at most $m$.

*Proof, interior endpoints.* Suppose $0<\alpha<\beta<1$. Continuity and maximality of the slope interval give $R(\alpha)=R(\beta)=1$, with $R<1$ between them. If no two prefix-discrepancy lines crossed in $(\alpha,\beta)$, the indices realizing their maximum and minimum could be held fixed there. Therefore $R$ would be affine across the entire interval. An affine function equal to one at both endpoints is identically one, a contradiction. An interior crossing has the required rational form.

*Proof, boundary endpoints.* If $\alpha=0$, continuity and $R(0)=p_m$ imply $p_m\le1$; nonconstancy then forces exactly one symbol 1. Write $w=0^a10^b$, $a+b=m-1$. All its lower slope constraints have numerator zero or less, while its upper bound is

$$
\beta=\min\{2/m,\;1/\max(a,b)\}\ge1/(m-1)>1/m
$$

(with $1/0=+\infty$). Thus $1/m$ lies strictly inside $I_w$. If $\beta=1$, bit-complement symmetry gives the analogous interior fraction $1-1/m$. This covers all cases. QED.

## 3. Sharp two-Farey-gap inequality

Let $\mathcal F_m$ be the increasing Farey fractions of order $m$. All endpoints $\alpha,\beta$ lie in $\mathcal F_m$: they are 0, 1, or the slope bound $(q\pm1)/k$ of a contiguous factor with $k\le m$. By the lemma, every nonconstant admitted word spans at least **two consecutive Farey cells**.

We now prove that for $m\ge5$ the combined width of any two consecutive cells of $\mathcal F_m$ is at least $2/[m(m-2)]$, with equality only at the two ends of the Farey order.

Write the three consecutive fractions as

$$
\frac ab<\frac pq<\frac cd,\qquad
pb-aq=1,\qquad cq-pd=1,
$$

with $b,q,d\le m$. Their total span is

$$
\delta=\frac1{bq}+\frac1{qd}.
$$

The two determinant identities imply $q\mid (b+d)$, since $p(b+d)=q(a+c)$ and $\gcd(p,q)=1$.

* If $q\le m-2$, then $\delta\ge 2/(mq)\ge 2/[m(m-2)]$. Equality would require $q=m-2$ and $b=d=m$. This conflicts with $q\mid(b+d)=2m$, equivalently $(m-2)\mid4$, and the necessary neighboring-fraction coprimality for $m\ge5$: the only candidate $m=6$ has $\gcd(4,6)>1$. Therefore equality cannot occur here.
* If $q=m$, both adjacent denominators are at most $m-1$. Since $0<b+d<2m$ and $m\mid(b+d)$, we have $b+d=m$. Thus $\delta=1/(bd)\ge4/m^2>2/[m(m-2)]$ for $m\ge5$.
* If $q=m-1$, divisibility and $b,d\le m$ show that $b+d=m-1$ or $b+d=2(m-1)$. In the first case, $\delta=1/(bd)\ge4/(m-1)^2>2/[m(m-2)]$. In the second, the only possible denominator pairs are $(m,m-2)$, $(m-1,m-1)$ and $(m-2,m)$. The middle pair is impossible, as consecutive reduced Farey fractions cannot share denominator $m-1>1$. The other pairs give $\delta=2/[m(m-2)]$.

In the equality cases, the determinant equations imply that the middle fraction is $1/(m-1)$ or $(m-2)/(m-1)$, and the outer endpoints are, respectively,

$$
(1/m,\;1/(m-2)),\qquad
((m-3)/(m-2),\;(m-1)/m).
$$

Any interval spanning more than the two needed Farey cells is strictly wider. The sharp lower bound follows for all nonconstant words. A constant word has support width $1/m>2/[m(m-2)]$ for $m\ge5$.

## 4. Equality words: forced by the factor inequalities

Suppose the support endpoints are exactly $(1/m,1/(m-2))$. Since the positive lower endpoint is attained by a factor of length $k\le m$,

$$
(q-1)/k=1/m
$$

forces $q=2$ and $k=m$, so the full word has exactly two ones. Likewise a factor achieving the upper endpoint obeys

$$
(q+1)/k=1/(m-2).
$$

As $m\ge5$ and $k\le m$, this forces $q=0$, $k=m-2$. Thus a contiguous run of $m-2$ zeros exists; the two remaining positions are ones, at the two ends. Therefore $w=10^{m-2}1$.

Conversely, this word has whole-word lower constraint $1/m$ and internal zero-run upper constraint $1/(m-2)$. Its proper factors have at most one one, and no factor inequality gives a stricter bound; the exact support is $(1/m,1/(m-2))$. Bit complementation gives the second word $01^{m-2}0$, with the complementary support endpoints. This completes the theorem. QED.

## 5. Reproducibility and coverage

Files adjacent to this note:

- R160_farey_min_gap_check.py — independent implementation scanning **every binary string** at every length 1 through 18, recomputing all factor slope inequalities with exact Fraction arithmetic.
- R160_farey_min_gap_verification.json — per-length admitted-word counts, rational minima, every minimizing word, and test status.

The checker covered 524,286 binary candidates and found 3,694 admitted words for lengths 1–18; all 14 tested lengths $m=5,\ldots,18$ matched the sharp theorem and its complete equality classification. These finite checks corroborate the symbolic all-length proof; they do not replace it. Independent mathematical review remains NOT_REVIEWED.

## 6. Next scientific frontier

1. Combine this all-length sharp *minimum* slope width with the R159 reversal relation $W_w+W_{w^R}=2/\Delta_w-m$ to obtain a joint bound on reciprocal widths. **Exact sharp reversal-pair theorem (R160B).** Combining R159B with the proved minimum gap yields

   $\boxed{\max_w(W_w+W_{w^R})=m(m-3),\qquad m\ge5.}$

   The only maximizers are the two endpoint-defect palindrome words $10^{m-2}1$ and $01^{m-2}0$, where each individual width is $m(m-3)/2$. This exact sum maximum does not by itself establish the individual maximum over all words.
2. Seek a sharp restriction on the reversal-odd skew $W_w-W_{w^R}$ or a positive combinatorial decomposition of the individual width. The open target is $\max_w\lfloor W_w\rfloor=(m-2)(m-1)/2-1=m(m-3)/2$ for all $m\ge5$, followed by the even-length modular improvement using the R158 residue certificates.
3. Continue the exact all-length saturation-threshold conjecture and the separate at-most-two signature-fiber conjecture, preserving source-word identity for any loss-sensitive BRC observer.

## 7. Control/source scope

Current work is an independent portable external scalar Sturmian observer under the preexisting scientific pin. The previous historical session EM-DIRECT-DAF2F3 is provenance, not the current run's execution identity. This paper creates no formal CLAIM, RR, review, native X6 or physics claim. Future Research Activity association requires a verified current own session, Source readback observations and proper role authority.
