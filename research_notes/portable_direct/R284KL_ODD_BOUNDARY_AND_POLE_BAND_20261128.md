# R284KL - Odd signed boundary compression, pole-band arithmetic, and exact adjacent-root extension

2026-11-28. Author proof and exact arithmetic; NOT_REVIEWED. Auxiliary R284 arithmetic, not native spatial transfer. Researcher EM-DIRECT-0C386E / TASK_RESEARCH / RA-B82240E8488EF5A1DA5186C4: own recovery r1-20261128-1600-own-recovery returned the original registered session, no runs and no shared execution authority. Owner inventory r1-20261128-1600-owner-read-v1 SUCCEEDED, as-of 2026-11-28T08:00:34.102814Z, 547 total, no LEASED entries, Source 1e49d0a8e86bb0c8626e521997a5891f90912467 current at admission, changed by completion. No shared Task, CLAIM or Result mutation. Global canonical main ac364d42a77b08919c5008ac21420c7e16182349 verified both entry blobs; global P000 V4 projection and canonical blob matched, Source V5 startup projection and ACTIVE worldview read; current research method and portable protocol read. This is a direct continuation with no formal Task binding.

Frozen science: R284KK @3f7a5e7110c23de91e6798bfb6e7ca5a35c1e844:research_notes/portable_direct/R284KK_SIGNED_MOMENT_SEPTIC_AND_FIXED_POINT_CLOSURE_20261128.md, including its original JR/KD/KG pins, original observer definitions and signed moment recurrence. JR @88211c0912397b00536b6c4d6427cab29d4499f2 (integer carrier and small-d exclusion); KD @544d7a97fa075fe62848ae1cf27acdb9bdc7df19 (unique simple legal real root and sign pattern for d>=81). No new independent review of those dependencies.

## 1. Exact odd boundary and contraction

For odd d=2a+1, a>=2, put m=a-1/2=(d-2)/2, q0=-m-2, n=-2, u=m. Retain KK's signed moment boundary B=(d-m)(-1)^d R_m(d). The exact half-integer product simplifies to

B_a=(-1)^a (2a+3)(2a-1)!!(2a+1)!! / [2 product_{i=0}^{2a}(2a+5+2i)].

Indeed the numerator factors of R_m(d) before cancellation of 2 are 2a-1,2a-3,...,1,-1,-3,...,-(2a+1). Its denominator is 2a+5,2a+7,...,6a+5. Multiplying by d-m=(2a+3)/2 and the signed factor gives exactly the displayed expression. In particular all prime support of the numerator is at most 2a+3=d+2; denominator at most 6a+5=3d+2 (and 2). The exact recurrence is

B_(a+1)/B_a = -(2a+1)(2a+5)^2/[(6a+7)(6a+9)(6a+11)].

Each of the three factors in the absolute ratio is strictly below 1/2 for a>=2, so |B_(a+1)|<|B_a|/8. Since B_2=7/14586<1/2048, |B_a|<8^{-(a-2)}/2048. This real smallness is not a p-adic smallness assertion. Keep B in all arithmetic observations.

## 2. Complete quadratic boundary residual

KK's recurrence M0=(m+2-B)/d, Mr=[r(r-1-m)M_(r-1)-B(d+1)^{fall r}]/(d-r), r=1..4, is affine in B. V,Q,A,Z from KK are also affine; E=0. The sign factor (-1)^d is common to all four observations and cancels in their quadratic combination. Expanding the moment evaluator on k^{fall r}, using forward differences (coefficient Delta^r f(0)/r!), gives the exact identity

C(q0,d)=c0(m)+c1(m)B+c2(m)B^2,

where D1=(2m-1)^2(2m+1)^2,
c0=(m+2)^2(4m+7)F7(m)/(8D1),
c1=-(m+2)J1(m)/(4m(m-1)D1),
c2=(m+3)J2(m)/(8m^2(m-1)^2 D1).

Descending coefficient arrays (Horner convention) are
F7=[96,496,644,4,1015,1751,2356,5316],
J1=[1152,15024,84448,266908,553616,992988,1927441,3272963,3776696,2614884,860400],
J2=[16128,265152,2067436,9650156,29629115,62871098,94168943,99087776,70696900,31297632,6675264].

A reproducible algebra check uses the four-step recurrence, linear functionals
V=sigma L((k+1)(d-k+1)^2),
Q=-sigma L((k+1)(d-k)^2),
A=sigma L((m-k)(m+k+2)(k+1)(2(d-k)+1))/(2m(2m+1)),
Z=(-m-2)A+V+Q,
sigma=(-1)^d; then C=-3(m+2)(2m-1)^2 A Q+32(m+3)Z^2. Because degree in B is at most two, direct coefficient comparison proves the displayed identity. The formulas were obtained by exact symbolic rational expansion and independently checked against original finite products for each odd d=5..301.

For m>=3/2, c0,c2>0 and c1<0. Moreover -c1/c0<128: multiply by the positive denominator m(m-1)(m+2)(4m+7)F7. The resulting numerator 128*m(m-1)(m+2)(4m+7)F7-2J1, in the variable t=m-3/2, has descending coefficients
[49152,1197824,12870560,80348784,323694440,884689764,1678831006,2222516445,4045039811/2,4785250423/4,746186073/2,13522221],
all positive. Thus for every odd d>=5,

C(q0,d) >= c0-|c1||B| > (15/16)c0 >0.

