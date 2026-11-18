# EC49FFC — Exact full-BRC-key native length and support-dominance theorem

Date: 2026-11-09 (Asia/Shanghai). Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scope: original six-operation signed-X6 native words, original nine-state DFA, complete BRC key `(x,y,z)`, observation horizons H2–H9. Status: author-side derivation and exact finite computation; independent Driver admission pending.

## Theorem A — full key fixes native path length and native endpoint

The original operation alphabet is `a,c,d,e,f,g`, with **ordered signed six-axis microstep words**

```text
a=(-1,-1), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1),
e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).
```

The positive/count-admissible forward-count identities for a word of operation length `h` with its complete BRC key `K=(x,y,z)` are

```text
#a=z-1, #e=z, #c+#d=x+y-h-1,
#f=h+1-y-2z, #g=h+1-x.
```

**Theorem.** For every original legal word with such a key, the number of native signed microsteps is exactly

```text
L_native(h,K) = 2*(x+y+z-1),
endpoint_X6 = (+2,0,0,0,0,0).
```

**Proof.** Put `t=#c+#d=x+y-h-1`. The native operation lengths in alphabet order are `2,4,4,4,2,2`. Hence

```text
L = 2(z-1) + 4t + 4z + 2(h+1-y-2z) + 2(h+1-x)
  = 2(x+y+z-1).
```

Each of `c,d,f,g` has zero net signed X6 displacement; `a` contributes `-2 E1` and `e` contributes `+2 E1`. Their count difference `#e-#a=1` proves the endpoint. Both claims hold before DFA filtering and preserve all six native signed axes. In particular, if the same key is legal at different horizons, its native microstep length is identical. QED.

**Corollary (bounded full-key inventory).** Put `t=#c+#d`. Every forward-count-admissible key/horizon pair is uniquely parameterized by

```text
z>=1, t,f,g>=0, t+f+g=h+1-2z,
(x,y,z)=(t+2z+f, t+g, z).
```

For `h=2..9`, this yields exactly

```text
sum_{h=2}^9 sum_{z=1}^{floor((h+1)/2)} binom(h+3-2z,2) = 294
```

count-admissible pairs involving 164 distinct keys. The forward-count equations permit `y=0`; the strict `x,y,z>0` subspace consists of 270 pairs involving 140 distinct keys. Native path length is at most `4h<=36` in these horizons. This is a complete bounded search domain for **individual** original operation words, not yet a proof of the full five-key minimum.

## Theorem B — 22-template monotone closure for arbitrary path count

Let `S` be **any finite collection** of legal original signed-X6 words at H2–H9, using at most five complete BRC keys. Let `S_h` be the set of its nonzero terminal DFA labels at horizon `h`. Define `B={16,32}` and `L={1,2,4,8}`, and for `h=4..9` let `b_h=[B subset S_h]`, `l_h=[L subset S_h]`. Suppose

```text
L subset S_2, B subset S_3,
for all h=4..9: b_h OR l_h,
sum_{h=4}^9 b_h >= 4,
sum_{h=4}^9 l_h >= 2.
```

**Claim.** `S` contains an exact 22-word legal subsystem matching one of the fifteen high/low observation templates classified in EC49FEO. Thus, from the previously obtained 94-native-edge lower bound for those templates,

```text
C_native(S) >= 94,
```

regardless of how many additional legal paths `S` includes.

**Proof.** Let `U={4,5,6,7,8,9}` and `M={h in U: l_h=0}`. The all-covered hypothesis implies `M subset {h:b_h=1}`, and the low-count hypothesis gives `|M|<=4`. At least four late horizons are high-capable, so extend `M` inside that set to an exactly four-element set `A`. Choose one legal word per label of `B` for `h in A`, per label of `L` for `h in U\A`, two high words at H3 and four low words at H2. This selects `4+2+4*2+2*4=22` distinct legal words. Selection cannot add a sixth key or an extra native prefix. The 22-template lower bound yields the claim. QED.

**Exact Boolean-profile corollary.** Each late horizon has one of four statuses: neither, full-B only, full-L only, both. Of all `4^6=4096` six-horizon status profiles, exactly **483** satisfy the three late-horizon predicates above. Independently:

```text
483 = sum_{u+v+w=6; u+w>=4; v+w>=2} 6!/(u! v! w!),
```

with `u` B-only, `v` L-only and `w` both. The other 3,613 logical profiles require other tests; they are not certified feasible.

**Consequence for the original <=93-edge mother objective.** Any candidate inside this frozen model must violate at least one displayed Theorem-B signature-support hypothesis to escape the completed 22-template obstruction. Merely increasing the number of paths while retaining these supports cannot improve the 94-edge minimum.

## Executed finite evidence

Two independent local Python standard-library implementations were executed. They directly generated and checked **812,924 nonzero-label original words** at H2–H9 from the frozen DFA, across **294 count-admissible key/horizon pairs** (290 with nonzero labels). Each word was expanded to ordered signed native six-axis microsteps and checked for both Theorem-A identities. The strictly positive subspace contains **811,355** of these words across 270 pairs. The Boolean proof was checked for all 4,096 profiles by a fifteen-template enumeration and a separate multinomial calculation. The EC49FDN/EC49FEG explicit 22-word five-key witness was freshly re-expanded and its union of native signed prefixes was exactly **94**.

Reproducible inputs, local execution sources and report: `VERIFY_EC49FFC_COMPACT.py`, `VERIFY_EC49FFC.py`, `COMPACT_REPORT_EC49FFC.json` and `EXACT_REPORT_EC49FFC.json` (compact source and summary are also published under this directory). Historical dependencies: EC49FEO 15-template certificate at author commit `1df1dd9682b881ef6ebb3f96f599bf5ce3a849e4`, EC49FFB H7 23-word frontier at author commit `ef25dbe1a5518196d2e9cb57c6ff20e84cd1e44c`. The finite 22-template optimality inherits its existing author-side proof and review status; Theorem A and the dominance-selection proof are direct mathematical derivations.

## Next EC49FFD

Search **inclusion-minimal rank-nine terminal-label supports**, not simply larger path counts. Apply the Theorem-B support sieve and the already classified 23-word single-mixed-family certificates to exclude dominated profiles. For remaining minimal supports, test genuine five-key feasibility then exact signed native prefix optimization. Keep individual keys and native signed path prefixes intact; preserve frozen scientific input and current owner/CLAIM authority.
