# T6: universal cancellation of all 7² denominator factors by fifth-moment precision

Date: 2026-11-23 (Asia/Taipei). Own RESEARCH_DRIVER `EM-DVR-DEBB5E`, original SID `MCP-9b4714dc46b948afa4875a86c89c713c`. **New mathematical proof subunit, not a Native accepted Result or completed Task.** The proof extends the separately saved 7³ cancellation in `research_notes/driver/2026-11-23_t6_universal_p7cube_p11cube_p13square_cancellation.md`, and preserves all authorship of p17/p19/q14 work.

## Theorem

For any two finite multisets `A,B` of positive integers `e>=1`, with each separate exponent-mass sum at most `2331`, define `H_k(X)=sum_{e∈X}(e/(e+1))^k`. If `H_k(A)=H_k(B)` for every `0<=k<=5`, then

`m_A(d)=m_B(d)` for **every** `d=e+1>=2` divisible by `49`.

No assumption is made on the maximal prime factor, on sign/component separation or on uniform multiplicities. This is a strict necessary consequence of the original full-moment T6 hypotheses `H_0,...,H_6`; it does not close T6 or eliminate the remaining single-7 denominator layer.

## Full rational-to-modular reduction

Write `S_k(X)=sum_{e∈X}(e+1)^(-k)`. The binomial triangular identity `H_k=sum_{i=0}^k(-1)^i binom(k,i)S_i` implies exact equality `S_1(A)=S_1(B),...,S_5(A)=S_5(B)`. Throughout, the equations are the **complete** observations over all prime factors; individual p-components are not assumed equal.

1. There are no admissible `7^4` denominators since `7^4=2401>2332`. The exact-7³ denominators are `343j, 1<=j<=6`. Every side admits precisely 30 feasible multiplicity profiles under `sum_j(343j-1)m_j<=2331`. Reducing `7^(3k)*(S_k(A)-S_k(B))` modulo seven for `k=1,2,3` isolates the exact-7³ profile moments. Their three-coordinate signature `(sum m_j*j^(-k) mod7)_{k=1,2,3}` is injective over all 30 feasible profiles, as verified by the standalone checker. Therefore their multiplicities coincide, and the matched `7³` atoms can be cancelled.
2. The remaining exact-7² denominators are `49j`, `1<=j<=47`, `7∤j`—41 named types. Let `a_j=m_A(49j)` and `b_j=m_B(49j)`, with separate budgets `sum_j(49j-1)a_j<=2331` and similarly for `b`.
3. Multiply each full exact equality `S_k(A)-S_k(B)=0` by `7^(2k)`, for `k=1,...,5`. Lower-valuation `v_7(d)<=1` contributions are divisible by `7^k`; previously matched `7³` contributions cancel. Thus
   `sum_j(a_j-b_j)*j^(-k) ≡ 0 (mod 7^k)`, `k=1,2,3,4,5`.
   Every inverse exists modulo `7^k` since `7∤j`. This preserves all original composite denominators and exact side budgets.
4. The finite set `P={m_j ∈ N^41: sum_j(49j-1)m_j<=2331}` has exactly **512,672** elements. This is checked twice: by full multiplicity recursion and independently by coefficient DP of `prod_j (1-z^(49j-1))^(-1)` through degree `2331`.
5. Define `sig_K(m) = (sum_j m_j*j^(-k) mod 7^k)_{k=1,...,K}`. Exact enumeration yields **512,416** distinct 4-coordinate signatures and precisely **256** collision fibers, each containing exactly two feasible profiles. In a second independent full enumeration, those 256 pairs all receive *different* fifth-coordinate residues modulo `7^5=16807`. Therefore **all 512,672 five-coordinate signatures are distinct**.
6. The five congruences from (3) give `sig_5(a)=sig_5(b)`. Injectivity forces `a=b`, so all exact-7² denominators cancel. Combining (1) yields equality for every denominator divisible by `7²`. QED.

This is an exact finite-exhaustion certificate, not a heuristic or a source-state inference. No floating point is used.

## Verification

Fixed source: `research_checks/T6_P7_SQUARED_FIFTH_MOMENT_INJECTION_CHECK_20261123.py`, GitHub commit `282b69d4bcf65d47781256db32c12912d97bb5f1`, byte-identical remote readback. The original driver turn executed this standard-library Python program with all assertions passing:

- high `7³`: 30 feasible profiles and 30 unique three-moment signatures;
- low `7²`: 512,672 feasible profiles; exactly 512,416 four-moment signatures; exactly 256 two-profile fibers;
- the fifth signature separates all 256 fibers; final `PASS`.

The 512,672 finite candidate vectors include all legally possible restrictions of either original T6 side; the proof retains all other denominators as unknown contributions in the modular elimination.

## Research status / boundary

New mathematical subunit: **one complete precise theorem**, published and executable-checker verified. Native Review accepted 0; Result admitted 0; formal Task completed 0; mother objective completed 0. No new researcher CLAIM or owner replacement. Full prime-one-valuation and lower 5/3/2-power mixed moment reconstruction remain open. The original q14 delegation plan requires exact Source-byte authentication before any formal nonauthor review.
