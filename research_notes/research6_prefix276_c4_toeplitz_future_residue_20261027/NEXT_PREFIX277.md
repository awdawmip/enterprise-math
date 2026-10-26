# PREFIX-277｜有来源的 r=2 C4 历史读出合法性与最小相位残差

## 已证且无需重做

PREFIX-276 的 Stage50 声明载体中，Toeplitz 一阶延拓精确圆盘为 `|c_(H+1)-u*B^-1 v|<=rho`（`T_H` 严格正定）；对 `c1=i/2`，`c2` 在以 `-1/4` 为中心、半径 `3/4` 的圆盘内。

两个具体有限 C4 源包：`A=[1,-i]`, `B=[2,-i,-1]`，分别 `Z=2,6`，`c1=i/2`、`c2=0,-1/3`，Stage50 双输入外部读出 `r1` 四相全部相同；`r2,p0` 分别 `5/18` 与 `10/27`。一维有理参数族 `(2/(1+t²), -i, -(t-1)²/(1+t²))` 给出无穷多不同 `c2`。作者侧独立精确 BRC 观察脚本 89 个不同有理参数全部通过；不是 Stage46 原生执行。

## 第一个未解问题

现行有来源的 `Stage50` 声明双输入 `p_external(r,p)`，其 `r=2` 条件历史 T² **能否**由完整真实 Source 的合法 preparation / port / field 操作实现，并在同一 detector/boundary/physical time 类型内重复？必须获得真实 `model_law_id` 和原始可执行 Stage46/50 入口才作原生结论。

## 可执行研究单元

1. 精确定位当前 canonical source 对历史移位 `T^r`、字段/端口 C4 门、检测 effect 以及调用入口的版本与适用准备范围；查是否需要原包 bundle。`src/enterprise_math/brc_weighted_recurrent.py` 仅正有理质量，不是相位后端。
2. 证明 A/B 源载体到完整原生 `H_n` 状态（Cell、Port、相位、场、材料动量、来源、边界、独立时间）的真实类型化嵌入；若接口未定义，给出精确首缺对象，不暗填物理更新。
3. 有权且有环境时执行原始 Stage46/Stage50 的规定双输入 `r=1,2,p=0..3`，保存入口、stdout、输入、源码 pin 和观察，区分加载验证与物理操作证据。
4. 若真实合法操作无法读取 r2，计算其允许观察代数下的最小充分 moment 商及不可见 future residue；利用 PREFIX-276 的圆盘约束提出可判别后继实验。不要把同刻闭环/solver iteration 写成心跳间隔。
5. 正式 Source 状态机权限可用时核对活跃 owner，走当前 Task CLAIM/Result/Driver 路径；目前只可称作者侧稿件 `NOT_ADMITTED`。

## 判定标准

一个明确、可复核的合法性证明 + 真实原始接口运行结果，或者说明首个缺失字段/规则并形成具有精确未来读数差异的数学证书。保留 P000 六维本体与三维切片语义，遵守 `ACTUAL_TYPED_BRC_ONLY`，审查与作者严格分开。
