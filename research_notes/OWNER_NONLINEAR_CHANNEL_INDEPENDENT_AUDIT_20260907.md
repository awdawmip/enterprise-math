# 非线性通道总质量商：独立审计

状态：`AUXILIARY_INDEPENDENT_AUDIT / PURE_ALGEBRA_SUPPORTED / FINITE_CONSUMER_PROBES_PASS / NOT_FOUNDATION`。

辅助工作包 `/root/exact_solver`；不是正式 task、claim 或 Researcher-ID。只审核本轮已完成结果，未新开一般动力系统或参数问题；作者文件和原几何 consumer 均未修改。

## 1. 审计结论与冻结输入

审计对象：`OWNER_NONLINEAR_CHANNEL_QUOTIENT_20260907.md` 与 `experiments/owner_nonlinear_channel_20260907/channel_quotient.py`；沿原矩阵及微观分支调用路径读取 `research_notes/owner_geometry_20260907_check.py`。

在完整 `X=Q_{>=0}^6` 上，作者的任意集合观察分类成立：给定任意集合映射 `q:X->Y`，存在每个操作的后继 `R_i` 满足 `q A_i=R_i q`，且每个 `R_i` 仅在实际像 `q(X)` 上单射，已经足以且恰好要求

`q=f∘L`，其中 `L(x)=sum x_c`，`f:Q_{>=0}->Y` 任意。

没有线性、连续、可测、q 满射或所有 `R_i` 交换的隐含前提。该结论首先是质量向量 carrier 上的定理，不是微观 BRC carrier 的商定理。未发现要求撤销结论或修补代码的阻断问题。

| 文件 | SHA-256 |
|---|---|
| 作者数学笔记 | `edcc5694bd2a85cebc0836110d03142ad3637cd953e96b2c98c08fbbe8e77ffc` |
| `channel_quotient.py` | `c90d67e9d56bc14e2d2adea36b8f69ba2e1afc21c794c22aee73e69de34bd844` |
| 被复用的原几何 consumer | `d92a45acb9c455b88a3786ce99ae919cbfbd5a0b09b55ce3dfeb6b39b633c4a7` |

## 2. 任意集合论证的逐式核对

原矩阵列为输入、行为输出。固定 i 的分量不变，其余五个分量都成为 `(L(x)-x_i)/5`，故 `L A_i=L`、`A_i^2=A_i`。

设 `S=q(X)`。因子化关系本身已经保证 `R_i(S) subset S`。对任意 `s=q(x)`，有

`R_i(R_i(s))=q(A_i^2 x)=q(A_i x)=R_i(s)`。

左、右两边作为 `R_i` 的输入分别是 `R_i(s)` 与 s，二者都在 S，因此只使用 `R_i|S` 的单射性即可消去外层 `R_i`，得到 `R_i(s)=s`。所以

`R_i|S=id_S`，且 `q A_i=q`。

这一步没有把 `R_i^2=R_i` 或恒等性扩展到 `Y\S`。若 Y 有未观察到的元素，操作可以在那里不恒等；例如固定全部质量标签，同时交换两个额外元素 a、b。若 q 满射，才有 S=Y，从而可见操作在整个 Y 恒等。允许 `R_i` 在 S 外不单射也不影响已证结论。

若 `L(u)=L(v)` 且 `u_i=v_i`，原公式直接给出 `A_i u=A_i v`。由不变性得到

`q(u)=q(A_i u)=q(A_i v)=q(v)`。

对任意同总质量的 x、y，取一个当前富余坐标 a 和亏缺坐标 b，将

`t=min(u_a-y_a, y_b-u_b)>0`

从 a 转移到 b。转移是精确有理数且不会越过目标，因此每个中间分量位于对应初、终值之间。每步至少消去一个不匹配坐标，已匹配坐标不会再被选；最后一步至少同时消去两个，故从至多六个初始不匹配坐标出发，步骤至多五。x=y 时空链单独成立。

