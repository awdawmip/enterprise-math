# R522 — signed BRC 辅助标量四十五阶 Toeplitz 子式：全正整数参数符号分类

日期：2026-11-04。科学输入冻结：R462@`18783e01e3646c72b7aab3b16d3f565e83e6446f`；前沿：R521@`04a60dd4f9c42b2cee578bf97823ea1649e2d488`。AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED。

## 条件定理

令 k>=1 为整数，r=2k+1，C_k=binom(2k,k)/(k+1)>0。对 2<=t<=r 定义 H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x²)^(r-t)，其余 t 取零。令 D_m(k)=det(H_k(3+i-j)) (0<=i,j<m)，D_0=1。

以冻结 R452/R462 引理为共同假设：固定 t>=2 时，p_t(k)=H_k(t)/C_k 在 k 的正整数上等于 Q[k] 中次数 <=2t 的多项式。则

```
D_45(k)>0  (1<=k<=11);
D_45(k)<0  (all integers k>=12).
```

因此 r=3,5,...,23 时为正，从奇数 r=25 起恒负。结合 R521 得 D_44(k)>0>D_45(k) 对 12<=k<=17 成立，另有 k=6 时 D_44(k)<0<D_45(k)。

## 精确计算辅助证明

设 f_m=D_m/C_k^m。Toeplitz–Hessenberg 递推为
```
f_0=1;
f_m=sum_(a=1)^m (-1)^(a-1) p_(a+2)*p_2^(a-1)*f_(m-a).
```
逐项次数上界为 2(a+2)+4(a-1)+6(m-a)=6m；deg f_45<=270。取 G(k)=[k(k+1)(2k+1)(2k+3)]^45*(k+2)，deg G=181，在正整数域严格正。

对 k=1..90 精确求约分有理数 f_45/G，令 L>0 为分母最小公倍数，delta_j=Delta^j[L*f_45/G](1) (0<=j<90)，S(k)=sum_(j=0)^89 delta_j*binom(k-1,j)。全部整数 L、delta_j 收录于 R522_EVIDENCE.json。

deg(G*S)<=181+89=270。精确 BigInt 在 k=1..271 的271个互异点逐点检查
```
L*D_45(k)=C_k^45*G(k)*S(k).
```
这两边在除以 C_k^45 后是次数不超过270的 Q[k] 多项式，故恒等式 L*f_45=G*S 对所有 k 成立。

证书中的 S(1)..S(11) 严格为正。对 epsilon_j=Delta^j S(12) (0<=j<90)，证书保存全部90项，**每项严格为负**。整数 u>=0 时 S(12+u)=sum epsilon_j*binom(u,j)<0，因为 binom(u,j)>=0 且 epsilon_0<0。乘回 C_k^45、G(k) 和正数 1/L，得到全正整数分类。

## 验证、范围、继续

node R522_VERIFY.js > R522_EVIDENCE.json：R522_EXACT_JS_PASS；271点恒等式、20个直接 signed 45x45 Bareiss 行列式、900项 signed 与 ballot–Catalan 双表达式交叉核验。
python R522_INDEPENDENT.py > R522_INDEPENDENT_EVIDENCE.json：R522_INDEPENDENT_PASS；Python 3/SymPy 1.14 Berkowitz 对原始 signed 45x45 整数矩阵计算 k=1..20，与独立 ballot 递推一致，覆盖 k=11/12 变号边界，并完成900项系数交叉核验。全部为精确整数运算，独立性限于作者侧两种实现。

载体与观察：冻结 signed BRC 支路的带符号整数系数 H_k(t) 和固定偏移3的 Toeplitz 子式标量，保留抵消而不转正质量。此结果属于辅助标量全参数符号分类，跨阶数机制继续开放。

GitHub 认证身份 awdawmip；当轮 Sites 配置为 static_machine_readonly、write_relay_enabled=false、research_authority_granted=false。原生 Owner 查询返回 CONTROL_QUOTA；session_start 返回 STATIC_READONLY_SCOPE_DENIED（operation_sent=false）。没有原生 Researcher-ID、CLAIM、Result 或 Driver 接纳。P000、ACTIVE 世界观和冻结输入未修改。

下一最小研究单元：s=3,m=46，次数上界276，92项 Newton 差分和277个整数点。机理分支：固定 k=11,12,17,18 构造有理阶数生成函数、计算分母和主导代数根，解释阶数变号与无限尾部。
