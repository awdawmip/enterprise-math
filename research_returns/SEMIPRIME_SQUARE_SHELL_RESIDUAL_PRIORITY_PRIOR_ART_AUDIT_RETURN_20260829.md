# 半素数平方壳 residual-priority / Fermat–Lehman–Hart 外部先例审计：研究回报

Researcher-ID: `EM-SSMFPA-B7C914`  
Task: `RS-SEMIPRIME-SQUARE-SHELL-RESIDUAL-PRIORITY-PRIOR-ART-AUDIT`  
Publication: `TP2-6F3C9418A72D0E5B31C4`  
Claim: `chatgpt-ssmfpa-20260829-1744-b7c914`  
Branch: `research/semiprime-square-shell-residual-priority-prior-art-audit-em-ssmfpa-b7c914`

Status: `TERMINAL_RESEARCH_RETURN / EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED / NO_NOVELTY_CLAIM`

## 1. Terminal verdict

Hard target:

`SEMIPRIME_SHELL_RESIDUAL_PRIORITY_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`

Disposition:

`SUCCESS / CLASSICAL_CORE_EXACTLY_DUPLICATED + NORMALIZED_PRIORITY_RULE_NOT_LOCATED_IN_AUDITED_SET`

The audit separates two layers that must not be conflated:

1. **The mathematical search object is classical.** The adjacent-square midpoint scan is Fermat; the multi-`k` residual `x_k^2-4kN` is multiplier-Fermat / Lehman / Hart; modular rejection of nonsquare residue classes is established sieve practice.
2. **The exact finite-window ordering**
   `score(k)=e_k/(2*x_k-1)`
   **was not found as an explicit multiplier-priority rule in the frozen primary/authoritative audit set.** Hart's paper advances multipliers in order; the current FLINT implementation likewise advances a fixed-480 multiplier stream and tests each residual without sorting by this score.

The second statement is deliberately classified only as `NO_MATERIAL_MATCH_IN_AUDITED_SET`. It is **not** a novelty, priority, patentability, Working Truth, or factorization-advantage claim.

## 2. Claim-by-claim classification

| Parent/audited claim | Classification | Boundary |
|---|---|---|
| `F_N(t)=(A0+t)^2-N` and first square at the factor midpoint | `EXACT_DUPLICATE` | Fermat difference-of-squares in square-shell coordinates. |
| Reject candidates whose residual is not a quadratic residue modulo selected moduli | `EXACT_DUPLICATE` | Standard modular square rejection / Fermat-style sieving. |
| `x_k=ceil(sqrt(4kN))`, `e_k=x_k^2-4kN`; square `e_k` gives factors | `EXACT_DUPLICATE` | Classical multiplier-Fermat / Lehman / Hart near-square object. |
| Cycle through multipliers and test the near-square residual | `EXACT_DUPLICATE` | Hart OLF baseline; independently visible in FLINT. |
| Rank a finite multiplier window by `e_k/(2*x_k-1)` | `NO_MATERIAL_MATCH_IN_AUDITED_SET` | Exact ranking rule not located; no novelty inference permitted. |
| Replace ascending `k` by a smarter multiplier selector | `ADJACENT_METHOD` | Multiplier selection is itself old and actively explored. |
| Other arithmetic/modular Fermat accelerations | `ADJACENT_METHOD` | McKee and modern sieve work materially narrow any broad novelty framing. |

Full source-by-source ledger is frozen at:

`research_artifacts/SEMIPRIME_SQUARE_SHELL_RESIDUAL_PRIORITY_PRIOR_ART_AUDIT/prior_art_ledger_20260829.json`

## 3. Classical chain: Fermat -> Lawrence -> Lehman -> Hart

The relevant lineage is older and broader than the shell terminology.

- Fermat searches for `X^2-Y^2=N`.
- Modern historical treatment by Hittmeir records F. W. Lawrence's 1895 generalization to multiples `kN`.
- Lehman (1974) systematizes suitable multipliers and difference-of-squares searches on multiples (conventionally including `4kN`) to obtain the classical deterministic `N^(1/3)` regime.
- Hart (2012) turns this multiplier-near-square idea into the One Line Factoring algorithm: for successive multipliers it forms `s=ceil(sqrt(ni))`, tests the residual from the next square, and takes a gcd when that residual is square.

