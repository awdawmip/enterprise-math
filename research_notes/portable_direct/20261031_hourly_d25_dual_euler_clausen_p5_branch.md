# D25/LIFT — dual Euler–Clausen p≡5 mod6 polynomial factorization

2026-10-31 Asia/Hong_Kong, research lane \`chatgpt-research-hourly-enterprise-math-20260923\` (not maintenance). Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific Source \`c47e13e4aba0e006366f989d6334d443f6333ae3\`; P000 ACTIVE_LOCKED unchanged. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** This is external p-adic mathematics, not P000 native X6 transfer, native task execution, or a proof of the original p³ LIFT target.

## A complete finite-field polynomial identity

For every prime \(p=6m+5\ge5\), put

\[
a_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3},\quad
G_m(z)=\sum_{k=0}^{m}\binom{m}{k}\binom{2m+1}{k}z^k.
\]

**Theorem (coefficientwise over \(\mathbb F_p[X]\)):**

\[
\boxed{\sum_{n=0}^{p-1}a_n X^n
\equiv (1-X/2)\,G_m(X/2)^2\pmod p.}\tag{1}
\]

**Proof.** Classical Clausen and Euler hypergeometric transformations give in \(\mathbb Q[[z]]\)

\[
{}_3F_2(\tfrac12,\tfrac13,\tfrac23;1,1;z)
={}_2F_1(\tfrac16,\tfrac13;1;z)^2
=(1-z)\,{}_2F_1(\tfrac56,\tfrac23;1;z)^2.
\]

For \(p=6m+5\), \(\tfrac56\equiv-m\) and \(\tfrac23\equiv-(2m+1)\pmod p\). The first \(p\) Gauss coefficients reduce to \(\binom mk\binom{2m+1}k\) for \(0\le k\le m\) and zero for \(m<k<p\); all factorial denominators are p-units. Thus up to degree \(p-1\) its transformed square equals \((1-z)G_m(z)^2\). The latter has degree \(2m+1<p\). Substituting \(z=X/2\) gives the original coefficients exactly. QED.

Classical external sources: NIST DLMF Clausen identity §16.12.2, https://dlmf.nist.gov/16.12.E2 ; Euler transformation §15.10.11, https://dlmf.nist.gov/15.10.E11 . Originality of the transformation itself is **not** claimed. The scoped application and explicit original-coefficient observer are the project-level derivation.

## Original weighted readout and a two-port first-digit observer

With \(\theta=z\,d/dz\) and \(W=1+6\theta\),

\[
W[(1-z)G_m^2]=(1-7z)G_m^2+12z(1-z)G_mG_m'.
\]

At original \(X=1\), i.e. \(z=1/2\), the original signed 216 sum satisfies

\[
\boxed{A_p=\sum_{n=0}^{p-1}(6n+1)a_n
\equiv \tfrac12 G_m(\tfrac12)[6G_m'(\tfrac12)-5G_m(\tfrac12)]\pmod p.}\tag{2}
\]

This factorization is a universal theorem in the displayed p≡5mod6 family. **It does not by itself prove that either port vanishes for every prime**, nor does it establish the exploratory \(A_p\equiv-p\pmod{p^3}\). Keep the signed ports \((G,G',6G'-5G)\), original weighted operator, source index and observer precision separate under BRC; the final scalar cannot reveal which vanishing mechanism was used.

## Executed finite evidence and still-open character split

A self-contained Python stdlib program computes original \(a_n\) by its integer recurrence **without using the claimed Clausen transformation**, constructs \(G_m\) from integer binomials and checks every coefficient up to \(X^{p-1}\), then independently tests (2). Executed for **277 primes \(p\equiv5\pmod6,\ p<4000\)**: **506,795 exact coefficient comparisons** and 277 weighted readouts passed. Program marker:

\`PASS_D25_DUAL_EULER_CLAUSEN_P5_POLYNOMIAL_EXACT\`

Observed — **finite conjectural pattern, not proved**: for p mod24=5 or 11, \(G_m(1/2)\ne0\) and \(6G_m'(1/2)-5G_m(1/2)=0\) (70 and 71 cases); for p mod24=17 or 23, \(G_m(1/2)=0\) and the Robin port is nonzero (68 and 68 cases). In this window the split corresponds to quadratic character \((2/p)=-1\) for Robin and \(+1\) for Gauss zero. Anchor residues (p,m,G,Robin): (5,0,1,0), (11,1,8,0), (17,2,0,1), (23,3,0,6), (29,4,25,0), (41,6,0,7), (53,8,20,0). No finite check gives universal vanishing or the frozen p³ theorem.

Verifier path: \`research_notes/portable_direct/d25_dual_euler_clausen_negative_branch_check_20261031.py\`. Executed local SHA256: \`6a91edfdcb93eca71397336570a14fa28d4c1229c52e10ac0b93827d87fee123\`. Run log SHA256: \`9ffb3153cd52b4c454dc064b955ac818de774ae01acf63e5c51d432eec781261\`. No Lean or native H0/B0/divided-power/semilinear-Frobenius experiment.

## Frontier and precise next action

Prior GH-174 mirrored p≡1mod6 case, earlier uniform valuation/precision-prefix and another lane's first-digit bridge are **consumed**, not re-credited. The new p≡5mod6 identity is an exterior comparator; frozen D25/LIFT mathematical obligation remains prove the **complete signed \(C+L-J+I\equiv0\pmod p\) for all \(p\equiv13,19\pmod{24}\)**. Next discriminating portable question: derive/prove or refute the p≡5mod6 quadratic-character selection by finite-field symmetry, Gauss/Jacobi sum or CM special-value method, then test whether the typed-port mechanism transfers to the original frozen p³ signed bridge. Maintain original 216 normalization, source pins, signed contributions and valuation walls.

Native gateway 0.6.11 read for this run: \`research_authority_granted=false\`, \`executor_binding_configured=false\`, active quota 5/5, control \`CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED\`. Historic own recovery #6424 and continuation #6425 had \`execution_authorized=false\`; those are historical reads, not a current owner claim. No service session_start, CLAIM, OPEN, Source checkpoint, Result, review, or admitted activity was performed; protected staging and maintenance conversation untouched. Native restoration is assigned to \`awdawmip/enterprise-math#1558\` and original p373 experiment to #1559. When the current Source allows: own exact recovery/continuation → lawful identity/session transition → typed successor CLAIM/open → fresh Source authority check → truthful native checkpoint. Scheduler unchanged.