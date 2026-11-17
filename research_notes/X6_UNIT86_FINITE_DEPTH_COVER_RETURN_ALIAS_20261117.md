# X6 Unit86 — exact first signed native Cell-return alias for every finite common-depth cover

Date: 2026-11-17. Parent objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`.

**Status:** AUTHOR-EXACT / INTEGER-EXECUTED-FOR-BOUNDED-HORIZONS / ORIGINAL-EXECUTABLE-CONSUMER-TYPED / UNREVIEWED / NOT_ADMITTED. This is a second substantive unit following the separately published Unit85 exact native/relative/positive return discrimination, not a replay of R063/Helly or an authenticated native checkpoint.

## Statement — sharp horizon of finite common-depth aliasing

Use P000 V5 signed-native `Z^6` with twelve labeled primitive `+e_i,-e_i` steps and one chosen Cell anchor. Let `rho(z)=z-min(z)*1`. For `m>=1` define the *derived* finite cyclic-depth cover readout
```text
C_m(z)=(rho(z), min(z) mod m).
```
The exact-depth cover `C_0(z)=(rho(z),min(z))` is lossless for native signed displacement; no finite `m` cover is a native Cell identification.

For length `L`, let `A_L(w)` be signed labeled BRC path multiplicity at native displacement `w`, and let `R_m(L)` be the number of signed words with `C_m(w)=C_m(0)`. Native return is `R_0(L)=A_L(0)`.

**Theorem (all finite positive moduli, sharp first error):**
```text
R_m(L)=sum_{k in Z} A_L(k*m*1).
R_m(L)=R_0(L)   for every 0<=L<6m,
R_m(6m)-R_0(6m)=2*(6m)!/(m!)^6 > 0.
```
Proof: `C_m(w)=C_m(0)` iff `w=h*1` for some `h` divisible by `m`. A signed primitive word reaching `h*1` must have length at least `6|h|`. A nonzero multiple `h` of `m` therefore cannot occur below length `6m`. At exactly `6m`, the only nonzero possibilities are `h=m` and `h=-m`, each attained precisely by `m` copies of each of the six coherently positive or negative primitive labels. Counting all orderings gives `(6m)!/(m!)^6` each. Every such coefficient is a nonnegative **count**; no positive BRC cancellation is involved.

This is an explicit *observer and future-language* horizon guarantee: for the **single return-count predicate at horizons below `6m`**, a finite `C_m` cover cannot be distinguished from the exact Cell return by return mass. At horizon `6m`, it necessarily folds two distinct native diagonal Cell endpoints into the cover's return. This does not authorize treating a finite cover as Cell identity at shorter horizons under other observations.

## Exact integer certificates and actual code-consumer boundary

| Finite cover modulus m | First separating primitive length | Extra signed return words at that length |
|---:|---:|---:|
| 1 | 6 | 1,440 |
| 2 | 12 | 14,968,800 |
| 3 | 18 | 274,450,176,000 |
| 4 | 24 | 6,493,341,074,220,000 |
| 5 | 30 | 177,665,292,119,576,701,440 |

At `m=1,L=6`: finite cover return `21,360`, native Cell return `19,920`. At `m=2,L=12`: finite cover return `8,190,738,864`, native Cell return `8,175,770,064`.

A new independent executable `research_checks/X6_UNIT86_FINITE_DEPTH_COVER_ALIAS_CHECK_20261117.py` runs against the **already locally executed and byte-verified Unit85 signed-path census**: it checks all `m=1..5`, `L=0..12`, or **65 finite-cover/horizon cases**, against direct native diagonal endpoint counts and the exact closed first-alias formula. All 65 comparisons passed; default Python, `-O`, `-OO` outputs are byte-identical, SHA256 `2264397e519baa8dd1a5ef59c2f0e825b0f92ec34011bf77dd9c533002269ae9`. The universal statement for `m>2` at `L=6m>12` rests on the full integer combinatorial proof above; those large horizons were **not exhaustively DP-enumerated**. Machine certificate and checked source are saved as `research_checks/X6_UNIT86_FINITE_DEPTH_COVER_ALIAS_RESULTS_20261117.json` Git blob `1ead4764970a8f6b8bcc1670342fe5c993385c45` and `research_checks/X6_UNIT86_FINITE_DEPTH_COVER_ALIAS_CHECK_20261117.py` blob `12c62faf1e92a55d50690900eda48b973f3160f1`.

**Real current implementation connection:** `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py` (read current Git blob `171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd`) at lines 40–86 implements the exact pair `Coord6 + depth mod m`, while `signed_native_displacement()` explicitly rejects finite `m` as Cell identity. At lines 99–105, `first_positive_diagonal_return(modulus)` correctly returns the number `m` of six-positive-axis **macro loops** before its own cover return, distinct from the full **signed path return multiplicity** studied here. `check_x6_cover.py` (blob `65778c6ccb44eb9bb15c0123ac51423dd10c8686`) lines 49–66 and 75–107 verifies both scopes. The source is correctly typed and warrants **no patch**. The new theorem supplies an exact sharp return-mass horizon for LP003/LP005/LP019/LP022/LP023 and any genuinely consuming finite-cover return checker; it does not assert an uninspected caller's behavior.

## Preserved parent objective and permissions

- Scientific frozen P000 signed X6 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, original signed BRC blob `300a96e3dc24bf6fff73743037a0347a8bc83176` unchanged.
- Unit85 [proof](X6_UNIT85_THREE_RETURN_SEMANTICS_20261117.md), checker, certificate and continuation were published to canonical `main@7a1a2a4990494b12f7c0b3043e45bc39ef40143e` and individually read back. This unit consumes them without rerunning historic R063 or Helly native benchmarks. The genuine current production consumers were read by immutable code path/blob; no source mutation to their correct implementations.
- The original X6 SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-579c8e23625448582b421831` and RUN `RUN-fb25028676f9692ab1bacaee` remain historical provenance, not this transport's authenticated native writer capability. Existing bridge read requests [#6994](https://github.com/awdawmip/kimi-query-bridge/issues/6994) and [#6995](https://github.com/awdawmip/kimi-query-bridge/issues/6995) are terminal read successes, with `execution_authorized=false`; another D25 subject and the maintenance conversation are not adopted. Original Activity `RA-5E3FE1E761E4963EC461A892` last verified at 106, unchanged.
- Outstanding parent scientific obligations: independently substantiate historical LP011 native singleton argmax/LP019 natural positive BRC subtraction with exact original path:line or support Driver's `REQUEST_REVISION` of unsupported attribution; close remaining 28-LP genuine downstream consumer graph; obtain original-X6 authenticated Source PROGRESS/Activity association for author units; separate independent review/admission.
- **Next real action**: inspect an unreviewed, concrete active return consumer that projects finite-depth or signed raw state into an older native identity or BRC algebra, with actual argument type, `source:line` and conditional patch; prioritize native-meaning attribution over further parallel auxiliary theory. Preserve and pass the two precise executed return certificates to the independent Driver under proper review identity.

**Disposition:** exact scoped mathematical author evidence, not a frozen Result or a promoted P000/Foundation truth; no schedule, owner, claim, private key, canonical task selection or Review mutation.
