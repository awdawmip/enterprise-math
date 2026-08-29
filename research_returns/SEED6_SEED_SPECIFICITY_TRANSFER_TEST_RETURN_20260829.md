# Seed-6 Seed Specificity Transfer Test — Research Return

Status: `TASK_TERMINAL_RETURN`

- Task-ID: `RS-SEED6-SEED-SPECIFICITY-TRANSFER-TEST`
- Publication-ID: `TP2-45170A2BBF5D87471FCD`
- Researcher-ID: `EM-S6X-6ACB29`
- Claim-ID: `chatgpt-s6x-20260829-16509c`
- Execution record: `ER-5573D4422F2608C1B00B`
- Execution branch: `research/seed6-seed-specificity-transfer-test-em-s6x-6acb29`
- Execution base: `65d1cae115e648f5154a898cd3ba83a2a2b27223`
- Hard target: `SEED6_SPECIAL_VS_GENERIC_STRUCTURE_CLASSIFIED`
- Terminal verdict: `MIXED_SPECIFICITY`

## 1. Executive result

The current Seed-6 bridge signatures do **not** identify `6=2·3` as a mathematically unique bridge seed.

The transfer audit separates them into five layers:

1. the rooted Boolean `B3` coatom cell / Levi `C6` / prime-valuation SNF `(1,1,2)` is **`PRIME_PAIR_GENERIC`**;
2. gcd-edge reconstruction and the common-lcm-top property are **`COPRIME_PAIR_GENERIC`**;
3. the three perfect-matching states and the support-faithful two-row column complex are **`ARBITRARY_PAIR_GENERIC`** for distinct decorated carriers under the freshness rule;
4. the product-square checksum, rank-one bridge determinant, and abstract `S4 -> S3` action on the three perfect matchings are **`TAUTOLOGICAL`** standard consequences of the chosen product/matching data;
5. parity orientation and uniqueness of a carrier decomposition **`FAILS_UNDER_TRANSFER`**.

What is genuinely Seed-6-specific is only external arithmetic-order metadata: `2` and `3` are the smallest possible distinct prime carriers, `2` is the unique even prime, and `6` is the first scalar product of two distinct primes. None of those facts enters the carrier-incidence, gcd, matching, rank-one, or global gluing laws unless one deliberately adds order/parity labels.

Therefore the recommended architecture is:

> keep `6` as the canonical reference and teaching coordinate, but formulate the mathematics on a **decorated carrier pair `(a,b)`**, and retain several seed types rather than treating the scalar `s=ab` as the complete state.

This is `MIXED_SPECIFICITY`: Seed-6 is the first and cleanest representative of the prime-pair stratum, not a unique core geometry.

## 2. The transfer object must be a decorated seed

Let

\[
\Sigma=(a,b),\qquad a,b>1,
\]

be the **decorated seed**, and let its scalar be

\[
s(\Sigma)=ab.
\]

A fresh prime `r` means `gcd(r,ab)=1`; fresh `p,q` are distinct primes with `gcd(pq,ab)=1`.

Define

\[
C_r^{a,b}=(ar,br)
\]

and the local triangle

\[
T_r^{a,b}=\{ab,ar,br\}.
\]

For two fresh primes `p,q`, define the three unordered pairing states

\[
P_0=\{ab,pq\},\quad
P_1=\{ap,bq\},\quad
P_2=\{aq,bp\}.
\]

The scalar `ab` alone is not enough. For example,

- `12=(3,4)` is a coprime thick-carrier seed, while `12=(2,6)` is an overlapping-carrier seed;
- `18=(2,9)` is coprime, while `18=(3,6)` has carrier overlap.

Thus transfer statements must name the carrier decomposition, not only the integer seed.

## 3. Exact local transfer theorem

Put

\[
d=\gcd(a,b).
\]

For every fresh prime `r`,

\[
\gcd(ab,ar)=a,
\qquad
\gcd(ab,br)=b,
\qquad
\gcd(ar,br)=rd.
\]

