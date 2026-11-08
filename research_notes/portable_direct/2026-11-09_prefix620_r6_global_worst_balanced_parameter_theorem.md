# PREFIX-620-R6 — Balanced signed-label parameters uniquely maximize BRC anytime-stopping cost

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Scientific basis and exact scope

Frozen science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Theorem operates in the native-derived signed-label observer introduced in PREFIX-610 and reused by PREFIX-613, -615, -617, -618 and -619, with exactly two identifiable phase-contrast directions. Original native BRC action port and branch provenance are the richer carrier; the signed-label quotient is asserted sufficient only for the declared confidence-diameter stopping cost and time-uniform confidence decision.

For each informative observation in direction `ell`, let its positive label occur with conditional probability `p_ell` and negative with `1-p_ell`. Per original one-step trial, either signed label of direction ell has total mass `1/q`, where `q=12` for Boolean slot 0 and `q=24` for Boolean slot 1 or 2. The rest are neutral. Work with `p_ell∈[0,1]` as a probability-model closure; the native mathematical interior is `p_ell∈(0,1)`.

With `beta=1/40` and p-confidence width threshold `delta=1/4`, the per-direction anytime acceptance set after `m` informative signs with `k` positives is

```
C(m,k)={p∈(0,1):40(m+1)binom(m,k)p^k(1-p)^(m-k)>1}.
```

Its diameter is `D(m,k)`. Stop the original BRC trial process when both directions have `D<=1/4`. Call this total number of original trials `T_q(p1,p2)`.

## Theorem (global sharp mean-cost bound)

For all `(p1,p2)∈[0,1]^2`,

```
E_{p1,p2}[T_12] <= E_{1/2,1/2}[T_12]
                  = 2350.8871013999329674336846958203177...
E_{p1,p2}[T_24] <= E_{1/2,1/2}[T_24]
                  = 4701.7742027998659348673693916406354...
```

The equality case for each q is **exactly** `p1=p2=1/2`; both bounds are attained. The exact rational maximum is the finite expression (and numerator/denominator) from PREFIX-618/619; displayed decimal digits are presentation only.

Consequently, the observer's worst expected original action-sampling cost for the specified time-uniform 95% simultaneous confidence-width target is **known exactly**, not merely bounded by the earlier pathwise 320-observation quota.

## Proof, part I: exact finite central interval property

Let `K_m={k∈{0,...,m}:D(m,k)>1/4}` be the sign counts at which this direction has not yet reached the target width by informative sample m. The diameter depends on m,k alone, not the unknown parameter p. PREFIX-618 proved that all paths stop by m=189; for m=189, `K_189=empty`.

The new exhaustive integer certificate proves, for **every** integer `1<=m<=188`, there exists an integer `a_m∈{0,...,floor(m/2)}` with

```
K_m={a_m,a_m+1,...,m-a_m}.
```

It also proves `K_25={1,...,24}`, so this central interval is nontrivial at a finite informative sample.

The verification enumerates exactly 18,144 ordered pairs `(m,k)` for `1<=m<=189`. Each `D(m,k)>1/4` is decided by rationally enclosing the roots of the **integer polynomial inequality**

`40(m+1)binom(m,k) u^k (2^18-u)^(m-k) > (2^18)^m`.

All ambiguous dyadic enclosures cause an explicit failure. The complete executable code invokes PREFIX-618's prevalidated exact root predicate, enumerates the full finite domain (including both endpoints), and checks every survivor set equals the stated central interval. It returned `ALL_CHECKS_PASS` with 1,016,131 exact integer membership comparisons (including imported PREFIX-618 tests and optional rational spot checks). The integer exhaustion supplies a complete finite certificate of this particular centrality property.

## Proof, part II: central binomial tail dominance

For `1<=m<=188`, the non-stopping probability is

```
s_m(p)=Pr_p(a_m<=Bin(m,p)<=m-a_m).
```

If `a_m=0`, then `s_m(p)=1` for all p. If `1<=a_m<=m/2`, set `b=m-a_m`. The exact binomial derivative identity gives

