# D25 / SECOND-DIGIT-LIFT — exact original E3↔E4 CM-fibre quadratic twist, residue-class Frobenius sign gate

**Date:** 2026-10-27. **Lane:** TASK_RESEARCH, `chatgpt-research-onhour-enterprise-math-20260923` only. **Mother:** ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. **Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific Source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

**Status:** AUTHOR-SIDE / EXACT ALGEBRAIC THEOREM AND TWIST-CHARACTER BRANCH PROVED / EXECUTED ORIGINAL-CURVE FINITE POINT-COUNT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0 / NOT_SOURCE_CHECKPOINT / NOT_RESULT / REGISTER_PENDING / SYNC_DEBT. No all-prime LIFT, native Frobenius coefficient, Source CLAIM/open, or review is asserted.

## 1. Actual original models: source and weighted observers

The published Chisholm–Deines–Long–Nebe–Swisher (2013), *p-Adic Analogues of Ramanujan Type Formulas for 1/π*, Section 2, defines **both actual families**, not arbitrary short Weierstrass replacements:
[original paper, page 3](https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf).

For `s²=2` over `K=Q(s)`, use the common chosen branch `s=+sqrt(2)` at the real embedding and preserve its conjugate `sigma(s)=-s`:

```text
t3=(2-s)/4;    c3=t3/27;      4*t3*(1-t3)=1/2.
E3(t3): y3²+x3*y3+c3*y3=x3³.

t4=(3-2*s)/6;                 4*t4*(1-t4)=1/9.
E4(t4): y4²=x4*(x4²+x4+t4/4).
```

The previously recorded **weighted truncations** are, exactly,

```text
W_p = sum(k=0..p-1) (6k+1) (2k)!(3k)!/((k!)^5 216^k)
S_p = sum(k=0..p-1) (8k+1) (4k)!/((k!)^4 2304^k).
```

They arise from the respective Clausen-weighted `d=3, λ3=1/2` and `d=4, λ4=1/9` hypergeometric families. This does **not** declare the hypergeometric weighted sums equal to the raw elliptic point-count traces or to the H0/B0 operator. The published Guo–Zudilin theorem establishes `S_p ≡ p*(-3/p) (mod p³)`; the full `W_p-S_p` bridge remains unproved for all target primes.

## 2. Exact theorem: same j but a nontrivial, explicitly identified quadratic twist

Complete the square and translate the **published original** curves to their short Weierstrass forms:

```text
X3=x3+1/12,  Y3=y3+(x3+c3)/2,
  Y3²=X3³+A3 X3+B3,
  A3=-(5+2s)/432,           B3=(12+7s)/23328.

X4=x4+1/3,   Y4=y4,
  Y4²=X4³+A4 X4+B4,
  A4=-(5+2s)/24,            B4=(7+6s)/216.
```

Put `d=s/6`. Direct exact arithmetic in `Q[s]/(s²-2)` proves

```text
d²=1/18;            d³=s/108;
A3=d² A4;           B3=d³ B4;
N_{K/Q}(d)=-1/18.
```

Consequently their `j` invariants are **identical**. Over `L=K(r)`, with `r²=d`, the explicit isomorphism `E4→E3` is

```text
X3=d*X4;   Y3=d*r*Y4;
x3=d*(x4+1/3)-1/12;
y3=d*r*y4-(x3+c3)/2.
```

The original invariant differentials `ω3=dx3/(2y3+x3+c3)=dX3/(2Y3)` and `ω4=dx4/(2y4)=dX4/(2Y4)` satisfy `φ*(ω3)=r^(-1)ω4`. This `r` must be retained for any period/Gauss–Manin normalization comparison.

Importantly **the two original models are not K-isomorphic**: if `d=e²` for `e∈K`, then `N(d)=N(e)²≥0` in `Q`, contradicting `N(d)=-1/18`. Their common `j` therefore does *not* license an unlabelled same-basis equality of periods, Frobenius matrices, or p-adic companions. The nonzero discriminants and nonexceptional CM j ensure this is precisely the quadratic-twist distinction.