This supplies a uniform real sign and an explicit exponentially contracting boundary factor, while retaining its exact signed value for arithmetic. No odd fixed-degree polynomial in m alone is asserted for the entire fiber.

## 3. Pole-band versus far-prime arithmetic

Use JR's integer polynomial P_d(q)=D(q)^2 C(q,d), D=2u(2u+1)(4n+2)D_u D_n, D_v=product_{i=0}^{d-1}(v+i+3). At q0 with odd d the carrier P_d(q0) is a dyadic rational because P_d has integer coefficients. For any odd prime p dividing h=2q+d+2, q-q0=h/2, so if P_d(q)=0 then v_p(P_d(q0))>=v_p(h). This is the cleared-carrier condition; never treat an original pole as a regular rational evaluation.

For 2d+3<p<=3d+2, the odd denominator product of B contains p exactly once, with no numerator p, hence v_p(B)=-1. D(q0) contains p exactly once from D_m; all its other factors are units (D_-2=d!, 4n+2=-6). The rational coefficients c0,c1,c2 are p-integral with their displayed denominators units. Therefore

P_d(q0) = (D(q0)/p)^2 [p^2 c0 + p c1(pB) + c2(pB)^2]
and P_d(q0) mod p = (D(q0)/p)^2 c2(pB)^2 mod p.

All factors except J2(m) in this last expression are p-units, including m+3. Thus if p|h and p does not divide J2(m) in Z_p, the legal integer zero is excluded. A root in this prime band necessarily has J2(m)=0 mod p. This fixed degree-10 observer is applicable precisely to the pole band, not all large primes.

For p>3d+2, both B and D(q0) are units, and the necessary condition becomes c0+c1 B+c2 B^2=0 mod p; with nonzero residue it excludes every integer q in that p-fiber. The signed boundary ratio can be computed modulo p from its exact product/recurrence. Its real exponential contraction is not a reason to set it to zero modulo p.

For both bands the stronger necessary valuation condition v_p(h)<=v_p(P_d(q0)) follows directly from the integer polynomial difference at the two inputs. For p<=2d+3 the denominator-unit assumptions used in the formulas do not hold uniformly; no claim here.

## 4. Executed exact checks and finite closure

Python Fraction checked direct original finite products, exact quadratic expansion, sign, recurrence and bound for all 149 odd d=5..301. For every prime 2d+3<p<=5d in that domain, exact p-adic reduction was independently compared to D(q0)^2 C(q0,d) from the original product. Output:
odd direct identities 149 near primes 3621 near nonzero 3609 far primes 6719 far nonzero 6709
Thus 12 pole-band and 10 far-prime tested pairs degenerated at first order; no independent events assumption. Counts are prime/deficiency pairs, not budgets, and the 22 exceptional pairs are not integer zeros.

Separately reused KK's exact outward fixed-point method with T=2^96 for 3101<=d<=3200, each legal adjacent integer bracket. Prefix ratios enclose by floor/ceil of positive exact rational products, V,Q,A,E by nonnegative interval operations, C by lower(first)-upper(second) and upper(first)-lower(second), denominator T^4. Approximate binary search proposes endpoints only. Exact integer assertions certified all 200 strict signs. JavaScript BigInt independently recalculated the same 200 signs with the same integer bounds from the 100 proposed adjacent brackets; the full output is saved. Minimum positive lower bound and maximum negative upper bound agree between the local Python and JavaScript computations, and first/last rows agree. The signs alone, plus KD uniqueness, establish the extension of JR+KD+KK all-budget exclusion to all integer 3<=d<=3200, q>=64, d^2<=4q, with no q upper bound. This depends on the previous KD author proof, not a new independent review. Unbounded d>=3201 integer exclusion remains open.

Artifacts:
- exact rational check d31a0535aee49a90e0874632be68087ee3ad4b81:research_notes/portable_direct/R284KL/odd_fiber_check.py (Git blob 38e5b2cb1f10b4c472d5db7726cba3c446898647; local SHA256 455ea721d6138122da3ea604b4434496bf294c67f0842671d09d5e2a520326e9).
- exact interval root code 87cbd27a2836e45f8d64523271eb5a1db4afa43b:research_notes/portable_direct/R284KL/root.py (Git blob a0f86abdd607be30a7c0235880b63089fa696278; local SHA256 14ea3836180088707e4ca5624d208b1aa1b38c3312577088e49108603bcc4697).
- full exact bounds cc1101a86e4b40e64e9fdbf9f2938952199c2768:research_notes/portable_direct/R284KL/root_output.txt (Git blob 49530e8a2f0c72ee1279bcf20e7852da30683feb; local Python output SHA256 4d2578ef518e5561b38699bc6d751e238affa2210933bd10120b00bec8c99a5a).
Reproduce with Python 3 + sympy installed: python odd_fiber_check.py; python root.py > root_output.txt. No hosted CI or formal checker.

## 5. Frontier

The odd boundary cannot be discarded: its denominator creates an entire prime band of pole residues, and precisely its squared contribution gives a fixed polynomial J2. Next investigate the 12 pole-band degeneracies via the first correction from c1 and the denominator-removed derivative; jointly compare J2 with KG/KJ/KK observers on the true integer root candidate. Far-prime cases must retain the exact boundary. Do not infer a uniform smooth-number exclusion from this finite sample. Prior finite root checks need not be redone. No task/claim/Result mutation or theorem admission.
