# R5 — Exact outer signed-support theorems at asymmetric stopping times

2026-11-07 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scientific scope

Frozen source pins unchanged: Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Direct predecessor 4077f06c62331ada77bdad48531bd66551ac3e1d, research_notes/brc_r5_asymmetric_inner_support_band_20261107_t1540. Mother target: equality of four-observer images O4(FULL_HIST) and O4(seedless LR), W=(eP,eQ,TP,TQ). The present model is a frozen finite four-stage P/Q-BRC LR observer, not full native X6 dynamics.

Use real flows x=(g,a,b,u,v,w,z), with 0<=a,b<=g<=1, C0=13a/40+b/80, C1=a/10+9b/40, C2=3a/40+21b/80, 0<=u<=C0, 0<=v<=C1, 0<=w<=C2, 0<=z<=a/10, 0<=v-z<=9b/40. The exact time and seven stop-mass formulas appear verbatim as Fraction coefficients in VERIFY.py, preserving seven keys r=(1/10,1/2,3/4,1,5/4,3/2,19/10) and their first LR moment. Seedless LR adds 9bz=4a(v-z). Define Uλ=eQ-(1+λ)(1-eP) and its optimal terminal declaration Sλ(x)=Σ [1-(1+λ)rj]_+ Mj.

## New theorem (all real λ on two exact time sections)

For each ε=+1/100 and ε=-1/100, fix TP=31/10+ε, TQ=31/10-ε. For **every real λ∈[-1/10,1/10]**, max_FULL_HIST Uλ = max_seedless_LR Uλ = Hε(λ). On each row Hε(λ)=B+Aλ:

ε=+1/100:
| interval | B | A |
|---|---|---|
| [-1/10,-351/17291] | 48387/193750 | -32654/96875 |
| [-351/17291,0] | 331779/1325000 | -3631949/11925000 |
| [0,351/16589] | 331779/1325000 | -52793/225000 |
| [351/16589,1/10] | 48387/193750 | -19709/96875 |

ε=-1/100:
| interval | B | A |
|---|---|---|
| [-1/10,-26217/398347] | 190719/775000 | -268871/775000 |
| [-26217/398347,-351/17291] | 24204/96875 | -505373/1743750 |
| [-351/17291,0] | 331671/1325000 | -3180001/11925000 |
| [0,351/16589] | 331671/1325000 | -43357/225000 |
| [351/16589,1/10] | 24204/96875 | -297283/1743750 |

**New asymmetric phenomenon:** ε=-1/100 introduces a genuine additional optimizing-flow switch λ=-26217/398347 (about -0.06581). At ε=+1/100, the only nonzero optimizing-flow switches in this range are the inherited -351/17291 and +351/16589. λ=0 changes the declared key set.

## Explicit seedless attaining policies

All tuples are (g,a,b,u,v,w,z). At ε=+1/100: P_outer=(2186/2325,1814/2325,2186/2325,0,2693/9300,0,907/11625) attains both outer intervals, P_inner=(1,974/1325,1186/1325,0,1457/5300,0,487/6625) both inner intervals. At ε=-1/100: N_far=(138/155,138/155,138/155,1/25,897/3100,0,69/775) attains the leftmost interval; N_outer=(742/775,742/775,618/775,0,853/3100,0,371/3875) both intermediate-left and positive-right outer intervals; N_inner=(1,1226/1325,1014/1325,0,1403/5300,0,613/6625) both inner intervals. Declare the whole mass on every LR key with 1-(1+λ)rj>0 and zero otherwise. Every policy obeys all legal probability constraints, times, Q mass/moment normalization, and exact seedless identity.

## Rigorous universal upper certificate

The sixteen affine feasibility inequalities are Li(x)<=0 (zero-based indexes in VERIFY.py). For each of 11 (section, λ-endpoint) combinations, VERIFY.py provides rational nonnegative multipliers μ_i and unrestricted νP,νQ and checks the eight exact coefficients of the identity

  Sλ(x) - Σ_i μ_i Li(x) - νP TP(x) - νQ TQ(x) = K.

Thus Sλ(x)<=K+νP(31/10+ε)+νQ(31/10-ε) for every FULL_HIST policy satisfying the two fixed time equations. Each of the 11 resulting rational bounds equals the objective of an explicit feasible seedless policy. On each of the nine closed λ subintervals, the *same* seedless policy achieves equality at both endpoints. Since the positive LR-key set is fixed on each interval, Sλ(x) is affine in λ for every flow. Interpolating its two exact universal dual bounds and matching primal values proves the theorem for **all real λ**, without numerical discretization.

The exact standalone Fraction checker verifies the eleven universal dual identities, eleven upper/primal equalities, nine whole intervals, all five seedless flows and moment constraints. Output is in EXACT_OUTPUT.txt. Exploration used approximate LP only to discover candidates; the published proof depends solely on these exact rational certificates.

## Remaining mother target

This is a result for a signed one-parameter support direction at two fixed asymmetric time pairs. Full four-observer set equality for all times/directions remains unresolved; a global four-dimensional separator needs re-optimized seedless nonattainment. Independent reviewer admission and native Result/CLAIM are pending. Next: derive λ switch curves as ε varies, then test general four-dimensional normal directions. See NEXT_UNIT.md.
