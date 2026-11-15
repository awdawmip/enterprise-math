# RH full-integer road: an unconditional superquadratic small-parameter energy barrier

Date: 2026-11-15.
Status: proved auxiliary theorem (classical existence of nontrivial zeta zeros used); not a native Result, independent admission, Task closure, or proof of RH.

Provenance: original full-integer road and research question EM-FREE-C4A91D (RH-ROAD-TAIL-20260909, TP2-DCE65A0EFCE8151C39BD). The fixed-`N` first-order expansion was developed in the Driver's earlier prime-count/nearfield work. The exact Mellin–Plancherel/Hardy-energy mechanism was established in `2026-11-15_rh_road_exact_mellin_plancherel_energy_criterion.md` (main@7fe5d9ec3d61c6c12456b953a58d5fb2d48fefd5). The new combination and divergence proof below are by RESEARCH_DRIVER EM-DVR-DEBB5E. Shared Driver context; not an independent reviewer endorsement.

## Definitions and statement

For (a>0) and all positive integers (n,N), retain the **whole integer** road
[
R_a(n)=prod_{pmid n}(1-p^{-a}),quad R_a(1)=1,quad
c_a=zeta(1+a)^{-1},
]
[
B_{a,N}=sum_{nle N}R_a(n)-1-(N+	frac12)c_a,qquad
E_a=sum_{Nge1}rac{|B_{a,N}|^2}{N^2}in[0,infty].
]
Let (Lambda(n)) denote von Mangoldt's function and (psi(N)=sum_{nle N}Lambda(n)). Set (q_N=psi(N)-N-	frac12).

**Theorem.** Unconditionally, using the classical existence of nontrivial zeros of the Riemann zeta function,
[
sum_{Nge1}rac{|q_N|^2}{N^2}=+infty,
qquad
oxed{ lim_{adownarrow0}rac{E_a}{a^2}=+infty }.
]
The second limit is in the extended nonnegative reals; it does **not** assert (E_a<infty) for any (a), or a uniform upper estimate. Equivalently, for every (K>0) there exists (a_K>0) such that (E_a>K a^2) for all (0<a<a_K).

## 1. Exact first variation at each fixed integer

For (n=p^k>1), (R_a(n)=1-e^{-alog p}=alog p+O_n(a^2)). For (n) with at least two distinct prime factors, (R_a(n)=O_n(a^2)). Also (R_a(1)=1) and the Laurent expansion of zeta at (1) gives (c_a=a+O(a^2)). Therefore, **at every fixed (N)**,
[
lim_{adownarrow0}rac{B_{a,N}}a
=sum_{p^kle N}log p-(N+	frac12)
=psi(N)-N-	frac12=q_N. 	ag{1}
]
This pointwise assertion is not yet uniform in (N).

## 2. The prime-count first variation has infinite weighted square energy

Suppose for contradiction that (Q=sum_{Nge1}|q_N|^2/N^2<infty). Put
[
H_N=psi(N)-N=q_N+	frac12,qquad H(x)=H_{lfloor xfloor}quad(xge1).
]
Because adding the constant (1/2) preserves weighted square summability,
[
P:=int_1^infty |H(x)|^2,rac{dx}{x^2}
=sum_{Nge1}rac{|H_N|^2}{N(N+1)}<infty. 	ag{2}
]
For (Re s>1), exact Abel summation and the standard Dirichlet series for (Lambda) give
[
G(s):=int_1^infty H(x)x^{-s-1},dx
=rac1ssum_{nge1}(Lambda(n)-1)n^{-s}
=rac{-zeta'(s)/zeta(s)-zeta(s)}s. 	ag{3}
]
Let (h(v)=H(e^v)e^{-v/2}), (vge0). Equation (2) gives (|h|_{L^2(0,infty)}^2=P). Cauchy–Schwarz applied to the Laplace transform yields, for every (sigma>1/2) and real (t),
[
G(sigma+it)=int_0^infty h(v)e^{-(sigma-rac12+it)v},dv,
qquad
|G(sigma+it)|lesqrt{rac{P}{2(sigma-rac12)}}. 	ag{4}
]
It also gives a holomorphic extension of (G) throughout (Re s>1/2).

Classically (zeta) has at least one nontrivial zero; by its functional-equation symmetry, choose such a zero (ho=eta+igamma) with (etage1/2) (no assumption of RH). The logarithmic derivative (-zeta'/zeta) has a nonremovable simple pole at (ho) with residue (-m), where (mge1) is its multiplicity; (-zeta(s)) cannot cancel it, and (ho
e0).

- If (eta>1/2), (3)'s meromorphic continuation has a pole *inside* the holomorphy half-plane established by (4), impossible by identity of analytic continuations.
- If (eta=1/2), take (s=ho+delta) with (delta>0) sufficiently small. From the meromorphic expression (3), (|G(ho+delta)|sim m/(|ho|delta)), while (4) bounds it by (sqrt{P/(2delta)}). These are incompatible as (deltadownarrow0). (If a pole already lies in the open half-plane, the previous case applies.)

Thus (2) and hence (Q<infty) are false:
[
Q=sum_{Nge1}rac{(psi(N)-N-rac12)^2}{N^2}=infty. 	ag{5}
]
No assumption on the location of *all* zeta zeros enters this argument.

## 3. Fatou's lemma transfers the divergence to the small-a road

The summands are nonnegative. Apply Fatou to the sequence (adownarrow0) and use (1):
[
liminf_{adownarrow0}rac{E_a}{a^2}
=liminf_{adownarrow0}sum_{Nge1}rac{|B_{a,N}/a|^2}{N^2}
gesum_{Nge1}rac{|q_N|^2}{N^2}
=infty. 	ag{6}
]
For an arbitrary real (adownarrow0), the equivalent finite-partial-sum argument avoids any need to select a specific sequence: first choose (M) with (sum_{Nle M}q_N^2/N^2>2K), then by (1) choose (a_K>0) so that (sum_{Nle M}|B_{a,N}/a|^2/N^2>K) for all (0<a<a_K). This proves the claimed extended limit.

## Interpretation and open boundary

The result gives a **lower-scale constraint**, not a competing global upper bound. It is compatible with previously proved (o(a)) *nearfield partial-energy* upper bounds, because (a^2ll a) and those results do not control the whole infinite tail. It is also compatible with (E_a=infty) for some or all small (a). In particular it neither proves RH nor invalidates earlier scoped nearfield results.

The key contribution is the rigorous noncommutation of fixed-index first-order variation and an (N)-infinite square-energy bound with (O(a^2)) normalization. Any proposed global (E_a=O(a^2)) estimate is now unconditionally excluded; estimates at a weaker scale (e.g. (o(a))) remain open and must be assessed separately. A further quantitative rate would require additional information on the distribution of the prime-count discrepancy or a new energy mechanism.

Cross-references: `2026-11-15_rh_road_small_a_primecount_firstorder_pnt_nearfield.md`; `2026-11-15_rh_road_exact_mellin_plancherel_energy_criterion.md`; `2026-11-15_rh_road_l2_energy_shifted_zeta_zero_obstruction.md`.
