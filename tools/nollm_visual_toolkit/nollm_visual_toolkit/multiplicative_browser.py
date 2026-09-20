"""Render-time migration of the pinned multiplicative UI using existing exact engines.

No new numeric family. Original template stays unchanged; anchors fail closed.
"""
from __future__ import annotations

SCRIPT = r'''
// M09: existing multiplicative consumer adapter, not another arithmetic kernel.
const MulExact = (() => {
  'use strict';
  const copy=x=>JSON.parse(JSON.stringify(x));
  const defaults=()=>({engine:'legacy-float',scale:'1',initialBits:64,maxBits:192});
  function source(text) {
    if(typeof text!=='string'||!text.length||text.length>256||/[^0-9./]/.test(text))throw Error('精确尺度必须是至多256字符的原始文本');
    let n,d,syntax;
    if(/^[1-9][0-9]*$/.test(text)){n=BigInt(text);d=1n;syntax='INTEGER';}
    else if(/^[1-9][0-9]*\/[1-9][0-9]*$/.test(text)){[n,d]=text.split('/').map(BigInt);syntax='FRACTION';}
    else if(/^(0|[1-9][0-9]*)\.[0-9]+$/.test(text)){const [w,f]=text.split('.');d=10n**BigInt(f.length);n=BigInt(w)*d+BigInt(f);syntax='DECIMAL';}
    else throw Error('精确尺度仅接受正整数、n/d、普通十进制文本');
    if(n<=0n)throw Error('精确尺度必须为正');
    return {text,syntax,numerator:String(n),denominator:String(d),unreduced:true};
  }
  function options(value=defaults()) {
    if(!value||Array.isArray(value)||Object.keys(value).sort().join(',')!=='engine,initialBits,maxBits,scale')throw Error('精确观察选项结构无效');
    if(!['legacy-float','certified'].includes(value.engine))throw Error('未知归格引擎');
    const s=source(value.scale),n=BigInt(s.numerator),d=BigInt(s.denominator);
    // Explicit browser-observer range, compared in integers. CLI source is broader.
    if(4n*n<d||n>4n*d)throw Error('网页精确归格尺度范围为1/4至4');
    if(!Number.isSafeInteger(value.initialBits)||!Number.isSafeInteger(value.maxBits)||value.initialBits<8||value.maxBits>512||value.initialBits>value.maxBits)throw Error('精度要求8≤初始位数≤最大位数≤512');
    return copy(value);
  }
  function safeInt(s) {
    const n=BigInt(s);if(n< -9007199254740991n||n>9007199254740991n)throw Error('格点超出网页安全整数载体');
    return Number(n); // Checked integer transport; never a numerical decision.
  }
  async function build(config,opts,hooks={}) {
    opts=options(opts);
    if(opts.engine!=='certified')return MulMath.build(config);
    const s=source(opts.scale),f=MulMath.build(config,true);
    const population=await NollmCertifiedHex.populationLexicographic(
      f.records.map(r=>r.phase),s.numerator,s.denominator,
      {initialBits:opts.initialBits,maxBits:opts.maxBits,includeCertificates:true,
       cancelled:hooks.cancelled,yieldControl:hooks.yieldControl});
    f.records.forEach((r,i)=>{const c=population.certificates[i];r.coord=c.cell===null?null:c.cell.map(safeInt);r.cell_status=c.status;});
    f.cell_engine='CERTIFIED_INTEGER_RESIDUAL';f.cell_scale_source=s;f.cell_membership_exact=population;
    return f;
  }
  const exact=f=>f?.cell_engine==='CERTIFIED_INTEGER_RESIDUAL';
  function summary(f){if(!exact(f))return null;const {certificates,...rest}=f.cell_membership_exact;return copy(rest);}
  function stats(f) {
    if(!exact(f))return MulMath.stats(f);
    const total=f.records.length,p=total-1,grid=Array.from({length:8},()=>Array(32).fill(0)),fibers=new Map();
    for(const r of f.records){
      if(r.coord!==null){const k=r.coord.join(',');if(!fibers.has(k))fibers.set(k,[]);fibers.get(k).push(r.n);}
      if(r.n){const band=Number(NollmAngularExact.evaluateDivision(BigInt(r.n-1)*8n,BigInt(p)).quotient);grid[band][NollmAngularExact.phaseBin(r.phase,MulMath.M,32)]++;}
    }
    const pop=f.cell_membership_exact,n=x=>x===null?null:safeInt(x);
    return {population:total,positive_population:p,prime_count:Object.keys(f.prime_phase).length,
      rings:8,sectors:32,grid,distinct_phases:new Set(f.records.slice(1).map(r=>r.phase)).size,
      angular_cv:null,area_sector_cv:null,iid_cv_scale:null,
      angular_cv_squared_exact:NollmAngularExact.fromCounts(Array.from({length:32},(_,j)=>grid.reduce((s,r)=>s+r[j],0)),'1000000'),
      area_sector_cv_squared_exact:NollmAngularExact.fromCounts(grid.flat(),'1000000'),
      approximate_metrics_role:'OMITTED_FROM_EXACT_OBSERVER',
      occupied_hex_centers:n(pop.occupied_cells),occupied_hex_centers_bounds:pop.occupied_cells_bounds.map(safeInt),
      collision_groups:n(pop.collision_groups),extra_identities_at_shared_centers:n(pop.excess_identities_if_collapsed),largest_fiber:n(pop.max_cell_load),
      unresolved_cell_identities:pop.unresolved_identities.slice(),max_display_quantization_error:null,fibers};
  }
  function multiply(f,a,b) {
    if(!exact(f))return MulMath.multiply(f,a,b);
    if(![a,b].every(x=>Number.isSafeInteger(x)&&x>=0&&x<f.records.length))throw Error('因子须为范围内整数');
    const n=a*b;if(n>=f.records.length)return {a,b,product:n,in_range:false};
    const [A,B,Z]=[f.records[a],f.records[b],f.records[n]];
    return {a,b,product:n,in_range:true,phase_defect:n?((Z.phase-A.phase-B.phase)%MulMath.M+MulMath.M)%MulMath.M:null,
      omega_defect:n?Z.omega-A.omega-B.omega:null,ideal_relative_error:null,rounded_relative_error:null,
      approximate_metrics_role:'OMITTED_FROM_EXACT_OBSERVER',zero_phase:n?null:'undefined; multiplication by zero is handled separately'};
  }
  function hexData(f) {
    if(!exact(f))return copy(MulMath.hexData(f));
    if(f.records.some(r=>r.coord===null))throw Error('存在未判定格点，禁止导出完整hex数据');
    const d=MulMath.hexData(f);Object.assign(d.metadata,{cell_engine:f.cell_engine,cell_scale_source:copy(f.cell_scale_source),
      cell_membership_exact:summary(f),rounding:'certified integer-residual A2 cell; approximate ideal pixels are separate'});
    return copy(d);
  }
  function midpoint(f,n) {
    const bounds=f.cell_membership_exact.certificates[n].base_certificate.coordinate_bounds;
    const mid=b=>Number(BigInt(b.lower_numerator)+BigInt(b.upper_numerator))/(2*Number(BigInt(b.denominator)));
    const q=mid(bounds[0]),r=mid(bounds[1]);return [q+r/2,Math.sqrt(3)*r/2]; // Display only; cannot select a cell.
  }
  return Object.freeze({defaults,source,options,build,stats,multiply,hexData,summary,exact,copy,midpoint});
})();
'''

