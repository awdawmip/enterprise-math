# PREFIX-1106 — Signed scaled Beta moments shrink the effective integer-edge band

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_AUXILIARY_CERTIFICATE / NOT_REVIEWED. Continuing own R6 Activity RA-0ABD84561C86E53067DB0322, EM-DIRECT-780BBE / TASK_RESEARCH. Original own session registration r6-20261123-2358-session-start-own-v1 read SUCCEEDED. Current LEASED query r6-20261126-1652-owner-read-v1 last observed RUNNING (EVENT_ISSUE_GUARD_CHANGED restart); no new claim, run, shared task mutation or formal result. This is independent continuation of the existing line.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint/time/residual companions. Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. The full six-axis Cell equality, ordered branch multiplicity, ports, signs and phase remain in the original joint BRC carrier. Only the inherited exact radial test identity D_m(k)=L[x^m(1-x)^k] is used; no native update or independent classical numerical reference is computed.

Immutable parents:
- 04ca670bf23a2b37e9182921376cb28e87992658:research_notes/portable_direct/2026-11-26_r6_prefix1105_effective_integer_edge_band.md
- 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md
- 08f0330096daa21d866aef04ea1db0c6d4f24384:research_notes/portable_direct/2026-11-26_r6_prefix1095_certified_lower_edge.md
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md
- acd24d8499f11d2b8faa6cd0fd8567735f295333:research_notes/portable_direct/2026-11-26_r6_prefix1104_compressed_exception_sieve.md
- f0476c7795f31809302dae513504a06d1e9a9e4c:research_notes/portable_direct/2026-11-26_r6_prefix1101_adaptive_precision.md

## 1. Improved effective theorem

