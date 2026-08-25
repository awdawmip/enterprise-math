# Driver Review — QRF-R1 Independent Foundation Verification

Status: `DRIVER_ACCEPTED_DOWNGRADE / LITERAL_CANDIDATE_REFUTED / REPAIRED_EQUIVALENT_REFORMULATION / NOT_FOUNDATION_ADMITTED`

Date: `2026-08-25`

Driver-ID: `EM-DVR-R63A21 / CONTROL_PLANE`

Task:
`RS-QRF-R1-INDEPENDENT-FOUNDATION-VERIFICATION`

Taskbook source:
`41a1bbdf23831f9ad2af160df4a6bd5603f22547`

Owner branch/head:
`research/qrf-r1-independent-foundation-verification@f58db1dcfe4c709c864530bc66374d8cdb10ea12`

Researcher-ID:
`EM-QRF1-6457ED`

Primary report:
`research_outputs/QRF_R1_INDEPENDENT_FOUNDATION_VERIFICATION_20260822.md`

## 1. Driver verdict

The returned leading verdict

`DOWNGRADE_R1_EQUIVALENT_REFORMULATION`

is accepted.

The literal six-premise QRF-R1 package does **not** uniquely select exponent `p=2`.

The failure is exact and occurs at the refinement semantics, not at the monotone-multiplicative rigidity step.

## 2. Accepted rigidity theorem

For `S:N_{>0}->N_{>0}` strictly increasing and completely multiplicative,

`S(mn)=S(m)S(n)`,

the report correctly proves that

`S(n)=n^alpha`

with one common positive exponent `alpha`, and integer-valuedness on every positive integer forces `alpha=p` to be a positive integer.

The identity exclusion removes `p=1`, leaving `p>=2`.

The proof is theorem-level. The power-law step follows from monotonicity applied between powers of `2`; the integral-exponent step is valid by the forward-difference argument.

This part of QRF-R1 is accepted as classical rigidity structure, not Enterprise-specific novelty.

## 3. Decisive literal-premise countermodel

Let `R=R_S` be the max-safe coarse inverse. For a coarse fiber with

`k=R(N)`, `w_k=S(k+1)-S(k)`, `r=N-S(k)`,

define

`J_d(N)=d k + floor(d r/w_k)`.

Then

`J_1(N)=R(N)`

and the detail coordinate is

`j_d(N)=floor(d r/w_k)`.

At the information lower bound `d=w_k`, one has exactly

`j_{w_k}(N)=r`,

so the fiber is resolved bijectively.

This is a single coarse/refinement family in the literal sense of premise 4 and it does not presuppose a square or root formula.

Therefore every strictly increasing `S` admits such a capacity-tight fiber-rank refinement. In particular

`S(n)=n^3`

satisfies all six literal frozen premises while `p=3`.

Hence:

`QRF_R1_LITERAL_UNIQUENESS_OF_P2 = REFUTED`.

This directly triggers the taskbook downgrade condition.

## 4. Scale-equivariant repair

The report's natural repair is mathematically sound:

`T_d(N)=R_S(N S(d))`,

`D_d(N)=T_d(N)-dR_S(N)`.

After rigidity, for `S(n)=n^p`,

`T_d(N)=floor(d N^(1/p))`.

The first nontrivial max-safe fiber has size

`W=2^p-1`.

At `d=W`:

- `p=2` succeeds with detail labels `0,1,2`;
- `p=3` fails exactly because `D_7(4)=D_7(5)=4`;
- for every `p>=4`, `D_W(1)=0` while `D_W(2)>=2`, so label `1` is skipped and injectivity is impossible.

The Driver independently replayed the executable regression through `p=12`; only `p=2` is tight under the repaired scale-equivariant family.

Thus:

`SCALE_EQUIVARIANT_FIRST_FIBER_TIGHTNESS + SCALE_RIGIDITY => p=2`

is accepted.

## 5. Primitive-strength classification

The repair does not rescue QRF-R1 as a *strictly weaker* replacement for the quadratic law.

On the declared scale class, the repaired package is theorem-equivalent to

`S(n)=n^2`.

If max-safe orientation is counted inside the replacement primitive package, the package is stronger than the bare equation because the square law by itself does not select max-safe rather than another coarse-collapse orientation.

Therefore the correct decomposition is:

- `QRF-R1a`: scale-rigidity theorem — monotone complete multiplicativity + integer values gives `S(n)=n^p`;
- `QRF-R1b`: scale-equivariant first-fiber tightness characterization — among `p>=2`, selects `p=2`.

`QRF-R1b` may be retained as an explanatory structural characterization, but not as a strict foundational weakening.

## 6. Scope / Foundation boundary

Accepted:

`QRF_R1_LITERAL_PACKAGE = REFUTED_AS_UNIQUE_SELECTOR`

`QRF_R1_SCALE_RIGIDITY = VERIFIED`

`QRF_R1_SCALE_EQUIVARIANT_REPAIR = VERIFIED`

`QRF_R1_REPAIRED_STRENGTH = EQUIVALENT_REFORMULATION`

Not accepted:

- Foundation promotion of the literal R1 package;
- a claim that first-fiber information tightness alone selects quadratic scale;
- derivation of max-safe orientation from quadratic scale;
- novelty claims for monotone multiplicative rigidity.

## 7. Closure

`DRIVER_REVIEW = ACCEPT_DOWNGRADE`

`DOWNGRADE_R1_EQUIVALENT_REFORMULATION = ACCEPTED`

`FOUNDATION_ADMITTED = false`

`SUCCESSOR_AUTOMATICALLY_OPENED = false`

This closes independent verification of QRF-R1 at the task scope.