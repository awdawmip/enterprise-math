# PREFIX-710-R6 — Repairing the count-max/gamma-max observer mismatch; certified 192×192 gamma-clock exclusion

Date: 2026-11-12 (Asia/Shanghai). Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Mother question: PREFIX-675, global optimization of the frozen two-clock BRC auxiliary observer.
Prior exact inputs: PREFIX-700 true Erlang maximum moment kernel; PREFIX-705 stochastic order for 189 survivor tails; PREFIX-706 exact gamma witness; PREFIX-708 valid Efron–Stein certificate; PREFIX-709 attempted joint survivor shortcut.
Evidence grade: AUTHOR_RECOMPUTED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED.

## A. Precise correction of PREFIX-709

The stopped count N_p belongs to {25,...,189}, and given N_p=k, the completed time T_p is Gamma(k,1). The frozen two-stream observable is Y(p,z)=max(T_p,T_z) for independent gamma-clock streams. It is *not* max(N_p,N_z).

If s_n(p)=Pr(N_p>n), the actual continuous-time survivor is
S_p(u)=exp(-u) sum(n=0..188) s_n(p) u^n/n!.
PREFIX-709 instead treated J_n=s_n(p)+s_n(z)-s_n(p)s_n(z) as Pr(Y>n). That J_n is the survivor of max(N_p,N_z), a different observable.

There is a direct exact counterexample to the load-bearing PREFIX-709 upper bound. For its cell i=j=191, lower corner x=(191/384,191/384), compute PREFIX-709's count-max bound U_191,191 using the original formula. Exact integer comparisons give 0<U_191,191<1, whereas the true frozen Gamma-clock variance satisfies Var[Y(x)]>137. In particular Var[Y(x)]>U_191,191. The script certifies both inequalities without floating arithmetic.

A second small counterexample to the moment identification is p=z=0: both stopping counts equal 25, hence max(N_0,N_0)=25, but the two independent Gamma(25,1) clocks have
E[max(T_0,T_0)] = 3913470354001175/140737488355328 > 27 >25.
Thus the reported 33766/36864 (91.596%) PREFIX-709 certification was for the wrong moment kernel and is not a demonstrated gamma-clock exclusion certificate. The original separate PREFIX-708 certificate remains available at its own stated assumptions.

## B. Correct gamma-clock moment kernel

With independent streams, the gamma survivor of Y is S_Y(u)=S_p(u)+S_z(u)-S_p(u)S_z(u).
Let c_nm=binom(n+m,n)/2^(n+m+1), and s_n=s_n(p), t_m=s_m(z). Exact integration yields

mu(p,z)= sum_n s_n + sum_m t_m - sum_nm c_nm s_n t_m,

E[Y²](p,z)=2 sum_n (n+1)s_n + 2 sum_m (m+1)t_m
             - sum_nm (n+m+1)c_nm s_n t_m.

All these values are rational for rational p,z. The checker uses a common integer denominator and an exact contracted binomial kernel (not a count-max substitution).

The PREFIX-705 survivor-order theorem implies S_p(u) is nondecreasing in p for every u>=0. It follows that Y(p,z) is stochastically nondecreasing separately in p,z. In particular both mu and E[Y²] are nondecreasing on the full square D=[0,1/2]².

## C. New interval theorem and certified fraction

For G=192 and closed boxes
B_ij=[i/(2G),(i+1)/(2G)] × [j/(2G),(j+1)/(2G)],
write a_ij for its lower-left corner and h_ij for its upper-right corner. Define the actual gamma-clock variance bound

U^Gamma_ij = E[Y(h_ij)²] - mu(a_ij)².

Since mu is nonnegative and both mu and E[Y²] are monotone, every x in B_ij satisfies Var[Y(x)]<=U^Gamma_ij. Take the PREFIX-706 exact witness e=(0,3/20) and b=559812917/1000000. The checker separately reconfirms b<W(e)-mu(e)/2.

The complete finite exact calculation finds exactly 26445 ordered cells satisfying U^Gamma_ij<b, with
min_selected(b-U^Gamma_ij) > 15701/1000000.

**Theorem 710.1.** For every real q>=2 and all x in the union R_710 of these 26445 closed cells,

V_q(e)-V_q(x) > (15701/1000000) q² > 0,

where V_q=q²Var(Y)-q E[Y]. Therefore every global maximizer lies outside R_710. Its exactly certified fraction of the full square is

26445/36864 = 8815/12288 (approximately 71.73665%),

and its absolute area is 8815/49152. Its area ratio to PREFIX-708's separately certified area equals 2256640/1037793 (>2.17). This is a ratio of areas, not an assertion of set containment.

Proof: For x in B_ij and t=1/q in (0,1/2],
W(e)-t mu(e) >= W(e)-mu(e)/2>b, while W(x)-t mu(x)<=W(x)<=U^Gamma_ij. Subtract and multiply by q². Closed box boundaries are covered by the weak interval bounds; interiors have disjoint area. The checker evaluates all ordered pairs exactly using symmetry only to reduce duplicate calculation. QED.

## D. Reproducibility and next frontier

Companion script PREFIX710_R6_GAMMA_MAX_INTERVAL_REPAIR.py rebuilds all 189 survivor count rows (9529 nonzero cells) under the frozen width predicate; checks the gamma witness, the exact p=z=0 moment, the integer gamma kernel against the original reference, each selected interval bound, the minimum gap and explicit failure of the PREFIX-709 load-bearing inequality. Local execution: ALL_CHECKS_PASS PREFIX710-R6. This is author recomputation, pending independent review.

10,419 ordered cells are unresolved by this interval bound. Next: refine only those cells using gamma-clock moment Bernstein/derivative bounds and compare fixed witness at both t endpoints 1/24 and 1/12 to target continuous q in [12,24]; isolate the true global optimizer. Do not reuse PREFIX-709's count-max U as a gamma variance upper bound. Scientific pin/P000/ACTIVE worldview unchanged.
