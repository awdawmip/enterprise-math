// Exact BRC N=4 S23, original six-source causal model. Frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34
function verify() {
"use strict";
const N=3360000,R=6*N/5,H=N;
const check=(x,m)=>{if(!x)throw Error(m)};
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 12 24 34","12 13 23 24","24 34 12 14"];
const PAIRS_FULL=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 12 24 34","12 13 23 24","23 34 12 13","24 34 12 14"];
const K1="2/5 0 2/5 1/5;2/5 2/5 0 1/5;3/5 0 0 2/5;2/5 2/5 0 1/5";
const K2="1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2";
const K3="0 1/2 1/2 0;0 1 0 0;0 1 0 0;0 0 1/2 1/2";
const names=["D1","D2","D3","D4","D6","D7","D8","K1_new","K2","K3"];
const scale=q=>{let [a,b="1"]=String(q).split("/").map(Number);let x=N*a/b;check(Number.isSafeInteger(x),"fraction "+q);return x};
const mix=rows=>M.map((ws,i)=>[0,1,2,3].map(j=>{let s=ws.reduce((v,w,k)=>v+w*rows[k][j],0);check(s%20===0,"mixture "+i);return s/20}));
const kernel=rows=>{check(rows.length===4&&rows.every(r=>r.length===4&&r.every(x=>Number.isSafeInteger(x)&&x>=0)&&r.reduce((v,x)=>v+x,0)===N),"kernel");return mix(G.map(g=>rows[g]))};
const pair=s=>kernel(s.split(" ").map(w=>[1,2,3,4].map(j=>N*[...w].filter(c=>+c===j).length/2)));
const free=s=>kernel(s.split(";").map(w=>w.trim().split(/\s+/).map(scale)));
const bank=[...PAIRS_FULL.filter((_,i)=>i!==4).map(pair),...([K1,K2,K3].map(free))];
check(bank.length===10,"ten labels");
const prepareScaled=z=>{
 check(z.length===11&&z.every(x=>Number.isSafeInteger(x)&&x>=0&&x<=N),"strategy");
 let src=A.map((a,i)=>{const x=z[a],b=z[B[i]],c=z[C[i]],tail=(N-x)*(N-b)/N,mid=(N-x)*b/N,last=tail*c/N;
 check([tail,mid,last].every(Number.isSafeInteger),"causal");return [x,mid,last,tail-last]});
 check(src.every(r=>r.every(x=>x>=0)&&r.reduce((v,x)=>v+x,0)===N),"sources");
 return mix(src);
};
const prepare=z=>prepareScaled(z.map(scale));
const risk2=(p,q)=>Math.max(...p.map((row,i)=>row.reduce((sum,v,j)=>sum+Math.abs(v-q[i][j]),0)));
const at=(s,t,u)=>prepareScaled([s,t,u,0,0,N,0,0,0,0,0]);
const J=t=>prepare([1,t,0,0,0,0,0,0,0,1,0]);
const raw={W:[1,0,0,0,1,0,0,0,0,0,0],J:[1,"1/3",0,0,0,0,0,0,0,1,0],A:["1/7",1,0,0,0,0,1,1,1,0,1],B:[1,"1/7",0,0,0,0,1,1,1,0,1],C:["1/7",1,0,0,0,1,0,0,0,0,0],X:[1,"1/15",0,0,0,0,1,1,1,0,1],Y:[1,0,0,0,0,0,0,0,1,1,1],Z:[0,1,0,1,0,1,1,0,0,0,0]};
["00000000000","00000001000","00000000001","00101000000","00110000000","00101001000","00100000001","00100000000"].forEach((s,i)=>raw["T"+(i+1)]=[...s].map(Number));
raw.U=[..."00110000001"].map(Number);raw.V=[..."10000000000"].map(Number);raw.H=["1/4",1,0,0,0,1,0,0,0,0,0];raw.Hm=["1/5",1,0,0,0,1,0,0,0,0,0];
check(Object.keys(raw).length===20,"20 policies");
const policies=Object.fromEntries(Object.entries(raw).map(([n,z])=>[n,prepare(z)]));
const minRisk2=p=>Math.min(...bank.map(q=>risk2(p,q)));
check(Math.max(...Object.values(policies).map(minRisk2))===R,"discrete upper");
const fixed=bank.slice(0,7),core=["W","X","Y","Z","T5","U","V","Hm","J1","Jp"],P=core.map(n=>n==="J1"?J(1):n==="Jp"?J("1/5"):policies[n]);
check(P.every(p=>Math.min(...fixed.map(q=>risk2(p,q)))>=R),"core fixed");
let forbidden=[];
for(let a=0;a<10;a++)for(let b=a+1;b<10;b++)for(let c=b+1;c<10;c++){
let best=Math.max(...[0,1,2,3,4,5].map(i=>[0,1,2,3].reduce((v,j)=>v+Math.max(P[a][i][j],P[b][i][j],P[c][i][j]),0)-N));
if(5*best>=9*N)forbidden.push([a,b,c]);
}
check(forbidden.length===84,"triple 84");
let minHits=Infinity;
for(let n=0;n<3**10;n++){let x=n,labels=[];for(let i=0;i<10;i++){labels.push(x%3);x=Math.floor(x/3)}
let hits=forbidden.reduce((v,[a,b,c])=>v+(labels[a]===labels[b]&&labels[b]===labels[c]?1:0),0);
check(hits>=1,"coloring "+n);minHits=Math.min(minHits,hits)}
check(minHits===1,"min hits");
const jcheck=[[0,8],["2/5",8],["2/5",7],[1,7]].map(([t,i])=>({t:String(t),decoder:names[i],risk2:risk2(J(t),bank[i])}));
check(jcheck.every(v=>v.risk2<=R),"J endpoints");
const face=(a,b)=>at(N*a/5,N*b/5,0);
let faceCells=0,faceCounts={};
for(let a=0;a<5;a++)for(let b=0;b<5;b++){let pts=[face(a,b),face(a+1,b),face(a,b+1),face(a+1,b+1)];
let worst=bank.map(q=>Math.max(...pts.map(p=>risk2(p,q)))),ix=worst.indexOf(Math.min(...worst));
check(worst[ix]<=R,"face "+a+","+b);faceCounts[names[ix]]=(faceCounts[names[ix]]||0)+1;faceCells++}
const n=10,grid=[];
for(let a=0;a<=n;a++){grid[a]=[];for(let b=0;b<=n;b++){grid[a][b]=[];for(let c=0;c<=n;c++)grid[a][b][c]=at(N*a/n,N*b/n,N*c/n)}}
const get=(a,b,c)=>grid[a][b][c];
let cubeCounts={},worstCertified=0,worstCell=null,witness="",cubes=0;
for(let a=0;a<n;a++)for(let b=0;b<n;b++)for(let c=0;c<n;c++){
let corners=[];for(let i=0;i<2;i++)for(let j=0;j<2;j++)for(let k=0;k<2;k++)corners.push(get(a+i,b+j,c+k));
let worst=bank.map(q=>Math.max(...corners.map(p=>risk2(p,q)))),best=Math.min(...worst),ix=worst.indexOf(best);
check(best<=R,"cube "+a+","+b+","+c+":"+best);
cubeCounts[names[ix]]=(cubeCounts[names[ix]]||0)+1;
if(best>worstCertified){worstCertified=best;worstCell=[a,b,c]}
witness+=ix.toString(10);cubes++;
}
check(cubes===1000&&witness.length===1000,"coverage");
const mid=prepare(["1/20","1/20","1/20",0,0,1,0,0,0,0,0]);let cc=[];
for(let i=0;i<2;i++)for(let j=0;j<2;j++)for(let k=0;k<2;k++)cc.push(get(i,j,k));
check(mid.every((r,i)=>r.every((v,j)=>8*v===cc.reduce((sum,p)=>sum+p[i][j],0))),"multi-affinity midpoint");
const edge=u=>prepare(["3/5","3/10",u,0,0,1,0,0,0,0,0]);
let edgeRisks=[{u:"0",decoder:"K1_new",risk2:risk2(edge(0),bank[7])},{u:"5/7",decoder:"K1_new",risk2:risk2(edge("5/7"),bank[7])},{u:"5/7",decoder:"D6",risk2:risk2(edge("5/7"),bank[4])},{u:"1",decoder:"D6",risk2:risk2(edge(1),bank[4])}];
check(edgeRisks.every(v=>v.risk2===H)&&minRisk2(edge(0))===H,"edge sharp");
const gcd=(a,b)=>b?gcd(b,a%b):a,frac=x=>{let d=gcd(x,2*N);return x/d+"/"+(2*N/d)};
return {pass:"PASS_BRC_N4_S23_FULL_THREE_PARAMETER_CUBE_SHARP_THREE_FIFTHS_20261102",scientific_source_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",model:"six positive-weight sources AU0 AU1 AV BU0 BU1 BV; shared causal b_U",scale:N,tv_denominator:2*N,decoders:names,K1_new:K1,claim:"Sharp 3/5 over S18 union J([0,1]) union F([0,1]^3), seven fixed decoders and three free stochastic kernels",F:"(s,t,u,0,0;1,0,0,0,0,0)",cube:{vertices:1331,cubes,counts:cubeCounts,worst_selected_corner_risk:frac(worstCertified),worst_cell:worstCell,decoder_index_witness_1000_cells:witness,criterion:"One common decoder for all eight corners of each of 1000 cells; tensor multi-affinity and TV convexity cover every real interior point."},j_endpoint_risks:jcheck.map(v=>({...v,risk:frac(v.risk2)})),face_cells:faceCells,face_counts:faceCounts,old_policies:20,old_policies_max_min:"3/5",lower_core:core,forbidden_triples:forbidden.length,colorings_checked:3**10,min_monochromatic_hits:minHits,causal_edge_endpoints:edgeRisks.map(v=>({...v,risk:frac(v.risk2)})),causal_edge_bank_sup:"1/2",evidence_class:"author exact integer execution; independent review pending"};
}
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(),null,2));
