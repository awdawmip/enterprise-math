# D25/LIFT — exact even-harmonic factorization and eighth-digit source-labeled Frobenius seam

2026-10-25 | `TASK_RESEARCH` | AUTHOR PROOF + EXACT AUTHOR-SIDE COMPUTATION | `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT` | `NONBLIND`.

## Provenance and immutable scope

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source: `c47e13e4aba0e006366f989d6334d443f6333ae3`. A later control/main commit does not repin that Source.

Inherited, without new contribution credit: original WZ/factorial five-port identity, the source factor all-precision jet, and the modulo-`p^6` and `p^7` compressed seam. The source-exposed seventh-digit result already exists in `research_notes/portable_direct/20261025_driver_context_d25_p7_nonlinear_frobenius_seam_nonblind.md`. This note supplies a different, new eighth-digit consequence and an exact even-harmonic product identity for its binomial observer. This is external p-adic arithmetic; the same-prime same-original-class H0/B0/CM/DP correspondence remains **unproved**.

For any prime `p=6m+1 >=13`, all source factors take values in `Z_(p)` and we retain **both** the old edge and the four labeled genuine tails:

\[
Q_p(z)=T_p(z)^2\bigl(R_p(z)^2 A_p(z)+L_p(z)\bigr),\quad H_p(z)=A_p(z)+L_p(z),
\]
\[
T_p(z)=\prod_{j=1}^{p-1}(1+z/j),\quad R_p(z)=(1-z)/(1+z/(p-1)),
\]
\[
A_p(z)=2m C(z)K_U(z),\quad L_p(z)=\frac{3z}{220}B(z)P_{\rm base}(z).
\]

The exact `C,K_U,B,P_base`, with all true port labels and all p-unit denominators, are fixed by `research_notes/portable_direct/20261025_offphase_d25_source_factor_jet_all_precision.md`. Set `a_i=[z^i]A_p(z)`, `ell_i=[z^i]L_p(z)`; `ell_0=0`.

## New observation: exact even-harmonic compression before any p-adic truncation

The finite permutation `j -> p-j` gives the **rational equality**

\[
\prod_{j=1}^{p-1}(1-p/j)=\prod_{j=1}^{p-1}(j-p)/j=(-1)^{p-1}=1.
\]

Consequently, **not merely modulo a power of p**, 

\[
\boxed{T_p(p)=\binom{2p-1}{p-1}=\prod_{j=1}^{p-1}\left(1-\frac{p^2}{j^2}\right).}
\]

In `Z_p` the factors on the right lie in `1+p^2 Z_p`, so logarithms are valid. Writing `h_r=\sum_{j=1}^{p-1}j^{-r}` obtains an **exact convergent identity**

\[
\boxed{\log T_p(p)=-\sum_{k\ge1}\frac{p^{2k}}k h_{2k}.}
\]

This eliminates the need to redo odd-harmonic pairing for each precision. For the target primes, `h_2,h_4,h_6` are divisible by `p`: finite-field power-sum vanishing holds because `p-1` divides none of `2,4,6`. Define the p-integral observers

\[
\Theta=h_2/p,\qquad\Omega=h_4/p,\qquad\Xi=h_6/p.
\]

For `p>=13`, terms `k>=4` have valuation `>=8` (indeed the `k=4` term even has valuation `>=9`), so

\[
2\log T_p(p)\equiv-2p^3\Theta-p^5\Omega-\tfrac23p^7\Xi\pmod{p^8}.
\]

Only the square of the leading logarithmic term contributes nonlinearly before the eighth digit; hence

\[
\boxed{T_p(p)^2\equiv1-2p^3\Theta-p^5\Omega+2p^6\Theta^2-\tfrac23p^7\Xi\pmod{p^8}.}
\]

The other observer factor is exact:

\[
R_p(p)^2=(1-p)^4/(1-2p)^2
\equiv1+2p^2+4p^3+9p^4+20p^5+44p^6+96p^7\pmod{p^8}.
\]

For all degrees `d>=3`, its rational generating coefficient has the compact closed form `[z^d](1-z)^4(1-2z)^{-2}=(d+5)2^{d-4}`. The new seventh-degree coefficient is `96`.

## Theorem: complete eighth-digit source-labeled seam

Let `D_p=Q_p(p)-H_p(p)`; inherited original-source proof gives

\[
D_p=\bigl(T_p(p)^2R_p(p)^2-1\bigr)A_p(p)+\bigl(T_p(p)^2-1\bigr)L_p(p)
\]

as an **exact equality**. Define the already-established lower-degree expression, **evaluated using sufficiently precise p-adic coefficients rather than arbitrarily lifted residues modulo `p^7`**, by

\[
\begin{aligned}
\mathcal D_{<7}:={}&p^2(2a_0)
+p^3\{2a_1+(4-2\Theta)a_0\}\\
&+p^4\{2a_2+(4-2\Theta)a_1+9a_0-2\Theta\ell_1\}\\
&+p^5\{2a_3+(4-2\Theta)a_2+9a_1+(20-4\Theta-\Omega)a_0-2\Theta\ell_2\}\\
&+p^6\{2a_4+(4-2\Theta)a_3+9a_2+(20-4\Theta-\Omega)a_1\\
&\hspace{32mm}+(44-8\Theta+2\Theta^2)a_0-2\Theta\ell_3-\Omega\ell_1\}.
\end{aligned}
\]