Also,

\[
\operatorname{lcm}(ab,ar)=abr,
\qquad
\operatorname{lcm}(ab,br)=abr,
\qquad
\operatorname{lcm}(ar,br)=\frac{abr}{d}.
\]

These formulas give an exact overlap observable. Define

\[
\Delta_T
=
\frac{
  \left(
    \gcd(ab,ar)\,
    \gcd(ab,br)\,
    \gcd(ar,br)
  \right)^2
}{(ab)(ar)(br)}.
\]

Then

\[
\boxed{\Delta_T=d^2}.
\]

Hence the local triangle detects carrier overlap exactly without additive distance and without any factor-recovery objective.

The edge-gcd reconstruction rule

\[
ab=g_{01}g_{02},\quad
ar=g_{01}g_{12},\quad
br=g_{02}g_{12}
\]

holds for all three vertices **iff** `d=1`. Likewise, all three pairwise lcms have the same top `abr` **iff** `d=1`.

Therefore these signatures are exactly `COPRIME_PAIR_GENERIC`.

By contrast,

\[
(ab)(ar)(br)=(abr)^2
\]

holds for arbitrary positive `a,b,r`. It is `TAUTOLOGICAL`.

## 4. What transfers from the Seed-6 Boolean cell

The completed local Seed-6 task identified, for prime `r>3`,

\[
\{6,2r,3r\}
\]

as the three coatoms of the Boolean divisor lattice `B3` of `6r`; its rank-aware Levi graph is `C6`, and its prime-valuation incidence matrix has SNF `(1,1,2)`.

Exactly the same statement holds whenever `a,b,r` are three distinct primes. Therefore the entire normalized Boolean/coatom/Levi/SNF package is

`PRIME_PAIR_GENERIC`.

The taskbook controls

\[
6=2\cdot3,\;
10=2\cdot5,\;
14=2\cdot7,\;
15=3\cdot5,\;
21=3\cdot7,\;
22=2\cdot11,\;
35=5\cdot7
\]

all lie in the same prime-pair stratum. Their normalized local bridge cell is the same after carrier-role relabeling.

The smallest coprime decorated seed that exits this stratum is

\[
(3,4),\qquad s=12.
\]

With fresh `r=5`,

\[
T_5^{3,4}=\{12,15,20\}.
\]

Its gcd reconstruction and common-lcm-top properties remain valid because `gcd(3,4)=1`, but it is not the coatom layer of a three-prime Boolean `B3`.

More generally, for prime-power carriers

\[
a=p^\alpha,\qquad b=q^\beta,\qquad p\ne q,
\]

and fresh prime `r`, the prime-valuation column matrix is

\[
A_{\alpha,\beta}
=
\begin{pmatrix}
\alpha&\alpha&0\\
\beta&0&\beta\\
0&1&1
\end{pmatrix}.
\]

Its determinant is `-2 alpha beta`. The gcd of its `2x2` minors is `g=gcd(alpha,beta)`, so

\[
\operatorname{SNF}(A_{\alpha,\beta})
=
\operatorname{diag}
\left(
1,\,
g,\,
\frac{2\alpha\beta}{g}
\right).
\]

Thus the Seed-6 SNF `(1,1,2)` occurs exactly at `alpha=beta=1` inside this prime-power family. For `(3,4)` the SNF is `(1,1,4)`; for `(4,9)` it is `(1,2,4)`.

This proves that exponent thickness is a real transfer boundary that support-only incidence would erase.

## 5. Pairing orbit and bridge rectangle transfer

For fresh distinct primes `p,q`, the bridge rectangle is

\[
M_{a,b;p,q}
=
\begin{pmatrix}
ap&aq\\
bp&bq
\end{pmatrix}
=
\begin{pmatrix}a\\b\end{pmatrix}
\begin{pmatrix}p&q\end{pmatrix}.
\]

Therefore

\[
(ap)(bq)=(aq)(bp)
\]