UI_SCRIPT = r'''
 let desiredConfig=seed.config,cellOptions=MulExact.defaults(),computeState='LOADING',generation=0,ready=Promise.resolve();
 const dependent=['session','report','json','png','snapshot','find','next','trace','multiply','setPhase','resetPhases','prime'];
 function requireReady(){if(computeState!=='READY'||!F)throw Error('当前计算尚无可读取结果：'+computeState);return F;}
 function setBusy(busy){for(const id of dependent)$(id).disabled=busy;}
 function controls(){return MulExact.options({engine:$('cellEngine').value,scale:$('cellScale').value,initialBits:number('cellBits'),maxBits:number('cellMaxBits')});}
 function syncCells(){ $('cellEngine').value=cellOptions.engine;$('cellScale').value=cellOptions.scale;$('cellBits').value=cellOptions.initialBits;$('cellMaxBits').value=cellOptions.maxBits; }
 function emptyView(){F=null;stats=null;screen=[];visible=[];drawn=0;pair=null;path=[];ctx.clearRect(0,0,cv.width,cv.height);$('heat').getContext('2d').clearRect(0,0,$('heat').width,$('heat').height);$('label').textContent='计算未完成';$('cv').textContent='—';$('collision').textContent='—';$('detail').textContent='尚无当前格点';$('product').textContent='计算未完成';$('densityInfo').textContent='完整统计暂不可用';$('cellReadout').textContent='';$('drawCount').textContent='尚无当前画面';}
 function rebuild(c,o=cellOptions){
   const config=MulMath.cfg(c),opts=MulExact.options(o); // Validate before invalidating valid state.
   $('error').textContent='';const token=++generation;desiredConfig=config;cellOptions=opts;computeState='COMPUTING';emptyView();setBusy(true);syncCells();$('cellStatus').textContent='计算中，不显示旧格点';
   ready=(async()=>{try{
     const next=opts.engine==='certified'?await MulExact.build(config,opts,{cancelled:()=>token!==generation,yieldControl:()=>new Promise(r=>setTimeout(r,0))}):MulMath.build(config);
     if(token!==generation)return null;
     const st=MulExact.stats(next);F=next;stats=st;selected=Math.min(selected??3,F.records.length-1);computeState='READY';setBusy(false);
     sync();syncCells();updateStats();product();detail();request();return token;
   }catch(e){if(token!==generation)return null;computeState='FAILED';emptyView();setBusy(true);$('cellStatus').textContent='计算失败；没有浮点回退';fail(e);throw e;}})();
   ready.catch(()=>{});return ready;
 }
 function exactStatus(){return !F?computeState:(MulExact.exact(F)?F.cell_membership_exact.status:'LEGACY_FLOAT');}
 function reportRecord(){
   requireReady();const {fibers,...s}=stats;
   const record={schema:'NOLLM_MULTIPLICATIVE_REPORT_V1',lab_version:'0.1.0',config:F.config,statistics:s,pair,scope:'browser whole-population counts; pair test only; not an all-pairs certificate'};
   if(MulExact.exact(F))Object.assign(record,{schema:'NOLLM_MULTIPLICATIVE_REPORT_V2',cell_engine:F.cell_engine,cell_scale_source:F.cell_scale_source,
     cell_membership_exact:MulExact.summary(F),cell_options:cellOptions,pixel_rendering_is_approximate:true,geometry:'DECLARED_A2_OBSERVER_NOT_NATIVE_X6'});
   return MulExact.copy(record);
 }
 function updateStats(){
   if(!MulExact.exact(F)){updateStatsLegacy();$('cvLabel').textContent='等面积扇区 CV（近似显示）';$('cellStatus').textContent='旧浮点归格';$('cellReadout').textContent='';return;}
   const p=F.cell_membership_exact,r=stats.area_sector_cv_squared_exact.readout;
   $('cvLabel').textContent='等面积扇区 CV²（整数＋残差）';$('cv').textContent=r.integer+' / '+r.scale;
   $('cellReadout').textContent='+ '+r.residual_numerator+' / '+r.residual_denominator;
   $('collision').textContent=stats.collision_groups===null?'未判定':stats.collision_groups.toLocaleString();
   $('cellStatus').textContent=p.status==='CERTIFIED_ALL'?'全部确定归格；精确轴向字典序平局':'未判定 '+p.unresolved_identities.length+' 个身份；不猜测格点';
   $('densityInfo').textContent='占用格上下界 '+p.occupied_cells_bounds.join('—')+'；归格尺度 '+cellOptions.scale+'；显示尺度 '+F.config.scale+'。完整统计不包含未判定猜值。';
   const h=$('heat').getContext('2d'),maximum=Math.max(...stats.grid.flat());for(let i=0;i<8;i++)for(let j=0;j<32;j++){const a=stats.grid[i][j]/(maximum||1);h.fillStyle=`hsl(${168-22*a} 37% ${96-66*a}%)`;h.fillRect(j*16,i*16,16,16);}
 }
 function detail(){
   if(!F||selected===null)return;
   if(!MulExact.exact(F)){detailLegacy();return;}
   const r=F.records[selected],c=r.coord,ids=c===null?null:stats.fibers.get(c.join(','));
   $('detail').textContent=JSON.stringify({n:r.n,phase:r.phase,phase_modulus:MulMath.M,omega:r.omega,cell_status:r.cell_status,
     hex_qrs:c===null?null:[...c,-c[0]-c[1]],same_center_count:ids===null?null:ids.length,same_center_first_ids:ids===null?null:ids.slice(0,24),
     cell_scale_source:F.cell_scale_source,ideal_display_only:r.ideal},null,2);$('query').value=r.n;$('next').disabled=c===null;
 }
 function session(){requireReady();const s={schema:'NOLLM_MULTIPLICATIVE_SESSION_V1',lab_version:'0.1.0',config:F.config,view_state:state()};
   if(MulExact.exact(F)){s.schema='NOLLM_MULTIPLICATIVE_SESSION_V2';s.cell_options=cellOptions;}return MulExact.copy(s);}
'''

