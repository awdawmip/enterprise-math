# R749SSG — Sharp uniform noise radius for recovering an unknown cutoff

**Date:** 2026-11-16 (Asia/Shanghai). **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen auxiliary scientific input:** `a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Predecessor:** R749SSF in Draft PR #2557, which proves that the exact raw ratio identifies cutoff and errors. This paper isolates **cutoff identity** under additive real-valued measurement noise; it does not require recovering the two original integer errors.

## Observation interface and theorem

For labeled weights `(1,1,2,3,6)`, define `C_q=|{k∈Z^5_{≥0}:Σw_j k_j≤q−1}|` and `T_q=Σk_1` over that set. Let `q≥6` be an unknown integer and allow independent integer errors `|e|,|d|≤2`. The exact raw ratio and the noisy reading are

\[
X(q,e,d)=\frac{T_q+e}{C_q+d},
\qquad Z=X(q,e,d)+\eta,\quad |\eta|\le\varepsilon.
\]

Write `S_q={X(q,e,d): |e|,|d|≤2, e,d∈Z}` for the 25-element finite set (R749SSF proves internal injectivity).

**Theorem.** The exact minimum distance between different cutoff classes is

\[
\boxed{\inf_{q\ne q',\ q,q'\ge6}\operatorname{dist}(S_q,S_{q'})=\frac1{201}.}
\]

It is attained at `q=6` and `q'=7` by

\[
X(6,2,-2)=\frac43,\qquad
X(7,-2,2)=\frac{89}{67},\qquad
\frac43-\frac{89}{67}=\frac1{201}.
\]

Consequently every raw-ratio observation with **strict additive noise** `|eta|<1/402` determines the unknown integer cutoff `q` uniquely by the nearest cutoff-class decoder. This global radius is sharp. At noise `1/402` the midpoint `535/402` has the two realizations

\[
\frac43-\frac1{402}=\frac{535}{402}
=\frac{89}{67}+\frac1{402}.
\]

## Exact infinite proof

R749SSF defines the rational interval envelope

\[
I_q=\left[\frac{T_q-2}{C_q+2},\frac{T_q+2}{C_q-2}\right]
=[L_q,U_q]
\]

and the integer gap numerator

\[
G(q)=(T_{q+1}-2)(C_q-2)-(T_q+2)(C_{q+1}+2).
\]

For all `q≥7`, the envelope gap is

\[
L_{q+1}-U_q=\frac{G(q)}{(C_q-2)(C_{q+1}+2)}.
\]

The desired strict inequality `L_{q+1}-U_q>1/201` is exactly the positivity of the integer expression

\[
F(q):=201G(q)-(C_q-2)(C_{q+1}+2).
\]

Using the exact R749SSF source count recurrence, the certificate verifies `F(q)>0` at every integer `7≤q≤35`. The generating functions in R749SSF show that for each residue class `q≡b (mod 6)` with `q≥36`, `F(q)` is a degree-at-most-10 polynomial (the degree-11 cross-product terms cancel). Accordingly for `b=36,37,38,39,40,41`,

\[
F(b+6j)=\sum_{i=0}^{10} f_{b,i}\binom{j}{i},\qquad
f_{b,i}=\Delta_6^iF(b).
\]

The attached standard-library exact-integer certificate computes all 66 coefficients. **Every coefficient is strictly positive** and the common tenth difference equals `382,112,640`. Each binomial coefficient is nonnegative for integer `j≥0`, proving the strict envelope separation

\[
\boxed{L_{q+1}-U_q>\frac1{201}\qquad(q\ge7).}
\]

For the exceptional pair `q=6,7`, the 25-value spectra have closest values `4/3` and `89/67`: at q6 the second largest is 17/13, while at q7 the second smallest is 90/67, so no other cross-value pair is as close. For `q=6` versus `q≥8`, the lower envelope endpoint at q8 is `77/50`, and

\[
\frac{77}{50}-\frac43=\frac{31}{150}>\frac1{201}.
\]

Every pair `q,q'≥7` has distance strictly greater than 1/201 by the ordered envelope gaps. This covers all pairs and proves the exact minimum. The sharp noise statement follows by the triangle inequality and the displayed midpoint witness. `□`

## Different observables require different precision

The uniform positive noise radius applies **only to recovering the integer cutoff q**. To identify both integer errors as well, the separation between legal observations at the *same* q can be arbitrarily small:

\[
X(q,e+1,d)-X(q,e,d)=\frac1{C_q+d}\xrightarrow[q\to\infty]{}0.
\]

Hence no strictly positive **uniform absolute additive noise radius** recovers the full triple `(q,e,d)` for every q≥6. This provides an exact two-tier observer statement: the cutoff carrier is uniformly robust, while the fine error-coordinate carrier requires scale-dependent precision. It is a source-observer claim, not a native BRC port or X6 time theorem.

## Exact reproducibility and next question

`R749SSG_SHARP_CUTOFF_NOISE_CERT.py` recomputes exact source counts and the six residual polynomial certificates, checks 7≤q≤35 directly, evaluates the exceptional 6/7 finite spectra, and verifies the resulting lower bounds by exact rational arithmetic. `R749SSG_SHARP_CUTOFF_NOISE_RESULTS.json` contains all 66 positive coefficients and the sharp witness; local Python run returned `PASS`. Review is `AUTHOR_EXACT_NOT_REVIEWED`.

Next: determine an explicit **scale-dependent sharp noise radius** for simultaneous recovery of both errors, and return to the original smooth-subtracted Y observer's infinite unknown-cutoff collision question.
