# R5 — exact mixed-weight repair library equals hypercube domination

Date: 2026-11-15. Scientific parent frozen at `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Evidence status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Model: auxiliary indexed-center radius-two integer-event observer, with the **mixed half-unit weight** of R5 PR #2427 commit `0683f51f871695db1bec29bef864df788c317d5f`; no claim of native X6 embedding.
Dependencies: the previously proven all-m product decomposition (commit `669c96f388bb2d84ef297e9a2ee09a5751c97353`) and the exact weighted mixed-optimizer classification (commit `0683f51f871695db1bec29bef864df788c317d5f`).

## Definitions

For any integer `m>=2`, take the event gaps `(3,2,2,3,(2,1)^m)`, radius 2 and center budget `K=m+3`. Closure masks are `0,a,b,ab`: `a` shortens gap 0 and `b` gap 3 by one. Let `J_t(S)` be sum of distances to the closest selected center subject to full radius-two coverage. Define the mixed penalty
`g_mix(S)=1_{[0 in S or (1_{2 in S} != 1_{8 in S})]}`
and minimize `J_t(S)+g_mix(S)/2`. The old optimum family contains the five seven-event cores
`O_0=0125,O_1=0135,O_2=0235,O_3=0245,O_4=0246`
with **every** binary suffix `(s,v)`, where `s` is the first suffix bit and `v in {0,1}^d`, `d=m-2`.
New `a` cores are `1235,1245,1246` with `s=1`, and `1345,1346` with `s=0`.
New `ab` additionally contains `1236` with `s=1`. For each core, all `v` occur. All these families are weighted optima by the earlier exact mixed-optimizer theorem.

Define replacement distance `rho(S,T)=|S\T|`. An old advice library `L` radius-two repairs a new optimizer family `F_t` iff `forall S in F_t, exists T in L:rho(S,T)<=2`. Write its minimum size `kappa_t^mix(m,2)`. Let `Q_d` be the binary d-dimensional hypercube, adjacency = one-bit change, and `gamma(Q_d)` its closed-neighborhood domination number (with `gamma(Q_0)=1`).

## Theorem (exact for all m>=2)

```
kappa_a^mix(m,2)  = 2^(m-2) + gamma(Q_(m-2)),
kappa_ab^mix(m,2) = 2^(m-1).
```

### Exact seven-event distance certificate

For cores in the order `1235,1236,1245,1246,1345,1346`, their distances to `O_0,...,O_4` are:

| new core | to O0 | O1 | O2 | O3 | O4 |
|---|---:|---:|---:|---:|---:|
|1235|1|1|1|2|3|
|1236|2|2|2|3|2|
|1245|1|2|2|1|2|
|1246|2|3|3|2|1|
|1345|2|1|2|2|3|
|1346|3|2|3|3|2|

By the all-m optimal-family decomposition, for core `C`, old core `O_j`, and suffixes `(s,v)`, `(s',v')`,
`rho(C+(s,v),O_j+(s',v'))=rho(C,O_j)+1_{s!=s'}+Hamming(v,v')`.

### Lower bound for a

For every `v in Q_d`, the new target `1346+(0,v)` has distance at most two only from `O_1+(0,v)` or `O_4+(0,v)`. Thus **one distinct mandatory baseline entry per v** is necessary: at least `N=2^d` old configurations.

Each baseline entry has core distance 2 from the different new target `1245+(1,w)`, and its first suffix bit differs, so its total repair distance is at least 3. Consequently all `1245+(1,w)` must be repaired by entries **other than the chosen N baseline entries**. Any such old entry can repair these targets only for a set of vertices `w` contained in one closed neighborhood of `Q_d`: its base core distance is at least 1, leaving at most one bit of v-change. The additional entries therefore provide a dominating set of `Q_d`. At least `gamma(Q_d)` extra entries are necessary, proving `kappa_a>=N+gamma(Q_d)`. The argument remains valid if the library had more than one entry eligible for a particular mandatory target: choose one mandatory entry per vertex, then count all remaining entries.

### Upper bound for a (constructive)

Choose any dominating set `D subseteq Q_d`. Store
```
O_1+(0,v) for v in D;
O_4+(0,v) for v not in D;
O_0+(1,v) for v in D.
```
Exactly `N+|D|` entries are stored. The targets `1346+(0,v)` are reached by the same-v `O_1` or `O_4`. Each `1345+(0,v)` has `u in D` with `Hamming(u,v)<=1`, so `O_1+(0,u)` repairs it. Both `1235+(1,v)` and `1245+(1,v)` are repaired by `O_0+(1,u)` for such `u`. Finally `1246+(1,v)` is repaired by `O_0+(1,v)` if `v in D`, or by `O_4+(0,v)` if `v not in D`. Every distance is at most 2. Choose a minimum dominating `D` to obtain equality.

### Exact ab theorem

The same `N` forced entries from `1346+(0,v)` remain. The additional new target `1236+(1,v)` has core distance at least 2 to every old core, so any radius-two repairing old configuration **must have suffix exactly `(1,v)`**. These `N` distinct requirements are disjoint from the first `N`, yielding `kappa_ab>=2N`.

Store `O_1+(0,v)` and `O_0+(1,v)` for **every** `v`. The former repairs both `s=0` cores, and the latter repairs all four `s=1` cores of `ab` within two replacements, so `kappa_ab<=2N`. QED.

## Consequences

1. This reduces the full mixed-model advice problem to an established discrete-combinatorial invariant: **hypercube domination**. Its exact value for arbitrary d need not be independently solved to obtain an exact all-m structural formula.
2. For `d=0,1,2,3,4`, exhaustive cube domination gives `gamma=1,1,2,2,4`, hence `(kappa_a,kappa_ab)` for `m=2..6` is `(2,2),(3,4),(6,8),(10,16),(20,32)`.
3. If `d=2^r-1`, a binary perfect Hamming code of length d is a dominating set with exactly `2^d/(d+1)` words. The sphere covering bound makes it minimum; thus `kappa_a=2^d(1+1/(d+1))`, `kappa_ab=2^(d+1)`. For example `d=7,m=9`: `kappa_a=144`, `kappa_ab=256`.
4. The sphere covering lower bound `gamma(Q_d)>=2^d/(d+1)` and probabilistic dominating-set bound `gamma(Q_d)<=2^d[ln(d+1)+1]/(d+1)` (sample each vertex with probability `ln(d+1)/(d+1)`, then add uncovered vertices) imply `kappa_a/2^d ->1` and `kappa_a/kappa_ab ->1/2` as `d->infinity`. The upper estimate can be trivially capped by `2^d`. This is a structural asymptotic statement, not a claim of a faster general algorithm.
5. The suffix coordinate `v` is an observer residual: the radius-two baseline witness must preserve each old v exactly, while the additional repairs are compressed to a domination code. Distances and provenance of the old helper states are retained.

## Exact reproducibility and evidence limits

An attached standard-library Python verifier reconstructs the complete core-distance matrix, proves finite domination numbers `d=0..4` by enumerating all smaller subsets, checks explicit minimum-library witnesses against each full new optimizer set, verifies the `d=7` Hamming-code sphere certificate, and independently performs exact brute-force minimum cover for `d<=1`. The general theorem is established by the proof above, not extrapolation. Raw executed output and verifier are in this same directory.

Next scientific question: construct a finite-state transfer algorithm for the exact `gamma(Q_d)` reduction under **restricted regular suffix languages** and a possibly different old-state language; preserve old helper vertices instead of silently replacing their availability by the new-target language. Independently audit the inherited seven-event optimal-family decomposition before raising the evidence level.
