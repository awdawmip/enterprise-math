# EC49FXU — Every frozen C11 product is realized by a genuine Farey anchor

**Date:** 2026-11-23 (Asia/Shanghai). **Frozen scientific pin:** BRC16943, unchanged.
**Evidence status:** AUTHOR_PROVED / EXACT_EXHAUSTIVE_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
**Scope:** positive, reduced rational anchors with determinant-minus-one Farey branches, their *normalized* scalar C11 traces and indexed reflection spectra. This is an auxiliary arithmetic observer; no native Heartbeat-X6 dynamical claim is made.

## Parent sources and genuinely new question

- EC49FWS, frozen parent \`awdawmip/enterprise-math@95507f064ee46910b32e26d1c49e6df4a05b84fc:research_notes/portable_direct/EC49FWS_FAREY_ONE_HOLE_FIBER_OBSERVER_THEOREM.md\`.
- EC49FWQ 50-factor census: \`awdawmip/enterprise-math@d091c8f2757f67c18be8056ae976b1e092a21098:research_notes/portable_direct/EC49FWQ_BLIND_FACTOR_FULL_SUPPORT_PROBES_THEOREM.md\`.
- EC49FXT two-sided reflection: \`awdawmip/enterprise-math@c93c05b18957fd0e75375afce7e3cd5bc42d0c70:research_notes/portable_direct/EC49FXT_TWO_SIDED_FAREY_REFLECTION_THEOREM.md\`.

FWS embeds actual anchors into an **enlarged** 600-state product model but left open whether all product states, especially the three indispensable equal-spectrum ambiguity witnesses, are realizable by actual anchors. This note settles that exact reachability question.

## Definitions and normalization

Use the original 44-residue frozen predicate \(P_{10}\) with slope table \(\{(0,0):\{3\},(0,1):\{0,3,4,5\},(1,0):\{2,3,4,5\},(1,1):\{2,3\}\}\), and

\[
C_{11}(h,n)=P_{10}(h\bmod10,n\bmod10)\mathbf 1_{9h+10n\not\equiv0\pmod{11}}.
\]

Choose integers \(a,c>0\) with \(\gcd(a,c)=1\), and \(b=a+c\). Put \(e=a^{-1}\pmod b\), with \(1\le e<b\), and

\[
h_0=(ae-1)/b,\quad n_0=e-h_0,\quad
X(t)=(h_0+at,n_0+ct).
\]

Then \(c h_0-a n_0=-1\), and the genuine anchor is \(q=a/b\). Follow the *same* FWQ/FWS mod-10 normalization: for direction \((a,c)\bmod10\), pick the lexicographically first \((x,y)\in\{0,\ldots,9\}^2\) with \(cx-ay\equiv-1\pmod{10}\); the unique \(t_0\in\{0,\ldots,9\}\) satisfies \(X(t_0)\equiv(x,y)\pmod{10}\). Define

\[
U(t)=P_{10}(X(t_0+t)),\qquad
V(t)=\mathbf1_{9h(t_0+t)+10n(t_0+t)\not\equiv0\pmod {11}}.
\]

The 10-bit support \(U\) belongs to the frozen 50-mask census. \(V\) is either full or is missing exactly one of the 11 columns. The indexed 110-bit word is \(W(t)=U(t\bmod10)V(t\bmod11)\).

## Theorem — exact surjectivity onto all 600 frozen product states

**Every** \(W=U\times V\), with \(U\) any of the original 50 normalized ten-bit masks and \(V\) full or missing exactly one mod-11 column, equals the normalized C11 trace of some genuine reduced positive rational anchor \(a/(a+c)\).

More strongly, all 600 states possess witnesses with

\[
\boxed{1\le a\le79,\quad 1\le c\le79,\quad \gcd(a,c)=1.}
\]

Within this *specified square search and normalization*, the bound 79 is sharp: the square \(1\le a,c\le78\) realizes 599 states. Its sole missing state is \(U=788\), missing column \(z=5\), first witnessed by \(a=28,c=79\), hence \(q=28/107\), \(t_0=8\).

### Complete finite proof and correctness of the certificate

The companion standard-library Python file performs an exhaustive, fully deterministic integer certificate:

1. Rebuild all 72 primitive mod-10 directions, the lexicographic determinant-minus-one representative of each, and the resulting **exactly 50** distinct frozen \(P_{10}\) words. This fixes normalization independently of witness choice.
2. Enumerate every pair \(1\le a,c\le79\) with gcd 1. Compute the unique determinant-minus-one canonical base using the modular inverse \(a^{-1}\pmod{a+c}\), its normalization shift \(t_0\in[0,9]\), the exact ten-bit word and the full/one-hole mod-11 factor.
3. Collect distinct ordered pairs \((U,V)\). There are **600**. Since the frozen ambient family has exactly \(50\cdot12=600\) possible pairs, this exhausts that family and proves surjectivity. Repeating on the whole 78-square yields exactly 599 and locates the single omitted state.
4. For the *first actual anchor witnessing each of the 600 states*, directly evaluate original \(C_{11}(X(t_0+t))\) and \(U(t\bmod10)V(t\bmod11)\) at every \(t=0,\ldots,109\). All **66,000** equalities hold. These checks do not substitute an interpolated mask for the original \(P_{10}\) predicate.
5. Independently reconstruct the indexed reflection spectrum from the identity
   \[
   D_{U\times V}(s,t)=2\bigl(|U||V|-|U\cap(s-U)|\,|V\cap(t-V)|\bigr),
   \]
   for all \((s,t)\in\mathbb Z/10\times\mathbb Z/11\), using exact cardinality counts. The census has **478** distinct spectra: **356 singleton** and **122 doubleton** fibers, matching the frozen FWS population.

The finite loop bounds, predicate, normalization, integer divisibility and exact witness list are all included in the accompanying script and JSON output; this is an exhaustive finite witness proof for the stated 600-state domain, not probabilistic testing.

## Corollary — genuine-anchor sharpness of FWS fixed-site observation costs

Use the **same observer information model as EC49FWS**: before any Boolean probes, the observer sees the complete indexed reflection-defect spectrum, does not receive the hidden anchor \(a/b\) or affine origin, and must distinguish its remaining normalized C11 product states with minimum Hamming separation \(r\) under an adversarial erased mod-11 factor. Probe sites are fixed independently of the spectrum.

Because the image of actual anchors onto \((U,V)\) equals all 600 frozen products, the FWS lower-bound ambiguity pairs and upper-bound layouts are **both attained by genuine anchors**. Consequently, for \(1\le r\le10\),

\[
\boxed{N_{\rm fixed}^{\rm genuine}(r)=3(r+1),\qquad
\#\mathrm{Opt}_{\rm genuine}(r)=\binom{11}{r+1}^{3}16^{r+1}.}
\]

Here the cost counts Boolean readings at physical CRT sites, *not* the separately studied coupled two-bit physical activation in EC49FXJ–FXS.

Explicit actual-anchor equal-spectrum doubletons for the three disjoint minimal difference supports (same missing column in each pair):

| Minimal support | Product words and missing column | Genuine anchors \(q\), shifts \(t_0\) |
|---|---|---|
| \(\{1,4,6,9\}\) | \(U=447,1005;\ z=7\) | \(1/2,\ t_0=0;\ 13/66,\ t_0=6\) |
| \(\{2,7\}\) | \(U=367,491;\ z=6\) | \(1/8,\ t_0=0;\ 23/58,\ t_0=3\) |
| \(\{3,8\}\) | \(U=701,949;\ z=3\) | \(1/6,\ t_0=0;\ 7/46,\ t_0=5\) |

The complete seven difference supports have doubleton multiplicities \(24,24,24,13,13,12,12\) (122 in total); the script records the exact labels. For any fixed probe layout, the adversary may choose one of the genuinely realized missing-column variants, so the original FWS counting lower bound now applies to actual-anchor images.

**Information-scope boundary:** Revealing the exact anchor and normalization to the observer would give extra side information and change the classification task. Likewise, the two-sided reflection \(w_+(s)=w_-(-s-1)\) uses the appropriate origin relation; unknown origins remain informative provenance. The theorem proves reachability of the full *coarse normalized product image*, not independence of anchor, height, branch, rational neighbor values and original X6 state.

## Interpretation, provenance and next scientific question

Actual-anchor existence alone cannot reduce the previous fixed-site budget, because every coarse product state occurs. A stricter model must retain further jointly observed information — for example the anchor residue or height, cross-time predecessor, branch/origin or a native typed X6 transition — and compute its fibers before claiming an improved observer.

Exact next inquiry: condition the same 600-state genuine-anchor witness population on a declared, nontrivial **observable** of \((a,b,t_0,H,\mathrm{branch})\), derive the resulting indexed-spectrum fibers, and quantify whether the robust fixed-site cost decreases. Choose an observable whose acquisition cost is included; avoid treating hidden anchor labels as free information. Retain P000, ACTIVE residual/worldview conditions and the frozen BRC16943 scientific premise without a native-dimensional reinterpretation.

Publication of this proof and finite certificate is not a formal Task CLAIM, independently accepted Result or Review.
