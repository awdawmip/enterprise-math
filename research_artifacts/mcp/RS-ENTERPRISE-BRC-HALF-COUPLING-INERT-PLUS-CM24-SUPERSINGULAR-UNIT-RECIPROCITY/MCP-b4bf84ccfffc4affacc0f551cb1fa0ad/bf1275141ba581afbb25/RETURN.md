# CM(-24) supersingular unit reciprocity — research return

Status: `RESEARCHER_RETURN / UR_PROVED_FROM_AUDITED_IMPORT_AND_FROZEN_INPUTS`.

Researcher: `EM-DIRECT-49ADE6` (`TASK_RESEARCH`).
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-SUPERSINGULAR-UNIT-RECIPROCITY`.
Publication: `TP2-17BF80BAD90666A57EC9`.
Execution: `ER-E97E2B99EEA5F2124A59`; run `RUN-cd80604b199723bbf24b0924`, generation 1.

## Result and scope

For every prime \(p=6m+1\) with \(p\equiv13,19\pmod{24}\), the frozen quantities satisfy
\[
\boxed{\frac{g}{p}\,\bigl(-6Q'_m(1/2)\bigr)\equiv1\pmod p.}\tag{UR}
\]

The proof imports the **weighted** mod-\(p^2\) theorem of Chisholm–Deines–Long–Nebe–Swisher (2013), checks its exact supersingular CM(-24) specialization, and composes it with the accepted finite Clausen and Legendre interfaces. It does not assume Sun A14(ii), an ordinary unit root, or a mod-\(p^3\) supercongruence. The mathematical contribution here is closing the current task by an audited existing theorem and exact interface translation; no claim of an original supercongruence is made.

By the frozen parent equivalences, `JT0` follows and `JT2 iff LIFT` remains. **LIFT is not attacked or proved in this task.** The parent Objective is not declared complete. A formal Source Result and independent Driver review remain separate from this derivation.

## 1. Frozen data and precision

Work in \(\mathbb Z_{(p)}\). Put
\[
b_k=\frac{(1/6)_k(1/3)_k}{(k!)^2},\qquad
B_k=b_k2^{-k},\qquad
g=\sum_{k=0}^{p-1}B_k,\quad
h=\sum_{k=0}^{p-1}(12k+1)B_k.
\]
All these finite coefficients have denominators prime to \(p\). The accepted parent gives \(p\mid g\),
\[
P_{2m}(T)=Q_m(T^2),\quad Q_m(1/2)=0,\quad Q'_m(1/2)\ne0\quad(\bmod p),
\]
and
\[
h\equiv-6Q'_m(1/2)\pmod p.\tag{H}
\]
The exact parameter displacement is retained:
\(1/6=-m+p/6\), \(1/3=-2m+p/3\). Thus the same \(g/p\) is the first divided displacement from the terminating family, not a newly normalized proxy. Computing \(g\) only modulo \(p\) would erase it; the proof retains \(g\bmod p^2\) until after division by \(p\).

The parent CM0, SIMPLE, JT0/UR and JT2/UR+LIFT results are consumed as accepted inputs, not rediscovered.

## 2. The exact imported theorem

Chisholm et al., *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1 (2013), DOI [10.3390/math1010009](https://doi.org/10.3390/math1010009), Theorem 1, printed page 12, prove the following weighted congruence. For \(d\in\{2,3,4,6\}\), a totally real CM parameter \(\lambda\), and the normalized Ramanujan coefficient \(\alpha\) in the corresponding identity with weight \(1+\alpha k\),
\[
\sum_{k=0}^{p-1}(1+\alpha k)
\frac{(1/2)_k(1/d)_k(1-1/d)_k}{(k!)^3}\lambda^k
\equiv \operatorname{sgn}\left(\frac{1-\lambda}{p}\right)p\pmod{p^2}.\tag{CDLNS}
\]
Here \(\operatorname{sgn}=-1\) for supersingular reduction and \(+1\) for ordinary reduction. The hypotheses include good reduction, no ramification in \(\mathbb Q(\sqrt{1-\lambda})\), and \(\alpha,\lambda\in\mathbb Z_p^\times\). The supersingular case is explicitly part of the theorem; it is not an extension of an ordinary-only formula made here.

The weighted theorem is restated as Theorem 2.1 of Babei–Roy–Swisher–Tobin–Tu, [arXiv:2408.08844v3](https://arxiv.org/abs/2408.08844v3). Their correction in Theorem 2.2 concerns the **unweighted companion theorem**, which this proof does not invoke. Their stronger weighted mod-\(p^3\) formula (6.8) is not used as a theorem.

## 3. Every specialization hypothesis

Take \(d=3\), \(\lambda=1/2\), \(\alpha=6\). The exact complex normalization is
\[
\sum_{k\ge0}(6k+1)
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}2^{-k}
=\frac{3\sqrt3}{\pi}.
\]
This is the positive first row of Table 3 in Guillera, [arXiv:1807.07394v4](https://arxiv.org/abs/1807.07394v4), with its equation (1) convention: \(a=1/(3\sqrt3)\), \(b=6/(3\sqrt3)\), \(z=1/2\). The ratio \(b/a=6\) fixes the coefficient; it is not fitted from finite primes. That table's modular degree is a different parameter from the hypergeometric \(d\).

Write \(s^2=2\) and \(t=(2-s)/4=(1-\sqrt{1-\lambda})/2\). The theorem's model is
\[
E:\ y^2+xy+(t/27)y=x^3.
\]
It has
\[
c_4=(9-8t)/9,\qquad \Delta=t^3(1-t)/27^3,
\qquad j=\frac{27(9-8t)^3}{t^3(1-t)}=2417472+1707264s.
\]
The other choice of square root gives its conjugate. These are the frozen discriminant -24 CM values, roots of
\(X^2-4834944X+14670139392\); the CM field is \(\mathbb Q(\sqrt{-6})\).

The parameter field of \(\lambda\) is \(\mathbb Q\), which is totally real, and \(|\lambda|<1\). All target primes exceed 3, so \(6\) and \(1/2\) are p-adic units. The extension \(\mathbb Q(s)\) has discriminant 8, hence is unramified at every target prime. Since \(t(1-t)=1/8\), both factors are integral units away from 2, and the displayed discriminant is a unit at every prime above \(p>3\). This verifies good reduction without omitting any target prime.

For either target class, \(p\equiv1\pmod3\), \(p\equiv3\) or \(5\pmod8\), so
\[
\left(\frac{-3}{p}\right)=1,\quad
\left(\frac2p\right)=-1,\quad
\left(\frac{-6}{p}\right)=-1.
\]
Thus the CM curve is supersingular (the same frozen inert-CM input), and
\(\bigl((1-\lambda)/p\bigr)=\bigl((1/2)/p\bigr)=(2/p)=-1\). The two signs in (CDLNS) multiply to \(+1\). The nonsplit but unramified quadratic extension is allowed: the theorem does **not** require \(t\in\mathbb Q_p\).

Consequently, with
\[
W_p:=\sum_{k=0}^{p-1}(6k+1)
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}2^{-k},
\]
we obtain the all-prime theorem
\[
W_p\equiv p\pmod{p^2}.\tag{W}
\]

## 4. Translation through the frozen finite interface

This step uses the already closed finite Clausen/valuation interface only to translate (W); it does not reopen the parent harmonic or tail problem.

Let \(F(z)={}_2F_1(1/6,1/3;1;z)\), \(F_{<p}(z)=\sum_{k<p}b_kz^k\), and \(\theta=z\partial_z\). Clausen's coefficient identity is
\[
F(z)^2={}_3F_2(1/2,1/3,2/3;1,1;z).
\]
Every coefficient of degree less than \(p\) agrees when \(F\) is replaced by \(F_{<p}\). Exactly,
\[
(1+6\theta)F_{<p}^2=F_{<p}(1+12\theta)F_{<p}.
\]
At \(z=1/2\), this gives
\[
gh=W_p+\sum_{\substack{0\le i,j<p\\i+j\ge p}}
\bigl(1+6(i+j)\bigr)B_iB_j.\tag{C}
\]
The accepted valuation blocks for \(p=6m+1\) are 0 on \(k\le m\), 1 on \(m<k\le2m\), and 2 on \(2m<k<p\). In any pair in (C), at least one index exceeds \(2m\), because otherwise \(i+j\le4m<p\). Its term is divisible by \(p^2\), while the other factor is p-integral. Thus the frozen tail contributes zero modulo \(p^2\), and
\[
gh\equiv W_p\pmod{p^2}.\tag{B}
\]
There is no exchange of an infinite p-adic sum with a truncation: Clausen is used coefficientwise through degree \(p-1\), and the remaining finite pairs are controlled separately.

Combine (W) and (B). Because \(g=pG\) with \(G\in\mathbb Z_{(p)}\),
\[
pGh\equiv p\pmod{p^2}
\quad\Longrightarrow\quad Gh\equiv1\pmod p.
\]
Insert (H) to obtain (UR). Conversely, (UR), (H), and (B) imply (W); the interface is bidirectional at precisely these moduli. The constant 1 comes from the normalized supersingular sign product, and the factor -6 comes from the frozen spatial derivative \(H_m(z)=Q_m(1-z)\), \(1+12z\partial_z\) at \(z=1/2\).

## 5. BRC carrier and observer boundary

Branches remain labeled by \((p,k)\), and serial pairs by \((p,i,j)\); the two prime residue classes are not averaged. The exact positive rational weights \(B_k\), index-weighted masses \((12k+1)B_k\), and pair weights are retained. Positive weighted BRC alternative composition sums exact masses, and serial composition multiplies them, matching the two sides of (C). Degree/index labels are retained until the finite cutoff observer is applied; a total-only CWM summary cannot recover the tail split.

The signed spatial derivative and modular unit are separate exact coordinates, not positive CWM states. In particular, no absolute value, Boolean support, logarithm, or valuation-only representation substitutes for the unit residue. The allowed observations are exact finite rational arithmetic, reduction modulo \(p^2\), proven division by \(p\), and then reduction modulo \(p\). The order is essential.

Source tool coverage and actual executable reuse are recorded separately. A matching positive CWM tool is used only for its exact mass law; it does not prove the arithmetic normalization.

## 6. Validation and independence

The deterministic checker passed on the fixed discrimination set `13,19,37,43,61,67,109,139`, four primes in each target class. It verified the exact finite coefficient/product translation and detected all 40 deliberately wrong weight, sign, and precision cases. It actually executed the unchanged source functions `direct_Bs`, `frac_mod`, `q_value_and_derivative`, and positive weighted BRC CWM composition. The flat bundle also passed an isolated `python -I` reproduction in a new temporary directory, with identical scientific records and exact trace hashes.

The completed shared-context mathematical audit found no blocking issue in the full theorem specialization and interface composition. A separate two-prime transcription check preserved an exact precision witness: at p=19 the weighted tail is 4332 modulo 19^3, although it is zero modulo 19^2. This only refutes an unauthorized precision upgrade; it does not evaluate LIFT or its R_p target.

These finite checks are falsification/translation checks, not the all-prime proof. The all-prime conclusion depends on (CDLNS), its verified specialization, and the frozen theorem interfaces. This is not an expanded replay of the old 77-prime scan. See `RUN.json`, `VALIDATION.md`, and the source manifests for exact evidence.

The task's two-route obligation is conditional on the first route failing to close or refute UR. The audited supersingular special-function/CM theorem closes UR, so no second unproved Gamma or Wronskian calculation is invented or claimed. The imported theorem's original proof uses the period/quasiperiod and supersingular Frobenius framework; that published proof remains an explicit dependency rather than a new derivation attributed to this execution.

All collaborators share the root's source-exposed context. This work is `NOT_INDEPENDENT / NONBLIND_DISCLOSED` for formal review purposes. Existing contributor history (`EM-DIRECT-E1F2B6`, `EM-DIRECT-FA0C27`, and inherited predecessor provenance) is preserved; a fresh session does not confer reviewer independence. The predecessor's private work remains UNKNOWN, and accepted parent proofs are credited to their original records.

## 7. Remaining work and control recommendation

After exact checks and a frozen Source Result, request independent Driver review of the imported theorem applicability and precision bridge. Do not redispatch this task to repeat CM0, SIMPLE, or an enlarged UR prime scan if the proof is accepted. The mathematical successor is the already isolated second digit `LIFT`, under a separate lawful Task route; this return neither publishes that Task nor asserts its truth.

Method harvest: `RESULT_ONLY / AUDITED_PRIOR_ART_APPLICATION_AND_INTERFACE_COMPOSITION`. No new general-purpose tool family, Foundation amendment, novelty claim, or parent-objective closure is requested.
