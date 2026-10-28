# D25 — unramified half-slope Frobenius: even-rank lattice law and p-adic second-digit precision

2026-10-28, on-hour TASK_RESEARCH. **AUTHOR-SIDE / EXACT CONDITIONAL THEOREMS / SIX EXECUTED INTEGER CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED**.

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen **scientific** Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Ordinary-control logical Research lane: chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance lane chatgpt-hourly-enterprise-math-20260921. No current Source session/CLAIM/run is asserted.

## The actual scientific need and narrow hypothesis

Existing [native H0/B0 support #1559](https://github.com/awdawmip/enterprise-math/issues/1559) requires the original p=373 divided-power [X]U mod 373², module rank, native Frobenius direction/eta, complete signed odd Green/Hesse, original κ and Delta−R, and reproducible raw sources. The prior [rank-one parity no-go](https://github.com/awdawmip/enterprise-math/blob/4eab4f4b0d65708233ab87bd7477b896aaccc24e/research_notes/portable_direct/20261028_onhour_d25_native_unramified_rankone_parity_no_go.md) excludes a free unramified *rank-one* semilinear model, conditional on a unit first square digit. This note proves the **all-rank invariant** and a separate **precision impossibility**, without redoing that proof or replacing the native benchmark.

Let p>2; let O be an unramified quadratic complete discrete valuation ring over Z_p, with residue field k=F_{p²} and involution σ. Let L=O^r (r>0), A an integral r×r matrix, F(x)=Aσ(x), and assume the **conditional** measured same-operator square

(A)    A σ(A) ≡ p U (mod p²), with U mod p invertible in GL_r(k).

U may be a matrix; its being scalar is **not** presumed. No evidence currently establishes (A) for the actual frozen H0/B0. The coefficients below are external arithmetic, not native P000 six-axis coordinates.

## Theorem I — all-rank parity and mod-p image=kernel

Under (A), **r is even**, rank_k(F mod p)=r/2, (F mod p)²=0 and image(F mod p)=kernel(F mod p). Thus, if an authenticated original-class native operator of free rank 2 satisfies (A), its mod-p rank is **exactly 1**, and an odd-rank free unramified model of *any* rank is excluded. Unlike the predecessor result, this statement applies to every r.

**Proof.** Choose any actual integral lift of A mod p² to O. Its product Aσ(A) is divisible by p, and B=Aσ(A)/p is integral with B mod p=U mod p invertible. Thus B is in GL_r(O), so F²(L)=pB(L)=pL **exactly**. Set M=F(L). F becomes invertible over the fraction field, is injective on L, and induces a σ-semilinear isomorphism L/M → M/F(M) = M/pL. Hence the O-lengths of L/M and M/pL agree. Because their sum is length(L/pL)=r, both have length r/2: r is even. As pL⊂M, the vector space M/pL is precisely im(F mod p), hence its rank is r/2. Also Fbar²=0, so im(Fbar)⊆ker(Fbar) and the two have the same dimension r/2; equality follows. QED.

**Sharpness.** For any even r=2s, the direct sum of s copies of A=[[0,p],[1,0]] with σ fixing integer entries obeys Aσ(A)=pI and has rank r/2 modulo p. This is a toy existence witness, **not** a native H0/B0 matrix.

**Optional scalar specialization.** If the measured same-operator square in (A) is further *proved* scalar U=uI, then applying σ and associativity gives p(u−σ(u))A=0 mod p². Because A mod p has positive rank, u mod p is σ-fixed. For target primes p≡13,19 mod24, O/p²=(Z/p²)[T]/(T²−2) and σ(T)=−T, so the *scalar square-unit's* T coefficient must vanish modulo p. No such assertion is made about the native odd Green/Hesse branch or [X]U, whose operator type is unverified.

## Theorem II — one p-adic digit is lost by normalized squaring

Suppose, **only after authenticating its definition**, a proposed native output U_F is derived as F²/p from an integral F. Knowing F mod p² and F² mod p² is **insufficient** to determine U_F mod p². One may compute F (hence F²) through p³, directly read U_F mod p², or prove an applicable canonical-lift constraint. A mod-p² Frobenius matrix alone cannot certify the requested two digits after dividing by p.

**Constructive proof retaining signed source.** For c,d∈Z_p, let v=1+p(c+dT) and

A_(c,d) = [[0, p v],[1, 0]],    σ(T)=−T.

All A_(c,d) agree modulo p², have rank 1 mod p, and A_(c,d)σ(A_(c,d))≡pI₂ mod p². Yet their full integral squares are p diag(v,σ(v)). Dividing by p gives

U_(c,d)=diag(1+p(c+dT),1+p(c−dT))  mod p²,

which varies by p times both a **fixed** and a **signed anti-invariant** component while the measured F mod p² and F² mod p² stay unchanged. The three choices (c,d)=(0,0),(1,0),(0,1) show the sharpness. QED.

At p=373: p²=139129, p³=51895117. All three matrices have upper-right entry 373 mod139129, all square to 373I₂ mod139129, and their normalized square digits are respectively

U_00=diag(1,1),
U_10=diag(374,374),
U_01=diag(1+373T,1−373T)   (mod139129).

Thus the signed anti-invariant **second digit** cannot be reconstructed from an operator truncated one digit too early. The toy T variable is **not** identified with the original native [X] coefficient.

## Executed exact certificate and provenance

The companion checked Python source is research_notes/portable_direct/d25_native_frobenius_half_slope_rank_precision_guard_20261028.py. It was actually run with exact modular integer arithmetic in (Z/p³)[T]/(T²−2) for **p=13,19,37,43,211,373**. In each case (2/p)=−1, so the quadratic coefficient ring is unramified; assertions check identical F mod p², rank-one Fbar, identical F² mod p², and three distinct U_F mod p² including opposite signed T ports. Actual output:

    PASS_D25_NATIVE_FROBENIUS_EVEN_RANK_AND_P3_PRECISION_WITNESS 6 primes
    P373_U_LIFTS_MOD_P2 [((1, 0), (1, 0)), ((374, 0), (374, 0)), ((1, 373), (1, 138756))]
    NATIVE_H0_B0_EXECUTED False

Both statements are proved algebraically; finite checks validate the six illustrative instances and checker implementation, not the unknown native experiment or independent theorem review.

**BRC COMPOSE_APPLIED:** source-typed carrier (p,r,O,σ,L,F,F(L),F²(L),rank Fbar,ν_p,U_F,ordered signed conjugate coordinates). The p²-to-normalized-p² map has distinct source fibers; erasing p³ source digits changes this observer. The external quadratic ring is not a native P000 X6 two-dimensional plane or a six-axis model, and nothing changes the ACTIVE worldview.

## Highest durable frontier and next executable action

**Native #1559 remains OPEN / PENDING_OWNER / NATIVE_NOT_EXECUTED** on this run's GitHub read (last issue update 2026-10-28T07:14:58Z). Keep its original fixed p=373 H0/B0 divided-power object and validation conditions unchanged. A genuine executor must identify the original coefficient ring and Frobenius definition; measure free module rank, mod-p operator rank and signed branches, provide [X]U mod139129 directly or calculate a *defined normalized square* using p³-precision source, and report original κ and Delta−R with raw reproducible evidence. Only **if** the actual square meets (A), use Theorem I for diagnostic consistency. These lemmas are not native acceptance in place of the experiment.

**No-redo:** accepted D24 UR/CM0, previous D25 Clausen original216 jets, frozen scalar source interface and previous rank-one no-go. Next native scientific act is real p373 evaluation with responsible authorized owner, not another toy rank calculation. Any mathematical continuation must preserve original source labels, sign and integrality.

**Research authority observed this run:** current Site v0.6.11 reports research_authority_granted=false, executor_binding_configured=false, active native control quota 5/5 and upstream code review pending. Historical Research-lane #6575 is a read-only recovery pointer; #6576 final FAILED/TimeoutExpired. No fresh CLAIM/OPEN, native Result, Research Activity or Source checkpoint is claimed; source registration remains REGISTER_PENDING/SYNC_DEBT. The original logical Research lane and maintenance lane are distinct. The scheduled research task and notification settings were not altered.