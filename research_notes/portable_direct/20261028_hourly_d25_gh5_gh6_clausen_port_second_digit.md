# D25/LIFT GH-5 / GH-6 — next p-adic digit of the labelled Clausen middle port

Date: 2026-10-28 (Asia/Hong_Kong). Lane: TASK_RESEARCH `chatgpt-research-hourly-enterprise-math-20260923`. Parent: D25/LIFT/JT2; publication `TP2-B6F4FC938FF94941C1B7`; original scientific Source pinned at `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Evidence: author-derived exact algebra and executed finite modular/rational checks, **UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is not a canonical Source checkpoint, native X6 run, or theorem promotion.

## Exact input and source/observer contract

Consume GH-2's *labelled* original S-Gauss coefficients and GH-3's single-port Clausen reduction without recomputing or crediting those facts as new discoveries. For each prime $p\equiv19\pmod{24}$, let

$$a=(p-3)/8,\quad b=(3p-1)/8,\quad h=(p-1)/2,\quad d=(p-3)/4.$$

The original auxiliary Gauss carrier is $u_k=(1/8)_k(3/8)_k/((k!)^2 9^k)$. For $a<i\le b$ define the **exact rational** $p$-integral units $\beta_i=u_i/p\in\mathbb Z_p^\times$. The finite, source-labelled middle-middle port is

$$M_p=\sum_{\substack{a<i,j\le b\\ i+j>h}}(8(i+j)+1)\,\beta_i\beta_j\in\mathbb Z_p.$$

It is a signed weighted port, not a positive BRC mass; the two original source indices and the cutoff remain part of its observer. GH-3 proved only $M_p\equiv-\beta_b^2T_p\pmod p$ with $T_p$ as defined below. The next-digit claim must retain the correction caused by the original $p$-dependent reversal.

## GH-5. Exact deformation and a second-digit theorem

For $0\le r\le d$ put

$$g_r=9^r\frac{(1/8)_r^2}{(3/4)_r\,r!},\qquad
H_r=\sum_{j=0}^{r-1}\left(\frac1{8j+8}+\frac1{8j+6}-\frac2{8j+1}\right),\quad H_0=0.$$

All displayed denominators are $p$-units in the stated ranges. The original coefficient recurrence gives the **exact rational** backward step

$$\frac{\beta_{b-r-1}}{\beta_{b-r}}
=\frac{9(8r+1-3p)^2}{(8r+8-3p)(8r+6-3p)}\qquad(0\le r<d).$$

By dividing this step by $g_{r+1}/g_r=9(8r+1)^2/((8r+8)(8r+6))$ and multiplying the finite steps, obtain

$$\boxed{\frac{\beta_{b-r}}{\beta_b}\equiv g_r(1+3pH_r)\pmod{p^2}}\qquad(0\le r\le d).$$

Define the unchanged GH-3 coefficients and three finite observers:

$$c_t=9^t\frac{(1/4)_t^3}{(1/2)_t(3/4)_t\,t!},\quad
T_p=\sum_{t=0}^d(8t+1)c_t\in\mathbb Z_p,\quad
C_p=\sum_{t=0}^dc_t\in\mathbb Z_p,$$

$$K_p=\sum_{r+s\le d}(8(r+s)+1)g_rg_s(H_r+H_s)\in\mathbb Z_p.$$

**Theorem GH5 (all $p\equiv19\bmod24$):**

$$\boxed{\frac{M_p}{\beta_b^2}\equiv -T_p+p(6C_p-3K_p)\pmod{p^2}.}$$

**Proof.** Make the lossless finite reindexing $i=b-r,j=b-s$. Its original cutoff is precisely $r+s\le d$ and its original weight becomes $8(i+j)+1=6p-(8(r+s)+1)$. Substituting the preceding $p^2$ reversal expansion yields an uncorrected sum $-\sum_{t\le d}(8t+1)\sum_{r+s=t}g_rg_s$, a $6p\sum_{r+s\le d}g_rg_s$ term, and a $-3pK_p$ term. The exact coefficientwise Clausen identity (as consumed in GH-3) states $\sum_{r+s=t}g_rg_s=c_t$. Hence the three terms are $-T_p$, $6pC_p$, $-3pK_p$ modulo $p^2$. All steps use rational identities and unit-denominator arithmetic. QED.

Consequently, **conditional on** the still-open universal congruence $T_p\equiv0\pmod p$, the next-digit identity is

$$\boxed{\frac{M_p}{p\beta_b^2}\equiv-\frac{T_p}{p}+6C_p-3K_p\pmod p.}$$

This statement never infers $T_p=0$ from a finite experiment. Replacing $K_p$ by zero is an unjustified loss of the deformation/provenance information.

## GH-6. Exact countercertificate to uncorrected lifting and finite valuation observations

At $p=19$ the executed exact check gives $(T_p/p,C_p,K_p)\equiv(18,3,5)\pmod{19}$, $M_p/\beta_b^2\equiv76\pmod{19^2}$ and $M_p\equiv209\pmod{19^2}$. Indeed $-19\cdot18+19(6\cdot3-3\cdot5)=-285\equiv76\pmod{361}$; the naive uncorrected $-T_p\equiv19$ is false modulo $361$.

At $p=43$ one instead has $(T_p/p,C_p,K_p)\equiv(38,20,13)\pmod{43}$, so

$$-T_p+43(6C_p-3K_p)\equiv-43\cdot38+43\cdot81\equiv0\pmod{43^2}.$$

An independent exact rational evaluation of the **original labelled double sum** establishes $v_{43}(M_{43})=2$ and $M_{43}/43^2\equiv22\pmod{43}$. Thus the extra vanishing at $43$ is exactly one additional digit, not a claim of infinite cancellation.

The companion stdlib checker was executed and passed: for **all 1227 primes** $5\le p<10000$, the same truncated $T_p$ (with $d=\lfloor(p-1)/4\rfloor$ outside the 19-class) has $v_p(T_p)=1$; this is a finite exact-computation observation, not an all-prime theorem. For **all 37 primes** $p<2000$, $p\equiv19\pmod{24}$, the original middle port and GH-5 formula agree modulo $p^2$, with $p=43$ the only member of that finite set where $M_p\equiv0\pmod{p^2}$. The checker also reconstructs the original rational source for $p=19,43$ without replacing it by a Gauss gauge. The two observations highlight different phenomena: $T_p/p$ remains nonzero at $p=43$, but the *labelled* lifted port cancels through $C_p,K_p$.

## Scope and next action

Mathematical indices here are auxiliary coefficient ranks, not native spatial axes or a substitute for P000's six-dimensional X6 with independent time. This is a BRC-compatible provenance/valuation-carrier audit: $T_p$ alone is an insufficient next-digit observer; $(T_p,C_p,K_p,\beta_b)$ retains the declared port reconstruction to precision $p^2$. The exact theorem says nothing by itself about the original W/S supercongruence, a source-faithful nonlocal WZ map, H0/B0, $[X]U\bmod p^2$, Frobenius $\eta/\kappa$, or native $p=373$ experiments. All remain open D25 acceptance obligations.

Next precise science step: seek a finite-field/WZ proof or counterexample for $T_p\equiv0\pmod p$ first in the 19-class; then use the GH-5 $K_p$ port to test whether a finite boundary identity can bridge GH-2/GH-4 and R36 without erasing the original six Hasse labels, two finite endpoints, or positive-infinity port. Formal controller recovery is separately tracked in `awdawmip/enterprise-math#1558`: Source currently has a predecessor CLAIM mismatch, and this portable record neither claims authority nor releases a claim. Preserve the old Research session/staging and immutable source pin for the canonical successor.
