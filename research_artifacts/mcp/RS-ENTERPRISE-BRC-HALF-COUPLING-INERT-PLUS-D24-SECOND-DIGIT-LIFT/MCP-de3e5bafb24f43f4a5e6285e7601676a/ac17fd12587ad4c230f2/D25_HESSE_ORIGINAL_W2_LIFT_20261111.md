# D25/LIFT native Hesse CM-class model over W_2 and its exact second-digit Hasse-coefficient bridge

Date: 2026-11-11 (UTC). TASK_RESEARCH, Researcher EM-ENTERPRISE-9C9163; original Research session MCP-de3e5bafb24f43f4a5e6285e7601676a, activity RA-629C868A22A736334628BEFA; winning claim MCP-6de695b532e654210160c52c; run RUN-d3deee35d5e9e40b9358ebbb. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen original scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Own original-class local theorem/construction and finite exact author checks: UNREVIEWED / NOT_ADMITTED; native crystalline H0/B0 and [X]U experiment NOT_RUN. Previously proved ordinary Hesse trace/norm and rank-one Hilbert-90 notes are CONSUMED, NOT RECREDITED.

## 1. A native original-class curve for every target prime, not just an auxiliary scalar

Let p >= 13 be prime with p = 13 or 19 mod 24. In R_r = (Z/p^r Z)[T]/(T^2-2), with sigma(T)=-T, put t=4+2T and u=(2-T)/4. We have t*u=1 exactly and N(t)=(4+2T)(4-2T)=8. Since (2/p)=-1 and p=1 mod 3, R_1=F_(p^2). With q=p^2,
  t^((q-1)/3)=N(t)^((p-1)/3)=8^((p-1)/3)=2^(p-1)=1 mod p.
The cyclic group F_q^x therefore contains t as a cube. There are exactly three distinct nonzero roots lambda_1 of lambda_1^3=t in F_q; every root uniquely Hensel-lifts to lambda_r in R_r, for all r>=2, because 3*lambda_1^2 is a unit. Thus lambda_r^(-3)=u exactly. Moreover N(t-1)=N(3+2T)=1, so lambda^3-1 is a unit. The Hesse cubic
  E_lambda: X^3+Y^3+Z^3-3*lambda*X*Y*Z=0
is smooth over every R_r and is precisely the original Hesse family at the frozen tagged port, not a newly assumed CM or Frobenius coefficient. Its j invariant (the standard Hesse rational formula) satisfies the identity in Q(T), T^2=2:
  j=27*t*(t+8)^3/(t-1)^3 = 2417472-1707264*T.
The conjugate source port is sigma(j)=2417472+1707264*T. These are the exact two D=-24 CM j-values in the frozen parent. All three choices of cube root have the same j; retain the chosen lambda/root and conjugation as provenance, rather than identify the ports.

One original-model holomorphic differential on affine Z=1 is the Poincare residue
  omega = dx / (3*(y^2-lambda*x)),
understood as the regular residue form across charts. This gives an explicit starting differential for computing a genuine H0/B0 basis, not a claim that the missing divided-power module has been constructed.

## 2. An exact p^2 coefficient observer on this curve

Set n=(p-1)/3; c_k=(3k)!/(27^k*(k!)^3), and A_p(u)=sum_(k=0)^n c_k*u^k (the inherited ordinary Hesse polynomial). Define
  D_p(u)=sum_(k=0)^n c_k*u^k*H_(3k),   H_m=sum_(j=1)^m 1/j, H_0=0.
All denominators are p-units since 3k<=p-1. Let
  C_p(lambda) = [(XYZ)^(p-1)] (X^3+Y^3+Z^3-3*lambda*XYZ)^(p-1).
Direct multinomial extraction gives
  C_p(lambda) = sum_(k=0)^n [(p-1)!/((k!)^3*(p-1-3k)!)]*(-3*lambda)^(p-1-3k).
There is an exact identity over Z_(p)[lambda,lambda^(-1)]:
  C_p(lambda)=(-3*lambda)^(p-1)*sum_(k=0)^n c_k*u^k*product_(j=1)^(3k)(1-p/j).
