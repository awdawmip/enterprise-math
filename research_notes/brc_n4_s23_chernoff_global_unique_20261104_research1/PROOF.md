# BRC N=4 / S23: global uniqueness of the optimized Chernoff efficiency crossover

Date: 2026-11-04.
Status: AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Scope, provenance, statement

Frozen model: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34, the source-tagged two-state T/B sampling experiment. Its full-source T observation has laws (s(1+v)/2, 1-s, s(1-v)/2) and their swap. Its B observation is a Bernoulli event with success probabilities s(1+v)/2 and s(1-v)/2. Costs are c_T=2-s and c_B=1. Fix the lawful contrast v=2h=1/21, x=v²=1/441, and 0<s<1.

Let F=C_T/(2-s)-C_B with both Chernoff informations **actually optimized**; G=F/[s(1-s)]. THEOREM: G is strictly increasing on the entire interval (0,1), extends continuously to the endpoints with G(0)<0<G(1), and consequently F has **exactly one** interior zero. The previous exact local certificate, at commit 6897b5e082ba6d707f1cb1683032b9a3b3233882, brackets this globally unique zero by

  10243902443/100000000000 < s_c < 10243902445/100000000000.

Illustrative high-precision numerical root (not proof): s_c≈0.1024390244380379439163644981548556894.

## Exact optimized coefficient in a complex-analytic coordinate

Put k=s/(2-s), so s=2k/(1+k) and s(1-s)=2k(1-k)/(1+k)². Write

  L(y)=Σ_{n≥0} y^n/(2n+1)=atanh(sqrt(y))/sqrt(y), L(0)=1,
  ψ(y)=1/2 Log(1-y)+Log L(y),
  r(x)=sqrt(1-x),

using branches continued from x=y=0. Set α=v L(x), γ=kv L(k²x). The Bernoulli Chernoff coefficient for δ=2t-1 is

  M(δ)=[k r(x) exp(αδ)+sqrt(1-k²x) exp(-γδ)]/(1+k).

Its stationary exponent is

  δ*=[ψ(k²x)-ψ(x)]/[v(L(x)+kL(k²x))].

This is its admissible global minimum. For y in [0,x], L(y)≥1, L(y)-1≤y/[3(1-y)] and ψ'(y)=-(L(y)-1)/[2y(1-y)L(y)], with the continuous value at zero. Therefore 0≤δ*≤(1-k)v/[6(1-x)²]≤3087/387200<1/125<1. Strict convexity of M for k>0 proves the optimizing claim.

The stationary equation α k r exp(αδ*)=γ sqrt(1-k²x) exp(-γδ*) yields the exact logarithm of the **optimized** coefficient:

  B(k,x)=1/2 Log(1-k²x)
         +Log((L(x)+kL(k²x))/((1+k)L(x)))
         -[kL(k²x)/(L(x)+kL(k²x))][ψ(k²x)-ψ(x)].

The full tagged Chernoff coefficient is T(k,x)=[1-k+2k sqrt(1-x)]/(1+k). Thus

  Φ(k,x)=B(k,x)-(1+k)/2 Log T(k,x)

is equal to F(s) on the real frozen model at x=1/441. This algebraic/logarithmic formula also gives Φ(0,x)=Φ(1,x)=0.

## A uniform holomorphic bound

Take complex |x|≤1/4 and dist(k,[0,1])≤1/4. Then |k|≤5/4, |1+k|≥3/4, |k²x|≤25/64. The absolutely convergent L series gives

  |L(x)-1|≤1/9; |L(k²x)-1|≤25/117<1/4;
  |D|=|L(x)+kL(k²x)|≥47/144;
  |D/((1+k)L(x))-1|≤65/96;
  |kL(k²x)/D|≤225/47.

The arguments of each logarithm remain in its analytic branch near 1. Applying |Log(1+z)|≤|z|/(1-|z|),

  |Log(D/((1+k)L(x)))|≤65/31;
  |Log(1-k²x)|≤25/39;
  |ψ(k²x)|≤17/26; |ψ(x)|≤7/24.

