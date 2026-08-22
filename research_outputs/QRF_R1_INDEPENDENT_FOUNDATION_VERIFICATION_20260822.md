DOWNGRADE_R1_EQUIVALENT_REFORMULATION

# QRF-R1 Independent Foundation Verification — Scale Coherence and First-Fiber Tightness

Researcher-ID: `EM-QRF1-6457ED`  
Task: `RS-QRF-R1-INDEPENDENT-FOUNDATION-VERIFICATION`  
Taskbook source: `41a1bbdf23831f9ad2af160df4a6bd5603f22547`  
Frozen Enterprise source snapshot: `d16877c3b62a7d3b7568780c732f610c260c13c1`

## 1. Leading finding

QRF-R1 does **not** uniquely select `p=2` from the six frozen premises as literally stated.

The failure is not in monotone-multiplicative rigidity. That part is valid and can be proved directly from the stated hypotheses. The failure is that premise 4 — “a single root/refinement family used both for coarse collapse and for resolving the first nontrivial fiber” — does not specify how refinement is tied to multiplicative scale composition. Under its literal wording there is a non-circular fiber-rank refinement family that resolves the first fiber at the information lower bound for **every** `p>=2`, including `p=3`.

This triggers the taskbook kill/downgrade condition: an admissible `p>=3` model satisfies every frozen premise at the same lower bound.

There is a natural repair: require the refinement family to be the **scale-equivariant family**

`T_d(N) := R_S(N S(d))`.

With this exact narrowing, first-fiber tightness does uniquely select `p=2`. However, after unpacking the definitions, the repaired `S`-level package is equivalent to the square law on the declared class, not a strictly weaker law. If max-safe orientation is counted as part of the replacement package rather than as a separately retained readout convention, the full package is stronger than the bare square law.

Therefore the candidate is best retained only as an **equivalent structural reformulation / explanatory decomposition**, not as a strict foundational weakening.

## 2. A — rigidity chain audit

### 2.1 Exact theorem from the frozen scale premises

Assume only:

1. `S: N_{>0} -> N_{>0}`;
2. `S` is strictly increasing;
3. `S(mn)=S(m)S(n)` for all positive integers `m,n`.

Then there exists a positive integer `p` such that

`S(n)=n^p`

for every positive integer `n`.

The identity exclusion then removes `p=1`, leaving `p>=2`.

### 2.2 Direct proof of power-law rigidity

Complete multiplicativity gives

`S(1)=S(1)^2`.

Since values are positive, `S(1)=1`. Strict increase gives `S(2)>1`.

Set

`alpha := log S(2) / log 2 > 0`.

Fix `n>=2`. For every positive integer `q`, put

`a_q := floor(q log_2 n)`.

Then

`2^{a_q} <= n^q < 2^{a_q+1}`.

Monotonicity and complete multiplicativity imply

`S(2)^{a_q} <= S(n)^q < S(2)^{a_q+1}`.

Taking logarithms and dividing by `q log n` gives

`alpha * a_q/(q log_2 n) <= log S(n)/log n < alpha * (a_q+1)/(q log_2 n)`.

Both outer expressions converge to `alpha` as `q -> infinity`. Hence

`log S(n)/log n = alpha`,

so `S(n)=n^alpha` for every `n`.

Hypotheses actually used here:

- positivity, to take logarithms;
- order monotonicity;
- the power cases of complete multiplicativity, `S(x^q)=S(x)^q`.

Strictness is stronger than necessary for this step; nondecreasing plus nonconstancy would suffice to obtain a positive exponent.

### 2.3 Integer-valued powers force integral exponent

Now use the codomain `N_{>0}`. Suppose `alpha` is not an integer and let

`r := floor(alpha)+1`.

For `f(x)=x^alpha`, the `r`-th forward difference

`Delta^r f(n)`

is an integer for every positive integer `n`, because it is an integer linear combination of the integer values `(n+j)^alpha`.

The standard integral representation of a forward difference gives

`Delta^r f(n) = integral_[0,1]^r f^{(r)}(n+t_1+...+t_r) dt_1...dt_r`.

Because `r-1 < alpha < r`,

`f^{(r)}(x)=alpha(alpha-1)...(alpha-r+1)x^{alpha-r}`

is strictly positive and tends to `0`. Hence `Delta^r f(n)` is strictly positive and tends to `0`. For all sufficiently large `n` it lies strictly between `0` and `1`, contradicting integrality.

Therefore `alpha=p` is a positive integer.

### 2.4 Relation to prior art

This chain is classical rather than Enterprise-specific:

- Erdős' monotone multiplicative theorem is stronger than needed here: an increasing multiplicative arithmetic function already has power-law form. Everett Howe, “A New Proof of Erdős's Theorem on Monotone Multiplicative Functions,” *American Mathematical Monthly* 93 (1986), 593–595, DOI `10.1080/00029890.1986.11971896`, isolates the completely multiplicative power-law step used above.
- Putnam 1971 A6 asks precisely for the integrality conclusion: if `n^alpha` is an integer for every positive integer `n`, then `alpha` is a nonnegative integer. The forward-difference proof above is included so the verification does not depend on a hypothesis mismatch or on the Phase-B packet as proof authority.

