# CIRCULARITY_AUDIT

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`

## Scan rule

A node is circular if closing it requires a statement equivalent to the desired conclusion, or if the proof silently replaces the full zero set by the critical-line zero set before RH has been proved.

## Candidate A — Claude V6

### Spectral determinant target

\[
\det_\zeta(L^2_{\Phi,K}^{reg}-(z^2+1/4))=C\,\Xi(z)
\]

is **not circular merely because it would imply RH**. It would be a legitimate bridge if proved independently with domain, regularization, zero/pole, multiplicity and completeness control.

Status: `OPEN_BRIDGE`, not counted as circular.

### Direct spectral bijection

Any statement of the form
`Spec(H) = {gamma_n^2+1/4 : zeta(1/2+i gamma_n)=0}` only controls the zeros already known on the line unless the RHS is independently proved to exhaust all nontrivial zeros. Exact exhaustion is the load-bearing content.

Status: `SPECTRAL_BRIDGE_GAP`.

## Candidate B — Gershon

### Remark 19

The paper explicitly notes that an increasing-modulus critical-line zero ordering used to infer positive growth already assumes critical-line reality. This is correctly self-identified by the source as non-independent evidence.

Status: `CIRCULARITY`.

### Lemma 11

The reciprocal-coefficient expansion is written using
\(\rho_m=-1/t_m^2\) and then the `n` smallest Riemann zeros as the dominant poles. This is legitimate only if the full pole set relevant to `1/g` is exactly that real sequence, or if all omitted complex poles are independently excluded. That exclusion is RH-level information.

Status: `CIRCULARITY_OR_MISSING_COMPLEX_ZERO_CONTROL`.

### TP2 vs TP∞

The manuscript correctly states early that TP2/log-concavity is necessary, not sufficient. Any inference `TP2 ⇒ RH` is rejected. Its later claimed closure must stand entirely on the higher-order universal determinant lemmas, which fail independently at Lemma 10.

Status: `NECESSARY_NOT_SUFFICIENT` for TP2 alone.

## Candidate C — Yamaguchi

The proof writes the Hadamard product for
\(F(z)=\xi(1/2+iz)\) as a product over real numbers `±gamma_k`, obtained by “pairing zeros at 1/2 ± i gamma_k”.

Without RH, a zero \(\rho=\beta+i\gamma\) of \(\xi\) yields

\[
z=-i(\rho-1/2)=\gamma-i(\beta-1/2),
\]

which is real iff \(\beta=1/2\).

Hence the claimed real-zero factorization is equivalent to the conclusion being sought. The same hidden assumption is repeated in the logarithmic-derivative formula and in the removable-pole argument.

Status: `CIRCULARITY`.

## Candidate D — CIPHER negative control

The bridge equation reduces to a functional-equation identity at zeros. A tautology cannot supply the missing spectral constraint.

Status: `CIRCULARITY / TAUTOLOGY`, correctly detected.

## Audit verdict

No candidate-specific full RH chain survives the circularity scan.

The most important distinction is:

- a hard theorem that *would imply* RH is not automatically circular;
- a proof of that theorem that already parameterizes **all** zeros as critical-line zeros is circular.

Candidate A has an **open legitimate bridge**; Candidate C has a **circular attempted bridge**.
