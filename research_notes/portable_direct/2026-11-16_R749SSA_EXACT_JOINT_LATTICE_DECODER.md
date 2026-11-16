# R749SSA — exact mixed integer-error feasibility and the first global two-budget table

**Date:** 2026-11-16 (Asia/Shanghai). **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen scientific pin:** \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Continuation of R749SRZ (same research branch / Draft PR #2546) and R749SRY (Draft PR #2543).

## Question and fixed model

Retain the five *labeled* positive integer source weights \`(1,1,2,3,6)\`, with first weight-one source marked. The exact combinatorial counts are
\[
C_q=\#\{k\in\mathbb Z_{\ge0}^5:\sum w_i k_i\le q-1\},\quad
T_q=\sum_{\sum w_i k_i\le q-1} k_1.
\]
Use the exact smooth part \(H_4(q)=1/6+1/(2q)-115/(36q^2)+115/(6q^3)-16315/(108q^4)\), the ideal six-phase cycle \(P=(455,-295,-25,185,-25,-295)/36\), and the three offsets \(J=(0,1,5)\). For each sampled \(q=r+h\), the observation under independent integer count errors \(e,d\) is
\[
Y_q(e,d)=\frac{q^3(T_q+e)}{C_q+d}-q^4H_4(q),\quad
|e|\le M,\ |d|\le K,\ C_q+d>0.
\]
The decoder chooses the unique minimum-\(\ell_\infty\)-distance phase signature \(S_a=(P_a,P_{a+1},P_{a+5})\), with a tie counted as failure. Define the global recovery threshold \(N(M,K)\) as the smallest integer \(N\ge1\) for which the decoder is correct at every \(r\ge N\) under every permitted independent error pair.

R749SRZ established a two-budget asymptotic and the special \(M=0,K=0,\ldots,4\) thresholds. The new question is whether existence of an adversarial *joint* integer-error vector can be tested without enumerating \(((2M+1)(2K+1))^3\) vectors.

## Theorem A — complete extremal-coordinate and integer-interval criterion

For arbitrary \(k\) independent observation coordinates of the above positive-denominator rational form, any two real signatures \(S_a,S_b\), and any integer budgets \(M,K\ge0\), the existence of an integer vector of paired count errors making rival \(b\ne a\) tie or beat \(a\) is equivalent to one of at most \(2k\) extremal-coordinate cases passing \(k-1\) independent exact integer-interval feasibility checks.

**Step 1 (global scalar range endpoints).** At a given sampled integer \(q\), set \(c=C_q>0,t=T_q\ge0,d_{\min}=\max(-K,1-c)\). The minimum possible scalar observation is reached at
\[
e=-M,\quad d=\begin{cases}K,&t-M\ge0,\\d_{\min},&t-M<0;\end{cases}
\]
the maximum is reached at
\[
e=+M,\quad d=\begin{cases}d_{\min},&t+M\ge0,\\K,&t+M<0.\end{cases}
\]
These are **integers in the original allowed set**, not continuous relaxations. For each fixed positive denominator the observation is increasing in \(e\); when \(e\) is fixed, it is monotone in \(d\), with derivative sign opposite to \(t+e\).

**Step 2 (why one global endpoint suffices).** Let a failing vector have true distance \(u=\max_i|Y_i-S_{a,i}|\), and choose an index \(j\) attaining that maximum. Write \(Y_j-S_{a,j}=\sigma u\), \(\sigma\in\{-1,+1\}\). Rival \(b\) ties/beats precisely when
\[
|Y_i-S_{b,i}|\le u\quad\text{for every }i.
\]
At \(j\), this is equivalent to \(0\le\sigma(S_{b,j}-S_{a,j})\le 2u\). Replace only its paired count errors with the **attainable** scalar minimum if \(\sigma=-1\), or scalar maximum if \(\sigma=+1\). This moves the \(j\)-coordinate farther in the same direction, changing \(u\) to \(u'\ge u\). It keeps the rival coordinate within \(u'\); the untouched coordinates are within the earlier \(u\). Thus a failing vector always has one coordinate at one of its two global extrema.

**Step 3 (exact integer feasibility for other coordinates).** After fixing that extremal coordinate \(j\), let \(u=|Y_j-S_{a,j}|\), reject the case if \(|Y_j-S_{b,j}|>u\). For each \(i\ne j\), the admissible observation interval satisfying both distance bounds is
\[
L_i=\max(S_{a,i}-u,S_{b,i}-u),\qquad
U_i=\min(S_{a,i}+u,S_{b,i}+u).
\]
For each candidate integer denominator error
\[
d\in[\max(-K,1-C_q),K]\cap\mathbb Z,
\]
the exact equivalent numerator error interval is
\[
e_{\rm lo}=\max\!\left(-M,\left\lceil (L_i+q^4H_4(q))(C_q+d)/q^3-T_q\right\rceil\right),
\]
\[
e_{\rm hi}=\min\!\left(M,\left\lfloor (U_i+q^4H_4(q))(C_q+d)/q^3-T_q\right\rfloor\right).
\]
This coordinate can be satisfied iff some denominator candidate has \(e_{\rm lo}\le e_{\rm hi}\). Coordinates are independent, so all must pass; the constructed vector is then an exact adversarial witness. Conversely Steps 1 and 2 guarantee that every possible failure appears in an extremal case. This proves the equivalence. QED.

The criterion takes at most \(2k(k-1)(2K+1)\) rational interval tests per competing signature, plus \(2k\) anchor tests: \(O(k^2(K+1))\), independent of the numerical magnitude of \(M\) except arithmetic bit length. It includes cases with \(M>T_q\), when a perturbed numerator may be negative.

## Theorem B — all nine exact global recovery thresholds for small paired budgets

The following are the *minimal global integer thresholds*, for every \(r\ge N(M,K)\) and all allowed errors:

| Denominator budget \(K\) / numerator budget \(M\) | \(M=0\) | \(M=1\) | \(M=2\) |
|---|---:|---:|---:|
| \(K=0\) | **35** | **53** | **65** |
| \(K=1\) | **261** | **267** | **273** |
| \(K=2\) | **507** | **513** | **513** |

**Finite part.** For each of nine \((M,K)\) pairs the executable Python \`Fraction\` checker applies Theorem A at all cutoffs \(1\le r<1350\), a total of 12,141 cutoff/budget evaluations. The last failing cutoff for each is \(N(M,K)-1\), and the corresponding exact integer numerator and denominator witnesses are recorded in the JSON. It crosschecks 96 independently enumerated complete four-budget error cubes: \(1\le r\le24\), \(M,K\in\{0,1\}\).

**Infinite part.** Predecessor R749SRY proved \(0<R(r)-P_{r\bmod6}<1600/r\) for \(r\ge516\), and \(C_r\ge r^5/4320\). The exact generating function also yields \(T_r/C_r<r/6+1\) at \(r\ge1350\). Therefore, for \(r\ge1350\), \(M,K\le2\),
\[
\|Y-S_{r\bmod6}\|_\infty
<
\frac{1600}{r}
+\frac{(4320/r^2)\,[M+K(r/6+1)]}{1-4320K/r^5}
\le
\frac{63374339249936}{28025208984321}
<\frac{15}{4}.
\]
The six ideal signatures have minimum \(\ell_\infty\) separation \(15/2\), so no rival can tie the true signature on the entire infinite tail. Combining this with exact finite testing proves the nine thresholds for *all* positive integer cutoffs. QED.

## Reproduction, limits and next research

Run from the artifact directory:
\`python3 R749SSA_JOINT_LATTICE_CERT.py > R749SSA_JOINT_LATTICE_RESULTS.json\`

The R749SSA file imports \`R749SRZ_JOINT_COUNT_ERROR_CERT.py\` in the same directory for the unchanged frozen source model. No third-party Python modules are needed. The recorded result is \`PASS\`. The author has verified exact rational computations, witness completeness and the finite-plus-tail argument; external independent mathematical review remains open (\`AUTHOR_EXACT_NOT_REVIEWED\`).

This is an explicitly typed *auxiliary positive labeled-source observer* with preserved model and allowed future operation; no extra native spatial axis, time identification or signed BRC/Heartbeat morphism is inferred. Next: remove the linear dependence on \(K\) via floor sums or polyhedral integer feasibility; determine residue-dependent additive corrections to the two-budget asymptotic; test a source-label and signed-port preserving interface to BRC using its actual admissible operations.
