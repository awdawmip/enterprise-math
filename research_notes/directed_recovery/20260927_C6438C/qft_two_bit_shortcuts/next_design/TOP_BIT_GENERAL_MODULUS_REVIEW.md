# Shared-context symbolic review: top selected bit, arbitrary modulus

Verdict: no substantive mathematical defect found in the stated scalar family.
This is a shared-context author-side review, not independent admission. The
review used source reading and symbolic algebra only: no scientific import,
numerical example, host reference calculation, native execution or new query.

The reviewed complete draft is `TOP_BIT_GENERAL_MODULUS.md`, SHA-256
`880fb9d90f9258e0b96f6f47281bd711b11bd2ec515bddb6a6212cf45266ee89`.
I also read the frozen `typed_floor_moments.py` implementation, SHA-256
`633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`,
and reused the already read stretch proof and highest-bit shortcut proof
identified in the draft. No source or previous artifact was changed.

## Algebra and endpoints

Substituting `t=d-Vz` into the low expression gives
`V(M-3z)+(3-2M+6z)(d-Vz)`, exactly the displayed `F_low`.
The high expression is `V(z-M)+(2M-1-2z)(d-Vz)`, exactly
`F_high`. Thus all five coefficients in each piece are correct.

For `d<L/2`, integral `z<M/2` ensures that both `z` and `z+1` use the
low piece, allowing its endpoint. For `L/2<=d<L`, both use the high
piece. At `d=L/2`, `t=0`; the formulas agree, and assigning that point
to the high segment is valid. At the last compressed position the shifted
value `B(M)=0` is an empty overlap, not an out-of-domain nonempty sum.
The construction covers `ell=0` and `g=2` without a separate formula.

Since `P=2V`, the adjacent quotients differ by `e` in `{0,1}` and
`z=2q+e`. Expanding with `e^2=e` yields precisely draft equation (3).
The three difference-power identities in (4) follow from
`Delta_1=e`, `Delta_2=2qe+e`, and `Delta_3=3q^2e+3qe+e`.
This eliminates products of independent floors; it does not assume alignment.

An implementation must combine the rational terms before requiring exact
division. In particular, `q^2e=(2Delta_3-3Delta_2+Delta_1)/6` is integral,
whereas `Delta_3/3` and `Delta_2/2` individually need not be integers.
The draft explicitly allows a common-denominator implementation.

## A simpler exact-division implementation consequence

Independently collecting the terms of draft (3)-(4), with its
`D=b0+b1*d` and `F0=a0+a1*d+2Dq+4cq^2`, gives the integer identity

```text
3 A(d) = 3 F0
       + (-6a0 - 6a1*d + 3D - c) Delta_1
       + (-6D + 6c) Delta_2
       - 8c Delta_3.
```

Indeed the coefficients of `Delta_1,Delta_2,Delta_3` before multiplying
by three are respectively `-2a0-2a1*d+D-c/3`, `-2D+2c`, and `-8c/3`.
This consequence leaves the frozen draft unchanged. Summing the displayed
integer numerator over a segment and calling one certified `exact_div(3)`
is a possible future implementation. It still requires all typed coefficient,
moment-combination and division receipts. It is not executed evidence.

## Calls, complexity and scope

The strict low interval ends at `L/2-1`; its canonical count in the draft is
correct. The high segment starts at `b+R*m` with its own local index and offset.
Zero-count segments are omitted. Each nonempty segment needs moments for
offsets `b_segment` and `b_segment+V`, all with total degree at most three:
the largest mixed term is a degree-one displacement factor times a
degree-two floor moment. Cubic floor differences have no displacement factor.
There are at most two segments per orientation and two orientations, hence
at most eight top-level table calls. This does not bound native work by eight.

At `r=0` the negative orientation starts at `R`, excluding a second copy of
zero displacement. Coincident half-modulus heads retain their multiplicity.
For `R>L`, an orientation may contain one term or be empty; no enumeration
of residues is needed. Exchanging pair order is valid for these scalar weights,
not an unproved matrix transpose shortcut. Raw normalization stays `4^-g`.

The polynomial-bit conclusion is sound in the explicit scale length
`O(g+log(R+1))`, not in `log(g)+log(R+1)` for a succinct exponent-only input.
The inspected fixed-degree routine makes a single recursive child at a node;
normalization and transposition follow Euclidean modulus reduction, with a
constant number of degree-three operations per node. Integer bit lengths
remain polynomial in these explicit parameter lengths. This supports the
symbolic composition claim, while actual recursion, arithmetic, setup,
storage and replay costs remain to be measured in a new implementation.

No new arbitrary-modulus result has been executed here. The existing aligned
successor retains its original admission domain. This proof supplies neither
an order/address oracle, general non-top two-bit evaluation, growing-mask
compression, arbitrary chronological matrix products nor a Shor sampler.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1
