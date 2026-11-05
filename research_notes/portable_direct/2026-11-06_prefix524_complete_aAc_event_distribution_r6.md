# PREFIX-524 — Entire aAc event-count distribution and sharp 12th-order BRC gate-pair recurrence

Date: 2026-11-06 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Task line: RS-X6-NATIVE-ROTATION-DYNAMICS; Researcher-ID EM-X6-D301A6; activity RA-44516488349E028C6341C063.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Immediate dependencies: PREFIX-518 (symbolic four-STAR transition model); PREFIX-520 (phase return generating function); PREFIX-522 (reachable aAc gate and exact local condition); PREFIX-523 (gate/BRC pair constraint, event spacing and second factorial moment). Norms: current P000 / ACTIVE Heartbeat World, research method, portable research protocol and current global mathematical evidence policy.

## 1. Exact population

Fix one of the 24 S4 chart relabelings h. At macro length d, count all 48 initial directed phases, each next phase chosen among the 3 legal ports and each macro microtrace independently marked INNER/OUTER. The population size is exactly 48·6^d, including the d=0 population of 48 empty macro-histories with distinct starting phases.

Let H_h(w) be the number of *indexed* occurrences of the signed-axis color word aAc in the full ordered native microtrace. Each hit ends at a macro index i >= 2. By the local characterization of PREFIX-522, a hit at i occurs exactly when the directed target phase is T_h and the two most recent branch labels are INNER. For any two hits at i<j, PREFIX-523 proves j-i=2m >=4. Write a_m for the number of unbranched phase itineraries of length 2m returning to a fixed directed phase. PREFIX-520 proves a0=1, a1=0, a2=5, a3=28, a4=297 and

a_(m+5)=5a_(m+4)+26a_(m+3)+78a_(m+2)+135a_(m+1)-243a_m.

Its rational series is
A(x)=(1-5x-21x²-75x³-108x⁴)/(1-5x-26x²-78x³-135x⁴+243x⁵).

All statements below refer to this explicitly defined symbolic graph, with signed X6 elementary steps and branch/source retained in the population.

## 2. All-order factorial-moment theorem

Define F_k(d)=sum_w binom(H_h(w),k) for integers k>=1, d>=0, where the sum is over all 48·6^d labeled histories. Define

R(t)=sum_(m>=2) 2^(2m-2) a_m t^(2m) = [A(4t²)-1]/4.

Then for **every** integer k>=1 and d>=0, the ordinary generating function is exactly

**sum_(d>=0) F_k(d)t^d = [9t²/(1-6t)²] R(t)^(k-1).**

Proof: Mark k ordered distinct aAc occurrences at macro indices i1<...<ik. For the first marked hit at i1, the incoming-regular phase graph has 3^i1 phase prefixes ending at T_h; the final two INNER labels are fixed, leaving 2^(i1-2) branch strings. Its generating series is sum_(i1>=2)3^i1·2^(i1-2)t^i1 = 9t²/(1-6t).

For consecutive marked hits separated by g=2m>=4 macros, the intermediate phase segment returns from T_h to T_h in exactly a_m ways; its last two branch labels are fixed as INNER and the other g-2 labels are free, giving the weight a_m·2^(2m-2). This is exactly R(t). The suffix after the last hit has six independently labeled successors per macro, contributing 1/(1-6t). Multiplication gives the displayed formula. Extra unmarked occurrences cause no issue: each history with H occurrences contributes exactly binom(H,k) choices of ordered marked positions. This is a bijective infinite-length combinatorial proof.

In particular F_1(d)=9(d-1)6^(d-2) for d>=2, and F_2(d) is the PREFIX-523 pair count. Necessarily F_k(d)=0 if d<4k-2, consistent with the sharp event-spacing theorem.

## 3. Exact bivariate generating function of the complete hit distribution

Introduce the integer-counting polynomial P_d(z)=sum_w z^(H_h(w)), preserving all multiplicities. Since z^H=[1+(z-1)]^H=sum_(k>=0)binom(H,k)(z-1)^k, sum over k and all d gives

