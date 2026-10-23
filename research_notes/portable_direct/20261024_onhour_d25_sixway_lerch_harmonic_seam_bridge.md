# D25/SECOND-DIGIT-LIFT — Six-way Lerch elimination of the last seam Fermat quotient

**2026-10-24 | TASK_RESEARCH | exact author-side proof + independent modular author checks | UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.**

Mother: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; Task publication \`TP2-B6F4FC938FF94941C1B7\`. **Frozen scientific Source pin:** \`c47e13e4aba0e006366f989d6334d443f6333ae3\` (not the mutable GitHub head). Provenance Research lane: \`chatgpt-research-onhour-enterprise-math-20260923\`; separate maintenance lane neither used nor impersonated. P000 \`ACTIVE_LOCKED\`; account rule read head \`e29d16ce5d2abb0f99684e96ec41a8a8ba4e106f\`. This is classical finite rational modular algebra used as an external typed tool, not a new Heartbeat-World assumption.

## Exact inherited unfinished objective

The preceding [original-endpoint low-jet/two-sector proof](20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md) @ \`0f60695147d861c2f40448e46ef3adebab78c1c1\` established, for every prime \`p=6m+1\`, the exact reduction

\[
\mathrm{EP/LIFT}\iff \mathcal D_m^{\mathrm{finite}}\equiv0\pmod p,
\]
\[
\mathcal D_m^{\mathrm{finite}}=
\frac{A_m-G_m+B_m}{p}+J_m^{\mathrm{lo}}+B_m Z_m^{\mathrm{hi}}
+\frac{B_m}{9}\left(28-6H_{2m}-12q_p(6)\right),
\]
where \`B_m=(2m-1)!(2m)!/(4m)!\`, \`q_p(a)=(a^{p-1}-1)/p\`, and all other symbols, including **both nonzero high sectors and both seam/terminal contributions**, retain the preceding note's exact definitions and proofs. In particular \`A_m-G_m+B_m\in p\mathbb Z_{(p)}\` has already been established; division by \`p\` is legal. **Neither the target zero nor the native benchmark was previously proved/completed.**

The smallest removable mismatch in this exact same FIN target was the independent-looking \`q_p(6)\` scalar inside the p-normalized two-seam correction. It can be eliminated *without changing the target, term provenance or p-adic precision*.

## New task-level theorem — six-block harmonic seam normalization

For every prime \`p=6m+1>=7\`, let \`H_0=0\`, \`H_r=\sum_{k=1}^r1/k\in\mathbb Z_{(p)}\`. Then

\[
\boxed{H_m\equiv H_{2m}+H_{3m}\pmod p},\tag{LH}
\]
\[
\boxed{q_p(6)\equiv-\frac{3H_m+H_{2m}}{6}\pmod p},\tag{L6}
\]
and consequently, **for the original full D25/LIFT finite certificate**,
\[
\boxed{
\mathrm{EP/LIFT}\iff
\mathcal F_m\equiv0\pmod p,
}\tag{FIN-H}
\]
\[
\boxed{
\mathcal F_m:=
\frac{A_m-G_m+B_m}{p}
+J_m^{\mathrm{lo}}
+B_mZ_m^{\mathrm{hi}}
+\frac{B_m}{9}(28+6H_m-4H_{2m}).
}\tag{HF}
\]

Thus the seam/terminal correction no longer contains an independent Fermat quotient or a large integer power. The remaining required all-prime zero of \`\mathcal F_m\` is **open**; this theorem is a precise algebraic simplification of its proven equivalent finite target, not a proof that this target vanishes.

### Complete elementary proof (product permutation, not finite interpolation)

For any integer \`2<=a<p\`, write \`b_k=\lfloor ak/p\rfloor\` and \`r_k=ak-pb_k\` for \`1<=k<p\`. Because multiplication by \`a\` permutes the nonzero residues modulo the prime \`p\`, the integers \`r_k\` are exactly \`1,\dots,p-1\` in some order. Therefore the **exact integer identity**

\[
1=\prod_{k=1}^{p-1}\frac{r_k}{k}
=a^{p-1}\prod_{k=1}^{p-1}
\left(1-\frac{p\,b_k}{ak}\right)
\]

holds. Every denominator is a p-unit. Expand the finite product through \`p^2\` and write \`a^{p-1}=1+pq_p(a)\`: it follows, rigorously for every such prime, that

\[
\boxed{a q_p(a)\equiv
\sum_{k=1}^{p-1}\frac{\lfloor ak/p\rfloor}{k}\pmod p.}\tag{Lerch}
\]

No infinite analytic continuation and no assumed theorem are involved.

For \`a=2\`, the floor equals 1 precisely on \`3m<k<=6m\`. Because \`H_{6m}=H_{p-1}\equiv0\pmod p\`,

\[
2q_p(2)\equiv H_{6m}-H_{3m}\equiv-H_{3m}\pmod p.\tag{2}
\]

For \`a=3\`, the floor takes values 0,1,2 on \`[1,2m]\`, \`[2m+1,4m]\`, \`[4m+1,6m]\`, respectively, whence

\[
3q_p(3)\equiv2H_{6m}-H_{4m}-H_{2m}
\equiv-2H_{2m}\pmod p,\tag{3}
\]
where \`H_{4m}\equiv H_{2m}\pmod p\` by reflection \`k\mapsto p-k\`.

For \`a=6\`, the floor equals \`j\` on the consecutive block \`jm+1<=k<=(j+1)m\`, for \`j=0,\dots,5\`. Hence

\[
6q_p(6)\equiv
\sum_{j=1}^{5} j\left(H_{(j+1)m}-H_{jm}\right)
=5H_{6m}-\sum_{j=1}^{5}H_{jm}
\equiv-2H_m-2H_{2m}-H_{3m}\pmod p,\tag{6}
\]
using reflection \`H_{5m}=H_m\`, \`H_{4m}=H_{2m}\`.

The **exact** integer factorization \`6^{p-1}=2^{p-1}3^{p-1}\` gives \`q_p(6)\equiv q_p(2)+q_p(3)\pmod p\`. Multiply (2) and (3) appropriately:

\[
6q_p(6)\equiv-3H_{3m}-4H_{2m}\pmod p.
\]

Comparison with (6) and invertibility of 2 proves (LH). Substitute \`H_{3m}=H_m-H_{2m}\` to obtain (L6). Finally

\[
28-6H_{2m}-12q_p(6)
\equiv 28-6H_{2m}+2(3H_m+H_{2m})
=28+6H_m-4H_{2m}\pmod p.
\]

Since \`B_m/9\in\mathbb Z_{(p)}\` (every factorial argument is below \`p\`, and \`p>3\`), replacement in the inherited equivalence is valid modulo \`p\`; this proves (FIN-H). QED.

## Exact executed author checks and nonclaims

The check was executed with Python 3 integer modular arithmetic and modular inverses, no floats, on **21 primes \`7<=p<200\`, \`p\equiv1 mod6\`**. Independently checked: individual (2)/(3)/(6), (LH), (L6), equality of both seam corrections, and \`FIN\` versus \`FIN-H\` using separately reconstructed inherited low-jet and **both** high-sector finite sums. In every case all algebraic checks passed; the *original target zero also held in this finite sample only*.

Selected witnesses (columns are \`p; H_m,H_{2m},H_{3m}; q_p(6); old/new seam residue; (A-G+B)/p, low first jet, two-sector high; \mathcal F_m\` modulo \`p\`):

| p | Hm | H2m | H3m | q6 | seam old/new | divided | low jet | high | F |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 8 | 1 | 7 | 11 | 3/3 | 0 | 6 | 4 | 0 |
| 19 | 5 | 11 | 13 | 2 | 7/7 | 15 | 8 | 8 | 0 |
| 31 | 9 | 21 | 19 | 23 | 5/5 | 6 | 4 | 16 | 0 |
| 37 | 8 | 10 | 35 | 19 | 9/9 | 35 | 14 | 16 | 0 |
| 61 | 0 | 11 | 50 | 49 | 15/15 | 28 | 3 | 15 | 0 |

The companion source checker was executed locally under \`/mnt/data/enterprise_math/d25_lerch_seam_harmonic_check.py\` for author verification (not a GitHub path, native benchmark or independent review). The proof, not these 21 finite tests, establishes (LH), (L6) and equivalence (FIN-H) for all primes in the claimed domain. This derives a classical Lerch-style congruence in the present problem; **no claim of new-to-literature discovery** is made.

## Scope, information retained, and next mandatory science

BRC: \`REUSE_APPLIED / COMPOSE_APPLIED\`. Carrier = signed original hypergeometric finite family with branch labels low / high-A / high-B / seam-\`2m\` / seam-\`4m\`+terminal, exact p-valuations/units and a first/second-digit observer. (FIN-H) replaces only the \`q_p(6)\` scalar in the **mod-p** second-digit observer; it does **not** collapse either high interval, dispose of terminal data, or license p-adic third-digit reuse. Original native benchmark object, input and validation conditions unchanged.

**Immediate open proof obligation:** In (HF), prove that the divided first digit, low first jet, BOTH high-sector sums, and explicit harmonic seam correction cancel for *all* target primes, by a terminating contiguous-WZ finite certificate with boundary terms; or produce a strict obstruction. Because (HF) no longer depends on \`6^{p-1}\`, attempt a coefficientwise harmonic/binomial matching of the two high-sector heads against the low jet, retaining \`m+1,2m,2m+1,4m\` seams. A new list of finite zero residues would not discharge this obligation.

No new canonical Source role, CLAIM, open/run, native checkpoint, Result, Driver review, or native benchmark was created. Research Site currently reports v0.6.11 and \`research_authority_granted=false\`. Readback of existing Research-lane bridge requests: #6186 recovery status is local ACTIVE without Source authority; #6187 exact continuation rejected \`PREREQUISITE_NOT_SUCCEEDED\`; #6188 canonical dispatch finally \`FAILED/TimeoutExpired\`. Do not reuse their Issue numbers as native request IDs. [Support #1539](https://github.com/awdawmip/enterprise-math/issues/1539) is the existing responsible restoration path. Old staged UR records remain separately sourced. No scheduler or notification configuration was touched.
