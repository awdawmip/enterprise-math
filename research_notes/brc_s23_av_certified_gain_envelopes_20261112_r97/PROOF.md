# R97 — Certified nonstationary gains and exact critical envelopes

Date: 2026-11-12. Scientific status: author-side proof and exact finite checks; independent review pending.
Frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Lineage: R86, R90, R94–R96; immediate predecessor R96 commit `9291e012cc0fc19032fffb8a697526e51b61268f`.
Scope: auxiliary finite rational circular-source model, not a native six-axis or physical-heartbeat transfer. P000 is unchanged.

## R97.1 Certified-interval online acquisition theorem

Fix a full immutable source identity set S (time *and* branch), observation signature and closed rational covering domain. At request i, lazy exact answering costs L_i >= 0; if a full exact winner profile was previously installed, one may answer via that profile for E_i >= 0. The once-only profile construction cost P belongs to a known *certified* interval [P_lo,P_hi], with P_lo >= 0; exact current and future costs need not be known before the decision. All cost measures share a fixed unit and include the charged memory/retention/witness-recovery costs. Once purchased, the cheaper of lazy and profile-assisted exact routes is available at each request. There is no uncharged time-dependent holding cost.

Define the per-query possible saving g_i=max(0,L_i-E_i). Before answering query i, the algorithm receives certified bounds 0<=ell_i<=g_i<=u_i<=rho*ell_i for fixed rho>=1; zero lower bound consequently forces zero actual gain under this contract.

Algorithm: Initially keep h=0. Until purchase, buy *before* request i exactly when ell_i>0 and h+ell_i>=P_hi. Otherwise serve it lazily and set h=h+ell_i. Following purchase, serve each request using min(L_i,E_i). The online algorithm does not know future requests.

**Theorem.** For every finite stream, letting OPT be the offline best exact cost,

```
0 <= ONLINE-OPT <= rho*P_hi.
If P_lo>0: ONLINE <= (1+rho*P_hi/P_lo)*OPT.
```

For exact savings and exact build cost, rho=1 and P_lo=P_hi=P, recovering the factor-2 cost-model guarantee of R96.

**Proof.** Put A=sum_i min(L_i,E_i), G=sum_i g_i. Because a purchased profile can be retained and the cheaper route can always be chosen, buying later never improves on either purchasing at the beginning or never purchasing: OPT=A+min(P,G).

If no purchase occurs, ONLINE=A+G. For G<=P the algorithm is optimal. For G>P, every previously observed positive lower-bound increment was handled without reaching P_hi, so sum ell_i<P_hi. The certified width gives G<=rho*sum ell_i<rho*P_hi, and ONLINE-OPT=G-P<=rho*P_hi. The P_hi=0 case is covered by zero gains or immediate acquisition.

If purchase occurs first before request k, let H=sum_{i<k}g_i. Prior to triggering, the accumulated lower bound h<P_hi; H<=rho*h<=rho*P_hi. Since h+ell_k>=P_hi>=P and G>=h+ell_k, the offline optimum purchases. Thus ONLINE=A+H+P, OPT=A+P and ONLINE-OPT=H<=rho*P_hi.

For the multiplicative inequality, in every case where the online algorithm is not optimal the offline optimum purchases, hence OPT>=P>=P_lo. Combine this with the additive regret bound. QED.

A concrete missing-width counterexample is P=1, ell_i=0 and g_i=1 for n requests: the lower-bound-trigger algorithm rents n times while OPT=1. An empirically estimated CPU-time interval does not establish the theorem's certification assumptions unless its bound against actual runtime cost is separately proved. The unconditional additive statement remains meaningful even if P_lo=0.

## R97.2 Exact source/domain critical-point envelope

Retain the original R90 directed half-open rational circular membership, with source time t, full (t,branch) identity, observer signature sigma=(j,x,a,b) (j,a,b integers, x rational), and closed rational parameter interval I=[L,U]. The six affine expressions whose integer crossings contain every source-membership transition are

```
a*z; b*z; (a-b)*z;
x+(t-j)*z; x+(t-j-a)*z; x+(t-j-b)*z.
```

For slope c!=0 and offset d, set low=min(cL+d,cU+d), high=max(...), and
N_I(c,d)=max(0,floor(high)-ceil(low)+1); for c=0 put N_I(c,d)=0, since a constant-integer expression creates no isolated crossing. Let T be the distinct source-time set. Define

```
K_bound = 2 + sum_{t in T} sum_{the six forms (c,d) for t} N_I(c,d).
```

**Theorem.** Every point breakpoint of the full exact winner profile on I belongs to the endpoints together with the union of these integer crossings. Consequently there are at most K_bound point atoms and at most 2*K_bound-1 point/gap atoms. The bound can be counted with six affine forms per distinct source time, without building the profile, using exact rational arithmetic. Bit complexity depends on the sizes of times, rational endpoints and coefficients.

**Proof.** Between adjacent crossings, each involved fractional part has a fixed integer offset and the signs of relevant affine differences cannot change. Every directed half-open membership predicate M_t is constant on each resulting open interval. Its separate endpoint value accounts for strictness and coincident boundaries. A lexicographic maximum over finitely many such predicates is likewise constant on these gaps; any winner-profile point breakpoint lies in the crossing union. Counting integer levels crossed by c*z+d gives N_I(c,d); summing over all times allows duplicates and so is an upper bound. Deduplication leaves no more than K_bound points, and each adjacent pair contributes one open gap. QED.

This is an exact *representation-size* bound, useful as a source/domain-aware prebuild feature. It is not a guaranteed CPU-time or memory-price bound. Its derivation retains BRC rational phase residues, time fibers and the full source branch identity needed for output recovery.

## Reproducible checks (CPython, exact Fraction)

The companion check_r97.py.gz.b64 and verification_r97.json.gz.b64 are losslessly gzip/base64 encoded. Decode with `base64 -d FILE.gz.b64 | gzip -d > FILE`. Run the decoded script with the unchanged R96 reproducibility bundle's check_r82.py, check_r86.py and check_r90.py through check_r96.py. R96's original program, inputs and scientific pin are unchanged.

The executed script exhausted **261,268** cost sequences (purchase-price uncertainty, bounded gains, varied length including empty, buy and no-buy cases). For each it independently enumerated all offline purchase times; the regret and stronger instance-sensitive ratio assertions passed. The exact circular-source profile suite computed **34** profiles from **17** source/signature keys under the broad domain [-1/4,3/5] and narrow domain [1/16-1/1200,1/16+1/1200]. All profile point sets matched the original exact per-time cut union and obeyed K_bound. **68** full-domain/singleton classifications matched the independent exact rational reference.

Recorded broad median: **581** exact profile point atoms, median upper bound **688**. Recorded narrow median: **2** point atoms and upper bound **2**. All 34 measured build times, graph-representation sizes, per-key affine endpoint counts and rational representation-bit volumes are in the attached verification JSON; CPU figures are single-process observations. For a single time at fixed domain [0,1/1000] and signature (0,1/7,1,2), source t=100,1000,10000 respectively gave exactly **2,5,32** critical points, showing source time magnitude matters independently of source count and domain width.

## Next discriminating unit R98

Derive empirically *validated* build-price ranges from critical envelope and rational operand lengths using held-out source/signature/history versions. Measure cold and warm query work, retained historical graph cost, rational integer arithmetic and CHANGES witness recovery; check actual costs against every claimed forecast interval. Maintain a fallback when intervals are not certified. Keep Source task/owner authorization, native activity and independent review separate from this author-side mathematical contribution.
