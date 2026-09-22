"""Offline BigInt port of certified_hex.py at M03 82ffedbf.

Extends the existing angular/BRC browser port. Arithmetic certificates match
Python, including signed floor division, correlated quarter-turn roots and
outward interval rounding. Pixel conversion is outside this module. Native X6
and arbitrary-angle transcendental evaluation are outside its declared scope.
"""

SCRIPT = r'''
// NOLLM_CERTIFIED_HEX_BIGINT_PORT_V1
const NollmCertifiedHex = (() => {
  'use strict';
  const M=65536n, TIE='HALF_TOWARD_POSITIVE_INFINITY_THEN_MAX_ERROR_Q_R_S', LEX_TIE='MINIMUM_EUCLIDEAN_DISTANCE_THEN_AXIAL_LEXICOGRAPHIC';
  const abs=x=>x<0n?-x:x, min=(a,b)=>a<b?a:b, max=(a,b)=>a>b?a:b;
  const sign=x=>x<0n?-1n:x>0n?1n:0n;
  function integer(value, name='integer') {
    if (typeof value==='bigint') return value;
    if (typeof value==='string' && /^(0|-?[1-9][0-9]*)$/.test(value)) return BigInt(value);
    if (typeof value==='number' && Number.isSafeInteger(value) && !Object.is(value,-0)) return BigInt(value);
    throw new TypeError(name+' requires an exact integer or canonical decimal string');
  }
  function positive(value,name) { const v=integer(value,name); if(v<=0n)throw new RangeError(name+' must be positive');return v; }
  function bits(value) {const v=integer(value,'bits');if(v<8n||v>512n)throw new RangeError('bits must be in 8..512');return v;}
  function budget(initial,maxBits) {const a=bits(initial),b=bits(maxBits);if(a>b)throw new RangeError('invalid precision budget');return [a,b];}
  function floor(n,d) {
    const t=NollmAngularExact.evaluateDivision(abs(n),d);
    return n>=0n?t.quotient:t.remainder===0n?-t.quotient:-t.quotient-1n;
  }
  const ceil=(n,d)=>-floor(-n,d);
  // Browser port of core.integer_nth_root(p=2) under the BRC root boundary.
  // The loop is integer bisection, not a floating sqrt seed.
  function rootTrace(value) {
    const n=integer(value,'radicand');if(n<0n)throw new RangeError('negative radicand');
    let lo=0n,hi=1n;
    if(n<2n)lo=n;
    else {while(hi*hi<=n)hi*=2n;while(lo+1n<hi){const mid=(lo+hi)>>1n;if(mid*mid<=n)lo=mid;else hi=mid;}}
    const residual=n-lo*lo;
    if(residual<0n||residual>=2n*lo+1n)throw new Error('root collapse certificate failed');
    return {root_index:lo,polynomial_residual:residual};
  }
  const root=n=>rootTrace(n).root_index;
  class Interval {
    constructor(lo,hi,b) {
      this.lo=integer(lo);this.hi=integer(hi);this.bits=bits(b);this.scale=1n<<this.bits;
      if(this.lo>this.hi)throw new RangeError('inverted interval');Object.freeze(this);
    }
    same(y){if(!(y instanceof Interval)||this.bits!==y.bits)throw new TypeError('interval scales must match');}
    add(y){this.same(y);return new Interval(this.lo+y.lo,this.hi+y.hi,this.bits);}
    neg(){return new Interval(-this.hi,-this.lo,this.bits);}
    sub(y){return this.add(y.neg());}
    mul(y){this.same(y);const p=[this.lo*y.lo,this.lo*y.hi,this.hi*y.lo,this.hi*y.hi];return new Interval(floor(p.reduce(min),this.scale),ceil(p.reduce(max),this.scale),this.bits);}
    ratio(n,d){n=integer(n);d=positive(d,'denominator');const a=this.lo*n,b=this.hi*n;return new Interval(floor(min(a,b),d),ceil(max(a,b),d),this.bits);}
    sqrt(){if(this.lo<0n)throw new RangeError('negative root interval');const l=root(this.lo*this.scale),h=root(this.hi*this.scale);return new Interval(l,h+(h*h<this.hi*this.scale?1n:0n),this.bits);}
    intersect(l,h){return new Interval(max(l,this.lo),min(h,this.hi),this.bits);}
    record(){return {lower_numerator:String(this.lo),upper_numerator:String(this.hi),denominator:String(this.scale),bits:String(this.bits)};}
  }
  function rootRatioBound(n,d,b) {
    n=integer(n);d=positive(d,'radicand denominator');b=bits(b);if(n<0n)throw new RangeError('negative radicand');
    const S=1n<<b,k=root(floor(n*S*S,d)),R=n*S*S-d*k*k;
    if(R<0n||R>=d*(2n*k+1n))throw new Error('root-ratio certificate failed');
    return [new Interval(k,k+(R===0n?0n:1n),b),{kind:'ROOT_RATIO_POLYNOMIAL_RESIDUAL',radicand_numerator:String(n),radicand_denominator:String(d),scale:String(S),root_index:String(k),polynomial_residual:String(R)}];
  }
  function memo(cache,key,make,limit){if(cache.has(key))return cache.get(key);const value=make();if(cache.size>=limit)cache.delete(cache.keys().next().value);cache.set(key,value);return value;}
  const rotations=new Map(),phases=new Map();
  function rotationPowers(b) {return memo(rotations,String(b),()=>{
    const S=1n<<b,one=new Interval(S,S,b),out=[];let c=new Interval(0n,0n,b);
    for(let i=0;i<14;i++){const nc=one.add(c).ratio(1n,2n).sqrt(),ns=one.sub(c).intersect(0n,2n*S).ratio(1n,2n).sqrt();c=nc.intersect(0n,S);out.push(Object.freeze([c,ns.intersect(0n,S)]));}
    return Object.freeze(out.reverse());
  },16);}
  function phaseBounds(tick,b=64) {
    tick=integer(tick,'tick');b=bits(b);if(tick<0n||tick>=M)throw new RangeError('phase tick out of range');
    return memo(phases,String(tick)+':'+String(b),()=>{
      const q=floor(tick,16384n),rest=tick-q*16384n,S=1n<<b;let c=new Interval(S,S,b),s=new Interval(0n,0n,b);
      if(rest){let i=0n;for(const [a,z] of rotationPowers(b)){if(rest&(1n<<i)){[c,s]=[c.mul(a).sub(s.mul(z)),s.mul(a).add(c.mul(z))];}i++;}}
      c=c.intersect(0n,S);s=s.intersect(0n,S);
      return Object.freeze(q===0n?[c,s]:q===1n?[s.neg(),c]:q===2n?[c.neg(),s.neg()]:[s,c.neg()]);
    },8192);
  }
  function roundAxial(q,r,d) {
    q=integer(q);r=integer(r);d=positive(d,'denominator');const src=[q,r,-q-r];
    const a=src.map(n=>floor(2n*n+d,2n*d)),e=a.map((v,i)=>abs(v*d-src[i]));
    const k=e[0]>=e[1]&&e[0]>=e[2]?0:e[1]>=e[2]?1:2;
    a[k]=-a.reduce((sum,v,i)=>i===k?sum:sum+v,0n);
    const residual=src.map((v,i)=>v-a[i]*d),pairs=[[0,1],[0,2],[1,2]];
    if(pairs.some(([i,j])=>abs(residual[i]-residual[j])>d))throw new Error('outside nearest cell');
    return {kind:'RATIONAL_AXIAL_CELL_CERTIFICATE',source_numerators:src.map(String),denominator:String(d),cube_cell:a.map(String),signed_residual_numerators:residual.map(String),corrected_axis:['q','r','s'][k],boundary:pairs.some(([i,j])=>abs(residual[i]-residual[j])===d),tie_rule:TIE};
  }
  function certifyBox(q,r,s) {
    q.same(r);q.same(s);const c=[q,r,s],S=q.scale;
    if(c.reduce((a,v)=>a+v.lo,0n)>0n||c.reduce((a,v)=>a+v.hi,0n)<0n)throw new RangeError('box misses cube plane');
    if(c.every(v=>v.lo===v.hi)) {const cert=roundAxial(q.lo,r.lo,S);return {status:cert.boundary?'CERTIFIED_TIE':'CERTIFIED_INTERIOR',cell:cert.cube_cell.slice(0,2),rounding_certificate:cert,margin_numerators:null};}
    const proposed=roundAxial(q.lo+q.hi,r.lo+r.hi,2n*S),a=proposed.cube_cell.map(BigInt),margins=[];
    for(const [i,j] of [[0,1],[0,2],[1,2]]){const shift=(a[i]-a[j])*S,low=c[i].lo-c[j].hi-shift,high=c[i].hi-c[j].lo-shift;margins.push(S-max(abs(low),abs(high)));}
    return {status:margins.every(v=>v>0n)?'CERTIFIED_INTERIOR':'UNRESOLVED_BOUNDARY',cell:margins.every(v=>v>0n)?a.slice(0,2).map(String):null,margin_numerators:margins.map(String),rounding_certificate:null};
  }
  function linearRootSign(a,b,n,d) {
    if(a===0n||n===0n)return sign(b);if(b===0n)return sign(a);if(sign(a)===sign(b))return sign(a);
    return sign(a)*sign(a*a*n-b*b*d);
  }
  function cardinal(source) {
    const {n:identity,tick,sn,sd}=source;let coeff;
    if(tick===null)coeff=[0n,0n,0n];else if(tick===0n)coeff=[1n,0n,-1n];else if(tick===16384n)coeff=[-1n,2n,-1n];else if(tick===32768n)coeff=[-1n,0n,1n];else if(tick===49152n)coeff=[1n,-2n,1n];else return null;
    const n=identity*sn*sn,d=sd*sd*(tick===16384n||tick===49152n?3n:1n);
    const a=coeff.map(k=>{const whole=root(floor(k*k*n,d)),half=linearRootSign(2n*abs(k),-(2n*whole+1n),n,d);return k>=0n?whole+(half>=0n?1n:0n):-whole-(half>0n?1n:0n);});
    const e=coeff.map((k,i)=>{const o=linearRootSign(-k,a[i],n,d);return [-k*o,a[i]*o];});
    const cmp=(i,j)=>linearRootSign(e[i][0]-e[j][0],e[i][1]-e[j][1],n,d);
    const k=cmp(0,1)>=0n&&cmp(0,2)>=0n?0:cmp(1,2)>=0n?1:2;
    a[k]=-a.reduce((sum,v,i)=>i===k?sum:sum+v,0n);let boundary=false;
    for(const [i,j] of [[0,1],[0,2],[1,2]]){const c=coeff[i]-coeff[j],b=a[j]-a[i],upper=linearRootSign(c,b-1n,n,d),lower=linearRootSign(c,b+1n,n,d);if(upper>0n||lower<0n)throw new Error('radical outside cell');boundary=boundary||upper===0n||lower===0n;}
    const cert={kind:'SHARED_RADICAL_AXIAL_CELL_CERTIFICATE',radicand_numerator:String(n),radicand_denominator:String(d),source_coefficients:coeff.map(String),cube_cell:a.map(String),signed_residuals:coeff.map((k,i)=>({radical_coefficient:String(k),integer_part:String(-a[i])})),corrected_axis:['q','r','s'][k],boundary,tie_rule:TIE,comparison:'SIGN_SEPARATED_INTEGER_SQUARE_COMPARISON'};
    return {status:boundary?'CERTIFIED_TIE':'CERTIFIED_INTERIOR',cell:cert.cube_cell.slice(0,2),rounding_certificate:cert,margin_numerators:null};
  }
  function source(n,tick,sn,sd) {
    n=integer(n,'n');sn=positive(sn,'scale numerator');sd=positive(sd,'scale denominator');
    if(n<0n)throw new RangeError('negative identity');
    if(n===0n){if(tick!==null)throw new TypeError('zero has no phase');}
    else{tick=integer(tick,'tick');if(tick<0n||tick>=M)throw new RangeError('tick outside domain');}
    return {n,tick,sn,sd};
  }
  function sourceRecord(v){return {n:String(v.n),phase_tick:v.tick===null?null:String(v.tick),phase_modulus:String(M),scale_numerator:String(v.sn),scale_denominator:String(v.sd),observer:'DECLARED_POLAR_A2_NOT_NATIVE_X6'};}
  function coordinates(v,b) {
    const [radius,rt]=rootRatioBound(v.n,1n,b),[third,tt]=rootRatioBound(v.n,3n,b),[c,s]=phaseBounds(v.tick===null?0n:v.tick,b);
    const a=radius.mul(c).ratio(v.sn,v.sd),z=third.mul(s).ratio(v.sn,v.sd);
    return [[a.sub(z),z.ratio(2n,1n),a.neg().sub(z)],[rt,tt]];
  }
  function locate(n,tick,sn=1,sd=1,options={}) {
    const v=source(n,tick,sn,sd),[initial,maximum]=budget(options.initialBits??64,options.maxBits??192),history=[];let b=initial;
    for(;;){const [coords,roots]=coordinates(v,b),decision=cardinal(v)||certifyBox(...coords);history.push(String(b));
      if(decision.cell!==null||b===maximum)return {schema:'NOLLM_CERTIFIED_POLAR_CELL_V1',source:sourceRecord(v),...decision,coordinate_bounds:coords.map(x=>x.record()),root_certificates:roots,refinement_bits:history,tie_rule:TIE};
      b=min(2n*b,maximum);
    }
  }
  function lexLess(a,b){return a[0]<b[0]||(a[0]===b[0]&&a[1]<b[1]);}
  function adaptLexicographicCell(base) {
    let cell=base.cell;
    if(base.status==='CERTIFIED_TIE'&&cell!==null){
      const proof=base.rounding_certificate,q0=BigInt(cell[0]),r0=BigInt(cell[1]);
      const keys=new Map();
      for(const [dq,dr] of [[0n,0n],[1n,0n],[-1n,0n],[0n,1n],[0n,-1n],[1n,-1n],[-1n,1n]]){const q=q0+dq,r=r0+dr;keys.set(String(q)+','+String(r),[q,r]);}
      const candidates=[...keys.values()].sort((a,b)=>lexLess(a,b)?-1:lexLess(b,a)?1:0);
      let best=candidates[0];
      if(proof.kind==='RATIONAL_AXIAL_CELL_CERTIFICATE'){
        const [qn,rn]=proof.source_numerators.slice(0,2).map(BigInt),d=BigInt(proof.denominator);
        const dist=([q,r])=>{const dq=qn-q*d,dr=rn-r*d;return dq*dq+dq*dr+dr*dr;};
        let bd=dist(best);for(const c of candidates.slice(1)){const cd=dist(c);if(cd<bd||(cd===bd&&lexLess(c,best))){best=c;bd=cd;}}
      } else if(proof.kind==='SHARED_RADICAL_AXIAL_CELL_CERTIFICATE'){
        const n=BigInt(proof.radicand_numerator),d=BigInt(proof.radicand_denominator),[cq,cr]=proof.source_coefficients.slice(0,2).map(BigInt);
        const bc=([q,r])=>[-2n*cq*q-cq*r-cr*q-2n*cr*r,q*q+q*r+r*r];
        const compare=(a,b)=>{const [aa,ab]=bc(a),[ba,bb]=bc(b);return linearRootSign(aa-ba,ab-bb,n,d);};
        for(const c of candidates.slice(1)){const order=compare(c,best);if(order<0n||(order===0n&&lexLess(c,best)))best=c;}
      } else throw new Error('unsupported exact tie certificate for lexicographic adapter');
      cell=best.map(String);
    }
    return {schema:'NOLLM_MULTIPLICATIVE_CELL_CERTIFICATE_V1',status:base.status,cell,
      tie_rule:LEX_TIE,base_certifier_tie_rule:base.tie_rule,base_certificate:base};
  }
  async function populationLexicographic(phi,sn,sd,options={}) {
    if(options.includeCertificates!==undefined&&typeof options.includeCertificates!=='boolean')throw new TypeError('includeCertificates must be boolean');
    const want=options.includeCertificates??false,onCell=options.onCell;
    const base=await population(phi,sn,sd,{...options,includeCertificates:true,onCell:onCell?((rec,i)=>onCell(adaptLexicographicCell(rec),i)):undefined});
    const certs=base.certificates.map(adaptLexicographicCell),counts=new Map(),unresolved=[],ties=[];
    for(let i=0;i<certs.length;i++){const rec=certs[i];if(rec.cell===null)unresolved.push(String(i));else{const key=rec.cell.join(',');counts.set(key,(counts.get(key)??0n)+1n);if(rec.status==='CERTIFIED_TIE')ties.push(String(i));}}
    const missing=BigInt(unresolved.length),total=BigInt(certs.length),occupied=BigInt(counts.size),complete=missing===0n,loads=[...counts.values()];
    return {schema:'NOLLM_MULTIPLICATIVE_CERTIFIED_A2_POPULATION_V1',status:complete?'CERTIFIED_ALL':'UNRESOLVED_BOUNDARY',
      population:base.population,certified_identities:base.certified_identities,phase_modulus:base.phase_modulus,
      phase_source_sha256:base.phase_source_sha256,phase_source_encoding:base.phase_source_encoding,
      unresolved_identities:unresolved,tie_identities:ties,occupied_cells:complete?String(occupied):null,
      occupied_cells_bounds:[String(occupied),String(occupied+missing)],collision_groups:complete?String(loads.filter(x=>x>1n).length):null,
      excess_identities_if_collapsed:complete?String(total-occupied):null,max_cell_load:complete?String(loads.reduce(max,0n)):null,
      scale:base.scale,precision_counts:base.precision_counts,tie_rule:LEX_TIE,base_certifier_schema:base.schema,
      base_certifier_tie_rule:base.tie_rule,certificates:want?certs:null,
      scope:'CERTIFIED_A2_OBSERVER_ONLY; LEGACY_AXIAL_LEXICOGRAPHIC_TIE; NO_NATIVE_IDENTITY_COLLAPSE'};
  }
  function parseScale(text) {
    // Original lexical source is retained. Never reconstruct a rational from Number.
    if(typeof text!=='string'||text.length>256)throw new TypeError('scale requires decimal or fraction text, at most 256 characters');
    let n,d;
    if(/^[1-9][0-9]*\/[1-9][0-9]*$/.test(text)){const a=text.split('/');n=BigInt(a[0]);d=BigInt(a[1]);}
    else if(/^(0|[1-9][0-9]*)(\.[0-9]+)?$/.test(text)){const a=text.split('.');d=a.length===1?1n:10n**BigInt(a[1].length);n=BigInt(a.join(''));}
    else throw new TypeError('invalid scale text');
    if(n<=0n||2n*n<d||n>3n*d)throw new RangeError('layout scale must be in one-half..three');
    return {text,numerator:String(n),denominator:String(d)};
  }
  function stable(x) {if(x===null||typeof x!=='object')return JSON.stringify(x);if(Array.isArray(x))return '['+x.map(stable).join(',')+']';return '{'+Object.keys(x).sort().map(k=>JSON.stringify(k)+':'+stable(x[k])).join(',')+'}';}
  function verifyCellRecord(record) {
    try {const decimal=x=>{if(typeof x!=='string'||String(integer(x))!==x)throw new TypeError('noncanonical decimal');return x;};
      const s=record.source,h=record.refinement_bits;if(!Array.isArray(h)||h.length===0)return false;
      const actual=locate(decimal(s.n),s.phase_tick===null?null:decimal(s.phase_tick),decimal(s.scale_numerator),decimal(s.scale_denominator),{initialBits:decimal(h[0]),maxBits:decimal(h[h.length-1])});return stable(actual)===stable(record);
    } catch(e) {return false;}
  }
  async function population(phi,sn,sd,options={}) {
    // Validate and snapshot all mathematical inputs before the first await.
    if(!Array.isArray(phi)||phi.length<2||phi.length>65536||phi[0]!==null)throw new TypeError('phase population must start with null, length 2..65536');
    if(options.includeCertificates!==undefined&&typeof options.includeCertificates!=='boolean')throw new TypeError('includeCertificates must be boolean');
    const limits=budget(options.initialBits??64,options.maxBits??192),sources=Array.from(phi,(tick,i)=>source(i,tick,sn,sd));
    const cellCounts=new Map(),unresolved=[],ties=[],certs=[],precision={};
    for(let i=0;i<sources.length;i++) {
      if(options.cancelled?.())throw new Error('CERTIFICATION_CANCELLED');
      const v=sources[i],rec=locate(v.n,v.tick,v.sn,v.sd,{initialBits:limits[0],maxBits:limits[1]}),b=rec.refinement_bits.at(-1);
      precision[b]=(precision[b]??0n)+1n;
      if(rec.cell===null)unresolved.push(String(i));else{const key=rec.cell.join(',');cellCounts.set(key,(cellCounts.get(key)??0n)+1n);if(rec.status==='CERTIFIED_TIE')ties.push(String(i));}
      if(options.includeCertificates)certs.push(rec);
      if(options.onCell)options.onCell(rec,i);
      // Cooperative UI yield, not a numerical or temporal stopping rule.
      if(options.yieldControl&&i%128===127)await options.yieldControl();
    }
    if(options.cancelled?.())throw new Error('CERTIFICATION_CANCELLED');
    if(!globalThis.crypto?.subtle)throw new Error('SHA256_UNAVAILABLE: no unverified digest fallback');
    const bytes=new TextEncoder().encode(JSON.stringify(sources.map(v=>v.tick===null?null:String(v.tick))));
    const digest=await globalThis.crypto.subtle.digest('SHA-256',bytes),sha=Array.from(new Uint8Array(digest),x=>x.toString(16).padStart(2,'0')).join('');
    if(options.cancelled?.())throw new Error('CERTIFICATION_CANCELLED');
    const total=BigInt(sources.length),missing=BigInt(unresolved.length),occupied=BigInt(cellCounts.size),complete=missing===0n;
    const loads=[...cellCounts.values()];
    return {schema:'NOLLM_CERTIFIED_POLAR_POPULATION_V1',status:complete?'CERTIFIED_ALL':'UNRESOLVED_BOUNDARY',population:String(total),certified_identities:String(total-missing),phase_modulus:String(M),phase_source_sha256:sha,phase_source_encoding:'COMPACT_UTF8_JSON_ARRAY_NULL_OR_DECIMAL_STRINGS',unresolved_identities:unresolved,tie_identities:ties,occupied_cells:complete?String(occupied):null,occupied_cells_bounds:[String(occupied),String(occupied+missing)],collision_groups:complete?String(loads.filter(x=>x>1n).length):null,excess_identities_if_collapsed:complete?String(total-occupied):null,max_cell_load:complete?String(loads.reduce(max,0n)):null,scale:{numerator:String(sources[0].sn),denominator:String(sources[0].sd)},precision_counts:Object.fromEntries(Object.entries(precision).map(([k,v])=>[k,String(v)])),tie_rule:TIE,certificates:options.includeCertificates?certs:null,scope:'CERTIFIED_A2_OBSERVER_ONLY; NO_NATIVE_IDENTITY_COLLAPSE'};
  }
  return Object.freeze({Interval,rootRatioBound,phaseBounds,roundAxial,certifyBox,locate,population,parseScale,verifyCellRecord,LEX_TIE,adaptLexicographicCell,populationLexicographic});
})();
'''
