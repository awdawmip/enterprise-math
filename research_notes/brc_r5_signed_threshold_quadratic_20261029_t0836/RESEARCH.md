# R5｜四维观察的有符号阈值与二变量二次可行性定理

**2026-10-29，作者侧可移植研究。** 状态：`AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED`。本结论限于此前的有限双测度序贯统计模型；不是原生 Heartbeat X6 动力学，也不是正式 Source Result、数学准入或独立审查。

## 输入和权限

冻结本轮唯一账户知识输入：`GLOBAL_KNOWLEDGE_V1 main@f7ab5d4dc91d41a028048a691a3b40b111ffdf48`。已读规范入口、Enterprise Math 项目路由、P000 投影（原文 Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`）、ACTIVE 世界观、BRC 与数学/代码规范。项目规范输入 `awdawmip/enterprise-math main@3d715614576c0687380028e764a179eeaa346fc8`；已读 AGENTS、P000、联合关系观察保真、Heartbeat-X6、portable/autonomous 协议。直接前沿为本 PR 的 `brc_r5_sensitive_tail_bellman_20261029_t0337`（含 greedy 的两实变量精确判据）与 `brc_r5_ancestor_boundary_20261029_t0750`（完整终端直方图非凸性，但不等于四维非凸）。

原生 Gateway 的 `research_authority_granted=false`、`active_jobs=5/5`、`executor_binding_configured=false`；活跃任务只读查询明确返回 `CONTROL_QUOTA`。未认证当前 owner、未取得 CLAIM、Result 或 Review；GitHub 作者侧保存不等于原生权限。

## 定理一：有限有符号阈值是声明错误的完整半空间描述

令终端似然比严格递增为 `s_1<...<s_m`，各签名的 Q 终止质量 `H_i>=0`，且 `sum H_i=sum s_i H_i=1`。终端随机声明 P 的质量为 `0<=z_i<=H_i`。记 `q=e_Q=sum z_i`，`b=1-e_P=sum s_i z_i`。则 **对全部实数随机声明**，`(q,b)` 可实现当且仅当

```
0 <= q <= sum_i H_i,
for every lambda in {s_1,...,s_m}:
 sum_{s_i<lambda}(s_i-lambda)*H_i
      <= b-lambda*q
      <= sum_{s_i>lambda}(s_i-lambda)*H_i.
```

证明：`b-lambda*q=sum(s_i-lambda)z_i`，每项独立在 `[0,H_i]` 中，分别选满负、正系数得到两个精确支持界。反向令 `Z(H)=sum_i[0,H_i](1,s_i)`。这是平面线段 Minkowski 和；非退化时其所有边平行于某个 `(1,s_i)`，故两侧的完整边法向仅为 `±(-s_i,1)`，恰好给出上述不等式。退化为一个斜率/零质量时，`q` 区间与阈值等式直接给出整个线段/原点。由此充分且包括零流边界。对于多个同签名终止历史，任何聚合 `z_i` 都可取共同终端声明概率 `z_i/H_i` 实现；**这个压缩只在未来无继续决策的终端声明操作上安全**。

这一形式取代旧 greedy fill 的分段 min/max，给出至多 `2m` 个固定方向的**线性**观测不等式，而非抽样检查。

## 定理二：来源敏感 diamond 真实四维集合的两实变量二次判据

固定原精确模型 `S=(1/2,1,3/2,5/2)`。root 继续概率为 `U`，两条独立可见路由的 Q 继续流为 `L,R`，在共同汇聚状态只能使用**一个**共享的新鲜无种子硬币 `gamma`。令

```
0<=L,R<=U<=1
h=(7/450)*L + (7/200)*R
M=gamma*h
TQ=1+U/2+(3/40)*L+(11/40)*R+M
TP=1+(3/4)*U+(3/40)*L+(33/80)*R+(3/2)*M
L=(80/3)*((3/2)*tQ-tP-1/2)
M=tQ-1-U/2-(3/40)*L-(11/40)*R.
```

对目标四向量 `(p,q,tP,tQ)`，`L` 已由停止时间确定，`M` 由 `U,R` 确定。gamma=0 时全程终端签名 Q 质量为 `H0=b0+U*bU+L*bL+R*bR`，来源敏感继续的签名增量为 `D=L*dL+R*dR`。下列全部向量按签名 S 排列，系数是旧 `mu,nu,eta` 严格正核和 BRC 来源路径 Q 质量的精确化简：

```
b0 = (1/2,0,1/2,0)
bU = (9/160,3/40,-9/40,3/32)
bL = (247/7200,-101/1800,7/450,1/160)
bR = (3/50,2/25,-6/25,1/10)
dL = (247/115200,67/19200,-1097/115200,7/1800)
dR = (3/640,13/1600,-69/3200,7/800)
```

`dL_s = v_A*eta_A(s)+v_B*eta_B(s)-1_{s=3/2}*(7/450)`，`dR` 同理，`v=(11/1200,23/3600)`、`w=(1/40,1/100)`，行列式 `det(v,w)=-49/720000`。严格有 `sum D_s=sum sD_s=0`。当 `h>0` 时 `H_s=H0_s+(M/h)D_s`；**不能**将来源敏感核替换为固定核。

**必要充分条件（全部实数 LR 策略）**：存在两个实数未知 `U,R` 使 `0<=U<=1`、`0<=L<=U`、`0<=R<=U`、`0<=M<=h`、`0<=q<=1`，并满足：

当 `h>0`，对每个 `lambda in S` 的八条不等式
```
sum_{s<lambda}(s-lambda)*(h*H0_s+M*D_s)
     <= h*((1-p)-lambda*q)
     <= sum_{s>lambda}(s-lambda)*(h*H0_s+M*D_s).
