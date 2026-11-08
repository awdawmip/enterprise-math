# D25 / Original 216 grade-two source-port: exact quadratic-character normalization

Date: 2026-11-08 Asia/Hong_Kong. Independent second author-side unit after the finite 3F2 port theorem. **Exact universal algebraic proof; 148-prime independent regression; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.**

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.
Publication `TP2-B6F4FC938FF94941C1B7`; frozen science `enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.
Prior theorem: `research_notes/portable_direct/20261108_onhour_d25_w216_grade2_3f2_source_port.md` at `fc6474d86e5cbb4b1079c5c7e0f0dcb19cd741c8`.

## Stronger closed-form normalization of the original grade-two tail

Let `p=6m+1>=7` be prime and `N=(p+1)/2=3m+1`. Let `w_n=(6n+1)(2n)!(3n)!/((n!)^5 216^n)` and `K_r=(1)_r(5/6)_r(7/6)_r / ((3/2)_r^3 2^r)` in `F_p` for `0<=r<m`. The previous exact reduction was

\[
\frac1{p^2}\sum_{n=N}^{4m}w_n
\equiv C_p\sum_{r=0}^{m-1}(6r+4)K_r\pmod p,
\quad C_p=\frac{N+1}{(N!)^4 216^N}.
\]

**New theorem (every prime `p=1 mod6`):**

\[
\boxed{C_p\equiv \frac19\left(\frac6p\right)\pmod p,}
\qquad
\boxed{T_W(p)\equiv\frac19\left(\frac6p\right)
\sum_{r=0}^{m-1}(6r+4)\,
\frac{(1)_r(5/6)_r(7/6)_r}{(3/2)_r^3 2^r}\pmod p.}
\]

The Legendre factor is a field element (+1) or (-1), not an auxiliary Frobenius-basis choice.

**Proof.** Put (h=(p-1)/2), so (N=h+1\equiv1/2\pmod p). Wilson's theorem gives (h!^2\equiv(-1)^{h+1}\pmod p), hence (h!^4\equiv1\pmod p) and (N!^4\equiv N^4\equiv1/16\pmod p). Therefore

\[
C_p\equiv\frac{(3/2)16}{216^{h+1}}=
\frac{24}{216}\cdot216^{-h}
=\frac19\left(\frac{216}{p}\right)
=\frac19\left(\frac6p\right)\pmod p.
\]

The penultimate equality follows from Euler's criterion and (\chi_p(216)^{-1}=\chi_p(216)); (216=6^3). All inverses exist because (p>3). QED.

For the **two frozen target classes**, quadratic reciprocity gives the explicit signed port

\[
\boxed{T_W(p)\equiv
\begin{cases}
-\frac19 S_p, &p\equiv13\pmod{24},\\
+\frac19 S_p, &p\equiv19\pmod{24},
\end{cases}\quad
S_p=\sum_{r=0}^{m-1}(6r+4)K_r.}
\]

The numerical sign distinction is a rational unit/Legendre-character fact; it does **not** identify the actual native Frobenius or H0/B0 geometry. The same original index/valuation/provenance from the preceding theorem is retained.

## Executed proof-bound check

An independent check of the claimed `C_p=chi_p(6)/9` equality, using Euler's criterion and the previous direct-original-binomial verifier, passed all **148 primes** (7\le p\le2000, p\equiv1\pmod6) (including 77 target primes).

Witnesses `(p, chi_p(6), C_p, S_p, T_W)`:
- `(7,-1,3,4,5)`
- `(13,-1,10,1,10)`
- `(19,+1,17,5,9)`
- `(37,-1,4,5,20)`
- `(211,+1,47,130,202)`
- `(373,-1,290,217,266)`

This algebraic simplification removes factorial dependence from the original tail normalization and separates a known quadratic-character sign from the unresolved finite hypergeometric port `S_p`.

## Exact continuation

The unchanged frozen mother is original `Delta_p-R_p=0 modp` / `W_p=p modp^3` for target classes. The existing accepted first-digit statement and this theorem reduce the third-digit obligation to an explicit **lower-grade defect + signed `S_p/9` cancellation**. Seek a Fricke/Cartier source-preserving lower-grade transfer supplying exactly that signed coefficient; independently test any proposed map at p=13/19/373, retaining odd Green/Hesse source where present.

Highest native evidence debt [#1559](https://github.com/awdawmip/enterprise-math/issues/1559): p373 original-class H0/B0 divided-power `[X]U mod139129`, rank, Frobenius direction/eta, signed kappa and Delta-R with independent reproduction. `PENDING_OWNER / NOT_EXECUTED`.

Native Source at 2026-11-08 04:56 UTC: `STATUS_DATABASE_UNAVAILABLE`, original target request `onhour11-20261106-1400-exact-research-lane-continuation` not reissued. Site local `research_authority_granted=false`. Research lane `chatgpt-research-onhour-enterprise-math-20260923` (maintenance lane excluded). `REGISTER_PENDING`, no verified native session/claim/run/checkpoint; author-side result remains `UNREVIEWED / NOT_ADMITTED`.
