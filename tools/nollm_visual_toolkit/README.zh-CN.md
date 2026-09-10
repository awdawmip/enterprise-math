# Nollm Visual Toolkit 0.3.0

**研究工作台／重要研究基础工具候选。** [English](README.md)

离线、可复算的整数六角场与显式 X6 数据观察工具。严格区分 **对象身份、观察映射、屏幕绘制**。0.3.0 在 0.2.0 工作台上增加了完整的网页生成与本地预览链路；它仍然是研究观察／导出工具，不是定理接纳、Nollm 生产集成，也不声称六维空间能够无损嵌入三维。

## 最快使用

在本目录使用 Python 3.10 或更新版本：

```sh
python -m pip install .

# 生成一个自包含网页并立即本机预览
nollm-viz demo --out study.html --preview

# 一次生成 hex + X6 的静态预览站点，并打开首页
nollm-viz site --out preview-site --preview
```

`--preview` 会先写文件，再启动仅监听 `127.0.0.1` 的本地 HTTP 服务并尝试打开默认浏览器；按 Ctrl-C 停止。生成的工作台页面仍然是单文件、自包含、无 CDN、无遥测、无账户依赖。

如果只想生成文件而不启动服务器：

```sh
nollm-viz demo --out study.html
nollm-viz render data.json --out study.html
nollm-viz site --out preview-site
```

## 网页生成与预览

### 1. 单页工作台

```sh
nollm-viz render data.json --out study.html --preview
nollm-viz render data.csv  --out study.html
```

单页 HTML 内嵌完整规范化数据、数据 SHA-256 指纹和工作台程序。用户标题、字段等数据先作为 JSON 载荷进入模板，不执行其中的 HTML/JavaScript。

### 2. 静态研究站点

```sh
# 无输入时生成内置 65,536 整数 hex + 729 状态 X6 示例
nollm-viz site --out preview-site

# 用自己的多个数据集生成站点
nollm-viz site run-a.json run-b.csv --out comparison-site --title "实验对比"

# 内置示例可调小 hex 数量，或不生成 X6
nollm-viz site --out quick-site --hex-count 4096 --no-x6
```

站点目录包含：

- `index.html`：可切换各研究页面的预览首页；
- 每个数据集一个自包含工作台 HTML；
- `manifest.json`：`NOLLM_VISUAL_SITE_V1`，记录工具版本、页面、数据类型、记录数和规范数据指纹。

首页中的 iframe 只是观察页面切换器，不合并、不重写数据；每个工作台仍可独立打开和分发。同一有序数据集与标题会得到确定性的站点清单和首页，不写入时间戳、主机路径或随机数。

### 3. 预览已有页面或站点

```sh
nollm-viz preview study.html
nollm-viz preview preview-site
nollm-viz preview preview-site --port 8000 --no-open
```

默认 `--host 127.0.0.1`、`--port 0`（自动选择空闲端口）。单 HTML 模式只允许访问目标 HTML，不把同目录其他文件顺带暴露。目录模式用于明确预览整个生成站点。非回环地址默认拒绝；确需局域网访问时必须显式同时给出目标主机和 `--allow-remote`：

```sh
nollm-viz preview preview-site --host 0.0.0.0 --port 8000 --allow-remote
```

这会扩大可访问范围，应只在受信网络中使用。

## 已实现工作台功能

- 六边形单元、可旋转的 A2 cube 平面，以及明确标记层高来源的分层视图。
- X6 六条 FCC 载体轴线、十二个正反方向；选择三个分量观察，或仅显示遗漏分量为零的真实切片。完整六分量始终保留。
- 整数、素数及合数背景、同余类、Q16 商／余数、一个权重单位之差、赋值以及自定义数值图层。
- 精确坐标切片、切片动画、摄像机旋转、编号／整数／坐标反查、重叠身份轮换、邻域与倍乘轨迹。
- 原关系边保留；筛选不删除数据。素数图不删去合数背景。零的赋值使用 null，不伪造有限值。
- JSON 和规定 CSV 格式的无损往返、PNG 截图、当前可见图元 SVG、绑定数据指纹的会话保存与恢复。SVG 不承诺包含全部界面、图例和关系叠加；PNG 像素不是可逆数据格式。
- 整数校验、投影重叠审计和确定性示例生成。渲染不抽样，但有限屏幕像素允许重叠。

静态 Matplotlib 出图仍为可选依赖：`python -m pip install '.[static]'`。

## 坐标和观察约定

