# Nollm Visual Toolkit 0.4.0

**研究工作台／重要研究基础工具候选。** [English](README.md)

离线、可复算的 hex／X6 观察工具，并新增专门的 **Multiplicative Memory Field Lab（乘法记忆场实验页）**。始终严格区分 **算术/原生身份、观察坐标、屏幕绘制**。这是研究基础设施，不是数学定理接纳，也不修改 Nollm 生产运行时。

## 最快使用

```sh
python -m pip install .

# 原有 typed hex/X6 工作台
nollm-viz demo --out study.html --preview

# 一次生成 hex + X6 + 乘法记忆场研究站
nollm-viz site --out preview-site --with-field --preview

# 单独生成乘法记忆场网页
nollm-viz field --out multiplicative.html --count 65536 --preview
```

页面均自包含，不依赖 CDN、账户、遥测或远程服务。本地预览默认仅监听 `127.0.0.1`；非回环地址仍必须显式 `--allow-remote`。

## 0.4.0：乘法记忆场实验页

这次不是把整数直接压成一张“好看的图”，而是先保留 BRC 要求的算术 carrier，再生成观察坐标。

### 先保留算术 carrier

对每个正整数：

```text
n = product p^v_p(n)
A(n) = sum v_p(n) * h_seed(p)
```

`h_seed(p)` 是确定性的无符号 32 位质数相位码，并固定 `h_seed(2)=0`，让 ×2 的额外质数相位不干扰原有 dyadic frame。`A(n)` 使用**不取模截断的整数累加**，因此串行乘法在 carrier 层保持：

```text
A(ab) = A(a) + A(b)
```

0 是特殊吸收态，不参与对数恒等式；1 是乘法单位。整数身份、质因数分解和 valuation 是 carrier，下面的半径/角度只是 observer。

### 乘法观察器

对 `n>0`：

```text
r(n) = n^alpha
theta(n) = frame_strength * (pi/4) * log2(n)
         + phase_strength * 2*pi*A(n)/2^32
```

默认 `alpha=1/2`，对应二维等面积密度候选。页面同时画出 16 条间隔 22.5° 的 Nollm frame 参考辐条，明确区分“当前 frame 骨架”和“研究用质数相位”。

网页可以直接操作：

- 调整数的数量和质数相位 seed；
- 调径向指数、frame 强度、质数相位强度；
- 一键切换 `Frame only` / `Prime phase` / `Hybrid`；
- 按素数/合数、`n mod k`、`Omega(n)`、`v2(n)`、质数相位着色；
- 点选整数，反查质因数分解和整数相位累加值；
- 查看 `n, mn, m^2n, ...` 乘法轨迹；
- 测角向 sector CV、等面积径向 CV；
- 自动显示“角向 CV / 独立均匀占位基准 `sqrt((S-1)/B)`”；
- 导出 PNG 和配置 JSON。

屏幕像素只是观察器。即使多个点落到同一像素，也不合并算术身份。

### 当前 65,536 点有限对照

固定默认 seed、64 个角扇区、每块 1024 个连续正整数时：

- Hybrid 角向 CV：`0.2344`；
- 独立均匀占位基准：`sqrt(63/1024)`；
- Hybrid / iid 基准：`0.945`；
- Frame-only / iid 基准：`27.696`；
- `alpha=1/2` 的等面积径向 CV：`0.0001`。

这些是**固定有限总体的观察诊断**，不是渐近定理，也不证明当前相位方案全局最优。

## 网页研究站

0.3.0 的网页生成与预览继续保留，并能直接挂上乘法记忆场：

```sh
# hex + X6
nollm-viz site --out preview-site

# hex + X6 + 乘法记忆场
nollm-viz site --out preview-site --with-field

# 指定乘法场总体和 seed
nollm-viz site --out preview-site --with-field \
  --field-count 65536 --field-seed 814210

# 多个自己的数据集 + 乘法场
nollm-viz site run-a.json run-b.csv --out comparison-site \
  --title "实验对比" --with-field

# 预览已有页面或站点
nollm-viz preview multiplicative.html
nollm-viz preview preview-site
```

首页 iframe 只负责切换观察页面，不合并数据。`manifest.json` 仍使用 `NOLLM_VISUAL_SITE_V1`；乘法场页面记录为 `multiplicative-field-observer`，并保存确定性配置指纹。

## 原有工作台能力保持不变

- 原生六边形单元、A2 cube 平面和显式 layer stack；
- 显式六分量 X6 数据、六条 FCC 载体轴线／十二个正反方向；
- 切片、查找、投影碰撞审计、邻域、整数标签倍乘轨迹；
- Q16 商/余数、同余类、素数背景和自定义图层；
- 规范 JSON/CSV 无损往返、PNG/SVG 观察导出、绑定数据指纹的会话恢复。

hex 与 X6 不互相补造坐标。A2 的 `(q,r,-q-r)` 是二维显示平面，不是六个独立原生维度；X6 到三维的 FCC 线性组合仍只是声明的观察器，不是已经完成的全局原生桥。

## CLI

```sh
nollm-viz validate data.json
nollm-viz render data.json --out study.html --preview
nollm-viz convert data.json --out data.csv
nollm-viz profile data.json --axis s --out slices.json
nollm-viz import-legacy interactive_65536.html --out recovered.json

nollm-viz field --out field.html --count 65536 --seed 814210 \
  --alpha 0.5 --frame-strength 1 --phase-strength 1 \
  --certificate carrier.json
```

`--certificate` 是有限总体上的精确算术 carrier 检查，不是无限尺度均匀性证明。

## 核验

0.4.0 本轮实际完成：

- 共发现 45 项单元测试：44 通过；1 项可选 Matplotlib 测试因环境未安装该依赖而跳过；
- 7 项乘法场单元测试全部通过；
- 12 项网页/站点测试全部通过，包含乘法场站点集成；
- Chromium 对完整 65,536 点乘法场执行 21 项专项验收，页面错误 0、网络请求 0；
- Python 与浏览器的代表性质数相位码一致；
- 65,536 总体 carrier certificate 对 16,384 个有界乘积做精确检查，相位累加加法失败 0；
- `field`、`site --with-field` CLI 冒烟通过；
- 0.4.0 wheel 构建通过，包含 `multiplicative.py`、`web.py`、`workbench.html`。

0.2/0.3 既有 typed workbench 浏览器证据单独保留，不冒充本轮重新认证。真实 iOS Safari、物理触摸、仓库全量 CI、Nollm 实际负载和生产性能仍未认证。

## BRC / 结论边界

本轮对乘法场研究面实际应用 BRC：

- population：声明的有限整数区间；
- carrier：整数身份、稀疏 prime valuation、整数 prime-phase accumulator；
- serial composition：普通整数乘法；
- observer：半径、角度、颜色、CV、屏幕位置；
- 信息损失保护：observer 不替代 carrier；
- 状态：可执行研究观察器，不进行 Foundation/定理晋升。

确定性质数相位散列是研究选择，不是经典数论的 canonical 定义；有限 CV 不是渐近结论。

## 版本边界

- **0.2.0**：typed hex/X6 与身份保护。
- **0.3.0**：确定性静态站点生成和受限 localhost 预览。
- **0.4.0**：加入以精确算术 carrier 为底层的 Multiplicative Memory Field Lab，并接入 CLI、站点和完整 65,536 点浏览器专项验收。

许可证：继承 Enterprise Math 的 MIT License。
