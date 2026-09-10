# 乘法记忆场 · Phase32 对照扩展 0.1.0

Nollm Visual Toolkit 0.3.0 的独立研究扩展。仓库已存在 16 位 `multiplicative.py` 与 `multiplicative_lab.html`；本模块保留它们，另开 `phase32_lab.py/html`，不覆盖原实验。三方案不仅位数不同，相位步长/散列定义也有变化，不能把指标差异单独归因为提高精度。原工具版本、V2 数据协议、X6 观察器和 Nollm 内核不变。本扩展没有把二维复数观察改称六维原生空间。

## 使用

在 `tools/nollm_visual_toolkit` 安装现有工具后：

```sh
python -m pip install .
# 生成三种对照方案的完整网页站，并复用 0.3.0 本地预览服务
python -m nollm_visual_toolkit.phase32_lab --site --out multiply-site --preview
# 生成单个离线 HTML
python -m nollm_visual_toolkit.phase32_lab --mode hash --out field.html
# 生成可复算的指标报告
python -m nollm_visual_toolkit.phase32_lab --mode hash --out field.html --report metrics.json
```

单页打开不需要 Python、网络、CDN 或账户；`--preview` 需要安装包含现有 `web.py` 的完整工具，默认 loopback 预览，不把它声称为公网部署。本轮 ZIP 包提供新增源码与已生成页面，不是假冒完整 0.3.0 安装包。

`--config` 接受保存的完整参数封套，亦接受其中的 `config` 对象。网页恢复按钮接受带 `schema/version/config` 的完整参数封套。`--site` 输出目录中的三个独立页面及首页，不能与单页 `--config` 混用。

## 接回现有工作台

```sh
python -m nollm_visual_toolkit.phase32_lab --mode hash --out field.html --hex-data phase32.json
nollm-viz render phase32.json --out shared-workbench.html --preview
```

V2 适配器不把图像倒推成原生坐标：保留整数标签、相位分子/分母、分解、理想浮点位置与每个观察 Cell 的身份。`layer` 明确是 Ω(n) 观察层。原来的 X6 模式不受此扩展影响。

## 做什么

- 保留 0—65535 的全部 65536 个标签；密度统计对 1—65535 等权，0 单独保留为吸收点，分解/相位为 null。
- 三种方案切换：质数序号相位、固定种子质数散列相位、逐数黄金角非乘法对照。
- 连续相位平面、近邻六角单元、独立的 Ω(n) 显示层。拖动、缩放、60° 观察旋转及环视。
- 修改任一范围内质数的相位并重算所有复合数，保留 uint32 相位分子。
- 验算 a×b、显示精确模相位缺陷、连续浮点相对误差、落格后相对误差；乘积越界明确拒绝，不绕回。
- a→ab→ab² 轨迹、整数查找、点选、同格身份轮换；多重占格不合并原标签。
- 64 扇区和 8 个等面积环的完整总体计数，角向 CV、联合 CV、空箱和占格多重数；相机变化不影响指标。
- 参数 JSON、包含分解和相位的全量数据 JSON、当前自包含网页、PNG 截图导出。

## 算术定义与精确性

令 D=2^32，声明 G=2654435761 为有限整数相位步长（并非精确无理黄金角）。按递增质数编号 j=1,2,...，序号方案为 `k(p_j)=(jG+seed) mod D`。散列方案用文件中的确定性 32 位混合函数，不声称密码学用途或真正随机性。用户覆盖表优先。

两种乘法方案均定义：

```
k(1)=0
k(n)=sum(v_p(n)*k(p)) mod D
z(n)=sqrt(n)*exp(2*pi*i*k(n)/D), n>0
z(0)=0
```

因此 `k(ab)=k(a)+k(b) mod D` 与 `z(ab)=z(a)z(b)` 在其定义范围内成立。模相位是精确整数计算；根号、三角函数及最近六角单元是浮点观察。误差证书不能把后者当成精确原生 Cell 分配。

对照定义 `k(n)=(n-1)G mod D`，只保证 k(1)=0，不保持一般乘法；2×2 已有反例。有限相位不是对象身份，所有数据始终保留 n；相位重合、格点重合、屏幕遮挡不得合并身份。相位/坐标也不是任意整数乘法的低成本推断算法：本扩展明确使用了分解/筛表。

相位分子在 0..D-1，递推求和小于 2^33；编号、分箱等乘积也在 JS 安全整数范围内。参考：MDN `Number.MAX_SAFE_INTEGER`，https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER 。哈希的 32 位乘法用 `Math.imul`。这些是实现工具，不是新的算术定理。

## 密度指标的范围

以 r²=n、最大半径²=N-1 定义 R 个等面积环；环号 `min(R-1, floor(nR/(N-1)))`。角向箱使用精确相位 `floor(kS/D)`。CV 是箱计数的总体标准差除以均值。零不入统计，原始标签仍保留。

当前固定种子 0、N=65536、R=8、S=64、格距 1 的完整结果：

| 方案 | 角向 CV | 环×扇区 CV | 多重占格额外标签数 | 模相位乘法 |
|---|---:|---:|---:|---|
| 质数序号 | 0.199307 | 0.247274 | 18038 | 保持 |
| 质数散列 | 0.023675 | 0.079105 | 8181 | 保持 |
| 逐数黄金角 | 0.000800 | 0.005870 | 0 | 不保持 |

这不是无穷均匀分布、任何种子均好、最优模型或语义效果的证明。扩大/旋转相机不改变这些结果；修改相位种子、总体、环箱数、格距会改变相应观察。

## 验证

```
python -m unittest discover -s tests -p 'test_phase32_lab.py' -v
python tests/browser_phase32_lab.py
```

新增 17 项 Python 测试；39 项 Chromium 浏览器检查。Python 检验全量分解恢复和所有正整数有序因子对（积<65536）的模相位恒等式；浏览器对三方案全部相位及箱计数与 Python 比对。导出重新打开、0、越界、负测试、修改质数只按赋值改变、移动视口均已检查。

截图是实际浏览器渲染，不是图像生成的示意。验收通过 `set_content`，不是 iOS Safari/真实触摸认证。没有重跑整个 EM CI 或旧工具全部测试；本增量不修改旧核心、前端或预览服务，只扩展 package-data 对新 HTML 的包含。图片与浮点取格可能随浏览器出现微小边界差异。

## 结构复用与边界

`EXTEND_EXISTING_TOOL`：新增观察页及生成器，复用既有 `web.serve_preview` 接口。不扩写正式 BRC 定理族；正质量分支语义不适用于此处的复相位。实际遵守观察保真要求：保留 n、质数赋值、模相位、量化坐标和原始身份组，先比较精确相位再比较浮点显示，密度直方图是派生观察而非状态替代。P000、X6/FCC 原生定义、原关系和生产数据不变。