六角示例采用 `F(4n+d)=2 R60 F(n)+(d&1,d>>1)`，其中 `R60(q,r)=(-r,q+r)`。六邻接方向属于二维 A2 实现载体；`(q,r,-q-r)` 是三维显示坐标中的平面，不是六条独立原生空间轴。示例中的数位深度**不是** Nollm 物理层号。

X6 必须显式提供六个有符号整数分量。显示向量依次为 `(1,1,0)`、`(1,-1,0)`、`(1,0,1)`、`(1,0,-1)`、`(0,1,1)`、`(0,1,-1)`。按分量线性组合只是**声明的三维显示观察器**，不是已经完成的全局原生／FCC 桥。原分量、身份、关系和元数据全部保留，同一投影中心的多个身份分组反查而不合并。选择三个分量不等于处于三轴切片，除非其余相对分量确实为零。

遵循当前 `definitions/00_CURRENT_NATIVE_FOUNDATION.md`、`definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md` 和 `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json` 的类型边界。屏幕坐标、摄像机、欧氏出图和网页预览均不重新定义原生轴、度量、时间或 Cell 身份。本工具不改写项目基础定义。

## 数据格式

```json
{"schema":"NOLLM_VISUAL_DATA_V2","kind":"hex","title":"示例","metadata":{},"records":[{"id":"object-A","n":9,"coord":[2,3],"fields":{"score":7}}],"relations":[]}
```

X6 使用 `kind: "x6"` 和六个完整坐标。ID 是唯一字符串，不必等于行号；`n` 可省略。记录支持 `layer` 和额外 JSON 元数据。关系使用已存在的 `source`、`target` ID。当前限制为 1—200,000 条记录、坐标绝对值不超过 1,000,000；通用 JSON 整数须位于浏览器精确整数范围。这是实现边界，不是原生空间边界。不完整坐标和非有限浮点数被拒绝。

CSV 首行为 `#nollm-meta=<JSON>`，列名为 `id,coord_json,extra_json`。使用工具自带导出，不把任意扁平 CSV 当成同一协议。额外字段、关系、元数据和 null 保留。会话指纹描述浏览器规范化数据，不是服务器签名；规范 JSON 和原始来源字节的哈希分开记录。内置 SHA-256 后备实现只用于标准指纹，不是密码学创新或身份认证。

```sh
nollm-viz validate data.json
nollm-viz convert data.json --out data.csv
nollm-viz profile data.json --axis s --out slices.json
nollm-viz import-legacy interactive_65536.html --out recovered.json
```

旧版导入仅解码 JSON 字面量，不执行 HTML 或 JavaScript；原型零赋值的哨兵修正为 null。标准库 API 从 `nollm_visual_toolkit` 导入；0.3.0 还导出 `build_site`、`demo_site`、`preview_server` 和 `serve_preview`。

## 核验与限制

```sh
python -m unittest discover -s tests -v
```

0.3.0 本轮离线回归运行 36 项单元测试：35 通过，1 项可选 Matplotlib 静态出图测试因当前执行环境未安装 Matplotlib 而跳过；新增的 10 项 Web 测试全部通过。另完成已安装 CLI 的 `demo -> validate -> site` 冒烟，验证生成页、数据指纹和 `NOLLM_VISUAL_SITE_V1` manifest 一致。

0.2.0 已记录的 43 项 Chromium 工作台界面验收仍是**未改动 workbench 前端逻辑**的既有证据；本轮没有把它重新包装成新的浏览器认证。真实 iOS Safari、物理触摸设备、任意第三方数据、仓库全量 CI、Nollm 实际负载和 200,000 条上限性能仍未认证。

大量 SVG 导出或动画重绘可能较慢。动画是观察辅助，不是原生时间模拟。倍乘轨迹追踪声明的整数标签，不证明坐标乘法实现任意整数乘法。网页预览服务器用于研究查看，不是生产 Web 服务。

## 版本边界

- **0.2.0**：把原型误称“六轴”的三条直角轴视图改为明确分型的 hex／X6 模式，修复局部缩放范围、行号身份假设、零赋值、投影重叠丢身份和会话恢复。
- **0.3.0**：保留上述数学／观察契约，新增静态站点生成、首页内嵌预览、manifest、localhost HTTP 预览、单文件访问隔离、非回环绑定显式授权，以及 `demo/render/site --preview` 连续工作流。

BRC 对本轮 HTTP／静态页面工程层为 `NOT_APPLICABLE`；没有通过网页层压缩或替换整数、坐标、赋值、关系等数学载体。

许可证：继承 Enterprise Math 的 MIT License。
