# R555｜固定 k=14 的 signed BRC 正负各半密度与有限零项

Date: 2026-11-05. Scientific frozen input: Enterprise Math R462 at `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Continuation: R554 commit `4bd18834e62eec2067db351c5794a9b58e79b8e3` and R541/R551 algorithms. Object: signed-BRC auxiliary scalar Toeplitz–Hessenberg determinants; no native X6 dynamics promoted.

## 定理（作者侧计算机辅助精确证明）

对任意非负整数 m，定义 Catalan 数 `C_j=binom(2j,j)/(j+1)`，取 `k=14,r=29`，
`H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t)` （`2<=t<=r`），其余 t 取 0；
`D_0(k)=1`，`D_m(k)=det(H_k(3+i-j))_{0<=i,j<m}`。
则
`
lim_{N->infinity} #{0<=m<N:D_m(14)>0}/N
=lim_{N->infinity} #{0<=m<N:D_m(14)<0}/N=1/2.
`
并且 `{m>=0:D_m(14)=0}` 为有限集。

## 精确递推及根结构

`H_k(t)=binom(r+t,2t) sum_{q=0}^{min(floor((t-1)/2),k)} binom(t-1,2q)4^q C_{k-q}`；
设 `p_t=H_k(t)/C_k`，`a_j=(-1)^(j-1)p_{j+2}/p_2`，`s_m=D_m(k)/(C_k p_2)^m`。
`C_14=2674440,p_2=31465,d=27`，因此
`
sum_{m>=0}s_m z^m=1/(1-sum_{j=1}^{27}a_j z^j),
Q(y)=y^27-sum_{j=1}^{27}a_j y^(27-j).
`
全部28个 t=2..29 的原始整数卷积与 Catalan 恒等式一致（计28项）。

`R555_VERIFY.py` 使用 SymPy 数值根**仅生成候选**，在源码固定27个有理复中心、半径 `1/10000`，对 `Q(c+w)=sum b_j w^j` 检验：
`
max(|Re b_1|,|Im b_1|) eps >
 |Re b_0|+|Im b_0| + sum_{j>=2}(|Re b_j|+|Im b_j|) eps^j.
`
精确 Fraction 检查全部27盘（351对两两不交）通过；最大右/左比 <3/500。
唯一最大模根为简单非实共轭对 `lambda,conj(lambda)` 且 `|lambda|>18`，其余25个根 `|lambda_j|<7`。
简单根的生成函数部分分式残数均非零。

## 非分圆根比值证书

在素数 `p=65537` 上（`3^32768=-1 mod p`, p-1=2^16），全部 Q 系数分母可逆，首项及常数项均非零模 p。
令
`
E(u)=Res_y(Q(y),u^27 Q(y/u)),  R(u)=E(u)/(u-1)^27.
`
逐点模 p 结果式计算 `u=0..729`，精确 Newton 插值出729次多项式 E；逐次精确除以 `(u-1)` 共27次，得到702次 R，且 `R(1)!=0 mod p`。另在两个插值区间外的点核对独立 SymPy resultant。

若存在不同特征根之比为 q 次单位根，则 `Phi_q` 整除有理系数 R，且 `phi(q)<=702`。由 `phi(q)>=sqrt(q/2)` 可取完整范围 `2<=q<=985608`。Euler phi 完整筛选给出1356个候选（最大 q=2940）。所有 `gcd(R mod 65537,Phi_q mod 65537)=1` 均通过，模 p 中不存在该类分圆因子，因而有理数域中亦不存在。这个判据要求 R 在该素数下保持预期次数，此处已精确检查。

因此 `lambda/conj(lambda)` 非单位根，令 `lambda=rho*exp(i theta)`，`theta/(2 pi)` 无理。
`s_m=2|A|rho^m cos(m theta+arg A)+O(sigma^m)`，其中 `rho>18,sigma<7,A!=0`。
Weyl 等分布给出正负索引各自然密度 1/2；特征根比值全部非单位根，Skolem–Mahler–Lech 定理给出零项有限性。经典定理只用于明示的线性递推对象。

## 本轮实际计算与独立检查

`R555_ROUCHE_PASS`: 27根盘、351对不交、最大精确右/左比近似0.00486042529（近似显示用于阅读，判定用 Fraction）。
`R555_RECURRENCE_PASS`: `m=0..1024` 中正515、负510、零0、相邻换号304。
`R555_MOD_INTERPOLATION_PASS`: `deg E=729,deg R=702`；范围外两个精确独立结果式取值检查。
`R555_CYCLOTOMIC_CHUNK_PASS`: 1356个分圆候选用同一 R 系数 SHA256 `c84af0f4ea7c4cb3f40087cac608edbeb118893d1def03dbffe79e53e57824bc` 分四段覆盖 `[0,800),[800,1000),[1000,1150),[1150,1356)`；每段检查通过。
`R555_RAW_H_AND_BERKOWITZ_PASS`: 28个原始 H 双算法检查，原始整数矩阵 1..16 阶行列式与递推全部一致。

All computations are exact integer, fraction or finite-field predicates; root candidate discovery uses numeric approximations only before exact isolation. Mathematical status: AUTHOR-SIDE PROOF / INDEPENDENT DRIVER REVIEW PENDING.

## 待解决问题

(1) k=15 的29次特征根隔离和模 p 非分圆证书；(2) 对全部 k>=5 统一构造主导根模长间隔的参数化估计；(3) 原研究方向 s=3,m=63 全正整数参数分类。
