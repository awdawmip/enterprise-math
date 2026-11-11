# R719 — Exact two-axis-local BRC triple-source recovery with two probes

**Research mode/status:** TASK_RESEARCH, author-side theorem and exhaustive finite exact verification; no claim of native X6 event admissibility, Result acceptance or independent Driver review. Parent Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; scientific freeze preserved at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Direct predecessor: R718 author Draft PR #2079, theorem `2026-11-11_R718_BRC_TAGGED_AXIS_STAR_DECODING_THEOREM.md`.

## Model, BRC carrier and observer

Fix `V={0,...,n-1}` representing **six X6 native axis identities** when `n=6` (not six ordinary Euclidean vector directions). A Boolean source state `h=(h_T)_{T in binom(V,3)}` retains distinct triple identities; its exact pair-degree observer is

```text
D_ij(h) := sum_{T contains {i,j}} h_T.
S(a,b) := {T : a in T or b in T}.
```

The chosen BRC population is the *labeled candidate triple identities*, and the operator here is exact additive Boolean-branch counting into integer pair-ledger coordinates. This is not a positive-weight cancellation or a claim about a physical force field. Allowed future operations for the compression certificate: the old complete state `h0` is known, a new state `h1` is obtained by toggling any number of triple bits **only inside** `S(a,b)` for a *known unordered pair* of event-axis tags, and the new pair ledger is read. Two explicitly chosen source-membership probes are permitted. Signs, provenance/order, Cell/Link/Port identities, V29 PASS/TRANSFER, V39 loop `j` and physical time remain separate native data pending a concrete mapping.

## R719.1 (general two-axis kernel)

**Statement.** Let `n>=5`, `a!=b` and `W=V\{a,b}` of size `m=n-2`. Consider differences `z_T` supported on `S(a,b)`, with `D(z)=0` over the rational field. Then

```text
z_{abi}=0                  for every i in W,
z_{bij}=-z_{aij}=:-x_ij    for {i,j} in binom(W,2),
sum_{j in W\{i}} x_ij=0   for every i in W.
```

These equations are necessary and sufficient. As the unsigned vertex-edge incidence matrix of the complete graph `K_m` has rank `m` over characteristic zero for `m>=3`,

```text
dim_Q ker(D restricted to S(a,b)) = binom(m,2)-m = m(m-3)/2.
```

For `n=5` (`m=3`) this is zero; for `n=6` (`m=4`) the kernel has dimension exactly **2**.

**Proof.** The ledger row for a pair `ij` with both endpoints in `W` forces `z_aij+z_bij=0`. The ledger rows `ai,bi` then say `z_abi+sum_j x_ij=0` and `z_abi-sum_j x_ij=0`. Adding and subtracting give `z_abi=0` and the displayed zero-vertex-sum equations. The `ab` row then vanishes. For the rank assertion, a left-kernel vector `u` of the unsigned incidence matrix obeys `u_i+u_j=0` on every edge of `K_m`; any triangle forces all `u_i=0` in characteristic zero. Rank is therefore `m`, yielding the dimension. QED.

The boundary cases `n=3,4` also have injective two-star restriction by inspection (at most one edge in `W`); no dimension formula with the full-row-rank argument is asserted for them.

## R719.2 (explicit six-axis lossless repair with exactly two probes)

Let `n=6`, distinct known tags `a,b`, and rename remaining axes `W={i,j,k,l}`. From the previously verified full `h0`, subtract the contributions of all frozen sources avoiding both tags from the new full pair ledger. Call the resulting 15 coordinates `L_{uv}`. Write

```text
s_uv := L_uv                              for u,v in W,
y_u := (L_au + L_bu - sum_{v in W\{u}} s_uv)/2,
d_u := L_au-y_u.
```

Then `y_u=h1_{abu}`, `s_uv=h1_{auv}+h1_{buv}` and `d_u=sum_v h1_{auv}`. Read **only the two distinct source bits**

```text
p := h1_{aij},  q := h1_{aik}.
```

All remaining `x_uv:=h1_{auv}` are recovered exactly:

```text
x_ij = p,    x_ik = q,
x_il = d_i-p-q,
x_jk = (d_i+d_j+d_k-d_l)/2-p-q,
x_jl = d_j-p-x_jk,
x_kl = d_k-q-x_jk.
h1_{buv} = s_uv-x_uv,
h1_{abu} = y_u,
h1_T = h0_T  when a,b not in T.
```

