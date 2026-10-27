// PREFIX285: exact source-labelled C4 BRC (Node 20+, BigInt only).
// J_p retains all four ordered source-pair terms. No π, trig or propagator.
'use strict';
const P=[[1n,0n],[0n,1n],[-1n,0n],[0n,-1n]], ZC=[0n,0n];
const C=(x,y=0n)=>[BigInt(x),BigInt(y)];
const add=(a,b)=>[a[0]+b[0],a[1]+b[1]];
const neg=a=>[-a[0],-a[1]];
const mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];
const conj=a=>[a[0],-a[1]];
const sq=a=>a[0]*a[0]+a[1]*a[1];
function gcd(a,b){if(a<0n)a=-a;if(b<0n)b=-b;while(b){[a,b]=[b,a%b]}return a||1n}
function f(n,d=1n){if(d<0n){n=-n;d=-d}if(!d)throw Error('zero denominator');const g=gcd(n,d);return [n/g,d/g]}
const fs=x=>x[1]===1n?String(x[0]):String(x[0])+'/'+String(x[1]);
const diff=(a,b)=>f(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const abs=x=>x<0n?-x:x;
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
const test=(x,msg)=>{if(!x)throw Error(msg)};
function corr(a,r){let v=ZC;for(let j=0;j<3-r;j++)v=add(v,mul(a[j],conj(a[j+r])));return v}
function effect(a,p){const z=a.reduce((s,x)=>s+sq(x),0n),b=[a[0],mul(P[p],a[1])];let sum=ZC;
 for(let j=0;j<2;j++)for(let k=0;k<2;k++)sum=add(sum,mul(b[j],conj(b[k])));
 test(sum[1]===0n,'nonreal pair result');return f(sum[0],2n*z)}
function all(){const groups=new Map();let input=0,brc=0,checks=0;
 for(let x=1n;x<=4n;x++)for(let y=1n;y<=4n;y++)for(let z=1n;z<=4n;z++)for(let u=0;u<4;u++)for(let v=0;v<4;v++){
  const a=[C(x),[y*P[u][0],y*P[u][1]],[z*P[v][0],z*P[v][1]]];
  const norm=a.reduce((s,k)=>s+sq(k),0n),h=corr(a,1),k=corr(a,2),p0=f(sq(a[0]),norm);
  const sig=[fs(f(h[0],norm)),fs(f(h[1],norm)),fs(f(k[0],norm)),fs(f(k[1],norm)),fs(p0)].join(';');
  const rel=[fs(f(a[1][0],x)),fs(f(a[1][1],x)),fs(f(a[2][0],x)),fs(f(a[2][1],x))].join(';');
  const obs=[effect(a,0),effect(a,1)];brc+=2;
  for(let p=0;p<2;p++){
   test(obs[p][0]>=0n&&obs[p][0]<=obs[p][1],'effect outside [0,1]');
   const cross=mul(P[p],mul(a[1],conj(a[0])));
   test(eq(obs[p],f(sq(a[0])+sq(a[1])+2n*cross[0],2n*norm)),'ordered pair analytic mismatch');checks++;
  }
  if(!groups.has(sig))groups.set(sig,new Map());const row=groups.get(sig);
  const diag=a.map(w=>fs(f(sq(w),norm))).join(';');
  if(row.has(rel)){const old=row.get(rel);test(old.diag===diag&&old.obs.every((q,p)=>eq(q,obs[p])),'nonunique normalized record')}
  else row.set(rel,{a,obs,diag,p0});input++;
 }
 let nonsingular=0,singular=0,two=0,maxfiber=0,adaptive=0,diagonal=0;const branches={'1':0,'-1':0,'i':0,'-i':0};
 for(const row of groups.values()){
  const vv=[...row.values()],o=vv[0],a=o.a,t=[a[2][0]/a[0][0],a[2][1]/a[0][0]];
  const isSingular=sq(a[0])===sq(a[2]);if(isSingular)singular++;else nonsingular++;
  maxfiber=Math.max(maxfiber,vv.length);test(vv.length<=2,'fiber larger than 2');
  if(vv.length===2){two++;test(isSingular,'double nonsingular fiber');const b=vv[1],r=a[1],z=a[0][0],rb=b.a[1],zb=b.a[0][0];
   test(rb[0]*z===mul(t,conj(r))[0]*zb&&rb[1]*z===mul(t,conj(r))[1]*zb,'wrong involution');
   test(o.diag===b.diag,'diagonal mass distinguishes partner');diagonal++;
   const p=(t[0]===1n&&t[1]===0n)?1:0;
   const d=diff(o.obs[p],b.obs[p]);test(d[0]!==0n,'adaptive effect failed');
   const qNum=abs(r[0])+abs(r[1]);test(qNum>0n,'zero relative amplitude');
   const gain=(t[1]===0n)?2n:1n;const gap=f(gain*z*qNum,a.reduce((s,k)=>s+sq(k),0n));
   test(eq(f(abs(d[0]),d[1]),gap),'exact gap mismatch');adaptive++;
   const label=t[1]===1n?'i':t[1]===-1n?'-i':t[0]===1n?'1':'-1';branches[label]++;
  }
 }
 function witness(a,b,blind,visible){const o=[effect(a,blind),effect(b,blind)];test(eq(o[0],o[1]),'missing blind pair');const z=[effect(a,visible),effect(b,visible)];test(!eq(z[0],z[1]),'visible pair failed');return {blind_p:blind,blind_value:fs(o[0]),separating_p:visible,separating_values:z.map(fs)}}
 const A=[C(1),C(0,1),C(1)],B=[C(1),C(0,-1),C(1)];
 const R={schema:'PREFIX285_C4_ORDERED_BRC_EXACT_V1',status:'AUTHOR_SIDE_MODEL_CHECK_PASS_NATIVE_DETECTOR_PENDING',
 input_packets:input,direct_ordered_pair_brc_effect_evaluations:brc,analytic_crosschecks:checks,
 signatures:groups.size,nonsingular_signatures:nonsingular,singular_signatures:singular,
 nontrivial_two_partner_fibers:two,max_relative_classes:maxfiber,diagonal_no_go_checks:diagonal,
 adaptive_one_setting_checks:adaptive,branches,
 fixed_menu_counterexamples:{'t=1':witness(A,B,0,1),'t=-1':witness([C(1),C(1),C(-1)],[C(1),C(-1),C(-1)],1,0)},
 prefix284_pair_J1:[fs(effect(A,1)),fs(effect(B,1))],
 scope:'C4 source-labelled formal BRC effect; not an original Stage50 run or a native H_n detector'};
 test(input===1024&&brc===2048&&groups.size===814&&two===66,'regression counts');return R;
}
if(typeof require!=='undefined'&&require.main===module)process.stdout.write(JSON.stringify(all(),null,2)+'\n');
if(typeof module!=='undefined')module.exports={all};