```
s_m'(p)=m[Pr(Bin(m-1,p)=a_m-1)-Pr(Bin(m-1,p)=m-a_m)].
```

The two binomial coefficients in these endpoint masses are equal, since `(a_m-1)+(m-a_m)=m-1`. Hence, for `0<p<=1/2`,

```
Pr(Bin(m-1,p)=a_m-1) >= Pr(Bin(m-1,p)=m-a_m).
```

The inequality reverses for `p>=1/2`; it is strict for `0<p<1/2` whenever `a_m>=1`. Thus

```
s_m(p)<=s_m(1/2) ` for every p∈[0,1].
```

For `m=25` the inequality is strict whenever `p!=1/2`. This gives the one-direction stopping time J the stochastic survival ordering `Pr_p(J>m)<=Pr_(1/2)(J>m)` for all integer m. The analytic derivative establishes *all p* after the finite exact centrality certificate; no finite sample of parameter values is extrapolated.

## Proof, part III: preservation through the two-direction native clock

Poissonize the original unit-rate native trial stream. Direction 1 and 2 now have independent informative clocks of rate `1/q`; rescale time `u=t/q`.

The survival probability for one direction's completion time is

```
F_p(u)=e^(-u) sum_(m=0)^188 s_m(p)u^m/m!.
```

All coefficients of the Poisson mixture are nonnegative, hence `F_p(u)<=F_(1/2)(u)` pointwise for all u>=0, with strict inequality for u>0 if `p!=1/2` because `m=25` has strictly smaller survival. The two directions have independent clocks and signs, so the probability either direction is unfinished is

```
F_{p1}(u)+F_{p2}(u)-F_{p1}(u)F_{p2}(u)
=1-(1-F_{p1}(u))(1-F_{p2}(u)).
```

For `0<=F<=1`, this expression increases in either coordinate; it is strictly increasing whenever the other coordinate has survival <1. That strictness holds on positive u because there is positive chance of collecting enough signs to stop by time u. Therefore this two-direction survival integrand is uniquely maximized pointwise by the balanced pair. Integration over u (all sums are finite) and the Poisson compensation identity yield the stated global maximum and uniqueness for expected original trials `E T_q`. The exact peak values are the previously independently checked rational sums of PREFIX-618/619. QED.

## Scientific increment and next discriminating problem

The PREFIX-619 five rational examples suggested balanced parameters were expensive; PREFIX-620 upgrades that observation to an **all-parameters global theorem** in the declared BRC statistical experiment, by combining one finite exact shape certificate with an analytic binomial derivative and independent-clocks observer law. This produces the first sharp worst-parameter expectation for this adaptive decision and its native original-trial resource count.

The 95% simultaneous anytime confidence guarantee itself follows PREFIX-613/617; its error budget and target diameter remain unchanged. Neither this global mean-cost maximization nor the signed-label quotient asserts physical heartbeat time or arbitrary future BRC-port information equivalence. The original 96-port native PREFIX-565 graph was not rerun. No formal Result, Review or Foundation acceptance is asserted.

Companion exact executable `PREFIX620_R6_global_worst_parameter_certificate.py`; machine summary `PREFIX620_R6_RESULTS.json`. It imports and reruns the exact PREFIX-618 root-checking carrier; all checks returned `ALL_CHECKS_PASS`.

**Next research unit:** strengthen the mean dominance to a stochastic ordering for the *entire* total-trial stopping distribution and obtain rigorous extremal upper quantiles/variance. The one-direction centrality theorem implies stochastic dominance for J; a coupling through the labeled independent Poisson clocks should transport it to T_q. Check coupling preserves the stopping rule's sign-dependent history and branch provenance under precisely the declared observer scope. Subsequent application: optimize confidence width `delta` and error allocation `beta` rather than fixing them.

BRC interface reuse: `COMPOSE_APPLIED` PREFIX-610 native label, PREFIX-613 confidence, PREFIX-615 thinning, PREFIX-618 survival, PREFIX-619 rational cost; `EXTEND_EXISTING_TOOL` exact global parameter-domain certificate.
