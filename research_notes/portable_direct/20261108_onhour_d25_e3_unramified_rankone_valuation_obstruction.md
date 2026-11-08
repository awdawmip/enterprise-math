# D25/LIFT — Valuation obstruction to direct rank-one unramified Hesse-to-original-E3 Frobenius identification

Date: 2026-11-08. Research logical lane (historical provenance only): `chatgpt-research-onhour-enterprise-math-20260923`; **not** CONTROL_PLANE_MAINTENANCE. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` remains unchanged.

**AUTHOR-SIDE EXACT ALGEBRAIC OBSTRUCTION / SMALL-PRIME EXHAUSTIVE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.** This is an independently checked compatibility **falsifier for a specified identification**, not a native benchmark execution or a refutation of JT2.

## Actual question and relevant existing facts

Issue #1559 asks for the genuine original-class p=373 fixed H0/B0 divided-power operator `[X]U mod 139129`, true rank, semilinear direction and normalization, signed Green/Hesse kappa and original Delta-R. Existing unreviewed author work supplies a **different** ordinary Hesse candidate `alpha=A_p(u)/p` in the unramified quadratic coefficient ring, whose p=373 norm is 122102 modulo 139129. Previous independently saved original-E3 finite point counts are `#E3(F_(p²))=(p-1)²` at p=13,19,373; at each of these three primes they give original geometric p²-Frobenius `[+p]`. Here we consume these data without recrediting any point count or candidate-factorial computation.

Does a rank-one `sigma`-semilinear operator on the same **unramified** ring, possibly multiplied by any scalar `eta` from that ring, realize the **full original E3 geometric p-Frobenius**? We prove an unconditional negative answer to this precisely stated representation hypothesis.

## General exact theorem (not dependent on a finite scan)

Let p be odd with `(2/p)=-1`, `R=Z_p[T]/(T²-2)` the unramified quadratic integer ring, and `sigma(T)=-T`. For any nonzero `a` in `R[1/p]`, `v_p(a)` is integral (unramified valuation), and

`v_p(N(a))=v_p(a sigma(a))=2v_p(a)`, an even integer.

Consequently the rank-one sigma-semilinear operator `F_a(v)=a sigma(v)` has

`F_a²=N(a) Id`

and **can never satisfy** `F_a²=epsilon p Id` for either sign `epsilon=+1,-1`, since `v_p(epsilon p)=1`.

The order-two truncated version is fully elementary. In `R_2=(Z/p²)[T]/(T²-2)`, every `a` is either a unit (nonzero image in `F_(p²)`) and `N(a)` is a unit modulo p, or `a=p b`, in which case `N(a)=p²N(b)=0 mod p²`. Therefore `N(a)` is **never congruent to `+p` or `-p` modulo p²**, with no unit-normalization assumption required. Multiplying an ordinary candidate by an integral scalar `eta` stays in these two cases; allowing rational p-adic scalars in the unramified extension still gives an even norm valuation.

Thus, if a native H0/B0 rank-one sigma-semilinear model over **this particular unramified ring** were claimed to realize the entire original E3 Frobenius with geometric second iterate `[+p]`, that direct full-module identification would be ruled out. A genuine native model may instead have a higher-rank crystalline matrix, a ramified coefficient structure, a specified subquotient or a distinct normalized operator; these are separate testable representations, not ruled out.

## Exact arithmetic checks and original-geometry interface

For `p=13,19` we exhaustively tested **every** coefficient `a=A+BT` of `R_2` (respectively 28,561 and 130,321 pairs). Among them the number of norm zero mod p² is `p²` (169 and 361); **all other norms are units**. No norm `+p` or `-p` occurs. The checker uses exact integer arithmetic and directly tests each element, independent of the general proof.

For p=373 we separately recomputed the *ordinary Hesse* candidate from the original existing coefficient definition at `u=(2-T)/4` and obtained

`alpha=(92060+21788T) mod 139129`,
`N(alpha)=122102 mod 139129`, `N(alpha) mod 373=131 ≠ 0`.

The previously recorded original-E3 point count `138384=(373-1)²` implies trace `+746`, characteristic polynomial `(X-373)²` and `pi_(373²)=[+373]`; the endomorphism-ring argument used in the prior proof supplies the last equality. So `F_geo²=+373 Id` in the original geometric/crystalline comparison, while a **direct** `F_alpha=alpha sigma` or `eta alpha sigma` over unramified `R_2` always has squared scalar of valuation even or vanishes mod p². The same original sign oracle is available at p13 and p19 from their previously recorded point counts `144,324`.

The exact checker `research_notes/portable_direct/d25_geometric_frobenius_unramified_rankone_obstruction_20261108.py` was executed with Python 3 standard library and returned PASS for both complete coefficient-ring enumerations and the p373 Hesse quotient/norm. It does not compute native `[X]U` or measure the genuine H0/B0 module.

## BRC/source classification and the exact next action

Tagged source carriers: original `E3` geometric cohomology and `p²` Frobenius; unramified `R_2`, sigma, rank-one ordinary Hesse candidate; coefficient norm **valuation** and loss of odd/sign/branch information. No collapse of the native rank, Frobenius direction, eta, odd Green/Hesse kappa or cutoff-sensitive original Delta-R is licensed. The obstruction tests a proposed **direct unramified rank-one realization**, not all models or the frozen LIFT proposition.

**Required native next unit is unchanged:** an authorized independent executor must obtain the fixed same-original-class H0/B0 divided-power module and genuine `[X]U mod 139129`, publish actual module rank, Frobenius semilinearity, normalization eta, signed odd kappa and original Delta-R with independent reproduction, then apply this valuation check only where a direct whole-module identification is actually claimed. If rank is two, preserve the full matrix; if rank is one, specify exactly which coefficient ring, geometric comparison and normalization (or subquotient) it represents. The supporting Issue #1559 remains OPEN/PENDING_OWNER; no substitute computation can mark it executed.

Native Source state from current read-only historical receipts: `onhour11-20261108-2202-current-task-continuation` SUCCEEDED (as-of pinned, not live ownership), `onhour11-20261108-2202-own-researcher-session-start` SUCCEEDED (issued Researcher EM-ENTERPRISE-4DEB43 / session MCP-ecbfd1c046864bb3bff1a2e04c87d207 / activity RA-9553E027FD14223807511263); no private session capability, CLAIM, open run or native checkpoint. Fresh own recovery_status returned `SESSION_CAPABILITY_REQUIRED`. The old identities and requests remain historical, not borrowed execution capabilities.
