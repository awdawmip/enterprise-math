# EC49BV — Signed-X6 regular-filter BRC transfer and Parikh-signature minimal-rank theorem

Date 2026-10-31. Status **AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_BRC_AND_BRUTE_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**. This is a portable author-side scientific handoff, not an authorized canonical CLAIM/Result/Review or independent replication.

## Fixed inputs

- Account authority: GLOBAL_KNOWLEDGE_V1 `awdawmip/chatgpt-global-knowledge` immutable `main@3ef4e62e3eed330b48fbf6d49ad465c724c01f09`; P000 V4 ACTIVE_LOCKED, matching `P000_STARTUP.json` canonical blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, and ACTIVE `我眼中的世界.md`.
- Project current source: `awdawmip/enterprise-math` `main@ffec41a6b512dbc430ba2df9de719aeae5d73da3`; EC49BU predecessor PR #1730 commit `4c8f5f689625c6f93ec362ea6107c13be5a23fb1`.
- Native positive-weight signed-X6 BRC Python kernel: exact Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. Use native `endpoint_weight(n,d,wp,wm)` and `endpoint_multiplicity(n,d)` unchanged; the filtered observer is a typed mathematical extension, not native API functionality.
- Directions are twelve signed steps over **six** spatial axes, not twelve axes. Time/force/phase dynamics and three-dimensional slice embedding are out of scope.

## Theorem A — exact typed weighted regular-filter bridge (author proof)

For `Σ={±e_i:i=1..6}`, an ordered path `p=a_1...a_n`, displacement `d(p)=Σa_j`, positive rational weights `w_i^±`, and a finite subgroup `H≤S_6` permuting axes without changing signs, let `L⊆Σ*` be regular and recognized by a finite deterministic automaton `(Q,q0,δ,F)`. For each `h∈H`, use the Laurent-polynomial transfer matrix

`T_h(x)_{q,q'}=Σ_{a:δ(q,a)=q'} w(ha) x^a`, with `x^a=Π_i x_i^{a_i}`.

Writing `u` for the start row and `v` for the accepting column, the formal power series `F_{L,h}(z,x)=u(I-zT_h(x))^{-1}v=Σ_{n≥0} z^n uT_h(x)^n v` obeys

`[z^n x^d]F_{L,h}(z,x)=Σ_{p∈L, |p|=n, d(p)=d} Π_j w(ha_j)`.

**Proof.** Each nonzero summand of `T_h^n` is in one-to-one correspondence with an ordered accepted DFA run. Its Laurent monomial is the exact six-component signed endpoint; its positive rational coefficient is the ordered-step product. Coefficient extraction selects exactly `(n,d)`. This is a formal series, not a continuous-time propagator. For the unfiltered one-state accepting DFA and `h=id`, enumerate each signed axis count `n_i^+=max(d_i,0)+k_i`, `n_i^-=max(-d_i,0)+k_i`, `Σk_i=(n-||d||_1)/2`; each multinomial summand then agrees termwise with native `signed_brc.endpoint_weight`. Setting every weight to 1 agrees termwise with `endpoint_multiplicity`. QED.

## Theorem B — exact minimal rational-linear additive observer (author proof)

Fix `n,d`, assume `m=(n-||d||_1)/2∈N`. Let `a_i=max(d_i,0)`, `b_i=max(-d_i,0)`, `q_i=w_i^+w_i^-`. For any signed-axis permutation `h∈H` and path with ordered-step histogram determined by `k_i`, `Σk_i=m`,

`χ_w(hp)=c_h(d) Π_i q_{h(i)}^{k_i}`, where `c_h(d)=Π_i(w_{h(i)}^+)^{a_i}(w_{h(i)}^-)^{b_i}`.

Let `β(p)` be the *full Boolean atom* of all selected finite regular source-side path tests, including endpoint/boundary labels and needed pullbacks. Crucial observer protocol: select the source-side atom `β` **before** applying permutation `h` and reading fixed-instrument weighted mass. Define `K_β` as those k with at least one actual ordered legal word of atom β. For all nonnegative rational path bags, the exact minimum dimension of a **rational-linear additive** state that answers every `O_{β,h}(m)=Σ_{p:β(p)=β}m_p χ_w(hp)` is

`R=Σ_{β attainable} rank_Q [c_h(d) Π_i q_{h(i)}^{k_i}]_{h∈H,k∈K_β}`.

**Proof.** Each single-path-bag vector is one original column; by the exact weight formula, all words with the same `(β,k)` share their observer column. Every feasible signature is realized by a legal ordered word. Separate β selection makes the observation matrix a row-and-column block direct sum indexed by β. The minimal dimension of any rational-linear additive factorization equals the rank of that observation matrix (lower bound by rank submultiplicativity, upper bound by a row basis). Thus the stated formula is both necessary and sufficient. QED.

