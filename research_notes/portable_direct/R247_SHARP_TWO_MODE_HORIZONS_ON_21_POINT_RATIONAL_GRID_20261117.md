# R247 — Sharp two-mode horizons on a 21-point rational parameter grid

Date: 2026-11-17 (Asia/Shanghai)
Scope: Seven-source reversible sticky-reset auxiliary positive scalar observer, **finite** parameter grid.
Evidence: AUTHOR_PROVED / EXACT_RATIONAL_COMPUTATION_EXECUTED / NOT_REVIEWED.
Native BRC EffectHistogram: NOT_EXECUTED. Formal Task CLAIM / Result / Review: NONE.

## Provenance and input boundary

Continuation of R246 at `f27cf3726bb58f2b5705cb80c4b8f48d254011f9`; original scientific input remains pinned at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The present argument does not revise P000, the X6/heartbeat worldview or the source firewall. The model is an auxiliary scalar readout; it does not reconstruct port, sign, branch, source, multiplicity, provenance or cross-moment data.

Let
[
S_{21}={j/1000:j=390,391,ldots,410}.
]
At each `s` use the R246 parameters:
[
t(s)=rac{1691s-2615}{2615s-3539},qquad
alpha=(1/5,1/4,3/10,9/20,s,2/3,t(s)),
]
[
b_0=13/60,quad b_j=(5/18)|1/2-alpha_j|;(j=1,ldots,6),
quadpi_j=b_j/(1-alpha_j),
]
[
Z=sum_{j=0}^6b_j/(1-alpha_j)^2,quad
ho_j=b_j/igl[Z(1-alpha_j)^2igr],quad
P_{ij}=alpha_idelta_{ij}+(1-alpha_i)pi_j.
]
For each of the 63 proper masks `m=0,...,62`, let `D_m` include 0 and every nonzero source index selected by `m`. Put
[
W=(144,576,1440,4320,17280,86400,518400),
quad Phi_n=sum_{m=0}^{62}W_{operatorname{popcount}(m)},ho_{D_m}^{!T}P_{D_m}^{,n-1}{f1}.
]
Let `r` and `beta` be the leading Perron roots of masks 59 and 55 and let `A,B` be their positive spectral coefficients. Define
[
X_n=A r^{n-1}+Beta^{n-1},qquad E_n^{[2]}=Phi_n/X_n-1.
]
R243–R245 establish that the omitted positive spectral tail gives `E_n^[2] > 0` and strictly decreases with integer `n>=2` on this family. Their theorem is reused at exactly this scope.

## New finite-grid theorem

**Theorem R247.** Among the 21 rational parameter values in `S_21`, the smallest common integer `N` such that
[
E_n^{[2]}(s)<1/100qquad	ext{for all }sin S_{21}	ext{ and }nge N
]
is **270**. For the tolerance `1/1000`, the corresponding smallest common integer is **403**.

These are sharp *finite-grid* uniform thresholds. No inference is made that the same bounds hold at every real `s` between grid points.

**Proof by exact finite certificate.** For fixed rational `s`, write `P=diag(alpha)+u pi^T`, `u_i=1-alpha_i`. Choose `C=lcm den(alpha_i)`, `Q=lcm den(pi_i)`, `d=CQ`, `h_i=d alpha_i`, `u_i^*=C(1-alpha_i)`, `w_j^*=Q pi_j`. For any proper mask, integer state `v_i(0)=1` obeys
[
v_i(k+1)=h_iv_i(k)+u_i^*sum_{jin D_m}w_j^*v_j(k),qquad P_{D_m}^k{f1}=d^{-k}v(k).
]
Thus `Phi_n` is exactly rational by a 63-mask integer computation.

