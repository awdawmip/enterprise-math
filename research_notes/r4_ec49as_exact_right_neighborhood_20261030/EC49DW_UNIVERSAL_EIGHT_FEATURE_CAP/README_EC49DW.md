# EC49DW — universal eight-feature bound for native X6 continuation grammars

Date: 2026-11-02. Author-side mathematical result; **PORTABLE_DRAFT / EXACT_CHECK_PASS / UNREVIEWED / NOT_ADMITTED**. Continues EC49DV (immutable predecessor `9788592ccaeb4a9949b0f54cbfd66389ee2b9736`). Scientific source pins remain global `773d538180bfb49e24cffeb35c3ee75eb0628e2e` and EM `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current normative context read separately from global `97470bf98289ab00c020353e148e3b190edc660e` and EM `284995fa2e77fca69707ca4f5cd5eb865b54cd48`. P000 and ACTIVE worldview unchanged.

## Theorem: no ninth old A/B feature under any fixed open-loop primitive future alphabet

Historical objects are **genuinely ordered signed primitive paths in all six native X6 axes**. The historical application has length n even and exact full displacement D=-2E1. A/B record whether adjacent primitive pairs (+E1,+E2)/(+E2,+E1) have ever occurred. Let L be the last primitive's port (+E1=1,+E2=2,other=0). For any positive x,y, let X(w)=product_i x_i^(number of positive Ei steps in w), similarly Y(w); negative steps have unit factor. Count is a third instrument. Each accepted fixed future operator word is reported separately by all four final A/B buckets and all three instruments; returning means exactly +2E1 in six coordinates.

Define `z=(z00,z01,z10,z11,pA,pB,q,r)`, with `zab=1[(A,B)=(a,b)]`, `pA=1[A=0,L=1]`, `pB=1[B=0,L=2]`, `q=1[A=0,B=0,L=2]`, `r=1[A=0,B=0,L=1]`, and `H8(w)=(X(w)z(w),Y(w)z(w),z(w))`.

**For any alphabet Γ consisting of fixed finite nonempty signed-X6 primitive words, any finite set of historical paths and any selection of future operator words independent of historical hidden state, all future readout columns lie in span(H8). Thus `rank O_Γ,h ≤ rank H8 ≤ 24` at every horizon.**

If Γ contains the original seven operations `a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`, then **for every integer h≥2**:
```
rank O_Γ,=h = rank H8,     rank O_Γ,1..h = rank H8
```
for all strictly positive real x,y and every finite historical path population. This also holds when additional future operations are zero-displacement or generate A/B internally. In particular, no ninth *per-instrument old A/B seam-history* direction arises merely by augmenting the fixed open-loop native grammar.

### Complete analytic argument

Take any nonempty primitive future t and write s=its first primitive step, C=1[t contains internal adjacent (+E1,+E2)], T=1[t contains internal (+E2,+E1)]. Every adjacent pair of the concatenation is historical, internal to t, or exactly across the history/future seam. Therefore:
```
A(wt) = A(w) OR C OR (L(w)=1 AND s=+E2)
B(wt) = B(w) OR T OR (L(w)=2 AND s=+E1).
```
Expand the four bucket indicators. For C=T=0 and s=+E1 they are `(z00-q,z01+q,z10-pB+q,z11+pB-q)`; for C=T=0 and s=+E2 they are `(z00-r,z01-pA+r,z10+r,z11+pA-r)`; otherwise without new internal flags they are the old four z-buckets. For C=1,T=0 only final 10/11 survive, optionally shifted `(-pB,+pB)` if s=+E1; for C=0,T=1 only 01/11 survive, optionally shifted `(-pA,+pA)` if s=+E2; for C=T=1 only 11 survives with value 1. All are linear in z. Since `X(wt)=X(w)X(t)` and `Y(wt)=Y(w)Y(t)`, and future factors are strictly positive, each word-resolved instrument separately factors through the three weighted copies of z. This proves the upper bound **for arbitrary fixed primitive words, including those ending in positive steps and those with internal A/B**.

For the sharp lower span when Γ contains a–g, eight horizon-2 returning words `ef,ce,ec,de,ed,fe,ge,eg` recover all features: `ef` returns four original buckets; `(ce,11)-(ec,11)=pB`, `(de,11)-(ed,11)=pA`, `(ef,00)-(fe,00)=q`, `(eg,00)-(ge,00)=r`. At horizon 3, use `aee` for old buckets, `cce/ecc` and `dde/edd` for ports, and `eff/ffe` and `egg/gge` for q/r. Appending `(ae)^k` to either parity's witness has zero X6 displacement, creates no new A/B adjacency, and multiplies future x/y products by nonzero `(x3*x1²)^k` / `(y3*y1²)^k`. So every exact horizon h≥2 recovers all eight columns in every instrument. Together with the upper bound, ranks are equal. The cumulative horizon includes h=2. QED.

Eight is necessary already on **genuine historical words**, not just formal states: eight native n=10, D=-2E1 paths with the same positive count p=(1,3,0,0,0,0) have an exact z-determinant +1, checked again in this run. Their BRC products agree for any x,y, so the count channel alone distinguishes eight directions.

## Executed finite evidence and first saturation examples

Self-contained standard-library checker: `VERIFY_EC49DW.py.gz.b64`; exact JSON report: `EC49DW_EXECUTED.json.gz.b64`. Decode base64 then gzip. Actual decoded SHA256: Python `84d3646b29d2a19ec66bbac7db567744cf7b9f40bb378c5cd29b24a491a84458`, report `54183fdbcba6dc5fea00c9ac79c6314fa9c08522386f141ac2db1491419ffd2c`. It exhausts **all 22,620 native signed primitive future words of length 1–4**, all 12 formal initial states, checking the seam identity directly. It independently enumerates returning operator words for a–e, a–f, a–g and a–i, where the new two zero-return operators are `h=(1,2,-2,-1)` (internal A) and `i=(2,1,-1,-2)` (internal B). For a–i at horizon 1–4, exactly returning word counts are **1,12,111,936** and exact transfer ranks **4,8,8,8**. For a–e, ranks h1–5 are **4,5,6,5,6**; for a–f **4,7,7,7,7**; for a–g **4,8,8,8,8**.

Full historical-state DP (n=2,4,6,8,10,12; all six positive-count compositions and reachable A/B/last-port states) gives the following exact **historical** ranks of H6/H7/H8, for the *named integer parameter pairs only*:
| x / y class | n=8 | n=10 | n=12 | earliest n attaining algebraic ceilings |
|---|---|---|---|---|
| generic x=(2,3,1,2,3,4), y=(5,7,3,5,7,9) | 15/17/19 | 18/21/24 | 18/21/24 | **10** |
| oblique affine x=(2,2,1,2,3,4), y=(3,3,1,3,5,7) | 14/16/18 | 17/20/23 | 18/21/24 | **12** |
| proportional x=(2,3,1,2,3,4), y=2x | 12/14/16 | 12/14/16 | 12/14/16 | **8** |
| uniform x=(2,...,2), y=(3,...,3) | 6/7/8 | 6/7/8 | 6/7/8 | **8** |

The ceilings are respectively 3d,3d,2d,d for feature dimension d=6,7,8; the latter two follow from the exact weight relationships. Native n below each asserted first attainment were all enumerated and n must be even. The H6 result translates to the old a–e future observer for odd exact h≥3 and cumulative h≥2, **not** the special even h five-feature observer; H7 corresponds to a–f at h≥2, H8 to any superset of a–g at h≥2.

**Next discriminating observer:** two exact native histories of n=10 and identical p=(2,2), A=B=1,L=0 (thus identical z,X,Y for every x,y) have opposite first-appearance order of A and B. They are `(-1,-1,-1,-1,-2,1,2,1,2,-2)` (A first) and `(-1,-1,-1,-1,-2,2,1,2,1,-2)` (B first). An observer that explicitly reads the order distinguishes them and needs an additional historical coordinate. This is a change of observer, not a counterexample to the theorem's original four buckets.

## Authority and evidence status

Reuse applied to the existing EC49DT/EC49DU typed BRC observer, EC49DV exact native-history DP and previous real-path witnesses. Exact calculations above were actually executed with Python integers and Fraction; the all-horizon theorem is analytic. GitHub authenticated login is awdawmip, repository push permission available. Gateway 0.6.11 reports `research_authority_granted=false`, owner listing `CONTROL_QUOTA` (5/5), and this run's own RESEARCHER session-start returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. No active owner was resolved; no formal RA, CLAIM, Result, Driver review or Foundation admission. Next task `NEXT_EC49DX.md`.