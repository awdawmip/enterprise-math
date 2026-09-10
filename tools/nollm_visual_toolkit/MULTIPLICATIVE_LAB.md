# 乘法记忆场实验室 0.1.0

Nollm Visual Toolkit 0.3.0 的独立实验扩展。**不是原生 X6 模型、Nollm 生产层或新定理接纳。** 原工具的 hex / X6 协议、工作台和静态站点生成器不变。

## 启动与网页生成

在 `tools/nollm_visual_toolkit` 内安装当前源码后：

```sh
python -m pip install .
python -m nollm_visual_toolkit.multiplicative --scheme mixed --out multiplication.html --preview
# 同时生成完整整数检查报告和可导入原工作台的 V2 数据
python -m nollm_visual_toolkit.multiplicative --scheme mixed --out multiplication.html \
  --report report.json --hex-data field.json
nollm-viz render field.json --out generic-workbench.html --preview
# 放入既有多数据静态研究站
nollm-viz site field.json --out research-site --preview
```

生成的 HTML 自包含，浏览器内生成全部 0—65535 标签，不依赖 CDN、账户或服务器。
`--preview` 复用 0.3.0 的 localhost 服务，不配置公开站点。研究包的 `output/index.html` 是可直接打开的 mixed 方案；`golden_prime.html`、`spiral.html` 是对照。

## 数学对象与四个方案

令 M=65536，保留精确整数标签 n，以及模 M 的整数相位 h(n)。它不是概率权重，也不能因数值范围相同就与 Q16 概率混为一谈。正整数才定义质因数分解及 Ω(n)；零单独绘制，相位和 Ω 用 null。

- `valuation`：第 i 个质数（i 从 1 起）的相位为 i*25033 mod M。
- `mixed`：用源码固定的 uint32 整数混合式给每个质数赋相位；不是密码学哈希或随机性承诺。
- 上述两种方案都按 h(n)=h(n/p)+h(p) mod M 递推，因而 h(ab)=h(a)+h(b) mod M。
- `spiral`：h(n)=n*25033 mod M。用作均匀布局对照，不承诺乘法或单位元相容。
- `radial`：h(n)=0。严格满足相位乘法，但所有点同向；它是“乘法成立不推出均匀”的对照。

25033 是将黄金角比例 `(3-sqrt(5))/2` 乘以 M 后取最近整数得到的本次有限相位步长。可在网页中修改前 100 个质数的相位；文件配置可指定最多 100 个任意范围内质数。仅两个质因数方案使用这些修改。

连续观察：`z(n)=C*sqrt(n)*exp(2*pi*i*h(n)/M)`。整数相位的乘法恒等式是精确的；其复数展示仍用浮点，不能以小浮点残差冒充代数证明。

立体观察的高度是 Ω(n)（质因数总次数）乘显示间距；Ω(ab)=Ω(a)+Ω(b)。这不是 Nollm 物理层、时间或新增原生轴。六方向箭头属于二维 A2 六邻接载体；没有把三个正交轴冒充原生六轴。原 Toolkit 的显式 X6 模式保持不变。

六角观察使用浮点最近中心与字典序平局规则。所有相同中心的记录都保留原 ID、n、相位与连续位置，可循环反查。没有将身份做商或合并。浮点近边界选点不宣称为精确几何证书。

## 操作

- 全量生成、尺度调整、质数相位重设与恢复。
- 连续场 / 六角单元 / Ω 立体分层；拖动、缩放、六方向观察、自动环视。
- 固定 Ω 层的切片。计数明确区分原始总体和当前入画记录；不抽样，但屏幕可重合或裁切。
- 整数、素数（合数背景保留）、相位、Ω、量化误差着色。
- 精确 a*b 标签检查，整数相位差，连续浮点差，六角量化差分开显示；越界不取模回绕。
- 倍乘轨迹、点选反查与同格身份轮换。
- 配置保存/恢复、报告 JSON、完整 V2 数据、PNG、可再打开的当前独立网页。

## 计数口径与有限观察

正整数 1—65535，8 个径向等面积带、32 个角向扇区。每个 n 的面积带通过整数序号确定，角向扇区通过整数相位确定。CV 为 `sqrt(B*sum(count_i^2)/N^2-1)`；总体固定，零不计入密度。切片或相机不会更改总体统计。

| 相位方案 | 256 格 CV | 使用的相位数 | 占用六角中心 | 全部正整数乘法相位失败 |
|---|---:|---:|---:|---:|
| 质数序号步长 | 0.1348815222 | 6543 | 44731 | 0 / 736957 |
| 固定整数混合 | 0.0516865734 | 41023 | 57380 | 0 / 736957 |
| 逐整数螺旋 | 0.0037743492 | 65535 | 53417 | 736956 / 736957 |
| 同向退化 | 5.5677643675 | 1 | 257 | 0 / 736957 |

所有乘法对为有序 a,b>=1 且 ab<=65535。未枚举超出域的乘积，也没有把所有图上的成对关系枚举成平方数量。默认 5*7 的量化差较大并非代码错误：严格相位与六角取整是不同操作。

序号方案有 h(n)=25033*sum_i(i*v_{p_i}(n)) mod M；大量不同整数共用这个加权和，从而产生辐射纹理。这里的 6543 是本次有限总体的计数，不宣称无限范围的闭式。混合相位在本次固定计数上改善 CV，但没有证明一般均匀分布、最优性或实际记忆效果。IID 参考 `sqrt((B-1)/N)` 不是显著性检验，亦不能以低于参考值称为“更随机”。

## 检验

```sh
python -m unittest discover -s tests -p 'test_multiplicative.py' -v
python tests/browser_multiplicative.py --out /tmp/multiplicative-ui
```

23 个扩展单元测试；34 项 Chromium 专项检查。Python 与浏览器的全量整数相位、Ω、密度分箱相同；默认方案的 65536 对六角取整坐标也相同。包括实际点选、下载 PNG/JSON、导出独立网页后重新执行和会话恢复。浏览器宿主阻止 file/http 导航，因而以 `set_content` 执行自包含页面；这不是本地 URL 服务测试或 iOS Safari 认证。

不重复标记原 0.3.0 的检查为本轮已执行；未跑整个 EM 仓库 CI、原工作台完整测试或 Nollm runtime。CLI 的 `--preview` 和 V2 导出复用原有接口，当前变更的定向验证与既有证据分别保留。

## 观察与信息保留边界

BRC 检查的落实：EXTEND_EXISTING_TOOL。使用整数标签和素因数信息先做代数，再进入有损观察；密度汇总、浮点显示、格点归并都不替代原身份。正权重 BRC 的质量相消不适用于复数相位，本实验没有虚构正质量抵消或调用无关定理。数学推广、语义质量和多质数物理路由均不由本页面证明。

Web 实现参考：MDN CanvasRenderingContext2D、HTMLCanvasElement.toBlob、Number.isSafeInteger。网页使用标准 Canvas 2D 和 Blob，不包含自制密码学或远程脚本。
