# Stage500-B — Rightmost-h public-cursor repair for finite BRC futures

Date: 2026-11-07. Classification: AUTHOR_PROOF / EXACT_INTEGER_EXECUTED / INDEPENDENT_REVIEW_PENDING.

## Frozen sources and inherited frontier

Global science pin: \`bf84bd7c61a2444b59b1da96be57df0e9ae47e53\`; Enterprise Math science pin: \`2af3fc484eb11060b69e0afc1b562bcaf5ad1419\`; P000 source blob: \`bcc2590d3168a28f72e8b9f0f9b1f76faadcd488\`. Direct predecessor: Stage499-B commit \`3589ce2509d8f1091597750de3c2cbb19be5ea7f\`. Current behavioral rules independently read at global main \`efdcef2fa8a137ee4322fd0d7f2c3545e3714b50\`, Enterprise Math main \`c0aadcb644eed81558bc3e9df8cce71616fbacc2\`.

The parent problem is a typed, lossless compression of hidden signed-X6 directional history under declared future operations and observers. Stage499-B proved that a wholly original-tagged core can be compressed into F(core), with the final h+3 tagged tokens retained. Here the core may contain arbitrarily many public-source tokens; the rightmost h such tokens are enough for all futures of length ≤h under the stated grammar.

## Exact model

A token is (direction, source) with direction from 12 signed X6 directions A,...,L, carrying native displacement vectors ±e_1,...,±e_6, and source O (original) or P (public). A history is a nonempty finite token word w. Define F(w)=(D(w),E(w)), where D is six-component integer displacement and E has all 144 ordered consecutive direction-pair counts. Source tags are not directly observed. An action trace observes legality and F after every operation prefix.

The commands are: POP the final token; SET3C replace the third-last direction by C, preserving the source; INSERT2C insert a P-tagged C before the final two tokens (either length capped by precondition n<8 or uncapped); DELETE2 remove the second-last token; DELETE_LAST_PUBLIC remove the rightmost P-tagged token in the *entire* word. All commands preserve nonemptiness. This is the same grammar as Stage499-B.

For any nonempty u, |u|=1+Σ_ab E_ab(u). Both boundary directions are derived from F, because signed-X6 primitive vectors are distinct:
v(first(u))=D(u)-Σ_ab E_ab(u)v(b);
v(last(u))=D(u)-Σ_ab E_ab(u)v(a).
Consequently F(uv)=F(u)⊙F(v), where D adds, E adds plus the ordered boundary edge [last(u),first(v)], and F(empty) is the identity. The ⊙ operation is associative.

## Theorem 500.1 — Truncated provenance cursor

Fix h≥0, L=h+3. On histories w=c t with nonempty core c and fully tagged suffix t of exactly L tokens, let k=#P(c), r=min(k,h). Mark the rightmost r P-source tokens of c as P_1,...,P_r in left-to-right order. There is a unique decomposition

c=A P_1 B_1 P_2 B_2 ... P_r B_r

with each B_i an O-only run (possibly empty). If r=0, A=c. The initial A may contain P tokens only when k>h; its internal sources are deliberately not read. Define the cursor

K_h^P(w)=(F(A), (dir(P_1),F(B_1)),...,(dir(P_r),F(B_r)), t).

**For any two histories x,y in this domain, K_h^P(x)=K_h^P(y) implies x~_h y**, where ~_h is exact agreement of every command's legality and all F observations at each prefix of every common action trace of length at most h. This holds for both capped and uncapped INSERT2C variants.

### Proof

After j≤h legal commands represent the entire current history as an unchanged unknown A summarized by F(A), the remaining distinguished P markers with exact intervening O-run F summaries, and a completely explicit mutable tagged suffix t_j. At depth j<h its length satisfies |t_j|≥h+3−j≥4: each action reduces suffix length by at most one, and deletion of a public token from the core does not shorten the suffix. All POP, SET3C, INSERT2C and DELETE2 updates therefore target the suffix alone. Their legality, including n<8 for capped insertion, is determined from the exact total length contained in the summaries and suffix.

For DELETE_LAST_PUBLIC, if t_j contains P, remove the rightmost such suffix token. Otherwise its target, if available, is the rightmost surviving distinguished core P. Removing that marker joins its adjacent O-run summaries via ⊙, including the newly created boundary edge. If the removed marker was the leftmost distinguished one, join its right run to F(A). No unrepresented token is opened.

The only case where A might contain P is k>h. Then r=h and prior to a new action at depth j<h, at most j stored core P markers could have been removed; at least h−j≥1 distinguished P marker remains. Thus no new action can target any hidden P inside A. When k≤h, A contains only O tokens, so absence of distinguished core P markers certifies that the core has no public token. All legal actions are therefore reproduced with exact updated summaries. Associativity of ⊙ reconstructs exact F of the whole history after each prefix. Equality of K_h^P yields matching transition/observation trees by induction on j. QED.

The cursor contains at most h+1 summaries with 150 integer components each and a fully tagged h+3 suffix. Its direct representation uses
O(150(h+1)log_2(n+1)+h log_2 12+(h+3)log_2 24) bits
for n current tokens, hence O((h+1)log(n+1)+h) bits with this fixed twelve-direction alphabet. Its storage is independent of the total number k of public source tokens. Initial construction requires O(n) input processing. This is a *sufficient exact quotient*, with no assertion of global minimality.

## Proposition 500.2 — Sharp marker count for this truncation interface

For each h≥1, take U=AABA and V=ABAA. Tag the second token of U (respectively V) as P and all other gadget tokens as O. Add h−1 P-tagged C tokens and h+3 O-tagged C suffix tokens, producing X_h,Y_h.

F(U)=F(V) and both end in A, hence F(X_h)=F(Y_h). If only the last h−1 core P tokens are retained, then the compressed prefix is either U or V but their F summaries coincide, and the rest of the truncated signatures coincide. Apply DELETE_LAST_PUBLIC exactly h times: the first h−1 operations delete identical trailing public C tokens and have equal observations. The h-th deletes the second gadget token; the gadget values become ABA and AAA, which have unequal D and E. Thus their first differing observation on this trace occurs exactly at depth h. For this summary-and-last-P-markers representation, replacing h by h−1 is unsound for every horizon h≥1.

## Exponential family and exact execution

Let seven independent O-only blocks each be U or V, separated by three single P-tagged markers (B,C,A), and followed by the same O-only C^(h+3) suffix. For h=1,2,3 all 2^7=128 distinct histories have the same K_h^P. At h=1 and h=2 the ignored prefix A contains public markers: this is genuine source-sensitive compression, not merely Stage499-B's all-original core.

The attached exact Python stdlib checker is packaged losslessly in deterministic gzip+base64 form as \`REPRO_STAGE500B.py.gz.b64\`, with source SHA256 \`b4bfe28d72e5f31a6483bbb83dd7fe5208d15ea7943c8d9e6c48e08edf922867\`. Restore and execute in this directory:

\`\`\`sh
python3 -c 'import base64,gzip,pathlib; p=pathlib.Path("REPRO_STAGE500B.py.gz.b64"); pathlib.Path("REPRO_STAGE500B.py").write_bytes(gzip.decompress(base64.b64decode(p.read_text())))'
python3 REPRO_STAGE500B.py
\`\`\`

Exact saved stdout: \`REPRO_STAGE500B_EXECUTED.json\`. The actual executed test performed 908 history audits, 34,653 legal action-tree prefix states, 36,660 transition comparisons, 384 family-history entries, 762 full trace-family comparisons, 343 path-concatenation associativity checks, and verified sharpness for h=1,...,5. All assertions passed. Tests include both capped and uncapped insertions and multiple tagged source/direction patterns; the general theorem is proved independently of the finite tests.

BRC reuse: ordered signed-X6 path populations and multiplicities are retained, with exact F-valued observer and future operation semantics. The repair permits arbitrary deep hidden provenance so long as the final h removable core P markers are distinguished. This is a purely typed static path-history quotient, not a proposed physical time dynamics.

## Next mathematical question

Stage501-B: extend DELETE_LAST_PUBLIC to DELETE_KTH_PUBLIC_FROM_RIGHT(k) for k≥2 and test whether the number of core provenance markers sufficient for a horizon h is kh, or a sharper function of source density and insertion behavior. Independently benchmark exact-bit and peak-memory costs of Stage494 recount vs Stage495 one-solve Euler–BRC ranking on identical 144-active-edge heterogeneous inventories. Native claim/session and independent Driver review remain governed by the actual live service.