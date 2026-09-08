# 正支撑压缩后的有限 raw 对偶证书：原空间保证与取等纤维

日期：2026-09-08。root 提供候选推导，独立子代理已完成第 7 节限定纸面复核，结论为 `BOUNDED_PAPER_PROOF_PASS`；这不是盲发现，也不是正式 Task、Result、Driver review、Working Truth 或 Foundation 变更。本篇没有运行新的数学程序，也没有声称实现了下述验证器。

目标是复用已有正支撑压缩，把一个明确有限的整数对偶证书变成对任意有限原始负支撑的保证。这个方向是已有 raw/Jordan 与有限证书工具的专门组合，不主张一般 L1 对偶原理的新颖性或新的全局工具族。

## 1. 实际覆盖检查与精确缺口

本轮实际调用 canonical `tools/enterprise_toolbox.py --json coverage`，查询 `raw X6 compressed carrier integer dual stability certificate`，返回 `REUSE_CANDIDATE_FOUND`。完整机器输出保存在本轮 owner 的覆盖证据中。查询命中了 `candidate.x6.positive_support_raw_compression_certificate`、`result.x6.positive_support_raw_l1_compression`、一正消费者、双正 bound/equality 论文及 T2 有限证书族等；这些匹配需要按合同判断，词面命中不等于执行。

已读取并复用的压缩合同保持全部 raw 三轴范数，却没有接收任意二十张整数表、穷尽压缩 carrier 上的势、再返回全空间线性稳定性界的接口。一正消费者仍只覆盖 p<=1；已有双正与 star 论文各给具体对偶。这一确切输入/输出缺口支持 `EXTEND_EXISTING_TOOL`，不支持宣称现有工具失效或重新发明另一套原生坐标。

## 2. 固定输入及有限载体

始终在同一外部锚点、带标号 signed raw X6 图中。两个有限正 BRC 人口先聚合并 Jordan 抵消，得到辅助 signed 数账

\[
f=\sum_{s\in S}w_s\delta_s-n,\quad w_s>0,\quad n\ge0,\quad n(S)=0,
\quad P=\sum_s w_s,\quad N=\sum_z n(z),\quad M=P+N.
\]

质量为有理数，可统一用严格正整数分子与共同分母书写；负号属于分析差，不是负 BRC primitive。这里先取非空有限 S。

按已证明的压缩法，令 `A_i={s_i:s in S}`，`c_i=max(A_i)+1`，`C_i=A_i union {c_i}`，`C=product_i C_i`。映射 `phi_i` 固定 A_i 中各值，把其余整数统一送至 c_i；`phi` 为逐坐标乘积。对任意三轴集合 I，记 `C_I=product_(i in I) C_i`。

正点完整纤维是 singleton：`phi^{-1}(s)={s}`。因此压缩后

\[
f'=\phi_*f=\sum_{s\in S}w_s\delta_s-n',\quad n'(S)=0,
\]

P、N、M 和二十张 raw 三轴表各自的 L1 范数均保持。若 `h_I,h'_I` 为压缩前后的表，则

\[
D=\sum_{|I|=3}\|h_I\|_1=\sum_{|I|=3}\|h'_I\|_1.
\]

`|C|=product_i(|A_i|+1)<=(|S|+1)^6` 是容纳大小，不是实际支撑数。这里只在该明确有限集合上提出证书条件，不把 phi 当物理等距或可逆坐标运动。

## 3. 有限整数证书定理

给定正整数 L、非负整数 B，以及二十张完全定义的整数表

\[
b_I:C_I\longrightarrow\mathbb Z,\qquad |b_I(t)|\le L.
\]

表只能查询自己的三轴地址。定义有限势 `F(z)=sum_(|I|=3) b_I(z_I)`。逐一核查全部 `z in C minus S` 满足

\[
F(z)\le-B,
\]

并记 `a_s=F(s)`；a_s 可以是 signed 分析整数，不要求它是正质量。则对于上述固定 S 上任意严格正权，以及任意有限原始负人口，均有

\[
\boxed{L D\ge\sum_{s\in S}a_s w_s+B N.}
\]

证明只需压缩及有限换序：

\[
L D\ge\sum_{I,t\in C_I}b_I(t)h'_I(t)
=\sum_s F(s)w_s-\sum_{z\in C\setminus S}F(z)n'(z)
\ge\sum_s a_s w_s+B N.
\]

如果另有正整数 A 满足所有 `a_s>=A` 且 `B>=A`，便得 `L D>=A M`。可把稳定性系数保留为规范未求值 `DIV(L,A)`；定理与核验只需整数乘加和比较，不要求计算商、根或浮点近似。若 A 条件不成立，有限势证书仍可能给出有用的非均匀正权线性界，不能把它误报为统一 M 界。

S 为空时单独用常值压缩到一个点，且已有 `D=20N=20M`；不调用空集合 max，也不通过空正点条件制造稳定性比值。零差另无须定义任何比值。

