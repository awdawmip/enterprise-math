# R467｜signed BRC 辅助标量右缘 s=201–208 的无限参数正性证书

日期：2026-11-02。状态：作者侧精确整数／符号计算机辅助证明；尚待独立数学审查与正式 Result 接纳。

## 固定输入和数学对象

规范读取（本轮同一快照）：GLOBAL_KNOWLEDGE_V1 main@7dc75fa683495777ad29736d88c55f7c3b314cad；Enterprise Math main@284995fa2e77fca69707ca4f5cd5eb865b54cd48。科学冻结输入沿用 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；上一证书前沿 R466@b70a0c06d6743071665df31209d97b7e34b3f81a。P000 及 ACTIVE 世界观均未修改。本命题仅针对 signed BRC 辅助标量模型。

对奇数 $r=2k+1$、整数 $2\le s\le r$，定义

$$
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.
$$

设 $a_j=H(r,r-j)$（$0\le j\le r-2$；越界置零），相邻 Toeplitz 子式

$$
D_{2,j}=a_j^2-a_{j-1}a_{j+1},
\qquad
D_{3,j}=\det(a_{j+v-i})_{i,v=0}^{2}.
$$

**本轮命题**：对每个固定整数 $s\in\{201,202,\ldots,208\}$，对所有整数 $k\ge k_0=\lfloor(s+2)/2\rfloor$，取 $j=2k+1-s$，则 $D_{2,j}>0$ 与 $D_{3,j}>0$。

## 证明与检查范围

沿用冻结 R462/R452 的 E/O/R 精确恒等式，令 $C_k=\binom{2k}{k}/(k+1)>0$ 与 $B_t(k)=H(2k+1,t)/C_k$。对于每个固定 $s$，设 $u=k-k_0\ge0$、$F=(2s+4)!$、$Q_t(u)=F B_t(k_0+u)\in\mathbb Z[u]$（$t=s-2,\ldots,s+2$）。记

$$
A=Q_s,\ B=Q_{s-1},\ C=Q_{s+1},\ D=Q_{s-2},\ E=Q_{s+2}.
$$

构造

$$
P_2=A^2-BC,\qquad
P_3=A^3-2ABC+DC^2+B^2E-DAE.
$$

按原定义 $D_{2,j}=C_k^2P_2(u)/F^2$，$D_{3,j}=C_k^3P_3(u)/F^3$。八个 $s$ 逐一精确展开后，均有 $\deg P_2=4s$、$\deg P_3=6s$，**全部系数严格为正**；共16个参数化整数多项式、16,376个严格正系数。因为 $u\ge0$，即推出每个指定 $s$ 对无限多个合法整数 $k$ 的正性。

独立代数一致性核验对每个 $s$ 检查完整整数多项式恒等式

$$
A P_3=P_2^2-(B^2-DA)(C^2-AE).
$$

另在 $k=k_0,k_0+1$、$t=s-2,\ldots,s+2$ 完成80项原始 signed 卷积、80项正 Catalan 公式交叉核验。全部符号运算使用 Python 无界整数；非负整数多项式乘法可采用精确 Kronecker 编码，含负系数时采用原始整数卷积。八个正系数流的 SHA256、次数和起始域见 R467_EVIDENCE.json，实际分段运算每个 s 均通过。

## 条件性 PF₃ 拼接至 r=231

沿用 R447 的左缘 $0\le j\le22$、先前 R452–R466 覆盖的右缘 $2\le s\le200$ 以及本轮的新右缘 $s\le208$。对奇数 $99\le r\le231$，当 $j\ge23$ 时，$s=r-j\le208$，因此两侧覆盖全部合法位置。结合 R450 的局部充分判据及此前作者侧依赖，得到**条件性** $T^{(r)}\in PF_3$，新增 $r=225,227,229,231$。

本轮另采用独立正 Catalan 整数表达式，在这四个 $r$ 上逐一检查908项正系数、908项严格正二阶相邻子式、908项严格正三阶相邻子式，共**2724项**精确判号；32项原始 signed 卷积与32项交替 Catalan 恒等式交叉核验通过。R467_ROW_EVIDENCE.json 记录两个长度前缀整数流哈希；R467_ROW_VERIFY.py 可复核。R447/R450 的半无限 PF₃ 推论及其依赖仍以各自未独立审核的原始证明为依据。

## 复现、活动与未完成问题

在完整 Git 分支内执行：

    python research_notes/r467_signed_brc_right_edge_201_208_20261102_emr3/R467_REPRODUCE.py 201 208
    python research_notes/r467_signed_brc_right_edge_201_208_20261102_emr3/R467_ROW_VERIFY.py

首个脚本直接重用已发布 R466 目录的 R465_EXECUTED_REPRODUCE.py 与其 R462_VERIFY_FROZEN_KERNEL.py；实际首次计算分段完成 s=201–208，随后本轮以 s=201 单独运行包装器再次通过。整行脚本本轮独立执行通过。GitHub 身份 awdawmip 具有 push 权限；原生 em_session_start 返回 STATIC_READONLY_SCOPE_DENIED / operation_sent=false，活跃 Owner 查询返回 CONTROL_QUOTA。因此当前为作者侧 GitHub 持久化研究，正式 CLAIM、Result、Review 和 Research Activity 仍待有权会话办理。

下一研究单元：完成 s=209–216 的正系数证书并检查对应 r=233,235,237,239；同时考察 s、k 联合增长下 E/O/R–Turán 凝聚的统一正性下界或反例。