# D25 / SECOND-DIGIT-LIFT — 216/2304 signed-observer p^4 bridge (finite candidate)

2026-10-29, onhour Research lane `chatgpt-research-onhour-enterprise-math-20260923`.
AUTHOR-SIDE / EXECUTED / FINITE_CANDIDATE / UNREVIEWED / NOT_ADMITTED.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged. No claim/session/open/Source Result asserted.

## Original signed finite observers, integer meaning

For primes p>3 define in Z_(p), with exact cutoff n=0,...,p-1,

[
 A_p=sum_{n=0}^{p-1}(6n+1)rac{inom{2n}{n}^2inom{3n}{n}}{216^n},
 qquad
 B_p=sum_{n=0}^{p-1}(8n+1)rac{inom{2n}{n}^2inom{4n}{2n}}{2304^n}.
]

Set chi_p=(-3/p), equal to +1 for p=1 mod 3 and -1 for p=2 mod 3. Both denominators are p-units for p>3. Distinct index, weight, cutoff and valuation-port sources are preserved before comparing the *final scalar observation*; the BRC carrier is the labelled signed 216 and 2304 streams and exact quotient ring Z/p^4, not positive branch mass.

### New finite candidate, NOT a theorem

[
oxed{A_p-2B_p+pchi_pstackrel{?}{equiv}0pmod{p^4},quad p>3.}	ag{C1}
]

Equivalently, *if* the already proved B congruence applies, the third digit defects obey

[
 alpha_p:=(A_p-pchi_p)/p^3,quad
 eta_p:=(B_p-pchi_p)/p^3,
 qquad alpha_pstackrel{?}{equiv}2eta_ppmod p.
	ag{C2}
]

The divisions in C2 are justified by the externally proved B theorem and, for A, only by the explicitly reported finite check (until the open A theorem is established). C1 avoids assuming A's integrality quotient globally and is the mathematically primary candidate. At precision p^3, (C1) would imply A_p=B_p=p chi_p mod p^3; this is a potential shorter attack on the frozen five-port equation, not a completed proof.

## Established external theorem; attribution and exact distinction

Victor J. W. Guo and Wadim Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019) 329–358, arXiv:1803.01830v6, Introduction (2), Theorem 1.1:
https://arxiv.org/html/1803.01830v6

Their *proved* result is exactly `B_p=p chi_p (mod p^3)` for all p>3, with the **8n+1, 2304** summand and a second half-truncation result. Their paper does NOT thereby prove C1 or the **6n+1, 216** target: these have different coefficients and signed observers. Do not cite their B theorem as a proof of A or silently identify the two distributions.

Thus the original frozen A target (on p=13,19 mod 24) is *equivalent, using the external theorem*, to the still-open `A_p-B_p=0 (mod p^3)`. The already-recorded D25 finite Clausen low/high source conservation is the exact internal interface for analyzing this defect, not a discarded port identity. C1 predicts a stronger relation across all p>3, not a replacement for the original native benchmark.

## Executed evidence and precision sharpness

The companion exact Python guard uses the *two different coefficient recurrences*
[
a_n/a_{n-1}=rac{(2n-1)(3n-2)(3n-1)}{36n^3},quad
b_n/b_{n-1}=rac{(2n-1)(4n-3)(4n-1)}{288n^3},
]
only for 1<=n<p so every modular denominator is invertible.
It executed all 237 primes 5<=p<1500. ALL satisfied A_p-B_p=0 mod p^3 and C1 mod p^4. The exact raw binomial factorial route independently matched both streams mod p^5 for p=13,19,373.

| p | chi_p | alpha_p mod p | beta_p mod p | (A_p-2B_p+p chi_p)/p^4 mod p |
|---:|---:|---:|---:|---:|
| 11 | -1 | 2 | 1 | 5 |
| 13 | +1 | 9 | 11 | 9 |
| 19 | +1 | 12 | 6 | 14 |
| 373 | +1 | 228 | 114 | 174 |

The last column is a **p^5 defect**, not a contradiction to C1. In particular p=13 already proves C1 cannot simply be strengthened to p^5; the exact quotient is 9 mod 13. For p=373 the raw residues are A mod p^4=11832087049, B mod p^4=5916043711, and 228=2*114 mod 373.

Code: `research_notes/portable_direct/d25_A216_B2304_p4_character_bridge_guard_20261029.py`.
Observed PASS: `PASS_AB_P3_THEOREM_CONSISTENCY_AND_P4_BRIDGE 237 primes < 1500`; raw-binomial checks: PASS for 13,19,373. Local executed code SHA256 `f95deee8f4368ac724e66bd3b65e208fc68369b28e5c75a414f35ff8a48ca017`. Finite domain and exact modular arithmetic give a finite certificate, not an all-prime theorem.

## Current scientific frontier and authority

Next discriminating step: produce or falsify an all-prime finite WZ / hypergeometric / CM transformation certificate for C1 (or its weaker p^3 A-B consequence) *preserving the two original signed streams and their low/high cutoff sources*. Compose it with Guo–Zudilin's B theorem and map the resulting A-B cancellation to the frozen five ports T00+T01+T02+T10+T11=p-p^2 Theta_p (mod p^3) for p=13,19 mod 24. Do not relabel finite verification as proof.

The separate highest-priority native H0/B0 fixed p=373 divided-power [X]U modulo 139129, rank, actual semilinear Frobenius, signed Green/Hesse, kappa and independent acceptance remain NOT_EXECUTED by this scalar unit. See support #1559, which has no confirmed executor at this author's latest direct read. Native execution does not follow from BRC analogy or from a p-adic scalar identity.

This note and companion code are author-side GitHub evidence only; the Site on 2026-10-29 was static read-only for this subject, with research_authority_granted=false; REGISTER_PENDING / SYNC_DEBT. No canonical claim, continuation checkpoint, Result, independent review, or task completion is asserted.
