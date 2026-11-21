# EC49FVR — Adaptive two-scale 46-layer 11-adic rational-phase certificate mesh

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_PERIOD_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.

**Frozen science:** BRC16943, unchanged. Parent: `awdawmip/enterprise-math@4bc0d713421384f7590aeeb6424472fe42e5dd3e:research_notes/portable_direct/EC49FVQ_FORTY_SIX_DENOMINATOR_MESH_THEOREM.md`. The 46-layer menu and the Bernoulli phase/projective no-root reduction are inherited *verbatim*. This note improves the numerical covering theorem using only the extra denominators accessible at the actual height \(H\). It is independent portable research, not a formal shared Task CLAIM or a Heartbeat X6 native Result.

## Statement

Let \(S_H\) be the reduced fractions \(h/d\in(0,1)\) with \(d\le H\) for which the inherited **complete projective mod-11 no-root certificate** holds, so \(t(x)\ne h/d\) for every rational Bernoulli detection width \(x\in(0,1)\) in the parent model.

**Adaptive two-scale mesh theorem.** For every integer \(H\ge256\) and every real interval \(I\subseteq[0,1]\),

\[
\boxed{|I|>\frac{490}{143H}\quad\Longrightarrow\quad I\cap S_H\ne\varnothing.}
\]

The coefficient \(490/143=3.42657342657\ldots\) is a **26.6012% improvement** on the parent \(1760/377=4.66843501326\ldots\); it is an upper bound, not a global optimum for \(S_H\).

More specifically, put \(j=\lfloor\log_2 H\rfloor\), \(k=2^j\) and \(\rho=H/k\in[1,2)\). For the *fixed parent menu* \(\mathcal D=\{(r,e)\}\) of 46 pairs define \(T_j(H)\subseteq S_H\) to consist of all certified reduced fractions with denominators

\[
d_{\ell,r,e}=r2^{j+\ell-e}\le H,\qquad \ell\in\{0,1\},\ (r,e)\in\mathcal D.
\]

The worst value of \(\rho\) times the periodic maximum gap in units of \(1/k\), over all \(\rho\in[1,2)\) and all 20 exponent classes, is at most \(490/143\). The exact *supremum of these stagewise bounds* is

\[
\begin{array}{c|c|c|c}
j\text{ parity}&\sup \rho\cdot(k\,\mathrm{gap})&
k\,\mathrm{gap}\text{ just below critical }\rho&
\text{critical }\rho\\\hline
\text{even}&490/143&280/143&7/4\\
\text{odd}&10465/3294&3680/1647&91/64
\end{array}
\]

The first value dominates. Equality in the supremum is a limiting stage bound as \(\rho\) approaches a cutoff from below; no claim that any single finite \(H\) attains it.

## Explicit source menu and complete finite certificate

The inherited 46 pairs are the following 18 pairs, plus the 6 \((3,e)\) for \(2\le e\le7\), plus all \((r,e)\) with \(r\in\{47,11,23,53,27,31,29,61\}\) and \(\lceil\log_2r\rceil\le e\le7\):

```text
(1,0),(7,3),(13,4),(1,1),(1,2),(1,3),(1,4),(7,4),
(13,5),(7,5),(1,5),(1,6),(7,6),(13,6),(1,7),
(7,7),(13,7),(91,7)
```

Let \(L=\operatorname{lcm}\{r:(r,e)\in\mathcal D\}=84915883381329\), \(C=2L\), and use the **exact integer observer coordinate**

\[
y=Ck\frac hd,\qquad M=14080C.
\]

For each \((r,e,\ell)\), let \(s=C2^e/(2^\ell r)\in\mathbb Z\). For fixed \(j\) the certified residue mask from this layer in the period \([0,M)\) is

\[
P_{j,r,e,\ell}
=\{s h:1\le h<M/s,\ \gcd(h,2r)=1,\
 C_{11}(h,r2^{j+\ell-e}-h)=1\},
\]

where \(C_{11}\) is the inherited **complete projective** no-root predicate, including the distinguished projective point and the \(z=3\) collision; the modulus-110/exact modular form is reproduced in the verifier.

The period is legitimate because

\[
\frac Ms=14080\frac{2^\ell r}{2^e}
\]

is a multiple of both \(110\) and \(2r\) for all \(e\le7,\ell\in\{0,1\}\). The denominator inside \(C_{11}\) depends only on \(j+\ell-e\pmod{20}\) (all exponents are positive for \(j\ge8\)). Thus every stage mask is completely determined by one of the 20 values \(j=14,\ldots,33\); this also covers \(8\le j\le13\).

The level-0 menu is present at all heights \(H\ge k\). A level-1 layer enters at the ratio

\[
\rho_{\ell=1}=\frac{d}{k}=\frac{2r}{2^e}.
\]

The distinct entrances in \(1<\rho\le2\), sorted in exact rational arithmetic, are

\[
\frac{11}{8},\ \frac{91}{64},\ \frac{23}{16},\
\frac{47}{32},\ \frac32,\ \frac{13}{8},\
\frac{53}{32},\ \frac{27}{16},\
\frac74,\ \frac{29}{16},\ \frac{61}{32},\
\frac{31}{16},\ 2.
\]

For every exponent class, start from all level-0 points and level-1 points whose threshold is at most 1, then insert entire level-1 masks at each entrance. On each half-open interval of height ratios between consecutive entrances, the union is constant. Sort the points modulo \(M\), include the cyclic wrap, and compute the maximal integer gap \(G\) exactly. If \(t\) is the **next** entrance, then throughout that interval \(\rho G/C\le tG/C\). Direct exhaustive enumeration of all 20 exponent classes and all entrances gives the parity table above. At \(\rho=2\), the next dyadic level takes over.

Consequently every interval in the original phase coordinate of length exceeding \((G/C)/k\) meets a certified point. This remains true after clipping the periodic mask to \([0,1]\), since gaps to the endpoints are bounded by adjacent gaps in the infinite periodic set. Using \(H=\rho k\) and the stage bounds gives the claimed \(490/(143H)\) uniformly.

## Verification and scope

Run `python EC49FVR_ADAPTIVE_TWO_SCALE_VERIFY.py` using only Python 3 standard-library integer/rational arithmetic. It re-derives the mod-11 predicate directly from the parent observer coefficients, compares it on **12,100** positive exponent pairs against the reduced residue test, checks **20/20** full \(j\bmod20\) stages and all 13 entrance cutoffs, and independently enumerates finite-height fractions at five heights per \(j=8,9,10,11\). Each full stage has **92,960** distinct period points after both dyadic levels are included. It returns `ALL PASS`. The companion output retains each stage's exact critical ratio and gap.

**Evidence status:** exact exhaustive finite-period certificate plus the preceding period-reduction proof; inherited Bernoulli algebra and its no-root implication are parent-dependent; independent mathematical review, native RESULT and project admission remain pending. The finite masks are source-level arithmetic observations, not native X6 operations, so no native BRC–Shor numerical computation is claimed.

**Next:** Search for another finite denominator menu or mixed-prime certificates that push the absolute coverage coefficient below \(490/143\), possibly with a useful uniform discrepancy estimate for moving intervals of length \(\asymp1/H\). Preserve all composite denominator layers and their provenance until a scope-specific observer-safe redundancy certificate exists.
