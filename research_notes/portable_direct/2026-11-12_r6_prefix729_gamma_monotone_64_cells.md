# PREFIX-729-R6 — Exact monotone Gamma subbox certificate covering 64 whole grid cells

Date: 2026-11-12 (Asia/Shanghai).
Parent mathematical objective: PREFIX-675.
Previously checked frontier: PREFIX-728.
Scientific input **unchanged**: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Evidence grade: **AUTHOR_EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem

Use the same frozen 189-row BRC stopping observer and two independent conditional unit-rate Gamma completion clocks of PREFIX-726. Write
\(\mu(p,z)=E[\max(T_p,T_z)]\), \(M_2(p,z)=E[\max(T_p,T_z)^2]\), \(W=M_2-\mu^2\), and \(V_q=q^2W-q\mu\).
Let \(e=(0,73/500)\). For every real \(q\ge2\) and **every** \((p,z)\) in the closed square

\[
\mathcal R=[5/48,1/8]\times[5/48,1/8],
\]

the following strict inequality holds:

\[
\boxed{V_q(e)-V_q(p,z)>100q^2}.
\]

The square exactly comprises the 64 complete cells whose 384-grid indices are \((i,j)\in[40,48)\times[40,48)\). This is a fresh independent certificate of all 64 cells; a duplicate-free increase over PREFIX-718's 139,018-cell union is **not yet claimed**, pending its historical membership mask.

## Derivation: two monotone moments replace loose derivative bounds

Let \(w_{n,k}\) be the frozen number of surviving branches at depth \(n\) and weight \(k\). The exact integer reconstruction gives \(\sum_{n<189}\#\{k:w_{n,k}\ne0\}=9,529\) and extinction at row 189.
For every \(n<189\), the normalized Bernstein coefficients \(b_{n,k}=w_{n,k}/\binom nk\) are in \([0,1]\), symmetric under \(k\leftrightarrow n-k\), and nondecreasing for \(k<n/2\). All properties were checked by exact integer cross multiplication. Paired Bernstein derivative terms imply \(s_n(x)=\sum_k w_{n,k}x^k(1-x)^{n-k}\) is nondecreasing on \(0\le x\le1/2\).

Conditional Gamma-clock survival is

\[
P(T_x>u)=e^{-u}\sum_{n=0}^{188}s_n(x)\frac{u^n}{n!}.
\]

Thus \(T_x\) is stochastically increasing in \(x\), and the maximum of the independent clocks has coordinatewise nondecreasing \(\mu\) **and** \(M_2\). On any closed subrectangle with coordinatewise lower corner \(\ell\) and upper corner \(h\), for \(t\in[0,1/2]\),

\[
f_t(e)-f_t(p,z)\ge
W(e)-M_2(h)+\mu(\ell)^2-t\bigl(\mu(e)-\mu(\ell)\bigr),
\qquad f_t=W-t\mu.
\]

The right-hand side is affine in \(t\). Checking its endpoints \(t=0,1/2\) proves the bound for the entire real continuum.

## Exact finite certificate

Partition each coordinate interval into 16 equal parts of width \(1/768\), giving 256 **closed** subrectangles (boundaries overlap harmlessly).
Use the exact Gamma kernel from \`PREFIX726_R6_GAMMA_WITNESS_LIPSCHITZ.py\`:
\(c_{nm}=\binom{n+m}{n}/2^{n+m+1}\). The companion Python program computes both moments at the 152 symmetry-reduced rational mesh vertex pairs using arbitrary-precision integer sums. It checks the frozen 189 rows and all monotonicity inequalities.

For every nonnegative rational \(x\), with integer scaling \(S=10^6\), the integer floor \(\lfloor Sx\rfloor\) rigorously encloses \(x\) between its floor/S and (floor+1)/S. Apply downward bounds to \(W(e)\), \(\mu(\ell)^2\), and upward bounds to \(M_2(h)\), \(\mu(e)\). On every one of 256 subrectangles the minimum (over both endpoints in \(t\)) of the **integer-rounded lower certificate** has common denominator \(2S^2\).
Its smallest integer numerator is

\[
\boxed{210867495694150}
\]

at lower mesh index \((80,95)\), so the lower certificate is \(105.433747847075>100\). This is a directed-rounding rational lower bound, not a floating-point estimate.

The program passed \`ALL_CHECKS_PASS PREFIX729-R6\` locally. Its output JSON records the full exact minimum numerator, mesh, surviving cell count, witness floors and reproducible bounds. The comparison is uniform in every real \(q\ge2\); there is no extrapolation from sampled \(q\).

## Why this route advances the mother objective

PREFIX-728 controlled an L1 diamond of radius \(1/975\) but had zero fully covered grid cells. Direct two-moment monotone subboxes certify an \(8\times8\) whole-cell square without requiring a global variance-gradient bound, producing a quantitative \(100q^2\) improvement witness.

This region is within the external 2-parameter Gamma auxiliary observation domain; it is not a proof of a native P000 spatial embedding. The original 139,018/147,456 aggregate is retained until precise overlap reconciliation.

## Reproduce and next question

Run \`python PREFIX729_R6_MONOTONE_SUBBOX.py\` in the same directory as the pinned \`PREFIX726_R6_GAMMA_WITNESS_LIPSCHITZ.py\`. The script imports its exact kernel, uses integer arithmetic for all acceptance decisions, and writes \`PREFIX729_R6_RESULTS.json\`.

Next: retrieve the exact PREFIX-712/714/716/718 certified cell membership (not merely total counts), intersect with the 64-cell square, and update the **deduplicated** union. Then attempt adaptive larger subboxes for additional whole cells. Preserve the frozen science pin and distinguish author certificates from independent review.
