# Nollm layered observer audit: Coverage shape and sampling-dependent thickness

Status: RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED
Progress-Event-ID: NOLLM-LAYER-MEASURE-AUDIT-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Date: 2026-09-09
Mode: TASK_RESEARCH / direct user continuation; no formal Task-ID or CLAIM
Source snapshot: enterprise-math@1f8effce7520abd30c6b5b66fff167e12eea0e25
Parents:
- research_notes/nollm_hecke_radix_multiplicative_field_sync_20260908.md
- research_notes/nollm_hecke_tree_zeta2_thickness_bridge_20260908.md
Executable: experiments/nollm_hecke_layer_views_20260909_c6c82.py
Executable immutable commit: c39e5b58766e214af50966e6fe279eb7c7d7af3b
Executable Git blob: 2bffcb42e21e67c96a0ab07dd95ec0ddc3f5e1a1

## Scope and observation conventions

This continues the already-persisted p=5 construction, rather than claiming its rediscovery.
It studies ordinary integer lattices as a mathematical slice/comparison model. Rank d below
is not a claim about physical world dimension or a modification of P000.

The displayed vertical coordinate k is radix expansion depth, NOT a Nollm physical layer.
Each planar layer is divided by sqrt(5^k) solely for comparable visual scale. The first five
displayed layers contain all points. An interactive eight-layer viewer subsamples only the
display of large layers (at most about 4,000 points per layer); all statistics and residue
checks use complete data. No Nollm runtime implementation or parameter was changed.

## 1. Exact endpoint map is not isotropic Coverage

Reuse the eight determinant-5 matrices in the parent synchronization note, with application
order P_k=M_k...M_1. Let S_0={0}, S_k=D_k+M_k S_(k-1). For the original digit sets
D_k={(-2,0),(-1,0),(0,0),(1,0),(2,0)}, exact enumeration verifies:

- |S_k|=5^k, k=1,...,8;
- P_8=[[0,-625],[625,625]]=625 omega;
- S_8 maps bijectively to every pair modulo 625, with 390,625 distinct points.

Thus the torus quotient is exactly uniform, and P_8 is conformal. Nevertheless the
ordinary Euclidean Coverage cloud is not isotropic. In the hex basis
E=[[1,1/2],[0,sqrt(3)/2]], its axial covariance is exactly

C_8=[[146056,49592],[49592,50516]].

The Euclidean standard-deviation axis ratio sqrt(lambda_max/lambda_min) is
3.788961510834..., while the endpoint map's singular-value ratio is 1.

Rigid camera rotation preserves this axis ratio. It cannot remove the anisotropy.
The finite torus quotient and the Euclidean point cloud are different observers:
residue completeness does not imply a round, connected or spatially uniform cloud.
This does not contradict the parent's finite residue-bijection statement.

## 2. A small exact digit optimization improves geometry without changing arithmetic

Restrict D_k to {0,+u,-u,+v,-v}, where u,v are two of the three nearest-neighbor axial
directions e1=(1,0), e2=(0,1), e3=(1,-1). Require five distinct residues modulo M_k.
Exactly two sets are legal for each of these eight matrices, hence 2^8=256 possibilities.

Enumerate all 256 choices. Optimize the endpoint second-moment anisotropy with an exact
rational objective, not a floating search decision. Store H=5 C in axial coordinates.
Then H_k=M_k H_(k-1) M_k^T+D_k^T D_k, and the objective is

tr(E H E^T)^2/det(E H E^T)
=4(H_00+H_01+H_11)^2/(3 det H).

One minimizer uses direction pairs, in step order:

(e1,e3), (e1,e2), (e1,e2), (e2,e3),
(e1,e3), (e1,e3), (e1,e2), (e1,e3).

The exact minimum objective is 57576669888/10831034651.
The final H is [[245462,-6528],[-6528,176674]].
The resulting standard-deviation axis ratio is 1.726374382772....

Both constructions still have all 390,625 distinct endpoint residues. Exact convex-hull
and lattice-site counts give:

| observer | original digits | compact digits |
|---|---:|---:|
| endpoint map singular-value ratio | 1 | 1 |
| Coverage standard-deviation axis ratio | 3.788961510834 | 1.726374382772 |
| lattice sites inside/on convex hull | 1,076,065 | 628,663 |
| occupied fraction of those sites | 0.363012457426 | 0.621358343023 |
| endpoint residue count modulo 625 | 390,625 | 390,625 |

This is an exact optimum ONLY within the declared 256-element digit family. It is not
a global optimum over digit sets, matrices or all field architectures. Second-moment
improvement and hull occupancy are not proofs of all-scale equidistribution.

## 3. Repeated exact returns do not erase Coverage shape memory

For a uniformly chosen independent digit word, normalized as an observer (not an
uncertainty kernel), covariance obeys

C_k=M_k C_(k-1) M_k^T+Q_k,

where Q_k is the covariance of D_k. The mean is zero for the centered sets.
Individual deterministic shear amplitudes can cancel in P_8, but this sum of transported
positive covariances need not become isotropic.

For repeated copies of the original eight-step block, let A=625 R_(60 degrees) in Euclidean
coordinates and Q=C_8. After t blocks,

C^(t)=sum_(j=0..t-1) A^j Q (A^j)^T.

Exact recurrence with numerical spectral readout gives:

| radix depth | standard-deviation axis ratio | long-axis angle modulo 180 degrees |
|---|---:|---:|
| 8 | 3.788961510834 | 18.6331410771 |
| 16 | 3.788909545952 | 78.6330775639 |
| 24 | 3.788909545819 | 138.6330775641 |
| 32 | 3.788909545819 | 18.6330775641 |

This is a covariance computation, NOT enumeration of 5^32 points.
There is a near three-block orientation cycle in this observer, not progressive rounding.
It comes from the deliberately chosen 60-degree block rotation and the 180-degree
identification of an ellipse axis. It is not evidence for a universal arithmetic period 24.

## 4. Correct the higher-rank extrapolation: fixed-index layers give d(d-1), not d

For d>=2, let a_(d,p)(r) count all index-p^r sublattices of Z^d, with each distinct
sublattice counted once. Classical Hermite normal form gives

sum_(r>=0) a_(d,p)(r) t^r = product_(i=0..d-1) (1-p^i t)^(-1),

equivalently

a_(d,p)(r)=product_(i=1..d-1) (p^(r+i)-1)/(p^i-1).

Let J=max{j: L is contained in p^j Z^d}. Scaling L=p^j L' is a bijection, so at
fixed index p^r,

P_r(J>=j)=a_(d,p)(r-dj)/a_(d,p)(r),

with a(s)=0 for negative s. In particular the exact J histogram is

a(r-dj)-a(r-d(j+1)).

Since a(r) is asymptotic to c_(d,p) p^((d-1)r), for each fixed j,

P_r(J>=j) -> p^(-d(d-1)j),
P_r(J=j) -> (1-p^(-d(d-1)))p^(-d(d-1)j).

This is a proved derivation from the stated classical count. The parent's suggestion
that the exponent might simply become d is incorrect for this fixed-index sampling
measure. Scaling consumes d index powers, AND the layer population grows at rate
p^(d-1) per index exponent. Both factors are needed.

At p=5, depth r=24, exact count ratios give:
d=2: about 0.04; d=3: about 0.000064; d=4: about 0.000000004096.
Their limits are 5^-2, 5^-6, 5^-12 respectively, not 5^-d.

The executable checks 500 local count identities: d=2,...,6, p=2,3,5,7, r=0,...,24.
It independently enumerates every rank-two column HNF for p=5, r=0,...,8 and verifies
the common-content histograms. Numerical tests supplement, rather than replace, the derivation.

## 5. Pooling all index layers changes even the rank-two law to inverse fourth power

A different, natural interpretation of 'all layers' is to choose uniformly from all
distinct sublattices of index at most X. Let G(L) be the greatest positive integer g
such that L is contained in g Z^d, and write F_d(X) for the number of such lattices.

The same exact bijection now gives

P_X(g divides G)=F_d(floor(X/g^d))/F_d(X).

Classical sublattice growth is F_d(X)~c_d X^d. Therefore

P_X(g divides G) -> g^(-d^2).

Möbius inversion yields the limiting exact-content law

