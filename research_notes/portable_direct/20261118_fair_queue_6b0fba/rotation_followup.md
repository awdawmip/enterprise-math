# 移动图册上的具名三力 Port 事件

任务 RS-X6-NATIVE-ROTATION-DYNAMICS。11 月 17 日的前沿将三十二条无向符号对角线上的商 $Q_{[v]}=\mathbb Z^6/(m\mathbb Z v)$ 随共同框架 $H=(C_2)^6\rtimes A_6$ 输运。[双陪集结果](rotation.md)确定拼接两段步词时需要的相对框架。若读数同时含图册、步词和具名 Port，应改用联合对象的稳定子；158 是前述两段步词在指定读数下的类数。

取已发表的 R762BY 条件事件。固定 Cell 锚点、正整数强度、三个各占不同轴的具名 Port 及循环 Links。可用 Port $p$ 将轴 $x$ 替换为一个空轴 $y$，其余两条射线不动。在基准图册 $D=(1,\ldots,1)$ 保留旧符号 $s$。以下把 $s$ 用作有向射线坐标，具名来源、原有分支、事件次序及可独立观测的内在荷或相位须分别携带。

**定理。** 若 $g e_i=\epsilon_i e_{\pi(i)}$，先执行基准事件再换框架得到 $s\epsilon_y$，以固定符号规则反序执行则得到 $s\epsilon_x$。对非空的可用 Port 集，每个不同轴对都出现在某条允许分支。故对全部分支交换的固定符号框架恰为统一翻号乘 $A_6$ 的 720 个元素。取 $[v]$ 中的符号修正规则
$$
E^v_{p,x\to y}:s e_x\longmapsto s\,v_xv_y\,e_y .
$$
它在 $D$ 恢复基准规则、对 $v\sim -v$ 良定义，并在整个 $H$ 上逐条满足
$$
 G_g E^v_{p,x\to y}=E^{gv}_{p,\pi(x)\to\pi(y)}G_g .
$$
这里 $\pi$ 表示轴置换。右路新符号为 $s\epsilon_x(\epsilon_xv_x)(\epsilon_yv_y)=s v_xv_y\epsilon_y$。两路有相同的占用、空轴和命名端口。每条符号线可从 $D$ 通过逐轴翻号得到，故这个等变要求唯一决定上述基准规则的延拓。同图册的多次替换从 $x_0$ 到 $x_n$，符号总乘数为 $v_{x_0}v_{x_n}$。

**检验。** 独立实现既有具名支路枚举，取 Port 0 可用。960 个有符号状态、2,880 条有向分支，在 32 张图册下逐一检验三种框架（翻第一轴、纯三循环、三循环附源轴三翻号）。276,480 次比较全部相等。逐种框架用未修复规则时，2,880 条分支中各有 960、0、960 个反例。由 $(+1,+2,+3)$ 将 Port 0 改至轴 4，只翻轴 1 即可直接观察到 $+4$ 与 $-4$ 的差异。下方 JavaScript 使用 0 起始的轴编号，可在标准 JS 引擎重放。

```javascript
let tests=0, failures=0; const fixed=[0,0,0];
const maps=[[0,1,2,3,4,5],[1,2,0,3,4,5],[1,2,0,3,4,5]], signs=[[-1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,-1,1,1,1]];
for(let x=0;x<6;x++)for(let a=0;a<6;a++)for(let b=0;b<6;b++){
 if(new Set([x,a,b]).size!==3)continue;
 for(let y=0;y<6;y++)if(![x,a,b].includes(y))for(let ss=0;ss<8;ss++){
  const s=[0,1,2].map(i=>1-2*((ss>>i)&1));
  for(let g=0;g<3;g++){
   const p=maps[g], e=signs[g];if(e[x]!==e[y])fixed[g]++;
   for(let mask=0;mask<32;mask++){
    const v=Array.from({length:6},(_,i)=>1-2*((mask>>i)&1));const w=Array(6);
    for(let i=0;i<6;i++)w[p[i]]=e[i]*v[i];
    const left=[s[0]*v[x]*v[y]*e[y],s[1]*e[a],s[2]*e[b]];
    const right=[s[0]*e[x]*w[p[x]]*w[p[y]],s[1]*e[a],s[2]*e[b]];
    if(left.some((z,i)=>z!==right[i]) || v[x]*v[y]!==(-v[x])*(-v[y]))failures++;
    tests++;
   }
  }
 }
}
if(tests!==276480||failures||String(fixed)!=="960,0,960")throw Error("check failed");
```

**物理边界。** 两路使用同一 Cell 锚点、端口名字、循环 Links、强度和外部时钟标签。这一试验没有给定真实三力事件的前后钟读数。若要将条件平方用于物理旋转，还需要来源可追的事件许可、换图册许可及两路实测末态与时间增量；射线的换号与未观测的 Port 内荷各自有不同检验。

[11 月 17 日的 32 图册前沿](https://github.com/awdawmip/enterprise-math/blob/fa2b887a5a6d071b191f2adc94a902fe26a20f15/research_artifacts/mcp/RS-X6-NATIVE-ROTATION-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/7ec46ff81cd7ab42fcbb/X6_ROTATING_DIAGONAL_32_CHART_EQUIVARIANT_BUNDLE_20261117.md) · [R762BY 的条件三力 Port 模型](https://github.com/awdawmip/enterprise-math/blob/91356f8b05c2682ca1bf454d9ea5fae686b7ee95/research_notes/portable_direct/R762BY_PORT_GATED_SIGNED_TRIAD_CLOSURE_THEOREM.md) · [原具名支路枚举入口](https://github.com/awdawmip/enterprise-math/blob/91356f8b05c2682ca1bf454d9ea5fae686b7ee95/research_notes/portable_direct/R762BY_PORT_GATED_NATIVE_TRIAD_VERIFY.py)
