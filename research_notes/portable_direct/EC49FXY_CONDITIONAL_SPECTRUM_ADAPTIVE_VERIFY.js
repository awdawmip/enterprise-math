'use strict';
// EC49FXY — exact integer conditional-spectrum checking. Frozen scientific input BRC16943.
const must=(p,s)=>{if(!p)throw Error(s)},mod=(n,m)=>(n%m+m)%m,gcd=(a,b)=>b?gcd(b,a%b):a;
const inv=(a,m)=>{for(let x=1;x<m;x++)if(mod(a*x,m)===1)return x;throw Error('inverse')};
const slopes={'0,0':[3],'0,1':[0,3,4,5],'1,0':[2,3,4,5],'1,1':[2,3]};
function P(h,n){h=mod(h,10);n=mod(n,10);if(h%5===0&&n%5===0)return false;
const s=h%5===0?5:mod(n*inv(h%5,5),5);return slopes[`${h%2},${n%2}`].includes(s)}
const reps=new Map();
for(let a=0;a<10;a++)for(let c=0;c<10;c++)if(gcd(gcd(a,c),10)===1){
let x=-1,y=-1; outer:for(let xx=0;xx<10;xx++)for(let yy=0;yy<10;yy++)if(mod(c*xx-a*yy+1,10)===0){x=xx;y=yy;break outer}
let u=0;for(let t=0;t<10;t++)if(P(x+a*t,y+c*t))u|=1<<t;
reps.set(`${a},${c}`,{x,y,u})}
must(reps.size===72&&new Set([...reps.values()].map(s=>s.u)).size===50,'50 supports');
function norm(a,c){
const b=a+c,e=inv(a,b),h0=(a*e-1)/b,n0=e-h0,{x,y,u}=reps.get(`${a%10},${c%10}`);
let t0=-1;for(let t=0;t<10;t++)if(mod(h0+a*t-x,10)===0&&mod(n0+c*t-y,10)===0){t0=t;break}
must(t0>=0,'normalization');
const L0=9*(h0+a*t0)+10*(n0+c*t0),L1=9*a+10*c;
const z=mod(L1,11)===0?null:mod(-L0*inv(mod(L1,11),11),11);
must(z!==null||mod(L0,11)!==0,'degenerate factor');
return {a,b,c,u,z,h0,n0,t0}}
const states=new Map();
for(let b=2;b<=139;b++)for(let a=1;a<b;a++)if(gcd(a,b)===1){
const s=norm(a,b-a),k=`${s.u}/${s.z}`;if(!states.has(k))states.set(k,s)}
must(states.size===600,'600 states');
function spec(s){const U=Array.from({length:10},(_,i)=>s.u>>i&1),V=Array.from({length:11},(_,i)=>Number(s.z!==i));
const a=Array.from({length:10},(_,t)=>U.reduce((q,x,j)=>q+x*U[mod(t-j,10)],0));
const v=Array.from({length:11},(_,t)=>V.reduce((q,x,j)=>q+x*V[mod(t-j,11)],0));
return a.flatMap(x=>v.map(y=>2*(U.reduce((p,q)=>p+q,0)*V.reduce((p,q)=>p+q,0)-x*y))).join(',')}
const fibers=new Map();for(const s of states.values()){const k=spec(s);if(!fibers.has(k))fibers.set(k,[]);fibers.get(k).push(s)}
const pairs=[];for(const f of fibers.values()){
must(f.length===1||f.length===2,'spectrum fiber');
if(f.length===2){must(f[0].z===f[1].z,'pair factor');
pairs.push({G:f[0].u^f[1].u,z:f[0].z,H:Math.max(f[0].b,f[1].b)})}}
must(fibers.size===478&&pairs.length===122,'pair census');
const mask=a=>a.reduce((m,j)=>m|1<<j,0);
const groups=[{id:'A',rows:[1,4,6,9]},{id:'B',rows:[2,7]},{id:'C',rows:[3,8]}].map(g=>({...g,G:mask(g.rows)}));
must(groups.every(g=>pairs.some(p=>p.G===g.G&&p.H<=22)),'early minimal group');
must([...new Set(pairs.map(p=>p.G))].every(G=>groups.some(g=>(G&g.G)===g.G)),'support inclusion');