**For all primes `p=6m+1>=13`:**

\[
\boxed{\begin{aligned}
D_p\equiv \mathcal D_{<7}+p^7\Bigl[&2a_5+(4-2\Theta)a_4+9a_3
 +(20-4\Theta-\Omega)a_2\\
&+(44-8\Theta+2\Theta^2)a_1
 +(96-18\Theta-2\Omega-\tfrac23\Xi)a_0\\
&-2\Theta\ell_4-\Omega\ell_2+2\Theta^2\ell_1\Bigr]\pmod{p^8}.
\end{aligned}}
\]

**Proof.** Multiplying the two displayed binomial/edge factors gives the new coefficient
`[p^7](T^2R^2-1)=96-18Theta-2Omega-(2/3)Xi`, while the lower coefficients through degree six are precisely those in `D_<7`. Multiplication by `A_p(p)=a_0+a_1p+...+a_5p^5+O(p^6)` contributes only these terms modulo `p^8` because `T^2R^2-1` begins in degree two. Similarly, `T^2-1` begins in degree three and `L_p(p)=ell_1p+...+ell_4p^4+O(p^5)`, so its newly exposed degree-seven contribution is `-2Theta ell_4 - Omega ell_2 + 2Theta^2 ell_1`. All discarded terms have p-valuation at least eight; coefficients are p-integral. QED.

**Information-loss interpretation.** The old edge first observes `Xi` at this precision; the genuine four-tail discrepancy first contains a term **quadratic** in `Theta`, namely `2Theta^2 ell_1`. Neither is visible from the scalar compressed observer without restoration coordinates. BRC method resolution: `COMPOSE_APPLIED` to source-labeled p-valuations and coefficient jets. No positive-mass/phase cancellation, native physical transfer, or clean-blind review is inferred.

## Exact author-side verification

Companion program `d25_p8_seam_checker.py` uses only the Python standard library and integer rings modulo `p^8`. It reconstructs (1) the full source old-edge `p-2` factor and the genuine four-tail rational transfer at `z=p` and (2) the independent truncated polynomial jets to degree five; separately verifies the exact even-factor product `T=prod(1-p^2/j^2)`, the binomial harmonic prediction, the exact old-edge factorization and the p^8 seam. A degree-five jet is only required to agree with the original *uncompressed* values modulo `p^6`; it is **not** incorrectly promoted to equality modulo `p^8`.

**Executed: PASS 206/206** for all primes `13<=p<3000`, `p=1 (mod 6)`. Sample residues are exact:

| p | `D_p (mod p^8)` | `Xi (mod p)` | new old-edge coefficient `(mod p)` | new genuine-tail coefficient `(mod p)` |
|---:|---:|---:|---:|---:|
| 13 | 55,952,689 | 4 | 6 | 6 |
| 19 | 1,292,878,541 | 1 | 11 | 6 |
| 31 | 649,998,887,054 | 12 | 25 | 30 |
| 37 | 1,734,449,525,770 | 7 | 18 | 30 |
| 109 | 1,528,353,903,123,609 | 25 | 88 | 9 |

This is author-side exact finite checking of the source-factor mathematics, not independent Driver evaluation, source-native runtime evidence, an uncollapsed W(r,t) reconstruction, or all-prime computational proof. Universal algebraic statements above are proved from the inherited exact source identity and the displayed rational/p-adic manipulations.

## Recovery and exact next action

Fresh account-main snapshot observed at `e374f213cc834049f52f37127a035539ae14ff4d`, current EM main before publication at `f1f7d85354df2f03c2eba1ecdab165374dab3c6b`; the frozen scientific Source remains `c47e13e4aba0e006366f989d6334d443f6333ae3`. The current Site-bound interface reports `static_machine_readonly` / `write_relay_enabled=false` / `research_authority_granted=false`; own-client checkpoint read returned `ACCESS_DENIED` and exposed tools provide no `recovery_status`. No own service session, claim, run, or native Source checkpoint is asserted.

Already-existing `p^7` mathematics and prior `p^6` are not reclaimed as this author's discoveries. Source-native formal continuation, writer/provenance and independent admission remain pending. UR V2 original four-file bundle (historical 94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) was not located in current main code-search, the accessible current Library D25 folder or targeted Google Drive file-name search; a negative *bounded search* is not proof of nonexistence. Do not reconstruct and relabel the prior completed UR mathematics.

**Next legitimate owner action:** after obtaining own true `recovery_status`/original request receipts and Source exact continuation with winning claim, attach the already-published portable evidence to the correct task provenance and native checkpoint, then secure independent review; if the current task is assigned elsewhere, do not claim its ownership. Next mathematical unresolved unit remains the same-prime, same-original-class CM/DP representative/semilinear second-digit correspondence, not further isolated p-adic jet arithmetic. No new scheduler, hosted cron or review identity is created.