# X6 Unit164 — R061 bidirectional length spectrum: exact observer fibers and N-BRC nonfaithfulness

Date: 2026-11-19. Task: RS-X6-LEGACY-PLANE-RECONCILIATION (publication TP2-B4A441B23DA3159232C2).
Author/source lane: EM-X6-FB6990 / MCP-082892eb480e45dea6d4b9fcc0491034 / logical conversation chatgpt-research-onhour-enterprise-math-20260923.
Status: AUTHOR_PROVED / FINITE_EXACT_EXECUTED / SOURCE_COMPARISON / UNREVIEWED / NOT_ADMITTED.
Frozen scientific baseline: 59538f585d037d09ef687b28715c4bc1a3f9fe03.
Frozen historical comparison: fd2bcff10ca6e147348b6c1236027fc0d2877df3.

## Actual historical consumer and typing
Historical `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` (blob 58ccac6d8b88dcfd91a0a6017ca7b29187b4e7b0), lines 19–58, 170–221 and 233–289, defines the nonnegative min-zero decoder, its directed square gauge, and reverse decoder. Historical `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md` (blob da35c76869ff88e46e28e33ba5bc37c95374a15d), §§4–5, is the **actual downstream consumer**: an unordered pair of the two directed gauge values, plus a *separately typed orientation-tagged path disjoint union*. These are relative/chart observer statements, not present-day native X6 metric or path identity. Current retyped spectrum (main blob 358a4997157d7546d88e63ae8d32e95feebf9c08) already explicitly identifies the observer scope. This audit does not allege a faulty historical implementation or alter R063.

## Exact theorem (fixed sector and axis-order convention)
Let `a >= 1`, `0 <= b <= a`; take the old min-zero directed chart value `D=(a,b,0)`. The **squared** unordered two-direction gauge spectrum from the historical formulas is
[
 Sigma(a,b)={a^2+b^2,;a^2+(a-b)^2}_{multiset}.
]
The map on canonicalized fixed-sector inputs `(a,b)` has *exactly* these fibers:
[
 Sigma^{-1}(Sigma(a,b))={(a,b),(a,a-b)},
]
with duplicate members identified (a singleton exactly when `2b=a`). In particular, it never has a fiber of size greater than 2 in this stated domain. If the positive axes are not already labeled/ordered, a separate axis-permutation label must be retained; the theorem does not silently identify it.

**Proof of completeness.** Write the ordered spectrum values `s<=t`, `S=s+t`, `D=t-s`, and `u=|2b-a|`. Exact integer identities give
[
 2S=5a^2+u^2,qquad D=au.
]
Thus `x=a^2` is a positive perfect-square root of
[
 5x^2-2Sx+D^2=0.
]
The other algebraic root is `u^2/5`. If `u>0`, this second root is not an integer square: otherwise `u^2=5v^2` with integer `v>0`, which contradicts the parity of the prime-5 valuations. If `u=0`, the other root is zero, also excluded by `a>=1`. Hence the spectrum uniquely determines `a`; it determines `u=D/a`, then the only possible integer values `b=(a\pm u)/2` are precisely `b` and `a-b`. Conversely substitution exchanges the two spectral entries. QED.

## Exact BRC and native-lift consequence
For the raw signed Cell displacement `(a,b,0,0,0,0)` anchored at an actual Cell, the native squared length is `a^2+b^2`, and the positive-step shortest-path N-BRC weight is `B(a,b)=binom(a+b,b)`. The spectrum-involution companion `(a,a-b,0,0,0,0)` has native squared length `a^2+(a-b)^2` and weight `B(a,a-b)=binom(2a-b,a-b)`. Since `binom(a+b,b)` is strictly increasing in `b` for fixed integer `a>=1`, the two BRC values are distinct for any nonsingleton fiber.

Thus the **unordered relative length spectrum alone** does not determine native signed squared length or N-BRC path multiplicity. One additional binary orientation/branch selector distinguishes the two chart states, and one bit is necessary on a doubleton. This is a local, exact sufficient-state statement at the specified fixed-sector domain; it is not a global final-Cell address codec or a physical rotation result.

Sharp examples:
- `(a,b)=(1,0)` versus `(1,1)`: both have spectrum `{1,2}`; signed native squared lengths `1,2`; N-BRC `1,2`.
- `(3,1)` versus `(3,2)`: both have spectrum `{10,13}`; signed native squared lengths `10,13`; N-BRC `4,10`.
- For each `a>=1`, `(a,0)` and `(a,a)` have the same spectrum `{a^2,2a^2}` with N-BRC weights `1` and `binom(2a,a)`; ambiguity grows without bound.

The historical Stage3 §5 explicitly *keeps* two orientation-tagged path families. That provenance-preserving choice is justified, not refuted, by the theorem. A scalar-only downstream consumer would require a separate proof of its intended sufficiency.

## Reproducibility and precise gap
An independent Python integer checker exhausts `1<=a<=128,0<=b<=a`: 8,384 inputs, 4,224 different spectra (64 singleton, 4,160 doubleton), checking all reverse fibers and binomial inequalities with no failure. This finite check verifies a bounded window; the above theorem proves all positive `a` separately. Original historical R061/R063 tests were not rerun.

Source ledger classification: `PRESERVE_OBSERVER` (historical squared-gauge spectrum), `PRESERVE_PATH_BRC` (tagged disjoint union), `NO_CHANGE` to current signed-X6 retyping. No erroneous LP011/LP019 `commit:path:line` has been established here. Original R063 native benchmark remains complete and untouched. The incomplete 28-LP corpus/consumer audit, previously saved Units149–152 semantic-link debt, and independent Driver review remain open.