Therefore the parent quantity

`e_k = ceil(sqrt(4kN))^2 - 4kN`

is not merely “similar to” classical work. It is the same near-square residual search object, with a harmless conventional scaling of the multiplier.

Primary references:

1. R. Sherman Lehman, *Factoring Large Integers*, Mathematics of Computation 28 (1974), 637–646, DOI `10.1090/S0025-5718-1974-0340163-2`.
2. William B. Hart, *A One Line Factoring Algorithm*, Journal of the Australian Mathematical Society 92 (2012), 61–69, DOI `10.1017/S1446788712000146`.
3. Markus Hittmeir, *A time-space tradeoff for Lehman's deterministic integer factorization method*, Mathematics of Computation 90 (2021), 1999–2010; arXiv `2006.16729`.

## 4. Hart ordering is not residual-priority ordering

Hart's published algorithm uses a sequential multiplier variable. Its practical speedups include a fixed small-prime multiplier and modular square tests, but the paper does not first compute a window of residuals and reorder multipliers by normalized distance to the next square.

This distinction is independently testable in the current FLINT source. At pinned commit

`flintlib/flint@7c8c3c8f1c134fa93f3af98f044f9958b9c09a72`

`src/ulong_extras/factor_one_line.c`:

- defines `FLINT_ONE_LINE_MULTIPLIER 480`;
- multiplies the input by 480;
- computes the next-square residual `square - in`;
- advances by `in += n`;
- tests each residual for squareness.

There is no `e/(2x-1)` score, priority queue, window sort, or equivalent normalized-residual ordering in that implementation.

That is enough to reject the overly strong statement “the parent's score is just Hart's ordering.” It is not. The **residual object** is Hart/Lehman prior art; the **specific ordering functional** is a separate, narrower claim.

## 5. Exact normalization lemma

Let

`z=4kN`

be nonsquare,

`x=ceil(sqrt(z))`,
`e=x^2-z`,
`d=x-sqrt(z)`.

Then `0<d<1` and

`e = d(2x-d)`.

Since

`2x-d = (2x-1)+(1-d)`,

we obtain the exact identity

`e/(2x-1) = d + d(1-d)/(2x-1)`.

Also, because

`(x-1)^2 < z < x^2`,

we have

`0 < e < x^2-(x-1)^2 = 2x-1`,

so

`0 < score(k) < 1`.

Thus the parent score is precisely a normalized **phase inside the adjacent-square interval**. It contains no information beyond `(N,k)` and the next-square residual. This is useful for interpretation: any value of the heuristic must come from a better *search order*, not from a new arithmetic invariant carrying hidden factor information.

## 6. Modular filtering boundary

The parent observation

“if the Fermat residual is not a quadratic residue modulo `m`, skip the expensive exact square test”

is also classical in substance.

Hart explicitly uses modular square rejection as a practical speedup for his multiplier residuals. More recent work goes much further: Hittmeir's 2023 Journal of Number Theory paper develops a hyperbolic modular sieve and applies it to improve Fermat factorization. Therefore the parent QR filter should be treated as an `EXACT_DUPLICATE` baseline idea, not a shell-specific law.

Reference:

Markus Hittmeir, *Integer factorization as subset-sum problem*, Journal of Number Theory 249 (2023), 93–118, DOI `10.1016/j.jnt.2023.02.010`.

## 7. Adjacent multiplier-selection prior art

The audit also looked for methods that do **not** simply use ascending multipliers.

- Lehman's method is itself a systematic multiplier-selection framework.
- Hittmeir's later work changes how the Lehman search is organized and accelerated.
- Overmars and Venkatraman (2024) explicitly explore a continued-fraction mechanism for prescribing multipliers to Hart's OLF.

Reference:

Anthony Overmars and Sitalakshmi Venkatraman, *Continued Fractions Applied to the One Line Factoring Algorithm for Breaking RSA*, Journal of Cybersecurity and Privacy 4 (2024), 41–54, DOI `10.3390/jcp4010003`.

