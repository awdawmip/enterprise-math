# 三面地址迁移的可逆范围与模分片的最小补充信息

固定研究快照的三帧地址原型有 729 个六维空间键，其中 9 个落在已注册二维切片上。三个帧给这 9 个键共 27 种拼写。实际回放源程序的 8748 次带时标更新后，63 次的前后端都可用新切片地址精确重放。对只存地址余数的缓存，还能精确求出每个缓存输入对应多少种旧分片，以及要无错恢复旧分片至少需保留多少种附加标签。

这里对接同一公开提交中的两个**不同协议**。研究原型的 wire version 是 2；已注册切片协议的 version 是 1。这一对接关系由固定命名空间和轴映射给出。源程序运行过的时钟、边和域集合均为公开研究测试。没有生产数据库的实际行、分片系数、部署日志或生产帧注册表可供盘点。[任务书](https://github.com/awdawmip/enterprise-math/blob/fbaf7b0b5bf5f84415930a08ea88079c4c1d4e05/research_tasks/RS-COORD-CALLER-DATA-MIGRATION-20260916.md) · [冻结原型说明及原先已验证的范围](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_notes/CELL_ADDRESS_ADAPTER_V2_20260913_A8D47F21.md)

## 一、可用的两版调用与迁移条件

| 冻结来源与位置 | 用途及覆盖范围 |
|---|---|
| `src/enterprise_math/_cell_slice_codec.py` 11–32、35–64 行 | 固定两原生轴的三面编解码及具名步进。公开地址只许前三位恰一个零、另两位正，后三位零。 |
| `src/enterprise_math/cell_address.py` 19–67、74–99 行；`src/enterprise_math/__init__.py` 392 行 | 注册 runtime 与包导出。wire 包含 schema、codec、version、frame、六个坐标。实际先解码再调用原距离后端，旧标量/位移接口继续用原类型。 |
| `tools/validate_cell_address.py` 6–15 行；`tools/apply_coordinate_address_contract.py` | 前者是从标准输入实际消费公开 wire 的命令，本轮运行合法/不支持版本分别返回 0/2。后者生成及核对契约文本。冻结所有 Python 文件按七个公开 API 名称搜索，连同公开接口测试在内共命中五个文件，文件名列在 JSON。动态导入与无标签历史库不在该检索证明范围。 |
| `research_notes/cell_address_adapter_v2_20260913_a8d47f21/cell_address_adapter.py` 104–157、167–191、195–227 行 | 实验原型的具名空间键、帧表、严格持久化协议和实际分支 ID 去重。旧帧标签、偏移和轴置换一起核验。该原型只作为冻结数据的生产者、消费者。 |
| 同目录 `test_adapter.py` 22–58、96–149 行及 `results.json` | 三帧 A/B/C、729 个键、边及对照、一组有序时钟和初始/边界集合。脚本在临时树运行原程序，复核冻结的状态、计数、负控、范围；环境 Python 版本单列。 |
| `coordinate_address_contract.json` 及 `coordinate_contract_migration_manifest.json` | 切片以外的全 X6 最终地址编解码尚未注册。历史证明、完整原生坐标、轴向位移、已有边和时标保留原有语义。 |

[公开地址实现](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/src/enterprise_math/cell_address.py) · [切片编解码](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/src/enterprise_math/_cell_slice_codec.py) · [原型读写与具名边](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_notes/cell_address_adapter_v2_20260913_a8d47f21/cell_address_adapter.py) · [原始测试资料](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_notes/cell_address_adapter_v2_20260913_a8d47f21/test_adapter.py) · [契约清单](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/coordinate_contract_migration_manifest.json)

本次固定源命名空间 `X6-fixed-native-chart`，选择其已解码整数轴 0、1 对应目标 `X6_FIXED_E1_E2_CHART` 的 E1、E2。必须先以不可变帧表解码六维键；仅当末四维**实际为零**才接收。直接截取视图的前两位会把重排的轴当作另一原生方向。新空间缓存键取（旧空间命名域，完整 V1 规范 wire），等价于（旧空间命名域，已还原的完整原生键）。该键只识别空间点。时变状态另带时钟、记录标识；路径还带有序边、端口/方向、分支标识和权。分片编号仅能用来路由。

源里的不同帧拼写常给出同一空间键，无法仅用 V1 恢复旧拼写。转换器在每个被支持的 V1 结果旁保留原 UTF-8 wire、源提交、命名域和字节校验摘要。回滚时重跑双方的严格解析、核对目标字段，再返回保存的原字节。从 CLI 输入的字节空白及 CRLF 同样保留。回执摘要用于查出不一致；此处没有签名信任机制。

## 二、原有时钟、边与域的回放

原型测试让所有 $3^6$ 个原键在 12 个有序步骤更新。偶数步换帧而原键不动，奇数步沿原轴 $t\bmod6$ 走正向一步，并换入 A/B/C 的下一帧。这是源代码已有的真实测试时标。回放给出以下端点分类，逐行回放暂存完整源事件，将其与分类一起写入有序校验摘要。封存 JSON 含逐时钟计数与摘要，原测试可重建各行。[原时标与边界集合](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_notes/cell_address_adapter_v2_20260913_a8d47f21/test_adapter.py#L128)

| 起点和终点 | 事件数 | 本地回放行为 |
|---|---:|---|
| 都在切片 | 63 | 原序号、时标、换帧或具名步进逐条保留，两端均通过字节回滚。 |
| 外到内 | 18 | 保留完整源事件，标记进入切片。 |
| 内到外 | 27 | 保留完整源事件，标记离开切片。 |
| 都在切片外 | 8640 | 保留源六维记录，拒绝转换为切片内事件。 |

三帧对 729 键共生成 2187 个拼写；支持 27 个，其余 2160 个拒绝。原点完整保留，目标六位为 $(0,1,1,0,0,0)$。原域集合的横坐标是 $\{0,1,2\}$，逐点搬运保全该集合；直接以旧帧正数字段 $1,2,3$ 划区间会得到 $\{-1,0,1\}$。两种层视图的种子集合不同，空间键无须随显示层改名。

原型另有同两条边的三帧拼写，共六条声明。用来源权威 ID 和解码后的端点、原轴、方向、精确权比较，六条正确归并为两条。源中另行明确标为合成的平行边有不同 ID，应保留；三条边给出两步权重直方图 $\{1/6:1,1/4:1\}$。若累加同一物理边的帧副本，则原来一条权 $1/6$ 的路径会被错计九次。相同 ID 的冲突权重、错误端点、未知帧和注册偏移篡改均被拒绝。将 V1 直接传入旧数值序列 L1 消费者也按预期失败。[冻结边测试](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_notes/cell_address_adapter_v2_20260913_a8d47f21/test_adapter.py#L96)

## 三、模分片转换的精确障碍

以下 $M,q,u,v,s$ 是本次条件分片参数；上述来源没有给出这样的部署配置。用 $(m,n)$ 表示原切片。只写公开地址前三位 $(a,b,c)$。冻结解码有三支

$$
(a=0):\ (1-c,b-c),\qquad
(b=0):\ (a+1-c,1-c),\qquad
(c=0):\ (a,b).
$$

所以任意旧模分片 $L=um+vn+s\pmod q$ 满足

$$
L=ua+vb-(u+v)c+s+u\,\mathbf1_{a=0}+(u+v)\,\mathbf1_{b=0}\pmod q .
$$

设分片进程只能观测新地址的逐位模 $M$ 余数 $z=(a,b,c)\bmod M$。$M,q\ge1$ 可不同，取 $z_i\in[0,M-1]$。记 $I(z)=\{i:z_i=0\}$，以三个面 $a,b,c$ 为指标，令

$$
\delta=(u,u+v,0),\qquad h=\gcd(q,Mu,Mv),\qquad
B_z=uz_a+vz_b-(u+v)z_c+s.
$$

**分片纤维定理。** 可观测的 $z$ 恰为 $I(z)$ 非空的三元组。其可能旧分片的精确集合与大小为

$$
\mathcal L(z)=B_z+\bigcup_{i\in I(z)}(\delta_i+h\mathbb Z/q),\qquad
|\mathcal L(z)|=\frac{q}{h}\,\bigl|\{\delta_i\bmod h:i\in I(z)\}\bigr|.
$$

因此，一种额外标签要在所有兼容地址上与 $z$ 一起确定旧分片，所需字母表的最小大小为

$$
K_{\min}=\frac{q}{h}\,\bigl|\{0,u,u+v\}\bmod h\bigr|.
$$

证明如下。真正为零的那一位必须在 $I(z)$ 内；其它为零的剩余位可以由正的 $M$ 倍数产生。固定一个可能的面，两个正坐标独立增加 $M$ 的倍数。三个面上两项权系数分别为 $v,-(u+v)$、$u,-(u+v)$、$u,v$，各自产生同一剩余子群 $h\mathbb Z/q$。非负的加次数在有限群中已能遍历子群。故固定面的整条陪集都可达到。三位余数皆零时所有面都可用，达到最大基数 $K_{\min}$。按每个 $z$ 的候选值递增编号就能用这一字母表表示实际旧分片，证明上界可达。这是信息量界；实际转换若握有精确 V1，可以直接解码取得正确标签。

若 $M=q$，$h=q$，只要保留三种偏移中实际使用的那一种，附加信息便足够。即使读数器可为任意非线性函数，在不保存附加信息时也只有平凡旧分片能全域搬运，因为 $(0,q,q),(q,0,q),(q,q,0)$ 在缓存中都读成 $(0,0,0)$，但给出 $s+u,s+u+v,s$。特别地，将全域旧非平凡分片替换成一条新坐标仿射式会失败。若处理的是完整正整数坐标，观测“哪一位实际为零”能消除此失败。

**失败域和最优无标签错误率。** 给定非空零位集合 $I$，其对应的可见输入数是 $(M-1)^{3-|I|}$，包括 $M=1$ 时三零输入一项。以此对上式所给纤维大小作次数统计，就得到全部风险余数类。设三面等权，每面两个自由正坐标均独立均匀取 $1,\ldots,\operatorname{lcm}(q,M)$。这是明确的人为周期基准。令 $k=|\{0,u,u+v\}\bmod h|$ 及 $(e_1,e_2,e_3)=(0,2M-1,3M-1)$。所有仅见 $z$ 的预测器中，最优分片错误率恰为

$$
1-\frac hq\left(1-\frac{e_k}{3M^2}\right).
$$

给定 $z$，各可能面等权。在每个面上，余数陪集内的 $q/h$ 个输出等权，因为在完整周期上两个自由坐标到该子群的同态有等大纤维。因此最佳预测选在 $I(z)$ 中属出现最多次偏移的那个陪集，再选其中一个元素。若三偏移均异，双零时有 $3(M-1)$ 次面歧义，三零时少判两个面；若两种偏移不同，则有 $2(M-1)$ 次双零面歧义，三零少判一个面；若全同则没有择面损失。除以 $3M^2$ 并计入陪集内部的正确率 $h/q$ 即得。

同一基准还区分最长分片标签与平均信息。令 $K=q/h$，$D$ 为三个面两两配对中偏移模 $h$ 不同的对数，故当 $k=1,2,3$ 时 $D=0,2,3$。令 $H_3$ 是均匀选一个面所得偏移类的熵，三种情况依次为 $0,\log_2 3-2/3,\log_2 3$。则

$$
H(L\mid Z)=\log_2 K+\frac{2(M-1)D/3+H_3}{M^2}.
$$

因每个输入的可行面等权，单零输入只需区分陪集内的 $K$ 个等概率分片。偏移不同的一对面，在每个相关双零输入上增加一比特；此类输入各有概率 $2/(3M^2)$。三零输入概率为 $1/M^2$，增加 $H_3$。这是已声明分布下的条件熵。前述 $K_{\min}$ 则管最坏输入下的字母表大小。特别地，对任意有限 $M$，完全不用额外信息的全域精确恢复都等价于 $q\mid u$ 且 $q\mid v$，因为 $K_{\min}=1$ 同时强制 $h=q$ 和三偏移模 $q$ 相等。

例如 $M=q=5,(u,v)=(1,2)$ 时，61 个可能输入中 48 个唯一，12 个有两个旧分片，1 个有三个。额外标签最少 3 种，若不用标签，周期基准最优错误率为 $14/75$。而 $M=2,q=6,(u,v)=(1,1)$ 时，4 个输入各有三种可能，另 3 个各有六种，最优错误率升至 $3/4$。

## 四、复算和可回退的单记录转换

需要 Python 3.12 或更新版本、Git，以及含提交 `d2984d1a0c5c8221ee103084dd3da68dd039dfaa` 的公开仓库。脚本用 `git archive` 将此次所需的公开源码提至临时目录，以便原测试按其原本行为写出结果。输入仓库只读，无须私有附件。

```sh
python3 coord_check.py --repo /path/to/enterprise-math > /tmp/coord-replay.json
cmp /tmp/coord-replay.json coord_checked.json
python3 coord_check.py --repo /path/to/enterprise-math forward < legacy-v2.json > /tmp/moved.json
python3 coord_check.py --repo /path/to/enterprise-math rollback < /tmp/moved.json > /tmp/restored.json
cmp legacy-v2.json /tmp/restored.json
```

前两行重跑原实验、注册 CLI 正反控、真实源时标签、分支与范围检查。另以真正的 V1 公开编解码遍历 $M,q\le6$ 与全部 $u,v\bmod q$ 的 546 组参数，对完整周期的旧分片直接计数，核对每个纤维、所需附加标签及最优错误率。后两种模式对自备的冻结三帧 V2 地址提供可回退转换。`coord_checked.json` 的 `coverage_manifest` 记录本地支持、保留、隔离及数据不可得的面。生产存量迁移仍缺实际数据集、账号空间及帧注册来源的逐项对应。[转换与复算脚本](coord_check.py) · [原源重放和算术结果](coord_checked.json)
