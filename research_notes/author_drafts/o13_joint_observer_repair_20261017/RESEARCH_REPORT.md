# Enterprise Math / BRC O13 — Joint-observer repair theorem (AUTHOR DRAFT, 2026-10-17)

Scope: external finite auxiliary hypergraph over F_5. NOT a theorem about the P000 native 6-axis Cell space. This file is author evidence only, not a canonical Result, driver review, CLAIM, or Foundation update.

Pinned input: GLOBAL_KNOWLEDGE_V1 main b846271bb6e204d8ef57d68086cdd2d0782f9d02; Enterprise Math main 92496320c34767dc1f63b6e18d76170cb6b59f47. Previous frontier: O13 observer-horizon finite certificate, 2026-10-17.

## Exact definitions
Set Q = F5* x F5, with vertices ordered (x,s) for x=1,2,3,4 and s=0,...,4. Define E(a,s,d) = {(a,s),(2a,s),(3a,s),(a,s-d),(3a,s+2d)} for a,d !=0 and s in F5, all coordinates mod 5. These give 80 distinct five-point edges. A state T is a subset of holes, with surviving edges E disjoint from T; nu(T) counts surviving edges. H_j(T;v) counts all j-element U from Q\T such that nu(T union U)=v. Hminus_j(T;v) counts j-element V subset T such that nu(T\V)=v. The comparison group Gamma consists of (x,s)->(c*x, alpha*s+beta), c,alpha !=0 and beta arbitrary in F5; |Gamma|=80. J224 counts surviving vertex triples for which their three pair codegrees sort to (2,2,4).

For a column x write S_x(T) = {s:(x,s) in T}. For |S|=3 subset F5, mu(S) is its unique element that is the middle of a nondegenerate arithmetic progression inside S. Define
K43(T) = sum_{x != y, |S_x|=4, |S_y|=3} 1[ mu(S_y) not in S_x ].
All these quantities are Gamma invariants. In particular global affine changes of s preserve the midpoint relation.

## New sharp finite statement
For every pair of nonempty hole states T,T' with 1 <= |T|,|T'| <= 7, define
Phi(T)=(|T|,nu(T),H_1(T),H_2(T),Hminus_1(T),Hminus_2(T),K43(T)).
Then Phi(T)=Phi(T') iff T'=g(T) for some g in Gamma.

This is an exact, computer-assisted finite theorem: an exhaustive enumerator considers every sum_{k=1}^7 binom(20,k)=137,979 nonempty hole sets, partitions into exactly 1,804 Gamma orbits, verifies the Gamma action preserves all 80 edges and each field, and computes 1,804 distinct Phi values. Independent C++17 and independently reimplemented Python integer enumerations agree. Per k, orbit counts are 1,5,17,72,205,512,992. Starting from (k,nu,H1,H2), the class counts are 1,5,17,72,205,507,786; adding only J224 gives 1,5,17,72,205,507,791. Adding both backward histograms Hminus1 and Hminus2 gives 1,5,17,72,205,512,991. Adding K43 then gives all orbit counts, including all 992 orbits at k7.

When the four extra candidate fields are restricted to {J224,Hminus1,Hminus2,K43}, all 16 candidate subsets are checked: only the triple {Hminus1,Hminus2,K43} and the quadruple including J224 separate all 1,804 orbits. Thus the triple is uniquely minimum *among this candidate field family*, not among every possible observer.

## Exact counterexample — backward observations do not suffice
With bit order Q=(1,0..4),(2,0..4),(3,0..4),(4,0..4), take masks 8032 and 8096.
T_C={(2,0),(2,1),(2,3),(2,4),(3,0),(3,1),(3,2)}.
T_D={(2,0),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2)}.
Both have nu=2, identical H_j for *all* allowed forward horizons j, identical Hminus1 and Hminus2, identical J224=0 and identical unlabelled triple-codegree multiset. Yet K43(T_C)=0 while K43(T_D)=1: the s-midpoint of S_3={0,1,2} is 1, absent from S_2(T_D), but present in S_2(T_C).
They cannot be Gamma-equivalent: the unique four-hole and three-hole columns force c=1. The only affine s transformations preserving {0,1,2} are identity and s->2-s; neither maps the unique missing coordinate 2 in T_C's four-hole column to the missing coordinate 1 in T_D.

A different six-hole collision (masks 63 and 1086) has equal full unlabelled forward observer polynomials and even isomorphic surviving unlabelled hypergraphs, yet different column populations (5,1,0,0) versus (4,1,1,0). Thus no observer depending solely on the isomorphism type of the unlabelled surviving hypergraph can solve the general orbit problem.

## Future-operations guarantee and nonclaims
For the restricted domain 1<=|T|<=7, and operations consisting of addition of any unlabeled one hole or removal of any unlabeled existing hole, retaining only moves whose endpoints stay in the domain, the Gamma action is equivariant. Since Phi separates orbits, it exactly predicts the multiset of resulting Phi states. By induction it retains every finite unlabeled operation sequence in this restricted domain. It does NOT retain fixed labelled-port interventions, operations leaving k<=7, the original integer carry transfer operator, nor native six-dimensional P000 dynamics. No transfer bridge was established.

## Independent reproducibility and admitted limit
Evidence generated locally includes: orbit_scan.cpp/json, repair_scan.cpp/json, minimal_repair.cpp/json, verify_global.py, verify_pairs.py, independent_global_certificate.json, independent_witness_certificate.json, validation.log, run_checks.sh. Two independent languages reconstruct edges and group directly, use exact integer arithmetic and cross-check all orbit/cardinality counts. This is author's finite classification, not independent Driver review.

Native em_control_tasks returned CONTROL_QUOTA; native em_session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). The active Owner and task CLAIM therefore remain unverified; this author draft is not formally admitted.

NEXT: advance to k=8 using equitable partitions of the 80-element group, test whether K43 requires augmentation, and seek a compact orbit-witness / constraint certificate independent of total-subset enumeration. Also determine the minimal context necessary to lift restricted observer sufficiency to named-port transitions without erasing joint structural residues.
