"""Self-contained browser observer template; embedded in a .py for wheel inclusion."""
TEMPLATE = r'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>乘法数场 · Nollm 观察实验室</title>
<style>
:root{--bg:#101b28;--panel:#172536;--line:#31465a;--ink:#ecf3f9;--muted:#a6b8c8;--accent:#5ce0bf}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}header{padding:18px 24px;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:14px}header small{color:var(--accent);letter-spacing:2px;font-size:10px}h1{margin:2px 0;font-size:23px}h2{font-size:13px;margin:18px 0 9px;color:var(--accent)}h2:first-child{margin-top:0}.tag,.hint{font-size:11px;color:var(--muted)}main{display:grid;grid-template-columns:250px minmax(360px,1fr) 275px;height:calc(100vh - 100px);min-height:620px}aside{background:var(--panel);padding:17px;overflow:auto}aside:first-child{border-right:1px solid var(--line)}aside:last-child{border-left:1px solid var(--line)}label{display:block;font-size:12px;margin:8px 0;color:var(--muted)}input,button,select{font:inherit;color:var(--ink);background:#101d2b;border:1px solid var(--line);padding:7px;border-radius:5px;max-width:100%}input[type=number],select{width:100%}input[type=range]{width:100%;padding:0}button{cursor:pointer}button:hover{border-color:var(--accent)}button.primary{background:#245b55;border-color:var(--accent)}.row{display:flex;gap:6px;margin:7px 0}.row>*{flex:1;min-width:0}.stage{position:relative;min-width:0;min-height:0;overflow:hidden;background:#0d1723}#fieldCanvas{width:100%;height:100%;display:block;touch-action:none}#hud{position:absolute;left:14px;right:14px;top:12px;pointer-events:none;display:flex;justify-content:space-between;gap:10px;font-size:11px}#hud span{background:#132232dc;padding:7px;border:1px solid var(--line);border-radius:5px}#legend{position:absolute;bottom:12px;left:14px;right:14px;font-size:11px;color:var(--muted);pointer-events:none;background:#132232e0;padding:8px}.metric{font-size:22px;font-variant-numeric:tabular-nums}.box{padding:10px 0;border-bottom:1px solid var(--line)}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:11px/1.5 ui-monospace,monospace;padding:10px;background:#101d2b;max-height:240px;overflow:auto}#hist{width:100%;height:72px}#err{color:#ffb59c;font-size:12px;white-space:pre-wrap}a{color:var(--accent)}details{margin-top:15px}summary{cursor:pointer;font-size:12px}footer{font-size:11px;color:var(--muted);padding:8px 20px;border-top:1px solid var(--line)}
@media(max-width:1120px){main{grid-template-columns:230px minmax(340px,1fr)}aside:last-child{grid-column:1/3;display:grid;grid-template-columns:1fr 1fr;gap:16px}main{height:auto}.stage{height:75vh;min-height:560px}}@media(max-width:650px){header{padding:12px 15px}h1{font-size:19px}.tag{display:none}main{display:flex;flex-direction:column;min-height:0}aside{max-height:330px;padding:14px}.stage{height:65vh;min-height:420px}aside:last-child{display:block;max-height:none}.metric{font-size:20px}}
</style></head><body>
<header><div><small>NOLLM · VISUAL TOOLKIT / LAB 0.1.0</small><h1>乘法数场 · 观察实验室</h1></div><div class="tag">整数身份不变 / 相位可调 / 布局与量化分开<br>离线 HTML · A2 与候选极坐标，不伪造 X6</div></header>
<main><aside>
<h2>01 / 同一批数，两个布局</h2>
<label>布局<select id="layout"><option value="polar">候选：√n 半径 × 可加相位</option><option value="legacy">基准：原四进制六角编码</option></select></label>
<label>质数相位规则<select id="mode"><option value="golden">按质数顺序取黄金角（整数化）</option><option value="rank">按质数序号等分一周</option><option value="zero">全零相位（反例对照）</option></select></label>
<label>着色<select id="color"><option value="mod3">n mod 3</option><option value="prime">素数与合数背景</option><option value="n">整数标签 n</option><option value="q16">Q16 余数（权重 2731）</option><option value="load">量化单元重叠数</option></select></label>
<label><input id="quantized" type="checkbox">显示取整后的六角单元</label>
<label><input id="stack" type="checkbox">按数位深度立体分层（观察高度）</label>
<label>布局尺度 C：<span id="scaleText">1</span><input id="scale" type="range" min="0.5" max="3" step="0.1" value="1"></label>
<div class="hint">布局尺度改变格点占用；相机缩放只改变画面。两者不混用。</div>
<div class="row"><button id="fit">全图</button><button id="zin">放大</button><button id="zout">缩小</button></div>
<div class="row"><button id="turn">旋转 60°</button><button id="top">俯视</button><button id="oblique">立体</button></div>
<h2>02 / 改一个质数的相位</h2><div class="row"><label>质数 p<input id="prime" type="number" value="5" min="2"></label><label>相位格 0—65535<input id="tick" type="number" value="0" min="0" max="65535"></label></div>
<div class="row"><button id="applyPhase">应用</button><button id="resetPhase">清除所有修改</button></div>
<h2>03 / 倍乘与范围</h2>
<div class="row"><label>起点 n<input id="start" type="number" value="3" min="0"></label><label>倍数 k<input id="k" type="number" value="4" min="2"></label></div>
<button class="primary" id="trace">定位并画倍乘轨迹</button>
<label>显示 0 至 N<input id="limit" type="number" min="15" value="65535"></label><div class="row"><button id="prefix">应用范围</button><button id="all">全部数</button></div>
<details><summary>保存与复现</summary><div class="row"><button id="saveHtml">保存当前网页</button><button id="png">导出 PNG</button></div><div class="row"><button id="report">报告 JSON</button><button id="source">原数据 V2</button></div><div class="row"><button id="session">保存配置</button><label>恢复配置<input id="file" type="file" accept=".json"></label></div><p class="hint">PNG 不能反解数据；报告保留相位表与源数据指纹。原 V2 可直接交给 nollm-viz site。</p></details><p id="err" role="alert"></p>
</aside><section class="stage"><canvas id="fieldCanvas"></canvas><div id="hud"><span id="scene"></span><span id="count"></span></div><div id="legend"></div></section><aside>
<div><h2>观察审计 · 当前完整范围</h2><div class="box"><div class="hint">64 扇区计数 CV / 排除 0</div><div class="metric" id="cv"></div><canvas id="hist"></canvas><div class="hint">越低表示这次角向计数越接近均分，不代表局部无空洞。</div></div>
<div class="box"><div class="hint">六角取整后：占用格 / 身份数</div><div class="metric" id="occupied"></div><div class="hint" id="overlap"></div></div>
<div class="box"><div class="hint">所选 k 的全部可计算乘法对</div><pre id="audit"></pre></div></div>
<div><h2>点选反查</h2><div class="row"><button id="next">同一量化格的下一身份</button></div><pre id="detail"></pre><div class="hint">同格不合并 ID。候选极坐标的整数相位恒等式由定义保证；浮点成图与取整不继承严格乘法。</div><h2>保留的边界</h2><p class="hint">零没有质因数分解或相位。R²=n 固定了径向计数；该计数不是新发现。六方向属于显示平面的 A2 载体；分层高度不是 Nollm 物理层。</p><p class="hint" id="fingerprint"></p></div>
</aside></main><footer>候选模型比较工具，不改生产内核、X6 定义或原整数坐标。拖动画布旋转；按钮与滚轮调整观察。所有选中记录参与绘制，像素遮挡不等于身份消失。</footer>
<script id="payload" type="application/json">__LAB_PAYLOAD__</script><script id="initial" type="application/json">null</script>
<script>
'use strict';
const P=JSON.parse(document.getElementById('payload').textContent), M=P.modulus, rows=P.data.records, N=rows.length, spf=P.spf;
const $=id=>document.getElementById(id), canvas=$('fieldCanvas'), ctx=canvas.getContext('2d'), SQ=Math.sqrt(3);
const DEFAULT={layout:'polar',mode:'golden',color:'mod3',quantized:false,stack:false,scale:1,zoom:1,yaw:0,pitch:0,limit:N-1,selected:3,k:4,overrides:{}};
let S=JSON.parse(JSON.stringify(DEFAULT));
let phi=[],table={},points=[],cells=[],groups=new Map(),report={},screens=[],drawn=0,frame=0,drag=null,bounds={};
const mod=(x,m)=>((x%m)+m)%m;
const checkInt=(x,min,max)=>Number.isSafeInteger(x)&&x>=min&&x<=max;
const copy=x=>JSON.parse(JSON.stringify(x));
function validateState(s){
 if(!s||!['polar','legacy'].includes(s.layout)||!['golden','rank','zero'].includes(s.mode)||!['n','mod3','prime','q16','load'].includes(s.color))throw Error('不支持的布局或图层');
 for(const key of ['stack','quantized'])if(typeof s[key]!=='boolean')throw Error('布尔配置无效');
 for(const [key,lo,hi] of [['scale',.5,3],['zoom',.15,40],['yaw',-10000,10000],['pitch',-1.55,1.55]])if(typeof s[key]!=='number'||!Number.isFinite(s[key])||s[key]<lo||s[key]>hi)throw Error('观察范围无效：'+key);
 if(!checkInt(s.limit,15,N-1)||!checkInt(s.selected,0,s.limit)||!checkInt(s.k,2,N-1))throw Error('整数范围无效');
 if(!s.overrides||Array.isArray(s.overrides)||typeof s.overrides!=='object')throw Error('相位表格式无效');
 for(const [p,v] of Object.entries(s.overrides))if(!/^\d+$/.test(p)||!checkInt(+p,2,N-1)||spf[+p]!==+p||!checkInt(v,0,M-1))throw Error('只接受范围内质数的整数相位');
}
function configure(change){const next={...copy(S),...change};validateState(next);S=next;sync();recompute();}
function phaseTable(){table={};for(const p of Object.keys(P.golden))table[p]=S.mode==='zero'?0:(S.mode==='golden'?P.golden[p]:P.rank[p]);Object.assign(table,S.overrides);phi=[null,0];for(let n=2;n<N;n++)phi[n]=(phi[n/spf[n]]+table[spf[n]])%M;}
function roundHex(x,y){let q=x-y/SQ,r=2*y/SQ,s=-q-r,a=Math.round(q),b=Math.round(r),c=Math.round(s),da=Math.abs(a-q),db=Math.abs(b-r),dc=Math.abs(c-s);if(da>=db&&da>=dc)a=-b-c;else if(db>=dc)b=-a-c;return [a||0,b||0];}
function fact(n){if(n===0)return null;const a=[];while(n>1){const p=spf[n];let k=0;while(n%p===0){n/=p;k++;}a.push([p,k]);}return a;}
function trace(){let x=S.selected,out=[];while(x<=S.limit&&out.length<64&&!out.includes(x)){out.push(x);x*=S.k;}return out;}
function hexProd(a,b){return [a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]];}
function recompute(){
 phaseTable();points=[];cells=[];groups=new Map();const hist=Array(64).fill(0);let rmax=0;
 for(let n=0;n<=S.limit;n++){
  let x,y,t;if(S.layout==='legacy'){const [q,r]=rows[n].coord;x=q+r/2;y=SQ*r/2;t=mod(Math.atan2(y,x)/(2*Math.PI),1);}else{t=n?phi[n]/M:0;const rad=n?S.scale*Math.sqrt(n):0;x=rad*Math.cos(2*Math.PI*t);y=rad*Math.sin(2*Math.PI*t);}
  const cell=S.layout==='legacy'?rows[n].coord.slice():roundHex(x,y),key=cell.join(',');if(!groups.has(key))groups.set(key,[]);groups.get(key).push(n);cells.push(cell);
  if(n)hist[Math.min(63,Math.floor(t*64))]++;
  const z=S.stack?(rows[n].layer||0)*24:0;
  points.push([S.quantized?cell[0]+cell[1]/2:x,S.quantized?SQ*cell[1]/2:y,z]);rmax=Math.max(rmax,Math.hypot(x,y));
 }
 const mean=S.limit/64,cv=Math.sqrt(hist.reduce((a,c)=>a+(c-mean)**2,0)/64)/mean;
 const pairs=Math.floor(S.limit/S.k);let failed=0,witness=null,sumErr=0,maxErr=0;
 for(let n=1;n<=pairs;n++){
  if(S.layout==='legacy'){const got=hexProd(rows[n].coord,rows[S.k].coord),want=rows[n*S.k].coord;if(got[0]!==want[0]||got[1]!==want[1]){failed++;if(!witness)witness={n,k:S.k,predicted:got,actual:want};}}
  else{
   if(phi[n*S.k]!==mod(phi[n]+phi[S.k],M))failed++;
   const [q,r]=cells[n],[u,v]=cells[n*S.k],x=q+r/2,y=SQ*r/2,a=2*Math.PI*phi[S.k]/M,f=Math.sqrt(S.k);
   const dx=(x*Math.cos(a)-y*Math.sin(a))*f-(u+v/2),dy=(x*Math.sin(a)+y*Math.cos(a))*f-SQ*v/2;
   const error=Math.hypot(dx,dy)/(S.scale*Math.sqrt(n*S.k));sumErr+=error;maxErr=Math.max(maxErr,error);
  }
 }
 const sizes=[...groups.values()].map(a=>a.length);
 report={schema:'NOLLM_MULTIPLICATION_OBSERVATION_V1',lab_version:P.lab_version,data_sha256:P.data_sha256,population:S.limit+1,angular_population:S.limit,angular_bins:64,angular_counts:hist,angular_cv:cv,occupied_cells:groups.size,collision_groups:sizes.filter(n=>n>1).length,excess_identities_if_collapsed:S.limit+1-groups.size,max_cell_load:Math.max(...sizes),multiplier:S.k,multiplication_pairs:pairs,exact_failures:failed,first_witness:witness,quantized_relative_error_mean:S.layout==='polar'?sumErr/pairs:null,quantized_relative_error_max:S.layout==='polar'?maxErr:null,exact_scope:S.layout==='polar'?'phase ticks add and squared-radius labels multiply BY CONSTRUCTION':'exact complex multiplication of original Eisenstein coordinates',quantization_scope:'float display rounding; NOT original data or native production geometry',state:copy(S)};
 bounds={min:[Infinity,Infinity,Infinity],max:[-Infinity,-Infinity,-Infinity]};for(const p of points)for(let j=0;j<3;j++){bounds.min[j]=Math.min(bounds.min[j],p[j]);bounds.max[j]=Math.max(bounds.max[j],p[j]);}
 $('cv').textContent=cv.toFixed(5);$('occupied').textContent=groups.size.toLocaleString()+' / '+(S.limit+1).toLocaleString();$('overlap').textContent=`${report.collision_groups.toLocaleString()} 个重叠组；若合并会少 ${report.excess_identities_if_collapsed.toLocaleString()} 个身份。本工具不合并。`;
 $('audit').textContent=JSON.stringify({范围内乘法对:pairs,精确条件失败:failed,条件:S.layout==='polar'?'相位整数可加（定义保证）':'原六角坐标直接相乘',首个反例:witness,取整后平均相对偏差:report.quantized_relative_error_mean},null,2);
 $('legend').textContent=S.color==='prime'?'亮色：素数；灰色：合数；0 与 1 不是素数。':S.color==='mod3'?'颜色：青绿 = 余数 0；橙 = 余数 1；紫 = 余数 2。':S.color==='q16'?'颜色：(2731 × n) mod 65536；原始整数仍可反查。':S.color==='load'?'颜色：同一量化格中的身份数；颜色高不代表源数据重复。':'颜色：整数标签 n；屏幕重合不合并身份。';
 detail();drawHistogram(hist);schedule();
}
function detail(){const n=S.selected,cell=cells[n],ids=groups.get(cell.join(','));$('detail').textContent=JSON.stringify({id:rows[n].id,n,原始六角坐标:rows[n].coord,原始cube:[...rows[n].coord,-rows[n].coord[0]-rows[n].coord[1]],质因数指数:fact(n),相位格:phi[n],相位模数:M,观察取整格:cell,同格身份总数:ids.length,同格前二十个:ids.slice(0,20),倍乘轨迹:trace(),Q16余数:n*2731%65536},null,2);}
function drawHistogram(values){const c=$('hist'),r=c.getBoundingClientRect(),d=devicePixelRatio||1;c.width=r.width*d;c.height=72*d;const g=c.getContext('2d');g.scale(d,d);const m=Math.max(...values);g.fillStyle='#5ce0bf';values.forEach((v,i)=>g.fillRect(i*r.width/64,70-v/m*62,Math.max(.5,r.width/64-1),v/m*62));}
function rgb(n){if(S.color==='mod3')return ['#5ce0bf','#ffbc80','#b09bef'][n%3];if(S.color==='prime')return rows[n].fields.prime?'#5ce0bf':'#526274';let v=S.color==='q16'?n*2731%65536/65535:S.color==='load'?groups.get(cells[n].join(',')).length/report.max_cell_load:n/Math.max(1,S.limit);return `hsl(${210-165*v} 65% ${34+v*34}%)`;}
function schedule(){if(!frame)frame=requestAnimationFrame(()=>{frame=0;draw();});}
let transform=()=>[0,0];
function draw(){
 const rect=canvas.getBoundingClientRect(),d=devicePixelRatio||1;canvas.width=Math.max(1,Math.round(rect.width*d));canvas.height=Math.max(1,Math.round(rect.height*d));ctx.setTransform(d,0,0,d,0,0);const W=rect.width,H=rect.height;ctx.fillStyle='#0d1723';ctx.fillRect(0,0,W,H);
 const center=bounds.min.map((x,j)=>(x+bounds.max[j])/2),extent=Math.max(...bounds.max.map((x,j)=>x-bounds.min[j]),1),unit=Math.min(W,H)*.73/extent*S.zoom;
 const cy=Math.cos(S.yaw),sy=Math.sin(S.yaw),cp=Math.cos(S.pitch),sp=Math.sin(S.pitch);
 transform=p=>{const x=p[0]-center[0],y=p[1]-center[1],z=p[2]-center[2],a=x*cy-y*sy,b=x*sy+y*cy;return [W/2+a*unit,H/2-(b*cp-z*sp)*unit];};
 screens=[];drawn=0;
 for(let n=0;n<points.length;n++){const p=transform(points[n]);screens.push(p);ctx.fillStyle=rgb(n);if((S.layout==='legacy'||S.quantized)&&!S.stack&&Math.abs(S.pitch)<1e-8&&unit>1.5){ctx.beginPath();for(let j=0;j<6;j++){let a=(30+60*j)*Math.PI/180+S.yaw;const x=p[0]+unit/SQ*Math.cos(a),y=p[1]-unit/SQ*Math.sin(a);j?ctx.lineTo(x,y):ctx.moveTo(x,y);}ctx.closePath();ctx.fill();}else{ctx.fillRect(p[0]-.85,p[1]-.85,1.7,1.7);}drawn++;}
 const axislen=extent*.22,origin=transform([0,0,0]);ctx.lineWidth=1;ctx.strokeStyle='#7b9db177';ctx.fillStyle='#b8cbd8';ctx.font='10px system-ui';
 for(let j=0;j<6;j++){const a=j*Math.PI/3,p=transform([axislen*Math.cos(a),axislen*Math.sin(a),0]);ctx.beginPath();ctx.moveTo(...origin);ctx.lineTo(...p);ctx.stroke();ctx.fillText(['+q −s','+r −s','−q +r','−q +s','−r +s','+q −r'][j],p[0]+3,p[1]-3);}
 const path=trace();if(path.length){ctx.lineWidth=1.8;ctx.strokeStyle='#ffffff';ctx.beginPath();path.forEach((n,i)=>i?ctx.lineTo(...screens[n]):ctx.moveTo(...screens[n]));ctx.stroke();for(const n of path){const p=screens[n];ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(p[0],p[1],3,0,Math.PI*2);ctx.fill();ctx.fillText(String(n),p[0]+5,p[1]-6);}}
 $('scene').textContent=(S.layout==='polar'?'候选乘法观察器':'原四进制 A2 编码')+(S.stack?' / 观察分层':' / 平面');$('count').textContent=`入画 ${drawn.toLocaleString()} / 源 ${N.toLocaleString()} · 不抽样`;
}
function sync(){for(const k of ['layout','mode','color'])$(k).value=S[k];for(const k of ['stack','quantized'])$(k).checked=S[k];$('scale').value=S.scale;$('scaleText').textContent=S.scale;$('limit').value=S.limit;$('start').value=S.selected;$('k').value=S.k;$('fingerprint').textContent='原数据 SHA-256：'+P.data_sha256;}
function guarded(f){return ()=>{try{$('err').textContent='';f();}catch(e){$('err').textContent=e.message;}};}
for(const k of ['layout','mode','color'])$(k).addEventListener('change',guarded(()=>configure({[k]:$(k).value})));
for(const k of ['stack','quantized'])$(k).addEventListener('change',guarded(()=>configure({[k]:$(k).checked,pitch:k==='stack'&&$(k).checked?.75:0})));
$('scale').addEventListener('change',guarded(()=>configure({scale:+$('scale').value})));
$('applyPhase').onclick=guarded(()=>configure({overrides:{...S.overrides,[$('prime').value]:+$('tick').value}}));
$('resetPhase').onclick=()=>configure({overrides:{}});
$('trace').onclick=guarded(()=>configure({selected:+$('start').value,k:+$('k').value}));
$('prefix').onclick=guarded(()=>{const limit=+$('limit').value;configure({limit,selected:Math.min(S.selected,limit)});});
$('all').onclick=()=>configure({limit:N-1});
$('fit').onclick=()=>{S.zoom=1;S.yaw=0;S.pitch=S.stack?.75:0;schedule();};
$('zin').onclick=()=>{S.zoom=Math.min(40,S.zoom*1.4);schedule();};$('zout').onclick=()=>{S.zoom=Math.max(.15,S.zoom/1.4);schedule();};
$('turn').onclick=()=>{S.yaw=mod(S.yaw+Math.PI/3,2*Math.PI);schedule();};$('top').onclick=()=>{S.pitch=0;schedule();};$('oblique').onclick=()=>{S.pitch=.85;schedule();};
$('next').onclick=()=>{const a=groups.get(cells[S.selected].join(','));S.selected=a[(a.indexOf(S.selected)+1)%a.length];$('start').value=S.selected;detail();schedule();};
canvas.addEventListener('wheel',e=>{e.preventDefault();S.zoom=Math.max(.15,Math.min(40,S.zoom*Math.exp(-e.deltaY*.001)));schedule();},{passive:false});
canvas.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,startX:e.clientX,startY:e.clientY};canvas.setPointerCapture(e.pointerId);});
canvas.addEventListener('pointermove',e=>{if(!drag)return;S.yaw=mod(S.yaw+(e.clientX-drag.x)*.007,Math.PI*2);S.pitch=Math.max(-1.55,Math.min(1.55,S.pitch+(e.clientY-drag.y)*.007));drag.x=e.clientX;drag.y=e.clientY;schedule();});
canvas.addEventListener('pointerup',e=>{if(!drag)return;const click=Math.hypot(e.clientX-drag.startX,e.clientY-drag.startY)<4;drag=null;if(click){const rect=canvas.getBoundingClientRect(),x=e.clientX-rect.left,y=e.clientY-rect.top;let best=-1,d=100;for(let n=0;n<screens.length;n++){const z=(screens[n][0]-x)**2+(screens[n][1]-y)**2;if(z<d){d=z;best=n;}}if(best>=0){S.selected=best;$('start').value=best;detail();schedule();}}});
canvas.addEventListener('pointercancel',()=>{drag=null;});
function download(body,name,type){const blob=body instanceof Blob?body:new Blob([body],{type}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),3000);}
function snapshot(){return {schema:'NOLLM_MULTIPLICATION_SESSION_V1',lab_version:P.lab_version,data_sha256:P.data_sha256,state:copy(S)};}
function restore(x){if(!x||x.schema!=='NOLLM_MULTIPLICATION_SESSION_V1'||x.lab_version!==P.lab_version||x.data_sha256!==P.data_sha256)throw Error('配置版本或数据指纹不匹配');validateState(x.state);configure(x.state);}
function currentReport(){return {...copy(report),state:copy(S),prime_phase_table:copy(table),phase_modulus:M,drawn,quantization_is_floating:true};}
function exportHTML(){const clone=document.documentElement.cloneNode(true);clone.querySelector('#initial').textContent=JSON.stringify(snapshot()).replace(/</g,'\\u003c');return '<!doctype html>\n'+clone.outerHTML;}
$('session').onclick=()=>download(JSON.stringify(snapshot(),null,2),'number-field-session.json','application/json');
$('report').onclick=()=>download(JSON.stringify(currentReport(),null,2),'number-field-report.json','application/json');
$('source').onclick=()=>download(JSON.stringify(P.data),'number-field-source-v2.json','application/json');
$('saveHtml').onclick=()=>download(exportHTML(),'number-field-saved.html','text/html');
$('png').onclick=()=>canvas.toBlob(b=>{if(b)download(b,'number-field.png','image/png');else $('err').textContent='浏览器未能生成 PNG';});
$('file').onchange=async()=>{try{const f=$('file').files[0];if(!f)return;restore(JSON.parse(await f.text()));$('err').textContent='';}catch(e){$('err').textContent=e.message;}};
window.addEventListener('resize',()=>{schedule();drawHistogram(report.angular_counts);});
window.NumberFieldLab={configure,status:()=>({...copy(report),state:copy(S),drawn}),inspect:n=>({n,id:rows[n].id,coord:rows[n].coord.slice(),phase:phi[n],factors:fact(n),cell:cells[n]?.slice()}),report:currentReport,phase:n=>phi[n],point:n=>screens[n]?.slice(),rawData:()=>copy(P.data),snapshot,restore,exportHTML};
function preset(name){const opts={legacy:{layout:'legacy'},golden:{},zero:{mode:'zero'},layers:{stack:true,pitch:.85}};if(!(name in opts))name='golden';configure({...copy(DEFAULT),...opts[name]});}
window.NumberFieldLab.preset=preset;
window.addEventListener('hashchange',()=>preset(location.hash.slice(1)));
const initial=JSON.parse($('initial').textContent);if(initial)restore(initial);else preset(location.hash.slice(1));
</script></body></html>'''