for arbitrary `a,b,p,q`. This is exactly the vanishing `2x2` determinant of an outer product and is `TAUTOLOGICAL`.

The gcd decorations are more informative:

\[
\gcd(ap,aq)=a,\qquad
\gcd(bp,bq)=b,
\]

\[
\gcd(ap,bp)=pd,\qquad
\gcd(aq,bq)=qd,
\]

and

\[
\gcd(ap,bq)=\gcd(aq,bp)=d.
\]

Hence “diagonal gcds `1` and column gcds exactly `p,q`” is `COPRIME_PAIR_GENERIC`, with failure controlled exactly by `d`.

There are exactly three abstract perfect matchings of four named blocks. Under the freshness assumptions, the three **numerical** states `P0,P1,P2` are distinct whenever `a != b`; if `a=b`, `P1=P2` and only two numerical states remain.

Thus:

- the existence of three matchings is standard four-label matching combinatorics;
- the standard `S4` action on them has image `S3` and Klein-four kernel `V4`;
- that group-action fact is `TAUTOLOGICAL`, not Seed-6-specific;
- the noncollapsed three-state numerical realization is `ARBITRARY_PAIR_GENERIC` for distinct decorated carriers plus freshness.

## 6. Global gluing also transfers

A completed support-faithful Seed-6 gluing return identifies the `k`-column square complex as

\[
X_k\cong K_k\times I,
\]

with `K_k` indexing fresh columns and `I` indexing the two carrier rows.

Nothing in that product-CW identification requires the numerical carriers to be specifically `2,3`. For arbitrary distinct decorated carriers `a != b`, introduce vertices

\[
(a,r_i),\ (b,r_i)
\]

and the same horizontal/vertical square incidence. Relabeling the two rows gives the same complex `K_k x I`.

If numerical labels `ar_i,br_i` are used as the actual vertices, freshness prevents cross-row collisions when `a != b`: from `a r_i=b r_j`, after dividing by `d=gcd(a,b)`, coprimality forces a fresh prime to divide one carrier unless the reduced carriers are both `1`, which would imply `a=b`.

Therefore the support-faithful global incidence is `ARBITRARY_PAIR_GENERIC` for distinct decorated carriers.

In particular,

\[
V=2k,\qquad E=k^2,\qquad F=\binom{k}{2},
\]

\[
H_1(X_k;\mathbb Z)
\cong
\mathbb Z^{(k-1)(k-2)/2},
\qquad
H_2(X_k;\mathbb Z)=0.
\]

The natural row-preserving transport is endpoint-only and strictly compositional, so loop holonomy is identically trivial. These are properties of the product complex, not properties unique to Seed-6.

This also supplies a negative-control rule: homology created only after erasing the fresh-prime support is quotient-induced pseudo-topology, not evidence of a Seed-6-specific surface.

## 7. Seed-type stratification

The transfer test requires at least the following decorated-seed types.

| Type | Exact condition | First useful example | Structural effect |
|---|---|---|---|
| `C0_PRIME_PAIR` | `gcd(a,b)=1`, both distinct primes | `(2,3)` / 6 | full prime-atom `B3`, Levi `C6`, SNF `(1,1,2)` |
| `C1_COPRIME_ONE_SUPPORT_THICK` | coprime prime powers, at least one exponent >1 | `(3,4)` / 12 | gcd reconstruction survives; valuation thickness changes SNF |
| `C2_COPRIME_MULTI_SUPPORT` | coprime, at least one carrier has >1 prime support | `(2,15)` / 30 | block incidence survives; faithful prime-support cell has more atoms |
| `OVERLAP` | `a!=b`, `gcd(a,b)>1` | `(2,4)` / 8 | overlap defect `d^2>1`; gcd reconstruction/common top fail |
| `EQUALITY` | `a=b` | `(2,2)` / 4 | two carrier rows and two pairing states collapse |

This is more precise than a single “prime vs composite seed” split.