The necessary-and-sufficient Boolean/ledger certificate is: all reconstructed values are integral and in `{0,1}`, and all 15 pair counts of the reconstruction equal the actual new ledger. Uniqueness follows from R719.1 or the displayed linear solution.

The decoder therefore handles **up to all 16 changing bits** of the known two-star set using 15 exact pair counts, the prior complete state and two fixed Boolean probes. Equivalently, conditional on those observations, the remaining BRC provenance residual can be stored as these two source bits. The formula is covariant under relabeling all axes, provided the two tags and the probe axes are relabeled.

## R719.3 (two probes are optimal in worst case)

Choose the four non-tag axes `W`; set all four `h_abu=0`. On every edge `uv` of `K_4`, require `h_auv+h_buv=1`. Let the `a`-colored edges form one of the **three perfect matchings** of `K_4` and give `b` the complementary edge set. These are three different complete 16-bit source states with identical pair ledger: `L_uv=1`, `L_au=1`, `L_bu=2`, `L_ab=0`. One Boolean probe has only two possible outputs and cannot distinguish all three. R719.2 gives a uniform two-probe decoder. Thus

```text
worst-case minimum fixed membership queries = 2,
worst-case minimum adaptive membership queries = 2.
```

A fixed pair of individual triple-membership queries works globally **iff** its two queries target distinct adjacent edges of `K_4` (sharing one of the four non-tag axes), each tagged by either `a` or `b`. There are `12*2*2 = 48` such query pairs. Queries of `abu` are already determined by the ledger. Two probes on the same non-tag edge are redundant; two disjoint edges fail to distinguish the three perfect-matchings. Every adjacent pair gives two independent coordinates on the rank-two kernel from R719.1. QED.

## R719.4 (exact six-axis fiber census)

Hold the four outside-star bits fixed. There are `2^16=65,536` interior states. Exhaustive exact enumeration of the 15-row pair-ledger map gives

| Number of states per ledger fiber | Number of fibers |
| ---: | ---: |
| 1 | **64,096** |
| 2 | **672** |
| 3 | **32** |

Thus exactly **64,800** distinct ledgers arise, there are **768** unordered pairs of colliding states, and all collision differences have eight triple bits and one of **three** distinct Pasch-type 4↔4 supports.

Independent finite counting: four `abu` bits give a factor 16. For each edge of `K_4`, `(h_auv,h_buv)` is `00,01,10,11`. Let `F` be the set of mixed edges `01/10`. The ledger fixes `F` and its 4-vertex degree sequence; there are `2^{6-|F|}` choices for all unmixed edges. Nontrivial degree-sequence fibers appear for the three `F` that are 4-cycles (one double each), the six 5-edge `F` (two doubles each), and `F=K_4` (six doubles and two triples). Hence double fibers `16(3*4*1+6*2*2+1*6)=672`, triple fibers `16*2=32`, and single fibers `65,536-2*672-3*32=64,096`. The maximum multiplicity 3 proves a two-bit arbitrary-repair lower bound as well.

## Exact verifier and scope

`R719_BRC_DOUBLE_AXIS_LEDGER_VERIFY.py` uses only Python integer combinatorics and enumerates all 65,536 interior states, every collision fiber, all 120 pairs of candidate fixed probes, and 196,608 before/after decoder cases on three exterior baselines. Local execution returned:

```text
R719_BRC_TWO_AXIS_LOCAL_LEDGER_EXACT_PASS
interior_states=65536; distinct_pair_ledgers=64800
fiber_histogram={1:64096,2:672,3:32}
optimal_two_query_sets=48; decoder_cases=196608
```

The general kernel proof is symbolic for all `n>=5`, the rank and decoder results are symbolic for the stated six-axis candidate model, and the census is a complete finite calculation.

**Next discriminating native unit.** At frozen `a72226e2...`, locate a lawful signed and timed X6 event with explicit before/after Cell/Link/Port source identities, V29 PASS/TRANSFER and V39 loop `j`. Extract whether the changed candidate triads lie inside a single known star (R718), a known two-star (R719), or a larger set. In the two-star case, test which of the two residual source queries can be implemented by a lawful observer; retain sign/order/multiplicity and current/source ownership separately. A proof of actual event admissibility is still required to transfer this conditional decoder into native dynamics.
