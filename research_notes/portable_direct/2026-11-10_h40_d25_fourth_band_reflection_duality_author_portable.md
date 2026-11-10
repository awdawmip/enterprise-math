# D25/LIFT — exact low/high reflection duality for the fourth weighted p-adic band

Date: 2026-11-10. Role: TASK_RESEARCH, author-side portable evidence. Status: AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.

Frozen science: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, mother objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Predecessor-author evidence reused, not recredited: `research_notes/portable_direct/2026-11-10_h40_d25_weighted_fourth_band_p4_author_portable.md`, blob `806812e0a6e071fbb2e7fe57e2a30276d1e1aef5`.

## New theorem: pointwise fourth-band reflection

Let p>=13 be prime with p mod 24 in {13,19}, m=(p-1)/6, and a_k=(2k)!(3k)!/[216^k(k!)^5], with a_k treated as a rational p-local number. Then for *every* 1<=k<=2m, a_k is a p-unit, v_p(a_(p-k))=3, and

```math
a_{p-k}/p^3 = -1/(18 k^3 a_k)  (mod p).            (R)
```

Thus the **original labeled** weighted fourth-band correction obeys

```math
F_p := [sum_{j=4m+1}^{p-1} (6j+1)a_j]/p^3
    = sum_{k=1}^{2m} (6k-1)/(18 k^3 a_k)   (mod p).   (F-dual)
```

The high-band scalar F_p at precision p^4 is exactly reconstructed from low-band coefficients and original index labels using only operations in F_p.

## Proof

For j=p-k and 1<=k<=2m, Legendre's valuation formula gives v_p(a_j)=floor(2j/p)+floor(3j/p)=1+2=3, while v_p(a_k)=0. In F_p, Wilson's theorem gives

```math
(2j)!/p   = -(2j-p)!                 (mod p);
(3j)!/p^2 = 2(3j-2p)!               (mod p);
(p-2k)!   = 1/(2k-1)!               (mod p);
(p-3k)!   = (-1)^k/(3k-1)!          (mod p);
(p-k)!    = (-1)^k/(k-1)!           (mod p).
```

The two complete blocks in (3j)!/p^2 each contribute (p-1)! and the p-factor 2p gives 2. Fermat's theorem yields 216^{-j}=216^{k-1} (mod p), because p does not divide 216. Substitute into a_j:

```math
a_{p-k}/p^3
  = -2*216^{k-1}*((k-1)!)^5/[(2k-1)!(3k-1)!]
  = -2*(2k)*(3k)/(216*k^5*a_k)
  = -1/(18*k^3*a_k)                          (mod p).
```

Finally 6(p-k)+1=1-6k (mod p) and the high interval j=4m+1,...,p-1 is exactly the reflection of k=2m,...,1, establishing (F-dual). This argument is uniform over the stated prime class.

## Exact independent finite certificate

A standard-library Python integer verifier was executed for the complete set of **312** primes p<=10000 with p mod 24 in {13,19}. For all **491862** associated pairs (p,k), it reconstructed a_j from the original recurrence modulo p^4, checked p^3 divisibility and the pointwise law (R), checked the original weighted fourth-band sum against the reflected sum, and independently checked the residue via the preceding exact factorial formula for F_p. All comparisons succeeded.

Selected residues: F_13=5, F_19=4, F_37=26, F_43=30, F_61=15, F_157=96, F_373=278. The complete 312-row JSON certificate and runnable verifier are distributed in the author-side bundle `D25_WEIGHTED_FOURTH_BAND_REFLECTION_DUALITY_AUTHOR_PORTABLE_20261110.zip`, ZIP SHA-256 `56f4c371652d2529401a093594ccfe69929056fcb6932712b722ca99a3aff5e2`. The ZIP is a local deliverable unless separately published; its hash is byte identity, not a Source admission.

## Scientific relevance and next action

(R) is a BRC precision-specific, source-labeled residual reconstruction: after the declared p^{-3} operation followed by reduction mod p, fourth-band information is equivalent to a reciprocal low-band expression. This provides a concrete inverse-hypergeometric sequence for a finite contiguous/telescoping ansatz toward the still-open uniform W_p = p (mod p^3) objective; check any candidate identity with exact original coefficients and explicit k-domain before promoting a claim. The original-class H0/B0 and native Frobenius direction remain a separate exact-source task.

Native Source task writing/review requires a current issued session and winning CLAIM; this note does not assert either. The UR V2 historical original bundle (94687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) still requires original-byte restoration before writer/provenance repair; its already completed mathematics is unchanged.