This equality of Weierstrass coefficients plus non-square norm is a **symbolic all-characteristic-zero proof**; it does not depend on the following prime enumeration.

## 3. The target-prime Frobenius sign switch is exact, branch-sensitive

For every target prime `p≡13,19 (mod 24)`, `(2/p)=-1`, so the reductions use `F_{p²}=F_p[T]/(T²-2)` with `T^p=-T`. The norm of the twist parameter is

```text
N_{F_{p²}/F_p}(d)=-1/18,
χ_{F_{p²}}(d)=χ_{F_p}(-1/18)=(-2/p)
                = -1 for p≡13 (mod24),
                = +1 for p≡19 (mod24).
```

The equality `χ_{p²}(a)=χ_p(N(a))` is the exact quadratic-character norm criterion. By an **explicit change of the x-coordinate in the point-count character sum**, the twisted curves have opposite (respectively equal) q-Frobenius traces when this character is -1 (respectively +1):

```text
a_{p²}(E3) = χ_{F_{p²}}(d) * a_{p²}(E4).
```

This relation is unconditional for the stated curve models and good target primes. **Consuming** the separate pre-existing E3 CM plus rational three-torsion author-side theorem `a_{p²}(E3)=+2p` yields the conditional family corollary

```text
#E3(F_{p²})=(p-1)², both target branches;
#E4(F_{p²})=(p+1)² for p≡13 (mod24);
#E4(F_{p²})=(p-1)² for p≡19 (mod24).
```

The twist character and conditional implication are proved here; that previously authored CM theorem is not re-credited as new research or independently reviewed merely by reuse.

## 4. Independently executed exact finite-field point counts (not a native H0/B0 experiment)

The new standard-library checker at `research_notes/portable_direct/d25_original_E3_E4_CM_fibre_twist_20261027.py` (first verified immutable source commit `851ffb559881e3c5478abc3853aada25a6394164`, Git blob `b024818bbf72773532b3f3a3dfb1878ca791663d`) executes two distinct obligations:

1. Exact `fractions.Fraction` algebra in `Q(s)` establishes **all** listed A/B and twist identities and the negative rational norm, without floating-point fitting.
2. It independently enumerates **every x∈F_{p²}** for both published curves reduced to their explicitly proven short models, computes `χ_{p²}(f(x))=χ_p(N(f(x)))` (0 at zero), and adds the point at infinity. This does not infer either point count from a presumed trace or Frobenius scalar.

Executed exact results, selected primes spanning both target branches:

| p | χ(d) | #E3(Fp²) | #E4(Fp²) | a(E3) | a(E4) |
|---:|---:|---:|---:|---:|---:|
| 13 | -1 | 144 | 196 | 26 | -26 |
| 19 | +1 | 324 | 324 | 38 | 38 |
| 37 | -1 | 1296 | 1444 | 74 | -74 |
| 43 | +1 | 1764 | 1764 | 86 | 86 |
| 61 | -1 | 3600 | 3844 | 122 | -122 |
| 67 | +1 | 4356 | 4356 | 134 | 134 |
| **373** | **-1** | **138384** | **139876** | **746** | **-746** |

For p=373, `q=139129`, `N(d) mod373=145` is nonsquare, `#E3=(373-1)²`, `#E4=(373+1)²`. The exhaustive p373 count uses all **139129 field x-values for each model**, no approximations. Deterministic SHA-256 for the canonical JSON output of these seven rows:
`1c0d4e46d4be4862580f05a73b4e54c9545bb5a97a44ffee88abb0ab69220ca8`.

The **p373 opposite q-Frobenius signs constitute a typed negative gate**: despite the earlier exact finite congruence `W_373≡S_373≡373 (mod373³)`, no proof of the bridge may silently identify *untransported q-Frobenius traces* of these two published original curves. The algebraic twist, its field-of-definition, character and differential scaling must be transported first. This is a falsification of an implementation/proof shortcut, **not** a counterexample to LIFT, nor a demonstration that q-Frobenius and H0/B0 are the same object.

## 5. BRC information-loss audit; scientific and control continuation

