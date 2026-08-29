# Native Filament — Post-audit Hyperbola/Joukowski Independent Replication Return

Status: `FROZEN / INDEPENDENT / PASS_WITH_NARROWING`

Task-ID: `RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION`

Publication-ID: `TP2-7022EC048DC373BFA4CB`

Execution-record: `ER-6B4DCE596D23FB49EC67`

Claim-ID: `chatgpt-nfhjrep-20260829-0813`

Researcher-ID: `EM-NFHJREP-5C72A1`

Execution branch: `research/native-filament-postaudit-hj-rep-em-nfhjrep-5c72a1`

Execution branch base: `0f281e590e7e87d57f5947acb06dd647a9588a81`

Hard target:

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

Final hard-target verdict:

`ACHIEVED_WITH_NARROWING / H1_DISTINCT_TANGENT_OPEN_SUBTORSOR + H2_QUADRATIC_CHARACTER_DOMAIN + C2_NUMERIC_ONLY_COHERENCE`

## 1. Independence attestation

This return was reconstructed from the frozen statement-only packet

`audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825:research_inputs/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md#blob=6ce9ea10f02fded1959c55a1b78044ada434360f`

plus task/control-plane metadata needed to claim and freeze the execution. Before this return was frozen, I did **not** read PR #627, branch `research/native-filament-generalization-theorem-package-20260824`, prohibited source proof files, prohibited package-specific source checkers, or source-researcher proof opinions. The checker frozen with this return is a fresh standard-library script reconstructed only from the packet formulas and imports no theorem/checker code from the repository.

Independence status: `CLEAN_INDEPENDENT_CONTEXT`.

Source-exposure status at freeze: `BLIND_RAW_FROZEN`.

## 2. Verdict matrix

| Row | Verdict | Exact disposition |
|---|---|---|
| H1 | `VERIFIED_WITH_NARROWING` | H1a/H1b/H1c formulas are exact, but distinct same-family tangents parameterize only the off-diagonal part of the split hyperbola after translation quotient; the packet's unconditional full-torsor conclusion is too strong when the diagonal is nonempty. |
| H2 | `VERIFIED_WITH_NARROWING` | The orbit count and breaker bound are exact. For general odd finite fields `F_q`, replace Legendre-symbol notation by the quadratic character of `F_q`; the displayed Legendre formula is exact as written when `q` is an odd prime. |
| J1 | `VERIFIED_EXACT` | The Joukowski/Dickson involution, image-size formula, and saturation criterion follow exactly under `q` odd and `q∤2s`. |
| J2 | `VERIFIED_EXACT` | Independent second-moment reconstruction proves the lower extremal case forces `q|25` and the upper extremal case forces `q|7`; hence the only saturating cases are `(s,q)=(3,5)` and `(3,7)`. |
| C1 | `VERIFIED_EXACT` | Boundary alignment is exactly `q_b=s+2`; with the allowed premise `q_b<=5`, the unique nontrivial odd solution is `(3,5,9)`, giving `35`, `105`, and terminal odd factor `53`. |
| C2 | `VERIFIED_WITH_NARROWING` | The three `s=3` lane values and the integer equality `3M_9=105` are exact. The statement-only packet does not by itself prove a common causal/provenance mechanism behind the two occurrences of `105`; only exact numerical coherence is independently established here. |

## 3. H1 — split-hyperbola tangent/cover bridge

Work over a field `K` with `char(K) != 2`, with `B != 0` and `d_0 != d_1`. Put

`Q_i(x)=x^2/(2B)-d_i`,

`T_(i,u): y=-u x-Bu^2/2-d_i`,

`C_i=2(d_i-d_(1-i))`.

### H1a: concurrence identity

For `u != v`, the intersection of `T_(i,u)` and `T_(i,v)` is

`x=-B(u+v)/2`,

`y=Buv/2-d_i`.

Substituting this point into `T_(1-i,w)` gives

`B(w-u)(w-v)=2(d_i-d_(1-i))=C_i`.

Thus H1a is exact.

### H1b: common negative-dual values

The tangent intercept / negative Legendre-dual image at parameter `t` is

`D_i(t)=-Bt^2/2-d_i`.

Hence

`D_i(x)=D_(1-i)(y)`

if and only if

`B(y^2-x^2)=C_i`.

Thus H1b is exact.

### H1c: linear split-hyperbola isomorphism

Define

`Phi(x,y)=(a,b)=(y-x,y+x)`.

Then

`B ab=B(y^2-x^2)=C_i`.

Since `2` is invertible,

`Phi^{-1}(a,b)=((b-a)/2,(a+b)/2)`.

So the dual-overlap representation variety is exactly isomorphic to

`H_(B,C_i)={(a,b):Bab=C_i}`.

Thus H1c is exact.

### Required narrowing of the final bridge sentence

