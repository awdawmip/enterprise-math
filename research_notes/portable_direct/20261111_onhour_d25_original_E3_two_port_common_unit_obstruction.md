# D25/LIFT — original E3 fixed-z two-port common-unit obstruction and constructive shear repair

Date: 2026-11-11 Asia/Hong_Kong. Classification: **AUTHOR_SIDE / EXACT_ALGEBRAIC_CRITERION / 8_EXECUTED_FINITE_CASES / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Declared Research-onhour logical lane: `chatgpt-research-onhour-enterprise-math-20260923`. Maintenance `chatgpt-hourly-enterprise-math-20260921` is separate.

## Original sources and the precise new question

Consume without recrediting the already proved and published original E3 first-digit and second-digit raw-port results at `research_notes/portable_direct/20261111_onhour_d25_original_E3_formal_derivative_second_digit_port.md` and its two independent E3 coefficient constructors `d25_e3_original_formal_derivative_second_digit_20261111.py`. This unit asks a concrete **normalization falsification question** prompted by those data: can *one and the same coefficient-ring unit*, acting by multiplication and with no mixing between observer ports, align BOTH the original fixed-z Hasse coefficient and original signed `1+6 ∂lambda` derivative port to the frozen original scalar observations modulo p²?

For any p ≡ 13 or 19 mod 24, p>3, let `R_2=(Z/p²Z)[T]/(T²-2)`, `T²=2`, `σ(T)=-T`. Original curve `E3(t): y²+xy+(t/27)y=x³`, `t=(2-T)/4`, original local parameter `z=-x/y`. Put

- `H=H_{3,p-1}(t)` = coefficient of `z^{p-1} dz` in its normalized invariant differential with **fixed z**;
- `W_E=H+6∂lambda H` with `dt/dlambda=T/4`;
- `g=Σ_{k=0}^{p-1}B_k`, `h=Σ_{k=0}^{p-1}(12k+1)B_k`, `B_{k+1}/B_k=(6k+1)(3k+1)/(36(k+1)²)`, the original frozen scalar ports in Z/p²Z.

Previously proved source bridge and accepted CM0/UR give `H≡g≡0 (mod p)`, `W_E≡h (mod p)`, and `h mod p` is a unit. Reuse these as **stated hypotheses** for the following algebraic criterion; numerical checks independently confirm them for the eight specified primes.

## New exact criterion: a common multiplicative unit fails iff the first second-digit correction survives

**Proposition (two-port common-unit criterion).** Let R be any commutative ring with `p²=0`, `p` a principal nilpotent ideal, and values `H,g∈pR`, `W,h∈R^×` satisfying `W≡h (mod pR)`. There exists `u∈R^×` satisfying simultaneously

```text
u*H = g,         u*W = h
```

if and only if `H=g` in R. Moreover `u=h*W^{-1}` is unique, and `u≡1 (mod pR)`.

*Proof.* The second equality, because W is a unit, forces the unique candidate u; W≡h implies u≡1. Since H∈pR and p²=0, (u-1)H=0, so uH=H, proving necessity. Conversely if H=g, this u satisfies both equalities. QED.

In our specific `R_2` the necessary and sufficient **second-digit witness** is the typed quadratic coordinate

```text
D_p := (H-g)/p ∈ R_2/pR_2 ≃ F_p[T]/(T²-2).
```

Its two coefficients are part of the original measured residual and cannot be erased by a common near-identity scalar rescaling. The expression (H-g)/p means the coefficient tuple divided by p after verifying divisibility, so no forbidden inverse of p is used.

**Constructive exact repair within a declared two-port interface class.** In the family of equal-diagonal upper-triangular observer maps `A=[[u,c],[0,u]]` with `u≡1,c≡0 (mod p)`, the unique transformation satisfying `A·(H,W_E)^t=(g,h)^t` is

```text
u = h/W_E;
c = (g-u H)/W_E = -(H-g)/W_E             (mod p²);
c/p ≡ -D_p/(h mod p)                      (mod p).
```

It is exact since `W_E` is a unit; all denominators are units. The nonzero off-diagonal shear carries precisely the correction that a common scalar misses. This is an *observer-interface algebraic repair*, **not** a claim to have constructed native crystalline Frobenius, a Gauss–Manin isomorphism or the unknown H0/B0 normalization eta.

## Reproducible original p=373 certificate

At `p=373`, `p²=139129`, `R_2=(Z/139129)[T]/(T²-2)`, independent original E3 differential/binomial series already provide the raw curve. A fresh exact integer run of the original binomial E3 formula and the independently defined frozen B_k recurrence gives:

```text
H                = 130177 + 17904 T       (mod 139129)
g                = 8952
W_E              = 97151  + 8952 T        (mod 139129)
h                = 62835
W_E - h          = 373(92+24 T)
H - g            = 373(325+48 T)
h mod 373        = 171
u = h/W_E        = 11191+63410 T = 1+373(30+170 T)
u H - g          = 373(325+48 T)          != 0
c = (g-uH)/W_E   = 12309+126820 T = 373(33+340 T)
u W_E            = h
u H + c W_E      = g                       (mod 139129)
```

Thus the previously measured `325+48T` is now an **exact obstruction certificate to a specific proposed normalization class**, with an explicit smallest-form corrective shear in the declared equal-diagonal triangular family. Its nonzero odd component `48T` stays visible, retaining signed source. The independent older `92+24T` weighted difference determines u, but *cannot simultaneously* correct the unweighted H under a sole multiplicative unit.

## Eight original-class finite exact checks

The new verifier `research_notes/portable_direct/d25_original_e3_two_port_normalization_20261111.py` actually executed Python integer modular arithmetic for eight fixed target primes, reconstructing original E3 binomial coefficients and the separate source B_k recurrence, with exact unit inversion, rejection of the common scalar, and constructive repair checks:

| p | `D_p=(H-g)/p` | `c/p` for the unique triangular repair |
|---:|:---:|:---:|
| 13 | (4,9) | (8,5) |
| 19 | (3,16) | (14,5) |
| 37 | (28,9) | (22,15) |
| 43 | (24,19) | (30,13) |
| 109 | (62,47) | (69,40) |
| 139 | (114,25) | (104,35) |
| 157 | (51,106) | (123,34) |
| 373 | **(325,48)** | **(33,340)** |

Every `D_p` is nonzero. The script verifies `uW_E=h`, `uH+cW_E=g` for each listed case, and explicitly rejects the false condition `uH=g`. The previous independent original formal group recurrence versus E3 binomial coefficient calculation remains reusable cross-source verification; this run executes the binomial branch and original scalar recurrence rather than counting the historical formal recurrence as a newly executed separate test.

**Scope:** the criterion is a theorem under its ring/first-digit hypotheses; the failure of a common scalar is certified for the eight explicit primes, with a p373 hard negative control. No all-prime vanishing/nonvanishing claim for D_p is inferred.

## Direct impact on the still-unexecuted native benchmark

Support Issue `#1559` is for the true **same-original-class** divided-power H0/B0 `[X]U mod139129` native operation, actual module rank, semilinear Frobenius direction, eta and basis, full odd Green/Hesse κ, frozen scalar Delta-R and independent replication. This unit supplies one direct check at the **source-to-observer comparison map**: a proposed single common scalar rescaling of the two raw E3 fixed-z ports is refuted already at p373; a successful source-preserving comparison must give the additional correction law (which can be a connection, a more general matrix or another explicitly justified operation).

No native H0/B0 evaluator was run, no current claim/open exists in the Research-onhour lane, and this local algebraic A is **not** a substitute native operator. Reuse the accepted CM0/UR, prior source-port alignment, eight E3 Hasse/derivative measurements, p373 exact Delta=R=196, and signed κ without recrediting. The native ticket remains PENDING_OWNER pending a lawful executor.

## Recovery / Source

Fresh request `onhour11-20261111-1314-exact-cont` and task `onhour11-20261111-1314-exact-task` received native control read receipts `SUCCEEDED`, source snapshot `e9bac965ff0ff7d6e550e5595eee90370cd34d2e`; canonical route still `PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER` and `execution_authorized=false`. Existing Researcher registration `onhour11-20261111-1000-onhour-researcher-start` = SUCCEEDED (Researcher `EM-ENTERPRISE-CF1028`, session `MCP-7af27f545c01441eaf19206f89c6832b`, RA `RA-47ADB5B97D6D92FC28504B60`). Current own `em_site_control/recovery_status` returns `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; private custody status (including original registration request) returns `PRIVATE_CUSTODY_NOT_FOUND`. Those are specific capability boundaries, not a new CLAIM, Source checkpoint, Result or global host impossibility.

Next exact scientific action: a certified native H0/B0 executor applies the frozen same-original-class divided-power evaluator and produces `[X]U`, rank/direction/eta, odd κ and Delta-R with independently verified original input. Next comparison: test the real native-to-source mapping, including the necessary non-scalar two-port correction found here if applicable. The total LIFT/JT2 parent remains OPEN, with no new universal proof or counterexample.