No missing hypothesis was found in the rigidity chain.

## 3. B — literal first-fiber semantics admits a competing family

Let `R=R_S` be the frozen max-safe inverse:

`R(N)=max{k:S(k)<=N}`.

For any `N`, put

`k := R(N)`,
`w_k := S(k+1)-S(k)`,
`r := N-S(k)`.

Then `0<=r<w_k`.

For each refinement radix `d>=1`, define a single family

`J_d(N) := d k + floor(d r / w_k)`.

Its detail coordinate is

`j_d(N) := J_d(N)-dR(N) = floor(d r/w_k)`.

This definition uses only `S`, its max-safe coarse inverse, the current fiber width, and the rank inside that fiber. It does not mention `p`, roots, squares, or the target law.

It also satisfies the literal “same family” requirement:

`J_1(N)=R(N)`

for every `N`, so `d=1` is the coarse collapse and the same `J_d` family supplies all refinements.

On a fiber of cardinality `w_k`, the detail alphabet has at most `d` values. Therefore information capacity alone requires `d>=w_k` for lossless refinement. At the lower bound `d=w_k`,

`j_{w_k}(N)=r`,

so the fiber is resolved bijectively.

Thus **every** coarse fiber of **every** strictly increasing integer-valued `S` is capacity-tight under this family.

### 3.1 Explicit frozen-premise countermodel

Take

`S(n)=n^3`.

Then:

- `S` is strictly increasing;
- `S(mn)=S(m)S(n)`;
- `R_S` is max-safe;
- `J_d` is a single family with `J_1=R_S`;
- the first nontrivial fiber is `{1,...,7}`, of cardinality `W=7`;
- at radix `d=7`, `j_7(N)=N-1`, so refinement is lossless exactly at the information lower bound;
- the identity case is not involved.

Hence `p=3` satisfies all six frozen premises under a non-circular refinement semantics.

This is the decisive falsifier for the literal R1 uniqueness claim.

## 4. Minimal repair — scale-equivariant refinement

The natural intended strengthening is not merely “same family” but:

`T_d(N) := R_S(N S(d))`.

Define the detail

`D_d(N) := T_d(N)-d R_S(N)`.

This is non-circular: it is definable from `S`, `R_S`, and multiplicative scale composition before any exponent is selected.

If `k=R_S(N)`, then

`S(k)<=N<S(k+1)`.

Multiplying by `S(d)` and using complete multiplicativity gives

`S(kd)<=N S(d)<S((k+1)d)`.

Therefore

`kd <= T_d(N) <= (k+1)d-1`,

so

`D_d(N) in {0,...,d-1}`.

Thus radix `d` truly has information capacity `d` in this family.

After rigidity, `S(n)=n^p`, hence

`R_S(N)=floor(N^{1/p})`

and

`T_d(N)=floor(d N^{1/p})`.

The first nontrivial max-safe fiber is

`F_1={1,...,2^p-1}`,

with cardinality

`W=2^p-1`.

At the theoretical lower bound `d=W`, first-fiber tightness means that

`D_W(N)=floor(W N^{1/p})-W`

must be injective on `N=1,...,W`.

## 5. C — exact exclusion of competing exponents under the repaired family

### 5.1 `p=2` succeeds

For `p=2`, `W=3`.

`D_3(1)=0`.

For `N=2`,

`4 <= 3 sqrt(2) < 5`

because `16<=18<25`, so `D_3(2)=1`.

For `N=3`,

`5 <= 3 sqrt(3) < 6`

because `25<=27<36`, so `D_3(3)=2`.

Hence the first fiber is resolved bijectively at radix `3`.

### 5.2 `p=3` fails by an exact collision

Here `W=7`.

For `N=4` and `N=5`,

`11^3 < 7^3 N < 12^3`

because

`1331 < 1372 < 1728`

and

`1331 < 1715 < 1728`.

Therefore

`floor(7 * 4^{1/3}) = floor(7 * 5^{1/3}) = 11`,

so

`D_7(4)=D_7(5)=4`.

The lower-bound refinement is not injective.

### 5.3 Every `p>=4` fails

The first detail value is

`D_W(1)=0`.

For `N=2`,

`D_W(2)=floor(W(2^{1/p}-1))`.

For `p=4`,

`15(2^{1/4}-1)>2`

because `2^{1/4}>17/15`, equivalently

`2>(17/15)^4=83521/50625`.

For `p>=5`,

`2^{1/p}>1+1/(2p)`

since `(1+1/(2p))^p<e^{1/2}<2`. Hence

`W(2^{1/p}-1) > (2^p-1)/(2p) >= 31/10 > 2`.

