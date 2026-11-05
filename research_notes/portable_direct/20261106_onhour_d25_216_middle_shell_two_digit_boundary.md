# D25 SECOND-DIGIT-LIFT — original 216 middle-shell two-digit reflection and single-index boundary

Date: 2026-11-06. Mode: TASK_RESEARCH, AUTHOR-SIDE EXACT DERIVATION / 80-PRIME INTEGER CHECK, UNREVIEWED / NOT_ADMITTED. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; **frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3**. Research logical lane: `chatgpt-research-onhour-enterprise-math-20260923`; no maintenance lane identity. Does not supersede any native execution checkpoint.

## 1. Previously established inputs and question

The inherited original 216 coefficient is
$$
a_k=\frac{(2k)!(3k)!}{216^k(k!)^5}
=\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k}.
$$
The original 2304 coefficient is `b_k=binom(2k,k)^2 binom(4k,2k)/2304^k`. Put `W_p=sum_{k=0}^{p-1}(6k+1)a_k`, `V_h=sum_{k=0}^{h}(8k+1)b_k`, `h=(p-1)/2`. Consume the earlier proved full/half 2304 congruence and frozen source scalar equivalence; mother objective remains `Delta_p-R_p=0 (mod p)` for `p=13,19 (mod 24)`, corresponding to `W_p-V_h=0 (mod p^3)`. The preceding author-side CM-cusp triangular kernel `T[n,k]` and reflected 2304 compensation tail remain historical inputs; no new acceptance is inferred.

For primes `p=1 (mod 6)`, `p>=7`, define
$$
m=(p-1)/3,\quad J=(p-7)/6,\quad s=(p+1)/2,\quad L=\lfloor(2p-1)/3\rfloor.
$$
The exact valuations of `a_k` on `0<=k<p` split the original 216 sum into `0<=k<=m` (valuation zero), `m+1<=k<=h` (valuation one), `s<=k<=L` (valuation two), and `k>L` (valuation at least three). This is the narrowest single-index carrier for the missing p^3 digit and retains every source index/weight.

## 2. Theorem — two p-adic digits at the middle-shell top

For every prime `p=1 (mod 6)`, `p>=7`, let
$$
q_p(a)=(a^{p-1}-1)/p\pmod p,\quad \epsilon_p=(6/p)\in{+1,-1},
\quad
\gamma_p=3+2q_p(2)-\frac32q_p(6)\pmod p.
$$
Then
$$
\boxed{a_h/p\\equiv -2\epsilon_p(1+p\gamma_p)\pmod{p^2}.}
$$

Proof. Since `3h=p+h-1`, exact factorial rearrangement gives
$$
\frac{a_h}{p}
=\frac{\binom{p-1}{h}^{,2}}{h,216^h}
prod_{i=1}^{h-1}(1+p/i).
$$
Use `binom(p-1,h)=(-1)^h product_{i=1}^h(1-p/i)`, hence `binom(p-1,h)^2=1-2p H_h (mod p^2)`; multiply the remaining product to obtain `1-p(H_h+1/h)`. The standard finite harmonic identity `H_h=-2q_p(2) (mod p)` follows by expanding `2^p-2=sum_{i=1}^{p-1} binom(p,i)` and pairing the alternating harmonic sum. Further `1/h=-2(1+p) (mod p^2)`. Because `216^h=6^{3h}`, Euler's criterion and `(6^h)^2=1+p q_p(6)` give `216^{-h}=\epsilon_p(1-3p q_p(6)/2) (mod p^2)`. Multiplication proves the boxed formula. All denominators are p-units.

## 3. Theorem — exact reflected 216 hypergeometric kernel and differential endpoint

For `0<=j<=J`, set
$$
Q^A_{p,j}=
2^j\frac{(-h)_j^3}
{(1-p/2)_j(5/6-p/2)_j(7/6-p/2)_j},
\q\quad H^A_{p,J}(z)=sum_{j=0}^{J}Q^A_{p,j}z^j.
$$
The exact backward ratio of the original 216 coefficient is
$$
\frac{a_{h-j-1}}{a_{h-j}}=
\frac{18(p-2j-1)^3}{(p-2j-2)(3p-6j-7)(3p-6j-5)}
$$
for `j<J`. Its denominators are p-units on this precisely declared range, and the ratio equals `Q^A_{p,j+1}/Q^A_{p,j}`. Hence **exactly** `a_{h-j}/p=(a_h/p)Q^A_{p,j}` for all `0<=j<=J`.

The weight reverses as `6(h-j)+1=3p-2-6j`. Thus for the original signed middle-shell sum `M_p=sum_{k=m+1}^h(6k+1)a_k`,
$$
\boxed{\frac{M_p}{p}\equiv
-2\epsilon_p(1+p\gamma_p)
\big[(3p-2)H^A_{p,J}(1)-6\theta H^A_{p,J}(1)\big]\pmod{p^2},\quad\theta=z,d/dz.}
$$

