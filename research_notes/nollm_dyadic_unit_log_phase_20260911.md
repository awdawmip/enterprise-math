# Dyadic unit-log multiplicative field: exact carrier, dyadic discrepancy bound, and layer split

Status: `RESEARCH_NOTE / PROVED_DERIVATION_IN_DECLARED_FINITE_MODEL + FINITE_GEOMETRIC_OBSERVER / NOT_FOUNDATION / NOT_NOLLM_RUNTIME`

Date: 2026-09-11  
Research activity: `RA-nollm-multiplication-field-20260911-c6c82`

## 1. Why this branch exists

The reciprocal-prime phase candidate improved finite angular/cell statistics, but its random-access evaluation from an arbitrary integer value still naturally exposes a prime-factorization carrier. This note asks whether multiplication can be placed into a dyadic-resolution field **without factoring the odd part**.

The classical unit-group fact is the starting point, not a novelty claim: for `b>=1`, with `M=2^b` and `Q=2^(b+2)`, every odd unit modulo `Q` has a unique representation

`u = (-1)^eps * 5^t (mod Q)`, with `eps in {0,1}` and `t in Z/MZ`.

Equivalently `(Z/QZ)^× ~= C2 × C_M`.

## 2. Exact multiplicative carrier

For `n>0`, write

`n = 2^v u`, where `v=v_2(n)` and `u` is odd.

At dyadic precision `b`, define

`C_b(n) = (v, eps_b(u), t_b(u))`,

where `u=(-1)^eps 5^t mod 2^(b+2)`.

Then multiplication is componentwise:

- `v(ab)=v(a)+v(b)`,
- `eps(ab)=eps(a)+eps(b) mod 2`,
- `t_b(ab)=t_b(a)+t_b(b) mod 2^b`.

Thus this is an exact monoid homomorphism into

`N × C2 × C_(2^b)`.

No prime factorization is required to evaluate `C_b(n)`: strip powers of two, inspect the odd residue modulo `2^(b+2)`, choose the `eps` sheet from the residue modulo 4, and compute the base-5 discrete log inside the cyclic `1 mod 4` subgroup.

The complete integer identity `n` remains the canonical identity. `C_b` is a finite-resolution multiplicative observer and is many-to-one as a residue observer.

## 3. Exact bitwise unit-log decoder

For `a=5^t mod 2^(b+2)` with `a=1 mod 4`, the bits of `t=sum_j tau_j 2^j` can be recovered low-to-high.

After bits `<j` have been removed, the residual is `1 mod 2^(j+2)`. The exact valuation identity

`v_2(5^(2^j)-1)=j+2`

implies that modulo `2^(j+3)` the next residual is either

`1` or `1+2^(j+2)`.

The latter means `tau_j=1`; multiply by the inverse of `5^(2^j)` and continue. This uses `O(b)` refinement decisions and no factorization of `u`.

The verifier exhaustively compares this bit decoder with a complete discrete-log table for precisions `b=3,...,12`: **8,184 exact cases, zero failures**.

## 4. Optional one-circle character

If a single circle observer is desired at fixed precision, one may compose the source coordinates as

`Phi_b(n)=t_b(u) + eps_b(u)*2^(b-1) + v_2(n)*2^(b-3) (mod 2^b)`

for `b>=3`.

This sends the `C2` sheet to a half-turn and one factor of 2 to a 45-degree turn. At fixed `b`,

`Phi_b(ab)=Phi_b(a)+Phi_b(b) mod 2^b`.

Consequently the ideal symbolic polar coordinate

`z_b(n)=sqrt(n) * exp(2*pi*i*Phi_b(n)/2^b)`

satisfies ordinary multiplicative composition at the declared observer level. Floating trigonometry and physical hex rounding are **not** part of the proof.

For Nollm interpretation it is cleaner not to collapse all three source components into one angle: current Nollm research keeps ideal adjacent-layer rotation 22.5 degrees and `beta=2^(1/4)`. A factor `2^v` corresponds to `2v` virtual layer intervals, giving scale `beta^(2v)=2^(v/2)` and frame rotation `45v` degrees. The `t` coordinate can therefore remain a lateral unit phase, while `v` supplies the exact dyadic layer component and `eps` remains an explicit two-sheet state.

This is an observer construction only; it does not modify Nollm physical-layer semantics.

## 5. Exact dyadic-block phase theorem

Fix `b>=3`, `M=2^b`, and let `L>=b+2`. Observe the positive integers

`1 <= n < 2^L`.

For every phase value `a in Z/MZ`, its count has the exact form

`H_(L,b)(a) = 2^(L-b) - 2 + R_(L,b)(a)`,

where

- `R_(L,b)(a) >= 0`,
- `sum_a R_(L,b)(a) = 2^(b+1)-1`.

### Proof

Partition by `v=v_2(n)`. For

`0 <= v <= L-b-2`,

the odd part ranges across an integer number of complete residue systems modulo `Q=2^(b+2)`. There are `2^(b+1)` odd units modulo `Q`.

The map

`(-1)^eps 5^t -> t + eps*M/2`

is a surjective group character onto `Z/MZ` with kernel size two. Therefore each complete odd-unit residue system contributes **exactly two representatives to every phase**. At fixed `v`, each phase occurs

`2^(L-v-b-1)`

times; the additional `v*M/8` is only a cyclic phase shift.

Summing `v=0,...,L-b-2` gives the common pedestal

`2^(L-b)-2`.

