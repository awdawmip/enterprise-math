# R521 — signed BRC 辅助标量四十四阶右缘 Toeplitz 子式：全正整数参数符号分类

日期：2026-11-04。冻结 R462 科学输入 18783e01e3646c72b7aab3b16d3f565e83e6446f，依赖 R452/R462 固定 t 多项式引理。接续 R520@d48d38f86727a3e59fd42091f1d68280c217fe57。状态 AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED。对象为 signed-BRC 原始支路的辅助标量模型。

## 精确条件定理

整数 k>=1 时，令 r=2k+1, C_k=binom(2k,k)/(k+1)>0。对于 2<=t<=r，令 H_k(t)=binom(r+t,2t)*[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t)，其余 t 取 H_k(t)=0。令 D_m(k)=det(H_k(3+i-j)) (0<=i,j<m)，D_0=1。

假设冻结 R452/R462 引理：每个固定 t>=2 的 p_t(k)=H_k(t)/C_k 对所有正整数 k 取值同于一个 Q[k] 多项式，且 deg p_t<=2t。则

    D_44(k)>0：1<=k<=5 或 7<=k<=17；
    D_44(k)<0：k=6 或全部 k>=18。

没有正整数 k 上的零。换成 r=2k+1：负值为 r=13 及所有奇数 r>=37；正值为奇数 r=3..11 和 r=15..35。结合 R520：D_43(k)>0>D_44(k)，18<=k<=38。

## Hessenberg 递推、次数与精确计算证明

对 f_m=D_m/C_k^m，Toeplitz–Hessenberg 展开给出 f_0=1，f_m=sum_(a=1)^m (-1)^(a-1)*p_(a+2)*p_2^(a-1)*f_(m-a)。第 a 项次数 <=2(a+2)+4(a-1)+6(m-a)=6m，因此 deg f_44<=264。

取 G(k)=[k(k+1)(2k+1)(2k+3)]^44*(k+2)，其对 k>=1 为正，deg G=177。对 k=1..88 精确求约分有理数 f_44/G，取分母最小公倍数 L>0。定义整数 delta_j=Delta^j[L*f_44/G](1) (j=0..87)，S(k)=sum_(j=0)^87 delta_j*binom(k-1,j)。证书完整保存 L 和 88 个整数 delta_j。

deg(G*S)<=177+87=264。使用精确 BigInt 检查 k=1..265 全部满足 L*D_44(k)=C_k^44*G(k)*S(k)。由于除去正因子 C_k^44 后两边均为次数 <=264 的多项式，并在 265 个互异整数点相等，得到完整多项式恒等式 L*f_44=G*S。

S(1)..S(17) 的整数值在证书中列出，符号依次为 k=1..5 正、k=6 负、k=7..17 正。于 k=18 定义 epsilon_j=Delta^j S(18) (j=0..87)。证书列出全部 88 项，均严格为负。对任意整数 u>=0，有 S(18+u)=sum epsilon_j*binom(u,j)<0，因为二项式基非负且 binom(u,0)=1、epsilon_0<0。L、C_k 和 G(k) 在 k>=1 上严格为正，故 k>=18 的符号永久为负，条件定理得证。

## 两套精确实现及审核边界

node R521_VERIFY.js > R521_EVIDENCE.json：265 点多项式恒等式检查、20 项直接原始 signed 44x44 Bareiss 整数行列式、880 项原始 signed 卷积与 ballot–Catalan 系数检查，R521_EXACT_JS_PASS。

python R521_INDEPENDENT.py > R521_INDEPENDENT_EVIDENCE.json：分别构造原始 signed 矩阵并以 SymPy Berkowitz 精确计算 16 个 44x44 行列式，与独立 ballot 递推一致，覆盖 k=5/6、6/7、17/18 三处变号边界；另验证 880 项 signed/ballot 系数，R521_INDEPENDENT_PASS。该独立性是作者侧实现交叉检查。

当前 GitHub 身份 awdawmip 有仓库管理员/推送权限。原生 Owner 查询返回 CONTROL_QUOTA，原生 session_start 返回 STATIC_READONLY_SCOPE_DENIED 且 operation_sent=false；本成果尚无原生 Researcher-ID、CLAIM、Result 或独立 Driver Review。P000、ACTIVE 世界观、冻结科学输入均未修改。

下一研究单元 s=3,m=45：次数界 <=270，90 个 Newton 系数与 271 个整数点精确恒等式；另一独立路线是固定 k=5,6,7,17,18 的有理阶数生成函数主导代数根机制。
