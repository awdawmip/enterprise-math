# P017 — P2 Current-State Synchronization

Status: `OWNER CHECKPOINT / PROVED_WIP + EXTERNAL-COMPUTATION CONDITIONAL FINITE SPLICE / NOT CANONICAL / NO ALL-K P2 CLAIM`

At: `2026-08-25T21:34:00+08:00`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Project main observed: `b8e66057cb5102f004d3718a4149636b1891ea7c`

Owner head before this checkpoint: `3af80119a0cde47eeaf9991307aebf84441655b1`

Owner-isolation note: the branch is intentionally not rebased or merged with moving `main`; current-main movement is unrelated control-plane work.

## Frozen mathematical state

1. The earlier constant-penalty high-prime detector was corrected. The exact root-normalized weight

   \[
   \omega_K(n)=1-\sum_{p<K+1,\,p\mid n}\nu_p(n)\left(1-\frac{\log p}{\log(K+1)}\right)
   \]

   satisfies

   \[
   \omega_K(n)>0\iff\Omega(n)\le2
   \]

   for every state in the consecutive-square basin.

2. For the P017 binary carry

   \[
   O_m(K)=H_m(K)-H_{2m}(K),
   \]

   the exact bridge

   \[
   O_m(K)-\frac Km=r_K(m)-r_K(2m)
   \]

   reduces the prime-lift carry remainder to the standard Chen short-interval floor remainder. The unresolved analytic object is therefore not a new sieve family.

3. Sub-root modulus support can be controlled absolutely but cannot cross the parity/square-root barrier. A genuine P2 proof requires a super-root bilinear remainder estimate.

4. The finite side has advanced independently. Under the conservative public exhaustive-gap premise

   \[
   0<x<10^{20}\Longrightarrow\exists\text{ prime }q\in(x,x+1724],
   \]

   the exact two-stage prime-gap bootstrap supplies a P2 for the continuous range

   \[
   1\le K\le116{,}009{,}280{,}740{,}973{,}308,
   \]

   after splicing with the declared finite prime verification. The corresponding analytic variable reaches

   \[
   X=K^2\approx1.3458153218\times10^{34}.
   \]

   The stronger confirmed-maximal-record interpretation is retained separately as Tier B and is not used by default.

## Current bottleneck

The route is no longer blocked on inventing a weight, identifying the carry, or extending the finite computation. The remaining question is effectivity:

> Can a Chen/Iwaniec–Laborde-type bilinear remainder theorem, specialized to interval length \(X^{1/2}\), be replayed with explicit constants and a threshold below the conservative finite splice \(X\approx1.3458\times10^{34}\)?

The published-weight reconstruction suggests only a shallow super-root level, near

\[
D=X^{0.52854\ldots}=K^{1.05708\ldots},
\]

but this remains diagnostic until the exact source constants and all admissibility inequalities are replayed.

## Next executable action

1. Recover the exact Iwaniec–Laborde parameter inequalities and source constants rather than extrapolating from rounded optimizer values.
2. Re-optimize at \(\theta=1/2\) under the full theorem hypotheses.
3. Convert every implicit asymptotic remainder into an explicit threshold ledger and compare it with the Tier-A splice.
4. In parallel, test whether the square-specialized numerator and shallow strip reduce the high-prime two-dimensional tail or the bilinear constant.

Hard block: `NONE`.
