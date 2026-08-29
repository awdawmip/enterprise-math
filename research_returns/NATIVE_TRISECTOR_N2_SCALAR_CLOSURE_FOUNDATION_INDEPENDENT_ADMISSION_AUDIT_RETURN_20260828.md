# Native Tri-sector N2 Scalar Closure - Independent Foundation Admission Audit

Status: FINAL_FROZEN / FOUNDATION_N2_CONSEQUENCE_ADMIT / FOUNDATION_PRIMITIVES_UNCHANGED
Date: 2026-08-28
Researcher-ID: EM-NTN2A-56A913
Task: RS-NATIVE-TRISECTOR-N2-SCALAR-CLOSURE-FOUNDATION-INDEPENDENT-ADMISSION-AUDIT
Publication: TP2-4BE981A08B9A260B8E28
Claim: chatgpt-ntn2a-20260828-1335-56a913

## Verdict

PRIMARY_RECOMMENDATION = FOUNDATION_N2_CONSEQUENCE_ADMIT.

The exact native s=3 N2 scalar/set/relation closure survives independent admission audit. No P0/P1 primitive is changed. The admission does not include pointwise intrinsic allocation, an N0 breaker primitive, named physical longitudinal/transverse rails, the arbitrary odd-s comparator family, reverse derivation of native three-ness, or identification of the two unrelated theorem objects whose numerical value is 9.

The parent result was source-exposed and treated as the audit target, not as proof authority. This audit replaces two important parent dependencies with self-contained proofs: q_b=5 by a quadratic-character intersection count, and k_*=9 by direct period-10 analysis modulo 5.

## 1. Balanced-orbit scalar

Use the accepted shell A_r={(a,b,c) in N_0^3:min(a,b,c)=0,a+b+c=r}, |A_r|=3r, and accepted six-frame allocation torsor lambda_f(x)=C_r+p_f(x), C_r=1+3r(r-1)/2.

For r>=2 let O_r=S_3*(ceil(r/2),floor(r/2),0), as a set of distinct states. O_r is S_3-invariant, so its label multiset is frame-independent.

For r=2m the within-shell positions are {m,3m,5m}. For r=2m+1>=3 they are {m,m+1,3m+1,3m+2,5m+2,5m+3}. In both cases the mean position is 3r/2. Therefore

Z(r)=ceil(mean{lambda_f(x):x in O_r})
    =1+(3r^2+epsilon(r))/2,

where epsilon(r)=r mod 2, for every r>=2.

At r=1 the shell label multiset is {1,2,3}; its barycenter ceiling is 2, while the displayed formula gives 3. Hence r>=2 is an exact theorem boundary.

## 2. Independent breaker proof

For odd prime q with q not dividing 6 define

I0={-3x^2/2:x in F_q},
I1={-3x^2/2-1/2:x in F_q},

and Break(q) iff I0 union I1=F_q. This is an N2 predicate, not an N0 breaker primitive.

After scaling by -3/2, Break(q) is equivalent to Q0 union (Q0+delta)=F_q, where Q0 is the set of squares including 0 and delta=1/3.

Both sets have (q+1)/2 elements. For the quadratic character chi,

|Q0 intersect (Q0+delta)|=(q+1+chi(delta)+chi(-delta))/4.

Thus coverage holds exactly when this intersection has size 1.

If q=3 mod 4, the intersection is (q+1)/4, so size 1 forces q=3, excluded. If q=1 mod 4 and delta is square, the intersection is (q+3)/4>1. If q=1 mod 4 and delta is nonsquare, it is (q-1)/4, so size 1 forces q=5. Modulo 5, delta=2 is nonsquare and I0={0,1,4}, I1={1,2,3}. Therefore the unique nonsingular odd covering characteristic is

q_b=5.

## 3. Independent capacity proof

At q_b=5 use the N2 translated scalar family

Z_H(r)=H+(3r^2+epsilon(r))/2.

For r=0,...,9 the base values modulo 5 are

0,2,1,4,4,3,4,4,1,2.

The pattern has exact period 10. The zero positions modulo 10 are:

H=0: {0}
H=1: {3,4,6,7}
H=2: {5}
H=3: {1,9}
H=4: {2,8}

Every phase has a zero in every period, while H=0 and H=2 have exactly one. Hence the sharp maximum consecutive nonzero run is

k_*=9.

Deleting the finite initial shells does not change the eventual period or sharp maximum gap because every residue class modulo 10 recurs infinitely often for r>=2.