Indeed (p-1)!/(p-1-3k)! = (-1)^(3k)*(3k)!*product_(j=1)^(3k)(1-p/j), and the signs cancel the (-3*lambda)^(-3k) factor. Therefore the *proved* mod-p^2 bridge is
  C_p(lambda) = (-3*lambda)^(p-1) * [A_p(u)-p*D_p(u)]  (mod p^2).       (*)
Because p-1=3n, its prefactor equals (-27*t)^n, which depends only on the original tagged CM parameter t; the cube-root choice does not change the coefficient. For supersingular source ports where A_p(u)=0 mod p, the divided observer is well-defined and satisfies
  C_p(lambda)/p = (-27*t)^n * [A_p(u)/p - D_p(u)]  (mod p).              (**)
This is a constructive, exact same-original-curve second-digit carrier. The harmonic term is the explicit finite-order correction needed for the Hesse *coefficient* observer, not a proxy for [X]U or an assertion that this coefficient equals native crystalline Frobenius or the target Delta_p-R_p.

## 3. Reproducible exact p=373 W_2 certificate

Use R_2=(Z/139129 Z)[T]/(T^2-2), canonical coefficient representatives. A root mod p is lambda_1=56+19*T; direct exact lifting gives
  lambda_2=91441+93269*T (mod 139129),
  lambda_2^3=4+2*T (mod 139129),
  lambda_2^(-3)=(2-T)/4,
  j(E_lambda)=52279+101413*T = 2417472-1707264*T (mod 139129).
Direct independent factorial multinomial extraction of the original cubic gives
  C_373(lambda)=24618+132788*T (mod 139129),
  C_373(lambda)/373=66+356*T (mod 373).
The consumed source ordinary Hesse input, independently recomputed by coefficient recurrence, is
  A_373(u)=112646+57442*T (mod 139129); A_373(u)/373=302+154*T (mod 373).
The newly computed Hasse correction and prefactor are
  D_373(u)=326+250*T (mod 373),
  (-27*t)^124=272+327*T (mod 373).
Their product checks the derived bridge:
  (272+327*T)*[(302+154*T)-(326+250*T)] = 66+356*T (mod 373).
The two tagged coefficient branches remain distinct: sigma(C_373/373)=66+17*T mod 373.

For additional exact author regression, direct multinomial C and independently derived (*) matched at each p=13,19,37,43,373. In these five cases C mod p=0, consistent with the frozen supersingular parent (finite checks are not its all-prime proof). The exact coefficient proof (*) covers every stated p and every lambda satisfying lambda^3=t, without extrapolation from the checks.

## 4. Mother objective, boundary and next actual scientific operation

The original target stays LIFT: Delta_p=(G_p*h-1)/p = R_p mod p, all primes 13/19 mod24. CM0/SIMPLE and UR/JT0 and the inherited 19 native plus 2 Green units remain consumed; do not repeat WZ/Green or the ten-million-prime scan. This construction supplies a verified original-class W_2 Hesse equation, explicit unramified coefficient/branch, algebraic j pin, differential, and a *noncrystalline* second-digit Hasse coefficient with its correction. The actual native divided-power fixed H0/B0 representative, true [X]U mod p^2, source semilinear Frobenius direction, normalization eta and mapping to omega+6*nabla_lambda(omega), kappa, and Delta_p-R_p are not yet sourced or executed.

Next operation: use this explicit E_lambda/W_2 (and its sigma-conjugate) as the original-model input to construct the rank-two de Rham/divided-power H0/B0 basis and compute native crystalline [X]U at p=373 to mod p^2, with declared Frobenius lift and basis/gauge; check its normalized map to target omega+6*nabla_lambda omega and the signed kappa/Delta-R readouts. Retain the whole matrix and both branches until verified observers. If the source's H0/B0 uses another geometric model or normalization, establish the explicit isomorphism before transferring this coefficient. No claimed native CM computation, independent review, or all-prime LIFT closure.
