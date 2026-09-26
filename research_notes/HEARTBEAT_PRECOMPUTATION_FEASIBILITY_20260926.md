# BRC–Shor 预演算表：源码核对与有限门序规模

Progress-Event-ID: HEARTBEAT-PRECOMPUTE-FEASIBILITY-20260926-396A7437
Status: SOURCE_AUDIT_AND_STATIC_INSTRUCTION_CENSUS / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read: 396a7437e0de636f5b02b2c14539be35bbc7996b
Source read and publication preflight: 5d83c0582bdf7b2aa8d99160d6776133ecfd2240
Executable source: Stage100 cumulative 83db34752d587bfc9abcf0c83cb6c702e8c67295.
Research-Activity-ID: 未取得，REGISTER_PENDING；不借用服务session/CLAIM，不宣称正式研究准入。

## 1. 实际工作及范围

用户问“有可能预演算一个表来加速吗”。已核验挂载Stage100 ZIP：56,288,480字节，SHA256 f050f1e30dbba8ba80aad0827ff24161e21daebe6bd405cb196c0fe1d22de848，在独立目录解压，不修改父文件。读取原root_power.py、collision_first.py、common_generator.py、demand_stream.py及已保存CASE_21_2_10计数。

本轮新增执行仅从Python AST提取实际门编号调度并枚举指令标签，是源码/调度规模核对；没有振幅、相位、概率或模幂科学传播，没有新增科学BRC调用、Shor回归、编译表或速度实测。不能把这次统计当成Stage101编译器完成。P000、BRC-only、完整61模式、原有序门和全部状态/读取/CF语义不改。

## 2. 已有缓存，纠正上一答的推测

FusedPowerRotor.__init__已经调用make_direction一次并保存direction、z_power、min_den等；apply_numer不重新生成幂系数。因此不能说单根系数在每行上反复编译。重复建立同类幂表主要可能摊销跨实例或进程的初始化，不自动带来行级加速。

CollisionFirstPrepared还已有一次prepared round内的完整行复用，其键保留全部61分量的精确符号/二幂规范行。相同范数、主要两分量或当前概率不允许共用行结果。当前值得另试的是组合后有序操作的持久表，而非再加一层同样的单门缓存。

## 3. 源码绑定的静态规模

实际表达为：

    tuple(len(history)-c+1 for c,bit in enumerate(history) if bit)

深度i的列表是[i+1,i,...,2]的有序子序列，正好2^i种语法字。跨深度0..t-1的集合为[t,...,2]的全部子序列，共2^(t-1)种，含恒等空字。直接枚举原AST所得：

|控制位数|所有轮的历史位置数|不同语法门序（含空字）|
|---|---:|---:|
|4|15|8|
|6|63|32|
|8|255|128|
|10|1023|512|

这是所有可能报告历史的静态规模，不是某个N,a实际访问次数；没有声称512个算子已实际预计算/认证，也未将不同语法字进一步按算子等价归并。

继承的13,803是标准21完整恢复中的根字行作用次数，不是不同门序数。原CASE full_counts={phase_rows:12273,representatives:3038,root_rows:13803}，read_counts={phase_rows:5363,representatives:1505,root_rows:6125}。不能用13803/512推算加速倍数。

10位的固定顺序[10,...,2]可划成[10,9,8]、[7,6,5]、[4,3,2]三块，每块8个子序列表槽，共24槽；若只共用恒等项则22种语法块，每行最多顺序应用3块。4位分块为[10,9,8,7]、[6,5,4,3]、[2]，34槽，空字合并后32种。这是表键计数，不是存储字节数或吞吐实测。保持原顺序，不能按理想角度重排。

## 4. 建议表内容与成本判据

优先预演算真实有序门段的精确作用，而非所有世界状态或目标答案。每项绑定实际bank来源/版本、完整方向、分母、顺序、逆标记、编码和允许控制/观察范围。Stage98已证明候选形式：

    T_word = I + E C_word E^T,
    T_word x = x + E C_word(E^T x).

E可共享，每字存自己的精确系数与BRC证据。精确相位2和其他字母须补齐完整载体绑定，不能凭理想名称自动加入。当前并未执行一般有序字编译器；Netlib方案只作背景，不替代BRC。

低位宽可以比较最多512项全表；更大位宽用连续3/4位块或有限热点缓存，因为全表仍随t指数增长。相同固定bank、精度、坐标和相位调度下，内部门表不依赖N或模幂底数a，可跨实例复用；工作模乘不因此获得跨N,a复用权限。

运行时仍要把新场x代入，不能称任意完整后态只需O(1)查表。仅保存原单门列表也不会自动减少每行逐门作用。应检验组合后的算子与批量行作用能否降低实际开销。

重复R次的同一工作负载，需满足：

    C_build + C_load + R*(C_lookup+C_apply) < R*C_old

才有摊销收益。构建/认证、加载、热态端到端运行、表内存和整数位长分别测量。原Stage100已有短整数新API更慢的计时，不能因为配对或门序数少就预告速度倍数。

表项不允许含未知阶、因数或目标直方图来冒充计算。仍保留原x、全部尾项、工作标签、真实顺序、控制边界和已选报告。表缺失走精确原路线；不能设为零或恒等，不跨实际读取融合，不用浮点量化暗改模型。

## 5. 产物及下一单元

本地/mnt/data/precompute_feasibility/包含census.py、PRECOMPUTATION_CENSUS.json、FEASIBILITY.zh-CN.md。静态结果JSON SHA256 732e6ca7ea32b22f4edb66d1851c332265140265ff6847919bf0fab338afa702；脚本SHA256 74c9ee3c90d2b51f25088b6620b5e3197b83e857cb99a7a830ea2d2c25a151a4；完整本地说明SHA256 8783656da404466459a7e9930b2bab27781327fab8b31ff341be4148b6a28f33。

下一项是实际BRC绑定的连续块与低位宽全表两种可比较原型，然后按相同输入/随机带分别比较冷启动、重复运行与完整恢复。当前不宣称新表已生成、12组再次通过或有速度优势。

一般乘积反射的预编译已有Netlib LAPACK DLARFT/DLARFB背景；官方DLARFT明确有序前向/反向乘积及H=I-VTV^T。只读取官方HTML：https://netlib.org/lapack/explore-html/d7/d0d/group__larft_ga20e5a4f351b3ca7d30078547e55884f5.html 。没有运行LAPACK、没有首创一般预计算方法的声明。