Also |sqrt(1-x)-1|≤1-sqrt(3/4)<1/7, hence |T-1|≤10/21 and |Log T|≤10/11. The triangle inequality now gives the **complex uniform majorant**

  |Φ(k,x)|≤25/78+65/31+(225/47)(17/26+7/24)+(9/8)(10/11)
           =39835405/5000424 < 8.                    (1)

No estimated floating-point optimization enters (1).

## Endpoint division, coefficient positivity and Cauchy remainder

Define H(k,x)=Φ(k,x)/[k(1-k)] and J(k,x)=(1+k)² H(k,x)/2. The endpoint identities for Φ make H and J analytic at real k=0,1. For complex |x|≤1/4 and real k∈[0,1], the Hermite–Genocchi divided-difference formula gives |H|≤(1/2)sup|Φ_{kk}| and |H_k|≤(1/6)sup|Φ_{kkk}|. Cauchy estimates on k-disks of radius 1/4 combined with (1) give

  |H|≤128, |H_k|≤512, |J|≤256, |J_k|≤1280.         (2)

Write J(k,x)=Σ_{n≥0}g_n(k)x^n. Exact formal series algebra applied to the **true optimized** formula above shows g_0=g_1=0 and

  g_2=(1+k)(10k²+18k-1)/144,
  g_3=(484k^5+1364k^4+1960k^3+2360k²+661k-79)/12960,
  g_4=(268784k^8+1029808k^7+1837568k^6+2341248k^5
       +2721600k^4+3101952k^3+1606957k²+245942k-56159)
       /[10886400(1+k)].

Their derivatives are

  g_2'=(30k²+56k+17)/144 ≥17/144,
  g_3'=(2420k^4+5456k^3+5880k²+4720k+661)/12960 >0,
  g_4'=(1881488k^8+8329120k^7+16396496k^6+20390400k^5
        +19871040k^4+17090304k^3+10912813k²+3213914k+302101)
        /[10886400(1+k)²] >0.

Every displayed positive-coefficient polynomial is positive on k∈[0,1]. By (2), Cauchy's x-coefficient estimate at x0=1/441 and q=4x0=4/441 yields uniformly for **all** k∈[0,1],

  |J_k(k,x0)-Σ_{n=2}^4 g_n'(k)x0^n|
     ≤1280 q^5/(1-q)
     =1310720/16528589540757
     <17/(144·441²).                                  (3)

Consequently J_k(k,x0)>0 across the entire interval, hence G_s(s)>0 because ds/dk=2/(1+k)²>0.

A second Cauchy bound gives |J-Σ_{n=2}^4g_n x0^n|≤256 q^5/(1-q)<x0²/144. At k=0 all g_2(0)=-1/144, g_3(0)=-79/12960, g_4(0)=-56159/10886400 are negative, so J(0,x0)<0. At k=1, g_2(1)=3/8 and g_3(1),g_4(1)>0, and the same tail is <(3/8)x0²; therefore J(1,x0)>0. Continuity and strict increase imply exactly one zero. The previously verified narrow rational local bracket then identifies that global zero.

## Verification and boundaries

VERIFY.py reconstructs g_2,g_3,g_4 directly from the exact optimized logarithmic expression, tests their derivative formulas and coefficient positivity, and uses only exact rational arithmetic for all Cauchy-margin comparisons. Its executable checks cover the explicit algebraic/certified-rational obligations; the standard complex-analysis identities and their hypotheses are displayed for independent review, not represented as machine-formalized proof.

This result concerns one source-aware two-state information-efficiency comparison, at **h=1/42** and all real 0<s<1. It does not solve the original unrestricted ten-label decoder minimax (still [1/2,2/3]) or assert a new native X6 dynamics law. P000, source provenance and the task's frozen scientific input remain unchanged. Formal native task CLAIM/Result and independent project admission are pending.

## Next scientific unit

Under integer budget K and integer numbers of T and B trials, derive the **joint Chernoff exponent** for mixed allocations; do not add separately optimized Chernoff informations without checking their common exponent. Seek an exact mixed-vs-pure allocation certificate. Separately test whether the global uniqueness proof admits a contrast-uniform extension to every 0<h≤1/42, and preserve an exact counterexample if not.