Use the same b, rho=1/b-1, c,d, f(m)=rho*m+c+d/m, G(x)=g(x)/g'(b), B=Beta(m+1,k+1), and k=f(m)+e with |e|<=2 as 1105. Inherit .044<b<.045, 99<c<100, 9<d<10, g'(b)<0. The new bound, for every integer m>=10^8, is

  |D_m(k)/(g'(b)*B)+b^2*e/m| <= 1000*|e|/m^2 + (11/10)*10^15/m^3.        (1)

It follows that for |e|>=10^18/m^2, |e|<=2, m>=10^8 the sign of D_m(k) is the sign of e, and |D_m(k)/(g'(b)*B)|>2/m^3. In particular, with C=10^18 and m>=10^10, the PREFIX-1105 integer localization uses the same rational f enclosure of width <=1/8, but the expanded width is at most .145. Let L=floor(l-C/m^2), U=ceil(u+C/m^2)-1. The two endpoints L,U+1 are within |e|<=2, have strict signs negative, positive and lie in the 1097 monotonic cone. Thus L<=K_last<=U, U-L<=1, with the same exact-zero-aware single CT sign fallback. Any undecided inherited fast oracle of radius <=S^-3 (S=m+k+2) at the queried candidate j implies |D_m(j)/(g'(b)*B)|<=2/m^3 using the same normalization comparison K/|g'|<1 from 1105; hence |j-f(m)|<C/m^2. PREFIX-1104 therefore applies with A=10^18+1, M>=2*10^18 and the specified rational coefficient precision. The constants C, localization activation and sieve activation improve over 1105 respectively by 10^12, 10^6 and 5*10^12. Coefficient precision supply remains to be implemented and true-window execution remains open.

## 2. Scaled moment recurrence retaining the small observation factors

Let z=1/m, alpha=m+1, S=m+k+2, Y=X-b for X~Beta(m+1,k+1), M_n=E[Y^n]. Integration by parts of x(1-x) times the Beta density gives E[X(1-X)h'(X)]=E[(S X-alpha)h(X)] (boundary terms vanish for the parameters here). With h(X)=Y^n and v=b(1-b), L0=1-2b,

  (S+n) M_(n+1)=(alpha-S*b+n*L0) M_n + n*v*M_(n-1), M_0=1,

where the n=0 second term is zero. In particular alpha-S*b=A_e-b*d*z, A_e=1-b(c+e+2). This identity also follows algebraically from the exact rising-factorial Beta moments and hence extends to the complex z disk on which the rational denominators do not vanish.

Write q_n=ceil(n/2), H_n=M_n/z^q_n. For n even the powers of z cancel from both terms; for n odd only the first term retains a z. Thus the analytic continuation of the scaled recurrence at z=0 is

 H_(n+1) = b[(A_e+n L0-b*d*z)*z^(n mod 2)*H_n + n*v*H_(n-1)]
              /[1+b(c+e+2+n)z+b*d*z^2].

H_0=1. This proves analyticity of each scaled H_n on |z|<=1/16 for n<=6 and in particular shows the signed fifth moment has z^3 order without bounding it by an absolute odd moment. This is an exact identity for the auxiliary BRC test weight and does not assume a positive original signed carrier.

Let b0=.044, b1=.045, v1=b1(1-b1), A0=1-104*b1, A1=1-99*b0, Lmin=1-2*b1, Lmax=1-2*b0. For any 0<R<=1/16 define rational constants h_0(R)=1 and, for n=0,...,5,

 den_n=1-b1*(104+n)*R-10*b1*R^2,
 u_n=max(|A0+n*Lmin|,|A1+n*Lmax|)+10*b1*R,
 h_(n+1)=b1*(u_n*R^(n mod 2)*h_n+n*v1*h_(n-1))/den_n.

All den_n are positive. The n=0 missing term is zero. By induction on the analytic recurrence, |H_n(z)|<=h_n(R) on |z|<=R, uniformly in the entire declared real parameter box. The bound on u_n uses the actual signed interval for A_e+n L0, rather than adding the magnitudes of those terms separately.

For n<=4 expand H_n through degree 2-q_n; with R=1/16, z<=R/2, Cauchy and the geometric remainder imply

 |M_n-M_n^[2]| <= 2*h_n(R)*R^(-(3-q_n))*z^3.

For n=5,6 use R=10^-8 and |M_n|<=h_n(R)*z^3; M_6 is nonnegative for actual real Beta weight. This retains the small b and variance factors in the bound. Exact rational computations below give h_5(10^-8)<6.355e-6 and h_6(10^-8)<1.085e-7. Compared with the previous uniform moment coefficient 8192, this is a reduction by >10^9 and >7*10^10 respectively. The first four moment remainder coefficients are <122, 2.764, .063, .001685.

## 3. Refined complement payment using the local curvature of the test weight

Reuse precisely the PREFIX-1105 cutoff chi (inner radius 1/2000, outer radius 1/1000) and its weighted C^3 bound, and the density analytic bound |G|<=10^8 on |x-b|<=1/200. In 1105 the global log-curvature bound was used even though the cutoff boundaries are very close to the mode. Here let W=x^m(1-x)^k, W3=x^(m-3)(1-x)^(k-3). For m>=10^8 and |e|<=2, the modes p,p3 differ from b by <=8/m (directly from the same formulas in 1105), k<=22m and both modes and both inner cutoff boundaries lie in [.04,.05]. The distance from either mode to each of the inner boundaries is >=1/2500, since 8/m<1/10000. On the whole segment joining the mode to either boundary the negative second log derivative for W3 is >=(m-3)/(.05)^2 >=200m; for W it is >=400m. Taylor's theorem gives a gap >=100m/(2500^2)=m/62500. By unimodality the maximum on the complete complement is attained at an inner boundary, so

 sup_complement W3 <= max W3 * exp(-m/62500),

and the same for W. This uses a bound only on the segment between mode and cutoff, not a claim of such curvature on the entire interval [0,1].

All remaining factors in the complement proof of 1105 are valid at m>=10^8: max W3 <=125000 max W (p3 in [.04,.05]); integrating W from p to p+1/m gives B>=max W/(2m) since |(log W)''|<=700m there and exp(-350/m)>=1/2. The cutoff derivative norm J<2*10^15 and |g'(b)|>10^-6 are inherited. Paying both L((1-chi)W)/(g'(b)B) and E[(1-chi)P5] gives the inherited coefficient 10^32*m^4 with the NEW exponent exp(-m/62500). It is <=m^-3 for all m>=10^8: use exp(t)>=t^80/80! and exact comparison 10^32*62500^80*80!<(10^8)^73. No empirical estimate or neglected endpoint.

## 4. Combine the exact cancellation and remainders

The 1096 exact first two coefficients of M_n with c replaced by c+e are unchanged. For the degree-five density polynomial P5, a0=0,a1=1, a_j=g^(j)(b)/(j!*g'(b)). The actual parent derivative ratios bound |a2|<83, |a3|<2738, |a4|<51000. For now use the old analytic bounds |a5|<=10^8*200^5 and |G-P5|<=(5/4)*10^8*200^6*|Y|^6 on the cutoff support. Thus:
- first four moment remainder and full complement: <610/m^3;
- signed fifth moment contribution: <2.034*10^14/m^3;
- local sixth remainder: <8.679*10^14/m^3.

The exact rational sum of all terms is <1.1*10^15/m^3. The second-order coefficient is the same B2(e) from 1105, with B2(0)=0 and |B2'(e)|<1000 on [-2,2]. The first-order coefficient is -b^2*e. These facts prove (1). In particular (b0^2-1000/10^8)*10^18 minus the exact remainder constant exceeds 2, proving the strict sign and magnitude claims of section 1. This retains the full signed cancellation of the lower-order joint observer and of M5, rather than dropping terms in advance.

## 5. Executed exact auxiliary verification

The following script was executed in the local Python environment using Fraction. It checks the actual numerical constants, and compares the recurrence with direct raw-moment binomial algebra on 108 auxiliary parameter combinations (648 moment equalities). For m>=10^8 it also checks each bound on the actual centered moment. These are finite checks of the auxiliary algebra, not a rerun of the native BRC propagation or of all 18 old certified rows. The proof above supplies the uniform scope. The direct attempt to reconstruct higher signed density jets locally did not run because streaming container execution was unavailable; no higher-jet computation is claimed, and the conservative inherited Cauchy a5/a6 bounds remain in use.

```python
from fractions import Fraction as F
from math import factorial
b0,b1=F(44,1000),F(45,1000)
v1=b1*(1-b1); L0,L1=1-2*b1,1-2*b0
A0,A1=1-b1*104,1-b0*99
# bound scaled centered moments H_n = M_n / z^ceil(n/2)
def bounds(R):
 H=[F(1)]
 for n in range(6):
  den=1-b1*(104+n)*R-b1*10*R**2
  assert den>0
  U=max(abs(A0+n*L0),abs(A1+n*L1))+b1*10*R
  H.append(b1*(U*H[n]*(R if n%2 else 1)+(n*v1*H[n-1] if n else 0))/den)
 return H
R=F(1,16); H=bounds(R); Hreal=bounds(F(1,10**8));
# Cauchy on H_n, truncation at degree 2-ceil(n/2), for n<=4
err=[2*H[n]*R**(-(3-(n+1)//2)) for n in range(1,5)]
# uniform a5 bound from PREFIX-1105 and sixth local remainder
coeff=[1,83,2738,51000]; a5=10**8*200**5; a6=F(5,4)*10**8*200**6
small=sum(a*e for a,e in zip(coeff,err))+1
big5=a5*Hreal[5];big6=a6*Hreal[6];total=small+big5+big6
print('H complex:',[float(x) for x in H]);print('H real:',[float(x) for x in Hreal]);print('errors:',[float(x) for x in err]);print('terms:',[float(x) for x in (small,big5,big6,total)])
assert total<F(11,10)*10**15
# derivative term unchanged from parent; strict sign for |e|>=C/m²
C=10**18
assert (b0*b0-F(1000,10**8))*C-total>2
assert 10**32*62500**80*factorial(80) < (10**8)**73
assert F(8,10**8)<F(1,10000)
assert F(1,8)+2*F(C,10**20)<1
assert 2*10**18>C+1
print('C=',C,'m0=',10**10,'sieve M=',2*10**18)
# Direct raw moment comparison, exact independent auxiliary algebra checks.
from math import comb
from itertools import product
count=0
for b,c,d,e,m in product([b0,b1,F(44563,10**6)],[F(99),F(100)],[F(9),F(10)],[-2,0,2],[32,10**8,10**10]):
 z=F(1,m); alpha=m+1; S=m/b+c+e+2+d*z
 raw=[F(1)]
 for j in range(6):raw.append(raw[-1]*(alpha+j)/(S+j))
 M=[sum(comb(n,j)*(-b)**(n-j)*raw[j] for j in range(n+1)) for n in range(7)]
 for n in range(6):
  assert (S+n)*M[n+1]==(alpha-S*b+n*(1-2*b))*M[n]+(n*b*(1-b)*M[n-1] if n else 0)
  count+=1
  if m>=10**8:assert abs(M[n+1])<=Hreal[n+1]*z**((n+2)//2)
print('recurrence checks',count)
```

Actual output (floats for display only, all decisions rational): H complex=[1, .2364399180826922, .005398253297945518, .00196132373701022, 5.265158485211415e-5, 2.2938053215577452e-5, 8.509666359556362e-7]; H real=[1, .16560000795258037, .0019338752977960181, .0008023648318485318, 1.1219620157811503e-5, 6.35411927672013e-6, 1.0848672342737422e-7]; remainder coefficients (first four)=[121.05723805833841,2.763905688548105,.06276235958432703,.0016848507152676527]. Contributions (small,fifth,sixth,total)=[609.2321372283689,203331816855044.2,867893787418993.8,1071225604274647.1]. C=10^18, m0=10^10, sieve M=2*10^18. 648 recurrence equalities, 432 additional large-scale moment comparisons; all assertions passed. The actual executed script SHA256 was 50a4d0ce4609725fe169e059abd50cc83cd8d81a2f80c146fc2a5449d7e1c397.

## 6. Next discriminating work

The fifth and sixth local derivative payments now dominate essentially all of the new constant. Extend the existing 1096 exact nine-state signed density derivative certificate to orders 5 and 6 on a whole rational neighborhood of b, using a shifted signed polynomial before taking absolute bounds. This should discriminate whether the Cauchy envelope can be replaced by the true local derivative jet. Then feed the improved band into the actual 1104 sieve, using the full adaptive precision anchor supply, not rounded coefficient guesses. Exact zero, uniform Diophantine separation, other spectral zeros, c_2=0 and B_fix,odd(32) remain open. No independent mathematical review or formal task acceptance.
