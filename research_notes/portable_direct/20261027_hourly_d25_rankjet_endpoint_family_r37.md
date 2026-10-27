# D25/LIFT R37 — Second rank-jet detects an endpoint hidden from the first two observations at p=37

2026-10-27 (Asia/Hong_Kong). Portable TASK_RESEARCH author mathematics, same logical lane chatgpt-research-hourly-enterprise-math-20260923. Source scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Exact task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, D25/LIFT/JT2 OPEN.

AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This unit consumes, without recredit, R27/R28 finite-field maps and R36 integral p-adic Green inverse and endpoint-precision theorem. It is not native execution, CM, original W/S scalar equality, or independent review.

## Exact new question

R36 produced an unchanged-input, p=37 example in which the W-high/S-mid source observer U_37-M_37 vanishes modulo 37 and needs one endpoint digit only when requested modulo 37^2. But a quotient sufficient for a current scalar observation may not be sufficient under allowed future operations. Let the future operation be a rank jet theta^j, where theta=X d/dX acts on the ORIGINAL polynomial input f, and retain the ORIGINAL W/S source-labelled weights:

~~~
p=37, m=6, a_r=((2/3)_r)^3/((7/6)_r(4/3)_r r!),
h_r=(4/3)_r r!/((11/12)_r(17/12)_r),
v_r=C_6(2r+1)2^r-D_6(8r+13/3)9^r h_r,
C_m=3*216^(2m)*((2m)!)^5/(4m+1)!,
D_m=2*2304^(2m)*((2m)!)^4/(2m+2)!.
~~~

Define the family ell_j(f)=sum_(r=0..5) r^j v_r f_r for j>=0; the 0^0 coefficient at j=0 is 1. Its homogeneous-response endpoint moment is

~~~
Q_j=ell_j(a)=sum_(r=0..5)r^j v_r a_r.
~~~

## Exact rational/finite-field source certificate

A calculation with original rational Pochhammer/factorial coefficients (no altered f, synthetic free-source guess or inferred WZ identity) gives:

| j | Q_j mod 37^2=1369 | Q_j mod 37 | endpoint coefficient (Q_j/c_37) mod 1369 |
|---:|---:|---:|---:|
| 0 | 37 | 0 | 1258 |
| 1 | 1184=37*32 | 0 | 555 |
| 2 | 931 | **6** | 278 |
| 3 | 789 | 12 | 1037 |
| 4 | 1029 | 30 | 1316 |

Here c_37=678 modulo 1369 is R36's exact lifted cutoff unit, c_37=12 modulo37, and the j=2 endpoint coefficient is 278 mod1369 and 19 mod37. Thus the MINIMAL jet order which detects the missing boundary already at first-digit precision is **j=2**, not j=0 or j=1.

To turn this into a complete counterexample for endpoint deletion, take the unchanged original homogeneous input f=a and compare it with f=0. The entire vector of first five Picard–Fuchs sources of f is exactly zero, because L_W a=c_37 X^6. Zero input gives the same endpoint-deleted residual vector. Yet

~~~
ell_0(a)=0 mod37,  ell_1(a)=0 mod37,
ell_2(a)=6 mod37,  ell_2(0)=0 mod37.
~~~

Therefore the first two scalar/rank-jet readouts can factor through the interior sources modulo37, but the combined family containing theta^2 cannot. This excludes even nonlinear endpoint-free reconstructions for the specified original carrier and future operations, not just linear adjoints.

R36 theorem C gives an exact finite-precision resource conclusion:
- for the j=0 scalar alone: at N=1 retain zero endpoint digits; at N=2 retain one 37-adic digit;
- for j=0,1 together: same precision requirement (both Q_j have valuation 1);
- for j=0,1,2 together: at N=1 retain one endpoint digit; at N=2 retain BOTH endpoint digits, because Q_2 is a 37-adic unit.

This is a concrete BRC future-operator/observer failure of a tempting scalar-only quotient at the original target class p=37=13(mod24). It preserves W/S labels, true endpoint source, rank and p-valuation. It does not turn arithmetic rank into a P000 spatial coordinate or prove any original all-prime W/S supercongruence.

## Proof and executed check

The general family endpoint condition follows immediately by applying R36's exact Green adjoint with weights r^j v_r; the sharp precision rule follows from the minimum valuation among their Q_j. The displayed numerical residues were computed independently with exact Python-standard-library Fraction factorial/Pochhammer formulas. The accompanying check file verifies all five Q_j modulo 37^2, their endpoint coefficients, the exact six-term homogeneous recurrence and the original cutoff value. All checks PASS. Finite arithmetic is a p=37 certificate; the universal family precision statement is the algebraic R36 corollary, not an inference from this one prime.

**Next genuine open scientific unit:** use the integral p-adic Green adjoint against the actually unchanged-input R23 low-half p^2-divided W/S defect, incorporating R34/R35's Wilson-free local source jet and R28's endpoint. Determine whether an explicit inter-rank WZ source produces the required genuine compensation at both p=13,19(mod24), including exceptional p=181; if not, retain a nonzero labelled residue certificate. The six fixed-z=2 Hasse J/E channels, finite/infinite Green sources, H0/B0, [X]U mod p^2, semilinear Frobenius eta/kappa, p373 native experiment and independent Driver review remain separate obligations.