# R158 — Exact two-sided residue certificates for eventual Sturmian fiber appearance; complete m≤64 window

Date: 2026-11-15 (Asia/Shanghai). Scientific status: **AUTHOR_PROVED (general exact residue theorem); EXACT_FINITE_ENUMERATION (m≤64); NOT_REVIEWED**. This is the external scalar tied-phase Sturmian S23 observer, not a native X6/BRC embedding. Continue the existing R146–R157 scientific input pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; no source premise has been rebased.

Dependencies: R146 open-cut count identity, R152B first-period theorem, R157 exact Farey-cell enumeration/completeness argument and all-length extremal lower bound. Source: R157 pinned commit `faaf0e42eac30d3a2cafdbefe967a0785c560b2d`, `research_notes/portable_direct/R157_EXTREMAL_FAREY_THRESHOLD_M32_20261115.md`.

## 1. Exact model and question

Let (a/b<c/d) be reduced rationals, (b,d>0), (U,V∈\mathbb Z), and (D=bc-ad>0). For integer (L≥1), define the integer-phase count
[
C(L+1)=\left\lceil\frac{Lc-V}{d}\right\rceil-\left\lfloor\frac{La-U}{b}\right\rfloor-1.
]
For an admitted finite Sturmian word, ((a,b,c,d,U,V)) is the exact signature obtained by scanning its factor slopes and prefix cuts as in R157. Its permanent threshold (T_w) is the first (K≥2) for which (C(K')>0) for all (K'≥K).

R152B determines (T_w) by scanning up to (operatorname{lcm}(b,d)). We derive an exact **O(min(b,d)) residue-class certificate**, without any periodic scan or floating point.

## 2. Theorem R158A — left-endpoint exact arithmetic progression certificate

For each residue representative (t∈\{1,\ldots,b\}), set
[
r_t=(at-U)\bmod b\in\{0,\ldots,b-1\},\qquad
J_t=\left\lfloor\frac{bd+bV-d(U+r_t)-Dt}{Db}\right\rfloor.
]
Then for **all integers** (j≥0),
[
\boxed{C(t+jb+1)\le0\quad\Longleftrightarrow\quad j\le J_t.}
]
Therefore the entire set of nonpositive positions is the disjoint finite union
[
\boxed{\{L≥1:C(L+1)\le0\}=
\bigcup_{t=1}^{b}\{t+jb:0\le j\le J_t\}.}
]
An empty progression is understood when (J_t<0). Consequently, with
[
M=\max\bigl(\{t+bJ_t:1≤t≤b,\ J_t≥0\}\cup\{0\}\bigr),
]
the exact permanent threshold is (oxed{T=M+2}).

**Proof.** Set (x=(La-U)/b), (y=(Lc-V)/d), (r_L=(La-U)\bmod b). Then
[
y-\lfloor x\rfloor
=y-x+\frac{r_L}{b}
=\frac{LD+d(U+r_L)-bV}{bd}.
]
Since (C(L+1)=\lceil y-\lfloor x\rfloor\rceil-1), the count is positive if and only if the displayed rational is greater than 1. Thus
[
C(L+1)\le0\iff LD\le bd+bV-d(U+r_L).
]
For (L=t+jb), (r_L=r_t), and rearrangement gives (j≤J_t). The union and threshold follow. The argument also permits arbitrary integer cuts (U,V), including small (L) with negative algebraic counts; it uses the exact criterion (C>0). QED.

## 3. Theorem R158B — symmetric right-endpoint certificate

For each (t∈\{1,\ldots,d\}), let
[
s_t=((ct-V-1)\bmod d)+1\in\{1,\ldots,d\},\qquad
J'_t=\left\lfloor\frac{b s_t+bV-dU-Dt}{Dd}\right\rfloor.
]
Then
[
\boxed{C(t+jd+1)\le0\iff 0≤j≤J'_t.}
]
The analogous maximum of (t+dJ'_t) gives exactly the same (M). Selecting the smaller of (b,d) thus computes the threshold with (O(\min(b,d))) exact integer operations; this counts arithmetic operations, not bit complexity.

**Proof.** Write (y=(Lc-V)/d). The quantity (s_t/d=y-(\lceil y\rceil-1)) lies in ((0,1]), with (s_t=d) when (y) is integral. Since (C=\lceil y\rceil-\lfloor x\rfloor-1), (C>0\iff x<\lceil y\rceil-1=y-s_t/d). Multiply (y-x>s_t/d) by (bd), use (y-x=(LD+dU-bV)/(bd)), then group (L=t+jd). QED.

**Information semantics.** These are complete certificates for the declared scalar observer ((a/b,c/d,U,V)\mapsto\{C(K)>0\}_{K≥2}). They are not reconstruction certificates for the original symbolic word; R153–R156 exhibit distinct words with identical signatures.

## 4. Uniform width cutoff and finite evidence

Define the elementary length cutoff
[
H=\left\lfloor\frac{bd+bV-dU}{D}\right\rfloor.
]
For (L>H), the open intercept interval (((La-U)/b,(Lc-V)/d)) has length (>1), so (C(L+1)>0). Thus scanning beyond (H) is unnecessary; R158A/B are sharper and directly calculate the last nonpositive position.

**Complete exact finite window:** For each (1≤m≤64), enumerate every finite Sturmian word by rational midpoint sampling in every Farey cell of order (m) and each rational intercept cell. The classical mechanical-word construction covers the feasible word set: all slope-support endpoints have denominator at most (m), and the intercept word changes only at the finitely many (x=(-j\theta)\bmod1). The executable checker uses integers only, rebuilds factor inequalities and cut extrema independently for every generated word, and groups identical signatures.

For all (5≤m≤64), exhaustive exact calculation gives
[
T(m)=(m-2)\left\lfloor\frac{m-1}{2}\right\rfloor+1;
]
the only maximisers are (01^{m-2}0) and (10^{m-2}1); all observed signature fibers have cardinality at most 2. The first 32 lengths reproduce R157. Newly checked (33≤m≤64) contain **434,522 words**, **398,594 signatures** and **35,928 doubleton signature fibers**; total (1≤m≤64) is **466,502 words**, **427,920 signatures**, **38,582 pairs**. For (m=64), (T(64)=1923), with 27,834 words and 25,490 signatures.

A second finite pattern: for each (5≤m≤64),
[
\boxed{\max_w H_w=\frac{(m-2)(m-1)}2-1.}
]
This is a **finite-window fact**, not an asserted all-length theorem. It suggests a precise separate conjecture: prove the same width-envelope identity for every (m≥5). That would immediately prove the saturation upper bound for **all odd lengths**, since for odd (m), the right side plus 2 equals the proposed (T(m)). Even lengths then require the genuinely modular improvement furnished by R158A/B.

## 5. Recalculation and provenance

- Files: `R158_residue_check.py` and `R158_window_1_64.csv` adjacent to this note.
- Full finite enumeration: 64 lengths, with left/right residue thresholds checked equal for every signature; each signature's last nonpositive position was independently checked by a reverse direct scan (earlier exact batch) and a focused direct scan in the consolidated checker (all m≤20; deterministic sample above 20).
- Unrestricted observer check: **9,108** combinations, all reduced (0≤a/b<c/d≤1), (b,d≤8), (U,V∈[-2,3]), with left/right residue certificates equal to direct enumeration of all nonpositive (L).
- Every integer and midpoint computation is exact. The reported full-window statements are exhaustive **for the stated finite domain**; the symbolic residue theorems are all-parameter author-side proofs.
- The independent mathematical review remains `NOT_REVIEWED`.

## 6. Remaining mathematical frontier

1. Prove/disprove the general width-envelope inequality
[
\frac{\max_i(p_i-i\beta)-\min_j(p_j-j\alpha)}{\beta-\alpha}
\le \frac{(m-2)(m-1)}2-1
]
for all admitted finite Sturmian words. This is equivalent to the conjectured uniform cutoff before flooring. The extremal (01^{m-2}0) and (10^{m-2}1) attain equality; all m≤64 were checked.
2. For even (m), use the R158 modular residue certificate to rule out the (O(m)) residual positions between the width cutoff and the claimed threshold.
3. Classify all-length signature fibers above cardinality 2, retaining word/source identity when the observer requires it.

Control: On 2026-11-15 03:10 +0800 the original native exact-task lookup for `RS-S23-AV` returned `SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY` on Source `dba8eed3b25b2001c9b1357c292d85acf3147efd` (absence-only, no full owner projection). Existing historical Researcher-ID `EM-DIRECT-DAF2F3` is provenance, not current execution capability. This independent Source proof publication does not assert a formal CLAIM, Result or independent review.
