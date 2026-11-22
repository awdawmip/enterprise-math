# EC49FWQ — Sharp fixed-versus-adaptive reconstruction of frozen P10 under an unknown CRT factor

Date: 2026-11-22 (Asia/Shanghai). Frozen scientific pin: **BRC16943**, unchanged. Parents: EC49FWP at cbcfb8fe777f889d33b76ec7e378315a7122151f; EC49FWJ at 95ab4672c9251e155c44049b007330277fa83603; EC49FWO at 940ad416fa1eb47904b93860ea5364e869e3de74. Scientific status: **AUTHOR_PROVED / EXACT_INTEGER_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Exact question and hypothesis

Fix an odd integer q>=3 with gcd(q,10)=1. Let F be the **50** distinct ten-bit supports generated from the frozen P10 four-slope certificate by the **72** primitive mod-10 affine directions. An unknown nonempty V subset of Z/q and U in F form W=U x V under indexed CRT coordinates in Z/10 x Z/q. The observer knows **all** indexed reflection defects

    D_W(a,b)=|W symmetric_difference ((a,b)-W)|

for a in Z/10, b in Z/q. A physical probe at a site (j,v) gives one Boolean membership bit 1_W(j,v). The target is to reconstruct **U itself**, not merely its size or the original direction's label.

A *fixed physical probe set* is chosen before observing D_W or V. An *adaptive physical probe* may be located after observing D_W, but before knowing the membership bit. Count distinct Boolean membership reads; the full-spectrum acquisition, computation, storage and selection have their own costs and are not included in the probe-count metric.

## Theorem — exact cost and all optimal fixed layouts

For this frozen population and arbitrary nonempty unknown V:

    fixed minimum = 3q physical sites;
    adaptive worst-case minimum = 1 physical site.

Every fixed optimum selects, **for each v in Z/q**, precisely one j from each of three disjoint groups:

    A={1,4,6,9}; B={2,7}; C={3,8}.

The number of distinct optimal fixed layouts is exactly **16^q**. One universal optimum is

    Q* = {(j,v): j=1,2,3, v=0,...,q-1}.

At q=11 these values are **33** sites and **17,592,186,044,416** different optimal site sets. If the observed spectrum has only one preimage within the declared F x nonempty-V model, it requires zero extra membership reads.

### Proof: exact spectrum fibers

For any cyclic Boolean support S, put K_S(c)=sum_x 1_S(x)1_S(c-x). CRT factorization yields

    D_W(a,b)=2(|U||V|-K_U(a)K_V(b)).

The exact frozen ten-cycle census in EC49FWJ gives 38 indexed defect signatures from 50 distinct U supports: 26 singleton fibers and 12 doubletons. Across the 12 doubletons, the complete list of nonempty ten-site symmetric-difference supports is:

    T={0,1,2,3,4,5,6,7,8,9},
    {1,2,6,7}, {1,4,6,9}, {2,4,7,9},
    {2,7}, {3,4,8,9}, {3,8}.

The three pairwise disjoint difference supports A,B,C occur for **equal-cardinality** U pairs, with masks respectively (327,789), (367,491), and (701,949), where the j-th bit encodes site j.

For two product states with equal complete D_W and **equal total mass**, the exact odd-factor inverse of EC49FWO gives V=V', |U|=|U'| and D_U=D_U'. For two states with different total mass, EC49FWP's rank-one rigidity and exact frozen census give V=V'=Z/q and {U,U'} either {23,287} or {833,965}; both are ten-cycle defect doubletons. Consequently **every product-spectrum fiber contains at most two states**, and any two distinct states in the same fiber share V and have U difference supported on one of the seven sets listed above. Conversely any equal-mass U doubleton and any fixed V produces an identical-spectrum pair, and a different-mass U doubleton does likewise when V is full.

### Proof: fixed lower bound

