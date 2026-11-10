# PREFIX-680-R6 — Third-order BRC crossover certificate on a 737× larger slot band

Date: 2026-11-11 (Asia/Shanghai). Research mode: independent TASK_RESEARCH.
Status: AUTHOR_DERIVED / EXACT_INTEGER_FRACTION_RECOMPUTED / UNREVIEWED / NOT_ADMITTED.

**Frozen scientific input:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
**Prior frontier:** PREFIX-676 (`cd2c6681a6ed4857bb7d416e82a8642f6cc0739f`), local center jets (`d344451396a9bace91a9cbcdb14475c6641a9223`), PREFIX-678 (`029ecd8afe03187ea5b166708546a9d7e0554567`), PREFIX-679 (`79bac3086650d2772d4c6cb81fa27644c20be84e`).
BRC observer parameters are scalar probabilities/readouts of a frozen X6 Heartbeat World path observation, not newly introduced primitive spatial dimensions. Source P000, ACTIVE worldview and original scientific pin remain unchanged.

## Problem and exact objects

The same frozen 189-layer survivor histogram has `A_n(k)` surviving count paths after n observations, for n=0,...,188, with empty row n=189. Write
`s_n(x)=Σ_k A_n(k)x^k(1-x)^(n-k)`.
For independent Poissonized clocks `Y_p,Y_z`, put `Y(p,z)=max(Y_p,Y_z)`,
`μ(p,z)=E Y(p,z)`, `W(p,z)=Var Y(p,z)`, `V_q(p,z)=q² W(p,z)-q μ(p,z)`.
The difference between the diagonal and edge configurations factors as
`D_q(z):=V_q(z,z)-V_q(0,z)=qA(z)[q-q₀(z)]`, where
`A(z)=W(z,z)-W(0,z)`,
`B(z)=μ(z,z)-μ(0,z)`, and `q₀(z)=B(z)/A(z)` wherever `A(z)>0`.

The predecessor PREFIX-679 certified a single crossing for each real
`q∈[17.94869,17.94888]` inside `|z-0.053|≤1/330000000`.

## New theorem

Let `b=53/1000`, `ρ=1/625000` and
`I=[b-ρ,b+ρ]`. Then **for every real z∈I**,

`437/1000 < A(z) < 444/1000`,
`789/100 < B(z) < 791/100`,
and
**`45000 < q₀'(z) < 100000`**.

Consequently, for **every real q** in the explicitly certified range

`J=[447/25,901/50]=[17.88,18.02]`,

there exists exactly one `z_q∈I` with `D_q(z_q)=0`, and its crossing is transverse. On `I`, `D_q(z)>0` for `z<z_q`, and `D_q(z)<0` for `z>z_q`.
The inverse curve is differentiable on the interior of J and
`1/100000 < dz_q/dq < 1/45000`.

The **certified q-band width** increased from `19/100000` to `7/50`, exactly by `14000/19 > 736`; the **z radius** increased from `1/330000000` to `1/625000`, exactly by `528`.

## Proof, with independent exact model replay

**1. Finite path and moments.** The attached standard-library Python checker recomputes all 189 frozen rows (9,529 occupied cells), without changing the predecessor acceptance predicate. It constructs the first two derivatives of `s_n` at b by integer power sums, hence obtains exact rational values for
`A(b), A'(b), A''(b), B(b), B'(b), B''(b)`.
The exact floors after multiplication by 10^8 are, respectively,

`A: (44000296, -168056589514, -6667624082229)`,
`B: (789752024, 12845959424, -99127959112)`.

The same computation gives
`floor(10^8 q₀(b))=1794878866`,
`floor(10^8 q₀'(b))=6884631251314`,
and `floor(10^8 q₀''(b))=52862665534319204`.
These are exact rational floors; all strict comparisons below use the exact fractions, not these shortened decimal displays.

For `K_nm=binom(n+m,n)/2^(n+m+1)` and `J_nm=(n+m+1)K_nm/2`, the exact finite moments used are

`μ(p,z)=Σ_n[s_n(p)+s_n(z)] - Σ_nm K_nm s_n(p)s_m(z)`,

`H(p,z)=E[Y(p,z)^2]/2
=Σ_n(n+1)[s_n(p)+s_n(z)] - Σ_nm J_nm s_n(p)s_m(z)`,

`W=2H-μ²`. All n,m run from 0 through 188.

