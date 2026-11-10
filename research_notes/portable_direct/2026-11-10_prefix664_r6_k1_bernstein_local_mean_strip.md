# PREFIX-664-R6 — Local-mean and first-Bernstein-layer refinement doubles the certified BRC boundary strip beyond PREFIX-663

Date: 2026-11-10 (Asia/Shanghai). Researcher-ID: \`EM-DIRECT-B3D89A / TASK_RESEARCH\`. Research-Activity-ID: \`RA-DAF861B6073C1E68895EECB3\`.
Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Status: **AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem 664.1 — A stronger interior p-gradient on a fourfold larger rectangle
Let \`μ(p,z)=E[Y]\`, \`H=E[Y²]/2\`, \`W=2H−μ²\`, and \`V_q=q²W−qμ\` in the unchanged frozen 189-layer BRC statistical observation model. Define
\`\`\`
ε=2^(-15)=1/32768,   J=[607/4096,609/4096],
R=[0,ε]×J,           12≤q≤24 (every real value).
\`\`\`
For **every** \`(p,z)∈R\` and \`q∈[12,24]\`,
\`\`\`
μ(p,z) < 91;          ∂_p V_q(p,z) < -12650.
\`\`\`
Writing \`z_*(q)\` for the unique moving boundary maximizer from PREFIX-660 and \`M_q=V_q(0,z_*(q))\`, the **unique** maximizer over \`R\` is \`(0,z_*(q))\` and
\`\`\`
M_q−V_q(p,z) ≥ 12650 p + 6400000 (z−z_*(q))²,
\`\`\`
strict off that maximum. This expands area by **4× over PREFIX-663**, **64× over PREFIX-662**, and **32768× over PREFIX-661**. The PREFIX-660 exact q=12 and q=24 optimum brackets also apply to the enlarged rectangle.

## New proof ingredient 1 — retain the k=1 Bernstein second-difference layer

Write the frozen surviving path multiplicities as \`A_n(k)\`, with \`f_n(k)=A_n(k)/binom(n,k)∈[0,1]\`. The first four multiplicities \`k=0,1,2,3\` form an exact closed projection of the frozen \`wide(n,k)\` path recurrence, because its kth output depends only on k and k−1. Compute \`Δ² f_n(0)\` and \`Δ² f_n(1)\` from these exact rows.

Bernstein differentiation gives \`s_n''(p)=n(n−1)E[Δ²f_n(K)]\` for \`K~Binomial(n−2,p)\`. The inequality \`P(K≥2)≤binom(n−2,2)p²\` and the universal \`|Δ² f_n(k)|≤2\` yield
\`\`\`
|s_n''(p)| ≤ n(n−1) (
    |Δ² f_n(0)| + (n−2)p |Δ² f_n(1)|
                      + (n−2)(n−3)p²).
\`\`\`
The certificate computes (all sums \`n=2,...,188\`) the exact integers:
\`\`\`
A0=Σ n(n−1)|Δ²f_n(0)|                = 13800,
A1=Σ n(n−1)(n−2)|Δ²f_n(1)|          = 670800,
B2=Σ n(n−1)(n−2)(n−3)               = 45727338888,
C0=Σ (n+1)n(n−1)|Δ²f_n(0)|          = 485400,
C1=Σ (n+1)n(n−1)(n−2)|Δ²f_n(1)|    = 28815600,
E2=Σ (n+1)n(n−1)(n−2)(n−3)          = 7240161990600.
\`\`\`
The known nonnegative two-clock moment kernels are bounded by 1 for \`μ\` and \`n+1\` for \`H\`. On \`p∈[0,ε]\`, put
\`\`\`
U2=A0+A1ε+B2ε²,     H2=C0+C1ε+E2ε²,
U1=225+A0ε+(A1/2)ε²+(B2/3)ε³.
\`\`\`
By the exact edge-support identity \`0≤μ_p(0,z)≤225\` (PREFIX-659/662) and integration, \`|μ_pp|≤U2\`, \`|H_pp|≤H2\`, \`|μ_p|≤U1\`.

## New proof ingredient 2 — a local rather than universal mean bound

PREFIX-659's exact boundary Gamma reduction proves \`μ(0,Q)<89.456\` at \`Q=19/128\` and expresses \`μ(0,z)=25+Σ_{m=0}^{188}a_m s_m(z)\`, where \`0≤a_m≤1\`. The established binomial score bound on the present \`J\` gives \`|s'_m(z)|<21\` for \`m≤188\`, hence
\`\`\`
|∂_z μ(0,z)|<189·21=3969     (z∈J).
\`\`\`
Since \`|z−Q|≤1/4096\`, integrating first in z and then in p yields the strict uniform rational bound
\`\`\`
μ(p,z) < 89.456 + 3969/4096 + εU1
       = 1629075806660385760079 / 18014398509481984000 < 91.
\`\`\`
The fixed model variance \`W=2H−μ²\` consequently satisfies
\`\`\`
|W_pp| ≤ 2H2 + 2U1² + 182 U2.
\`\`\`

## Completion of the proof
For all \`q∈[12,24]\`, set \`K=576(2H2+2U1²+182U2)+24U2\`. The exact Fraction calculation is
\`\`\`
ε K = 314339667689549517864494883454305 /
      4951760157141521099596496896 < 64000.
\`\`\`
PREFIX-661's exact whole-edge-band gradients give \`∂_pV_12(0,z)<-76650\`, \`∂_pV_24(0,z)<-306490\`. As \`∂_p V_q/q=qW_p−μ_p\` is affine in q, the bounds imply \`∂_pV_q(0,z)<-76650\` for every real \`12≤q≤24\`. Thus for \`p∈[0,ε]\`,
\`\`\`
∂_p V_q(p,z) < -76650 + εK < -12650.
\`\`\`
Integration in p plus PREFIX-660's certified strict z-curvature \`∂²_zV_q(0,z)<-12800000\` proves the claimed stability and uniqueness. QED.

## Exact evidence and continuation

The companion \`PREFIX664_R6_K1_BERNSTEIN_LOCAL_MOMENT_CERTIFICATE.py\` recomputes the exact \`wide(n,k)\` predicate for \`k=0..3\`, 189 projected rows, all six Bernstein budgets, local mean envelope and rigorous rational gradient comparison. Companion JSON records the exact rational certificates. A local standalone copy passed all assertions (\`ALL_CHECKS_PASS 757\` before an extra score-domain check added to the published source; expected published-source count is 758). The proof reuses specific PREFIX-659, 660, 661 and 662 certificates, not a repeated 96-port native dynamics simulation.

**BRC resolution:** COMPOSE_APPLIED. The new projection retains the first four signed-path multiplicities exactly and accounts for the remaining coefficient mass through a rigorous quadratic tail envelope. Model/observer scope is unchanged.

**Next discriminating step:** attempt \`p≤2^-14\` by replacing the absolute second-derivative bound with a signed \`∂_pV_q\` Bernstein coefficient certificate or an exact interval kernel bound; independently construct triangle-wise variance upper bounds on \`0≤p≤z≤1/2\` for comparison against the boundary optimizer. Formal Result and independent review remain pending.