def prepare_template(template: str) -> str:
    """Adapt the unchanged, pinned old template. Fail rather than patch unknown UI."""
    import hashlib
    from .angular_dispersion_browser import SCRIPT as angular
    from .certified_hex_browser import SCRIPT as certified
    data = template.encode('utf-8')
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if blob != '6619c5da7ad03f38766bfc383d60b5505cb863e0':
        raise ValueError('multiplicative template changed; review M09 anchors before adapting')
    def once(old: str, new: str) -> None:
        nonlocal template
        if template.count(old) != 1:
            raise ValueError('M09 template anchor mismatch: ' + old[:80])
        template = template.replace(old, new, 1)
    def line(prefix: str, new: str) -> None:
        lines = [s for s in template.splitlines() if s.startswith(prefix)]
        if len(lines) != 1:
            raise ValueError('M09 line anchor mismatch: ' + prefix)
        once(lines[0], new)
    once('function build(c){', 'function build(c,skipCells=false){')
    once('coord:round(x,y)', 'coord:skipCells?null:round(x,y)')
    once('</script>\n<script>\n(()=>', '</script>\n<script id="mul-exact-engine">\n' + angular + certified + SCRIPT + '\n</script>\n<script>\n(()=>')
    once('到六角中心的误差</option>', '误差（仅旧浮点对照）</option>')
    once('<label>尺度 C<input', '<label>显示尺度 C<input')
    once('<button id="apply"', '<label>归格引擎<select id="cellEngine"><option value="legacy-float">旧浮点（对照）</option><option value="certified">整数＋残差（精确）</option></select></label>'
         '<label>精确归格尺度（原始文本，1/4—4）<input id="cellScale" type="text" value="1" maxlength="256"></label>'
         '<div class="row"><label>初始位数<input id="cellBits" type="number" value="64" min="8" max="512"></label><label>最大位数<input id="cellMaxBits" type="number" value="192" min="8" max="512"></label></div>'
         '<p id="cellStatus" role="status" aria-live="polite"></p><button id="apply"')
    once('<div class="hint">等面积扇区 CV</div>', '<div class="hint" id="cvLabel">等面积扇区 CV</div>')
    once('<canvas id="heat"', '<p id="cellReadout" class="hint"></p><canvas id="heat"')
    once(" const fail=e=>", UI_SCRIPT + "\n const fail=e=>")
    line(' function rebuild(c){', '')
    once(" function updateStats(){$('cv')", " function updateStatsLegacy(){$('cv')")
    # The inserted implementation also has this name: rename only the original one-line version.
    once(' function detail(){if(selected===null)', ' function detailLegacy(){if(selected===null)')
    line(' function session(){return', '')
    once("function world(r){let [x,y]=r.ideal;if(view==='hex'){", "function world(r){let [x,y]=r.ideal;if(view==='hex'&&r.coord===null){[x,y]=MulExact.midpoint(F,r.n);}else if(view==='hex'){")
    once(' function draw(){const box=', " function draw(){if(!F){ctx.clearRect(0,0,cv.width,cv.height);return;}const box=")
    once("if(view==='hex')cell(r,p);", "if(view==='hex'&&r.coord!==null)cell(r,p);")
    once(" function hue(r){let h=", " function hue(r){if(MulExact.exact(F)&&(r.coord===null||color==='loss'))return '#8a6a42';let h=")
    once(" function drawPair(){if(!pair?.in_range)", " function drawPair(){if(MulExact.exact(F)||!pair?.in_range)")
    # Fit exact hex display to its declared exact scale; no such conversion feeds arithmetic.
    once("const R=Math.sqrt(F.records.length)*F.config.scale,Z=", "const R=Math.sqrt(F.records.length)*(MulExact.exact(F)&&view==='hex'?Number(F.cell_scale_source.numerator)/Number(F.cell_scale_source.denominator):F.config.scale),Z=")
    once('pair=MulMath.multiply(F,', 'pair=MulExact.multiply(F,')
    once('pair.ideal_relative_error.toExponential(3)', "(pair.ideal_relative_error===null?'精确模式省略':pair.ideal_relative_error.toExponential(3))")
    once('pair.rounded_relative_error.toExponential(3)', "(pair.rounded_relative_error===null?'精确模式省略':pair.rounded_relative_error.toExponential(3))")
    # Preserve existing view-state checks, then await and suppress stale restore completion.
    once(' function restore(s){', ' async function restore(s){s=MulExact.copy(s);')
    once("s.schema!=='NOLLM_MULTIPLICATIVE_SESSION_V1'", "!['NOLLM_MULTIPLICATIVE_SESSION_V1','NOLLM_MULTIPLICATIVE_SESSION_V2'].includes(s.schema)")
    once("const c=MulMath.cfg(s.config),v=s.view_state;", "const isV2=s.schema==='NOLLM_MULTIPLICATIVE_SESSION_V2';if(Object.keys(s).sort().join(',')!==(isV2?'cell_options,config,lab_version,schema,view_state':'config,lab_version,schema,view_state'))throw Error('会话结构无效');const opt=isV2?MulExact.options(s.cell_options):MulExact.defaults();const c=MulMath.cfg(s.config),v=s.view_state;")
    once('rebuild(c);view=v.view;', 'const done=await rebuild(c,opt);if(done===null||done!==generation)return null;view=v.view;')
    once(' function snapshot(){const clone=', ' function snapshot(){requireReady();const clone=')
    once(" function run(fn){return()=>{try{$('error').textContent='';fn();}catch(e){fail(e);}};}", " function run(fn){return async()=>{try{$('error').textContent='';await fn();}catch(e){fail(e);}};}")
    # Existing model-changing event handlers use latest requested config during replacement.
    template = template.replace('...F.config', '...desiredConfig')
    once("scale:number('scale')}));", "scale:number('scale')},controls()));")
    once("$('scheme').onchange=run", "$('cellEngine').onchange=run(()=>rebuild(desiredConfig,controls()));$('scheme').onchange=run")
    once("$('next').onclick=()=>{if(selected===null)", "$('next').onclick=()=>{if(!F||selected===null||F.records[selected].coord===null)")
    once("$('prime').onchange=phaseSync", "$('prime').onchange=()=>{if(F)phaseSync();}")
    old_report = "const {fibers,...s}=stats;jsonDownload({schema:'NOLLM_MULTIPLICATIVE_REPORT_V1',lab_version:'0.1.0',config:F.config,statistics:s,pair,scope:'browser whole-population counts; pair test only; not an all-pairs certificate'},'multiplicative-report.json');"
    once(old_report, "jsonDownload(reportRecord(),'multiplicative-report.json');")
    once("jsonDownload(MulMath.hexData(F),", "jsonDownload(MulExact.hexData(requireReady()),")
    once("$('png').onclick=run(()=>cv.toBlob(b=>{if(b)blobDownload(b,'multiplicative-view.png');else fail('PNG 生成失败');}));", "$('png').onclick=run(()=>{requireReady();draw();const token=generation;cv.toBlob(b=>{if(token!==generation||computeState!=='READY')return fail('PNG所属计算已过期');if(b)blobDownload(b,'multiplicative-view.png');else fail('PNG 生成失败');});});")
    once('restore(JSON.parse(await file.text()));', 'await restore(JSON.parse(await file.text()));')
    line(' window.MulLab=', " window.MulLab={build:rebuild,configureCells:o=>rebuild(desiredConfig,{...cellOptions,...o}),get ready(){return ready;},session,restore,snapshot,report:reportRecord,data:()=>MulExact.copy(requireReady()),hexData:()=>MulExact.hexData(requireReady()),stats:()=>{requireReady();const{fibers,...s}=stats;return MulExact.copy(s);},certificate:n=>{requireReady();if(!MulExact.exact(F)||!Number.isSafeInteger(n)||n<0||n>=F.records.length)throw Error('无此精确证书');return MulExact.copy(F.cell_membership_exact.certificates[n]);},status:()=>({state:computeState,cell_status:exactStatus(),count:F?F.records.length:desiredConfig.count,drawn,selected,view,phase_scheme:desiredConfig.scheme,path:path.slice(),pair:MulExact.copy(pair),cell_options:MulExact.copy(cellOptions),occupied_hex_centers:stats?.occupied_hex_centers??null,collision_groups:stats?.collision_groups??null,extra_identities_at_shared_centers:stats?.extra_identities_at_shared_centers??null,largest_fiber:stats?.largest_fiber??null}),projectId:n=>{requireReady();return project(world(F.records[n]));},engine:MulMath,exactEngine:MulExact};")
    line(' try{rebuild(seed.config);', " try{const initial=seed.session?restore(seed.session):rebuild(seed.config);initial.catch(fail);}catch(e){fail(e);}")
    return template