For a tangent-concurrence triple, set

`a=w-u`, `b=w-v`.

Then `Bab=C_i`, but the hypothesis `u != v` is exactly `a != b`. Simultaneous translation

`(u,v,w) -> (u+t,v+t,w+t)`

leaves `(a,b)` unchanged, and every `(a,b)` with `Bab=C_i` and `a != b` lifts to such a triple. Therefore the exact quotient statement is

`{distinct-tangent concurrence triples}/G_a  ~=  H_(B,C_i) \ Delta_(B,C_i)`,

where

`Delta_(B,C_i)={(a,a):Ba^2=C_i}`.

The full split hyperbola is recovered only when `Delta_(B,C_i)` is empty, equivalently when `C_i/B` has no square root in `K`, or if the distinctness restriction is removed in a separately defined degenerate extension.

Minimal finite-field witness: over `F_5`, `B=C=1`,

`H={(1,1),(2,3),(3,2),(4,4)}`.

The diagonal points `(1,1)` and `(4,4)` force `u=v`, so they cannot come from the stated distinct-tangent problem. This is the precise reason H1 is `VERIFIED_WITH_NARROWING` rather than exact at the final torsor sentence.

## 4. H2 — finite-field sign-orbit quotient and breaker bound

Let `K=F_q`, `q` odd, `BC != 0`, and

`R={(x,y):B(y^2-x^2)=C}`.

### H2a: point count

Under `Phi`, `R` is isomorphic to `Bab=C`. Since `a` can be chosen arbitrarily in `F_q^*` and then `b=C/(Ba)` is forced,

`|R|=q-1`.

### H2b: common values and sign orbits

A common negative-dual value fixes `x^2` and `y^2`. Conversely changing the signs of `x` and `y` does not change that value. Hence the fibers are exactly the `G={+/-1}^2` sign orbits, so the common-value set is naturally `R/G`.

### H2c: Burnside count

Let `eta` denote the quadratic character of `F_q`, extended by `eta(0)=0`. Burnside gives:

- identity fixed points: `q-1`;
- flip `x -> -x`: `x=0`, hence `By^2=C`, giving `1+eta(BC)` fixed points;
- flip `y -> -y`: `y=0`, hence `-Bx^2=C`, giving `1+eta(-BC)` fixed points;
- simultaneous sign flip fixes only `(0,0)`, which is not in `R` because `C != 0`.

Therefore

`|R/G|=[q+1+eta(BC)+eta(-BC)]/4`.

For odd prime `q`, `eta` is the Legendre symbol and this is exactly the packet's displayed formula. If `F_q` is intended to include odd prime powers, the packet should use the finite-field quadratic character rather than prime-only Legendre notation.

### H2d: capacity bound

If `R/G` has one element, all `q-1` points of `R` lie in one sign orbit. Every sign orbit has size at most `4`, so

`q-1<=4`, hence `q<=5`.

This is an orbit-capacity theorem only. It does not promote breaker-coprime capacity into an unrestricted prime-run theorem.

## 5. J1 — central-lane Joukowski map

For odd `s>=3`,

`Lambda_s(a)=-sa-1/(2a)`.

For nonzero `a,b`,

`Lambda_s(a)-Lambda_s(b)=(a-b)(-s+1/(2ab))`.

Thus, when `q` is odd and `q∤2s`, two arguments have the same image exactly when

`a=b`

or

`ab=(2s)^(-1)`.

Set `c=(2s)^(-1)`. The fibers are therefore the orbits of the involution

`tau(a)=c/a`.

Its fixed points satisfy `a^2=c`, so there are `1+eta(c)` fixed points. The number of involution orbits, hence the image size, is

`[(q-1)+(1+eta(c))]/2=[q+eta(c)]/2`.

This proves J1a and J1b exactly. The lane equation itself is equivalent to `j=Lambda_s(a)`, so complete central-packet saturation is exactly

`Im Lambda_s subseteq J_s (mod q)`,

with equality whenever the two finite sets have equal cardinality. J1c is exact.

Boundary guard: if `q|s`, the inverse `c=(2s)^(-1)` does not exist and J1b is outside its stated domain. The checker explicitly probes `(s,q)=(5,5)` and obtains image size `q-1`, demonstrating why silently extending the formula through `q|s` is invalid.

## 6. J2 — extremal saturation uniqueness

No source second-moment identity was used. The required obstruction is reconstructed directly from `Lambda_s`.

Let

`J_s={-r,...,r}`, where `r=(s-1)/2`.

### Lower extremal `q=2s-1`

Assume `q=2s-1` is prime. Since `s` is odd, `q≡1 (mod 4)`. Modulo `q`,

`s=1/2`,

so

`Lambda_s(a)=-(a+a^{-1})/2`.

