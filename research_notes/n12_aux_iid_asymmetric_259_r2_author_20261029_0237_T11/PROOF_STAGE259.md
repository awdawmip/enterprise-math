# Stage259 — exact fifth adjacent all-real contact face (portable author proof)

2026-10-29. `AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED`. Author: this run's distinct local `EM-LOCAL-RESEARCH2-20261029T0237` (not a native Source identity). Parent Stage258 immutable author proof in existing Draft PR #1571. **External** finite ternary IID model only; no assertion about P000-native X6 or Heartbeat physics.

## Fully quantified theorem

Let `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`, `N=12`. Policies may stop, decide P/Q, and randomize at *every complete ordered history*, with arbitrary real conditional probabilities. Set `eP=Pr_P(decide Q)`, `eQ=Pr_Q(decide P)`, `tP=E_P[stopping depth]`, `tQ=E_Q[stopping depth]`. For real caps `a,b∈[0,1]` define `V12(a,b)=inf max(tP,tQ)` subject to `eP<=a, eQ<=b`, `V=+∞` if infeasible.

Set

```
λP = 107495424/1321555
λQ = 69606372/1321555
θP = 0, θQ = 1
H  = 7515691301/142727940
```

The following are exact `(eP,eQ,tP,tQ)` vectors, in counter-clockwise polygon order:

```
C3  = (402953351/5159780352, 1580673145/1934917632,
       635362439/214990848, 528551303/161243136)
C4  = (2315791267/23219011584, 6715503965/8707129344,
       3454944163/967458816, 2845990051/725594112)
C12 = (13392328801/69657034752, 5104265215/8707129344,
       16809787489/2902376448, 4457228801/725594112)
B12 = (14080778551/69657034752, 5014749965/8707129344,
       16378493239/2902376448, 4266808051/725594112)
B3  = (661800839/7739670528, 2348630905/2902376448,
       917102471/322486272, 745221767/241864704)
```

Let `R259=conv{(eP,eQ) of C3,C4,C12,B12,B3}`. It is a strictly convex rational **pentagon**, area exactly `163431317383515625/151628202826291740672`. For **all real** `(a,b)∈[0,1]^2`,

`V12(a,b) = H − λP*a − λQ*b  ⇔  (a,b)∈R259`.

This region shares the *entire* B3--B12 side with Stage258's C3--C12 side on `2a+b=11379926137/11609505792`, with Stage259 inside on the `<=` side and Stage258 inside on the `>=` side; their interiors are disjoint. The new opposite C4--C12 side lies on `2a+b=33809389661/34828517376` with Stage259 inside on the `>=` side.

For the Stage259 frozen exact cap

```
a* = 6257204592203/43535646720000
b* = 942101660479/1360488960000
```

we have the strict Stage258 exterior witness `11379926137/11609505792 − (2a*+b*)=3/10000`. Its **global exact optimum** is

`V12(a*,b*) = 673365388654906643/149830082294400000`.

An achieving policy has `tP=10196336991431739473/2397281316710400000 < tQ=V12`; both error caps are exactly saturated. No positive θP is required on R259: the global supporting time weight stays `(0,1)`.

## Universal dual proof

For any ordered observation history h, the ratio `Q(h)/P(h)` equals `L(s)=(2/3)^i 2^j` where s=(i,j,k) are its symbol counts. Under P-normalized mass define the Bellman backward recursion

`H(s)=min{λQ*L(s) [decide P], λP [decide Q], L(s)+Σ_z P_z H(s+e_z) [continue]}`,

omitting continuation at depth 12. The included standalone `STAGE259_EXACT_FACE.py` uses integer-rational Fractions, checks all **455** count states and all **1,274** possible action costs, finding exactly **809** strictly positive alternative-action gaps. The complete tie set is **10 two-action states**: `((0,0,k), P/C)` for k=3,...,11, and `((0,1,3), Q/C)`. All other optimal actions are unique. Root H is precisely the rational value declared above. Backward induction on any full ordered history yields

`tQ + λP*eP + λQ*eQ >= H`.

Since `max(tP,tQ)>=tQ` and both λ strictly positive, every feasible policy obeys `max(tP,tQ)>=H−λP*a−λQ*b`. This reasoning includes irrational history-dependent randomization and does not rely on numerical LP output.

## Exhaustive equality fiber and BRC source fidelity

