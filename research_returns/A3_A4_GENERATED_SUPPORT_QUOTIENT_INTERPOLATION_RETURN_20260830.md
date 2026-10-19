# A3 → A4 Generated-Support Quotient / Interpolation — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

- Task-ID: `RS-A3-A4-GENERATED-SUPPORT`
- Researcher-ID: `EM-A3A4GS-4F7C21`
- Claim-ID: `chatgpt-a3a4gs-20260830-1930-4f7c21`
- Theorem owner: `bridge/a3-a4-generated-support-v3`
- Owner head: `bae63a2aacbccd8fa41be8e842ce4a1a148b4883`
- Execution branch: `research/a3-a4-generated-support-quotient-interpolation-em-a3a4gs-4f7c21`
- Execution base: `d1abe92d79c42b0b5e955607f179caba29b11fd6`
- Terminal research verdict: `SUCCESS / QUERY-TYPED BOUNDARY CLASSIFIED`
- Proposed hard-target disposition: `A3_A4_QUERY_TYPED_PRECISION_AND_P022_INTERPOLATION_BOUNDARY_CLASSIFIED`

This task is a legacy scheduler entry rather than a post-cutover immutable V2 publication. At claim time no `research_task_records/<task-id>/<publication-id>.json` existed for this task. I therefore did **not** fabricate a V2 publication, execution record, or result record. The durable researcher handoff is this return + checker + certificate + PR + scheduler HANDOFF; Driver may republish under V2 if continued execution is desired.

## 1. Frozen question

The scheduler frontier asks for genuinely cross-owner A3→A4 progress after the first generated-support bridge slice, specifically:

1. pressure-test the low-rank quotient/residue precision solver against generated-support cancellation;
2. test the interpolation boundary against an actual intrinsic graph geometry used by the P022/A5 side;
3. rehome any statement that no longer genuinely depends on both A3 and A4.

The result is a sharp **query-typing boundary**, not a new universal support calculus.

## 2. Source and reuse pins

Consumed sources were frozen before the result:

- current execution base: `main@d1abe92d79c42b0b5e955607f179caba29b11fd6`;
- thin A3/A4 owner: `bridge/a3-a4-generated-support-v3@bae63a2aacbccd8fa41be8e842ce4a1a148b4883`;
- current thin bridge blob: `a3_a4_support_bridge.py@ee66d0f6d9846171ff732204d5337fb3c0087d75`;
- A3 future-precision dependency: `research/core/relation-quotient@4d6f66e01c797ebc66b08748bf9382302789c2e2`;
- `hidden_band_predicate.py@756bf3a9df5306ba82556e11c8f9b6e8737daeee`;
- `guard_quotient_module.py@4718a98dde4cc0374c3de3a7760e04f2be207d6f`;
- `two_guard_coset.py@9487fa4ce12c70e6b23f4d428d49923318cc3550`;
- intrinsic graph geometry: `geometry.py@a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152`;
- Research Relay #82, especially the generated-support, interpolation, future-precision, and rank-two cancellation entries.

Tool-reuse resolution:

- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`;
- `T8_RELATION_OBSERVABLE_SPECTRUM`: `REUSE_APPLIED`;
- A3 hidden-band residue machinery: `REUSE_APPLIED` from the frozen relation-quotient head;
- A3 guard quotient-module/Smith machinery: `REUSE_APPLIED` from the frozen relation-quotient head;
- intrinsic graph shortest-step distance: `REUSE_APPLIED_AS_POSITIVE_CONTROL`.

No new global tool family is claimed.

## 3. Exact pairwise normalization identity

Let positive integer capacities be `m_i,m_j`, integer totals be `c_i,c_j`, and

\[
Z_{ij}=m_jc_i-m_ic_j.
\]

For proof only, write the exact rational coordinate

\[
\rho_i=\frac{c_i}{m_i},\qquad \rho_j=\frac{c_j}{m_j}.
\]

Then

\[
Z_{ij}=m_im_j(\rho_i-\rho_j).
\]

Hence, exactly,

\[
Z_{ij}=0\iff \rho_i=\rho_j,
\]

and for every integer radius `R>=0`,

\[
|Z_{ij}|\le Rm_im_j
\iff
|\rho_i-\rho_j|\le R.
\]

This is **not** a proposal to replace the canonical integer bridge with rational storage. The integer cross-multiplication remains the implementation-safe representation. The identity is used only to expose what information the pairwise support query reads.

The checker exhausts `1<=m_i,m_j<=5`, `-10<=c_i,c_j<=10`, and `0<=R<=5`: `77,175` exact zero/support assertions, no mismatch.

## 4. Rank-one `(radius,residue)` is an exact fiber-profile certificate — and no more

Consider one scalar relation observable `z` on a coarse A3 fiber. If the hidden image is

\[
z\in z_0+q\mathbb Z,
\]

then for the A4-style finite band `|z|<=R`:

### Case `q=0`

`z` descends to the coarse state. The support truth is exactly `|z_0|<=R`.

### Case `q>0`

Define the least absolute residue

\[
\delta_q(z_0)=\min_{t\in\mathbb Z}|z_0+qt|.
\]

Then

\[
\exists z\in z_0+q\mathbb Z:\ |z|\le R
\iff
\delta_q(z_0)\le R.
\]

But `z_0+qZ` is unbounded, so unsupported representatives always exist. Therefore:

- if `delta_q(z_0)>R`, the whole fiber is exactly unsupported;
- if `delta_q(z_0)<=R`, the full integer fiber is mixed: supported and unsupported representatives both occur.

So `(R,residue)` is an exact **state-local fiber-profile** coordinate. It is not, by itself, an exact decoder of an arbitrary fine representative's current support truth, and it is not automatically a universal-fine-support certificate.

This precisely narrows the Relay shorthand “pairwise support consumes `(radius,residue)`”: the safe claim is a quotient-fiber profile, not unrestricted erased-witness recovery.

The checker verifies the residue formula for `1<=q<=12`, `-30<=z_0<=30`, `0<=R<=10`: `8,784` exact assertions, no mismatch.

## 5. Universal fine cross-support crosses a genuine rank-two boundary

Take the canonical cancellation pressure test with unit capacities and coarse groups

\[
A=\{0,1\},\qquad B=\{2,3\}.
\]

The future query “all four fine cross-pairs are radius-`R` supported” reads the four scalar relations

\[
W(c)=(c_0-c_2,\ c_0-c_3,\ c_1-c_2,\ c_1-c_3).
\]

Inside a fixed coarse state the partition kernel is

\[
\eta=(a,-a,b,-b).
\]

Therefore

\[
W(\eta)
=(a-b,\ a+b,\ -a-b,\ -a+b)
\]

with integer generators

\[
g_a=(1,1,-1,-1),\qquad
g_b=(-1,1,-1,1).
\]

Their rank is two. The gcd of all entries is `Delta_1=1`; the gcd of all `2x2` minors is `Delta_2=2`. Thus the Smith factors are

\[
(1,2),
\]

and

\[
\boxed{\mathbb Z^4/W(K_A)\cong\mathbb Z^2\oplus\mathbb Z/2\mathbb Z}.
\]

So the universal fine-support future language carries two free quotient coordinates plus a parity-type torsion residue. It cannot in general be represented by one coarse signed relation scalar or by one rank-one `(R,residue)` profile.

### Same coarse state, opposite truth

Both fine states below have coarse totals `(10,10)` and coarse cross relation zero:

\[
c^{+}=(5,5,5,5),
\qquad
c^{-}=(0,10,0,10).
\]

For `c+`,

\[
W(c^+)=(0,0,0,0),
\]

so universal radius-zero fine support is true.

For `c-`,

\[
W(c^-)=(0,-10,10,0),
\]

so universal radius-zero fine support is false.

This is an exact impossibility witness: no deterministic observable that factors only through the coarse cross relation can recover universal fine support on this fiber.

### Consequence for the bridge

The low-rank solver is valid only after the **future query has actually reduced to one scalar hidden band**. The universal fine cross-support query has not; it is a four-guard query with rank-two hidden image. Applying the rank-one solver there would be a type error, not an approximation theorem.

This conclusion genuinely uses both owners:

- A3 supplies the partition kernel and hidden quotient module;
- A4 supplies the support predicate whose future semantics distinguishes coarse support from universal fine support.

## 6. P022/A5 intrinsic graph metric is an exact positive interpolation control

The current intrinsic geometry API defines `graph_distance` as the shortest unweighted walk length on a closed, loop-free, symmetric adjacency relation. On a connected graph this is the natural-number shortest-step metric.

For such a graph let

\[
R_r=\{(x,z):d(x,z)\le r\}.
\]

Then for every nonnegative integers `r,s`,

\[
\boxed{R_r;R_s=R_{r+s}}.
\]

### Proof

The inclusion `R_r;R_s subseteq R_(r+s)` is the triangle inequality.

For the converse, suppose `d(x,z)=d<=r+s`. Choose a shortest path

\[
x=v_0,v_1,\ldots,v_d=z.
\]

Let

\[
k=\min(r,d),\qquad y=v_k.
\]

Then `d(x,y)=k<=r`. Also

\[
d(y,z)=d-k.
\]

If `d<=r`, then `d-k=0<=s`. If `d>r`, then `k=r` and `d-k=d-r<=s` because `d<=r+s`. Thus `(x,y) in R_r` and `(y,z) in R_s`, proving the reverse inclusion.

Therefore every connected undirected simple-graph shortest-step metric is split-complete at every integer budget pair. Its A4 missing-interpolation defect is empty.

### Regression

The checker exhausts every connected labelled simple graph on `2..5` vertices:

- order 2: `1` connected graph;
- order 3: `4`;
- order 4: `38`;
- order 5: `728`;
- total: `771` connected graphs.

It checks `247,206` split-composition queries on that exhaustive census, plus:

- path6: `1,296` queries;
- cycle6: `576` queries;
- 3x3 grid: `2,025` queries.

Total graph-metric queries: `251,103`; no mismatch.

The proof, not the finite census, establishes the theorem.

## 7. The geometry transfer gate is the main cross-owner conclusion

The graph result must **not** be silently imported back into the A3-generated support family.

The A3 bridge uses the normalized relation quantity

\[
|Z_{ij}|/(m_im_j)
\]

through exact integer cross-multiplication. P022/A5 graph geometry uses shortest-step distance on an explicitly declared adjacency graph. The present sources do not prove these are the same metric on the same quotient carrier.

Therefore the valid transfer rule is:

\[
\boxed{
A3\_GENERATED\_RADIUS\_METRIC
= P022\_INTRINSIC\_GRAPH\_DISTANCE
\quad\text{must be proved before graph geodesicity is transferred.}
}
\]

Without that identification theorem:

- A3 generated supports can still have missing interpolation witnesses;
- P022 graph metrics remain split-complete;
- the two results are `COMPOSABLE_INDEPENDENT`, not interchangeable.

This is the requested interpolation/cancellation boundary.

## 8. Rehome decisions

The following are **not** retained as new A3→A4 bridge-owned mathematics:

1. “Shortest-path graph metrics are geodesic/split-complete.” This is a geometry-side/classical shortest-path fact; here it is only a pressure-test control.
2. General Smith-normal-form quotient theory. That is already owned by the A3 future-precision machinery and toolbox reuse path.
3. Generic A4 relation composition. Already canonical A4.

The genuinely bridge-owned result is the **query-typed interface theorem**:

> pairwise hidden-band residue compression is exact only at scalar-fiber-profile strength; universal fine cross-support can require a higher-rank/torsion quotient because A3 cancellation changes A4 future truth; a P022 graph metric eliminates interpolation holes only after a separate A3↔P022 metric-identification theorem.

## 9. Exact checker

Checker:

`research_checks/A3_A4_GENERATED_SUPPORT_QUOTIENT_INTERPOLATION_CHECK_20260830.py`

Git blob:

`sha1:388593a440816b129b13ac0094030ef327a939f5`

SHA-256:

`sha256:fe22cf7698949461e80c1c3bf1c1884e989cb0dc4f79e49859aba4578fbf34e3`

Observed independent run:

```text
PASS checks=337072 a3=77175 rank1_band=8784 cancellation=10 graph=251103 connected_graphs=771 by_order={2: 1, 3: 4, 4: 38, 5: 728} representatives={'path6': 1296, 'cycle6': 576, 'grid3x3': 2025}
```

Machine-readable certificate:

`research_artifacts/A3_A4_GENERATED_SUPPORT_QUOTIENT_INTERPOLATION/certificate_20260830.json`

## 10. P000 / scope boundary

P000 remains untouched and assumed.

The A3/A4 material consumed here is older three-axis research-slice mathematics. This return does not promote it to a description of the full Enterprise native space. Full spatial reality remains the six-axis discrete Cell space; time remains separately typed.

No Foundation file, canonical bridge source, canonical A3 source, canonical A4 source, or P022 geometry source was mutated by this research execution.

## 11. Driver disposition recommendation

Recommended Driver decision:

`ACCEPT / CLOSE CURRENT LEGACY FRONTIER` if the goal was to classify the low-rank-vs-cancellation/interpolation boundary.

A successor should be published only if there is a **specific** P022/A5 candidate geometry for which the missing theorem

`A3_GENERATED_RADIUS_METRIC == P022_INTRINSIC_GRAPH_DISTANCE`

is both meaningful and genuinely uses A3 data. Otherwise a pure graph/interpolation continuation should be rehomed to P022/A5 rather than kept under A3→A4.

Do not interpret this researcher return as Driver acceptance, canonical promotion, or a claim that P022 graph geodesicity holds for arbitrary A3-generated supports.
