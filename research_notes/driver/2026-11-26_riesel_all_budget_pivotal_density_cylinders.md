# Riesel R4: positive-density pivotal cylinders at every budget b >= 11

2026-11-26. Informed Driver mathematical extension of the original EM-DIRECT-970E1C construction (RA-D2EC212845B63844081F9A14). Review/derivation, not a new Task claim or native Result/Review. No assertion of novelty relative to all unpublished author work.

## Exact scope and dependencies

Use the original twenty-prime P, F_n(a)=a^2 2^n-1, n>=1, proper-prime supplementary covering minimum delta_P, and the fixed 74-prime progression R4={A4+S4 j:j>=0}. See the [R4 definition](https://github.com/awdawmip/enterprise-math/blob/9b3680ea1c07b1364af5464a3469313ee616d408/research_notes/portable_direct/riesel_nine_frontier_20261124/r4/proof.md). All odd indices are already covered by P; 2 never divides F_n. Fixed inventory primality and the author's standard primitive-divisor theorem remain hypotheses/dependencies as in the [all-budget binary-leaf lower construction](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md), sections II-III, checked in the [Driver audit](https://github.com/awdawmip/enterprise-math/blob/0a9461102589067ad8b3bf4b982f0f8b1e5b0f5f/research_notes/driver/2026-11-25_riesel_r4_fixed_geometry_binary_lower_audit.md). Preserve the author's original theorem and authorship.

The earlier lower construction gives a pair of CRT prescriptions: ten anchors, t=b-11 earlier binary leaves, a target prime q of raw order D=5040*2^t, and two common repair primes. In the on prescription the target has one specified even-index phase; in the off prescription it is zero. All other selected/fixed phases agree. Its finite private-point argument excludes all lower-cost alternatives, giving exact costs b and b+1. We widen the single residue prescriptions to entire local fibers without changing the relevant covering predicate.

## 1. Even-phase quotient and exact local weights

For an odd prime p not dividing S4 write d=ord_p(2) and m=ord_p(4)=d/gcd(d,2). The condition at exponent n=2u is a^2*4^u=1 (mod p), equivalently a=+2^(-u) or -2^(-u) (mod p). Different u modulo m give disjoint two-element residue pairs, since equality up to sign is equivalent to 4^(u-v)=1. Every even-index active residue belongs to one of these m pairs. The remaining p-2m residues, including zero, activate no even index. Thus the exact weights under a uniform free root coordinate are:

* each particular phase: 2/p;
* inactive symbol: (p-2m)/p.

This uses even-index phases, not the larger possible set of residues activating some odd exponent; the latter is irrelevant because P already covers all odd exponents. The inactive count is positive: 2m divides p-1 (the even subgroup plus its negative), hence p-2m>=1.

## 2. Finite cylinder theorem

Let b>=11 and use any choice of the author's target q and other primes in the binary-leaf construction. Define U_b to contain all free odd primes p with ord_p(2)<=6720*2^(b-1). This set is finite since each p divides 2^d-1 for some d in the finite range. The author's private-point argument, applied to the old period 6720, gives this cutoff for inclusion-minimal periodic supplements of size <=b. In particular a putative proper cover of size <=b yields an inclusion-minimal periodic cover of at most that size, whose free primes lie in U_b. For sufficiently large roots every fixed prime in the finite set is a proper divisor whenever it divides F_n. Consequently the cutoff also governs the eventual proper-cover decision. Any finite exceptions do not affect relative natural density.

Let E be the finite set of free selected primes other than q in the paired construction, including the common repairs and any free anchors. Set I=U_b minus (E union {q}). Keep each p in E in its specified phase, but allow either sign. Keep each p in I inactive, but allow all p-2m_p inactive residues. The two cylinders C_on and C_off then specify, respectively, the target phase of q (two residues) or any of its inactive residues. The fixed inventory R4 stays unchanged, and all other free primes are unrestricted.

For every sufficiently large root in C_on the original b-prime cover works, while no cover of size <=b-1 is possible: any such periodic subcover would use only fixed coordinates and U_b and would have exactly the same even-phase options as in the original exclusion argument. For C_off the common repair cover works at b+1 and no cover of size <=b is possible by the same finite exclusion. The private-point and leaf witnesses are unaffected by signs or inactive-state substitutions. Thus C_on is contained, up to finitely many roots, in exact cost b, and C_off in exact cost b+1.

All moduli are distinct free primes coprime to S4. Hence CRT gives the following exact relative natural densities of the cylinders in the progression R4. With

    K_b = product_{p in E}(2/p) * product_{p in I}((p-2m_p)/p),

the densities are

    dens_R4(C_on) = K_b * 2/q,
    dens_R4(C_off) = K_b * (q-2m_q)/q.

They are disjoint and both strictly positive. The exact-cost sets themselves also have rational natural densities: use the finite cutoff for budgets b-1,b,b+1 and take differences of their eventually periodic predicates. This establishes a quantitative (finite-product, not yet evaluated for the huge inventories) lower bound on each of those exact densities. For q the raw order D is even, so 2m_q=D and the ratio of the two certified cylinder densities is (q-D)/2. This is a ratio of these particular cylinders, not the ratio of the full exact-cost densities.

Equivalently, conditioning on the remaining free coordinates in the common cylinder of mass K_b, at least the two target-phase residues give success of delta_P<=b and every inactive target residue gives failure. Two independent uniform draws of q with those other coordinates fixed therefore give different predicate values with conditional probability at least 4(q-D)/q^2. Averaging yields the unconditional resampling influence lower bound K_b*4(q-D)/q^2. This supplies a positive-measure refinement of the original essential-coordinate witness rather than a new maximum-order result.

## 3. Named witness check

The original budget-12 named witness q=20161 has ord_q(2)=10080. Thus m_q=5040, active count 10080 and inactive count 10081. With the other coordinates restricted to its common CRT cylinder, its one exact target phase has mass 2/20161 and its inactive symbol has mass 10081/20161. The certified off/on cylinder ratio is 10081/2. This does not evaluate the common mass or the full cost-12 density.

Executed exact arithmetic: trial-prime enumeration of all 302 odd primes p<2000; for each, directly enumerate the subgroup generated by 2 and its negatives and compare its cardinality to 2*ord_p(4). Zero mismatches. Direct multiplicative-order loop for 20161 returned 10080. Reproduction (integer JS, exact in these small ranges):

```js
function ord(p){let a=2%p,d=1;while(a!==1){a=2*a%p;d++}return d}
let checked=0,bad=[];
for(let p=3;p<2000;p+=2){
 let prime=true;for(let j=3;j*j<=p;j+=2)if(p%j===0){prime=false;break}
 if(!prime)continue;
 const d=ord(p),m=d/(d%2?1:2),s=new Set();let x=1;
 for(let j=0;j<d;j++){s.add(x);s.add(p-x);x=x*2%p}
 if(s.size!==2*m)bad.push(p);checked++;
}
const p=20161,d=ord(p),m=d/2;
console.log({checked,bad,p,d,m,inactive:p-2*m,ratio:(p-2*m)+"/2"});
```

## 4. Consequence and next question

At budget 18 the previously completed informed mathematical audit supports the maximum essential raw order 645120, with all 27842 high-period exclusions archived ([consolidated audit](https://github.com/awdawmip/enterprise-math/blob/14d43393c6fd07db28fd05c8a826bee82be00c4a/research_notes/portable_direct/2026-11-26_riesel18_consolidated_independent_mathematical_audit.md)). For the pivotal predicate at that budget, the sharper finite observer bound can reduce the inactive-coordinate inventory for the influence estimate; an exact-cost pair additionally needs the lower-budget predicate kept fixed. This is a useful counting interface for future density classification: independent local phase weights, exact Boolean union rather than counting overlapping cover dictionaries, and a certified pivotal subset. Full density, minimum support and least root are not computed here. Budget-19 sharpness is not settled by this argument. No new formal proof-checker or Native Review/Result/Task acceptance asserted.
