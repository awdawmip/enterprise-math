# PREFIX-666-R2 — A thirty-twofold wider signed-curvature BRC variance strip via finite Taylor/Bernstein certificates

Date: 2026-11-10. Research mode: independent author-side derivation, pending actual native Result and independent mathematical review. Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Scientific antecedent: PREFIX-659/660/661/665 at unchanged native first-stop BRC observer and exact 189-layer survivor recurrence. This is not a claim of all-native Heartbeat dynamics or the X6 rotation mother task's hard target.

## Theorem — expanded certified rectangle

Let `J=[607/4096,609/4096]`, `Q=19/128`, and `R=[0,1/128] × J`, with real `12 ≤ q ≤ 24`. In the frozen BRC first-stop observer let `μ(p,z)=E[Y]`, `H(p,z)=E[Y²]/2`, `W=2H−μ²`, `V_q=q²W−qμ`, and let `z_*(q)` denote the unique maximizer of `V_q(0,z)` on `J` (the proven edge lemma of PREFIX-660).

**On all of R**, exact rational interval bounds establish

- `μ(p,z)>86`;
- `μ_pp(p,z)>225`;
- `H_pp(p,z)<15400`;
- `W_pp(p,z)<−8000` and `V_{q,pp}(p,z)<−8000 q²`.

Using the independently established edge facts `V_{q,p}(0,z)<−76650` (PREFIX-661) and `V_q(0,z_*)−V_q(0,z) ≥ 6,400,000 (z−z_*)²` (PREFIX-660), integration yields

`M_q−V_q(p,z) ≥ 76650 p + 4000 q² p² + 6,400,000(z−z_*(q))²`, where `M_q=V_q(0,z_*(q))`.

The maximum on R is unique and occurs at `(0,z_*(q))`. The p-width (and area for the same z band) is **32 times** PREFIX-665's verified `1/4096` rectangle. The theorem says nothing about a maximum over the entire `[0,1]^2` parameter square.

## Native source and recurrence

Use the unchanged integer BRC survivor model (PREFIX-665): `A_0(0)=1`; for `n=1,...,189`, form `A_n(k)=A_{n−1}(k)+A_{n−1}(k−1)` and retain only the exact frozen `wide(n,k)` survivor decision. That decision is the integer-binomial threshold bracket in `PREFIX666_experiment.py` and is a faithful transcription of PREFIX-665's published native 189-layer observer. The last layer is empty. Define `f_n(k)=A_n(k)/binom(n,k)∈[0,1]`, `s_n(u)=Σ_k A_n(k) u^k(1−u)^{n−k}` for `0≤n≤188`.

Set `t_m(z)=s_m(z)` and `w_nm=2^{−(n+m+1)}binom(n+m,n)`; define

`a_n(z)=1−Σ_m w_nm t_m(z)`, `b_n(z)=n+1−Σ_m (n+m+1)w_nm t_m(z)/2`.

From the exact two-clock first-stop composition proved in PREFIX-659,

`μ(p,z)=Σ_n a_n(z)s_n(p)+Σ_m t_m(z)`, and

`H(p,z)=Σ_n b_n(z)s_n(p)+Σ_m(m+1)t_m(z)`.

These are finite native observer identities, retaining the originally defined BRC branch multiplicities; the rational arithmetic here evaluates their readouts and does not substitute a classical continuous dynamics.

## Proof and executable finite certificate

All computations use integers and Python `Fraction`. For each nonnegative integer `d≤n`, the Bernstein derivative identity gives

`∂_p^d s_n(0)=n^{underline d} Δ^d f_n(0)`;

and the uniform bound `|∂_p^d s_n(p)| ≤ 2^{d−1} n^{underline d}` follows from `0≤f_n(k)≤1` and `|Δ^d f_n(k)|≤2^{d−1}`.

For `F(p,Q)=Σ_n c_n(Q)s_n(p)`, where `c_n` is any of `a_n,b_n,a'_n,b'_n`, build the **degree-20 Taylor polynomial for its second p-derivative**:

`T_F(p)=Σ_{j=0}^{20} [Σ_{n≥j+2} c_n(Q)n^{underline(j+2)} Δ^{j+2} f_n(0)/j!]p^j`.

For each rational coefficient, bound `c p^j` on `[0,ε]`, `ε=1/128`, by `min(0,c)ε^j` and `max(0,c)ε^j`. The remainder is bounded by

`ε^21 / 21! × Σ_{n≥23} cap_c(n) 2^22 n^{underline 23}`,

with `cap_c(n)=1`, `n+1`, `21`, or `21(n+1)`, respectively. The first two follow from the nonnegative negative-binomial moment kernels. The latter two follow from the proved `|t'_m(Q)|<21` score bound on J (PREFIX-665). No floating-point comparison enters the certificate.

To transfer the p bounds to all z∈J, note that the exact native Bernstein identity gives the uniform-in-p estimate

`B_n(ε)=n(n−1) Σ_{k=0}^{n−2} binom(n−2,k) |Δ²f_n(k)| ε^k`,

with `|s_n''(p)|≤B_n(ε)` for every `p∈[0,ε]`. The negative-binomial weighted derivatives and `|t_m''(z)|≤2m(m−1)` yield

`|μ_{ppzz}(p,z)|≤Z_μ = Σ_n 2(n+1)(n+2) B_n(ε)`,

`|H_{ppzz}(p,z)|≤Z_H = Σ_n 2(n+1)(n+2)(n+3) B_n(ε)`.

Therefore, with `δ=1/4096`, each center p-derivative bound is enlarged by at most `δ max_{p∈[0,ε]} |F_{ppz}(p,Q)| + δ² Z_F/2` (Taylor in z). The certificate **computes these bounds for the widened rectangle** rather than treating PREFIX-665's p=0 second-z bound as uniform at later p.

To bound the mean, use the previously proven `μ(0,Q)>89.455` and `|μ_z(0,z)|<3969` on J and the fresh native Bernstein envelope

`|μ_p(p,z)|≤C_p(ε)=Σ_{n=1}^{188} n Σ_{k=0}^{n−1} binom(n−1,k)|Δ f_n(k)| ε^k`,

which holds because `0≤a_n(z)≤1`. Consequently

`μ(p,z)>89.455−3969δ−ε C_p(ε)`.

Exact output of `PREFIX666_certificate.py` places the decisive estimates in the rational intervals

`86 < μ_lower < 87`, `226 < μ_pp_lower < 227`, `15366 < H_pp_upper < 15367`, `−8225 < W_pp_upper < −8223`,

with exact rational values produced in `PREFIX666_results.json`. Combining `W_pp=2H_pp−2 μ_p²−2 μ μ_pp` and dropping the nonpositive square term yields `W_pp≤2 H_pp_upper−2 μ_lower μ_pp_lower <−8000`. Finally `V_{q,pp}=q²W_pp−qμ_pp<−8000q²` for `q∈[12,24]`. Integration proves the theorem.

## Execution, checks, limitations, next action

`python PREFIX666_certificate.py` recomputes the entire original 189-layer integer survivor recurrence and exact 20th-order Taylor/interval certificate, emitting `PREFIX666_results.json`. The independent `python PREFIX666_independent_sample_checks.py` reconstructs the readout and directly verifies all nine endpoint/midpoint checks at p∈{0,1/256,1/128} and z∈{607/4096,19/128,609/4096}; these **samples corroborate but do not prove** the uniform theorem. The finite rational certificate plus the analytic remainder bounds is the actual proof mechanism.

This is an **author-side, unreviewed, model-internal exact theorem** relying on PREFIX-659/660/661/665 and the frozen BRC observer pin. It does not establish the X6 rotation Task's arbitrary-triad signed C6 or native Cell-path lift, nor global maximality on the whole parameter square.

Next discriminating problem: use a two-variable Bernstein/subdivision certificate on the remaining complement `[1/128,1] × [0,1]` to bound the variance objective against the same edge maximizer; a separate route is to improve derivative cancellation to widen this local strip beyond `1/128` without inventing a physical rotation law. Maintain actual task-owner and native Result/Review authority separately from this independent author contribution.
