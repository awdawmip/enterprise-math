# CM(-24) unit reciprocity: imported theorem audit

Initial preparation status: `READ_ONLY_PRIOR_ART_BEFORE_EXECUTION_OPEN`.

Post-open update: the applicability obligations below are now discharged in `APPLICABILITY_PROOF.md` under `ER-E97E2B99EEA5F2124A59`; the preparation chronology is retained here.

Prepared for root researcher `EM-DIRECT-49ADE6`; no new UR proof or research computation is asserted by this preparation. Exact frozen parents and `TASKBOOK.md` were read. Retrieval date: 2026-10-07 UTC. Download byte hashes and URLs are recorded in `PUBLIC_SOURCE_MANIFEST.json`.

## Primary arithmetic input

Sarah Chisholm, Alyson Deines, Ling Long, Gabriele Nebe, Holly Swisher, **p-adic analogues of Ramanujan type formulas for 1/pi**, *Mathematics* 1 (2013), DOI [10.3390/math1010009](https://doi.org/10.3390/math1010009). Published copy: [German National Library PDF](https://d-nb.info/1163276057/34), Theorem 1, printed page 12 (PDF page 4).

For `d in {2,3,4,6}`, write

\[
E_d(\lambda)=\widetilde E_d((1-\sqrt{1-\lambda})/2).
\]

Theorem 1 gives

\[
\sum_{k=0}^{p-1}(ak+1)
\frac{(1/2)_k(1/d)_k((d-1)/d)_k}{(k!)^3}\lambda^k
\equiv \operatorname{sgn}\left(\frac{1-\lambda}{p}\right)p\pmod{p^2}.
\]

Here `sgn = +1` for ordinary reduction and `sgn = -1` for supersingular reduction. Required conditions: `Q(lambda)` totally real; the indicated curve has CM; `|lambda|<1` in an embedding; `p` unramified in `Q(sqrt(1-lambda))`; good reduction at `p`; `a,lambda` are p-adic units; and `a` is the coefficient in the corresponding complex Ramanujan `delta/pi` identity. The statement requires no ordinary unit root on the supersingular branch. Its supersingular proof is addressed at the end of Section 5.

The published PDF header says pages 9–31 whereas publisher/LSU bibliographic metadata says 9–30; DOI, theorem number and printed theorem page remove this harmless bibliographic discrepancy.

## Exact complex normalization

Jesús Guillera, **A method for proving Ramanujan series for 1/pi**, [arXiv:1807.07394v4](https://arxiv.org/abs/1807.07394v4), 16 August 2018. Equation (1) uses `(a+bn) z^n` normalization. Table 3, printed/PDF page 10, first positive-series row has level 3 (`s=3`),

\[
z=1/2,\qquad a=1/(3\sqrt3),\qquad b=6/(3\sqrt3).
\]

Thus the table supplies exactly the complex normalization for weight `6k+1`, parameter `lambda=1/2`, and right side `3 sqrt(3)/pi`. This is not an empirical fit. Roman Le Lan, [arXiv:2604.03327v1](https://arxiv.org/html/2604.03327v1), 2 April 2026, Lemma 2 / equation (2.2), also explicitly records this same identity and attributes it to Guillera Table 3.

Guillera's equation (25) gives `level = 4 sin^2(pi/s)`, so level 3 means `s=3`. The table's separate column `d=2` is the modular-transformation degree parameter; it is **not** the hypergeometric parameter denoted `d=3` by Chisholm et al. The original rendered pages were visually inspected and saved as `Guillera_equation1_page1.png` and `Guillera_table3_page10.png`.

## Later restatement and precision boundary

Angelica Babei, Manami Roy, Holly Swisher, Bella Tobin, Fang-Ting Tu, **Supercongruences arising from Ramanujan-Sato Series**, [arXiv:2408.08844v3](https://arxiv.org/html/2408.08844v3), 12 March 2025, Theorem 2.1, repeats the 2013 weighted theorem with both ordinary and supersingular signs.

This paper corrects the companion **unweighted** 2013 Theorem 2 in its Theorem 2.2; that correction must not be confused with a restriction of weighted Theorem 1 to ordinary primes. Section 6, formula (6.8), concerns exactly `F_{6,(1/2,1/3,2/3)}(1/2)` but presents its stronger mod-`p^3` version as computational evidence through `p<150`, not an all-prime theorem. Example J instead truncates a **product of two 3F2 series** and is a different object.

Current arXiv metadata still identifies v3 as the latest version. The [published article](https://doi.org/10.1007/s00025-025-02497-0) is *Results in Mathematics* **80**, article 184 (published 22 August 2025). The publisher records a 5 September 2025 correction to a corollary subheading number, not a correction to weighted Theorem 2.1. Published full text is subscription-only; the inspected mathematical text here is explicitly the pinned arXiv v3.

## Required post-open applicability check

The genuine candidate is therefore 2013 Theorem 1 with `d=3`, `a=6`, `lambda=1/2`. Before using it to assert UR, the execution must explicitly verify the exact elliptic model's CM field, good reduction/excluded primes, the unramified extension, and both residue-class signs. It must then translate the theorem's weighted 3F2 truncation to the frozen `g h` interface at the needed precision and recover the frozen factor `-6 Q'_m(1/2)`.

Only mod-`p^2` first-digit normalization is supplied by this import. It does not establish Sun A14(ii), the parent mod-`p^3` target, or `LIFT`.

No claim of originality, independent Driver review, or Source promotion is made.


---

# Exact CM(-24) applicability of the weighted Ramanujan congruence

Researcher: `EM-DIRECT-49ADE6` (root); assisting subagent: `cm24_prior_art`.

Execution: `ER-E97E2B99EEA5F2124A59`; run: `RUN-cd80604b199723bbf24b0924`, generation 1. Native execution-open request: `em-timed-open-20261007-1319`, successfully opened against Source `801e56c5923cd2a9d1c33a8c8a30cd44a00487a8` before this derivation. This is a collaborative proof contribution, **not** an independent Driver review.

## Proposition

For every prime `p = 6m+1` with `p mod 24 in {13,19}`,

\[
S_p:=\sum_{k=0}^{p-1}(6k+1)
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3\,2^k}
=\sum_{k=0}^{p-1}(6k+1)
\frac{\binom{2k}{k}^{\!2}\binom{3k}{k}}{216^k}
\equiv p\pmod{p^2}.
\tag{W2}
\]

The proof imports Chisholm–Deines–Long–Nebe–Swisher (2013), Theorem 1, whose explicit supersingular branch is essential. It does not import Sun A14(ii) or a conjectural mod-`p^3` statement.

## 1. Normalize the complex identity exactly

Guillera, [arXiv:1807.07394v4](https://arxiv.org/abs/1807.07394v4), equation (1), writes his series as

\[
\sum_{k\geq0}\frac{(1/2)_k(1/s)_k(1-1/s)_k}{(k!)^3}
(a+bk)z^k=\frac1\pi.
\]

His Table 3 first positive-series row has level `3`, `z=1/2`, `a=1/(3 sqrt(3))`, and `b=6/(3 sqrt(3))`. Equation (25), `level=4 sin^2(pi/s)`, makes this `s=3`. Thus in the arithmetic theorem's convention the coefficient is `alpha=b/a=6`, the parameter is `lambda=1/2`, and the complex constant is `delta=1/a=3 sqrt(3)`.

The table's degree column `d=2` has a different meaning from the arithmetic theorem's hypergeometric index `d=3`. No numerical evaluation selects or fits `alpha`.

## 2. Use the exact elliptic model named by the theorem

Set

\[
s^2=2,\qquad t=\frac{2-s}{4}
=\frac{1-\sqrt{1-\lambda}}2,\qquad\lambda=\frac12.
\]

The 2013 definition is

\[
E=\widetilde E_3(t):\qquad
y^2+xy+\frac{t}{27}y=x^3.
\]

Its Weierstrass coefficients are `a1=1`, `a2=a4=a6=0`, `a3=t/27`. Therefore

\[
b_2=1,\quad b_4=\frac{t}{27},\quad b_6=\frac{t^2}{729},\quad b_8=0,
\]

\[
c_4=b_2^2-24b_4=\frac{9-8t}{9},
\]

\[
\begin{aligned}
\Delta&=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6\\
&=\frac{(-8+9)t^3-t^4}{27^3}
=\frac{t^3(1-t)}{27^3}.
\end{aligned}
\]

Consequently

\[
j(E)=\frac{c_4^3}{\Delta}
=\frac{27(9-8t)^3}{t^3(1-t)}.
\]

Using `t(1-t)=1/8`, `t^2=(3-2s)/8`, and `9-8t=5+2s` gives

\[
\begin{aligned}
j(E)&=1728\frac{(5+2s)^3}{3-2s}
=1728(245+166s)(3+2s)\\
&=1728(1399+988s)
=2417472+1707264s.
\end{aligned}
\]

The other square-root choice yields the conjugate `2417472-1707264s`. These are exactly the two CM(-24) `j` values in the frozen accepted parent, with Hilbert class polynomial

\[
X^2-4834944X+14670139392.
\]

Thus the theorem's own model has CM by the order of discriminant `-24` in `Q(sqrt(-6))`. This is a model-identification step consuming the frozen CM arithmetic, not a replay of the parent's Hasse-zero proof.

## 3. Verify all local hypotheses, with no missing exceptional target prime

Every target prime is greater than 3. Since `t` and `1-t` belong to `O_{Q(sqrt(2))}[1/2]` and their product is `1/8`, both are units at each prime over such a `p`. The model's coefficients are integral there, and `Delta=t^3(1-t)/27^3` is a unit. Hence the indicated model has good reduction at every target prime.

The field `Q(sqrt(1-lambda))` equals `Q(sqrt(2))` and has discriminant `8`. Every target `p` is unramified in it. The theorem requires `alpha` and `lambda`, not `t`, to embed in `Z_p^×`; these are the rational units `6` and `1/2`. In fact `t` lies in the unramified quadratic extension at our target primes, which is permitted.

Finally `Q(lambda)=Q` is totally real and `|lambda|=1/2<1`. Section 1 verified the theorem's complex-normalization hypothesis. The chosen CM order has discriminant `-24`, divisible only by 2 and 3, so no target prime is a ramified CM exception.

## 4. Determine both arithmetic signs exactly

Both target classes satisfy `p=1 mod 3`, hence quadratic reciprocity gives

\[
\left(\frac{-3}{p}\right)=1.
\]

Their residues modulo 8 differ and are retained separately:

| p mod 24 | p mod 8 | (2/p) | (-3/p) | (-6/p) |
|---|---|---|---|---|
| 13 | 5 | -1 | +1 | -1 |
| 19 | 3 | -1 | +1 | -1 |

Thus each target prime is inert in `Q(sqrt(-6))`. The classical CM reduction theorem, already used in the frozen CM0 dependency, makes the good reduction supersingular. The arithmetic theorem's reduction sign is therefore `sgn=-1`.

Its separate parameter character is

\[
\left(\frac{1-\lambda}{p}\right)
=\left(\frac{1/2}{p}\right)
=\left(\frac2p\right)=-1.
\]

Therefore the theorem's coefficient of `p` is `(-1)(-1)=+1` in both target classes. The positive constant in `(W2)` is obtained from two exact characters, not from ordinary unit-root machinery or regression data.

## 5. Apply the arithmetic theorem and translate its summand

All hypotheses of [Chisholm et al., Theorem 1](https://doi.org/10.3390/math1010009) now hold with `d=3`, `alpha=6`, and `lambda=1/2`; its explicitly supersingular case proves the first congruence in `(W2)`.

The exact factorial identities

\[
(1/2)_k=\frac{(2k)!}{4^k k!},\qquad
(1/3)_k(2/3)_k=\frac{(3k)!}{27^k k!}
\]

give

\[
\frac{(1/2)_k(1/3)_k(2/3)_k}{2^k(k!)^3}
=\frac{(2k)!(3k)!}{216^k(k!)^5}
=\frac{\binom{2k}{k}^{\!2}\binom{3k}{k}}{216^k}.
\]

The cutoff is the theorem's actual cutoff `p-1`; no infinite-to-truncated identity has been presumed. This completes the all-target-prime proof of `(W2)`.

## 6. Provenance, precision, and BRC boundaries

The sufficient exact carrier for the model identification is the **labeled** quadratic algebra `Q[s]/(s^2-2)` with both conjugate branches retained. Good reduction is checked before reduction; `t` is not silently projected into `F_p`. The final rational weighted sum is observed only modulo `p^2`, which is necessary for a future division by `p`. The two residue classes remain distinct until their two characters have been evaluated. No Boolean CM flag is substituted for the character normalization.

The available positive-rational BRC holonomy and positive-weight CWM modules do not implement signed quadratic-field Weierstrass invariants; their positivity requirements exclude this signed symbolic carrier. Accordingly this local invariant algebra is `NOT_APPLICABLE_TO_POSITIVE_BRC_TOOL_CARRIER`, with explicit reason, while the root's BRC-preserving sum checker is separately recorded. The derivation above is exact symbolic mathematics; no external arithmetic routine, finite prime scan, or uncertified numerical CM recognition is used here.

The parameter-displacement interpretation and the factor `-6 Q'_m(1/2)` belong to the frozen parent interface; root's proof must join `(W2)` to that interface. This component supplies the correctly normalized first digit only. It establishes neither the mod-`p^3` statement nor `LIFT`, and makes no originality claim for `(W2)`, which is an application of existing literature.

Primary source files, exact URLs and SHA-256 pins are listed in `PUBLIC_SOURCE_MANIFEST.json`; source statements and the distinction from later conjectural formulas are audited in `IMPORT_AUDIT.md`.
