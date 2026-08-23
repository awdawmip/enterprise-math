# Targeted packet — pure valley state, full-band sieve, and factoring benchmark

Status: `FROZEN_TARGETED_VERIFICATION_INPUT`

Date: `2026-08-23`

Packet-ID: `VALLEY_BAND_PURE_STATE_AND_BENCHMARK_PACKET_20260823`

## 1. Evidence boundary

This packet exposes candidate recurrences and empirical checkpoints but withholds all source prototypes. The receiving researchers must write their own implementation and proofs.

Do not use code copied from the source conversation, cached runtime, unpublished prototype, or later reconstruction. A mathematically equivalent implementation must be independently authored.

The closed state recurrence may be classical. The task is not allowed to turn a reformulation into a complexity or novelty claim.

## 2. Candidate pure valley state

Let the factoring target be an odd nonsquare `N`, let `M` be a small positive multiplier, and put

`T=M*N`.

Consider integer states `(A,B,C)` satisfying

`C^2-A*B=T`.

On a candidate reduced orbit assume

`A*B<0`,

`|C|<sqrt(T)`,

and `A!=0`.

Define

`a=(isqrt(T)+|C|)//|A|`,

then update

`A_next=A*a^2+2*C*a+B`,

`B_next=A`,

`C_next=A*a+C`.

The receiving researcher must determine the correct sign/orientation conventions, admissible initialization, reduction hypotheses, zero/terminal states, and whether an absolute value on `C` is valid on every chosen orbit.

Candidate claim V1 is that, under a correct convention, this closed state reproduces the relevant continued-fraction/CFRAC partial quotients without retaining the usual continued-fraction `m,d` state or growing convergent numerators and denominators.

## 3. Candidate valley band

For a state `(A,B,C)`, define

`D(t)=A*t^2+2*C*t+B`.

Its discriminant is formally

`(2*C)^2-4*A*B=4*T`.

Candidate claim V2 is that, for a factor-base prime outside explicitly classified ramified or coefficient-degenerate cases, the congruence

`D(t)=0 mod p`

lies in at most two residue classes modulo `p`. Those roots can be used to sieve an entire integer band in `t` rather than evaluating every point separately.

The researcher must prove the exact relation between a smooth value of `D(t)`, the corresponding modular square relation modulo `N`, and the exponent vector used in the final linear algebra. Sign, multiplier, and square-factor bookkeeping must be explicit.

## 4. Candidate multiplier selection

A source prototype used a two-stage multiplier heuristic:

1. rank small squarefree multipliers by small-prime quadratic-residue/factor-base compatibility;
2. run short independent pilots and choose by normalized relation growth per unit cost.

Classify whether square multiples belong to the same effective quadratic-character class and whether the pilot score predicts final relation yield on held-out instances.

This is an empirical heuristic, not a theorem supplied by the packet.

## 5. Candidate band-opening policy

Opening a band has a fixed setup cost because factor-base roots and sieve updates must be prepared. The source checkpoint suggested that opening every moderate band is inferior to opening only unusually deep bands, with a fixed threshold near `a>=256` performing well on one implementation.

The benchmark must compare at least:

- point-only orbit collection;
- fixed thresholds `32,64,128,256,512`;
- one adaptive policy derived from an explicit expected-yield versus setup-cost model.

No threshold is privileged in advance. The claim survives only if it holds on a fixed, non-cherry-picked corpus and after implementation overhead is reported separately.

## 6. Frozen validation instances

The factors are disclosed solely for correctness checking and must not be used by the factoring procedure.

### 104-bit checkpoint

`N=11681976071094177586960974447503`

`N=2863308968584027 * 4079886662343389`.

### 112-bit checkpoint

`N=3023488086125431650366346299720263`

`N=53570471665823809 * 56439452409270407`.

### 128-bit checkpoint

`N=236865402759503171708411529790601388017`

`N=14465361523279898393 * 16374661800073417369`.

The source checkpoint reported success on these instances, but the reported wall times are not acceptance thresholds and must not be reproduced as if hardware-independent.

## 7. Required random corpus

Use a frozen deterministic generator for balanced semiprimes. Record the seed and the exact prime-generation rule before running the algorithms.

Minimum corpus:

- twenty 80-bit semiprimes for state/continued-fraction step equivalence;
- ten 96-bit semiprimes for complete benchmark comparison;
- five 104-bit semiprimes;
- three 112-bit semiprimes;
- the fixed 128-bit checkpoint above.

A 136-bit extension is optional and may not replace failures or missing data at lower sizes.

## 8. Required metrics

For each implementation and instance record:

- multiplier and factor-base bound;
- orbit steps;
- bands considered and bands opened;
- total band width;
- root-setup time;
- sieve time;
- candidate trial-division time;
- full relations;
- single-large-prime partial relations;
- optional double-large-prime edges and completed cycles;
- independent exponent-matrix rank;
- dependencies tested;
- factor success/failure;
- total wall time and peak memory;
- deterministic output digest.

Separate algorithmic work from language/runtime overhead wherever feasible.

## 9. Required baselines and ablations

At minimum compare:

1. a standard continued-fraction/CFRAC state implementation authored by the researcher;
2. the closed `(A,B,C)` point-only implementation;
3. the closed-state full-band variants;
4. `M=1` versus the frozen multiplier-selection procedure;
5. single-large-prime versus no-large-prime handling.

Double-large-prime handling is secondary. It may be added only after the core matrix is complete, and a slower null result must be preserved.

Mandatory negative controls:

- perturb one recurrence sign and show invariant failure;
- use an invalid band root and show relation verification rejects it;
- choose thresholds on the test corpus after viewing results and label that run invalid;
- compare relation counts without rank and show why raw counts can mislead.

## 10. Prior-art and claim boundary

The formal audit must compare the closed recurrence with real indefinite binary quadratic-form reduction, continued fractions, CFRAC, and related semiconvergent/intermediate-convergent sieving methods.

Allowed conclusions include exact equivalence, implementation-level simplification, a reproducible relation-yield improvement, a null result, or a narrowed heuristic. Do not claim subexponential improvement, superiority to modern QS/NFS, or historical novelty without separate proof and evidence.

## 11. Source provenance

Withheld source checkpoint:

- GLOBAL_KNOWLEDGE commit `96f685436622d8ce665f3f5acfcb715da8ab5d92`;
- earlier valley-band checkpoint `bac5386090f4be3123aaf7e4d26a6a49711c3669`.
