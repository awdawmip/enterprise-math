# ABC capped-core energy: exact coefficient-2 obstruction

Status: `RESEARCHER_FROZEN_CANDIDATE / AWAITING_DRIVER_REVIEW`
Task: `RS-ABC-ENTERPRISE-CAPPED-CORE-ENERGY`
Researcher: `EM-ABC1-C0E119`
Date: 2026-08-27

## 1. Provenance boundary

The published task says that an exact parent decomposition in terms of `R,H,beta,I_cap` was frozen in conversation, but the canonical task sources do not durably contain the formulas defining that parent `I_cap`. Therefore this artifact does **not** silently identify the conversation-frozen `I_cap` with a guessed formula.

The arithmetic below has two layers:

1. an independently reconstructed standard abc log layer, explicitly defined here;
2. an exact no-go identity valid for any split `H=I+D` inside that reconstructed layer.

This arithmetic is a derived readout layer only. It does not promote logarithms, valuations, radicals, or diagonal quotients to native Enterprise point/address semantics.

## 2. Independent exact definitions

Let `a+b=c`, `gcd(a,b)=1`, with positive integers. Put

- `C = log c`;
- `e_p = v_p(abc)`;
- `R = sum_{e_p>0} log p = log rad(abc)`;
- `H = sum_p (e_p-1) log p = log(abc/rad(abc))`;
- `beta = log(c^2/(4ab)) >= 0`;
- `q = C/R`.

For the natural independently reconstructed cap-two core define

`I_2 = sum_p min(e_p-1,2) log p`

and the uncapped surplus

`D_2 = H-I_2 = sum_p max(e_p-3,0) log p`.

Then, exactly,

`R+H = log(abc)`

and

`3C = R + H + beta + log 4
    = R + I_2 + D_2 + beta + log 4`.

The second identity is immediate from

`log(abc) + log(c^2/(4ab)) + log 4 = log(c^3)`.

## 3. The raw coefficient-2 cap bound is true but tautological

For every prime `p`,

`min(e_p-1,2) <= 2`.

Summing with weight `log p` gives the universal theorem

`I_2 <= 2R`.

Equivalently, if

`rad = rad(abc)` and `cap2 = product p^{min(e_p-1,2)}`,

then

`cap2 <= rad^2`.

No use of `a+b=c` is needed after the exponents are known. Hence this theorem contains no additive abc mechanism and by itself cannot force `q<=1+epsilon`.

## 4. Exact deficit identity: where all nontrivial abc content must live

More generally, suppose only that the repeated-prime height has a split

`H = I + D`.

Substituting in the exact decomposition gives, for every real `epsilon`,

`q <= 1+epsilon`

if and only if

`2R - I >= D + beta + log 4 - 3 epsilon R`.       (DEFICIT)

Proof:

`q<=1+epsilon`
iff `C <= (1+epsilon)R`
iff `R+I+D+beta+log4 <= 3(1+epsilon)R`
iff `(DEFICIT)`.

Therefore a naked coefficient-2 ceiling `I<=2R` is structurally insufficient: the missing quantity is not another upper bound on `I`, but a **positive deficit** `2R-I` large enough to pay `D`, boundary imbalance, and the constant term (up to the allowed `3 epsilon R`).

Any proposed decisive inequality which is merely `(DEFICIT)` rewritten in new notation is algebraically equivalent to the desired abc quality bound and must be killed under the taskbook rule. A genuine Enterprise advance would have to derive the deficit from an independently available local/carry/native invariant, rather than assume it.

## 5. Exact counterexamples to the two obvious coefficient-2 strengthenings

### 5.1 Capped core asked to pay the boundary

A natural strengthening is

`I_2 + beta + log 4 <= 2R`.

Exponentiating removes floating point:

`cap2 * c^2 <= rad^2 * a*b`.

For the primitive triple

`1+8=9`, `abc=72=2^3*3^2`,

we have

- `rad=6`;
- `cap2=12`;
- `D_2=0`.

The claimed inequality becomes

`12*9^2 <= 6^2*1*8`,

i.e.

`972 <= 288`,

which is false.

This is especially sharp because the uncapped surplus is exactly zero: the failure cannot be blamed on a hidden `D_2` tail.

### 5.2 Replace the capped core by the full repeated-prime height

The stronger-looking universal claim

`H <= 2R`

is also false. For

`32+49=81`,

`abc=2^5*7^2*3^4`, so

- `rad=42`;
- `height=abc/rad=3024`;
- `cap2=252`;
- `surplus2=12`.

Thus

`3024 > 42^2 = 1764`.

Moreover

`beta = log(81^2/(4*32*49))`

is small (about `0.04505`), so this failure is not a large-boundary artifact. It isolates the high prime-power surplus as a genuinely distinct obstruction.

## 6. Bounded exact census

The checker `scripts/check_abc_enterprise_capped_core_energy.py` enumerates primitive unordered triples in increasing `c`, uses exact integer factorizations, and tests the exponentiated inequalities.

Run used for this return:

`python scripts/check_abc_enterprise_capped_core_energy.py --limit 5000`

Result:

- primitive unordered triples checked: `3,800,228`;
- raw `I_2<=2R` failures: `0` (also globally proved termwise above);
- first boundary-paid coefficient-2 failure: `1+8=9`;
- first full-height coefficient-2 failure: `32+49=81`;
- exact regression certificates: PASS.

The finite scan is evidence/regression only; no global statement is inferred from enumeration.

## 7. Comparison with abc and terminal disposition

The useful universal theorem `I_2<=2R` is strictly **weaker** than what is needed for abc because it ignores the required deficit payment. Conversely, making the coefficient-2 route exactly strong enough by imposing `(DEFICIT)` collapses algebraically to `q<=1+epsilon` itself.

So the coefficient-2 capped-core route, **without an independently derived deficit mechanism**, hits the taskbook kill condition.

Primary verdict: `EXACT_OBSTRUCTION`.

What survives:

1. cap-two gives a clean, exact, universal radical-budget ceiling;
2. the correct target variable is the deficit `2R-I`, not merely `I`;
3. boundary and uncapped prime-power surplus are independent payment terms;
4. an Enterprise-specific carry/local mechanism could still be valuable if it proves a deficit inequality without importing abc.

Smallest unresolved unit:

`CANONICAL_I_CAP_DEFINITION_AND_AN_INDEPENDENT_DEFICIT_GENERATOR`.

The first part is also a provenance issue: the conversation-frozen parent formula must be durably published before a theorem about *that exact canonical* `I_cap` can be certified.
