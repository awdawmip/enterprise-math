# R518 — signed BRC 辅助标量：s=3、41阶 Toeplitz 子式全参数符号分类

日期：2026-11-04。冻结科学输入 R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`；接续作者侧 R517 @ `78c507473db8d6f79ccc1550dcb8a8be3217bb3a`。状态：**AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / NOT_ADMITTED / DRIVER_UNREVIEWED**。全程针对原始 signed BRC 辅助标量，保留 P000 与原生 X6 的模型边界。

## 定义与命题

对所有整数 k>=1，置 r=2k+1，C_k=binom(2k,k)/(k+1)>0，并定义

```
H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t),  2<=t<=r;
H_k(t)=0, otherwise;
D_m(k)=det(H_k(3+i-j))_(0<=i,j<m), D_0=1.
```

**定理（依赖冻结 R452/R462 的固定 t 多项式引理，对所有正整数 k）：**

```
D_41(k)>0 (1<=k<=5);
D_41(k)<0 (6<=k<=14);
D_41(k)>0 (k>=15).
```

因此奇数 r=3,5,7,9,11 为正，r=13,15,...,29 为负，自 r=31 起永久严格为正。与 R517 组合，有 D_40(k)>0>D_41(k) (k=6,7)；以及 D_40(k)<0<D_41(k) (15<=k<=28)。

## 完整精确整数证明

冻结引理提供 p_t(k)=H_k(t)/C_k∈Q[k] (t>=2 固定)，deg p_t<=2t。Toeplitz–Hessenberg 行列式满足

```
f_0(k)=1, f_m(k)=D_m(k)/C_k^m;
f_m(k)=sum_(a=1..m) (-1)^(a-1) p_(a+2)(k) p_2(k)^(a-1) f_(m-a)(k).
```

归纳中每项次数不超过 2(a+2)+4(a-1)+6(m-a)=6m，故 deg f_41<=246。取对整数 k>=1 严格为正的

```
G_41(k)=[k(k+1)(2k+1)(2k+3)]^41*(k+2), deg G_41=165.
```

以 k=1,...,82 的精确分数 f_41(k)/G_41(k) 的约分分母最小公倍数 L>0 归一化，构造82项整数 Newton 差分 delta_j，并令

```
S_41(k)=sum_(j=0..81) delta_j*binom(k-1,j), deg S_41<=81.
```

从而 f_41 与 G_41*S_41/L 均为次数<=246的有理多项式。实际通过 Node.js BigInt 在 **247 个不同整数点 k=1,...,247** 上逐点精确验证

```
L*D_41(k) = C_k^41*G_41(k)*S_41(k).
```

247个点上的恒等式和次数上界建立对所有整数 k 的完整多项式恒等式。完整 L、delta_j 和检验元数据见 `R518_EVIDENCE.json`。

证书在前14个整数点的准确符号为 k=1..5 正、k=6..14 负。平移至 k0=15 得到82项 epsilon_j=Delta^j S_41(15)，**每项严格为正**（完整整数列表见证书）。于是任意整数 u>=0 均有

```
S_41(15+u)=sum_(j=0..81) epsilon_j*binom(u,j)>0,
```

因为 epsilon_0>0，其他每一项均非负。L、C_k、G_41(k) 均为正，遂得全部 k 的三段符号分类，不是有限采样外推。

## 独立交叉核验与验证范围

`node R518_VERIFY.js > R518_EVIDENCE.json` 已实际运行并得到 `R518_EXACT_JS_PASS`：247点恒等式、20个41×41原始 signed 卷积矩阵 Bareiss 行列式与 Hessenberg 递推相等、820对 signed 卷积与 ballot–Catalan 公式相等。生成代码使用 BigInt 整数运算，不使用浮点数。

`python R518_INDEPENDENT.py > R518_INDEPENDENT_EVIDENCE.json` 已实际运行，Python/SymPy Berkowitz 从 ballot–Catalan 公式直接生成19个41×41矩阵并与独立编写的递推比较，覆盖 k=5/6、14/15 两处变号边界；另以不同实现核验820对原始卷积与 ballot–Catalan 恒等式，得到 `R518_INDEPENDENT_PASS`。这是实现与算法交叉核验，**不是**独立 Driver 数学审查。证书的普遍量化结论依赖上述冻结多项式引理与完整点值恒等式，而不是19个样本本身。

Frozen 科学对象不变；未把 signed BRC 辅助标量结论提升为原生 X6 动力学、Working Truth 或正式 Result。原生 Site research writer 仍为静态只读、`research_authority_granted=false`；owner 查询为 `CONTROL_QUOTA`，本轮无原生新 Researcher-ID、CLAIM 或 Driver acceptance。GitHub 成功保存的作者侧材料与正式控制注册分开。

## 下一可执行单元

在同一科学 pin 下继续 `s=3,m=42`：证明 deg f_42<=252，使用84项 Newton 差分、253个互异整数点的恒等式证书；如尾部平移同号无法快速出现，则先输出精确有限符号反例/最小转折界并探查生成函数极点。并行结构路线：固定 k=5,6,14,15，研究 `sum_m D_m(k)z^m=1/Q_k(z)` 的有理函数极点/相位，解释相邻阶数的符号转折。
