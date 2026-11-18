# EC49FSQ — Saturation lifting of original-native BRC price-swap phase diagrams

Date: 2026-11-18. Frozen BRC16943 scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Author research continuation of PR #2706@0842017a6bfdc83e7af59c6d2be0493dd53d58da and PR #2712@d149ad2ae47eaf43b40e12a4491dc293bf59c0a2. Original population: 310 configurations, 141 distinct named joint-response profiles, all 228 original physically named observations, uniform profile prior, all adaptive complete deterministic identification trees.

## 1. New exact saturation-lift lemma

Let \(\mathcal T\) be the finite original-native decision-tree class with nonnegative observation prices. Let \(N_q(T)\) count the total occurrences of a named observation q across the 141 profile paths (not merely the distinct tree nodes). An irredundant tree asks q at most once along each profile path, so \(0\le N_q(T)\le141\). Repeated q on a path is informationally redundant because original named outcomes for that profile are deterministic; deleting it never increases cost.

For any fixed prices of the other observations, write the unrestricted minimum total cost \(F(d)=\min_T[C_T(0)-dN_q(T)]\), where d is the discount applied to q in units of base price t. Suppose at \(d=d_0\) an actually feasible, globally optimal, complete named tree \(T_*\) has \(N_q(T_*)=141\). Then for **every real** \(d\in[d_0,1]\):

\[
\boxed{F(d)=F(d_0)-141(d-d_0).}
\]

Indeed, for every irredundant T,
\(C_T(d)=C_T(d_0)-(d-d_0)N_q(T)\ge F(d_0)-141(d-d_0)\).
The original optimal saturated tree attains equality. This is a global optimality certificate for a full continuous discount ray, regardless of competing trees and all other nonnegative prices.

For price-exchange comparisons, apply the lemma separately to q32 in the direct orientation and q34 in the swapped orientation. If both optimum witnesses saturate the respective q at the common reference a0, their two optima shift by exactly \(-141(a-a_0)\). Their **difference is invariant under this entire additional discount**, and the existing phase boundaries survive unchanged.

## 2. New full-dimensional three-price polyhedral cell family (EC49FSP-W lift)

Prices: q32 \((1-a)t\), q34 \((1-b)t\), q140 \((1-z)t\), other named observations t>0. Set \(F(a,b,z)=141V(a,b,z)/t\), with V the full unrestricted optimal average cost.

**New exact three-dimensional domain**

\[
\mathcal R_1=\{(a,b,z):31/64\le a\le1,\quad27/64\le b\le29/64,\quad0\le z\le1/8\}.
\]

Throughout \(\mathcal R_1\) the unrestricted native optima obey

\[
\boxed{\begin{aligned}
D(a,b,z)&=F(a,b,z)=306-141a-41b-4z,\\
S(a,b,z)&=F(b,a,z)=\min\{306-141a-41b-10z,\;303-141a-32b-17z\}.
\end{aligned}}
\]

Equivalently, the exact price-exchange cost difference is

\[
\boxed{D-S=
\begin{cases}
6z,&0\le z\le(9b-3)/7,\\
3-9b+13z,&(9b-3)/7\le z\le1/8.
\end{cases}}
\]

For b≥31/72 the first expression holds over the entire allowed z interval. The nontrivial separating segment joins (b,z)=(27/64,51/448) to (31/72,1/8), independently of a. All strictly positive z give D>S. The domain has positive three-dimensional volume \(33/16384\).

**Why this new domain is certified:** PR #2712's EC49FSP-W certificate gives exact unrestricted Bellman values over the entire b,z rectangle at a0=31/64 by six precise polygon vertices, and exhibits complete original-named trees with vectors (U,N32,N34,N140): direct (306,141,41,4), swapped P0 (306,41,141,10), swapped P1 (303,32,141,17). The direct tree has N32=141 and both swapped trees have N34=141. Apply the saturated-ray lemma for every point (b,z), separately on each optimal region. No extrapolated Bellman experiment is needed for the intervening a values.

## 3. Exact extension of the four-phase corner through q32/q34 zero price

Fix \(b=27/64\), extend \(a\in[31/64,1]\) and \(z\in[0,1/4]\). Set \(\Pi(U,m,n,k)=U-141a-mb-kz\) for direct vectors with N32=141, and \(\Psi(U,m,n,k)=U-141a-mb-kz\) for swapped vectors with N34=141 (m is N34 for direct, N32 for swapped). The complete costs are given explicitly:

\[
\boxed{\begin{aligned}
D&=\min\{306-141a-41b-4z,\quad307-141a-41b-10z\},\\
S&=\min\{306-141a-41b-10z,\quad303-141a-32b-17z,\\
 &\hspace{29mm}305-141a-32b-29z,\quad304-141a-28b-32z\}.
\end{aligned}}
\]

