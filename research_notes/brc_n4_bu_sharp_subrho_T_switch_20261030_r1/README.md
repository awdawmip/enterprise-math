# BRC N=4 BU：低于 rho 的精确双相 minimax 曲线（作者侧）

**2026-10-30 · AUTHOR_ANALYTIC_PROOF / EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED。**
本成果只涉及严格正的16叶 P/Q 两律因果停止辅助模型，保留完整观察器 `(T_stop, Decision, Z_BU)`，不声称 P000 原生 X6、三维晶包层、独立心跳时间或真实物理规律的等价性。所有量词连续域定理**以已公开作者侧16叶→四原子因果约化及 L0/L3 合法可观察事件 TV 对偶为显式前提**，需后续独立审核。

## 新定理及已验证证据

对所有实数
[
193/200\le a\le97/100,\quad151/1000\le b\le303/2000,
]
定义
[
\delta=(1-a)/3,\quad B_*=b-\delta,\quad
w=(2a-7b)/(2a+4b),\quad C=(7-a-21b)/(4a+12b+2),
]
[
E=B_*C/4=\frac{(a+3b-1)(7-a-21b)}{12(4a+12b+2)},\quad
H=bw/4=\frac{b(2a-7b)}{8(a+2b)},
]
[
T(a,b)=a^2+38ab-7a+105b^2-14b.
]
在原始声明的全部合法实数随机因果策略类中：
[
\boxed{d_2(a,b)=d_{23}(a,b)=\min(E,H).}
]
`T<=0` 时取 `E`，`T>=0` 时取 `H`；实际策略换支曲线是
[
\boxed{b=\gamma(a)=(7-19a+\sqrt{256a^2+469a+49})/105.}
]
每个固定的 `a` 在该矩形内均发生严格换支。全域满足 `b>3/20`、`b/a<rho=(sqrt(5889)-25)/329`，内部 `a<97/100<49/50`，故与前一 E 带、旧高比率 H 区、a>=97/100 高 b 带以及目前未合并的 PR #1720 均不重复。

关键普遍对偶下界（以前序作者侧证明为前提）：
[
e\ge L_0(u)=\frac{4a-14b-3au-(a+3b)u^2}{2(23-2u)}\ (u\le3/7),\quad
e\ge L_3(u)=\frac{u(a-(a+3b)u)}{2(7-2u)}.
]
另外直接由 P 律完整观察事件和 `A<=1` 证明 `e>=B_*u/4`。设 `v=bw/B_*`，符号恒等式给出 `E-H=(1-a)T/[24(a+2b)(2a+6b+1)]` 以及
`L0(w)=L3(w)=H; L3(C)=E`。当 `T<=0`，三个区间 `[0,w],[w,C],[C,1]` 由 `L0,L3,容量事件` 覆盖并给出 `e>=E`；当 `T>=0`，区间 `[0,w],[w,v],[v,1]` 同理给出 `e>=H`（精确分解确保 `L3(v)>=H`）。匹配合法策略：
`(A,B,u,U,V)=(1,B_*,C,B_*(1+C),B_*)` 和
`(a,b,w,b(1+w),b)`；完整 Q/P 观察原子差分别为
`(delta,E-delta,0,-E)/(0,0,E,-E)` 和
`(0,H,0,-H)/(0,0,H,-H)`，两律 TV 均取相应最优值。

两个严格有理见证：`a=193/200,b=151/1000` 时 `T=-13/2000`、最优 `E=37411/2877000`；同一 `a`、`b=303/2000` 时 `T=16573/800000`、最优 `H=526917/40576000`。本轮实际执行 `SymPy+Fraction` 精确脚本，完成 **27 项符号检查、9 组严格正16叶完整 BU 来源观察、两律 TV 有理核对**；终端末行：
`PASS_BRC_N4_BU_SHARP_SUBRHO_T_SWITCH_AUTHOR_ONLY_20261030`。

## 完整可重现原件

同目录 `COMPLETE_EVIDENCE.tar.br` 为 **Git blob 35f6f5c4b64856a7562c1f14a8d3145556ce75e1**，存储完整且实际执行的四份非空文件：`PROOF.md`（全文/连续域证明）、`VERIFY.py`（源码）、`VERIFY_EVIDENCE.txt`（原样 stdout）、`NEXT_TASK.md`（下一问题）。压缩包按 Brotli 11 压缩标准 TAR，档案原始字节 SHA-256 为 `b470b83df0f0072402d2b3a7af38348a35f42fb2096fe00f0b5296d5b84a6b96`；解压可用 Python `brotli.decompress` 再用标准库 `tarfile` 读取。四份研究源含精确分母、端点多项式、完整策略和旧成果不重做边界。

科学输入：Enterprise Math `main@ac546e5b50de499db81910d12855301391351e21`；GLOBAL_KNOWLEDGE_V1 `main@3f0674bcb634851783368c406b1c2269c0bd0748`，P000 启动投影与原件 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` 一致；历史继承入口：`1a4898a57e952245eeacb38be7adf109faa49f49`、`503308309c6a2f703ff82bd075fae9d79b312441` 及 PR #1720。实际 GitHub 登录 `awdawmip`；原生 Site `v0.6.11` 仅 `source:read/control:read`，`research_authority_granted=false`，当前 Owner 尚待 Source 核验。本次是研究文件持久化，**不是**原生 CLAIM、Result、审阅、Working Truth 或数学接纳。

**下一步：** 判定可扩大至何种精确半代数域仍保持 `min(E,H)`；选择一个刚跨越对偶证书有效域的有理点，提供新联合事件 TV 下界或严格更优合法策略。另需独立复核 L0/L3 事件混合权重及16叶到四原子的全部策略无损约化，最后研究向 P000 X6 原生携带者与未来观察的保真映射。