The secular equation for the dominant eigenvalue `lambda` of mask `m` is
[
f_m(lambda)=sum_{iin D_m}rac{b_i}{lambda-alpha_i}-1=0,qquad lambda>max_{iin D_m}alpha_i.
]
Exact dyadic bisection produces bounds `l<lambda<u` with `f_m(l)>0>f_m(u)`. Define
[
S_m(x)=sum_{iin D_m}rac{b_i}{(1-alpha_i)(x-alpha_i)},
quad Q_m(x)=sum_{iin D_m}rac{b_i}{(x-alpha_i)^2}.
]
The Perron amplitude is `W_popcount(m) S_m(lambda)^2/(Z Q_m(lambda))`. Because `S_m,Q_m` strictly decrease in `x` above all poles, the positive rational bounds
[
A_m^-=rac{W S_m(u)^2}{ZQ_m(l)}
 < A_m <
A_m^+=rac{W S_m(l)^2}{ZQ_m(u)}
]
hold; apply this separately to masks 59 and 55. Consequently `X_n^-<X_n<X_n^+` from the corresponding root and amplitude bounds.

For each of the 21 `s` values, and `(n,d)=(270,100),(403,1000)`, the supplied exact computation proves
[
oxed{(d+1)X_n^- -dPhi_n>0.}
]
For `s=41/100`, it also proves
[
oxed{dPhi_{n-1}-(d+1)X_{n-1}^+>0}
]
for each of the same tolerances. This is **44 strict rational sign checks**, using 104 dyadic root bisections for each Perron root at each parameter, all exact integers and `fractions.Fraction`. The time-monotonicity theorem then establishes both upper bounds and their sharpness on the full declared finite grid. QED.

## Verification and replication

Execute Python 3 standard library script `R247_finite_grid_two_mode_cert.py` in this directory; it writes deterministic JSON with all 44 positive comparison-margin digests and their numerator/denominator bit lengths. Direct local execution on 2026-11-17 returned `all_pass=true`, 21/21 parameters, 44/44 strict comparisons, about 8.6 seconds of wall time on the local host.

Locally generated complete verification JSON SHA-256:
`40a5e9145f732af15564b9269b4ffbca2b69fc1f17e1fa0c4fc3a7448484bab9`.
Script SHA-256 (local source):
`cee028677b3f6766413b4dd169b784b816d73673bbc693d8fd42cc93c0c6d929`.
Full 44-comparison JSON evidence is additionally preserved as [reversible gzip/base64 text](R247_verification_full.json.gz.b64). Recover with `base64 -d R247_verification_full.json.gz.b64 | gzip -d > R247_verification_full.json`, and verify the resulting SHA-256 against the value above. The Git blob for this archive was verified to match the locally encoded full output byte-for-byte (`f0ed1c66b06ee148d35b46521111d4d2f3581428`).

The expected SHA-256 here fingerprints the actual local run, not an independent mathematical review. Re-run on the exact published source and compare outputs before using hashes as cross-machine evidence.

Numerical values (diagnostic only; PASS depends solely on exact comparisons):
| s | E_270 | E_403 |
|---|---:|---:|
| 0.390 | 0.008428164 | 0.000654333 |
| 0.395 | 0.008760862 | 0.000713736 |
| 0.400 | 0.009124343 | 0.000787238 |
| 0.405 | 0.009521658 | 0.000878958 |
| 0.410 | 0.009955584 | 0.000993991 |

## Remaining mathematical frontier

The sharp finite-grid result does **not** settle the uncountable real interval `39/100<s<41/100`. Numerically the 270/403 errors rise toward `s=0.41`, whereas R246 proved nonmonotone behavior at 126 events. Therefore the missing theorem is a parameter-wide bound or sign certificate for `E_270^[2](s)<0.01` and `E_403^[2](s)<0.001`, or an explicit counterexample, without extrapolating the grid. A promising follow-up is certified interval differentiation of the rank-one transfer and two secular roots, with adaptive parameter subdivision and exact or directed-rounding evidence. Full bit-complexity comparisons to 230-order recurrence and 256-state direct propagation, and native joint-source BRC integration, also remain open.
