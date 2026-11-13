# R716 — Exact dihedral fibers of area-optimal odd BRC microphase rings

Date: 2026-11-11 Asia/Shanghai.
Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Immediate source: R715, research_notes/portable_direct/2026-11-11_R715_odd_ring_joint_profile_theorem.md, research commit ccc019123731b3ef59497c7f064151b0e3c00c7f.
Mode: independently derived author-side theorem in the explicitly declared R709b–R715 candidate scheduler; not a native Result or independently reviewed statement.

## Setup: population, BRC provenance, and observers

Fix an odd m >= 5. Let P be the ten two-element subsets (p,q), 1 <= p < q <= 5, representing the two phases at which each physical edge executes its two oppositely typed, separately source-labelled positive TRANSFER events. A rooted labelled history is a cyclic word w=(w_0,...,w_{m-1}) with w_i in P and w_i intersect w_{i+1 mod m} empty: no Cell is in two elementary events in a phase. The two source types on an edge can be ordered either way. For the phase-pair word put

e(p,q)=q-p-1; A(w)=m+sum_i e(w_i);
D_t(w)=# {i: p_i <= t < q_i} for t=1,...,4.

We study exactly A=m+3, the area minimum from R712. A phase-pair history and a fully source-typed history are different carriers. The observer (m,A,D) and the completed positive event ledger forget the physical edge root and (unless expressly retained) its source-type order bits. We classify the reindexing fibers; no BRC provenance is erased in the underlying histories.

The dihedral group D_m (order 2m) acts on the cyclic word by rotations i -> i+k and spatial reversal i -> k-i. This reversal reindexes physical edges and does not reverse physical time/phase order. The profile D_t and A are invariant under this action.

## Theorem R716-A: the dihedral action is free

For every odd m >= 5 and every area-optimal legal phase-pair history w, its stabilizer under D_m is trivial. Every orbit contains exactly 2m distinct rooted oriented histories.

Proof.

(1) A nontrivial rotational stabilizer would make w a repetition r=m/d>=3 times of a shorter cyclic legal word u of odd length d=gcd(m,k). The zero-length, length-one and length-three odd closed words are impossible because adjacent stage pairs are disjoint and the Petersen graph K(5,2) has girth five. For an odd legal closed word u of length d>=5, R712's Petersen excess lemma yields sum_{i<d} e(u_i) >= 3. Consequently w has total excess at least 3r>=9, contradicting A(w)-m=3. Thus no nontrivial rotation fixes w.

(2) Each reflection of an odd cycle fixes the midpoint of some physical edge of the index cycle, exchanging two adjacent positions i and i+1. If w is fixed by this reflection, it must satisfy w_i=w_{i+1}; these two equal two-element stage sets are not disjoint, contradicting legality. Thus no reflection fixes w.

The two cases exhaust D_m. QED.

## Theorem R716-B: exact unrooted/orientation-free residual fibers

From R715, for k=(m-5)/2 and unique r,s,t>=0 with r+s+t=k, the profile

D=(2+r+s, 2+t, 2+s, 2+r+t)

has N_m(D)=8m*binom(r+s,s)*binom(r+t,t) rooted phase-pair histories; every other D has zero. Since each D-specific set is stable under the free D_m action, the exact number of spatially unrooted, unoriented (bracelet) histories of this profile is

Q_m(D)=4*binom(r+s,s)*binom(r+t,t).

In particular the number of bracelet histories simultaneously attaining minimum area A=m+3 and minimum peak max D_t=ceil((m+3)/4) is

J_m = 4                                 if m=4n+1;
J_m = 4*(2+n^2)                       if m=4n+3, n=(m-3)/4.

For m=4n+1 the four classes exist for every n>=1, despite an increasing number of physical Cells. For m=4n+3 the number grows quadratically in n. The old fixed-edge count was V_m=2m J_m.

For the fully source-typed histories, each edge independently has two temporal type orders. The dihedral action still acts freely because its projection to phase-pair words acts freely, so the exact typed bracelet counts are 2^m Q_m(D) per profile and 2^m J_m jointly optimal.

## Exact memory interpretation and scope

For a known D-specific nonempty fiber, the number of distinct rooted phase-pair histories is 2m Q_m(D), while the number of bracelet histories is Q_m(D). Reconstructing an exact rooted orientation from a specified bracelet representative requires choosing one of exactly 2m frames, hence ceil(log2(2m)) bits in worst-case fixed-length binary encoding. Retaining every per-edge source order bit adds m bits when reconstructing the fully typed rooted history.

This is a raw-history reconstruction theorem, not yet a safe quotient for a future S3/V39 observable. R708's root-dependent holonomy is an explicit reason to keep the frame when that future observer is not dihedral invariant. The next step is to determine which dihedral transformations preserve the exact frozen Link/Port and V39 update interface, and then count the resulting observer-specific suborbits rather than assuming an unrooted state is predictive-sufficient.

## Exact verification

The companion Python program independently enumerates all rooted area-optimal phase-pair words for m=5,7,9,11, checks their orbit sets have size 2m and matches profile counts. It uses a separate exact rooted closed-walk dynamic program for m=13,15,17. Both agree with R715 profile formulas. The companion JSON records all seven tested m and the flag R716_DIHEDRAL_FIBER_EXACT_PASS. Finite checks complement the universal group-action proof; no floating point or arithmetic-precision assumption is used.

BRC resolution: COMPOSE_APPLIED (R712 Petersen excess + R715 profile fibers); exact population: source-labelled event histories; counted observer: four microphase residual boundaries and optional dihedral reindexing. Source/ontology: frozen P000 V5 at the above pin, with the native three-force closure premise retained. The event scheduler remains a declared candidate until native Link/Port timing admission is checked.
