'use strict';
// EC48 exact finite positive-source BRC face compatibility certificate. Node/V8-compatible.
// Independent research script; no native X6 update or Guard invocation.
function check(t,msg){if(!t)throw Error(msg||'assert');}
const gcd=(a,b)=>b===0n?a:gcd(b,a%b);
const key=(a,b)=>{const g=gcd(a,b);return (a/g)+'/'+(b/g);};
function model(P0,Q0){
 const H=P0.length,Y=P0[0].length,p0=P0.flat().map(BigInt),q0=Q0.flat().map(BigInt);
 check(p0.every(x=>x>0n)&&q0.every(x=>x>0n),'positive source');
 const pt=p0.reduce((a,b)=>a+b,0n),qt=q0.reduce((a,b)=>a+b,0n);
 return {H,Y,p:p0.map(x=>x*qt),q:q0.map(x=>x*pt),M:pt*qt};
}
function face(a,K,ra,rb){
 const {H,Y,p,q}=a, sg=p.map((v,i)=>v*rb===q[i]*ra?0:v*rb>q[i]*ra?1:-1);
 const qplus=q.reduce((s,x,i)=>s+(sg[i]===1?x:0n),0n),qzero=q.reduce((s,x,i)=>s+(sg[i]===0?x:0n),0n);
 const cols=[];
 for(let z=0;z<K**H;z++){
  let v=z;const c=[];for(let h=0;h<H;h++){c.push(v%K);v=Math.floor(v/K);}
  const pos=Array.from({length:K},()=>Array(Y).fill(false));
  const neg=Array.from({length:K},()=>Array(Y).fill(false));
  const neu=Array.from({length:K},()=>Array(Y).fill(0n));
  for(let h=0;h<H;h++)for(let y=0;y<Y;y++){
   const i=h*Y+y,m=c[h];
   if(sg[i]>0)pos[m][y]=true;else if(sg[i]<0)neg[m][y]=true;else neu[m][y]+=q[i];
  }
  if(pos.some((r,m)=>r.some((x,y)=>x&&neg[m][y])))continue;
  let lo=0n,hi=0n;
  for(let m=0;m<K;m++)for(let y=0;y<Y;y++){if(pos[m][y])lo+=neu[m][y];if(!neg[m][y])hi+=neu[m][y];}
  cols.push({c,pos,neg,lo,hi});
 }
 const par=cols.map((_,i)=>i),find=i=>{while(par[i]!==i)i=par[i];return i;};
 let edges=0;
 for(let i=0;i<cols.length;i++)for(let j=i+1;j<cols.length;j++){
  const a=cols[i],b=cols[j];let ok=true;
  for(let m=0;m<K;m++)for(let y=0;y<Y;y++)if(a.pos[m][y]&&b.neg[m][y]||a.neg[m][y]&&b.pos[m][y])ok=false;
  if(ok){edges++;par[find(j)]=find(i);}
 }
 const mp=new Map();
 cols.forEach((c,i)=>{const k=find(i),old=mp.get(k);
  if(!old)mp.set(k,[c.lo,c.hi]);
  else{if(c.lo<old[0])old[0]=c.lo;if(c.hi>old[1])old[1]=c.hi;}
 });
 const components=[...mp.values()].sort((a,b)=>a[0]<b[0]?-1:a[0]>b[0]?1:0),merged=[];
 for(const [lo,hi] of components){
  if(!merged.length||lo>merged.at(-1)[1])merged.push([lo,hi]);
  else if(hi>merged.at(-1)[1])merged.at(-1)[1]=hi;
 }
 return {ratio:key(ra,rb),qplus:String(qplus),qzero:String(qzero),
  proper:cols.length,edges,components:components.map(x=>x.map(String)),merged:merged.map(x=>x.map(String)),
  whole:merged.length===1&&merged[0][0]===0n&&merged[0][1]===qzero,
  both:merged.length>0&&merged[0][0]===0n&&merged.at(-1)[1]===qzero};
}
function analyze(P,Q,K){
 const a=model(P,Q),v=new Map();
 a.p.forEach((x,i)=>v.set(key(x,a.q[i]),[x/gcd(x,a.q[i]),a.q[i]/gcd(x,a.q[i])]));
 const r=[...v.values()].sort((x,y)=>x[0]*y[1]<y[0]*x[1]?-1:1);
 const faces=r.map(x=>face(a,K,x[0],x[1]));
 return {faces,region:faces.every(f=>f.whole),vertices:faces.every(f=>f.both)};
}
function verify(){
 const P=[[4,2,2],[4,4,4],[4,1,1]],Q=[[1,1,1],[1,1,1],[1,1,1]];
 const w=analyze(P,Q,2),f=w.faces.find(t=>t.ratio==='9/13');
 check(f&&f.qzero==='52'&&f.whole&&f.merged[0][0]==='0'&&f.merged[0][1]==='52','witness exposed face');
 for(let t=0;t<=8;t++){const alpha=180*8+36*t,beta=130*8+52*t;check(13*alpha-9*beta===5*234*8,'fractional face identity');}
 let seed=19880402;const rnd=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed;};
 let models=0,faces=0,nonempty=0,fullMemory=0,oneMemory=0;
 for(let H=2;H<=4;H++)for(let Y=2;Y<=3;Y++)for(let z=0;z<48;z++){
  const A=Array.from({length:H},()=>Array.from({length:Y},()=>1+rnd()%6));
  const B=Array.from({length:H},()=>Array.from({length:Y},()=>1+rnd()%6));
  for(let K=1;K<=Math.min(H,3);K++){
   const res=analyze(A,B,K);models++;faces+=res.faces.length;
   for(const f of res.faces){if(!f.merged.length){check(!f.whole&&!f.both);continue;}nonempty++;
    const ints=f.merged.map(x=>x.map(BigInt));
    check(ints[0][0]>=0n&&ints.at(-1)[1]<=BigInt(f.qzero),'bounds');
    for(let i=1;i<ints.length;i++)check(ints[i][0]>ints[i-1][1],'merged disjoint');
    if(f.whole)check(f.both,'whole entails endpoints');
   }
   if(K===H){check(res.region,'full-memory preservation');fullMemory++;}
   if(K===1){
    const a=model(A,B);let collinear=true;
    for(let y=0;y<Y;y++)for(let h=1;h<H;h++)
     if(a.p[h*Y+y]*a.q[y]!==a.p[y]*a.q[h*Y+y])collinear=false;
    check(collinear===res.region,'single-memory EC47 base case');oneMemory++;
   }
  }
 }
 return {schema:'EM_R4_EC48_EXACT_FACE_COMPAT_GRAPH_V1',all_checks:'PASS',
  arithmetic:'exact BigInt products and integer intervals',models,faces,nonempty,
  fullMemory,oneMemory,witness:{P,Q,K:2,denominator:'234',lambda:'9/13',
  neutral_q:'52',deterministic_neutral_mass:['0','52'],
  stochastic_neutral_mass:'52*t, 0<=t<=1',face_intervals:f.merged,
  compatibility_components:f.components.length},
  theorem_strength:'Universal result proved in note; samples corroborate implementation only',
  native_guard:'UNAVAILABLE_CONTROL_QUOTA',native_X6:'NOT_EXECUTED'};
}
if(typeof process!=='undefined'&&process.argv[1]&&/EC48_verify\.js$/.test(process.argv[1]))
 process.stdout.write(JSON.stringify(verify(),null,2)+'\n');