## 4. Saturation set and mixed-parity boundary

For even shell r=2m the invariant packet is

{6m^2-2m+1, 6m^2+1, 6m^2+2m+1}.

For nonsingular odd prime q, complete nonzero-residue root saturation requires q-1<=6, because there are only three quadratics. Thus q<=7. Direct roots give

q=5: {1} | {2,3} | {4}
q=7: {2,3} | {1,6} | {4,5}.

Therefore the transverse saturation characteristic set is exactly {5,7}.

Independently, for odd k>=5 in W_k={0,...,k-1}, take distinct u,v of the same parity and w of the opposite parity. All distances |w-u|,|w-v| are odd and at most k-2. If the larger distance is <=k-4, the product is at most (k-4)^2. If it is k-2, the second distinct same-parity point is at distance at most k-4. The endpoint construction realizes the bound. Hence

max |w-u||w-v|=(k-2)(k-4),

and every maximizing unordered distance pair is {k-4,k-2}. At k=9 this is {5,7}. This is an N2 integer grade-gap readout, not a physical rail or embedding metric primitive.

## 5. Closure and semantic guards

Only after the upstream N2 results are fixed do we compute

M_9=(9-4)(9-2)=35,
3M_9=105,
(3M_9+1)/2=53.

Thus the admitted native-instance scalar chain is

3 -> (5,7) -> 9 -> 35 -> 105 -> 53,

with native sector count 3 consumed as an upstream input, never reverse-derived from the target values.

NSA-01: PASS. No hidden primitive is introduced.
NSA-02: PASS. Only invariant-orbit descent from the accepted S_3 allocation torsor is consumed.
NSA-13: PASS. Admission stops at N2 scalar/set/relation strength.
NSA-14: PASS. The transitive dependency chain is explicit.
NSA-18: PASS. None of 5,7,9,35,105,53 is copied into the native premise.

The two values 9 remain typed separately:
- breaker-coprime capacity 9 = a periodic divisibility/readout run length;
- prime-incidence island cap 9 = a separate typed-Cell theorem object from another research line.
No dependency or identity is asserted.

## 6. T-A / T-B / T-C classification

T-A: FOUNDATION_ADMISSIBLE_ONLY_AT_NATIVE_S3_N2_SET_INSTANCE. The native s=3 packet has saturation characteristic set {5,7}; arbitrary odd-s uniqueness and physical centered-lane semantics remain research-only.

T-B: FOUNDATION_ADMISSIBLE_AT_NATIVE_S3_N2_SCALAR_SET_RELATION_INSTANCE. q_b=5, k_*=9, mixed-parity grade-gap {5,7}, and equality with the saturation set are admissible at N2 strength; named rails and the general comparator theorem are not.

T-C: FOUNDATION_ADMISSIBLE_AT_N2_SCALAR_CONSEQUENCE_STRENGTH. With native s=3 as input, 35,105,53 follow exactly. This does not derive native three-ness.

## 7. Durable evidence

Machine dependency ledger:
research_artifacts/NATIVE_TRISECTOR_N2_SCALAR_CLOSURE_FOUNDATION_INDEPENDENT_ADMISSION_AUDIT/dependency_ledger_20260828.json

Regression checker:
scripts/check_native_trisector_n2_scalar_closure_foundation_admission_audit.py

The checker passed r=2..128 over all six frames (3420 label evaluations), all 44 nonsingular odd primes q<200 for the character-intersection identity, all five mod-5 capacity phases, saturation scan q<200 giving exactly [5,7], and 49 odd windows k=5..101 for the mixed-parity extremal theorem. Finite checks are regression only; the proofs above are general.

INDEPENDENCE_STATUS = SHARED_AMBIENT_CONTEXT_DISCLOSED.
SOURCE_EXPOSURE_STATUS = NONBLIND_DISCLOSED.

HARD_TARGET = NATIVE_TRISECTOR_N2_SCALAR_CLOSURE_FOUNDATION_ADMISSION_INDEPENDENTLY_VERIFIED.
FOUNDATION_PRIMITIVE_MUTATION = NONE.

Recommended control-plane action: Driver-review this result. If accepted, admit only the narrowed native s=3 N2 scalar/set/relation consequence as maintained Foundation consequence knowledge, while leaving current P0/P1 primitives unchanged and retaining the full arbitrary odd-s theorem at research-layer strength.