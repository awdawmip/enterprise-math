# T6 / maximal p=17: universal 17²-cancellation and full-observer mixed congruences

Date: 2026-11-23 (Asia/Hong_Kong). Mode: TASK_RESEARCH, informed original Research lane `chatgpt-research-onhour-enterprise-math-20260923`; original Researcher `EM-X6-FB6990`, original SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Status: **AUTHOR_PROVED / EXACT_INTEGER_PRECONDITIONS_CHECKED / UNREVIEWED / NOT_ADMITTED**. This is portable mathematical evidence, not a current authenticated T6 CLAIM or semantic PROGRESS.

## Proposition 1: complete 17²-divisible denominator cancellation

Let A and B be finite multisets of **positive integer exponents** e, with per-side total exponent mass <=2331. Let a=e+1, and H_k(X)=Σ_(e in X) (1-1/(e+1))^k. If H_k(A)=H_k(B) for every k=0,...,6, then for each positive integer denominator a divisible by 17², its exact multiplicities in A and B agree.

This is unconditional relative to the stated integer-carrier/moment/mass hypotheses; other denominator prime factors and smaller-prime completion are unrestricted.

**Proof.** Put S_j(X)=Σ_(e in X) (e+1)^(-j), S_0(X)=|X|. The binomial transform H_k=Σ_(j=0)^k (-1)^j binom(k,j) S_j is invertible, so S_1(A)-S_1(B)=...=S_6(A)-S_6(B)=0 exactly.

As a<=2332 and 17³=4913>2332, every denominator with valuation v_17(a)>=2 has the form a=289q, q=1,...,8; these q are units mod17. Write c_q for the signed multiplicity. Multiply each S_j equality by 17^(2j), and reduce over Z_(17) modulo17. The v_17=1 terms carry a factor 17^j, and v_17=0 terms a factor 17^(2j). Therefore
   Σ_(q=1)^8 c_q q^(-j) == 0 (mod17), j=1,...,6.
All residue inverses exist, and every nonzero signed support index q requires at least one uncompensated denominator 289q on one side, costing 289q-1 total mass. Six distinct support indices cost at least Σ_(q=1)^6(289q-1)=6063, exceeding the joint budget 4662. Thus the nonzero support has size s<=5.

For any s distinct supported q, the first s equations have matrix M_(j,q)=(q^(-1))^j, j=1,...,s. Its determinant equals (Π q^(-1)) Π_(i<l) (q_l^(-1)-q_i^(-1)), nonzero mod17 because q are distinct among 1,...,8. Hence every c_q==0(mod17). Finally |c_q|<=floor(2331/(289q-1))<=8<17, so each c_q=0 as an integer. QED.

Reproducible integer prerequisites: 17³=4913; q_max=floor(2332/289)=8; residue inverses of q=1,...,8 are [1,9,6,13,7,3,5,15] mod17; per-side multiplicity ceilings [8,4,2,2,1,1,1,1]; sum first six distinct atom costs=6063. For the illustrative first-five-column 5x5 inverse-power matrix, determinant=16 mod17. The proof applies to *every* supported subset and does not require enumerating them.

## Proposition 2: necessary full-shape 17-adic signature (not p17-local rational equality)

After cancelling the common 17²-divisible denominators, let m_a denote the signed multiplicity of the remaining denominators d=17a with gcd(a,17)=1, a<=floor(2332/17)=137. All other denominators b are 17-adic units. The six exact full-shape moment equalities force
   Σ_(a:17∤a) m_a a^(-j) == 0 (mod 17^j),  j=1,...,6,
with inverses computed in Z/(17^j)Z, including full named multiplicity and cancellation provenance.

Indeed 0=S_j(A)-S_j(B)=17^(-j)Σ m_a a^(-j) + U_j, with U_j in Z_(17) from all 17-free denominators; multiply by 17^j. The congruences are *necessary* with arbitrary lower-prime completion, not sufficient for an actual collision.

In particular, the earlier exact p17 q12/q13/q14 scans required H0/H1/H2 (or H3) equality **inside the p17-only shapes**. They correctly exclude their declared p17-local equality models but do not alone eliminate full T6 collisions, since the 17-free remainder may compensate nonzero rational p17-local moments. The congruences above are the appropriate full-shape filter for the next open canonical p17 vertical-order classes, including current smallest as-yet-unclosed q5..q11 after the existing q1..q4 source work.

## Frozen sources and evidence boundaries

- Original Task input (preserved, not repinned): `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`, source commit `d84bd940cfb093cdc60e569f15cad58772a51dca`, Git blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`.
- Prior author p19² Vandermonde proof: `research_notes/portable_direct/onhour_20261123_t6_p19_v19_squared_mod19_universal_cancellation.md` (commit `c126a969570e871cca0bf9188dc0966716e54afb`). This p17 proof differs in its budget-derived <=5 sparse support requirement rather than a square 6x6 full catalog.
- Prior p17 q12/q13/q14 author certificates remain unchanged and retained at their stated local-model scopes.
- P000 ACTIVE projection read with canonical global blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; the shape moments are observer arithmetic, not replacement primitives.
- Native T6 winner/claim not established; original pending current Source continuation request `onhour-20261123-0105-t6-current-source-cont-v1` must be consumed by its **original request ID**, never reissued as the same mutation.

## Next exact scientific action

Apply the six *globally necessary* mixed p17 congruences to the actual frozen q5 vertical-order split roster with signed q0 and 17-free completion retained. If a modular candidate survives, derive its precise lower-prime completion rather than imposing p17-only equality. Independent author-source and arithmetic review precede any canonical acceptance. Parent T6=2332 remains OPEN.
