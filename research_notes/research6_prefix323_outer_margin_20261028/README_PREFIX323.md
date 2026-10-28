# PREFIX-323｜精确外部分离余量与中间尺度严格非空

2026-10-28，Research6 作者侧独立推导；`UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`。**这是静态辅助 S7-3 BRC 模型的结论，不是原生 X6/Detector 或时间演化定理。**

## 结论及数学证明

固定 PREFIX-321 的 16 个相位根与 204 个有理外包叶。保留同尺度两形状、5 项准确基础质量 Q0、10 项独立有界误差相干参考与带标签的 BRC 路径对。对其中 196 个严格分离叶，每叶原证书记有有理下界或上界 `m_i`；正负号取绝对值得 `a_i`。逐项比较 196 个分数，得

\[
\min a_i=\frac{186192}{100945},
\quad i_{zero\ based}\in\{18,82,140,170\}.
\]

最小叶 18 原文为 `[0,1,"23/32","3/4","1/8","3/16","+",0,"186192/100945"]`，四个最小位置由 C4 对称性对应。以整数运算严格证明全部 196 叶有 `29a_i²>98`，且最小者满足

\[
29\left(\frac{186192}{100945}\right)^2-98
=\frac{6746848606}{10189893025}>0.
\]

从而已发表证书的精确外部余量为

\[
\boxed{\delta_{ext}=\frac{186192}{100945}-\sqrt{\frac{98}{29}}>0}.
\]

继承 PREFIX-322 的临界尺度构造（作者侧，非独立接受）：

\[
H=\sqrt{98/29},\quad r_*=1/H,\quad
L=1062562/458329;
\]

\[
c_{sharp}=\min\left\{
\frac{1}{2}\left(\frac6{\sqrt{58}}-\frac{5\sqrt2}{16}\right),
\frac{\delta_{ext}}{2\sqrt2}\right\},
\quad
T=\min\left\{\frac12,\frac{\sqrt{98L/29}-\sqrt{120/29}}6\right\},
\quad
r_{band}=1/(H+c_{sharp}T).
\]

由有理平方根包围与单调区间运算，严格确定

\[
c_{sharp}=\frac{\delta_{ext}}{2\sqrt2},\qquad
T=\frac{\sqrt{98L/29}-\sqrt{120/29}}6.
\]

以下均为整数平方根生成的**严格区间**，不是浮点近似推断：

- `0.006199513494 < delta_ext < 0.006199513495`;
- `0.002191859015 < c_sharp < 0.002191859016`;
- `0.127467831328 < T < 0.127467831329`;
- `0.507536425594 < sqrt(L/9) < 0.507536425595`;
- `0.543901128758 < r_band < 0.543901128759`;
- `0.543983793275 < r_star < 0.543983793276`.

因此严格得到剩余可疑尺度带非空：

\[
\boxed{\sqrt{L/9}<r<r_{band}},
\qquad
\boxed{0.036364703163<r_{band}-\sqrt{L/9}<0.036364703164}.
\]

**解释限定：** 这仅排除“PREFIX-322 两端界已经覆盖全部尺度”的捷径；绝不表示存在平方最小覆盖球风险超过 `L` 的共同观测实例。完整连续 `G(r)\le L` 或显式反例仍未证明。未改准确 Q0、独立参考误差模型、来源标签或 P000。

## 完整物料（真实代码、完整证明、结果、下一问题）

本目录 `PREFIX323_SOURCE_PACKAGE.tar.gz.b64` 保存五份**完整原件**：
`PREFIX323_EXACT_OUTER_MARGIN_AND_NONEMPTY_BAND.zh-CN.md`、
`verify_prefix323.py`、
`RESULTS_PREFIX323.json`、
`NEXT_PREFIX324.md`、
`PACKAGE_MANIFEST_PREFIX323.json`。
编码为 `base64(gzip(tar(files)))`；文本包 Git Blob 为 `4017d3f620235a7decff9d8fb8ca31196d5da9e0`；该包内清单给出各文件的 SHA-256。可用以下命令解包：

```sh
base64 -d PREFIX323_SOURCE_PACKAGE.tar.gz.b64 | tar -xz
python verify_prefix323.py ../research6_prefix321_global_phase_sharpness_20261028/RESULTS_PREFIX321.json.gz.b64 > recomputed.json
```

验证已实际执行：源码标准库精确 `Fraction` 扫描 196/196 严格叶、零基四个最小位置、严格分数差，以及整数平方根严格代数区间；重新运行 PREFIX-321 的独立证书检查器得到 `PASS: 16 roots / 204 leaves / 196 S / 8 L`。**验证的是精确证书及其衍生，父研究的 Driver 独立审核尚未完成。**

冻结来源：GLOBAL_KNOWLEDGE_V1 `main@398ba80d59d3ea1559e6233eb1823ebdb4df934b`；Enterprise Math `main@4d32ef6f4fbd8330f762eb7cc9cf8b2a928243c5`；PREFIX-321 压缩证据 blob `9991eca5a08b263ab95ed686c6e4fa7faa13b8cc`，解压 JSON SHA256 `8c040669fbae1bfb1f70dd3f2ba8e3b9721121565c7432582b9a11e3bd2528e9`。当前原生 `em_status` 的 `research_authority_granted=false`；owner 查询 `CONTROL_QUOTA`，故无当前 CLAIM/Result/Driver 接纳的回执。

**PREFIX-324下一科学问题：** 对上述非空区间的**所有**同尺度、自由十参考报告，构造可复算的实代数全域恢复上界 `G(r)\le L`；否则给出全 Q0/十参考报告/四接触正权重/MEB²>L 的确切多态反例。辅助 BRC 向原生六轴 X6 的关系和动态保真映射仍待单独证明。
