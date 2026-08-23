# Statement packet — high-dimensional prime walls and support-filter algebra

Status: `FROZEN_TARGETED_VERIFICATION_INPUT`

Date: `2026-08-23`

Packet-ID: `HIGHDIM_PRIME_WALL_FILTER_EQUIVALENCE_PACKET_20260823`

## 1. Evidence typing

This packet exposes candidate statements but withholds the source derivations and source code. The receiving researcher must first reconstruct or refute the mathematics independently. Only after an independent theorem checkpoint is frozen may the researcher perform the required classical-equivalence and prior-art audit.

Do not use the free-research branch, Draft PR #595, its scripts, its source notes, or the GLOBAL_KNOWLEDGE research narrative as proof evidence before the checkpoint.

## 2. Primitive counting objects

For `s>=1` and `n>=1`, let `A_s(n)` be the number of ordered `s`-tuples of strictly positive integers

`(x_1,...,x_s)`

such that

`x_1^2+...+x_s^2=n`.

For `d>=1`, define the nonnegative-coordinate shell count

`C_d(n)=sum_{s=1}^d binom(d,s) A_s(n)`.

For a formal parameter `lambda`, define

`W_{d,lambda}(n)=sum_{s=1}^d binom(d,s) A_s(n) lambda^s`.

Equivalently, with

`S(q)=sum_{m>=1} q^(m^2)`,

`W_{d,lambda}(n)=[q^n](1+lambda*S(q))^d`.

Convolution below is additive convolution in `n`, with the usual `n=0` identity term restored when generating functions are used.

## 3. Candidate combinatorial identities

Classify the following as proved, narrowed, or refuted.

### H1. Support decomposition

`C_d(n)=sum_s binom(d,s) A_s(n)` is the exact reconstruction of the nonnegative shell from its positive-support spectrum.

### H2. Recoloring semigroup

For the carrier transform

`T_lambda(F)=1+lambda*(F-1)`,

`T_lambda o T_mu = T_(lambda*mu)`.

Determine precisely what this does and does not imply for the coefficient arrays `W_{d,lambda}`.

### H3. Dimension convolution

`W_{d+e,lambda}=W_{d,lambda}*W_{e,lambda}`.

Give the exact coefficient-level statement, including the `n=0` convention.

### H4. Fixed-face survival

For `C_d(n)>0`, deletion of one named coordinate has survival ratio

`C_{d-1}(n)/C_d(n)=1-E_d[s]/d`,

where `E_d[s]` is mean support size under the uniform nonnegative shell state.

## 4. Candidate four- and eight-dimensional walls

Define

`Q4(n)=2*C_4(n)-4*C_3(n)+3*C_2(n)`,

and

`Q8(n)=16*C_8(n)-64*C_7(n)+112*C_6(n)-112*C_5(n)+70*C_4(n)-28*C_3(n)+7*C_2(n)`.

Classify:

### H5. Four-dimensional wall

For every odd integer `n>1`,

`n is prime  <=>  Q4(n)=n+1`.

For `n=p*q` with distinct odd primes,

`Q4(n)-(n+1)=p+q`.

### H6. Eight-dimensional wall

For every odd integer `n>1`,

`n is prime  <=>  Q8(n)=n^3+1`.

The researcher must identify the exact divisor-sum content of `Q4` and `Q8`, rather than treating finite zero-mismatch tests as proof.

## 5. Candidate lambda=2 classification

At `lambda=2`, `W_{d,2}` numerically matches the signed-coordinate square-shell multiplicity obtained by decorating each positive coordinate with two signs. This is an arithmetic audit channel; it does not by itself add negative axes to the native carrier.

For odd prime `p`, candidate H7 states that `lambda=2` is the unique nonzero value satisfying the following stated criterion in `d=4`:

> the coefficient vector of `W_{4,lambda}(p)` on the admissible support components is proportional to the single four-square divisor wall, so the readout is support-composition independent.

The researcher must formalize the criterion, determine its actual domain, and prove uniqueness or supply a counterexample. Do not generalize finite integer-lambda scans to arbitrary complex `lambda` without proof.

## 6. Twelve-dimensional boundary

A source experiment observed a normalized `d=12` prime residual compatible with the classical semicircle/Sato-Tate example arising from twelve squares. Candidate H8 is not a novelty claim:

- identify the exact modular/theta-form object involved;
- state the classical theorem that governs the residual distribution;
- determine whether any project-specific residual remains after classical equivalence is made explicit.

## 7. Required classification matrix

For H1-H8, report separately:

- exact identity status;
- hypotheses and small exceptions;
- shortest independent proof route;
- classical theorem or standard transform to which it is equivalent;
- genuinely project-specific content, if any;
- prohibited overclaim.

Allowed terminal labels are:

`EXACT_NEW_PRESENTATION_ONLY`,

`CLASSICALLY_EQUIVALENT`,

`STRICTLY_STRONGER_THAN_STATED_CLASSICAL_BASELINE`,

`REQUIRES_SCOPE_NARROWING`,

`REFUTED`,

or `OPEN_AFTER_AUDIT`.

## 8. Computation

Write an exact checker independently. It must compute `A_s`, `C_d`, `W`, `Q4`, and `Q8` from definitions; verify coefficient identities on declared finite ranges; test composites including prime powers and products of three primes; and include a deliberately incorrect coefficient vector as a negative control.

Computation is supporting evidence only. The prime-wall equivalences require proofs from exact divisor-sum identities.

## 9. Frozen provenance

Source checkpoint, withheld until independent proof freeze:

- Enterprise Math branch head `093733e443297e4276f426c591f7836d10698470`;
- GLOBAL_KNOWLEDGE event `43aa6322485ccbd9b85a17b6d3ee4963033cd18c`.