The remaining valuations contain exactly

`1+2+...+2^b = 2^(b+1)-1`

integers, producing the nonnegative remainder `R`. QED.

## 6. Consequences: deterministic phase discrepancy at the geometric critical scale

Let `P_(L,b)` be the empirical distribution of `Phi_b(n)` on `1<=n<2^L`, and `U_M` the uniform distribution on `Z/MZ`. The theorem writes `P` as an exactly uniform pedestal plus a tail of size `T=2^(b+1)-1`. Hence

`TV(P_(L,b), U_M) <= (2^(b+1)-1)/(2^L-1)`.

Every nontrivial discrete Fourier coefficient satisfies the same upper bound, and the discrepancy of every subset of phase bins is bounded by this total variation.

This gives a particularly useful scaling. If

`b = L/2 + O(1)`, so `M = Theta(sqrt(N))`,

then

`TV = O(N^(-1/2))`.

This is exactly the order suggested independently by the geometric resolution requirement for a radius `sqrt(N)` disk: adjacent angular spokes at the outer radius have spacing approximately

`2*pi*sqrt(N)/M`.

Thus the regime `M=Theta(sqrt(N))` simultaneously gives:

1. enough angular directions to keep outer spoke separation at constant cell scale, and
2. a proved `O(N^(-1/2))` global phase-discrepancy bound on dyadic populations.

This square-root compatibility is a proved statement for the declared phase observer on dyadic populations. It is **not** a theorem about Nollm physical Coverage or semantic recall.

## 7. Resolution tower: why one fixed circle is the wrong infinite object

The exponent coordinates refine exactly:

`t_(b+1) = t_b + eta_b 2^b`, with `eta_b in {0,1}`.

If

`w_b = exp(2*pi*i*t_b/2^b)`,

then

`w_(b+1)^2 = w_b`.

So the successive circle observations do not preserve the same point angle; the finer point chooses one of two square roots of the coarse point. This is the bonding relation of the dyadic-solenoid inverse-limit picture. The underlying exact exponent carrier is the 2-adic coordinate `t in Z_2`; the circle at each `b` is a finite observer of that carrier.

This resolves an earlier tension: a single fixed circle cannot both keep all old angles unchanged and obtain a genuinely new binary phase bit while preserving group homomorphism. The extra bit must appear as a branch/root choice, or the representation must gain another coordinate/history surface.

## 8. Finite geometry observations

The following are **display-observer measurements**, not part of the theorem.

At `N=65,536`, choose the geometric critical precision `b=11`, `M=2048`:

- 64-sector CV: `0.0068131`;
- occupied 2D display hex cells: `58,486 / 65,536 = 0.89243`;
- 2D collision groups: `6,082`, maximum load `8`.

If the arithmetic sheet `eps` and valuation `v_2` are retained alongside the displayed cell rather than projected away, the same run has:

- unique `(cell,eps,v_2)` states: `64,863 / 65,536 = 0.98973`;
- collision groups: `665`;
- maximum load: `3`.

At `N=1,000,001`, `b=13`, `M=8192`:

- 64-sector CV: `0.00118772`;
- occupied 2D display cells: `891,433 / 1,000,001 = 0.89143`;
- retaining `(eps,v_2)` raises distinct `(cell,eps,v_2)` states to `988,931 / 1,000,001 = 0.98893`, maximum load `4`.

A sweep over `N=2^10,...,2^20` using `b=ceil(log2(2*pi*sqrt(N)))` keeps the observed 2D occupied ratio near 0.89 and the layered ratio near 0.99 in this finite population. These ratios are empirical; no asymptotic occupancy theorem is claimed.

The exact source-coordinate version with the lateral angle using only `t` gives 64,866 distinct `(cell,eps,v_2)` states at `N=65,536`; the 64,863 figure above includes the optional half-turn/dyadic-frame angle in the 2D projection. This distinction is retained rather than hidden.

## 9. Comparison with reciprocal-prime phase

The reciprocal-prime candidate assigns a generator to each prime and extends by valuation. The unit-log carrier instead obtains the multiplicative phase from the **odd residue of n itself**. It therefore closes the random-access factorization concern for the finite dyadic observer.

At the same `N=65,536`, `b=11`, the reciprocal candidate has approximately 57,342 occupied display cells and angular CV about 0.02598. The natural unit-log character gives 58,486 occupied cells and CV about 0.00681 under the same display scale.

The comparison does not establish a universal ordering: maximum cell load and other local statistics differ, and the display quantizer is not native Nollm geometry.

## 10. Classical context and novelty boundary

The structure `(Z/2^kZ)^× ~= C2 × C_(2^(k-2))`, with 5 generating the `1 mod 4` subgroup, is classical. Likewise inverse-limit/solenoidal language is standard topology. The research contribution claimed here is only the **combination** with the multiplicative-memory-field question, the exact dyadic population count, the square-root phase-resolution compatibility, the factorization-free layered interpretation, and the measured Nollm-oriented observer consequences.

## 11. Next unresolved unit

The next useful step is not more random phase search. It is to decide how the exact source triple

`(v_2, eps, t in Z_2)`

should meet actual Nollm `22.5° / beta / Q40 Coverage` without flattening away the coordinates that make multiplication and refinement exact.

Candidate implementation experiment: retain `v_2` and `eps` as explicit research-state coordinates, expose `t_b` as a binary-refining lateral observer, and compare physical Coverage/recall locality against the existing prime-phase pages. No production change is authorized by this note.