## 4. 完整间隙与原始取等支撑

记 `E'_I=sum_t(L|h'_I(t)|-b_I(t)h'_I(t))>=0`。上述线性界有完整恒等式

\[
\boxed{L D-\sum_s a_s w_s-B N
=\sum_I E'_I+\sum_{z\in C\setminus S}(-F(z)-B)n'(z).}
\]

因此取等当且仅当每个表级项与每个实际负权的势惩罚都为零。令有限紧集 `Z={z in C minus S:F(z)=-B}`，原始负支撑必须位于 `phi^{-1}(Z)`。

这不是允许任意反演压缩：当某个 z 含 fresh 坐标 c_i 时，它的原始纤维一般无限，单靠有限紧集不能把原始负支撑唯一限定成那些代表点。如果进一步核验 `Z subset product_i A_i`，则 Z 中每个点的完整原始纤维都是 singleton，取等负支撑才真正限制在原始有限集合 Z 中。随后仍需逐表零间隙条件求解权，不能只凭支撑条件宣布完整分类。

也可以直接在原表上拉回 `tilde b_I(t)=b_I(phi_I(t))`。其绝对值仍不超过 L，配对值与压缩表相同；压缩前后的范数也相同，所以原表与压缩表的间隙总和一致。此论证保留 raw 地址语义，不把 can3 单独使用，也不假定观察到未包含于 I 的坐标。

## 5. 与已冻结 star 对偶的接口对应

已有 star sharp 论文的整数对偶是 `L=21,B=78,a_s=78` 的具体实例，故统一式为 `21D>=78M`。结构论文的对偶在其 J 表取零，给出 `L=1,B=1,a_s=7`；把 J 表的实际范数另计，得到已证明的更强 `D>=7P+N+|P-N|`。固定正权论文的第二对偶对应 `L=1,B=0,(a_1,a_2,a_3)=(20,-4,-4)`，因此给出 `D>=24w_1-4P`。

这里只说明合同和公式如何组合；未运行这些表在压缩 carrier 上的枚举，也未声称存在覆盖任意三正点几何的同一 sharp 证书。尤其 `7/26` 的全体三正上界仍未解决。

## 6. 未来可执行核验的有限边界

若实现本方向，输入必须绑定实际 S 和逐轴 fresh 类，检查 canonical `Spatial6` 身份、二十组三轴标签、完整表定义域、整数系数及势界，并在枚举前检查显式 carrier 预算。预算不足属于无法在该预算内完成核验，不能判定数学命题为假。外来表、少一行、多余地址或旧 S 均不能被默认为有效证书。

程序应返回实查载体大小、正点势、负点最坏势、紧集是否具有 singleton 原始纤维及完整整数界。穷尽有限证书配合本定理可以证明该指定 S 的保证；少量样例通过不能替代完整载体检查。它不自动寻找最优对偶、不证明任意 S 的统一常数，也不恢复微观 BRC、路径/history 或 branch multiplicity。

本篇实际依赖的冻结来源：

| 来源 | SHA256 |
| --- | --- |
| `research_notes/OWNER_POSITIVE_SUPPORT_RAW_COMPRESSION_REVIEW_20260908.md` | `2cb061262e713859fd419871d0be9e4d5041698a01a46a55bd5ef5fc3f7e38b4` |
| `experiments/owner_positive_support_compression_20260908/check_positive_support_compression.py` | `f7e31ef40a2af4da1eaf0726068b212bb5efd66e82056ef91c8ee29581853660` |
| `research_notes/OWNER_THREE_POSITIVE_EQUAL_MASS_STRUCTURAL_REVIEW_20260908.md` | `47f12081c02090cc19de25b2c8ed234b6ed8a5ed300ea4fb13df4d8ff71dcda8` |
| `research_notes/OWNER_THREE_POSITIVE_STAR_SHARP_STABILITY_REVIEW_20260908.md` | `6a809986a77a5cc21deb8cdb4062af13d44993fc465b073111eaacf5f7671fe1` |
| `research_notes/OWNER_THREE_POSITIVE_STAR_WEIGHT_PROFILE_REVIEW_20260908.md` | `fe5169d2e5e093d21753ad27994825ecf4f58d9ea2fa19d042dd445e78b6e0e6` |

## 7. 独立限定复核与取等边界补足

独立审查者为 owner 子代理 `execution_gate_review`。被审作者原稿 SHA256 是 `8fed4b7a6f7a0eca2b19a04336ce5e5439d5675f7282b5f3649e329e6671b7d8`。本次全文读取原稿及压缩证明，核对以上五个来源的实际字节，并阅读既有覆盖输出中的明确命中项；该覆盖文件 SHA256 为 `24eaf9234d60cea5f8117c820f273e719c25cd33a30bfa0111a4e3332656f6ab`。没有重新执行覆盖查询、数学 consumer、有限载体枚举或求解器。以下是对候选证明的独立核对和边界说明，不是另一份正式数学接受。

