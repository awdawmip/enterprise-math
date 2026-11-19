# 本原 Gaussian 直线上的最小分裂极化：二处和三处的六次方代价

在 $K=\mathbf Q(i)$ 的格 $L=\mathbf Z[i]^6$ 上取
$$
 H=\operatorname{diag}(1,1,1,-1,-1,-3).
$$
选本原向量 $u$（坐标生成单位理想），令 $n=u^*Hu\ne0$。固定 $Ku$ 成为 Hodge 子结构的六维子域，在其中取很一般的点。问在**同一个整格**上，与原 $K$ 作用相容而判别式为 $[-1]$ 的整极化，其 Euler 特征 $\chi$ 最小是多少？极化映射的度等于 $\chi^2$。第十四轮算出标准正线的 $\chi=9$ 和标准负线的 $\chi=1$。任意本原定号线的答案有时比这两个值大任意多倍。[原始非分裂模型](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_returns/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_RETURN_20260902.md) · [标准线、极化轨迹与既有文献](https://github.com/awdawmip/enterprise-math/blob/4cb5cbccfaa386790d82f99290135ad3135e1125/research_notes/portable_direct/20261118_fair_queue_6b0fba/fourteenth/weil.md)

## 两个正整数已经决定全部代价

设 $b=Hu$，其各坐标的 Gaussian 公因子理想写为 $(g)$。由于 $u$ 本原且 $H$ 的前五个对角元为单位，$(g)$ 整除 $(3)$。素数 3 在 $\mathbf Z[i]$ 中惰性，可唯一选 $g\in\{1,3\}$。用 $t=g$，$a=|n|/t$。当 $t=3$ 时，前五坐标都是 3 的倍数而 $u_6$ 不是，所以 $v_3(n)=1$，$a$ 与 3 互素。

**整数极化公式。** 令 $\mathcal N$ 为 $K^\times$ 中元素的正有理范数。所求最小值是
$$
 S_t(a)=\min\left\{\frac3t AB^5\ :\ A,B\in\mathbf Z_{>0},\quad A\equiv tB\pmod a,\quad \frac3t AB\in\mathcal N\right\}.\tag{1}
$$
当 $a=1$ 时同余条件恒成立。每一对合格的 $(A,B)$ 均给出实际的整极化。公式只需知道向量的范数和 $Hu$ 的公因子，不要求把该直线补成整正交基。

为看清整性，在 $Ku$ 与 $u^\perp$ 上分别用正有理数 $x,y$ 乘原形式。新矩阵为
$$
 H'=yH+\frac{x-y}{n}bb^* .
$$
这列尽很一般点的相容形式。具体地，一个有理自伴算子若保持该子域上很一般的 Hodge 分解，其闭保持条件便在整个子域成立。对正线，正三面的交恢复该直线，去掉它后，正交补中变化的所有正二面迫使算子为标量。对负线，正三面全部位于五维补空间，张成该补空间，在其中同样迫使算子为标量。两种情形均可把正子空间开集的保持条件延至整个 Grassmannian，再以子空间的交恢复直线。自伴性给出余下的块，且两标量为实有理数。整性由原交替型 $\frac12\operatorname{Tr}(ih')$ 判定，对 Gaussian 格等价于 $H'$ 各元为 Gaussian 整数，分别在基向量及其 $i$ 倍取值即可。

首先 $y$ 必须是整数。若某 Gaussian 素元处 $y$ 的赋值为 $-k<0$，以该素元的 $k$ 次方乘等式并约化。左边为零，$yH$ 项的剩余秩至少为五，而余下的整矩阵秩至多一，矛盾。现在 $bb^*$ 全体矩阵元生成 $(t^2)$，故整性剩下一个条件 $(x-y)t^2/n\in\mathbf Z$。这恰说明 $B=y$ 和 $A=tx$ 为正整数，且 $A\equiv tB\pmod a$。反向代入即得充分性。由 $\det H'=-3xy^5$，与原交替形式的归一化相同，$\chi=3xy^5$。分裂要求 $3xy^5$ 为范数，正有理四次幂 $y^4$ 可约去，于是得到 (1)。正性保证给出极化；此处只按极化形式计代价。

## 最小值的局部下降律

令 $h=v_2(a),\ k=v_3(a)$，置 $s=2^{\max(h-1,0)}3^k$。两型都满足
$$
                  S_t(a)=s^6 S_t(a/s).\tag{2}
$$
事实上 $(A,B)\mapsto (sA,sB)$ 在两边的所有合格整数对之间给出双射。因此约去这些因子以后，余下的模数与 3 互素，且至多含一个因子 2。

在 3 处，若 $k>0$ 则 $t=1$。一旦 $v_3(B)<k$，同余迫使 $v_3(A)=v_3(B)$，使 $3AB$ 的 3 进赋值为奇数，不能是 Gaussian 范数。故 $3^k$ 整除 $A,B$。在 2 处，若 $r=v_2(B)<h-1$，写 $B=2^r B_0$，同余迫使 $A=2^r A_0$ 且 $A_0\equiv tB_0\pmod4$。于是 $\frac3t A_0B_0\equiv3\pmod4$。奇整数若是有理 Gaussian 范数，必等于 $1\bmod4$，例如由所有 $3\bmod4$ 素数的赋值均偶立即得到。除以平方 $2^{2r}$ 不影响范数条件，故出现矛盾。将两者的必需因子约去，范数只变一个有理平方；同余模数同时除以 $s$。这就证明了双射和六次幂。

**两个取到等号的族。** 对 $a=1,2$ 均有 $S_1(a)=9$、$S_3(a)=1$。第一式由 $(3,1)$ 达到，小于 9 的正候选只给 $3$ 或 $6$，均有奇数的 3 进赋值。第二式取 $(1,1)$。因此
$$
 S_1(2^h3^k)=9\bigl(2^{\max(h-1,0)}3^k\bigr)^6,
 \qquad S_3(2^h)=2^{6\max(h-1,0)} .\tag{3}
$$
第一族的每个正范数 $M$ 都有 $t=1$ 的本原向量。例如 $M=2m$ 取 $(1,m,0,m-1,0,0)$，$M=2m+1$ 取 $(1,m,1,m-1,0,0)$。第二族取 $(3,0,0,3,0,(1+i)^h)$，其范数为 $-3\cdot2^h$，且本原。特别地，第一型总可取 $(3a,a)$ 得 $S_1(a)\le9a^6$；$a=3^k$ 在任意大的尺度上达到这个上界。

两条线甚至可以有**相同的带号范数**而极化成本不同。把第一族向量的分奇偶公式也用于负整数，和第二族同时取 $n=-3\cdot2^h$。由 (3)，$t=1$ 那条线的最小 $\chi$ 恒为 $t=3$ 那条的 $3^8=6561$ 倍，极化映射的最小度之比为 $3^{16}$。

另一端也可精确达到。对 $t=1$，$A=B$ 会使 $3AB$ 的 3 进赋值为奇数。所以 $A>B$ 时 $A\ge a+1$，$B>A$ 时 $B\ge a+1$。从而 $S_1(a)\ge3(a+1)$，等号恰在 $3(a+1)\in\mathcal N$ 时由 $(a+1,1)$ 达到。比如 $a=3j^2-1$ 对每个 $j\ge1$ 给出一条线性代价族。同一固定格上的算术差异由此既可线性增长，也可六次增长。

对 $t=3$ 且 $a\ge4$，也有 $S_3(a)\ge a+3$。$A=3B$ 不符合范数条件；若 $A>3B$ 则 $A\ge a+3$，若 $A<3B$ 则 $B\ge\lceil(a+1)/3\rceil$，此时 $B^5>a+3$。故等号恰在 $a+3$ 为范数时，由 $(a+3,1)$ 实现。每个与 3 互素的 $a$ 均能出现：取 $z=1$ 或 $1+i$ 使 $N(z)\equiv a\pmod3$，在前五维的 $(3,2)$ 型上用上述奇偶公式取首坐标为 1、带号范数为 $(N(z)-a)/3$ 的整向量。将其乘 3 再附上第六坐标 $z$，所得向量本原，$g=3$ 且 $n=-3a$。例如 $a=j^2-3\ge4$、$3\nmid j$ 即构成这一型的线性等号族。

## 范围与复算

这是 H0N 固定格上六维特殊子域的独立算术分支。九维域上 H0R 所需的 H0P 九方向正对象仍缺，该方向本轮的正式服务计数为零。很一般点的限定是在指定直线子域**内**，有额外 Hodge 自同态的特殊纤维还可能有其他极化。[H0R 原任务](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/HODGE_H0R_VERY_GENERAL_WEIL_ALGEBRAIZATION_TRANSPORT_20260919.md) · [H0P 冻结结果](https://github.com/awdawmip/enterprise-math/blob/c3a79e03e7fde0bbcd5f10d71c718376e62f4cb2/research_result_records/RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT/RR-D0D2E8489B7EC4AE9AB4.json)

运行 `python polar_check.py` 可对原 Gaussian 矩阵直接测试有理块倍数的整性，并用小模数逐对搜索复核最小值与局部下降。[复算程序](polar_check.py) · [完整结果](polar_checked.json)
