# R503 — signed BRC 辅助标量：二十六阶右缘 Toeplitz 子式全正整数参数分类

2026-11-03；状态：AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE，DRIVER_UNREVIEWED，NOT_ADMITTED。
冻结科学输入 R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`，前沿 R502 `3273d034df3b007beeb9a30c64dcf80ade0373d4`。行为规范按当前入口读取。P000 与 ACTIVE 世界观保持不变。

## 定理

对正整数 k，令 r=2k+1，C_k=binom(2k,k)/(k+1)>0，定义
H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t) 当 2<=t<=r，其他 t 为0。
设 D_m(k)=det[H_k(3+i-j)]，0<=i,j<m。

**D_26(k)>0 (1<=k<=6)，D_26(k)<0 (k>=7)。** 首个负值是 r=15，所有奇数 r>=15 均为负。结合 R502 的 D_25 符号，k=7,8,9 时 D_25>0>D_26。

## 无穷域证明及完整证书

由冻结 R452/R462 EOR 恒等式，固定 t 的 p_t(k)=H_k(t)/C_k 属于 Q[k] 且 deg p_t<=2t。Hessenberg 递推为
f_0=1，f_m=Σ_(ell=1)^m (-1)^(ell-1) p_(ell+2) p_2^(ell-1) f_(m-ell)，f_m=D_m/C_k^m。
归纳有 deg f_m<=6m（ell 项次数不超过 (2ell+4)+4(ell-1)+6(m-ell)=6m）；故 deg f_26<=156。

令 G_26(k)=k^26(k+1)^26(k+2)(2k+1)^26(2k+3)^26，deg G_26=105，所有 k>=1 时 G_26>0。
将 k=1,...,52 的精确 f_26(k)/G_26(k) 约分，取分母最小公倍数 L>0，得52个整数；记其前差分 δ_j，构造 S(k)=Σ_(j=0)^51 δ_j binom(k-1,j)，deg S<=51。

`R503_VERIFY.js` 通过157个各异整数 k=1,...,157 核对
L D_26(k)=C_k^26 G_26(k) S(k)。
两边除以 C_k^26 后为度数至多156的有理多项式，157点逐项完全相等，因此多项式恒等式成立。

完整系数证书在 `R503_EVIDENCE.json`：S(1),...,S(6) **全部严格为正**，而以7为原点的52项 ε_j=Δ^j S(7) **全部严格为负**。对每个整数 u>=0，S(7+u)=Σ ε_j binom(u,j)<0。因此由 L>0、C_k>0、G_26(k)>0 推出定理。

主程序实际完成157项恒等式检查、20项26×26原始 signed-BRC 直接 Bareiss 行列式检查、540项原始卷积与独立 ballot-Catalan 核对，输出 `R503_EXACT_JS_PASS`。独立 `R503_INDEPENDENT.py` 使用 ballot-Catalan 矩阵与 SymPy determinant，k=1,5,6,7,8,10 精确符号为 +,+,+,-,-,-，输出 `R503_INDEPENDENT_PASS`。独立程序属有限交叉检查；全参数结论依赖多项式次数界、157点证书和52项差分符号。

研究范围为冻结 signed BRC 辅助标量观察对象；不对原生 X6 心跳动态作额外推断。原生 Owner/CLAIM/Driver 审查权依当前任务状态单独认定。

## 下一单元

检验 s=3,m=27；54项 Newton 差分、163点多项式恒等式，寻找全部正整数 k 的符号区间。并比较 k=6、7、10 固定参数的有理阶数生成函数极点。
