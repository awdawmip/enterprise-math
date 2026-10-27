# Stage186 — author-level exact full-real optimality theorem

Research object: external ternary IID ordered-history stopping with horizon N=14, P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6). **AUTHOR_EXACT** with local executable exact certificate, not formally admitted or native P000 X6. 2026-10-27.

Define eP=P(decide Q), eQ=Q(decide P), tP=E_P T, tQ=E_Q T, and V14(alpha)=min_{eP,eQ<=alpha}max(tP,tQ), allowing every ordered-history-dependent randomized strategy that stops by time 14.

## Exact theorem

At the previously author-proved Stage185 boundary:
\[
\alpha_{185}=\frac{3684877789469437643}{10517860061584293888},\quad
V_{185}=\frac{2399458174541646935}{219122084616339456}.
\]
Put \(K=L=2558956801176/14133016123\) and
\(H=53350630346247249956056072189/387106994348511975111131136\).
For **all real**
\[
0\le\delta\le
\frac{15336010242985951840656073}{556045820435270953613773504512},
\]
the exact value is
\[
\boxed{V_{14}(\alpha_{185}+\delta)=V_{185}-\frac{5117913602352}{14133016123}\delta}.
\]
The new endpoint is
\[
\alpha_{186}=\frac{880819177025099228444495}{2513951372772311530733568},\qquad
V_{186}=\frac{15842003227930467204041319427}{1448035990716851441702535168}.
\]
For alpha strictly larger than alpha186, the **same Stage186 supporting line** is strictly below the true value.

## Global Bellman dual certificate

Represent a history by count state s=(n,a,b), with a count of symbol 0, b count of symbol 1. Every such history has likelihood ratio
\(\ell(s)=Q(\omega)/P(\omega)=2^{a+b}/3^a\).
For n<14 define the reduced-rational Bellman recurrence
\[
h(s)=\min\{K\ell(s),\, L,\, 1+\sum_{i=0}^2 P_i h(\mathrm{child}(s,i))\}.
\]
At n=14 the continue option is omitted. The 680 count-states have exactly two ties: R=(5,2,0) offers P/continue, and Z=(14,0,0) offers P/Q. All other 1,238 action gaps are strictly positive, minimum
\(8013894983737/219796666744896\). The root equals H above.

Backward induction on every *ordered history*, not merely count policies, yields
\(t_P+K e_Q+L e_P\ge H\) for any randomized stopping strategy. Hence
\[
V_{14}(\alpha)\ge H-(K+L)\alpha.
\]

## Exact primal attainment with two randomizations

Let r be the P-decision probability at R (otherwise continue) and z the P-decision probability at Z (otherwise decide Q). No history from R can reach Z: R has first-symbol count 2 while Z has count 0. Z cannot precede R because Z is terminal. Thus their intervention cones are disjoint.

Write O=(eP,eQ,tP,tQ). Exact suffix DP and independent unmerged ordered-history integer-weight DFS give
\[
\begin{split}
O_{00}&=(614327151481393049/1752976676930715648,\
112420430604569/320979616137216,\
2399458174541646935/219122084616339456,\
285698065347565/26748301344768),\\
\Delta_R&=(-4034771294375/4565043429507072,\
5111681875/3343537668096,\
-22213166676875/190210142896128,\
-13144174375/208971104256),\\
\Delta_Z&=(-6103515625/78364164096,\
6103515625/78364164096,0,0).
\end{split}
\]
Then O(r,z)=O00+r DeltaR+z DeltaZ, without mixed term. First-hit ordered-path counts are 10 at R and 1 at Z; first-hit masses under P/Q are (625/6912,625/15552) at R and (6103515625/78364164096,6103515625/78364164096) at Z.

The balance condition eP=eQ gives the **exact** relation
\[
\boxed{
r(z)=\frac{1085119418920651}{12688036931760000}
-\frac{10240000000000}{158600461647}z
}
\]
with both coins legal precisely for
\[
0\le z\le \frac{1085119418920651}{819200000000000000}.
\]
At z=zmax the R coin is r=0 and the complete exact Stage185 endpoint is recovered. At z=0 the R coin is positive and strictly <1, and the resulting endpoint is alpha186,V186. Thus the *terminal Z coin reaches the boundary z=0*, rather than R saturating.

For both endpoints direct rational verification gives eP=eQ=alpha, tP>tQ, tP+K eQ+L eP=H, monotone alpha and opposite monotone tP. All observables are affine along this real stochastic coin segment, so the endpoint checks imply optimality for the **entire real interval**, including irrational alpha.

Even with history-dependent tie coins, at each fixed count state all ordered histories have *equal P-weight and equal Q-weight*, by the IID products. Thus the relevant errors and expectation observables depend on a single effective coin for that state. This is a scope-limited sufficiency result for the finite IID observables only; it never erases native BRC signed or provenance information.

## Right-sharpness proof

The finite history-tree policy space is compact; the infimum is attained. For alpha>alpha186, equality to the Stage186 line would force equality in
\[
\max(t_P,t_Q)\ge t_P\ge H-Ke_Q-Le_P\ge H-(K+L)\alpha.
\]
Since K,L>0, this implies both eP=eQ=alpha and Bellman-minimizing actions at every positive-mass history. All 1,238 strict gaps force the fixed non-tie policy, leaving the R/Z effective coins. Their balanced legal interval has alpha<=alpha186, contradiction. The Stage186 support line is therefore strictly suboptimal to its right, without proving any Stage187 primal formula.

## Exact computational and successor evidence

Every state/action computation used Fraction exact arithmetic. Four deterministic corner vectors agree between suffix DP and full ordered-history DFS, visiting respectively 207250,207250,196750,196750 unmerged nodes (808000 total). All 13 local checks pass. The actually executed longer verifier, JSON certificate and full logs are preserved in the portable bundle EM_STAGE186_AUTHOR_EXACT_PORTABLE_20261027.zip; this GitHub note has the full proof and essential exact certificates.

Stage187 dual-only tangent: dK=-19366902213/33499918336, dL=-1, step=591176206447109672064/77292015228163893061. Candidate K187=30912926277555/175004717024, L187=948381852216/5468897407, H187=20011003723884904564897099291/149794525046841680093773824. Ties R=(5,2,0) P/C and T=(13,6,4) Q/C, all 1238 other gaps strictly positive, min 464592386670727/29031182497677312. **No Stage187 primal claim**. R is a *possible ancestor* of T (exactly four new symbol-0 and four symbol-1 observations in eight steps), so next work must inspect actual history reachability and any coin cross term before reusing an affine-cone argument.

Source/authority pins: Stage185 immutable authored parent commit 5611857ffef2eeb1de8d814b9a13af9efa6c670f; GLOBAL_KNOWLEDGE_V1 current verified main snapshot bb0c0f4538fbc3ea90fc4118ecc8ce88f09f17bc; Enterprise Math initial Source main snapshot 8d749d17162ffa5da8886b9883cc97db695b1640. GitHub identity awdawmip has write permission, but native em_control_tasks returned CONTROL_QUOTA and em_session_start returned STATIC_READONLY_SCOPE_DENIED/operation_sent=false, so live canonical owner, CLAIM and independent Driver admission remain unknown/ungranted. This is external mathematical evidence, not a native X6 Cell theorem.