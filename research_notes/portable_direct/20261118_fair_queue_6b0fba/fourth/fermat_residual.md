# 费马平方链的奇部碰撞筛与零进位阈值

任务 `RS-FERMAT-RESIDUAL-PRETERMINAL-20261004`，发布 `TP2-F1B81F13E3750A4181C1`。令 $F_n=2^{2^n}+1$，$x_j=2^{2^j}$，奇数 $q\ge3$ 的中心余数是唯一满足 $r_j\equiv x_j\pmod q,\ 2|r_j|<q$ 的整数。下述前缀筛给出比候选不整除更强的结论 $\gcd(q,F_n)=1$，可以在给定高度 $h<n$ 停止。其依据是经典的乘法阶条件。本次提取了在已算中心余数上发现短阶证书的判据、它与旧筛的严格差别，以及接收方重验的实际成本。[冻结任务书](https://github.com/awdawmip/enterprise-math/blob/919cd6838cc4a6a7a58d3fd3ba264e8a18e32d13/research_tasks/RS-FERMAT-RESIDUAL-PRETERMINAL-20261004.md)

## 从两个中心余数提取短阶证书

**命题。** 写 $r_j=\sigma_j 2^{b_j}m_j$，其中 $\sigma_j=\pm1$，$m_j>0$ 为奇数，置 $E_j=2^j-b_j$。若 $0\le i<j\le h<n$，$m_i=m_j$ 且 $E_i\ne E_j$，便有 $\gcd(q,F_n)=1$。

中心代表元满足 $0<|r_j|\le x_j$，故 $0\le E_j\le2^j$。因 2 在模 $q$ 上可逆，每个奇部满足 $m_j\equiv\sigma_j2^{E_j}\pmod q$。等奇部给出

$$
2^\delta\equiv\sigma_i\sigma_j\pmod q,\qquad
0<\delta=|E_j-E_i|\le 2^h<2^n.
$$

假定奇素数 $p$ 同时整除 $q,F_n$。平方 $2^{2^n}\equiv-1\pmod p$ 得 $\operatorname{ord}_p(2)=2^{n+1}$。另一方面 $2^{2\delta}\equiv1\pmod p$，而 $0<2\delta<2^{n+1}$，矛盾。此推导覆盖奇合数及其重素因子。注意在无折返段，每个 $m_j=1,E_j=0$，相同的 $E$ 必须跳过。

对 $q\ge5$，初态的 $(m_0,E_0)=(1,0)$，因此提前出现 $|r_j|=1$ 或新出现的其他带符号二幂均可检测。两个不同高度若 $|r_i|=|r_j|$，则 $b_i=b_j$、$E_i\ne E_j$，所以绝对值重复也被覆盖。留出区内的素数例为 $n=6,q=262657$，在第五步 $r_5=32$ 即获 $2^{27}\equiv1\pmod q$。该数的素性可用试除到 512 核验，判据自身无需试素。另有 $n=7,q=130561$，$r_5=32640=2^7\cdot255$，$r_6=-8160=-2^5\cdot255$，给出 $2^{34}\equiv-1\pmod q$。两例在全预算内都没有提前到达 ±1 或重复绝对值。

还有一族可在生成时验证的旧筛分离例。取 $j<n$，$\max(n+2,2^{j-1}+1)\le t\le2^j-1$，$q=2^t+1$。该候选满足经典同余 $q\equiv1\pmod{2^{n+2}}$。早于 $j$ 的余数都是原始二幂，至 $j$ 得 $r_j=-2^{2^j-t}$。若 $2^j-t$ 不是二幂，则绝对值尚未重复，且 $|r_j|>1$。奇部碰撞给出 $2^t\equiv-1\pmod q$。例如每个 $n\ge6$ 取 $j=n-1,t=2^{n-1}-3$ 均可。这一构造使用公开的二幂同余，实际筛还覆盖其他算术形状。

## 观察者丢弃模数时的精确阈值

固定 $q\ge5$ 为奇数，只交给观察者中心余数前缀 $z=(2,z_1,\dots,z_h)$。置 $L=2\max_j|z_j|$，$D=\gcd_{j<h}|z_j^2-z_{j+1}|$，空集的 gcd 取 0。**与此前缀相容的模数恰是全部满足 $q>L,\ q\mid D$ 的奇数。** 这些条件逐步保证同余且代表元居中，充分性来自平方递推的唯一性。若同时交付进位 $c_j=(z_j^2-z_{j+1})/q$，则出现首个非零进位时可准确恢复 $q$。所有进位均为零恰当 $q>2x_h$，这时 $z_j=x_j$，商 $A_j=(x_j-z_j)/q$ 也全为零。

留出区的 $n=6,h=4,q=274177,274433$ 同余于 1 模 256，均超过 $2x_4=131072$。两者的余数、商、进位分别都是同一个序列，但 $F_6=274177\cdot67280421310721$ 且 $\gcd(274433,F_6)=1$。因此任何只接收这些数值前缀、舍弃 $q$ 身份且要求零错误的方法，在该共同状态上必须保留未知。持有模数者仍可执行上面的证书检验；两个命题的观察预算不同。独立脚本对 $5\le q\le513$ 的全部 255 个奇数、$0\le h\le5$ 的每个实际余数等值类都验证了模数集合公式。

## 冻结试验与成本

每次只输入 $n,k$，生成 $q=1+2^{n+2}k$，预算 $h=n-1$。开发集取 $n=6,\ 1\le k\le512$。留出集取 $n=6,\ 513\le k\le2048$，以及 $n=7,8,\ 1\le k\le2048$。规则、两个区间和处理程序在读取留出标签前冻结，脚本 SHA-256 为 `ccbf5629aa6e725d676316ede82ee02dee4d34159470137adb0658cf6f9336d2`。证书只读已到达的余数。审计标签随后独立由整数 $\gcd(q,F_n)$ 计算；细分真因子、与 $F_n$ 相等、其余。所有入选候选均严格小于 $F_n$。

| 计量 | 开发 | 留出 |
|---|---:|---:|
| 同一范围内奇数个数 | 65,536 | 1,769,472 |
| 仅按经典同余生成的候选 | 512 | 5,632 |
| 对全部奇数各算 $n$ 次所需模平方（解析计数） | 393,216 | 13,238,272 |
| 对全部同余候选各算 $n$ 次 | 3,072 | 39,936 |
| 提前 ±1 排除数 / 含剩余终点回退的模平方 | 2 / 3,067 | 2 / 39,929 |
| 提前 ±1 或绝对值重复排除数 / 同口径模平方 | 10 / 3,056 | 22 / 39,883 |
| 奇部碰撞排除数 / 同口径模平方 | 14 / 3,048 | 43 / 39,834 |
| 奇部在线首次命中方案所需探测次数 | 3,062 | 39,877 |
| 独立复验所有短阶证书的模平方 / 模倍增 | 48 / 21 | 174 / 86 |
| 筛后未知 / 回退证实的真因子 | 498 / 0 | 5,589 / 1 |

为比较各方案，检查器实际对每项走完 $h$ 步，开发和留出各走 2,560、34,304 次模平方。表中在线成本由逐项首次命中位置恢复，未中者回退到 $n$。不使用筛表或素数分解，每项生成候选需一次移位和一次加法。每个受检余数做绝对值、取最低非零位、位长、移位和确切奇部的字典查找。保存至多 $h+1$ 项。若 $B=\lceil\log_2(q+1)\rceil$，每个奇部和余数至多 $B$ 位，$E_j$ 至多 $h+1$ 位，故流式工作储存为 $O((h+1)(B+h+1))$ 位并带常数个程序对象。这里开发最大候选 18 位，留出最大 22 位。整模平方被约减前至多 $2B$ 位。标签最大为 257 位，只用于审计。

短证书由 $(n,q,\delta,\sigma_i\sigma_j)$ 组成，接收方独立用从高位到低位的二进制幂检查；每张耗 $\operatorname{bitlen}(\delta)-1$ 次模平方和 $\operatorname{popcount}(\delta)-1$ 次模倍增。独立脚本还核对来源行及其两个中心余数，这一审计额外使用两次模幂调用。留出区在线节省 102 次模平方，超过“±1 或绝对值重复”基线 49 次；逐张重验额外需要 174 次模平方，重验计入后已超过直接模平方的 39,936 次。故数据仅支持新增前缀排除和可携带证书，不支持端到端加速。唯一真因子在筛中保留未知，回退才命中。筛后未知的候选仍要完成整除验证。

## 提升接口与复算

由 $x_j=qA_j+r_j$ 的平方恒等式直接得 $A_{j+1}=qA_j^2+2r_j A_j+c_j$。约化到第一隐藏位 $u_j=A_j\bmod q$ 后，使用冻结 BRC 模块的 `Affine.identity(1).then(step)` 按来源顺序复合整系数作用 $u\mapsto2r_j u+c_j$，最后 `apply` 取模。该接口的单条有序路径保留每一步 $(r_j,c_j,r_{j+1},u_{j+1})$。在 $(q,h)=(3,5),(9,5),(25,6),(641,5)$ 的 21 条边逐个与直接模 $q^2$ 比较，641 仅用于校准 $(r_5,u_5)=(-1,44)$。以一个整数 $q$ 上的单条平方链为载体，此处全部结果属外部数论。LIFT 研究 $q^k$ 的高阶进位和截面，MEMORY 研究给定模数的平方状态及允许后缀；这里处理候选首层整除和舍弃模数身份后的前缀，既有仿射律未作新定理。当前仍缺能在计入探测和第三方验证后普遍省时的候选族，及覆盖本筛未决模数的有效证书。[种子和来源说明](https://github.com/awdawmip/enterprise-math/tree/919cd6838cc4a6a7a58d3fd3ba264e8a18e32d13/research_inputs/fermat_residual_20261004) · [LIFT](https://github.com/awdawmip/enterprise-math/blob/919cd6838cc4a6a7a58d3fd3ba264e8a18e32d13/research_tasks/RS-FERMAT-RESIDUAL-LIFT-20261004.md) · [MEMORY](https://github.com/awdawmip/enterprise-math/blob/919cd6838cc4a6a7a58d3fd3ba264e8a18e32d13/research_tasks/RS-FERMAT-RESIDUAL-MEMORY-20261004.md) · [BRC 仿射实现](https://github.com/awdawmip/enterprise-math/blob/919cd6838cc4a6a7a58d3fd3ba264e8a18e32d13/src/enterprise_math/brc_transport.py)

在本页同目录运行下列命令，`EM_SOURCE_ROOT` 指向上述冻结版仓库检出。两个稀疏 JSON 的 `exceptions` 按 $(n,k)$ 列出所有偏离默认值的候选。列依次为 $n,k,q$、提前 ±1 层、绝对值重复层、奇部证书 $[i,j,r_i,r_j,E_i,E_j]$、gcd、整除标签。省略行的三个前缀观察都是未知，gcd 为 1，标签为 `no`。生成器和区间确定了所有省略行。开发、留出 JSON 的 SHA-256 依次为 `6ab7380688c3bd7170c11df37df8a831e947c0aab8594b91c105c0942e64d661`、`8bb350d4c99dcf872fe67ce04778ef1a9c5004ed0da511f95f06bb945afb7adb`。

```sh
python3 fermat_residual_check.py development --ledger fermat_residual_development.json
python3 fermat_residual_check.py holdout --ledger fermat_residual_holdout.json
python3 fermat_residual_certificate.py
python3 fermat_residual_check.py calibration --repo "$EM_SOURCE_ROOT"
```