Its exact fourth-order inhomogeneous endpoint is
$$
\mathcal L^A_p=
\theta(\theta-p/2)(\theta-1/6-p/2)(\theta+1/6-p/2)
-2z(\theta-h)^3(\theta+1),
$$
$$
\boxed{\mathcal L^A_pH^A_{p,J}(z)=
-2(J+1)(J-h)^3Q^A_{p,J}z^{J+1}.}
$$
Proof: the hypergeometric coefficient recurrence annihilates each degree `0..J`. Truncation leaves exactly the displayed `J+1` endpoint. This is the **216-model** companion of the already proved, different 2304 signed-tail `4F3` operator with `z=9` and quarters `±1/4` instead of sixths `±1/6`. Do not identify the two boundaries without the lower-shell and upper-shell compensation.

For first-order p-deformation, write
$$
q_j=2^j\frac{(1/2)_j^3}{j!(5/6)_j(7/6)_j},\quad
D_j=sum_{i=0}^{j-1}\left[-\frac3{2i+1}+\frac1{2i+2}+\frac3{6i+5}+\frac3{6i+7}\right].
$$
Then `Q^A_{p,j}=q_j(1+pD_j) (mod p^2)`, all declared denominators units. This supplies independently checkable two-digit transport.

## 4. Strict single-index exact reduction of the still-open LIFT

Put `B_p=sum_{k=0}^{m}(6k+1)a_k`, `U_p=sum_{k=s}^{L}(6k+1)(a_k/p^2)`, where `U_p` is needed modulo p. Exact valuations give
$$
\boxed{W_p\\equiv B_p+p(M_p/p)+p^2U_p\pmod{p^3}.}
$$
For target primes `p=13,19 (mod24)`, inherited first-digit congruences supply `p | (B_p-V_h)`. Therefore define the genuine two-digit observation
$$
D_p=(B_p-V_h)/p\pmod{p^2}.
$$
The mother third-digit condition is **\equivalent**, under the already pinned source scalar bridge, to the explicit *single-index* certificate
$$
\boxed{D_p-2\epsilon_p(1+p\gamma_p)
[(3p-2)H^A_{p,J}(1)-6\theta H^A_{p,J}(1)]
+pU_p\\equiv0\pmod{p^2}.}
$$
This avoids computing the previously constructed triangular CM-cusp matrix `T[n,k]`; it consumes one low-index 216 band, the original 2304 half-sum, one finite `216-4F3` middle polynomial and one valuation-two 216 band. It is a **strict single-index representation reduction**, not a completed all-prime vanishing proof. In particular a direct identification of `M_p/p` with the 2304 `V_tail/p` fails already for `p=13` (`149 != 89 mod169`): lower/upper signed ports matter.

## 5. Exact executed evidence / provenance

An author-side Python arbitrary-precision integer checker independently computes original binomial coefficients modulo `p^3`, the h-unit modulo `p^2`, each reflected `Q^A_{p,j}`, harmonic deformation, all fourth-order operator coefficients and the exact three-band W reconstruction. **80 primes p<=997 with p=1 mod6: all assertions passed**. Representative tuples `(p,J,a_h/p,M_p/p,D_p,U_p)`:
- `(7,0,30,31,32,5)`;
- `(13,1,145,149,59,10)`;
- `(19,2,131,254,297,9)`;
- `(67,10,1941,3079,2013,58)`;
- `(139,22,13759,18596,18239,13)`;
- `(373,61,19771,103721,75319,266)`;
- `(997,165,847452,651941,315149,27)`.
All displayed congruence residues use their indicated p-adic moduli. For each tested prime, `D_p+M_p/p+p U_p=0 (mod p^2)`; this remains a **finite observation** outside the proven identity and source premises. Test code `d25_216_middle_shell_reflection_20261106.py`; results `20261106_onhour_d25_216_middle_shell_reflection_results.json`.

**BRC:** `COMPOSE_APPLIED` to the original 216 coefficient and frozen 2304 half-sum; carrier records (model, p, k, reversed j, unit/valuation band, p-local q2/q6, sign ε, derivative θ, endpoint J, signed D and U). Allowed operations are p-adic division on the declared valuation band and precisely matched sums. Whole-sum compression takes place only after retaining all bands.

**Native gap** unchanged: original-class p=373 fixed H0/B0 divided-power module, `[X]U mod139129`, actual rank, semilinear Frobenius η/κ, odd Green/Hesse observer and independently reproducible native witness remain pending under Issue #1559, with no named executor at last read. This author-side hypergeometric certificate is NOT a native replacement or formal Result.

**Next exact work:** seek an adjoint/telescoper that kills the explicit `D_p+p U_p` bottom/upper correction against the new `216-4F3` endpoint, or connect it to the existing 2304 `4F3` boundary without erasing signed ports; separately execute native p373 input via lawful Source operator. Current formal Source claim/run/review states must be reconciled independently.