Therefore `D_W(2)>=2` for every `p>=4`.

But `D_W` is nondecreasing and takes values only in `{0,...,W-1}`. Since it starts at `0` and the second value is already at least `2`, label `1` is absent. A map from `W` inputs into exactly `W` possible labels that misses a label cannot be injective.

Thus no `p>=4` is capacity-tight at the first fiber.

Combining the three cases:

> Under the additional scale-equivariant definition `T_d(N)=R_S(N S(d))`, `p=2` is the unique integral exponent `p>=2` whose first max-safe fiber resolves losslessly at radix `W=2^p-1`.

## 6. D — orientation is independent

The exponent result and the max-safe/downward orientation must not be merged.

The square law `S(n)=n^2` does not itself select the coarse inverse

`R_max(N)=max{k:k^2<=N}`.

For example, a nearest-square collapse

`R_near(N)=argmin_k |N-k^2|`

with a fixed tie rule is a coherent alternative and differs already at `N=3`:

`R_max(3)=1`, while `R_near(3)=2`.

Moreover, once any such coarse partition is fixed, the same fiber-rank construction of Section 3 gives a capacity-tight refinement of its fibers at their information lower bounds.

Therefore capacity tightness does not derive the max-safe orientation. Max-safe/downward choice is an additional semantic primitive or convention, exactly as the taskbook requires us to separate.

The repaired exponent theorem should be stated as conditional on the max-safe scale-equivariant family; it is not a derivation of that orientation.

## 7. E — primitive-strength audit

Three distinct strengths must be separated.

### 7.1 Literal frozen package

The literal package is **too weak** to determine `p=2`, because the non-circular rank-refinement family `J_d` makes every `p>=2` first-fiber tight.

### 7.2 Repaired `S`-level package

Add the exact scale-equivariant refinement law

`T_d(N)=R_S(N S(d))`.

Then, on the declared class of strictly increasing completely multiplicative integer-valued scales with the identity case excluded,

`[scale coherence + scale-equivariant first-fiber tightness]  <=>  S(n)=n^2`.

The forward implication is proved above. The reverse implication is the explicit `p=2` computation.

Therefore this repaired package is an **equivalent characterization** of the quadratic law on the admitted model class. It is not a strict logical weakening.

It can still carry independent *semantic* content: it decomposes the square law into scale composition plus an information-tight refinement condition. That may be explanatory or useful for refoundation, but it must not be labeled a strictly weaker theorem package.

### 7.3 Full package including max-safe orientation

If max-safe orientation is counted as part of the replacement primitive package, the full package is stronger than the bare equation `S(n)=n^2`, because the equation alone does not select max-safe rather than nearest-cell or another coarse-collapse orientation.

Thus the strongest justified classification is not `STRICT_REPLACEMENT`.

## 8. Weakest-hypothesis statement and negative boundary

A sound repaired theorem is:

> Let `S:N_{>0}->N_{>0}` be nondecreasing, nonconstant, and completely multiplicative. Let `R_S(N)=max{k:S(k)<=N}` and define the scale-equivariant refinement `T_d(N)=R_S(N S(d))`. If the identity exponent is excluded and the first nontrivial max-safe fiber is losslessly resolved by `D_d=T_d-dR_S` at radix equal to that fiber's cardinality, then `S(n)=n^2` for all `n`.

Within the present proof, strict monotonicity can be weakened to nondecreasing plus nonconstancy. The exact negative boundaries are:

1. **Remove or weaken monotonicity:** complete multiplicativity alone does not force a common power exponent across primes.
2. **Remove complete multiplicativity / scale composition:** the power-law rigidity and the scale-equivariant detail bound fail.
3. **Remove integer-valuedness:** the exponent need not be integral.
4. **Remove identity exclusion:** `p=1` remains admissible.
5. **Leave “same family” undefined:** the rank-refinement countermodel makes every `p>=2` tight.
6. **Remove first-fiber tightness:** every integral `p>=2` survives the scale-rigidity stage.
7. **Try to derive max-safe orientation from tightness:** alternative coarse orientations remain possible.

## 9. Final verdict and recommendation

`DOWNGRADE_R1_EQUIVALENT_REFORMULATION`

Do not promote the frozen QRF-R1 as a strict replacement foundation.

If the route is retained, split it into two explicitly typed objects:

1. **QRF-R1a — Scale-rigidity theorem:** monotone complete multiplicativity + integer-valuedness gives `S(n)=n^p`, `p in N`.
2. **QRF-R1b — Scale-equivariant tightness characterization:** with `T_d(N)=R_S(N S(d))`, first-fiber capacity saturation selects `p=2` among `p>=2`.

Label QRF-R1b as an **equivalent structural characterization / explanatory decomposition** of the square law, not a strictly weaker axiom package.

Keep max-safe orientation outside the exponent-selection claim as a separately declared semantic choice.
