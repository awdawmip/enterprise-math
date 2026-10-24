// Exact BigInt author-side reproducibility. Run: node verify_action2_unimodality.js
'use strict';

const Q=[[1n,665n,1n,333n],[333n,333n,1n,333n],[1n,1n,1n,997n]];
const E=[[0,1],[1,2],[1,3],[2,3]],deg=[1n,3n,2n,2n];
const layers=[[0,8,110,17],[1,6,225,30],[2,4,322,60],[0,7,353,15],
[3,2,402,139],[1,5,426,30],[2,3,485,66],[0,6,502,17],
[3,1,533,176],[1,4,545,36],[2,2,579,86],[0,5,587,22],
[3,0,607,353],[1,3,612,49],[2,2,579,86],[0,4,634,30],
[1,2,648,73],[2,0,660,241],[0,3,660,44],[1,1,669,116],
[0,2,675,68],[1,0,681,220],[0,1,683,112],[0,0,689,214]];
const rows=[
[0,8,110,17],[1,6,225,30],[2,4,322,60],[0,7,353,15],
[3,2,402,139],[1,5,426,30],[2,3,485,66],[0,6,502,17],
[3,1,533,176],[1,4,545,36],[2,2,579,86],[0,5,587,22],
[3,0,607,353],[1,3,612,49],[2,1,631,129],[0,4,634,30],
[1,2,648,73],[2,0,660,241],[0,3,660,44],[1,1,669,116],
[0,2,675,68],[1,0,681,220],[0,1,683,112],[0,0,689,214]];
const p=(b,e)=>b**BigInt(e),size=c=>c[0]+c[1]+c[2],ok=(v,m)=>{if(!v)throw Error(m)};
function num(c){
let t=0n;for(const [i,j]of E){let v=1n;for(let a=0;a<3;a++)v*=p(Q[a][i]+Q[a][j],c[a]);t+=v;}
for(let i=0;i<4;i++){let v=deg[i];for(let a=0;a<3;a++)v*=p(Q[a][i],c[a]);t-=v;}return t;
}
function abc(x,z){return [
p(2n,z)*p(666n,x)+p(998n,z)*p(998n,x),
p(2n,z)*p(666n,x)+p(998n,z)*p(334n,x),
1n+3n*p(665n,x)+2n*p(997n,z)*p(333n,x)];}
function grouped(x,y,z){const [A,B,C]=abc(x,z);return A*p(666n,y)+B*p(334n,y)-C*p(333n,y)-2n;}
function F(x,y,z){const [A,B,C]=abc(x,z);return -334n*A*p(666n,y)-666n*B*p(334n,y)+667n*C*p(333n,y)+1998n;}
function S(k){return -1000n*(p(2n,k)+p(998n,k))+1334n*p(997n,k)+4666n;}
function mask(c){let m=Array(16).fill(0n);m[0]=1n;
for(let a=0;a<3;a++)for(let j=0;j<c[a];j++){
const t=Array(16).fill(0n);for(let b=0;b<16;b++)if(m[b])for(let i=0;i<4;i++)t[b|(1<<i)]+=m[b]*Q[a][i];m=t;}
return E.reduce((v,[i,j])=>v+m[(1<<i)|(1<<j)],0n);}
function verify(){
let identities=0;
for(const x of [0,1,2,3])for(const y of [0,1,2,3,6])for(const z of [1,2,7,17,288]){
const d=grouped(x,y+1,z)-1000n*grouped(x,y,z),[A,,C]=abc(x,z);
ok(num([x,y,z])===grouped(x,y,z),'grouped');
ok(d===F(x,y,z),'difference');
ok(F(x,y+1,z)-334n*F(x,y,z)===-334n*332n*A*p(666n,y)-667n*C*p(333n,y)-1998n*333n,'recurrence');
identities++;}
ok(S(1)===334664n&&S(287)>0n&&S(288)<0n,'threshold signs');
for(const [k,lo,hi]of [[287,616999n,617000n],[288,-720396n,-720395n]]){
const m=p(997n,k);ok(lo*m<1000000n*S(k)&&1000000n*S(k)<hi*m,'threshold interval');}
ok(995000n*2n-1000n*998n-4647336n<0n&&p(998n,2)>995n*p(2n,2),'monotonic gate');
let full=0,short=0;const cert=[];
for(const [X,Y,Z,k]of rows){
const c=[X,Y,Z],terminal=num(c);let best=null,where=null,steps=0;
full+=(X+1)*(Y+1);
for(let x=0;x<=X;x++)for(const y of [...new Set([0,Y])]){
const q=[x,y,k],gap=num(q)*p(1000n,size(c)-size(q))-terminal;
ok(gap>0n,'endpoint positive '+c+' '+q);
if(best===null||gap<best){best=gap;where=q;}
steps++;short++;}
ok(where.join(',')===[0,0,k].join(','),'minimum location');
cert.push({terminal:c,layer:k,original_points:(X+1)*(Y+1),endpoint_points:steps,min_gap_at:where,min_gap_numerator:best.toString(),denominator:'1000^'+size(c)});
}
ok(cert.length===24&&full===170&&short===90,'coverage');
const probes=[[0,0,1],[0,1,1],[0,2,1],[1,0,1],[1,1,1],[1,2,3],[2,2,7],[3,3,7],[0,0,288],[0,1,288],[2,5,60],[3,3,184],[0,0,17],[1,6,30],[3,2,139]];
for(const q of probes)ok(mask(q)===num(q),'mask '+q);
return {schema:'EM_BRC_ACTION2_UNIMODALITY_EXACT_V1',status:'PASS_AUTHOR_UNREVIEWED_NOT_ADMITTED',
source_model:{weights:Q.map(r=>r.map(Number)),denominator:1000,good_edges:E},
exact_identity_points:identities,independent_mask_dp_points:probes.length,
pure_action3_exact_threshold:288,sign_S_287:'POSITIVE',sign_S_288:'NEGATIVE',
interval_S_287:'616999/1000000<S(287)/997^287<617000/1000000',
interval_S_288:'-720396/1000000<S(288)/997^288<-720395/1000000',
source_transversal_commit:'0029daddde2e87ec299e1cfeb1a5f13edf4c3694',
all_original_layer_points:full,reduced_endpoint_points:short,certificates:cert,
limits:'Fixed auxiliary model only; analytic y-theorem, inherited unreviewed Hall classification; no native X6 transfer.'};
}

console.log(JSON.stringify(verify(),null,2));