```
当 `h=0`，因为两个正系数迫使 `L=R=M=0`，必须回到未乘 `h` 的阈值不等式，采用 `H=H0(U,0,0)`。**不能**在零流时把乘 `h` 的式子当作合法声明检验，它会退化为无效的 `0<=0<=0`。

证明：必要性来自已验证的时间恒等式、精确来源流以及定理一；对 `h>0` 乘正数 h 得到所列式。充分性从可行 `U,R` 恢复 root 硬币 `U`、路由硬币 `L/U,R/U` 和汇聚硬币 `M/h`，零分母时取零。定理一恢复每一终端签名的声明硬币。所得是真正无持久随机种子的合法行为策略，四维观察恰为目标。证毕。

将四维观察值固定之后，`h,H0,D,M` 关于 `U,R` 均是仿射函数。因此八条式子是 **总次数 <=2 的有理多项式不等式**；其余是线性约束，加一个零流线性边界分支。即：旧 greedy 方案被化成两个未知数、固定八条二次不等式（再加线性约束）的**精确实数存在性问题**。实闭域量词消去保证代数输入的可判定性，但本轮**没有执行全局 CAD/QE，亦没有取得一份四维非凸性证书**。

## 精确执行结果与边界

`VERIFY.py` 使用标准库 `fractions.Fraction` 实际重算双测度的全部正概率核与似然比矩、来源流行列式、时间恒等式、终端分布不变量；以独立 greedy 作为 oracle，与 signed-threshold 和交叉乘二次式逐点核对：

```
(U,L,R,gamma)=(1,1/2,1/3,2/5)
h=7/360, M=7/900
H=(342407/576000,21713/288000,114047/576000,1903/14400)
O=(20558467/40320000,942727/2880000,581/300,5893/3600)
random legal rational policies=1600
random feasible/infeasible observer pairs=8000
dense rational (q,b) grid=2601; accepted=883; rejected=1718
PASS_EXACT_R5_SIGNED_THRESHOLD_QUADRATIC_ORACLE
```

上述有限检查只是算术和代码回归；完整实数结论来自上文证明。它不自动推出 `conv(O_full)=conv(O_LR)`、真实 `O_LR` 非凸，或原生 X6 对应。尤其**此固定 diamond 已知有严格 Bellman 支撑差距，不能作为母问题反例**。

## BRC 与后继工作

`BRC: REUSE_APPLIED`：在确定模型的未来继续行为时保留两个来源、两路正质量以及有符号的来源预测分布差 `D`；只在明确终止后把同 LR 的声明概率聚合。这是针对本有限观察操作的充分性证明，不是路径、来源或原生离散关系信息的普遍消去许可。

下一问题：在**新**模型上先以精确有理 LP/Farkas 证书确认全部有符号 full/LR 四维支持相等；再将候选完整历史观察点代入这种低维二次系统，用覆盖全部实数的 QE/符号隔离/SOS 证明确实无解。未通过支持相等的模型直接标记 NO_GO。先决条件不是有限随机样本或同一旧 diamond 的重复搜索。

参考来源：项目 PR #1663 上述两个前驱的精确模型；P. Gritzmann & B. Sturmfels (1993), *Minkowski Addition of Polytopes*, SIAM J. Discrete Math., DOI 10.1137/0406019（标准凸几何背景）；Tarski–Seidenberg 的半代数投影定理（https://ncatlab.org/nlab/show/Tarski-Seidenberg+theorem）。未检验新颖性或论文优先权。数学审查及正式 Source 准入保持待办。