Direct transitions at z=1/6; swapped transitions at z=51/448,1/6,11/48. In this entire 2D rectangle the price-exchange penalty is

\[
\boxed{D-S=
\begin{cases}
6z,&0\le z\le51/448,\\
13z-51/64,&51/448\le z\le1/6,\\
19z-115/64,&1/6\le z\le11/48,\\
22z-159/64,&11/48\le z\le1/4.
\end{cases}}
\]

All six 141-profile original-named witness trees and the five exact original Bellman phase vertices are already preserved in PR #2712. Every direct witness has N32=141; every swapped witness has N34=141. The saturation lemma proves the whole extension, including the a=1 zero-price boundary.

## 4. A second, longer-z exact saturation slab from EC49FSN

A different base section from PR #2706 has \((a_0,b)=(1/2,7/16)\) and globally exact z phases on [0,1]. Its direct optimum is represented by the following original tree vectors until z=107/248:

\[
(306,141,41,4),\ (307,141,41,10),\ (309,141,41,16),\ (313,141,47,20).
\]

For the exchanged orientation F(b,a,z), the saturated q34 optimal vectors on [0,107/248] are

\[
(306,41,141,10),\ (303,32,141,17),\ (305,32,141,29),\
(304,28,141,32),\ (309,28,141,46),\ (311,28,141,51).
\]

Their costs use \(U-aN_{32}-bN_{34}-zN_{140}\) before exchange and \(U-bN_{32}-aN_{34}-zN_{140}\) after exchange. By exactly the same lemma, for **all real**

\[
\boxed{1/2\le a\le1,\quad b=7/16,\quad0\le z\le107/248}
\]

both unrestricted optima equal the respective minimum of the four/six displayed tree cost planes. Equivalently,

\[
\boxed{F(a,7/16,z)=F(1/2,7/16,z)-141(a-1/2)}
\]
and
\[
\boxed{F(7/16,a,z)=F(7/16,1/2,z)-141(a-1/2)}.
\]

Their exact difference equals the already certified EC49FSN difference on [0,107/248], strictly positive for z>0 and zero at z=0. At z=107/248 a saturated direct witness still attains the old optimum, even though it ties a nonsaturated alternate.

## 5. New original-native exact computational crosschecks

Reusing the frozen original 228-observer primary solver, 12 new endpoint/interior pairs were recomputed at a=1 (8 from the first two domains, 4 from the second slab). Values are exact fractions. Representative pairs D/S:

- (a,b,z)=(1,27/64,0): 9453/64 and 9453/64.
- (1,27/64,1/8): 9421/64 and 1171/8, gap 53/64.
- (1,27/64,1/4): 9357/64 and 2291/16, gap 193/64.
- (1,29/64,1/8): 9339/64 and 9291/64, gap 3/4.
- (1,7/16,1/3): 6947/48 and 1681/12, gap 223/48.
- (1,7/16,107/248): 70833/496 and 33665/248, gap 113/16.

The alternate, independently reconstructed original 94-family/CSV oracle also agrees at two new swapped a=1 anchors, z=1/8 and z=1/4, b=27/64. The precise 12 entries, state counts and source scope are in the accompanying EC49FSQ machine certificate. All other continuous points are proved symbolically by saturation, not by interpolation from the 12 experiments.

## 6. Type scope, status and frontier

This is a theorem of the finite native BRC16943 observer-identification optimization. The typed object is each original physically named deterministic observation and its joint response on one of 141 profiles. It neither compresses different named sensors nor changes the original state/profile population. The price variables are dimensionless observer-cost discounts, **not heartbeat time or native spatial axes**; P000 remains unchanged.

Evidence status: AUTHOR_PROVED / EXACT_PRIMARY_FINITE_EXHAUSTIVE_ON_NEW_ANCHORS / INDEPENDENT_PARTIAL / NOT_REVIEWED. Global continuum claims depend on previously published, exactly scoped primary Bellman vertex theorems and their full original-native feasible trees (PR #2706, PR #2712), plus the independent saturation proof above. Published in a portable research branch; not formal Task CLAIM, Result, Review, Foundation admission or Activity checkpoint.

Prior research metadata: historical Researcher EM-DIRECT-8454C6, SID MCP-44cfc4e6f2094f96861854ebefc77e84, Activity RA-ED136F89271FD89288F3E58D. Original control continuation request r4-ec49fso-20261118-1332-own-current-continuation-01 has verified terminal FAILED / CANONICAL_REJECTED: unknown current immutable task publication. No owner claim or authenticated execution permission is inferred from that metadata.

**Open scientific target:** find the sharp boundary of saturated q32/q34 optimality as z increases beyond 107/248 at b=7/16, and locate a lower-a boundary for the first three-dimensional wedge; determine whether additional non-saturated optimal-tree cells touch those faces. Those questions require new original Bellman/feasible-tree evidence, rather than an unsupported extrapolation of the saturation rule.