**2. Third-derivative certificate.** Each normalized Bernstein coefficient
`c_nk=A_n(k)/binom(n,k)` lies in [0,1]. With `N=189`, `M=188`, the standard Bernstein derivative-difference identities yield, uniformly for `x∈[0,1]`,

`|s_n|≤1`, `|s_n'|≤M`, `|s_n''|≤2M(M−1)=:d₂`,
`|s_n'''|≤4M(M−1)(M−2)=:d₃`.

For nonnegative K, `Σ_m K_nm≤1`; for the truncated range `J_nm≤N K_nm`. Differentiating the displayed finite moments along the two paths `(p,z)=(z,z)` and `(p,z)=(0,z)` and using their product rules gives uniform majorants

`U₀=3N`, `U₁=4NM`,
`U₂=N(4d₂+2M²)`,
`U₃=N(4d₃+6Md₂)`,
`H₃=N²(4d₃+6Md₂)`, and
`W₃=2H₃+6U₁U₂+2U₀U₃`.

Thus for the **differences** A and B,
`|A'''(z)|≤2W₃=218571424275456=:a₃` and
`|B'''(z)|≤2U₃=69527880576=:b₃` throughout [0,1/2].
These are model-independent consequences of the frozen finite survivor bounds and the displayed Poissonized moment kernels; the exact checker verifies their integer values.

**3. Local Taylor envelopes.** For `|z-b|≤ρ`, set

`e_A=|A'(b)|ρ + |A''(b)|ρ²/2 + a₃ρ³/6`,
`e_B=|B'(b)|ρ + |B''(b)|ρ²/2 + b₃ρ³/6`,
`A_- =A(b)-e_A, A_+=A(b)+e_A`,
`B_- =B(b)-e_B, B_+=B(b)+e_B`.

Taylor's formula and exact arithmetic give
`437/1000<A_-<A_+<444/1000` and
`789/100<B_-<B_+<791/100`.

In addition `|A''(z)|≤|A''(b)|+a₃ρ=:a₂^+` and
`|B''(z)|≤|B''(b)|+b₃ρ=:b₂^+`.

For `R=B'A-BA'`, the cancellation identity
`R'=B''A-BA''` implies

`R(b)-Lρ < R(z) < R(b)+Lρ`, where
`L=b₂^+ A_+ + B_+ a₂^+`.

Since `A_->0`, direct exact Fraction checks of the full rational jet give

`45000 < (R(b)-Lρ)/A_+² ≤ R(z)/A(z)²
≤ (R(b)+Lρ)/A_-² < 100000`.

Here `R(z)/A(z)²=q₀'(z)`. This proves the derivative and positivity claims; the exact envelope lower slope is greater than 45427 and the exact upper slope less than 92872.

**4. Full real-q band and sign.** Exact center arithmetic also verifies

`q₀(b)-45000ρ < 447/25 < 901/50 < q₀(b)+45000ρ`.

Since q₀ is continuous, strictly increasing on I, its image contains J in its interior. The intermediate value theorem proves existence for every q∈J, monotonicity proves uniqueness, and the displayed factorization of D proves the sign orientation. The inverse-function theorem gives the inverse derivative range.

## Execution and research status

The exact-Python replay was executed on the local author environment with integers and `Fraction` only, and returned `ALL_CHECKS_PASS PREFIX680-R6` on all asserted mathematical inequalities. Replayed precursor survivor structure and local center jets rather than depending on a floating approximation or claiming a new freeze. Run time on this environment was approximately 18 seconds, not a complexity guarantee. Source code: `PREFIX680_R6_EXACT_THIRD_ORDER_CROSSOVER_CERTIFICATE.py`; result summary: `PREFIX680_R6_RESULTS.json`.

Result type: author-side model-internal theorem and exact-computation certificate; independent semantic review, formal Result and Working Truth/Foundation admission remain to be carried out under their native roles. No shared CLAIM or Owner change is asserted by this research note.

**Next mathematical action:** Use this certified `0.0529984<z<0.0530016` neighborhood as a sign-correct slice in the two-dimensional Bernstein/pruning search. To reach the full 0.052–0.054 crossing bracket, derive local Bernstein second-derivative envelopes on consecutive rational subintervals, reusing the exact 189-row kernel. For the mother objective, certify the variance gap relative to the complete `p=0` maximum from PREFIX-675 throughout the remaining `0≤p≤z≤1/2` triangle.
