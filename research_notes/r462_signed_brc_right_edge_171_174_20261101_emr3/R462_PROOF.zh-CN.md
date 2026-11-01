# R462 | signed BRC 辅助标量：四个新的无限参数正性证书和 r=195、197 拼接

日期：2026-11-01。证据性质：AUTHOR_SIDE_EXACT_SYMBOLIC_AND_INTEGER；未经独立 Driver 审查，未正式接纳。

## 版本与研究对象

规范已按当前 GLOBAL_KNOWLEDGE_V1 main`0d6024a1bc66fabd689753a0e8a99f90c8d5e433` 和 Enterprise Math main`996d6ef33dfbb8a3a8902ea81e9ff09b18053a56` 读取；科学前沿仍固定于 R461 不可变提交 `93edee01b55905671c3797616daf072bed5a802b`，此前 R447（左缘）、R450（PF₃ 局部判据）、R452（EOR 因子分解）为依赖。P000、ACTIVE 世界观均未修改。

定义奇数 `r=2k+1`、`2<=s<=r` 时的原始 signed BRC 标量
`H(r,s)=binom(r+s,2s) [t^r] (1-t)(1+t)^(2s)(1+t²)^(r-s)`。
令 `a_j=H(r,r-j)` (j=0,...,r-2，其余为零)，
`D2_j=a_j²-a_(j-1)a_(j+1)` 和 `D3_j=det(a_(j+v-i))_{i,v=0,1,2}`。

**定理 A：** 对 `s in {171,172,173,174}` 和所有整数 `k>=floor((s+2)/2)`，有 `D2_(r-s)>0` 及 `D3_(r-s)>0`。

## 精确符号证明与复现

令 `C_k=binom(2k,k)/(k+1)>0`，`B_t(k)=H(2k+1,t)/C_k`。沿用 R452 恒等式 `(2t)!B_t(k)=E_t(k)O_t(k)R_t(k)`，其中
`E_t=prod_{v=0}^{t-1}2(k+1-floor(t/2)+v)`，
`O_t=prod_{v=0}^{floor(t/2)}(2k+2v+1)`，
`R_t=sum_{q=0}^{floor((t-1)/2)} binom(t-1,2q)2^q prod_{v=q}^{floor((t-1)/2)-1}(2k-2v-1) prod_{d=0}^{q-1}(k+1-d)`。

对于每个固定 s，取 `k0=floor((s+2)/2)`，`u=k-k0>=0`，`F=(2s+4)!`，定义 `Q_t(u)=F B_t(k0+u) in Z[u]`，t=s-2,...,s+2。设 `A=Q_s, B=Q_(s-1), C=Q_(s+1), D=Q_(s-2), E=Q_(s+2)`，则精确地
`P2=A²-BC`，`P3=A³-2ABC+DC²+B²E-DAE`，及
`D2_(r-s)=C_k²P2(u)/F²`，`D3_(r-s)=C_k³P3(u)/F³`。

使用 `R462_VERIFY.py` 的整数系数多项式乘法，在 s=171,172,173,174 **逐一完整检查** `P2,P3` 系数均严格为正；因此 u>=0 时两多项式严格正，推出定理 A。再逐个验证全多项式 Desnanot–Jacobi 恒等式
`A*P3=P2²-(B²-DA)(C²-AE)`；
另外在 k=k0,k0+1 和 t=s-2,...,s+2 对原始带符号卷积与独立 Catalan 表达式进行 40+40 项精确整数交叉检查。

| s | k0 | deg P2 | deg P3 | 正系数个数 | SHA256（整数流） |
|---:|---:|---:|---:|---:|---|
|171|86|684|1026|1712|`1eb864890e11ede658eda5d4d7779134c1f4286f15aaf40e1a893094bf77aded`|
|172|87|688|1032|1722|`e7c9f29600a04f3e9b0c4b48d854eeccefba6fa2316a4d54bdd3e4b166a12705`|
|173|87|692|1038|1732|`3639159c28374e7d2146622d267b98d1216ce77380ac2506dd24ee9f427f2836`|
|174|88|696|1044|1742|`789fb832f423b122be24cafbb71bbb3702bb8d13ed75dceee761e27528e1839f`|

合计 **8 个整数多项式，6908 个严格正系数、4 个全多项式凝聚恒等式**。四个单点进程均分别正常以 `R462_EXACT_PASS` 结束；先前一轮跨 173—178 的批运行中断，该中断并不被计为全区间验证。

## PF₃ 拼接与独立整数整行检查

由 R447 左边缘证书，所有奇数 r>=99 的 j<=22 已覆盖；由 R452—R461 及定理 A，右边缘 s<=174 覆盖。对 r=195，j>=23 蕴含 s=r-j<=172；对 r=197，j>=23 蕴含 s<=174。这两行的全部合法相邻二、三阶子式严格正。在 R450 局部充分判据等历史作者侧结论成立的共同前提下得到 `T^(195),T^(197) in PF3`，先前的奇数 r=99,...,193 拼接链延展至 r=197。

另运行 `R462_ROW_VERIFY.py` 用整数 Catalan 公式直接构造两行，逐项核对 390 个正系数、390 个正二阶子式、390 个正三阶子式（总 **1170 项**），另核对 16 个原始带符号卷积和 16 个交替 Catalan 公式。该固定参数整数检查独立于 R452 多项式正系数路线。签名流哈希在证据 JSON 中。

## 作用域、真实权限、下一问题

全部结果针对 signed BRC **辅助标量模型**。R447/R450 等先前数学依赖尚未被独立审阅；不自动赋予原生 X6 时间动力学、Working Truth、Foundation 或正式 Task Result 资格。

本轮 GitHub 当前连接用户为 `awdawmip`。原生研究会话启动以 `STATIC_READONLY_SCOPE_DENIED` 拒绝（operation_sent=false），活跃 Owner 清单因 `CONTROL_QUOTA` 未取得；所以未登记正式研究活动，也未声明任何 CLAIM、Result、Driver 审查或接纳。将作者侧证据保存于现有 Draft PR 分支。

复现（Python 任意精度整数）：
```bash
for s in 171 172 173 174; do python R462_VERIFY.py "$s" "$s"; done
python R462_ROW_VERIFY.py
```

下一步检查 s=175、176；另外用 EOR 分解和 Turán 凝聚寻找 s,k 同时无界增长时的统一正性下界或严格反例。