This does **not** duplicate `e/(2x-1)`. It does show that “do not search `k` in naive order” is far too broad to be regarded as novel.

James McKee's 1999 *Speeding Fermat's Factoring Method* (Math. Comp. 68, 1729–1737, DOI `10.1090/S0025-5718-99-01133-3`) is another important adjacent antecedent: it accelerates Fermat using different arithmetic structure, so any future novelty framing must be narrower than “a faster Fermat-like search.”

## 8. Frozen no-match statement for the exact score

The audit searched the exact formula and close semantic equivalents, including:

- `e_k/(2*x_k-1)` factoring / residual multiplier;
- `ceil(sqrt(kN))^2-kN` with multiplier ordering;
- distance to the next square as a multiplier priority;
- fractional-part / square-phase formulations of `sqrt(kN)`;
- near-square residual ordering;
- Hart/Lehman multiplier selection and later OLF variants.

Audited surfaces included Hart's published paper and institutional PDF, Lehman/McKee bibliographic primary records, Hittmeir's peer-reviewed/preprint work, FLINT's pinned implementation, and a 2024 OLF multiplier-selection paper.

Result:

`C5_NORMALIZED_RESIDUAL_PRIORITY = NO_MATERIAL_MATCH_IN_AUDITED_SET`.

Meaning only:

> Within the frozen sources and queries, no explicit factor-blind multiplier ordering by `e_k/(2*x_k-1)` (or an identified algebraically equivalent score) was located.

It does **not** mean that no such publication exists. It does **not** support a novelty claim. A wider patent/database/historical monograph search would be a different task.

## 9. Consequence for the parent research line

The correct research status is now sharper:

### Frozen classical / non-novel core

- shell midpoint -> Fermat;
- QR rejection -> established modular sieve idea;
- multi-`k` residual -> Lawrence/Lehman/Hart multiplier near-square;
- generic “choose multipliers better” -> established research axis.

### Narrow surviving object

Only the exact selector

`score(k)=e_k/(2*x_k-1)`

can remain as a separately named empirical heuristic, and only at the parent's already-frozen strength:

`FINITE_WINDOW_RESIDUAL_PRIORITY_HEURISTIC / NOT_A_FACTORIZATION_RESULT`.

It should not be called a new factorization method. Its empirical rank improvement and bit-size coverage collapse remain exactly as the parent result recorded them. Whether a scalable/streaming version reduces **total cost** belongs to the separate Hart-streaming-cost task and is not answered here.

## 10. Audit reproducibility and evidence policy

Frozen ledger:

`research_artifacts/SEMIPRIME_SQUARE_SHELL_RESIDUAL_PRIORITY_PRIOR_ART_AUDIT/prior_art_ledger_20260829.json`

Task-specific checker:

`research_checks/SEMIPRIME_SQUARE_SHELL_RESIDUAL_PRIORITY_PRIOR_ART_AUDIT_CHECK_20260829.py`

The checker validates:

- presence of every required classification class used by the audit;
- source coverage of Hart, Lehman, Hittmeir, McKee and the pinned FLINT implementation;
- exact integer bounds `0<e<2x-1` for nonsquare next-square residuals over a deterministic test range;
- reconstruction `z=x^2-e`, confirming that the normalized score is a derived phase coordinate.

No Working Truth, Foundation authority, canonical promotion, patentability conclusion, or factorization-gain claim is made.

## 11. Terminal routing

Terminal verdict:

`EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`.

Recommended Driver action:

1. accept the classical duplicate boundary for Fermat / QR sieve / multiplier residual;
2. retain `C5_NORMALIZED_RESIDUAL_PRIORITY` only as `NO_MATERIAL_MATCH_IN_AUDITED_SET`, never as novelty;
3. do not reopen the same prior-art audit by changing notation;
4. if the cost-audit sibling task proves no total-cost gain, close this residual-priority branch as an empirically interesting but noncompetitive ordering heuristic;
5. if a future novelty/legal-priority question is desired, publish a separate specialist patent/historical-search task rather than upgrading this literature no-match.
