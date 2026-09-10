# Nollm Visual Toolkit 0.2.0

**研究工作台／重要研究基础工具候选。** [English](README.md)

离线、可复算的整数六角场与显式 X6 数据观察工具。严格区分 **对象身份、观察映射、屏幕绘制**。这是软件版本发布，不是定理接纳、Nollm 生产集成，也不声称六维空间能够无损嵌入三维。

## 启动

在本目录使用 Python 3.10 或更新版本：

```sh
python -m pip install .
nollm-viz demo --out study.html
nollm-viz demo --kind x6 --out six_axes.html
```

用浏览器打开生成的 HTML。数据和程序包含在单个文件内，不需要 CDN、账户、服务器或遥测。默认示例含 0—65535 的全部 65,536 个整数。X6 示例是独立、明确标记的 729 状态合成六分量数据，绝不替旧六角数据补造缺失的原生坐标。

静态出图可选安装：`python -m pip install '.[static]'`。

## 已实现功能

- 六边形单元、可旋转的 A2 cube 平面，以及明确标记层高来源的分层视图。
- X6 六条 FCC 载体轴线、十二个正反方向；选择三个分量观察，或仅显示遗漏分量为零的真实切片。完整六分量始终保留。
- 整数、素数及合数背景、同余类、Q16 商／余数、一个权重单位之差、赋值以及自定义数值图层。
- 精确坐标切片、切片动画、摄像机旋转、编号／整数／坐标反查、重叠身份轮换、邻域与倍乘轨迹。
- 原关系边保留；筛选不删除数据。素数图不删去合数背景。零的赋值使用 null，不伪造有限值。
- JSON 和规定 CSV 格式的无损往返、PNG 截图、当前可见图元 SVG、绑定数据指纹的会话保存与恢复。SVG 不承诺包含全部界面、图例和关系叠加；PNG 像素不是可逆数据格式。
- 整数校验、投影重叠审计和确定性示例生成。渲染不抽样，但有限屏幕像素允许重叠。

## 坐标和观察约定

六角示例采用 `F(4n+d)=2 R60 F(n)+(d&1,d>>1)`，其中 `R60(q,r)=(-r,q+r)`。六邻接方向属于二维 A2 实现载体；`(q,r,-q-r)` 是三维显示坐标中的平面，不是六条独立原生空间轴。示例中的数位深度**不是** Nollm 物理层号。

X6 必须显式提供六个有符号整数分量。显示向量依次为 `(1,1,0)`、`(1,-1,0)`、`(1,0,1)`、`(1,0,-1)`、`(0,1,1)`、`(0,1,-1)`。按分量线性组合只是**声明的三维显示观察器**，不是已经完成的全局原生／FCC 桥。原分量、身份、关系和元数据全部保留，同一投影中心的多个身份分组反查而不合并。选择三个分量不等于处于三轴切片，除非其余相对分量确实为零。

遵循当前 `definitions/00_CURRENT_NATIVE_FOUNDATION.md`、`definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md` 和 `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json` 的类型边界。屏幕坐标、摄像机、欧氏出图不重新定义原生轴、度量、时间或 Cell 身份。本工具不改写项目基础定义。

## 数据格式

```json
{"schema":"NOLLM_VISUAL_DATA_V2","kind":"hex","title":"示例","metadata":{},"records":[{"id":"object-A","n":9,"coord":[2,3],"fields":{"score":7}}],"relations":[]}
```

X6 使用 `kind: "x6"` 和六个完整坐标。ID 是唯一字符串，不必等于行号；`n` 可省略。记录支持 `layer` 和额外 JSON 元数据。关系使用已存在的 `source`、`target` ID。当前限制为 1—200,000 条记录、坐标绝对值不超过 1,000,000；通用 JSON 整数须位于浏览器精确整数范围。这是实现边界，不是原生空间边界。不完整坐标和非有限浮点数被拒绝。

CSV 首行为 `#nollm-meta=<JSON>`，列名为 `id,coord_json,extra_json`。使用工具自带导出，不把任意扁平 CSV 当成同一协议。额外字段、关系、元数据和 null 保留。会话指纹描述浏览器规范化数据，不是服务器签名；规范 JSON 和原始来源字节的哈希分开记录。内置 SHA-256 后备实现已和 Python hashlib 比较，仅用于标准指纹，不是密码学创新或身份认证。

```sh
nollm-viz validate data.json
nollm-viz render data.json --out study.html
nollm-viz convert data.json --out data.csv
nollm-viz profile data.json --axis s --out slices.json
nollm-viz import-legacy interactive_65536.html --out recovered.json
```

旧版导入仅解码 JSON 字面量，不执行 HTML 或 JavaScript；原型零赋值的哨兵修正为 null。标准库 API 从 `nollm_visual_toolkit` 导入。

## 核验与限制

```sh
python -m unittest discover -s tests -v
# 可选界面核验：需要 Playwright 和本地 Chromium。
python tests/browser_smoke.py --out /tmp/nollm-ui
```

版本核验记录 26 项单元测试和 43 项 Chromium 界面检查，覆盖全部 65,536 个标签、Q16 重构、数据往返、切片、轨迹、邻域、X6 示例中 135 组投影重叠、会话恢复、导出及 390 像素移动布局。浏览器宿主通过 `set_content` 载入自包含 HTML，宿主不允许网络／文件导航。**未认证**真实 iOS Safari、触摸硬件、任意第三方数据、仓库全量 CI、Nollm 实际负载或 200,000 条上限性能。全量参与渲染不等于每个身份独占屏幕像素。

大量 SVG 导出或动画重绘可能较慢。动画是观察辅助，不是原生时间模拟。倍乘轨迹追踪声明的整数标签，不证明坐标乘法实现任意整数乘法。

## 版本边界

0.2.0 将原型误称“六轴”的三条直角轴视图改为明确分型的六角／X6 模式，修复局部缩放范围、行号身份假设、零赋值、投影重叠丢身份和会话恢复。包含源码、测试、清单及示例生成器；大型 HTML 数据不必入库。不会覆盖旧原型、历史研究活动、Nollm 架构或已接纳定理登记。

许可证：继承 Enterprise Math 的 MIT License。
