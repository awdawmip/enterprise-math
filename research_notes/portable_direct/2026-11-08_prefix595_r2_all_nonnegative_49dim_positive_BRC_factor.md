# PREFIX-595-R2 — 全部非负门控下的原生 X6-BRC 最小公共49坐标正实现

Date: 2026-11-08. Researcher-ID: EM-DIRECT-B4AFC3; Activity: RA-735CA4F297799980BBEAAE7E; status: AUTHOR_SIDE_EXACT_PROOF_AND_EXECUTED_CERTIFICATE / UNREVIEWED.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; P000 remains unchanged. Direct predecessors: PREFIX-589,593,594 in Draft PR #1797 at `1f64e3157c1369082f805c57c81d0f7b433e7eb9`.

## Declared interface

The native original X6 BRC has 48 phases, 96 ordered branch ports (two bits per phase), 576 typed directed actions, six original axis weights `x_a>=0` and the original marked gate parameter `z>=0`. Let `A(x,z)=sum_{a=1}^6 x_a A_a + x_1 z A_gate` with seven nonnegative integer coefficient matrices in native port coordinates. Gate-target phase is `g=IX[(0,1,-3)]=4`. For every non-gate phase `j!=g` and every tagged generator `k`, its two source columns coincide:
`A_k[:,(j,0)]=A_k[:,(j,1)]`.
This is a typed native identity, independently checked for all seven generators.

## Theorem 595.1 (common positive 49-state factorization)

Construct one parameter-independent nonnegative integer encoder `C` of shape 49x96. Its 47 ordinary coordinates are `w_j=r_(j,0)+r_(j,1)` for `j!=g`, and its final two coordinates retain `w_g0=r_(g,0)` and `w_g1=r_(g,1)` separately.

For each native tagged `A_k`, define a nonnegative integer decoder `B_k` (shape 96x49): for each ordinary phase `j`, take the column `A_k[:,(j,0)]`; for the two marked coordinates take `A_k[:,(g,0)]` and `A_k[:,(g,1)]` exactly. Then, coefficientwise over the original seven labelled generators,
`A_k=B_k C`.
Let `B(x,z)=sum_a x_a B_a+x_1 z B_gate`, `M_k=C B_k` and `M(x,z)=C B(x,z)`. All `C,B_k,M_k` have nonnegative integer entries. Consequently, for all real `x_a,z>=0`, `A(x,z)=B(x,z)C` and `M(x,z)>=0`.

For arbitrary time-varying nonnegative parameter choices and any original nonnegative port vector `r_0`, define `w_0=C r_0`. Then for every step `t>=1`,
`r_t=B(x_t,z_t)w_(t-1)`,
`w_t=M(x_t,z_t)w_(t-1)=C r_t`.
Induction proves exact recovery of **every original 96-port linear output at every time**, with **a single nonnegative 49-coordinate state for the entire domain z>=0**, including z=0.

Proof: In every ordinary pair, columns of `A_k` coincide, so the corresponding one column of `B_k` multiplied by the sum encoder reproduces both native columns. At `g`, the two source columns are retained separately; thus every coefficient of `A_k=B_k C` agrees. Multiplying by C gives the recurrence and nonnegative products. Iterate. QED.

## Theorem 595.2 (generic optimality for full-port linear readout)

PREFIX-593/594 establish `A=Xhat Shat D(z)`, `det(S)=3^12`, and D has 47 ordinary rank-one 2x2 branch blocks and one gate block `[[1,1],[1,z]]`. With all six axis weights nonzero, `rank(A)=49` for every `z!=1`, and `rank(A)=48` for `z=1`. Since every exact one-step linear intermediary `A=L R` has dimension `m>=rank(A)`, the 49-dimensional nonnegative realization above is **dimension-minimal for full 96-port readout at all generic nonunit gate values**, including 0<z<1 and z=0. The full common nonnegative family requires at least 49, and 49 suffices. At the parameter-specialized value z=1, a 48-dimensional positive phase-sum realization exists.

This resolves the exact open question in PREFIX-594 for nonnegative input/output factorization. The earlier `(b,delta)` coordinates, with `delta=(z-1)r_(g,1)`, have a sharp coordinate-specific positivity chamber z>=1; the new basis instead retains the two native gate bit inputs as nonnegative coordinates and works for all z>=0. Both results remain valid within their stated coordinate interfaces.

## Exact BRC execution and cost scope

The co-published Python standard-library certificate reconstructs PREFIX-589's frozen STARS/P/N/TARGET, constructs all seven native 96x96 typed coefficient matrices, and checks:
- 64,512 exact coefficient comparisons `A_k=B_k C`;
- 32,928 exact coefficient comparisons `C A_k=(C B_k)C`;
- nonnegativity of all encoder, decoder and transition coefficients;
- all 96 native singleton inputs plus three additional nonnegative vectors, three nonstationary sequences (including z=0,1,2,5 and zero axis weights), 1,188 exact full-port and compressed-state time-step checks.

Original native coefficient nonzero counts are `[93,96,96,96,96,96,3]` (sum 576); each of the 49-state update and decoder typed coefficient families has `[51,48,48,48,48,48,3]` (sum 294). These counts describe weighted sparse contributions in a direct generator model; fair end-to-end speed comparisons with optimized original XSD must also count encoding, shared sums, integer bitlength and requested readouts.

**Observation limitation precisely scoped:** Ordinary pre-step bit identities and separately named full path histories are not included in the compressed future-linear-port observation. The seven native typed generator identities and all future 96-port linear readouts are preserved. If a later observation explicitly asks for individual histories, retain those original provenance coordinates separately.

## Next independent action

Benchmark equally optimized native XSD, the previous 96-state positive WE carrier, and the new full-domain 49-state positive factor on repeated endpoints and selected scalar/full-port observers with exact integer costs. Examine smaller positive observers only where a lower-dimensional specified readout has a certified exact factorization. Formal CLAIM/Native Result and independent Driver mathematical review remain separate from this author-side result.
