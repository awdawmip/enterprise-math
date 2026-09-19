# 乘法数场观察实验室 0.1.0

这是 Nollm Visual Toolkit 0.3.0 的**新增研究页面**，不是替换原工作台、原生 X6 或生产内核。默认数据仍是发布版四进制 A2 编码的 0—65535，共 65,536 个不同整数。零保留，但没有质因数分解或相位。

## 直接使用

在已安装的主工具中生成：

```sh
python -m nollm_visual_toolkit.multiplication_lab --site number-field-site --preview
python -m nollm_visual_toolkit.multiplication_lab --out number-field.html
python -m nollm_visual_toolkit.multiplication_lab --count 4096 --site smaller-site
```

首页本身内嵌完整工作台，用 `iframe.srcdoc` 执行预览，无需网络、CDN、账户或服务器。四个入口分别是候选乘法布局、原六角编码、全零相位反例和立体分层。`multiplication.html` 可独立打开。

`--preview` 复用 Nollm Visual Toolkit 0.3.0 已有的 `web.preview_server`，没有另造 HTTP 服务。页面导出的原数据 V2 可直接输入现有 `nollm-viz render` / `site`。

## 怎么观察

- **布局**：原四进制 A2 坐标，与候选 `R²(n)=n`、模 65536 可加相位并列。
- **相位**：黄金角质数序号、质数序号等分、全零三种基准。可覆盖某个质数的相位；所有受影响整数按该质数赋值更新。
- **相机与尺度分开**：相机旋转和缩放不改统计；布局尺度 C 改变连续位置相对于固定单元的大小。六角取整是另一个可开关的观察器。
- **乘法**：按标签画 `n, kn, k²n, …`，并对范围内所有正整数 `n≤N/k` 检查。原 A2 编码乘 4 可成立，但一般坐标乘法不成立；极坐标模型的相位关系由定义保证，不算新的数论发现。
- **密度**：64 扇区计数变异系数、取整后占用格与重叠组同时显示；立体展示高度不参与底面重叠统计。径向等面积计数由 `R²=n` 固定，不能当作独立均匀性证据。
- **反查**：显示原坐标、整数 ID、因数指数、相位、量化格、同格其他身份。投影重叠不合并 ID。
- **复现**：保存当前网页、数据指纹绑定配置、报告、完整 V2 数据和 PNG。PNG 本身不是可逆数据。

## 精确层与显示层

质数 p 的相位格为整数 `a_p`，定义 `φ(n)=Σ v_p(n)a_p (mod 65536)`，因此 `φ(ab)=φ(a)+φ(b)` 是构造恒等式。默认黄金角格采用

`floor(k·65536·(3−sqrt(5))/2) mod 65536`

并以整数平方根实现，不依赖浮点数决定相位。相位分辨率 65536 是本实验的选择，不是将 Q16 权重语义直接当作空间相位。

屏幕位置 `C sqrt(n)·exp(2πi φ(n)/65536)`、三角函数、六角最近点取整和取整后相对误差属于浮点观察。有限计算没有证明无限等分布、任意前缀无空洞或 Nollm 语义性能。六方向是 A2 兼容显示；数位深度仅是展示高度，不冒充原生物理层或 X6 分量。

## 实际复用 / BRC 观察审计

`REUSE_EXECUTED`：发布版 `core.demo_hex`、`canonical_bytes` / `fingerprint`。网页全部原数据匹配发布版指纹 `94df92927ff6952c86344ee2f38b428d273c7e749cb41343e25d5c2c5ae51160`。

`EXTEND_EXISTING_TOOL`：增加独立实验页面和生成器。保留身份与质数赋值后再作相位、连续位置和量化读出；多对一量化保留完整同格身份列表。没有把正权重质量当作相位相消，也没有提升新的 BRC 定理。

## 验证

```sh
PYTHONPATH=. python -m unittest discover -s tests -v
python tests/browser_multiplication.py
```

本轮记录 18 项单元测试通过；浏览器报告含 48 个实际通过的检查。包括全部输入因数分解、精确相位、修改相位的赋值规律、指定范围内乘法对、原坐标反例、Python/浏览器计数一致、当前网页保存与新文档恢复、配置拒绝不改状态、实际点选、PNG/JSON 下载、srcdoc 首页切换、移动布局以及零外部请求。

宿主禁止原生 file:// 导航，浏览器通过 `set_content` 接收 HTML，并在独立文档上下文运行。没有绕过宿主策略；未认证原生 iOS Safari、真实触摸硬件、整个 EM 仓库 CI 或生产负载。

## 发布范围

保持正式工具版本 0.3.0；本实验室为单独版本 0.1.0 的研究扩展。它只增加模块、测试、说明和验证，不覆盖原模板、核心几何、研究活动历史、基础定义或 Nollm 运行内核。正式发布状态以 GitHub PR/commit 与研究活动 checkpoint 的不可变读回为准。
