/* S23 full real J-edge sharp 4/7, original source provenance; run: node VERIFY.js */
function verify() {
/* Exact S23 finite-policy scan; frozen input 43ec6098b1330ae86d0a7863be336c5d97f6ef34. */
'use strict';
const N=50400, M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const A=[0,0,0,1,1,1], B=[2,2,3,2,2,4], C=[5,6,7,8,9,10], G=[0,0,1,2,2,3];
const PAIRS=['34 24 34 24','34 23 34 34','34 34 34 23','24 24 12 12','12 12 24 34','12 13 23 24','23 34 12 13','24 34 12 14'];
const FREE=["4/7 3/7 0 0;4/7 3/7 0 0;0 32/63 3/7 4/63;1/7 0 3/7 3/7","1 0 0 0;1 0 0 0;4/7 0 0 3/7;0 4/7 3/7 0","4/7 0 3/7 0;4/7 3/7 0 0;3/7 0 1/7 3/7;4/7 0 0 3/7"];
function assert(x,m){if(!x)throw Error(m)}
function value(s){const [a,b='1']=String(s).split('/').map(Number), x=a*N/b;assert(Number.isSafeInteger(x),'fraction '+s);return x}
function mix(rows){return M.map((w,i)=>Array.from({length:4},(_,j)=>{let x=w.reduce((v,t,s)=>v+t*rows[s][j],0)/20;assert(Number.isSafeInteger(x),'mix '+i);return x}))}
function decoder(rows){return mix(G.map(g=>rows[g]))}
const PAIR=s=>s.split(' ').map(x=>[1,2,3,4].map(k=>N*[...x].filter(t=>Number(t)===k).length/2));
const KERNEL=s=>s.split(';').map(r=>r.trim().split(/\s+/).map(value));
const bank=PAIRS.filter((_,i)=>i!==4).map(s=>decoder(PAIR(s))).concat(FREE.map(s=>decoder(KERNEL(s))));
function prepare(z){const source=A.map((a,s)=>{const x=z[a],b=z[B[s]],c=z[C[s]],r=N-x,q=r*(N-b)/N,t=q*c/N;assert(Number.isSafeInteger(q)&&Number.isSafeInteger(t),'causal rational');return [x,r*b/N,t,q-t]});return mix(source)}
function risks(p){return bank.map(q=>Math.max(...p.map((row,i)=>row.reduce((sum,v,j)=>sum+Math.abs(v-q[i][j]),0))))}
function minrisk(p){return Math.min(...risks(p))}
function ratio(x){let a=x,b=2*N;const gcd=(x,y)=>y?gcd(y,x%y):x;let d=gcd(a,b);return `${a/d}/${b/d}`}
function scan(base){const total=base**11;let max=0,countMax=0,countAbove=0,at4sevenths=0;
 for(let id=0;id<total;id++){let k=id,z=[];for(let j=0;j<11;j++){const v=k%base;k=Math.floor(k/base);z.push(v*N/(base-1))}const r=minrisk(prepare(z));
  if(r>max){max=r;countMax=0}if(r===max)countMax++;if(r*7>8*N)countAbove++;if(r*7===8*N)at4sevenths++}
 return {total,max:ratio(max),maximizer_count:countMax,above_4_7:countAbove,at_4_7:at4sevenths}}
function edges(){let max=0,above=0,first=null,total=0;
 for(let free=0;free<11;free++)for(let bits=0;bits<1024;bits++){let z=[],shift=0;for(let j=0;j<11;j++)z.push(j===free?0:((bits>>shift++)&1)*N);
 for(let t=1;t<8;t++){z[free]=t*N/8;const r=minrisk(prepare(z));total++;if(r>max)max=r;if(r*7>8*N){above++;if(!first)first={free_index_0based:free,binary_other_coordinates:bits,free_value:`${t}/8`,risk:ratio(r)}}}}
 return {total,max:ratio(max),above_4_7:above,first}}
const J=t=>prepare([N,value(t),0,0,0,0,0,0,0,N,0]);


const binary=scan(2), ternary=scan(3), onecoord=edges();
assert(binary.total===2048&&binary.max==='4/7'&&binary.maximizer_count===832&&binary.above_4_7===0,'binary');
assert(ternary.total===177147&&ternary.max==='4/7'&&ternary.maximizer_count===40041&&ternary.above_4_7===0,'ternary');
assert(onecoord.total===78848&&onecoord.max==='5/8'&&onecoord.above_4_7===288,'fractional grid');
const OFF=['00000000000','00000001000','00000000001','00101000000','00110000000','00101001000','00100000001','00100000000'];
const O=(s,t)=>[s,t,0,0,0,0,1,1,1,0,1], Zt=(s,t)=>[s,t,0,0,0,1,0,0,0,0,0];
const raw={W:[1,0,0,0,1,0,0,0,0,0,0],J:[1,'1/3',0,0,0,0,0,0,0,1,0],
 A:O('1/7',1),B:O(1,'1/7'),C:Zt('1/7',1),X:O(1,'1/15'),
 Y:[1,0,0,0,0,0,0,0,1,1,1],Z:[0,1,0,1,0,1,1,0,0,0,0]};
OFF.forEach((bits,i)=>raw['T'+(i+1)]=[...bits].map(Number));
raw.U=[...'00110000001'].map(Number);raw.V=[...'10000000000'].map(Number);
const names=Object.keys(raw), P18=names.map(n=>prepare(raw[n].map(value)));
const risks18=P18.map(minrisk);
const expected=['4/7','16/35','4/7','4/7','4/7','4/7','4/7','4/7',
'1/2','1/2','1/2','1/2','4/7','1/2','1/2','1/2','4/7','4/7'];
assert(risks18.every((x,i)=>ratio(x)===expected[i]),'all 18 risks');
const eleven=['W','J','A','B','C','X','Y','Z','T5','U','V'];
const lower=eleven.map(n=>prepare(raw[n].map(value)));
const riskNum=(p,q)=>Math.max(...p.map((row,i)=>row.reduce((s,x,j)=>s+Math.abs(x-q[i][j]),0)));
assert(lower.every(p=>Math.min(...bank.slice(0,7).map(q=>riskNum(p,q)))*7>=8*N),'eleven require free labels below 4/7');
const forb=[];
for(let a=0;a<11;a++)for(let b=a+1;b<11;b++)for(let c=b+1;c<11;c++){
 const best=Math.max(...[0,1,2,3,4,5].map(i=>[0,1,2,3].reduce((s,j)=>s+Math.max(lower[a][i][j],lower[b][i][j],lower[c][i][j]),0)-N));
 if(best*7>=12*N)forb.push([a,b,c]);
}
assert(forb.length===111,'triple cert count');
for(let i=0;i<177147;i++){
 let x=i,labels=[];
 for(let j=0;j<11;j++){labels.push(x%3);x=Math.floor(x/3);}
 assert(forb.some(([a,b,c])=>labels[a]===labels[b]&&labels[b]===labels[c]),'label triple coverage');
}
const endpoint={
 K1_t0:ratio(riskNum(J(0),bank[7])),
 K1_t17_63:ratio(riskNum(J('17/63'),bank[7])),
 K3_t17_63:ratio(riskNum(J('17/63'),bank[9])),
 K3_t1:ratio(riskNum(J(1),bank[9]))
};
assert(Object.values(endpoint).join(',')==='4/7,4/7,18/35,4/7','all-real edge endpoint certificate');
const H=['1/4',1,0,0,0,1,0,0,0,0,0].map(value);
const Hrisks=risks(prepare(H)).map(ratio);
assert(Hrisks.join(',')==='1/1,1/1,1/1,5/8,1/1,53/80,5/8,1/1,1/1,3/4','off-edge adversary');
return {pass:'PASS_BRC_N4_S23_S18_ALL_REAL_J_EDGE_SHARP_4_7_20261102',
 source_pin:'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
 scale:N,TV_denominator:2*N,six_sources:['AU0','AU1','AV','BU0','BU1','BV'],
 kernel_group_rows:['AU','AV','BU','BV'],fixed_decoders:['D1','D2','D3','D4','D6','D7','D8'],
 free_kernels:FREE, S18_min_risks:Object.fromEntries(names.map((n,i)=>[n,ratio(risks18[i])])),
 lower_core:eleven,forbidden_source_event_triples:forb.length,three_colorings_verified:177147,
 edge_partition:['0','17/63','1'],edge_endpoint_risks:endpoint,
 exact_continuum_argument:'Convex L_K1(J(t)) on [0,17/63], convex L_K3(J(t)) on [17/63,1]',
 binary,ternary,one_coordinate_eighth_grid:onecoord,
 off_edge_H_policy:'1/4 1 0 0 0;1 0 0 0 0 0',H_bank_risks:Hrisks,
 arithmetic:'safe integer scale 50400, TV denominator 100800, no floating-point for mathematical quantities'};

}
if(typeof require!=='undefined' && require.main===module) console.log(JSON.stringify(verify(),null,2));