Take an arbitrary v in Z/q and restrict the unknown factor to V={v}. Each of the three equal-cardinality U doubletons with difference support A, B or C now gives a pair of product states with exactly the same full indexed spectrum. The products differ respectively only on A x {v}, B x {v}, C x {v}. A valid *fixed* observer must read at least one site in **each** of these pairwise disjoint sets, requiring at least three probes for this chosen v. Since the condition applies separately to all q possible singleton supports, the total is **at least 3q**.

### Proof: attainability and optimal layouts

Select per column v exactly one first-coordinate in A, one in B, and one in C. Such a triple meets every one of the seven possible ten-cycle difference supports (the other four all contain one of these three sets). Suppose two product states have the same indexed D_W. Their unknown V factors agree and are nonempty, so choose any active v in their common V; within this column, one of the three selected probes lies at a first-coordinate on which U differs. It distinguishes the states. Hence 3q suffices.

At an optimum of size 3q, the lower-bound conditions force precisely one from each A x {v}, B x {v}, C x {v} in every column, with no spare sites. There are 4*2*2=16 choices per column and exactly **16^q** optima overall.

### Proof: adaptive optimum

Every full indexed product-spectrum fiber has at most two states. From a known non-singleton fiber, select any physical position in the symmetric difference of the two candidate products, and query its membership. The single bit identifies U. A nontrivial equal-spectrum pair with V singleton witnesses that zero reads are not universally sufficient. Therefore the adaptive worst-case optimum is exactly one.

## What changed since EC49FWP / FWJ

EC49FWP proved that **total mass** can be recovered using two fixed probes even when V is unknown. The present result asks for the **entire original U word**, requiring 3q fixed probes in the same unknown-V model. EC49FWJ's three ten-site probes require a *known active* second-coordinate; a fixed column can be blank when V is arbitrary unknown. An observer permitted to choose any certified active column after interpreting D_W needs only three first-coordinate sites (and a fully spectrum-adaptive observer needs only one).

This quantifies the physical observation premium for unknown occupancy versus a programmable/conditional reader. It does not claim that obtaining the entire indexed defect spectrum is cost-free.

## Complete exact finite experiment

The accompanying standard-library Python script regenerates the frozen parity/projective P10 predicate and 72 primitive traces, deduplicates the 50 supports, checks all 38 ten-cycle spectrum fibers and seven difference sets, then computes the complete product spectrum for **every** nonempty V at q=3,7,11. Exact integer results:

| q | product states | indexed defect signatures | two-state fibers | same-mass pairs | different-mass pairs | fixed minimum |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 350 | 278 | 72 | 70 | 2 | 9 |
| 7 | 6,350 | 5,078 | 1,272 | 1,270 | 2 | 21 |
| 11 | 102,350 | 81,878 | 20,472 | 20,470 | 2 | 33 |

All assertions returned **ALL PASS**. The general q theorem is analytic, *conditional on* the cited parent finite P10 census and the full-indexed odd-factor inverse; this run's direct complete enumeration covers q=3,7,11. No remote CI, Lean or native X6 evolution was executed. The certificate is a frozen BRC-derived **auxiliary static CRT model**, with no extrapolation to full six-axis Cell dynamics or to moving-Farey successor observations.

## Next scientific frontier

The actual auxiliary Farey height update S_H -> S_(H+1) and its exact rational-anchor nearest-neighbor readout are pinned in EC49FVT @ a31340d5ff2dc5b8202388d7393a8b6817458c8e and EC49FVU @ ac3bdb073b8ccd821cd23e830bcb9ccaf8d09529. The next discriminating task is to construct and justify a *same-trace state/observation bridge* from the frozen ten-support and mod-11 exclusion to a contemporaneous height-state anchor and its signed successor pair; then test constancy of that successor readout on the verified static spectrum fibers. Retain anchor, height, branch and affine-line provenance. Until that bridge is proved, no dynamic sufficiency claim is made.

## Provenance and authority

Preserve all original papers and source pins. This note is independent **portable_direct** science associated with the unpublished-topic label RS-EC49AS; it makes no claim to a currently authenticated native Researcher/Activity, live CLAIM, Result, independent Review or P000 change.