**压缩的关键不仅是正 Cell 的 singleton 纤维。** 对每个 I，令 `T_I=pi_I(S)`。其中每个 raw 三元地址的各坐标都在对应 A_i 内，所以它在 `phi_I` 下的整个原始纤维也是 singleton；其表质量原本可能正、负或零，压缩均逐项固定。`T_I` 外没有正人口投影，故表质量非正，而且外部地址不能压入 `T_I`。其余纤维只合并非正项，遂有逐表 L1 等号。这也证明了第 4 节拉回表势的配对与间隙等式，未借用任何未被 I 观察的坐标。

**B=0 与非均匀正点势均在原定理内。** 证明只用了 `|b_I|<=L`、`F(z)<=-B` 及非负权，未除以 B，也未要求 a_s 为正。因而 `B=0` 时所得仍是 `L D>=sum_s a_s w_s`；即使部分 a_s 为负，该式也有准确含义。它不自行提供控制任意 N 的正系数统一 M 界。若另有质量约束，可另外推导，但不能省略该约束。

统一 A 的归约另有完整间隙。以第 4 节线性界的非负间隙记为 G，则

\[
L D-A M=G+\sum_s(a_s-A)w_s+(B-A)N.
\]

所以 `A>0`、全部 `a_s>=A` 和 `B>=A` 是第 3 节所用的充分条件；不能只取正点势的最小值而忽略 B。取这个统一界的等号时，除 G=0 外还须所有额外项为零。由于每个 w_s 严格为正，须全部 `a_s=A`；若 N>0 还须 `B=A`。N=0 时最后一项自动为零。特别地，B=0 不满足这一正 A 归约的 B 条件；第 5 节固定权对偶因此保留非均匀线性式，不被错误地提升。`DIV(L,A)` 只在 A 严格为正后作为规范符号系数使用。

**表级等号可以逐地址检验。** 每一项 `L|h'_I(t)|-b_I(t)h'_I(t)` 非负；它为零当且仅当：`h'_I(t)>0` 时 b_I(t)=L，`h'_I(t)<0` 时 b_I(t)=-L，`h'_I(t)=0` 时没有额外限制。等价地，严格内部系数 `|b_I(t)|<L` 强制该地址的 signed 质量为零。再加上每个实际负权只能位于 F=-B 的点，恰好给出第 4 节线性界的全部取等条件；只满足紧集支撑不是充分条件。

原始纤维可完全写为

\[
\phi^{-1}(\{z\})=\prod_i E_i(z_i),\qquad
E_i(z_i)=
\begin{cases}
\{z_i\},&z_i\in A_i,\\
\mathbb Z\setminus A_i,&z_i=c_i.
\end{cases}
\]

因此一个紧点的完整原始纤维为 singleton，当且仅当该点的所有坐标都属于对应 A_i。`Z subset product_i A_i` 正好保证所有紧点都具有这种性质，从而能直接把原始负支撑限制在有限 Z 内；这是无需进一步求权便可核验的充分步骤。若 Z 含 fresh 坐标，首先只能得到 `supp(n) subset phi^{-1}(Z)`，不能指定该 fresh 代表点为唯一原始位置。进一步的表级条件仍可能排除某些这样的紧点，所以不能反过来声称“未通过这个全 Z 检查就不可能完成任何有限取等分类”。Z 为空时线性取等强制 N=0。

**已有 star 对偶确实能通过同一压缩合同。** 活动轴的 A_i 是两个正端点，共同轴的 A_i 是共同坐标单点；三个已冻对偶的每张表只区分这些端点、共同坐标是否匹配及其余值。它们因而在每个 `phi_I` 纤维上恒定，限制到 C_I 后即满足本篇表类型。已冻论文的全原空间势界可限制到 C 使用。这是纸面接口对应，未伪称执行过 carrier 枚举，也没有给出任意三正点几何的统一 sharp 证书。

**退化与预算分支保持独立。** S 为空时 f 整体非正，每张 raw 表的 L1 都是 N，故 D=20N=20M；零差时二者为零，不定义比值，也不求空 A_i 的最大值。非空 S 的有限证书必须穷尽其实际 C 和全部表定义域；未完成预算内穷尽只能报告未完成。缺行、多余地址、非整数系数、旧 S 或势界反例则是该输入证书不合格，不能与资源不足混为一类。固定有限地址也没有把有理权变量变成有限多个样例。

限定结论：第 3 节线性定理、第 4 节完整间隙、原始紧集纤维条件及第 5 节三个具体接口对应均成立。本次只补本篇新纸面稿，来源论文、消费者、目录条目与正式研究状态均不改；未来程序仍须单独实现、核验和审查。

Global-Knowledge-Sync: main@eb09a0a / GLOBAL_KNOWLEDGE_V1