A control-taxonomy correction follows from the exact definitions: `35=5·7`, `10=2·5`, and `15=3·5` are all prime-pair controls, not composite-carrier controls. Genuine composite-carrier controls include `(3,4)`, `(4,9)`, and `(2,15)`.

## 8. Why the scalar seed is not canonical data

If all nontrivial factor-pair decompositions are allowed, ambiguity already occurs at

\[
12=2\cdot6=3\cdot4,
\]

and those two decompositions belong to different structural strata (`OVERLAP` versus `C1`).

Even if one requires `gcd(a,b)=1`, ambiguity eventually remains. If `omega(s)` is the number of distinct prime divisors of `s`, then the number of unordered nontrivial coprime carrier decompositions is

\[
2^{\omega(s)-1}-1.
\]

The first scalar with more than one such decomposition is

\[
30=2\cdot15=3\cdot10=5\cdot6.
\]

Thus “seed = scalar integer” loses structurally relevant decomposition data. The correct object is at least a decorated pair, or a scalar plus a chosen carrier partition.

## 9. Parity and the special role of 2

The local Seed-6 cell has a reflection swapping its two unordered seed carriers. If one adds parity labels, `2` and `3` become intrinsically distinguishable because one is even and the other odd.

This does **not** make Seed-6 unique:

- parity orientation survives on `6=(2,3)`, `10=(2,5)`, `14=(2,7)`, `22=(2,11)`;
- it already fails inside the prime-pair class at `15=(3,5)` and `21=(3,7)`.

So parity is a useful optional subtype decoration (`EVEN_ODD`) but not a core invariant of the bridge geometry.

The minimality of `2,3`, the fact that `2` is the unique even prime, and their location in the ordinary numerical order can be recorded as `SEED6_SPECIFIC / EXOGENOUS_ONLY`. They do not enter the intrinsic bridge laws proved above.

## 10. Transfer table

| Seed-6 signature | Classification | Exact transfer boundary |
|---|---|---|
| rooted Boolean `B3` coatom / Levi `C6` / SNF `(1,1,2)` | `PRIME_PAIR_GENERIC` | exact for distinct prime carriers; fails first at coprime `(3,4)` |
| gcd-edge reconstruction | `COPRIME_PAIR_GENERIC` | iff `gcd(a,b)=1` |
| common-lcm top | `COPRIME_PAIR_GENERIC` | iff `gcd(a,b)=1` |
| triangle product-square | `TAUTOLOGICAL` | arbitrary positive `a,b,r` |
| three abstract perfect matchings | `TAUTOLOGICAL` | standard matching count |
| three noncollapsed numerical pairing states | `ARBITRARY_PAIR_GENERIC` | distinct `a,b` + fresh `p,q`; equality collapses |
| `S4 -> S3` matching action with `V4` kernel | `TAUTOLOGICAL` | standard four-label combinatorics |
| rank-one bridge determinant | `TAUTOLOGICAL` | arbitrary `a,b,p,q` |
| rectangle diagonal gcd `1` / columns `p,q` | `COPRIME_PAIR_GENERIC` | iff `gcd(a,b)=1` |
| support-faithful `K_k x I` column-square complex | `ARBITRARY_PAIR_GENERIC` | distinct decorated carrier rows |
| natural flat transport / trivial holonomy | `ARBITRARY_PAIR_GENERIC` | inherited from product structure |
| parity orientation | `FAILS_UNDER_TRANSFER` | fails at prime pair `(3,5)` |
| scalar uniquely determines carrier decomposition | `FAILS_UNDER_TRANSFER` | all-pair semantics fails at 12; coprime-only semantics at 30 |
| `2,3` minimality / particular arithmetic order | `SEED6_SPECIFIC` | true only as external metadata; not a core bridge law |

No tested intrinsic bridge invariant is uniquely Seed-6-specific.

## 11. Exact 120-seed census

The checker exhausts all

\[
2\le a\le b\le16,
\]

giving exactly `120` decorated seeds. For each pair it chooses the two least fresh primes not dividing `ab` and checks the triangle, rectangle, pairing, support, parity, and scalar-decomposition claims using exact integer arithmetic.