每个双通道转移都有至少四个未动的真实通道，可以选其中任意一个为 gate。该步保持 gate 坐标和总质量，便给出上述 q 相等性。有限串接证明 q 在完整的每个总质量 fiber 上恒定。无需极限或平均迭代收敛。

取截面 `(t,0,0,0,0,0)` 定义 `f(t)`，即得 `q=f∘L`；L 对非负有理质量满射，所以 f 唯一。反向对任何 f，取所有 `R_i=id_Y`，立刻满足合同。若不要求像上单射，`q=id_X,R_i=A_i` 反例说明不能推出总质量因子化。

## 3. 域、零质量和“步骤”的边界

非负零质量 fiber 仅有零向量；不需要除以总质量，也不要求为零质量配置任何正分支。严格正域 `Q_{>0}^6` 同样闭于每个 A_i，且转移中间坐标处于两个严格正端点之间。截面改为 `(t/6,...,t/6)`，t 属于正有理数，即可得到同样的唯一因子化。严格正域没有零 fiber，不能在该域中接受零向量见证。

完整 carrier 是实质前提：任意另选子集未必包含转移链，不能自动套用连通论证。第三个未动通道也是实质结构；两个通道的类似 A_i 都是恒等，任意观察可通过合同，不能直接推广总质量结论。

五步的准确含义是**双通道质量转移见证**的统一上界，不是有向 A_i 动力学的步数，也不是任意共同像 gate 关系的最短链。作者的

`x=(5,0,0,0,0,0)`、`y=(0,1,1,1,1,1)`

在双通道转移模型中确实至少需要五步：五个最初为零、最终为正的接收通道分别至少要收到一次转移，每步最多增加一个通道。

独立检查以下两条更明确的边界：

1. 取 `u=(0,0,5,0,0,0)`，有 `A_1 x=A_1 u` 与 `A_0 u=A_0 y`（本段下标为 Python 的 0..5）。因此宽泛的共同像 gate 关系只需两链就连通这两个端点；第二链同时改变多个通道，不是作者 verifier 接受的一个双通道转移。
2. 初始 `x_0>0` 经任意实际 A_i 都仍满足第零分量严格正：若 i=0 则该分量不变；若 i!=0，则新的第零分量为 `(L-x_i)/5>=x_0/5>0`。因此任何有限 A_i 词都不能把这个 x 送到 `y_0=0`。尽管五步转移见证存在，实际有限动力到达仍不成立。

这两项直接核验了作者对三种关系的区分，没有另设动力学规律。空间位移与质量操作的联合 `(z,x)` 也未被该质量幂等性定理覆盖。

## 4. 证书验证器与微观 BRC 的独立核对

生成器（L84）冻结原始输入为 Fraction 元组，执行 donor/receiver 算法。验证器（L107）重新绑定调用方的两个端点、声明的非负或严格正域、总质量、至多五步、不可变步骤类型、链连续性、正有理转移、不同 donor/receiver 与未变化的 gate、最终端点。它随后直接调用原几何矩阵计算每步两侧共同像（`gate_image`，L52）。此矩阵来自启动时核验上述 SHA 的原 consumer；没有信任外部保存的公共像或文字 flag。

有限 verifier 的 `VALID` 只证明所输入的这条链。它没有执行任意 q、验证 `q A_i=R_i q`，也没有验证任意集合映射的单射性；这些是普遍定理的明确前提。它不要求链与确定性生成器逐步相同，只要链满足其有限合同即可。严格正标志在端点及每个中间向量重新核验；不只是生成时的描述。

局部精确输入探针通过：零质量空链、五步极端例、总质量 `11/3` 的严格正有理端点。8 项无效修改全部得到 `INVALID`：错误源端点、错误目标端点、删去末步、改转移量、gate 设为 donor、零点冒充严格正域、非 bool 域标志、浮点端点。同一非单位有理向量的三个 gate 矩阵像与闭式公式直接一致。未重跑作者 2978 对或完整 11-test suite。

