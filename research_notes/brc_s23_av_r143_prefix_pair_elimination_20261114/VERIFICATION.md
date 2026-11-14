# R143 exact verification record

Local execution date: 2026-11-14 (Asia/Shanghai).
Command: \`python check_r143.py\`.
Arithmetic: Python \`int\` (arbitrary precision), \`fractions.Fraction\`, exact integer floor; no floating-point thresholds or external dependencies.

Observed stdout:

\`\`\`json
{
  "status": "R143_PREFIX_INTEGER_ELIMINATION_PASS",
  "fully_exhaustive_memberships": 24528,
  "K1_memberships": 1022,
  "large_K_positive_witnesses": 1200,
  "boundary_word_checks": 2228,
  "saturation_cases": 9
}
\`\`\`

## Independence and completeness of finite checking

For each K=2,...,25 and m=1,...,9, compute every *actual* parameter breakpoint r/n (0<r<n), for each n=K-1,...,K+m-1, including non-reduced numerators. Evaluate the original floor differences at every event and an exact midpoint between consecutive events. Since each constituent floor is constant between these breakpoints and right-continuous at events, this enumerates the complete finite set V(K,m), not a sample. Independently enumerate every one of the 2^m binary words and compare its membership with the new prefix-pair algorithm. Total: 24*(2^1+...+2^9)=24,528 queries. The K=1 case is checked analogously: 2^1+...+2^9=1,022 queries.

For larger coefficients, construct exactly 1,200 positive words at K=2, 13, 10^80+139 and m=10,20,40,60 (100 rational phases for each pair). The algorithm recovers an independent rational phase and direct floor recomputation matches all 1,200 words. These positive tests and the algebraic exclusion certificate are distinct evidence types.

At m=5,...,13, independently obtain the reference Sturmian language from the complete breakpoint enumeration at K=(m-1)^2+2, then query every member at E(m) and E(m)-1. At E(m) all are present; at E(m)-1 exactly the pattern 1 0^(m-2) 1 and its complement are missing. There are 2,228 word-coefficient checks. This is finite regression supporting the proof route, not a proof of the all-m conjecture.

## Authorship, version and next open problem

R143 is a direct author-side exact membership theorem, with independent mathematical review NOT_REVIEWED. The frozen input retains its earlier pin and this note does not create a formal Task/CLAIM/Result or native X6 transfer.

Next: for each avoided word of R142, identify the active pairwise constraints at and above E(m) and prove whether N_min<=N_max necessarily holds. A negative result is reproducible from the two extremal pairs and K; a positive result has the rational midpoint witness.