**BRC COMPOSE_APPLIED.** Carrier: `(E3(t3),E4(t4),K,sigma,d,L/r,ω3,ω4,F_{p²})`. Observer: original curve point counts and signed q-Frobenius, plus the **separate** weighted hypergeometric observers `W_p,S_p` and the frozen `Delta_p-R_p`. Future operations: reduction mod target primes, quadratic character, possible isomorphism/differential transport, independently authenticated native H0/B0 comparison. Collapsing to a common `j` loses the `d` square class; collapsing to the unsigned degree/trace norm loses the **opposite p373 trace**, and collapsing the weighted sums to point counts changes observer type. The quadratic auxiliary field is **not** Enterprise native X6 geometry or a claimed native two-dimensional plane; P000 and ACTIVE residual-fidelity constraints are unmodified.

**Mother/frozen provenance:** D25/LIFT/JT2 remains OPEN after the accepted D24 UR/JT0. The previously proven Guo–Zudilin companion theorem, 815-prime `W` finite regression, 15-prime bridge, original E3 CM/2-/3-isogeny notes and the 31-term Wilson companion tail at p373 are read-only dependencies, not new unit credits. **New immutable author frontier:** exact published-original E3/E4 quadratic twist `d=s/6`, both unmodified models' differential scaling, uniform target-prime sign character, and seven independent field-point-count certificates including p373.

**Highest native evidence missing (unchanged):** fixed original-class H0/B0 divided-power representative, actual `[X]U mod373²=139129`, native rank, semilinear p-Frobenius and two-digit normalizer, original signed odd Green/Hesse, same-definition κ and `Delta-R`. The native benchmark remains `NOT_EXECUTED / PENDING_OWNER`, responsible intake [Enterprise Math #1559](https://github.com/awdawmip/enterprise-math/issues/1559), unassigned. It cannot be replaced by this curve-count checker. **Next exact native action:** authorized native executor identifies the *actual H0/B0 operator and basis* under frozen science pin, executes original p373 benchmark and publishes raw reproducible matrix/coefficients/signed readout; if comparing an E4 period or CM model, explicitly record the E3↔E4 `d=s/6` twist and p=373 sign. Route native evidence via real Researcher claim/open and independent Driver review. Otherwise no experimental success is claimed.

**Research-lane source control:** stable conversation `chatgpt-research-onhour-enterprise-math-20260923` (never the maintenance ID). Latest own recovery [bridge #6575](https://github.com/awdawmip/kimi-query-bridge/issues/6575) showed local service session `MCP-de3e5bafb24f43f4a5e6285e7601676a` ACTIVE but `source_authority_verified=false`, no own winning claim, open run or pending mutation; original dispatch `research-onhour-20261027-0507-dispatch-r13`, [#6576](https://github.com/awdawmip/kimi-query-bridge/issues/6576), terminated `FAILED / TimeoutExpired`. This turn's Site exact continuation query returned `CONTROL_QUOTA` (no new authorization), and old session-start repair is tracked by [#1539](https://github.com/awdawmip/enterprise-math/issues/1539). Neutral three-file staging archive `SD-d7c23e7984c2ddaac60a` remains separate provenance; no claim/Result review, fence override, blocked mutation replay, dispatcher bypass or maintenance identity use occurred.

**Checkpoint:** GitHub direct noncanonical `research_notes/portable_direct` source artifact, readback required; not a Source-native `publish_checkpoint` or formal Result. `completed_units` for **this author-side output only**: `[original E3/E4 exact quadratic twist, target-prime character derivation, independent seven-prime full Fp² point counts]`. `current_unfinished_unit`: original p373 H0/B0 benchmark and an all-prime proof/counterexample/strictly smaller LIFT certificate. `do_not_repeat`: accepted D24 UR, prior D25 notes, current twist derivation once persisted. `session/claim/run/request`: local ACTIVE but unverified Source authority / no own winning claim / no open run / failed original dispatch #6576, no new native request ID. **No scheduler, notifications, frozen scientific source, control authority or P000 modified.**
