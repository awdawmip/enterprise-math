# R154B — Complete classification of actual equal-denominator finite Sturmian words

Date: 2026-11-14 (Asia/Shanghai). Classification: AUTHOR-SIDE ALL-LENGTH PROOF; independent review NOT_REVIEWED. Frozen science input \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\` unchanged. Scope: the external tied-phase S23 scalar finite-mechanical-word observer, not native X6.

**This resolves the explicit open question in R153 and R154:** equal *nontrivial interior* denominators occur for genuine finite Sturmian words only in the two even-length alternating words.

## Statement

Let \(w=w_0\cdots w_{m-1}\) be a binary word of length \(m\), \(p_j=\sum_{0\le i<j}w_i\), and define its free-intercept slope support

\[
\alpha(w)=\max\left(0,\max_{0\le i<j\le m}
       \frac{p_j-p_i-1}{j-i}\right),\quad
\beta(w)=\min\left(1,\min_{0\le i<j\le m}
       \frac{p_j-p_i+1}{j-i}\right).
\]

Assume \(0<\alpha<\beta<1\), and the two fractions in lowest terms have the **same denominator** \(b>1\):

\[
\alpha=\frac ab,\qquad \beta=\frac cb,\qquad
0<a<c<b,\quad \gcd(a,b)=\gcd(c,b)=1.
\]

**R154B theorem (necessity and sufficiency).** There is an integer \(h\ge2\) such that

\[
\boxed{b=2h-1,\quad a=h-1,\quad c=h,\quad m=2h}
\]

and \(w\) is exactly one of

\[
\boxed{(01)^h,\qquad (10)^h.}
\]

Conversely, each such alternating word has the two stated support endpoints (proved independently in R153.3), so the classification is exact for **all lengths**, not just a finite sweep.

In particular, among genuine finite words, **equal reduced interior endpoint denominators are completely classified**. The pair's identical full coefficient-by-coefficient phase-fiber counts follow from R153.3:

\[
C_{(01)^h}(K)=C_{(10)^h}(K)
=\left\lceil\frac{K-1}{2h-1}\right\rceil,\qquad K\ge2.
\]

## Proof

**Lemma 1 — a finite word cannot realize both of its full-length endpoint bounds when both are interior.** If a word of length \(n\) has \(k\) ones, the two full-word bounds are \((k-1)/n\) and \((k+1)/n\). They cannot simultaneously be its actual support endpoints if \(0<(k-1)/n<(k+1)/n<1\). Indeed, inspect the suffix obtained by deleting the first letter. If that letter is 0, the suffix still has \(k\) ones and gives a stricter lower bound \((k-1)/(n-1)>(k-1)/n\). If that letter is 1, the suffix has \(k-1\) ones and gives the stricter upper bound \(k/(n-1)<(k+1)/n\) (since \(k+1<n\)). In either case the claimed simultaneous endpoints are impossible.

**Step 1 — gap and length.** A support endpoint with reduced denominator \(b\) must be attained by some factor length divisible by \(b\); thus \(m\ge b\). If \(k\) is the total number of ones, the full-word factor requires
\[
\frac{k-1}{m}\le\frac ab<\frac cb\le\frac{k+1}{m},
\quad\text{hence}\quad m(c-a)\le2b. \tag{1}
\]
If \(c-a\ge2\), then \(m\le b\), hence \(m=b\), \(c-a=2\). At \(m=b\), each endpoint can only be attained at the unique factor of length \(b\), forcing \(a=k-1,\ c=k+1\). This contradicts Lemma 1. Therefore
\[
\boxed{c=a+1.} \tag{2}
\]
Now (1) gives \(m\le2b\). At \(m=b\), both endpoints would again need the same full-word factor, giving gap 2 rather than 1; impossible. At \(m=2b\), (1) holds with equality, forcing both full-word bounds to be the actual endpoints, again contradicting Lemma 1. Consequently
\[
\boxed{b+1\le m\le 2b-1.} \tag{3}
\]

**Step 2 — fixed length-\((b-1)\) counts and a period.** By (3), only factor length \(b\) (not \(2b\)) can attain either endpoint with reduced denominator \(b\). Thus some length-\(b\) factor contains \(a+1\) ones (attaining the lower endpoint), and another contains \(c-1=a\) ones (attaining the upper endpoint).

Every length-\((b-1)\) factor contains **exactly \(a\)** ones. In fact, if a factor had \(t\ge a+1\), its lower bound \((t-1)/(b-1)\ge a/(b-1)>a/b\) would contradict \(\alpha=a/b\). If it had \(t\le a-1\), its upper bound \((t+1)/(b-1)\le a/(b-1)<(a+1)/b\) (because \(a+1<b\)) would contradict \(\beta=(a+1)/b\). Therefore \(t=a\).

Since consecutive length-\((b-1)\) factors have equal count, for every index \(0\le i\le m-b\),
\[
w_i=w_{i+b-1}. \tag{4}
\]
A length-\(b\) factor starting at such an index has \(a+w_i\) ones. Because both \(a\)- and \((a+1)\)-one length-\(b\) factors occur, the set of starting letters \(w_i\), \(0\le i\le m-b\), contains both 0 and 1.

**Step 3 — length-\((b-2)\) inequalities force central endpoints.** Remove the first letter from a length-\((b-1)\) factor starting at either of the preceding indices. The resulting length-\((b-2)\) factors have respectively \(a\) and \(a-1\) ones. The first supplies a lower-bound inequality, and the second an upper-bound inequality:
\[
\frac{a-1}{b-2}\le\frac ab,\qquad
\frac a{b-2}\ge\frac{a+1}{b}.
\]
Cross multiplication (with \(b\ge3\)) gives
\[
\boxed{b-2\le2a\le b.} \tag{5}
\]
If \(b\) is even and \(b\ge4\), (5) forces \(a=b/2-1\) or \(a=b/2\); in the former case \(c=b/2\), in the latter \(a=b/2\). Either violates the stipulated coprimality with \(b\). Hence \(b\) is odd and (5) forces
\[
b=2h-1,\quad a=h-1,\quad c=h,\quad h\ge2. \tag{6}
\]

**Step 4 — alternation and exact length.** Equation (6) yields \(\alpha<1/2<\beta\). A factor \`11\` would impose \(\alpha\ge(2-1)/2=1/2\), and a factor \`00\` would impose \(\beta\le(0+1)/2=1/2\). Both are impossible; hence every adjacent pair differs and \(w\) is alternating.

By (3), \(m\ge b+1=2h\). If \(m\ge b+2=2h+1\), take any alternating factor of length \(2h+1\). If it starts with 0, it has \(h\) ones and forces
\[
\beta\le\frac{h+1}{2h+1}<\frac h{2h-1}=\beta,
\]
a contradiction. If it starts with 1, it has \(h+1\) ones and forces
\[
\alpha\ge\frac h{2h+1}>\frac{h-1}{2h-1}=\alpha,
\]
again a contradiction. Therefore \(m=2h=b+1\), and the only possibilities are the two alternating words.

R153.3 proves their converse endpoints and fiber count formula. This completes the all-length classification. QED.

## Verification, exact scope and next question

R154's separate exact program \`R154_check.py\` exhaustively screened all binary words for \(m=1,\ldots,16\) (2,404 actual finite Sturmian words); it found exactly the two even-length alternating words in the equal-interior-denominator population. This finite sweep is **corroboration**, not the basis of this universal proof. R153.3's symbolic converse is already saved. No independent semantic review or Lean check has occurred (NOT_REVIEWED).

The proof uses only factor frequency bounds and elementary integers. It does **not** prove the much broader conjecture that every pair of *different* finite words with the same endpoints and complete phase-fiber counts must be alternating: distinct words might share cut data even with **unequal** endpoint denominators. The precise next question is to classify genuine unequal-denominator full-count aliases; R153.1 already provides an injective increment-code theorem for unrestricted cut **residues**, so any remaining aliases must be sought in the actual word-to-cut map and compatible integer lifts. R152B's full-length permanent-saturation threshold also remains open. No native X6 correspondence, P000 change, CLAIM or Result acceptance is asserted.
