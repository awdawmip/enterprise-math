# QTF3 bounded external prior-art and duplication check

Status: COMPLETED_BOUNDED_SEARCH / NO NOVELTY CLAIM.
Reviewer: EM-DVR-57CCCE. Date: 2026-09-10 Asia/Shanghai (2026-09-09 UTC).
Review target: RR-69FC34FA8AE1E91244F2, specifically the finite p-1 truncations L_p(1/2)=F_p(1) modulo p^3 on p>3,p=1 mod6.

## Search method and actual scope

Search surfaces were the web search index, arXiv's primary abstract/PDF pages, the primary publisher record, and NIST DLMF. Queries included:
- `"Mao" "Pan" truncated hypergeometric quadratic transformations modulo p^3 1/2`
- `hypergeometric "1/6" "1/3" "1/2" supercongruence quadratic transformation`
- `"quadratic" "truncated" "1/2" "p^3" Mao Pan`
- `site:arxiv.org "Split-prime supercongruence at the mixed CM point"`

Only primary sources support the classifications below. Secondary result summaries were routing hints. The relevant Mao-Pan introduction and main-results pages were inspected through the arXiv PDF text, especially printed pages5-6, Theorem2.1 and Equation(2.3), with surrounding scope statements. DLMF's transformation entry was read directly. The Shvets comparison is limited to its primary abstract; its proof is not adopted. The search is bounded, not exhaustive.

## Candidate classifications

1. **Exact antecedent for the retained Q2 input; partial antecedent for the reviewed p^3 target.** Guo-Shuai Mao and Hao Pan, [p-adic analogues of hypergeometric identities, arXiv:1703.01215v4](https://arxiv.org/pdf/1703.01215v4), Theorem2.1 / Equation(2.3), states the corresponding truncated quadratic transformation modulo p^2 when the least residue of -alpha is even, and explicitly treats it coefficientwise. Taking alpha=1/3 and p=6m+1 matches the reviewed proof's Q2 input. That displayed theorem has p^2 precision; it does not itself state the additional fixed-point p^3 lifting conclusion. The [2022 publisher record](https://doi.org/10.1016/j.jmaa.2021.125527) identifies the later 2F1-transformations publication.

2. **Classical analytic antecedent.** [NIST DLMF15.8.18](https://dlmf.nist.gov/15.8.E18) gives the underlying quadratic change of variable. With a=1/3 and b=2/3 it matches the formal-series transformation used for exact low-degree coefficients. This is not an assertion about finite truncation errors modulo p^3.

3. **Adjacent parameter family and different target.** Alex Shvets, [arXiv:2605.19773v1](https://arxiv.org/abs/2605.19773v1), studies coefficients of the cubed mixed-parameter period and a split-prime coefficient congruence. The parameter pair matches F_p's pair, but that abstract's coefficient/scale target differs from this review's comparison of two finite evaluations. It supplies no adopted proof of QTF3 here.

No exact duplicate of the full stated p^3 fixed-point target was identified in this bounded query set and inspected passages. This does not establish novelty. The classical transformation and p^2 antecedent are explicitly acknowledged; the current execution remains an attributed incorporation of pre-existing EM proof and peer-check sources.

## Review use

This artifact closes the bounded external prior-art/duplication work needed for the current paper-level review by recording actual queries, surfaces, candidate matches, distinctions and limits. It does not strengthen the theorem, replace the existing decisive non-author check, claim originality, or create a new mathematical task.