原 `brc_gate_observation`（L158）明确为每个非零质量分量放一条输入分支；这是声明的 lift，不是恢复一般微观对象。实际调用旧 `paths/observe`，对于

`(1,0,0,0,0,0)` 与 `(1/2,1/2,0,0,0,0)`，gate=2，

得到相同输出质量向量，但真实 WeightHistogram 分别为 `5[1/5]`、`10[1/10]`，CWM 的 count 分别为 5、10。二者质量都为 1。以原矩阵识别两点并不等于以微观 BRC 识别它们。

另直接复用原 `paths(0,(2,))` 与 `paths(0,(2,2))`：质量向量相同，但分支数从 5 变为 25，直方图从 `5[1/5]` 变为 `25[1/25]`。这给出矩阵 A_2 幂等而保留分支历史的操作并不幂等的实际证据，防止跨 carrier 使用第 2 节的幂等消去论证。

## 5. 有界探针的可接续片段

以下是最终通过的独立探针关键部分，可在仓库根目录以 Python `-B` 重放；只依赖上述冻结 consumer，不调用作者全套测试。首轮人工构造的严格正端点有总质量笔误，被探针自己的总质量断言发现；随后改为下列两端均为 `11/3` 的精确输入再运行，未修改被审代码或数学参数。

```python
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import sys
sys.path.insert(0, str(Path('experiments/owner_nonlinear_channel_20260907').resolve()))
import channel_quotient as cq
x=(5,0,0,0,0,0); y=(0,1,1,1,1,1)
w=cq.make_gate_witness(x,y)
assert len(w.steps)==5 and cq.verify_gate_witness(x,y,w).status=='VALID'
z=(0,)*6
assert cq.verify_gate_witness(z,z,cq.make_gate_witness(z,z)).status=='VALID'
xs=(F(17,6),)+(F(1,6),)*5
ys=(F(1,6),)+(F(7,10),)*5
assert sum(xs)==sum(ys)==F(11,3)
ws=cq.make_gate_witness(xs,ys,strictly_positive=True)
assert cq.verify_gate_witness(xs,ys,ws,strictly_positive=True).status=='VALID'
def reject(a,b,witness,**kw):
    assert cq.verify_gate_witness(a,b,witness,**kw).status=='INVALID'
reject(y,y,w)
reject(x,x,w)
reject(x,y,replace(w,steps=w.steps[:-1]))
reject(x,y,replace(w,steps=(replace(w.steps[0],amount=F(2)),)+w.steps[1:]))
reject(x,y,replace(w,steps=(replace(w.steps[0],gate=w.steps[0].donor),)+w.steps[1:]))
reject(z,z,cq.make_gate_witness(z,z),strictly_positive=True)
reject(x,y,w,strictly_positive=1)
reject((5.0,0,0,0,0,0),y,w)
u=(0,0,5,0,0,0)
assert cq.gate_image(x,1)==cq.gate_image(u,1)
assert cq.gate_image(u,0)==cq.gate_image(y,0)
v=(F(1,3),F(2,7),F(3,11),F(4,13),F(5,17),F(6,19))
for i in (0,2,5):
    assert cq.gate_image(v,i)==tuple(v[i] if c==i else (sum(v)-v[i])/5 for c in range(6))
a=cq.brc_gate_observation((1,0,0,0,0,0),2)
b=cq.brc_gate_observation((F(1,2),F(1,2),0,0,0,0),2)
assert a[0]==b[0] and (a[1].count,b[1].count)==(5,10)
assert a[2].entries==((F(1,5),5),) and b[2].entries==((F(1,10),10),)
one=cq.geometry.observe(cq.geometry.paths(0,(2,)))
two=cq.geometry.observe(cq.geometry.paths(0,(2,2)))
assert one[0]==two[0] and (one[1].count,two[1].count)==(5,25)
print('PASS')
```

本审计到此结束。结论不扩到其他操作、缩小的不闭载体、空间位置与内部寄存器的联合观察或任意微观 BRC 系统；没有提交、推送或注册新工具 family。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
