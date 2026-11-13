# R433｜signed BRC 辅助组合行 r=17 完整 PF₄ 精确证书

2026-10-31。**AUTHOR_SIDE_EXACT / FINITE_EXHAUSTIVE / DRIVER_UNREVIEWED / NOT_ADMITTED**。仅证明带符号 BRC 的辅助标量读出；不是 P000 原生 X6、六轴三维切片或物理动力学保真定理，P000 和 ACTIVE 世界观均未修改。

## 固定来源、待解决问题
本轮 GLOBAL_KNOWLEDGE_V1 canonical main `eb69ad2642ab0e0db3c48c9b323c83505e59ba62`；Enterprise Math canonical main `6351a9e0ace15c932e8c6e1297f46dfd1eb9e45f`。P000_STARTUP 中 canonical_blob_sha1 为 `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`，与实际读取原始 P000 的 Git Blob 一致，状态 ACTIVE_LOCKED。接续 R432 `83a97192b7e2bb5cc7e741b005d36bca9632a653`：此前奇数 r=13、15 已完整 PF₄，r=17 尚未分类；偶数全体 r≥4 与奇数 r≥99 非 PF₄ 的作者侧证据沿用原强度，不在本轮重验。

## 定义和定理
对整数 2≤s≤r 取
\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad H_{r,s}=\binom{r+s}{2s}\delta_{r,s}.
\]
固定 `r=17`、`n=15`，令 `a_h=H_{17,17-h}` (0≤h≤15)，其他下标置零。研究半无限 Toeplitz 矩阵 `T=(a_{j-i})_{i,j≥0}`。

**定理（R433）：T 的每个阶数 h≤4 的子式均非负，故第17行完整满足 PF₄。** 结合 R426 已有的 Newton 障碍，此行不满足 PF∞。本轮不推断 r≥19 的整行 PF₄。

## 有限支撑归约证明
任意 h 阶子式的行指标 `u_0<⋯<u_(h−1)` 和列指标 `v_0<⋯<v_(h−1)`。非零矩阵元要求 `u_i≤v_j≤u_i+n`。若行列式展开中存在非零项，则这些按行有序的区间与列具有完美匹配。按区间端点次序反交叉，存在对应顺序的非零匹配，因此必有每个 `u_i≤v_i≤u_i+n`；若不满足，行列式为0。

若相邻行距离 `u_(i+1)−u_i>n`，前后两组行可访问的列区间严格分离，行列式或者为0，或者等于低阶子式的**无负号**乘积。对阶数归纳，只要检查所有相邻行距离在 `1,...,n` 的不可分子式。Toeplitz 平移将首行置0；逐个枚举满足 `u_i≤v_i≤u_i+n` 的严格递增列组，恰好覆盖所有可能的不可分非零子式。这是严格有限的完备域，不是有限窗口抽样。

## 原始 signed 系数与全部精确枚举
`R433_VERIFY.py` 使用原始带符号系数 `[t^r](1-t)...` 与 Catalan 核独立对照16项系数。全部正，整行 gcd=38；除以正的38不改变任何子式符号。归一化 `a_0,...,a_15`：

```text
3411705 51175575 352336080 1471685475
4156927425 8382559185 12423001500 13726279710
11353874675 6999985025 3176099256 1037186150
235481246 35225190 3208920 145860
```

| 阶数 h | 正 | 零 | 负 |
|---:|---:|---:|---:|
| 1 | 16 | 0 | 0 |
| 2 | 3,160 | 0 | 0 |
| 3 | 603,768 | 0 | 0 |
| 4 | 114,678,252 | 0 | 0 |
| **合计** | **115,285,196** | **0** | **0** |

1–3阶使用 Python 标准库整数精确 Leibniz 公式；4阶用 `R433_FULL_PF4.cpp` 枚举，每个4阶行列式以 `__int128` 算三阶代数余子式并以 Boost `int256_t` 精确求和。最大系数 `M=13726279710` 满足 `6M³<2^127` 和 `24M⁴<2^255`，故运行中间数没有整数溢出，证据给出保守位界104、140位。程序用 r=6 的已知负四阶子式 `−4117994496` 做符号负对照；Python 另以 r=4 的三阶负值 `−1568` 和320个独立四阶样本做交叉核验。**没有使用浮点符号判定。**

实际运行：
```text
R433_R17_LOWER_EXACT {"1":{"positive":16,"zero":0,"negative":0,"total":16,"first_negative":null},"2":{"positive":3160,"zero":0,"negative":0,"total":3160,"first_negative":null},"3":{"positive":603768,"zero":0,"negative":0,"total":603768,"first_negative":null}}
R433_EXACT_LOWER_PASS 606944 spot 320 gcd 38
R433_R17_PF4_EXACT positive=114678252 zero=0 negative=0 total=114678252 negative_control=PASS
```

由完备域归约与全部正的精确验证，得任意半无限 Toeplitz h≤4 子式均非负，证毕。**证明为计算机辅助有限行定理，尚未独立 Driver Review / 数学准入。**

## 权限、来源隔离及下一单元
本轮 GitHub 真实连接身份 `awdawmip` 具 push 权限；原生 `em_control_tasks` 返回 `CONTROL_QUOTA`，`DIRECTED_RESEARCH` context 为 `authority_granted=false`。未独立确认 Source Owner，未取得正式 CLAIM/Result/Review。作者侧成果可以保存，但不因保存而获得权限、接受状态或原生 X6 保真。严格按 signed 支路和观察者范围保留这一界限。

下一最小单元：检查 `r=19` 完整 PF₄，若能找到负例则提供精确4阶 witness；此外寻找 `r=17` 的五阶负子式，决定 PF 阶数是否恰为4。任何未完成的高阶搜索均不得视为通过。