Exact class counts:

- `C0_PRIME_PAIR`: `15`;
- `C1_COPRIME_ONE_SUPPORT_THICK`: `23`;
- `C2_COPRIME_MULTI_SUPPORT`: `26`;
- `OVERLAP`: `41`;
- `EQUALITY`: `15`.

Regression totals:

- Boolean `B3` coatom cells: `15`;
- gcd-reconstructible cells: `64`;
- common-lcm-top cells: `64`;
- three-state numerical pairings: `105`;
- two-state equality degenerations: `15`;
- parity-oriented pairs: `56`;
- product-square checksum: `120/120`;
- rank-one bridge cross-product: `120/120`;
- overlap identity `Delta_T=gcd(a,b)^2`: `120/120`.

Minimal counterexamples in the census:

- numerical equality collapse: `(2,2)`, scalar `4`;
- distinct carrier overlap: `(2,4)`, scalar `8`;
- coprime but non-prime-pair: `(3,4)`, scalar `12`;
- prime-pair parity-orientation failure: `(3,5)`, scalar `15`;
- coprime multi-support carrier: `(2,15)`, scalar `30`;
- scalar decomposition ambiguity: `12`;
- coprime scalar decomposition ambiguity: `30`.

The checker additionally verifies the coprime-decomposition count formula for every `4 <= s < 500`.

## 12. Verdict and downstream recommendation

Hard target `SEED6_SPECIAL_VS_GENERIC_STRUCTURE_CLASSIFIED` is met.

Final verdict:

`MIXED_SPECIFICITY`

The exact recommendation is:

1. **Keep 6 canonical as a reference seed.** It is the smallest clean member of the prime-pair stratum and is an excellent coordinate for examples and drawings.
2. **Do not make 6 a uniqueness axiom.** The strongest local structural package already transfers to every distinct prime pair.
3. **Generalize mathematically to decorated carrier pairs `(a,b)`.** The scalar `ab` is not sufficient state.
4. **Retain multiple seed strata.** At minimum: prime-pair, coprime prime-power-thick, coprime multi-support, overlap, and equality/collapse.
5. **Use `Delta_T=gcd(a,b)^2` as an exact stratum detector** for overlap in the local triangle.
6. **Treat parity/order as optional decorations**, not as intrinsic bridge geometry.
7. **Do not promote standard perfect-matching, rank-one, or product-square identities as Seed-6 discoveries.**
8. If a future Seed-6-specific invariant is sought, it must use additional arithmetic structure not erased by carrier-role relabeling and must beat the control seeds `10,14,15,21,22,35`.

No factorization, endpoint-recovery, additive-distance, or performance interpretation is used in this result.

## 13. Reproducibility and source exposure

Task-local exact checker:

`research_checks/SEED6_SEED_SPECIFICITY_TRANSFER_TEST_CHECK_20260829.py`

Machine-readable census:

`research_artifacts/SEED6_SEED_SPECIFICITY_TRANSFER_TEST/transfer_census_120.json`

Checker SHA-256:

`sha256:90a76695c027cb44170938fdae7aa6869a6034a43d01e9f8bd243aaf35e12452`

Census SHA-256:

`sha256:224aa1aa2454d52998f2959bce8440a84a72d8c72f739ae3ca03cb5211a05043`

Upstream research inputs consulted during the audit:

- `RS-SEED6-BRIDGE-TRIANGLE-LOCAL-GROWTH`, frozen handoff `RR-94465ADA2AE22091D57D`, PR `#851`;
- `RS-SEED6-BRIDGE-SURFACE-GLOBAL-GLUING`, task-terminal return on PR `#852` (awaiting independent Driver review at time of this freeze).

The transfer formulas, overlap defect, decorated-seed stratification, prime-power SNF transfer, scalar-decomposition ambiguity, and 120-seed census were independently checked in this task. The task had no dependency gate on the pairing-orbit or degeneration tasks, so their still-running results were not required for closure.