// EC49FXY: after indexed-spectrum observation, select different sites in each fiber.
const bitcount=n=>{let c=0;while(n){n&=n-1;c++}return c};
const size=p=>bitcount(p.G)*(p.z===null?11:10);
const chosen=(p,r)=>{const a=[];for(let j=0;j<10;j++)if(p.G>>j&1)for(let z=0;z<11;z++)if(p.z!==z&&a.length<r)a.push([j,z]);return a};
const distance=(a,p)=>a.reduce((s,[j,z])=>s+Number((p.G>>j&1)!==0&&p.z!==z),0);
must(pairs.length===122&&fibers.size===478,'frozen census');
const ps=pairs.map(p=>({...p,delta_size:size(p)}));
const minimum=H=>H<=13?null:H<=15?40:20;
let cases=0,feasible=0,infeasible=0,checks=0;
const sample={};
for(let H=2;H<=139;H++){
 const present=ps.filter(p=>p.H<=H);
 const mu=present.length?Math.min(...present.map(p=>p.delta_size)):null;
 must(mu===minimum(H),'minimum mismatch H='+H);
 if([2,13,14,15,16,22,44,52,64,139].includes(H))sample[H]={pairs:present.length,minimum:mu};
 for(let r=1;r<=110;r++){
  cases++;
  if(mu===null){feasible++;continue}
  if(r>mu){infeasible++;must(present.some(p=>p.delta_size<r),'obstruction');continue}
  feasible++;
  for(const p of present){const a=chosen(p,r);
    must(a.length===r&&new Set(a.map(x=>x.join(','))).size===r,'set size');
    must(distance(a,p)===r,'adaptive distance');checks++}
 }
}
must(Math.min(...ps.map(p=>p.delta_size))===20,'global min');
const transition=ps.filter(p=>p.H<=16).sort((a,b)=>a.H-b.H||a.delta_size-b.delta_size);
must(transition.some(p=>p.H===14&&p.delta_size===40),'H14 witness');
must(transition.some(p=>p.H===15&&p.delta_size===40),'H15 witness');
must(transition.some(p=>p.H===16&&p.delta_size===20),'H16 witness');
let original=0;
for(const s of states.values())for(let t=0;t<110;t++){
 const h=s.h0+s.a*(s.t0+t),n=s.n0+s.c*(s.t0+t);
 must((P(h,n)&&mod(9*h+10*n,11)!==0)===((s.u>>(t%10)&1)!==0&&s.z!==t%11),'direct C11');
 original++;
}
console.log(JSON.stringify({
 schema:'EC49FXY_CONDITIONAL_ADAPTIVE_V1',frozen_pin:'BRC16943',result:'ALL_PASS',
 normalized_states:states.size,indexed_spectra:fibers.size,doubleton_fibers:pairs.length,
 original_integer_C11_checks:original,height_distance_cases:cases,
 feasible_cases:feasible,infeasible_cases:infeasible,physical_pair_distance_checks:checks,
 min_support_by_height:[{H:2,mu:null},{H:14,mu:40},{H:16,mu:20}],
 sample_heights:sample,initial_pair_certificates:transition.map(p=>({H:p.H,G:p.G,z:p.z,delta_size:p.delta_size})),
 theorem:'for H<=13 cost0; H14-15 cost r up to40 else impossible; H>=16 cost r up to20 else impossible',
 conditional_on:'complete indexed reflection-defect spectrum revealed before selecting Boolean sites',
 not_priced:'cost of obtaining the complete indexed spectrum',
 status:'AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED',
 native_x6_transfer:'NOT_CLAIMED'
},null,2));