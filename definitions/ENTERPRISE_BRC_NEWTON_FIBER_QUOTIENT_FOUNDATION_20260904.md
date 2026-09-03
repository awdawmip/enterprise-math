# Enterprise BRC Newton Fiber-Sum Quotient Foundation Addendum

**Effective:** 2026-09-04  
**Status:** CANDIDATE FOUNDATION BACKFLOW pending dedicated CI  
**Parent:** `ENTERPRISE_BRC_NEWTON_HANDOFF_RESONANCE_FOUNDATION_20260904.md` (`WBRC-T55`)

This addendum transports the main-backed result of PR #1196 into the all-research Weighted-BRC Foundation.  It gives the exact observer-safe provenance quotient after one fixed Newton affine pushforward.  It does not change T6's finite deterministic operation-quotient executable and does not claim minimality for weaker observer contracts such as edge-only observation.

## WBRC-T56 — Newton residual fiber-sum operation-safe quotient

Fix a finite source Taylor position set \(I\).  For every \(i\in I\), fix:

- source Newton scale \(\sigma_i\in\mathcal S_{\rm rad}\);
- Taylor degree \(k_i\ge0\);
- a shared selected-root multiplicity \(r\);
- a shared Newton scale \(\theta\in\mathcal S_{\rm rad}\).

For a rational coefficient state

\[
A=(a_i)_{i\in I}\in\mathbb Q^I,
\]

define

\[
\rho_i=\sigma_i\theta^{k_i-r},
\qquad
c_i=(\rho_i,k_i).
\]

Let \(C=\{c_i:i\in I\}\).  Define the fiber-sum observation

\[
\Pi:\mathbb Q^I\to\mathbb Q^C,
\qquad
\Pi(A)_c=\sum_{i:c_i=c}a_i.
\]

The complete residual Newton jet is exactly the family of residual polynomials

\[
Q_\rho(y)=\sum_k\Pi(A)_{(\rho,k)}y^k.
\]

Therefore for source states \(A,B\):

\[
\boxed{
A\text{ and }B\text{ have identical complete residual Newton jets}
\iff
\Pi(A)=\Pi(B).
}
\]

### Kernel transfer basis

For each fiber \(F_c=\{i:c_i=c\}\), choose an anchor \(i_c\).  Then

\[
\boxed{
\ker\Pi
=
\operatorname{span}_{\mathbb Q}
\{e_j-e_{i_c}:c\in C,\ j\in F_c\setminus\{i_c\}\}.
}
\]

Hence

\[
\operatorname{rank}\Pi=|C|,
\qquad
\dim\ker\Pi=|I|-|C|,
\]

and the first isomorphism theorem gives

\[
\boxed{
\mathbb Q^I/\ker\Pi\cong\mathbb Q^C.
}
\]

The only source-level freedom forgotten by the complete residual Newton observer is rational coefficient redistribution among provenance labels that have the same residual scale **and** the same Taylor degree.

### Coarsest full-residual observer-safe quotient

Any equivalence relation that preserves the **complete residual Newton jet** must refine equality under \(\Pi\), because every coordinate

\[
O_{\rho,k}(A)=\Pi(A)_{(\rho,k)}
\]

is itself a declared residual-jet observation.  Equality under \(\Pi\) is sufficient for every deterministic downstream operation whose input is only the residual jet.  Thus equality modulo \(\ker\Pi\) is the coarsest exact quotient for the full-residual observer and all future operations that factor through it.

This includes, when their typed domain conditions hold:

- semantic-zero elimination;
- residual-scale ordering;
- scale-one edge extraction;
- contact-order and root analysis;
- later rational or selected-root Newton steps;
- deterministic compositions of these operations.

### Coordinates that must remain distinct

The quotient key is exactly

\[
\boxed{(\rho,k)}.
\]

Different residual scales cannot merge: the residual scale spectrum and later scale ordering distinguish them.  The same residual scale at different Taylor degrees cannot merge: the residual polynomial/contact structure distinguishes the degrees.

### Source splitting and relabeling

One source coefficient may be split among any number of labels inside one \((\rho,k)\) fiber as long as the sum is unchanged.  Source labels and enumeration order are invisible after \(\Pi\).

This is a quotient of algebraic Taylor/characteristic provenance, not a statement that explicit positive branch provenance before determinant compression is recoverable or discardable.

### Main-backed evidence

PR #1196 dedicated exact gate:

- source positions = 7;
- residual coordinates / observer rank = 5;
- kernel dimension = 2;
- 10 exact anchor-transfer decomposition checks;
- 200 transfer-invariance checks;
- 75 downstream Newton-future checks;
- 11 coordinate-probe / no-merge checks;
- splitting/relabeling, edge-only boundary and production provenance-split witnesses PASS.

## Negative boundaries

### WBRC-N48 — full-residual minimality is observer-specific

The theorem is not minimal for a weaker observer.  An edge-only observer can ignore all current \(\rho<1\) fibers and admits a strictly coarser quotient.

### WBRC-N49 — residual quotient does not recover source provenance

Once source coefficients have been aggregated inside one \((\rho,k)\) fiber, the residual state does not identify the original labels or splitting.

### WBRC-N50 — different residual scales do not merge

Even at the same Taylor degree, distinct \(\rho\) coordinates remain distinguishable and may change later scale ordering.

### WBRC-N51 — different Taylor degrees do not merge

Even at the same residual scale, distinct Taylor degrees remain distinct polynomial/contact coordinates.

### WBRC-N52 — algebraic coefficient cancellation is not signed branch mass cancellation

Opposite Taylor/characteristic coefficients can cancel inside a fiber after algebraic compression.  This does not add signed/amplitude semantics to the positive branch carrier.

### WBRC-N53 — T6 principle reuse is not T6 executable reuse

T6 `operation_quotient.py` handles finite set states and deterministic endomaps.  WBRC-T56 is a finite rational linear fiber-sum quotient.  The future-observation principle is reused, but the existing T6 executable is not claimed to compute this quotient.

## Prior-art / novelty boundary

Kernels, quotient vector spaces and the first isomorphism theorem are classical linear algebra.  No generic novelty is claimed.  The Enterprise result is the typed Newton observer identification, the exact safe provenance boundary, and its integration with the T6 operation-safe quotient principle.