The involution is `a -> a^{-1}`, with fixed points `a=+/-1`. J1 gives

`|Im Lambda_s|=(q+1)/2=s=|J_s|`.

Thus saturation forces equality `Im Lambda_s=J_s`.

Directly,

`sum_(a!=0) Lambda_s(a)^2=(q-1)/2`,

because `sum a^2=sum a^{-2}=0` in `F_q`. Every nonfixed image value has fiber size two, while the two fixed arguments map to `-1` and `+1`, so

`sum_(a!=0) Lambda_s(a)^2=2 sum_(t in Im Lambda_s) t^2-2`.

Under saturation this gives

`sum_(t in J_s)t^2=(q+3)/4=r+1`.

But

`sum_(t=-r)^r t^2=r(r+1)(2r+1)/3`.

Since `r+1 !=0 mod q`, cancellation yields

`r(2r+1)=3 (mod q)`.

Here `r=(q-1)/4=-1/4 (mod q)`, hence

`-1/8=3 (mod q)`,

so `25=0 (mod q)`. Since `q` is prime, `q=5`, and then `s=3`. Direct enumeration confirms `(3,5)` saturates.

### Upper extremal `q=2s+1`

Assume `q=2s+1` is prime. Then `q≡3 (mod 4)` and, modulo `q`,

`s=-1/2`,

so

`Lambda_s(a)=(a-a^{-1})/2`.

The involution is `a -> -a^{-1}`. Since `-1` is nonsquare, there are no fixed points. Thus

`|Im Lambda_s|=(q-1)/2=s=|J_s|`,

so saturation again forces `Im Lambda_s=J_s`.

Now

`sum_(a!=0) Lambda_s(a)^2=-(q-1)/2`.

Every image fiber has size two, hence

`sum_(t in J_s)t^2=-(q-1)/4`.

Here `q=4r+3`, so modulo `q`, `r=-3/4`. Therefore

`sum_(t in J_s)t^2=r(r+1)(2r+1)/3=1/32`,

while

`-(q-1)/4=1/4`.

Thus `1/32=1/4`, so `7=0 (mod q)`. Since `q` is prime, `q=7`, hence `s=3`. Direct enumeration confirms `(3,7)` saturates.

Therefore J2a and J2b are exact, and J2c follows: `s=3` is the unique nontrivial odd-sector parameter saturating both extremal boundaries.

## 7. C1 — longitudinal/transverse boundary closure

With

`k_*=2q_b-1`,

the two closure equations are

`2q_b-5=2s-1`,

`2q_b-3=2s+1`.

Each is equivalent to

`q_b=s+2`.

Thus C1a is exact.

Using the packet-authorized independently established bound `q_b<=5`, together with odd `s>=3` and odd `q_b`, the only nontrivial solution is

`(s,q_b,k_*)=(3,5,9)`.

Then

`M_9=(9-4)(9-2)=5*7=35`,

`s M_9=3*35=105`,

`s M_9+1=106=2*53`.

Hence the terminal odd prime factor is exactly `53`.

Type guard: the `9` here is **breaker-coprime capacity** `k_*`. This return makes no identification with the separate native typed-Cell prime-incidence cap `9`; equality of the numerals is not a type bridge.

## 8. C2 — C3 bouquet coherence

Specializing the lane polynomial

`P_(s,j)(m)=2s m^2+2jm+1`

to `s=3` and `j=-1,0,1` gives exactly

`6m^2-2m+1`,

`6m^2+1`,

`6m^2+2m+1`.

Thus C2a is exact within the frozen `s=3` lane/slot-unfolding statement universe.

From C1,

`3M_9=3*35=105`.

Therefore the packet's named native `105` bouquet gate and the longitudinal tangent extremum are the **same exact integer**. What does not follow from the statement-only packet is the stronger interpretive claim that their common value has thereby been proved to arise from one shared mechanism, or that it cannot be an independent numerical coincidence/fitted constant in the native construction. Independent evidence here supports the narrowed wording:

> In the `s=3` closure, the two independently named quantities coincide exactly at the integer `105`; this is an exact coherence constraint, not by itself a provenance theorem.

That is why C2 is `VERIFIED_WITH_NARROWING`.

## 9. Independent pressure-test log

Frozen checker:

`research_checks/NATIVE_FILAMENT_POSTAUDIT_HJ_INDEPENDENT_CHECK_20260829.py`

It is standalone Python using only the standard library and packet formulas.

Observed result:

`PASS independent blind checker`

