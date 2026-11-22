# T6 / maximal p=13: full higher-valuation cancellation needs the second 13-adic digit

Date: 2026-11-23 (Asia/Hong_Kong). TASK_RESEARCH, informed original Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`. Original researcher `EM-X6-FB6990` / SID `MCP-082892eb480e45dea6d4b9fcc0491034`. **AUTHOR_PROVED / EXACT_INTEGER_PRECONDITIONS_CHECKED / UNREVIEWED / NOT_ADMITTED**. Portable Source theorem; not an authenticated Native T6 Result or PROGRESS.

## Theorem

Let A and B be finite multisets of positive integer exponents, each having sum <=2331, with exact moments H_k(X)=Σ_(e in X) (e/(e+1))^k. If H_k(A)=H_k(B) for k=0,...,6, then every denominator a=e+1 divisible by 13² has the same multiplicity on both sides, even in the presence of arbitrary 13-free or 13-single-valuation denominators.

The proof requires the *second 13-adic digit*: a first-digit Vandermonde alone leaves a genuine mass-admissible signed coefficient c_1=±13 for a=169.

## Proof

The binomial transform H_k=Σ_(j=0)^k (-1)^j binom(k,j) S_j, S_j=Σ a^(-j), shows equality of the original H_0,...,H_6 implies equality of S_j for j=1,...,6.

**Valuation 3 first.** Since 13³=2197<=2332<13⁴, the only denominator with v_13(a)>=3 is a=2197 (q=1). Let c_* be its signed multiplicity. Multiplying the exact S_1 equality by 13³ and reducing modulo13 isolates c_*: all v_13<=2 contributions are multiples of13 in Z_(13). Thus c_* == 0 (mod13). Each such exponent costs 2196 and occurs at most once on each side, so |c_*|<=1 and c_*=0.

**Valuation 2 next.** With the common a=2197 occurrences removed, the remaining v_13(a)=2 denominators are a=169q, q=1,...,12 (q=13 was valuation3). Let c_q be their signed multiplicities. Multiply the exact S_j difference by 13^(2j); all v_13<=1 denominators vanish modulo13, and the now-cancelled v_13=3 class has no contribution. Hence
    Σ_(q=1)^12 c_q q^(-j) == 0 (mod13), j=1,...,6.
The joint side-mass bound is 4662. Seven *distinct* nonzero signed support indices would cost at least Σ_(q=1)^7 (169q-1)=4725>4662. Therefore nonzero signed support has size s<=6. On any such support, the first s inverse-power equations give an invertible s×s Vandermonde matrix over F_13, because q∈{1,...,12} are distinct nonzero residues. Consequently c_q ==0(mod13) for every q.

For q>=2, |c_q| <= floor(2331/(169q-1)) <= floor(2331/337)=6 <13; hence these signed multiplicities vanish as integers. For q=1, however, the true bound is floor(2331/168)=13: the first-digit congruence permits c_1∈{-13,0,13}. Now use the **j=2** equation modulo 13²: multiplying S_2(A)-S_2(B)=0 by 13⁴ gives
    Σ c_q q^(-2) == 0 (mod13²),
because all v_13<=1 terms contain at least 13². After the other c_q have vanished, c_1==0 (mod169), and |c_1|<=13<169. Therefore c_1=0, proving the theorem.

## Exact arithmetic and limits

- a<=2332, 13³=2197, 13⁴=28561, q_max for v13² = floor(2332/169)=13, with q13 belonging to the already removed v13³ class.
- Joint distinct-support minimum costs: six cheapest (169q-1) sum=3543; seven cheapest sum=4725>4662.
- Residue inverses q=1,...,6 modulo13 are [1,7,9,10,8,11], and the corresponding six-column inverse-power Vandermonde determinant is 6 (mod13), nonzero. The proof applies to every size<=6 subset in q1..12.
- Per-side signed multiplicity bound for q1 is **13**, not <13. Omitting the modulo169 check leaves a genuine logical gap; 13 occurrences of denominator169 on one side cost 13×168=2184 <=2331 and are compatible with the first-digit condition alone.

After cancelling all common p13² and p13³ atoms, a full H0..H6 collision also satisfies for its remaining v13=1 denominators d=13a, gcd(a,13)=1:
    Σ m_a a^(-j) == 0 (mod13^j),  j=1,...,6.
This is a necessary full-shape mixed congruence, with arbitrary 13-free completion; rational moment equality inside a p13-only subfamily is a stronger condition that need not hold for the global collision.

## Provenance and next action

This extends the p19² and p17² high-valuation cancellation proof architecture while resolving the exceptional coefficient at the mass boundary. The currently selected mother Task is still `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. Frozen science remains `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` at `d84bd940cfb093cdc60e569f15cad58772a51dca`; P000 ACTIVE remains unmodified.

**Next actual mother-science unit remains the smallest pending p17 one-power vertical order**, starting with original q5 Source/reused q1..q4 and the six full-global mixed congruences from the companion p17 proof. p13 is a later maximal-prime layer and this theorem is available when it is reached. No new p13 Task/owner/claim is invented. Independent verification/admission remains pending.