P(G=g)=g^(-d^2)/zeta(d^2).

The inversion is justified, for example, using F_d(Y)<=C_d Y^d for Y>=1 and the
absolutely summable k^(-d^2) tail; d>=2. For d=2 one can derive the needed growth
directly from F_2(X)=sum_(n<=X) sigma_1(n)~zeta(2)X^2/2.

Concrete rank-two p=5 survival probabilities, computed by exact integer sums:

| X | F_2(X) | F_2(floor(X/25)) | P_X(5 divides G) |
|---|---:|---:|---:|
| 100 | 8299 | 15 | 0.001807446680 |
| 1000 | 823081 | 1342 | 0.001630459214 |
| 10000 | 82256014 | 131934 | 0.001603943512 |
| 100000 | 8224740835 | 13162383 | 0.001600340152 |
| 1000000 | 822468118437 | 1315981693 | 0.001600039763 |

The limit is 5^-4=0.0016, compared with 5^-2=0.04 under the deep fixed-p-index measure.

Therefore the previous zeta(2)/Basel connection remains correct in its specified
fixed-index local product ensemble. It is NOT a measure-independent consequence of
two-dimensional geometry, nor does equality in distribution establish an identity
of the full alias and Hecke dynamical processes.

## 6. Left radix prefixes must not be mislabeled as a nested Hecke walk

P_k=M_k...M_1 describes the radix expansion above, but P_k Z^2 need not lie inside
P_(k-1) Z^2. Exact integrality checks of P_(k-1)^(-1)P_k return:

k=1,2,8: nested; k=3,4,5,6,7: not nested.

Thus the plotted layers are radix layers, not automatically consecutive Hecke edges.
A genuine nested chain can be formed from right prefixes Q_k=M_8 M_7...M_(9-k):
Q_(k+1)Z^2 is contained in Q_k Z^2, and Q_8 has the same final product.
Its intermediate states and digit interpretation must be rederived in that convention.
The prior endpoint factorization and digit bijection remain valid.

## 7. BRC observer/provenance audit

Resolution: COMPOSE_APPLIED.
Population and branch identity are explicit integer digit words and distinct HNF
sublattices. Serial digit composition is affine radix expansion. Preserve digit-set
choice, full coordinate covariance, matrix/frame convention, common-content J/G,
and the sampling measure before projecting to scalar diagnostics.

Two decisive loss witnesses:
- complete torus support loses the Euclidean representative geometry;
- index or dimension alone loses the measure needed to determine the thickness exponent.

Neither positive digit-count mass nor covariance is a complex shear-cancellation
amplitude. No positive branch weight is promoted to a signed/phase mechanism.
The project valuation/skeleton-thickness interface is reused at its declared
pointwise and observer-typed scope. These notes do not claim theorem or Foundation promotion.

## 8. Reproduction and durable frontier

Run the executable with --output <directory>; add --plots for figures and offline HTML.
It checks the endpoint product, digit legality, full residue bijections, exact 256-choice
optimization, 500 local count formulas, direct HNF histograms, rank-two walk masses,
and pooled-index counts. The completed run returned PASS.

Earlier million-point angular experiments and the all-prime minimum-defect table were
not rerun here and are not counted as newly verified results.

Next smallest research unit: jointly optimize valid digit geometry and bounded matrix
paths while preserving a declared sampling measure and a genuine nested-chain frame.
In particular, test whether compact, bounded-neighbor digit rules can keep covariance
and hole fraction controlled over repeated cycles. An optimum for eight steps alone
does not certify that longer-horizon property.

## External mathematical provenance

- Chinta, Kaplan, Koplewitz, The cotype zeta function of Z^d, arXiv:1708.08547.
- Lagarias and Wang, Integral Self-Affine Tiles in R^n I. Standard and Nonstandard
  Digit Sets, JLMS 54 (1996), 161-179, DOI 10.1112/jlms/54.1.161.
- Kirat and Lau, On the Connectedness of Self-Affine Tiles, JLMS 62 (2000), 291-304,
  DOI 10.1112/S002461070000106X.

No novelty priority is asserted for classical counts, content decomposition,
self-affine tile theory, or the standard probability consequences derived here.