Only `binomial(m+5,5)` different k exist. For fixed six axes, finite H and fixed pattern automata, their feasible β signatures are found by finite multiset residual-count DFA/substring DP (states consist of residual signed histograms, a bounded suffix, finite filter bits); this avoids enumerating `12^n` raw ordered paths. An additional single global raw-path-count coordinate is needed iff the per-atom all-ones row fails to belong to the group-weight row span for at least one feasible β. This is a rank statement, **not** a lower bound on arbitrary nonlinear bit encoding.

## Theorem C — covariant detector weight identity

For co-transported weights `(h·w)(ha)=w(a)`, one has `χ_{h·w}(hp)=χ_w(p)` for every ordered path, by termwise multiplication. Thus the group-weight columns are identical per selectable source atom and covariant rank equals the number of attainable atoms. Fixed-instrument group ranks may be larger. A genuinely co-transforming detector/filter must separately transport its language, so co-transforming weights *alone* must not be advertised as total covariance.

## Exact executable evidence and native correspondence

The actual Fraction/DP checker and two **independent** direct cross-checks produced:

| Signed-X6 zero-displacement length | Ordered paths | Native weighted aggregate | Source filter atoms | Fixed H={id,(1 2)} rank | Covariant rank | Extra count coordinate |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 396 | 1,560 | 154 | 166 | 154 | 1 |
| 6 | 19,920 | 152,640 | 298 | 458 | 298 | 1 |
| 8 | 1,281,420 | 18,921,000 | 520 | 860 | 520 | 1 |
| 10 | 96,807,312 | 2,737,312,704 | 576 | 1,152 | 576 | 1 |
| 12 | 8,175,770,064 | 441,121,650,816 | 576 | 1,152 | 576 | 1 |

Here `wp=(2,3,3,2,1,1), wm=(1,1,1,1,1,1)`, paths start/end at the same X6 cell, and the atom filters comprise first/last ordered signed steps and the full Boolean algebra of substrings `(+e1,+e2)`, `(+e2,+e1)`, including their H pullbacks. The core multiset-support DP ran twice and reports were byte-identical, and matched **unchanged native functions** for every listed n. Direct exhaustive independent path enumeration (all 396, 19,920 and 1,281,420 paths) for n=4,6,8 matched **per-k/per-atom signature sets**, exact ranks and weights. Third checker covered all six permutations of axes 1–3 (`S3≤S6`) at n=4 using `wp=(2,3,5,7,11,13), wm=1`: 174 atoms, fixed rank **198**, covariant rank **174**, all 396 words independently enumerated; five nonzero/zero endpoint test coefficients matched native (examples `n=4,d=(1,-1,0,0,0,0):456`, `n=5,d=(1,-1,1,0,0,0):5760`). All computations are **exact rational/integer**, not floating sampling. No run of all billions of paths for n=10 or 12 is claimed.

`EXACT_REPORT_EC49BV.json` SHA256 `7101f0b7b77cb2bbf64a5eba617c97ebae0ec54ed639e1b7d5ee39c3337c2537`.
This GitHub folder contains the theorem/proof and scope in this README, the three byte-identical **actually executed** checker scripts, the unchanged native `signed_brc.py` implementation, three original exact JSON reports, and the source/next-task handoff. The separate full local source-and-log archive `EC49BV_full_sources.tar.xz` (13,052 bytes; SHA256 `fb7829758591f76eaff2b004879bc19f19d0c2be4de2955cb67c4a60bba9bfa7`) is delivered as a conversation attachment; the archive itself is **not** represented as published to GitHub. Regenerate all three reports in this folder using the commands in `SOURCES_AND_HANDOFF_EC49BV.md`.

## Provenance and status

The mathematical automaton representation is consistent with classical rational/recognizable formal series: Berstel–Reutenauer, *Noncommutative Rational Series with Applications* (Cambridge UP, 2010), DOI `10.1017/CBO9780511760860.001`; *Noncommutative rational Pólya series*, Selecta Math. (2021), DOI `10.1007/s00029-021-00629-2`. **No general new weighted automata priority is claimed.** New project-local scope is a typed exact native signed-X6/positive-BRC bridge, explicit source-side filter and fixed/covariant permutation observer, and certified compact histogram calculation.

Native MCP service `0.6.11` reports `research_authority_granted=false`, canonical code review required and current active-job quota 5/5; live owner query not successfully obtained. This publication is an **author-side draft on an existing research PR**, not a native Source CLAIM, frozen Result, independent Driver review, or P000 amendment. Only the static finite ordered positive-weight observer claims above are supported; no native rotation, heartbeat time, force, physical residual, negative/amplitude cancellation or three-dimensional-slice transfer is established.

## Next open scientific unit EC49BW (proposed; not an admitted Task)

For a variable observation horizon (pattern length growing with path length), characterize when the minimal additive observation rank is **uniformly bounded over even n** under arbitrary declared finite H, signed-X6 endpoint and positive rational BRC weights. Either construct a family with proved unbounded rank or an effective uniform bound with a finite-language certificate. Distinguish fixed from covariant instruments, carry the no-filter native bridge, and separate dimension from exact integer bit complexity. Preserve all provenance and current Source task/owner/independence boundaries.