- H1a exhaustive representative checks over `F_5,F_7,F_13`: `7,757,008` concurrence-equivalence checks.
- H1 split-hyperbola linear map/inverse checked exhaustively over representative nonzero `B,C` in the same fields.
- H1 distinctness failure witness over `F_5`: diagonal points exactly `[(1,1),(4,4)]` for `B=C=1`.
- H2 checked at `q=5,7,13,53`, including varied nonzero `B,C`; observed orbit classes agree exactly with Burnside:
  - `q=5`: character/orbit rows `(-1,-1,1)` and `(1,1,2)`;
  - `q=7`: `(-1,1,2)` and `(1,-1,2)`;
  - `q=13`: `(-1,-1,3)` and `(1,1,4)`;
  - `q=53`: `(-1,-1,13)` and `(1,1,14)`.
- J1 image-size and saturation equivalence checked for every odd `s<=15` and prime `q<=101` satisfying the formula's domain: `167` parameter pairs.
- J1 boundary witness `(s,q)=(5,5)` confirms the image-size formula must not be extended through `q|s`.
- J2 active search for every odd `s<=101` with prime `2s-1`: `21` lower-extremal cases; the only saturating case is `(3,5)`.
- J2 active search for every odd `s<=101` with prime `2s+1`: `23` upper-extremal cases; the only saturating case is `(3,7)`.
- C1 checked under odd `q_b<=5`, odd `s>=3`; unique closure is `(3,5,9)`.
- C2 lane identities checked for integer `m` across a representative signed range.
- `q=2` is explicitly outside H2/J1 odd-characteristic claims; `q|s` is outside J1b; nonprime extremal integers are outside J2's prime hypotheses; the H1 `u=v` slope collision is exactly the diagonal locus removed by the narrowing above.

Finite enumeration is used only as regression/pressure evidence. The universal conclusions H1–H2, J1–J2, C1–C2 above are supported by algebraic proofs.

## 10. Exact theorem wording after narrowing

The post-audit packet survives independent replication with the following exact statement boundary.

1. **H1.** H1a, H1b and H1c are valid over fields of characteristic not two. The dual-overlap variety is the full split hyperbola `H_(B,C_i)`. Distinct-tangent concurrence, modulo simultaneous translation of `(u,v,w)`, is `H_(B,C_i) \ Delta_(B,C_i)`, with `Delta={(a,a):Ba^2=C_i}`. It equals the full split hyperbola only when this diagonal is empty or when a separately stated degenerate `u=v` extension is admitted.
2. **H2.** For any odd finite field, `|R|=q-1`, common dual values are `R/G`, and `|R/G|=[q+1+eta(BC)+eta(-BC)]/4` for the finite-field quadratic character `eta`. For odd prime `q`, this is the packet's Legendre-symbol formula. If `|R/G|=1`, then `q<=5` by orbit capacity.
3. **J1.** For odd `q` with `q∤2s`, `Lambda_s(a)=-sa-(2a)^(-1)` is the quotient by `a -> (2s)^(-1)a^(-1)`, and its image has size `[q+eta((2s)^(-1))]/2`; central saturation is exactly image containment in `J_s mod q`.
4. **J2.** If `2s-1` is prime, lower-extremal saturation occurs only at `(s,q)=(3,5)`. If `2s+1` is prime, upper-extremal saturation occurs only at `(3,7)`. Hence `s=3` is the unique nontrivial odd sector count saturating both boundaries.
5. **C1.** Simultaneous longitudinal/transverse boundary alignment is equivalent to `q_b=s+2`. Under the allowed odd-breaker bound `q_b<=5`, the unique nontrivial odd solution is `(s,q_b,k_*)=(3,5,9)`, with `M_9=35`, `3M_9=105`, and `3M_9+1=106=2*53`. The capacity `9` remains typed separately from any native typed-Cell incidence cap also equal to `9`.
6. **C2.** The `s=3` lane values are exactly `6m^2-2m+1`, `6m^2+1`, `6m^2+2m+1`, and the named native bouquet gate `105` numerically coincides exactly with `3M_9=105`. This is an exact numerical/coherence constraint; a shared-origin or non-fitting provenance theorem requires separate evidence.

## 11. Failure modes and residues

No row is refuted. The only necessary corrections are statement-strength corrections:

- H1 must remove the diagonal split-hyperbola locus from the distinct-tangent quotient unless it is empty;
- H2 must use finite-field quadratic-character notation when `q` is an odd prime power rather than silently using a prime-only Legendre symbol;
- C2 must distinguish exact integer equality from an unproved common-provenance claim.

No unresolved mathematical decision remains at this task's statement-strength classification scope. Driver review should consume the exact J1/J2/C1 rows and the narrowed H1/H2/C2 wording; it should not promote or merge withheld source material automatically.

## 12. Final disposition

`PASS_WITH_NARROWING`.

The hard target is achieved: all six post-audit rows have been independently classified, universal proofs have been reconstructed, mandatory finite-field/boundary pressure tests pass, minimal statement-strength failures are isolated, and exact corrected theorem wording is frozen. This task now stops at task scope and returns to Driver/parent-objective reevaluation.
