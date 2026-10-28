# D25/LIFT: exact Clausen square modulo p² and a source-preserving third-digit cutoff defect

Research date: **2026-10-29 Asia/Hong_Kong**. Status: **AUTHOR-SIDE / PROVED CONDITIONAL ALGEBRAIC REDUCTION / EXECUTED EXACT INTEGER CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_H0_B0_NOT_EXECUTED**.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Original task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. **Immutable scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`**. This author-side research note changes neither the Source task nor its owner, Result or scientific acceptance status. The Research execution lane is `chatgpt-research-onhour-enterprise-math-20260923`; maintenance is distinct.

## 1. Original object and independently sourced exact identity

For any prime `p=6m+1>3`, work coefficientwise in `Z_(p)`, and define

\[
a_n=\frac{(1/3)_n(1/2)_n(2/3)_n}{(n!)^3},\qquad
b_n=\frac{(1/6)_n(1/3)_n}{(n!)^2}.
\]

Let `F_p(z)=Σ_{n=0}^{p-1} a_n z^n` and `H_p(z)=Σ_{n=0}^{2m} b_n z^n`. Both are original finite polynomials with denominators invertible for the displayed coefficient range. The *original* 216 weighted object is exactly

\[
A_p=\big[(1+6\theta)F_p(z)\big]_{z=1/2},\qquad \theta=z\frac{d}{dz},
\]
because `a_n 2^{-n}=binom(2n,n)^2 binom(3n,n)/216^n`. We preserve that cutoff, weight and full coefficient provenance.

Clausen's classical identity (NIST DLMF 16.12.2, specialized at `a=1/6,b=1/3`) gives the **formal power series identity over Q**:

\[
\left(\sum_{n\ge0}b_n z^n\right)^2=\sum_{n\ge0}a_n z^n.
\]

This is **classical prior art**, not claimed as a new hypergeometric identity: https://dlmf.nist.gov/16.12.E2 .

## 2. Theorem: exact full polynomial square modulo p²

For **every** prime `p=6m+1>3`,

\[
\boxed{F_p(z)\equiv H_p(z)^2\pmod{p^2}\quad\text{in }(\mathbb Z/p^2\mathbb Z)[z].}
\tag{T1}
\]

Proof: for every `0<=n<p`, `n!` is a p-unit. In `b_n`, the `(1/6)_n` factor first contains p at `n=m+1`, while `(1/3)_n` first contains p at `n=2m+1`. Thus `v_p(b_n)>=2` whenever `2m+1<=n<p`. In `a_n`, the three numerator factors first acquire p at indices `2m+1,3m+1,4m+1` respectively (corresponding to `1/3,1/2,2/3`), so `v_p(a_n)>=3` for `4m+1<=n<p`. Exact Clausen coefficient equality therefore implies that **every coefficient of degree <p** in `F_p-H_p^2` is divisible by `p²`. The degree of `H_p²` is `4m<p`, so these exhaust both polynomials. No asymptotic limit or numerical fitting is used.

This is a squared *full polynomial* congruence, stronger than an identity at a single `z`, but it is precisely scoped to p².

## 3. Theorem: uniform sharp obstruction and complete third-digit repair

The first omitted coefficient occurs at `n=2m+1`; Clausen coefficient equality gives

\[
[z^{2m+1}](F_p-H_p^2)=2b_{2m+1}.
\]

Exactly two p factors occur in `b_{2m+1}`, once from `6m+1=p` and once from `3(2m)+1=p`. Hence

\[
\boxed{v_p\big([z^{2m+1}](F_p-H_p^2)\big)=2.}
\tag{T2}
\]

Consequently (T1) **cannot** generally be upgraded to a full polynomial congruence modulo p³, for any such prime; no finite counterexample search is needed.

The failure at the third digit can nevertheless be reconstructed **exactly**. Define the typed high-parameter-source coefficients

\[
g_i=\binom mi\binom{2m}i\pmod p\quad(0\le i\le m),\qquad
q_j=\frac{b_j}{p^2}\pmod p\quad(2m+1\le j<p),
\]
with `G_p(z)=Σ_{i=0}^m g_i z^i` and `J_p(z)=Σ_{j=2m+1}^{p-1}q_j z^j`. The division by `p²` is exact in `Z_(p)`; all remaining denominator factors are units. Write `Π_<p` for deletion of *only* terms with degree `>=p` while retaining the original source-tagged coefficient pairs. Then

\[
\boxed{F_p(z)\equiv H_p(z)^2+2p^2\Pi_{<p}\big(G_p(z)J_p(z)\big)\pmod{p^3}.}
\tag{T3}
\]

Proof: truncate the exact companion series at degree `p−1`, write its tail beyond `2m` as `p² J_p` modulo `p³`, expand its square, reduce `H_p\bmod p=G_p`, and apply coefficientwise Clausen for every degree `<p`. This derivation leaves out no boundary terms and does not identify the degree truncation with evaluation.

## 4. Conditional supersingular-point consequence; nonlocal boundary witness

For any `z_0\in\mathbb F_p\setminus\{0,1\}` with `G_p(z_0)=0`, the full product `G_p(z_0)J_p(z_0)=0`, but its degree truncation need not vanish. Define the **over-cutoff pair observer**

\[
E_p(z_0)=\sum_{\substack{0\le i\le m,\,2m+1\le j<p\\i+j\ge p}}
g_iq_j z_0^{i+j}.
\]

The original unweighted third-digit residual obeys the exact identity

\[
\boxed{\frac{F_p(z_0)-H_p(z_0)^2}{p^2}\equiv-2E_p(z_0)\pmod p.}
\tag{T4}
\]

For the *original weighted operator* `1+6θ`, define `E_p^{(6)}(z_0)` by multiplying each source-pair summand above by `1+6(i+j)`. Then

\[
\boxed{\frac{[(1+6\theta)(F_p-H_p^2)](z_0)}{p^2}\equiv
12(\theta G_p)(z_0)J_p(z_0)-2E_p^{(6)}(z_0)\pmod p.}
\tag{T5}
\]

For the frozen target classes `p≡13,19 (mod24)`, the `G_p(1/2)=0` condition is checked by the finite certificate below; a **uniform** application of T4/T5 requires the corresponding independently established original-class CM/Hasse root theorem. This note does not promote the finite checks into such a theorem.

**Additional algebraic root fact.** `G_p={}_2F_1(-m,-2m;1;z)` satisfies `z(1-z)G''+[1+(3m-1)z]G'-2m²G=0` in `F_p[z]`. A root at `z_0\notin\{0,1\}` is simple: a hypothetical multiplicity `2<=r<=m<p` would leave the nonzero lowest-order term `z_0(1-z_0)r(r-1)`. Thus at a verified such root `F_p\bmod p=G_p^2` has *exact double* zero and `[(1+6θ)F_p]\bmod p` has a *simple* zero; their sensitivities to a p-adic input perturbation differ.