**P(t,z):=sum_(d>=0)P_d(z)t^d
=48/(1-6t)+[9t²(z-1)]/[(1-6t)²·(1-(z-1)R(t))].**

This is an exact rational bivariate formal series. The first term corresponds to k=0, the entire population; the other terms sum the geometric all-order factorial-moment series. The denominator 1-(z-1)R(t) has constant coefficient 1 and is therefore invertible as a formal series. For fixed d only finitely many k contribute.

The coefficient [t^d z^j]P(t,z) is exactly the count of d-macro histories with precisely j hits. Equivalently, by finite binomial inversion,

count(H=j)=1_(j=0)·48·6^d + sum_(k=max(1,j))^floor((d+2)/4) (-1)^(k-j) binom(k,j)F_k(d).

This supplies the full higher-event distribution and a reusable exact coefficient algorithm rather than just first and second moments. The exact BRC bound from PREFIX-523, H<=p_(h-L1), continues to constrain every history; to recover the **joint** (H,p) histogram keep the separate positive/negative axis-count transfer of PREFIX-523 before applying p=min(N+,N-).

## 4. Sharp minimal recurrence order for the pair correlation

Let B_d=F_2(d), and D(x)=1-5x-26x²-78x³-135x⁴+243x⁵. Algebraically,

R(t)=4t⁴(1-12t²)(5+72t²+1296t⁴)/D(4t²),

B(t)=sum B_d t^d
=36t⁶(1-12t²)(5+72t²+1296t⁴)/[(1-6t)² D(4t²)].

Set Q(t)=(1-6t)²D(4t²); Q(0)=1 and deg Q=12. Exact polynomial Euclidean division, including reduction modulo 101, gives gcd over Q[t] of the displayed numerator and Q equal to 1 (the numerator has nonzero leading coefficient mod 101). Therefore the rational generating function for B is **already in lowest terms**. By the standard rational-series/linear-recurrence correspondence, its minimal eventual constant-coefficient recurrence order over Q is **exactly 12**, sharpening PREFIX-523's bound of at most 12. No empirical minimality inference is used.

In ascending order Q(t) has coefficients
[1,-12,16,240,-1136,4992,-19968,59904,-214272,414720,-995328,-2985984,8957952].
Consequently B_d obeys the exact homogeneous recurrence sum_(j=0)^12 Q_j B_(d-j)=0 for every d>=13. At d=12 the product Q(t)B(t) has a nonzero t^12 coefficient, so the d=12 coefficient equation is inhomogeneous. The complete initial coefficients are calculated from the first theorem.

## 5. Executed certificate and exact checks

An independent exact integer graph DP uses the actual 48 phases, the 3 successor ports and both labeled native microtraces. It compares full hit histograms, all factorial moments and binomial inversions for d=0..15, and checks 24 chart-frame copies through d=9. A separate primitive-character direct scan enumerates all 48·(1+6+6²+6³+6⁴)=74,640 initial-phase-labeled histories up to four macros; results agree. It also recomputes 16 positive-even phase return coefficients and checks their previously established recurrence; a symbolic exact polynomial gcd check certifies minimal order 12.

Representative counts: at d=6 the H=0,1,2 histogram is (2,181,348; 57,960; 180). At d=10 the H=0,1,2,3 histogram is (2,768,096,880; 132,513,840; 1,762,128; 3,600). At d=15, H=4 occurs 864,000 times. All sum to 48·6^d at their respective depths.

Exact locally executed Python/SymPy certificate and full output are retained with this research handoff; the repository's JavaScript certificate and its execution JSON provide a separate engine check. Verification is author-executed finite checks plus an all-d constructive algebraic proof, pending independent mathematical review.

## 6. Next unresolved question

Use the explicit full-distribution rational function as an efficient readout; then refine it by one h-L1 BRC pair coordinate and evaluate whether the 96-state weighted transfer admits a smaller *joint-observer-safe* exact quotient. A candidate quotient must preserve all declared future (H,p) outputs, branches/source when requested and the complete family of continuations; compare fibers before dropping coordinates. The mother question of arbitrary triad C6 and native physical X6 rotation-selection remains active as a distinct proof obligation.
