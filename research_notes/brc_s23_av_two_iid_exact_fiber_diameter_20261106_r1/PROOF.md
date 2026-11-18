# S23/AV two-iid: exact indistinguishable-fiber diameter and strengthened reconstruction lower bound

Date: 2026-11-06. Status: author-side exact analytic theorem; rational checker executed; independent review pending. Scientific input remains frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Continuation of PR #1777 and refined two-iid bound at `6a00e023af967e99fe459d72b2e7d2dc1b861430`.

## Model

For all real `a,c in [1/2,7/8]`, `z=(1-a)c`, define full stop distribution `A(a,c)=(a,z,1-a-z)` on labels `(1,3,4)` and binary observation `B(a,c)=(z,1-z)`. The original unrelated parameter `b in [1/8,1/2]` is arbitrary. Two trials are independent conditional on the **same hidden** `(a,c)`. For a single parameter-independent row-stochastic `4 x 9` reconstruction kernel `L` (binary input outcomes `YY,YN,NY,NN`; full output outcomes `11,13,14,31,33,34,41,43,44`), set

`delta_2=inf_L sup_(a,c in [1/2,7/8]^2) TV(A(a,c) tensor A(a,c), [B(a,c) tensor B(a,c)] L)`,

where `TV(P,Q)=sum_j |P_j-Q_j|/2`.

## Theorem (all indistinguishable pairs)

For **every** two legal parameters giving the same binary observation, the two-iid full stop distributions have total variation at most `18/49`. The bound is attained for

`theta_0=(a,c)=(1/2,1/2)`, `theta_1=(5/7,7/8)`, both with `z=1/4`.

Consequently `delta_2 >= 9/49`. Combining this with the previously proved exact joint-kernel upper certificate gives

**`9/49 <= delta_2 <= 387769986271/2048000000000`.**

The new lower is strictly stronger than `15383/83769`, by exactly `22/586383`. The upper is carried forward unchanged.

## Analytic proof

**(1) All indistinguishable fibers.** Equality of `B` means equality of `z`, with `z in [1/16,7/16]`. For any fixed z, the legal a values are exactly

`alpha(z)=max(1/2,1-2z) <= a <= beta(z)=min(7/8,1-8z/7)`.

This follows from `1/2<=z/(1-a)<=7/8` and the legal bounds on a. Every listed endpoint is attained by a legal parameter pair.

**(2) Exact two-iid TV on a fiber.** For `a'=a+d>=a`, write `u=1-a-z`. Then `p=(a,z,u)` and `q=(a+d,z,u-d)`. Since legal `a>=1/2` and `u<=1/4`, the positive entries of `q tensor q - p tensor p` are precisely the coordinates `(1,1),(1,3),(3,1)` (possibly zero on the boundary); in row-major tensor index they are `0,1,3`. The `(1,4)` difference is `d(u-a-d)<0`, and all other signs follow directly. Thus

`TV(p tensor p,q tensor q) = [(a+d)^2-a^2]+2zd = (a'-a)(a+a'+2z)`.

For fixed z this is increasing in a' and decreasing in a, so the maximum on that fiber is attained at `a=alpha(z),a'=beta(z)`.

**(3) Maximize over the entire real legal domain.** The exact fiber diameter is

`D(z)=(2z-1/8)*(15/8)` for `1/16<=z<=7/64`;

`D(z)=(6z/7)*(2-8z/7)` for `7/64<=z<=1/4`;

`D(z)=(1/2-8z/7)*(3/2+6z/7)` for `1/4<=z<=7/16`.

The derivatives are respectively `15/4`, `12/7-96z/49` and `-9/7-96z/49`, hence the first two pieces strictly increase and the third strictly decreases in their indicated intervals. Therefore the global maximum is at `z=1/4`, with `alpha=1/2,beta=5/7` and

`D(1/4)=(5/7-1/2)*(1/2+5/7+1/2)=18/49`.

**(4) Universal reconstruction obstruction.** At the equality witnesses `B(theta_0)=B(theta_1)=(1/4,3/4)`, so `B(theta_0) tensor B(theta_0)=B(theta_1) tensor B(theta_1)`. For **every** parameter-independent kernel L, both binary experiments reconstruct the same R. The TV triangle inequality gives

`18/49=TV(P_0,P_1)<=TV(P_0,R)+TV(P_1,R)<=2 sup_(a,c) TV(P_(a,c),Q_(a,c)L)`.

Taking infimum over L yields `delta_2>=9/49`.

## Verification, status and scope

The complete real parameter-domain proof is the four analytic steps above. `VERIFY.py` executes 789 exact standard-library Fraction assertions covering the witness, endpoint identities, exact sampling and derivative-sign checks. Finite samples are supplementary, not the basis of the continuous proof. This is a **conditional tagged AV observer** result: any transfer to frozen original ten-label S23 `R_beh(k,10)` still requires checking lawful encoder/decoder/source maps and quantifiers. No independent review, formal CLAIM or mathematical admission is claimed.
