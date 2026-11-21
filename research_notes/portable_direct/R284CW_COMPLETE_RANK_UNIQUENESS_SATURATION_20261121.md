# R284CW — Complete top-R minimum-core classification and rank saturation of the frozen 34-bit Port observer

Date: 2026-11-21 (Asia/Shanghai)  
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**  
Scope: frozen finite 34-bit Port auxiliary observer, not native-X6 dynamics; independent portable research, with no shared TASK CLAIM.

## Frozen scientific source

Keep the exact R284CO scientific input, without changing the generator or arc geometry:

- Source: `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`
- Git blob SHA-1: `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`
- `P=17179869143; D=(1120832,6,13,1651128); Z=(0,390139,394465,1497639); SELECT=(0,1,2,4,5,6)`
- Frozen 65,536 codewords in the original enumeration order, SHA-256: `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`
- Exactly 64 labeled circular arcs. Let `d_k(x)` be the k-th smallest exact integer circular distance from codeword x to these arcs, k=1,...,64. Every `d_1(x)=0`.

An `R`-core is a subset of the 65,536 **distinct** codewords that preserves for every `k=2,...,64` the first `R` descending values of `d_k` **with multiplicity**. The level k=1 condition is automatic for a subset of size at least R.

## New complete finite theorem

**Theorem (entire rank domain, 1 <= R <= 65,536).** The only ranks with more than one minimum-cardinality R-core are

```
R = 779, 1263, 1563, 7587.
```

There are exactly **two** minimum cores at each of these four ranks, with respective minimum sizes **21,944; 25,997; 27,499; 42,637**. All other ranks admit exactly **one** minimum-cardinality core.

Moreover, at the precise **saturation rank**

```
R_sat = 24,850,
```

every codeword is individually required. At R=24,849 exactly 65,535 codewords are mandatory and the unique minimum core is that 65,535-point set. The single last added codeword is residue `14808969522` (original enumerated index `9312`, zero-based). Thus for each `R >= 24,850` the **entire 65,536-point population** is the only R-core and in particular the only minimum one.

This extends R284CV's classification from 20,000 to **all 65,536 ranks** without extrapolating from a finite prefix.

| R | Smallest core | Number of minimum cores |
|---:|---:|---:|
| 64 | 3,712 | 1 |
| 779 | 21,944 | 2 |
| 1,263 | 25,997 | 2 |
| 1,563 | 27,499 | 2 |
| 7,587 | 42,637 | 2 |
| 20,000 | 61,404 | 1 |
| 24,849 | 65,535 | 1 |
| 24,850–65,536 | 65,536 | 1 |

## General saturation and residual-quota proof

For a finite population X and functions `f_k:X→Z`, sort each level's values descending, retaining duplicates and original site IDs. For each site x and level k, write `B_k(x)=[a_k(x),b_k(x)]` for the complete **1-based** rank block having value `f_k(x)`. Define the earliest completed equal-value block rank

```
tau(x) = min_k b_k(x).
M_R = {x in X : tau(x) <= R}.
R_sat = max_{x in X} tau(x).
```

**Lemma A (forced set).** `M_R` is the exact union of those sites forced *individually* by the level-wise top-R multisets. If `b_k(x) <= R`, all occurrences of that value block at level k must be retained: values strictly greater than the cutoff and complete cutoff blocks are mandatory. Conversely, if each `b_k(x)>R`, every level containing x at its cutoff has a still-incomplete tied block and does not individually require this particular x. This converse concerns individual level mandates, not the coupled problem.

For each level k and rank R, let t be the R-th largest value, `H_{k,R}={x:f_k(x)>t}`, `E_{k,R}={x:f_k(x)=t}`, and `q_{k,R}=R-|H_{k,R}|`. The ordinary finite order-statistic lemma gives the exact equivalence

```
C preserves top-R at level k
iff H_{k,R} subset C and |C intersect E_{k,R}| >= q_{k,R}.
```

Therefore all R-cores are exactly the supersets of `M_R` satisfying the residual quotas

```
| (C \ M_R) intersect (E_{k,R} \ M_R) |
>= max(0, q_{k,R} - |E_{k,R} intersect M_R|).
```

At a rank with no tied cutoff (`f_k` values at positions R and R+1 differ for all levels), all residual quotas vanish. In general only tied-cutoff levels require a quota test. This reduction retains site identity and every labeled observation: no site or joint relation is erased without a cutoff-specific sufficiency certificate.

**Lemma B (saturation).** Since `tau(x) <= R_sat` for every x, `M_R=X` for all `R >= R_sat`. By Lemma A every element is then forced; consequently X is the only core and unique minimum core at such ranks.

**Finite classification.** The provided Python checker constructs the full 65,536-site population and all 63 nonconstant descending distance rows with **integer arithmetic only**. It computes all equal-value block endpoints and `tau(x)`. It independently tests every tied-cutoff rank below the measured `R_sat=24,850` against the exact quotas above. There are precisely **3,390** ranks having a cutoff tie below saturation, **356** of them with simultaneous ties in multiple levels. At every tested rank, all residual deficits are zero except the four ranks stated; each exception has exactly one unresolved level-64 quota of one item from two unforced sites. Therefore those four ranks have exactly two minimum cores, each consisting of `M_R` plus one eligible member. Lemma B covers all higher ranks without further enumeration.

The four eligible pairs, in increasing order of rank, are:
- 779: `6055669926`, `12724715924`
- 1263: `6051057018`, `12720103016`
- 1563: `6048093436`, `12717139434`
- 7587: `10044326029`, `14547547380`

The calculated minimum sizes and eight canonical SHA-256 core digests agree with immutable R284CV (its earlier finite-range certificate). At R=64 the mandatory set has 3,712 sites, and at R=20,000 it has 61,404 sites. The independent incremental prefix-frequency / integer-bitset scan over **all 65,535 nonterminal ranks** found exactly the same four outstanding quota ranks and no coupled event. Both are author-controlled computations, not independent external peer review.

## Reproduction and evidence

Run `python R284CW_saturation_proof_checker.py` in `research_notes/portable_direct/`, next to the unmodified pinned `R284CO_spectral_witness_checker.py`. The checker validates the frozen 65,536-entry hash, constructs 4,194,304 exact integer arc distances, sorts 63 level rows, computes the whole-domain theorem via the saturation reduction, and emits `R284CW_complete_rank_saturation_certificate.json`. Its output includes the final site, first saturation rank, all four binary exceptions, eight minimum-core SHA-256 digests and the observation counts. A separate incremental all-rank crosscheck was run locally to R=65,535. Source IDs and the exact frozen generator are retained; no scientific input is repinned.

**Review and model boundary.** `AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED`. The general lemmas are exact finite set arguments. The instance classification is contingent on the frozen Port codeword/arc definitions and the executable exhaustive certificate. No native Heartbeat X6 dynamical claim, formal Result, Working Truth or P000 change is asserted.

## Next question

Explain structurally why the last-to-be-mandatory word `14808969522` first enters at R=24,850 and why the four residual level-64 binary choices survive all other 62 distance levels. Search for a representation using the Port arc endpoint order and the joint residual incidence that predicts these exceptions without constructing all 4,194,304 distance values. Do not redo completed full-domain classification just to recover control context.

## Control / provenance

The work is independent portable science, following the previous R284CV research frontier. Historical source attribution: `EM-DIRECT-20B766`, `RA-617F40704F37299B15489DCA`; this invocation did not demonstrate possession of that legacy session's native private execution credential. Any missing Activity linkage requires the applicable original-identity or approved portable-source route; GitHub publication stands independently. No TASK CLAIM, shared owner alteration or independent review was performed.
