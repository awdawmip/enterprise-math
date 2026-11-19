# X6 Unit151 — R061 derived min-zero triangle gauge and sharp reversal distortion

**2026-11-19 | TASK_RESEARCH | EM-X6-FB6990 | AUTHOR_PROVED / FINITE_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED**

Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`; mother objective `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Scientific pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

## Source audit and disposition

Original frozen `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` (blob `58ccac6d8b88dcfd91a0a6017ca7b29187b4e7b0`) **lines 175–197** type the positive/min-zero length as native; **199–231** prove the triangle inequality, **233–253** give the reverse decoder. Current `main` file, blob `875e3b274e5be03c5872f782872065a0b96d14eb`, has already retyped the gauge as relative-observer-only. The historical triangle inequality is **PRESERVE_OBSERVER**, while its original native interpretation is **SUPERSEDE_AS_NATIVE**; no current-file patch is necessary.

## Exact theorem

For all `z in Z^3` define `D=(1,1,1)`, `c(z)=z-min_i(z_i)D`, `F(z)^2=sum_i c(z)_i^2`, and `Q=Z^3/ZD`. Then:

1. `c(z+kD)=c(z)`, and `F(z)=0` iff `z in ZD`. Thus `delta([p],[q])=F(q-p)` is a well-defined, separating, translation-invariant **asymmetric metric** on the *derived relative/carrier quotient*.
2. `F(x+y)<=F(x)+F(y)` for all integer triples. Indeed with `a=c(x),b=c(y)`, both coordinatewise nonnegative, `c(x+y)=a+b-mD` with `m=min_i(a_i+b_i)>=0`. Thus `0<=c(x+y)_i<=a_i+b_i`, so `F(x+y)<=||a+b||_2<=||a||_2+||b||_2`.
3. For `z not in ZD`, the **sharp** reversal ratio is `1/sqrt(2)<=F(-z)/F(z)<=sqrt(2)`. Permute coordinates of `c(z)` to `(0,a,b)` with `0<=a<=b`, `b>0`. Then `c(-z)=(b,b-a,0)` and
   `F(z)^2=a^2+b^2`, `F(-z)^2=b^2+(b-a)^2`.
   The upper bound is `2F(z)^2-F(-z)^2=a^2+2ab>=0`, the lower bound is `2F(-z)^2-F(z)^2=(b-a)(3b-a)>=0`. Equality occurs respectively at `(0,0,b)` and `(0,b,b)` for every positive integer `b`.
4. The native signed component metric `G(z)=sum_i z_i^2` satisfies `G(-z)=G(z)`, while `G(kD)=3k^2` and `[kD]=[0]`. Thus this triangle/reversal conclusion belongs precisely to the observer layer, not the native metric or primitive step-word identity. The observed historical `(3,4,0)` forward/reverse squares `25,17` fall strictly inside this sharp bound; native signed squares are `25,25`.

This is an all-integer proof, not inferred from finite sampling. The quotient is a derived readout; raw signed X6 Cell coordinates, common depth, and any needed path/branch provenance remain upstream under P000 and the joint-observer contract.

## Independent exact certificate

Standalone checker enumerated **343 vectors** in `[-3,3]^3` (336 non-diagonal) and **117649 ordered pairs**. Tested quotient addition, zero kernel, reversal bound and sharp witnesses, and triangle inequality by exact integer comparison (`(A-B-C)^2<=4BC` if `A>B+C`). All checks passed with CPython normal, `-O` and `-OO`; stdout including newline SHA256 `85f2138382b5612200b3b13094c49e10e5327563fa2b60d9bbb5b776105159b4`. Historical program and original six-file R063 benchmark **not executed**. Companion checker/certificate are separate and should only be cited as GitHub-published after their own readback.

## Durable continuation

**Mother target:** finite claim-level historical X6 reconciliation and true downstream consumer coverage. **New finding:** exact source-level R061 section-8 triangle inequality preserved as relative observer, with sharp ratio theorem; no additional native-ontology change. **Unresolved:** full 28-LP consumer coverage; LP011 alleged signed-argmax and LP019 alleged N-BRC subtraction faulty historical caller require exact `commit:path:line`; independent Driver review pending. **Do not repeat:** authored Units1–150, prior original R063 native benchmark, and original failed writes.

Latest observed native Unit148 request `onhour-20261119-0918-x6-own-unit148-native-progress-v1` = `SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED`, Source `9e80d79f719d17053397f00f4eebdbafbfd5133f`, PROGRESS comment `6997044394`. Original Unit149 native request `onhour-20261119-1000-x6-own-unit149-native-progress-v1` = `FAILED/GITHUB_PRIMARY_RATE_LIMIT`; no Unit149 Source publication established. Preserve original Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-dedc91932641535d284fc171`, RUN `RUN-c92057890282aaaeec520881`; previously recorded generation5 is historical, **not current write authority**.

**Next actual operation:** when native route is available, read fresh exact Source continuation and winning owner/RUN/generation, resolve failed Unit149 through the permitted contract without replaying its original failed mutation; then link already saved Unit149/150 and this unit when authorized. Continue genuinely uninspected historic/current 28-LP consumers. No author self-review or result admission.
