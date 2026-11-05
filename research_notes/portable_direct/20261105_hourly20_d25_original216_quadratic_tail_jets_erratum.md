# D25 — Original 216 quadratic tail jets and corrected reflected Pochhammer certificate

Date: 2026-11-05 (Asia/Hong_Kong). TASK_RESEARCH author-side portable mathematics.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific input: c47e13e4aba0e006366f989d6334d443f6333ae3.
Status: AUTHOR-DERIVED / ALGEBRAIC PROOF / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED.

## 1. Targeted erratum to the reflected endpoint note

In research_notes/portable_direct/20261105_hourly20_d25_original216_reflected_endpoint_constant_space.md at immutable commit 2853ec89d66c3ed0cc37c6bd1f50208032a93b3c, the reflected recursion is correct, but the subsequently displayed closed Pochhammer product has an index shift. For p=6m+1 >=7 prime, with

 b_k=(1/6)_k(1/3)_k / ((k!)^2 2^k),   d_r=b_(p-r)/p^2 mod p  (1<=r<=m),

the verified facts are

 d_1=1/10,
 d_(r+1)/d_r = 36 r^2/((6r+5)(3r+2))    (1<=r<m),

and the **correct** closed expression is

 d_r=(1/10) * 2^(r-1) ((r-1)!)^2 / [(11/6)_(r-1) (5/3)_(r-1)] (mod p).

Derivation: for s>=1, the recurrence factor 36s^2/((6s+5)(3s+2)) equals
2s^2/((s+5/6)(s+2/3)). The product for s=1,...,r-1 starts at 11/6 and 5/3, not at 5/6 and 2/3. The earlier closed expression with denominator (5/6)_(r-1)(2/3)_(r-1) was false. At p=19, r=2, it yields 11 whereas b_(p-2)/p^2 gives 2. The previous d_1, d-recursion, tail valuation theorem, and prefix algorithm do not depend on this erroneous closed expression and pass fresh separate regression below. This is a precise erratum, not an edit to the immutable earlier report.

All denominators in the corrected product are p-units for 1<=r<=m, since the original inverse recursion is defined for exactly this range.

## 2. New theorem: simultaneous zeroth, first and second logarithmic tail jets

For p=6m+1 >=7 prime, define for j=0,1,2 the high-tail moment

 T_j = sum_(0<=a,b<p; a+b>=p) (a+b)^j b_a b_b.

The Clausen high-strip valuation classification from the previous D25 note implies p^2 divides each T_j. Define reflected prefix moments in F_p:

 M_0(i)=sum_(r=1)^i d_r,
 M_1(i)=sum_(r=1)^i r*d_r,
 M_2(i)=sum_(r=1)^i r^2*d_r.

Then, for every such prime,

 (T_0/p^2) mod p = 2 sum_(i=1)^m b_i M_0(i),
 (T_1/p^2) mod p = 2 sum_(i=1)^m b_i [i M_0(i)-M_1(i)],
 (T_2/p^2) mod p = 2 sum_(i=1)^m b_i [i^2 M_0(i)-2i M_1(i)+M_2(i)].

More generally for any polynomial P(X) over Z_(p), the high-tail readout of weight P(a+b), divided by p^2 modulo p, is

 2 sum_(i=1)^m b_i sum_(r=1)^i P(i-r)d_r mod p.

This identity holds for polynomial weights of any fixed degree; degree <=2 is the complete value/first/second logarithmic jet. For P(X)=1+6X, it recovers the previous original-216 weighted high-tail formula T_0+6T_1 without recomputing the quadratic observer.

Proof: in the ordered strip a+b>=p, valuation exactly two occurs only at pairs (i,p-r) and (p-r,i), with 1<=r<=i<=m. All other pairs have valuation >=3. For the surviving pairs, b_i*b_(p-r)/p^2 ≡ b_i*d_r modulo p and a+b=p+i-r ≡ i-r modulo p. Symmetry supplies the factor 2. Expanding (i-r)^j gives the three expressions above. The proof is a finite exact valuation-and-residue argument, not a numerical extrapolation.

The three prefix moments M_0,M_1,M_2 and b_i,d_i can be updated together from the previously proved recurrences. The complete triple is obtainable with O(m) F_p operations and O(1) auxiliary field elements. For any fixed polynomial degree d, O_d(m) operations and O(d) storage suffice. No claim is made about the cost of other observers, primality checking, or the native H0/B0 module.

## 3. BRC observer relevance and exact witnesses

This adds the independent second logarithmic z-derivative port to the previously verified weighted original-216 tail, while preserving the source indices, p-valuations, ordered-pair multiplicity and signs. A zero of the weighted readout can hide nonzero moment coordinates: at p=13,

 (T_0/p^2,T_1/p^2,T_2/p^2)=(6,12,12) mod 13,

but (T_0+6T_1)/p^2=0 mod13. Thus one scalar tail cannot replace the three-component jet for every allowed subsequent operator. It does not identify the frozen parameter derivative Phi_xx, which requires its original source interface.

At p=373 the exact triple is (132,135,181), with 132+6*135 ≡196 mod 373. For p=19 it is (18,18,0), giving 12 for the weighted observer.

## 4. Exact verification and bounds

Standalone Python 3 checker: research_notes/portable_direct/d25_original216_quadratic_tail_jets_20261105.py.
It computes b_0,...,b_(p-1) modulo p^3 from the original recurrence; compares each of the three compressed moment readouts against a separate direct O(p^2) ordered-pair upper-strip convolution; checks the d_1 endpoint and all reflected d_r; and checks the explicit false-formula witness p=19,r=2.

Executed locally for all 35 primes 7<=p<=373, p≡1 mod6: PASS 35/35. These finite calculations test the arithmetic implementation, while the theorem's generality follows from the argument in §2.

No native p373 crystalline divided-power H0/B0, [X]U mod p^2, eta/kappa or Delta_p-R_p experiment is claimed or substituted. The exact R_p RHS remains to be read independently from the frozen original geometric source; the known parent reduction names R_p but does not itself evaluate it. The 216 second-jet triple can support an original z-derivative observer once its explicit map is established, without changing frozen science pins.

## 5. Recovery/continuation

Mother objective: the original D24 LIFT Delta_p=R_p modulo p for all target primes p≡13,19 mod24, together with unchanged p373 native evidence obligations.
Portable current result: corrected reflected Pochhammer certificate plus all-prime quadratic high-strip readout; author-side only, unrevewed/not admitted.
Canonical Source frontier: preserve existing checkpoint, completed_units, contributor history, unfinished unit and do_not_repeat. No claim of owner authority.
Next scientific action: locate the independently defined original R_p and its normalization at the frozen pin; if retrieved, compare p=13,19,373 and test whether the second z-jet is required. The preexisting native H0/B0 and semilinear Frobenius obligations continue separately.
Native pending read request to reconcile: research-hourly20-20261105-1126-native-continuation (queued/running at last observation); use the same request ID.
Service identity/claim/run: no live execution authority established in this author-side turn; do not close/modify old session or staging without its protection readback.