## 5. Executed reproducible integer evidence

Actually executed Python standard-library-only guard: `research_notes/portable_direct/d25_clausen_p2_square_guard_20261029.py`, committed and immutably read back at Git commit `71ef78af4a3680eadc9de2eaf1496178063c26d8`, Git blob `997c1dca7fc9dc68d3f98199fd0d572ea41fe1a0`. The checker tests **all 67 primes** `7<=p<800, p≡1 mod6` coefficientwise modulo p² and the entire T3 defect modulo p³. Original binomial formulas independently check weighted sums for seven selected primes. All assertions passed:

```text
PASS_D25_CLAUSEN_P2_POLYNOMIAL 67 primes 7<=p<800; coefficientwise mod p^2; exact first p^3 obstruction
P373: first missing coefficient at n=125 = 138*373^2 mod 373^3; H(1/2) mod p^2=8952; theta_H mod p=294; weighted_A mod p^3=373
P373: unweighted defect/tail=241/66; weighted defect/overflow=1/98; J(1/2)=252
```

For fixed `p=373, m=62`, the first missing coefficient has `(2b_125)/373² ≡138 (mod373)`; the **unweighted** third-digit defect is `241≡−2·66 (mod373)`, carried by the actual `i+j>=373` source pairs. The **weighted** defect is

\[
1\equiv12\cdot294\cdot252-2\cdot98\pmod{373}.
\]

Here `H_p(1/2)≡8952=24·373 (mod373²)` and `\theta H_p(1/2)≡294 (mod373)`; hence the weighted first p-adic digit is `12·24·294≡1 (mod373)`, consistent with the **independent original-binomial** `A_{373}≡373 (mod373³)`. The latter is a finite observation, not a universal A/B bridge proof.

**BRC / observer typing:** the carrier is the finite pair family `(p,i,j,g_i,q_j)` with original coefficient source and p-adic valuation; the observer is either the full unweighted scalar or the weighted `1+6θ` readout. The permitted future operation is degree truncation `Π_<p` before evaluation at `z=1/2`. Replacing it by evaluation before truncation loses the exact boundary residual. This is an *external finite-ring calculation*, not an X6 native geometry theorem or a native BRC-H0/B0 run; the project's P000 remains intact.

## 6. Exact remaining obligations / recovery packet

1. **Highest native acceptance gap:** existing [support #1559](https://github.com/awdawmip/enterprise-math/issues/1559), as of the 2026-10-29 read OPEN and PENDING_OWNER. An actually authorized original-class executor must compute the **same original H0/B0 divided-power** `[X]U mod 139129`, actual module rank, semilinear Frobenius direction/normalization, signed odd Green/Hesse, original κ and Δ−R, raw source/code/version, then independent review. None was executed in this author-side unit.
2. **Smallest unresolved mathematical unit:** use T3/T5 **with the full `Π_<p` cutoff and original weight** to construct a prime-sensitive identity linking this exact third-digit companion boundary correction to the preexisting 2304 half-cut comparison; target the original `A_p≡B_p (modp³)` for `p≡13,19 (mod24)`. In particular calculate and transport `E_p^{(6)}` without deleting it under the CM root; do not re-run the old 781-prime search, composite-length falsifiers, or completed 216 reflection lemmas.
3. **Source lifecycle / identity:** GitHub artifacts here are author-side, **UNREVIEWED / NOT_ADMITTED**. No Research-Activity registration, winning CLAIM, open run, formal Source checkpoint, Result or review is asserted. Research logical conversation `chatgpt-research-onhour-enterprise-math-20260923` only; maintenance lane is not used. Historical own recovery #6575 shows a session pointer and no Source-winning run; old dispatch #6576 ended `FAILED/TimeoutExpired`; no duplicate reissue. Gateway `0.6.11` read on 2026-10-29 showed Researcher writes ungranted, `write_relay_enabled=false`, quota 5/5. Recover through original requests and current canonical Source once an actually authorized route is available; do not invent an authorization or rebase the frozen scientific source pin.

**Proof-strength and novelty boundary:** Clausen is classical; T1–T5 follow by explicit p-adic valuation and **source-preserving truncation** in the current D25 application, as proved here. The numerical CM roots and universal 216/2304 p³ bridge remain in their respective evidence classes. Project note publication constitutes evidence preservation, not native experiment or theorem admission.