To analyze equality, aggregate the **P-weighted** action/visiting masses over all histories with the same counts s. Within that fiber every Q mass is exactly `L(s)` times P mass, and the one-step successor masses are multiplied by the original **positive labelled** `P_z` or `Q_z`. Conditioning the aggregated action P masses on aggregated P visiting mass produces a legal randomized count-state policy with exactly the same four observables `(eP,eQ,tP,tQ)`. This is an observer-relative sufficient quotient for *these four outputs and IID continuations* only, not a claim that arbitrary path observables are preserved. An acyclic randomized count policy can be independently pre-sampled as a finite convex mixture of deterministic count policies.

Bellman slack zero forces supported actions to be precisely the listed minimizing actions. Every effective deterministic equality policy is therefore `D_(k,M)`, where k=3,...,12 is the first all-neutral stop-and-decide-P depth, and M=Q or C determines the single special tie at s=(0,1,3). All other actions are the unique Bellman minimizers. Name the resulting four-observer vectors `B_k=obs(D_(k,Q))`, `C_k=obs(D_(k,C))`. For every k, `tQ>tP` and `tQ+λP*eP+λQ*eQ=H`. The exact executable checker proves the entire B_k family lies on the **four-observer** segment B3--B12, the C_k family for k>=4 lies on C4--C12, and C3 is the fifth exposed vertex. The five consecutive polygon turns are strictly positive; the displayed shoelace area follows exactly. Hence the full equality error fiber is precisely R259.

The additional continuation at `(0,1,3)` is reached by **three** ordered neutral/symbol-one source-labelled paths if k=3, but by **four** if k>=4. Thus `C3−B3=(3/4)*(C4−B4)` in **all four observables**, whereas `C_k−B_k=C4−B4` for k>=4. This positive BRC-compatible path-multiplicity fact explains the fifth corner and why a naive scalar or unordered-prefix collapse would give the wrong polygon. It is not an imported P000/BRC-native theorem.

For any real point in R259, a convex mixture of the five deterministic policies attains both caps. Every constituent has strict `tQ>tP`, so the mixture attains `V=H−λP*a−λQ*b`. Conversely, a minimizer exists by compactness of the finite product of policy simplexes. Equality in the dual bound with λP,λQ>0 requires both errors to meet their caps, every positively reached action to have zero Bellman slack, and tQ to attain the max; aggregation then forces the cap pair into R259. This completes both directions, including boundary and irrational parameters.

## Exact cap witness, actual execution and scope

At `(a*,b*)`, independently choose one of three complete deterministic policies at the root:

```
policy D_(3,C): probability 4353564672/103246484375
policy D_(12,Q): probability 841890839780122733/1677666785610156250
policy D_(3,Q): probability 765034255268522093/1677666785610156250
```

All three weights are strictly positive and sum to one. The full four-observer mixture is `(a*,b*,10196336991431739473/2397281316710400000,673365388654906643/149830082294400000)`, so it meets the dual bound. The independent full ordered-history DFS never merges histories, separately multiplies labelled P/Q positive masses and verifies **unit P/Q terminal mass** and exact agreement with the suffix DP for all 20 policies; **4,886 visited history nodes and 3,264 terminal decisions**. Observed local execution output includes `STAGE259_EXACT_BELLMAN_PASS 455 1274 809 10` and `STAGE259_EXACT_ALL_REAL_FACE_PASS`. Numerical LP was used only to discover candidate multipliers before the exact proof.

Code SHA256 (locally executed): `1638c87cc92699a60b95d060834df5185d6d9bcb38549e419b82395533731db1`.
Frozen science read pins for this turn: GLOBAL_KNOWLEDGE_V1 `main@229321bdae703ed7945ce46953d0ef3e32dee876`; Enterprise Math `main@7a07e93c4531e43b0f94f70a6f1b413c518d4b39`. P000 native file blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`, global P000 projection blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; ACTIVE worldview unchanged. Service reported `research_authority_granted=false`, current owner control query returned `CONTROL_QUOTA`; these author files are **not** Source CLAIM/Result/Driver acceptance or P000 correspondence proof.

## Next discriminating unit

Stage260: cross C4--C12 to strict left of `2a+b=33809389661/34828517376`. Select `a=6349626716117/43535646720000`, `b=984980765/1451188224`, for which the line gap is exactly `3/10000`. An exploratory *floating point* LP finds it feasible and suggests λP~82.31331235, λQ~53.15665618, `(θP,θQ)=(0,1)`, with mixed ties near `(0,0,4)` P/C and `(0,1,4)` Q/C. These floats are **not** a certified dual or theorem. Recover exact rational Bellman support, full positive-source observer policies and a matching primal proof or obstruction; seek the next all-real region and its complete five-vertex/other geometry. Preserve Source owner restrictions and all four observer types.
