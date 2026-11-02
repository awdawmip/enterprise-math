/* BRC N4/S23 S17 exact six-source certificate; run: node VERIFY.js */
const verifyS18=function verifyS18() {
  const N=12600,TV_DEN=2*N;
  const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
  const AA=[0,0,0,1,1,1],BB=[2,2,3,2,2,4],CC=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
  function check(b,msg){if(!b)throw Error("ASSERT:"+msg)}
  function frac(s){const parts=String(s).split("/"),p=Number(parts[0]),d=Number(parts[1]||"1"),scaled=p*N/d;check(Number.isSafeInteger(scaled),"exact rational scale "+s);return scaled}
  function divExact(a,d,msg){const q=a/d;check(Number.isSafeInteger(q),msg);return q}
  const OFF=["00000000000","00000001000","00000000001","00101000000","00110000000","00101001000","00100000001","00100000000"];
  const BASE=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 12 24 34","12 13 23 24","23 34 12 13","24 34 12 14"];
  const O=(s,t)=>[s,t,0,0,0,0,1,1,1,0,1],Zt=(s,t)=>[s,t,0,0,0,1,0,0,0,0,0];
  const raw={W:[1,0,0,0,1,0,0,0,0,0,0],J:[1,"1/3",0,0,0,0,0,0,0,1,0],A:O("1/7",1),B:O(1,"1/7"),C:Zt("1/7",1),X:O(1,"1/15"),Y:[1,0,0,0,0,0,0,0,1,1,1],Z:[0,1,0,1,0,1,1,0,0,0,0]};
  OFF.forEach((bits,i)=>raw["T"+(i+1)]=[...bits].map(Number));
  raw.U=[..."00110000001"].map(Number);
  raw.V=[..."10000000000"].map(Number);
  const names=Object.keys(raw);
  function F(a,b,c){const v=divExact((N-a)*(N-b),N,"v");return [a,divExact((N-a)*b,N,"f2"),divExact(v*c,N,"f3"),divExact(v*(N-c),N,"f4")]}
  function prepare(sourceRows){return M.map((weights,i)=>[0,1,2,3].map(atom=>divExact(weights.reduce((v,w,s)=>v+w*sourceRows[s][atom],0),20,"mix "+i+":"+atom)))}
  function P(policy){const z=policy.map(frac);check(z.length===11&&z.every(v=>v>=0&&v<=N),"legal policy");return prepare(AA.map((a,s)=>F(z[a],z[BB[s]],z[CC[s]])))}
  function Q(k){check(k.length===4&&k.every(row=>row.length===4&&row.reduce((a,b)=>a+b,0)===N&&row.every(v=>v>=0)),"stochastic kernel");return prepare(G.map(g=>k[g]))}
  const kernel=s=>s.split(";").map(row=>row.trim().split(/\s+/).map(frac));
  const pair=s=>s.split(" ").map(x=>[1,2,3,4].map(t=>divExact([...x].filter(y=>Number(y)===t).length*N,2,"pair")));
  const fixed=BASE.map(s=>Q(pair(s)));
  const kernelStrings=[
  "5/7 0 2/7 0;3/7 0 2/7 2/7;3/7 0 1/35 19/35;3/7 10/21 0 2/21",
  "11/21 10/21 0 0;10/21 11/21 0 0;1/21 10/21 0 10/21;0 0 11/21 10/21",
  "1/2 0 1/2 0;1/2 1/2 0 0;1/2 0 1/2 0;1/2 0 1/2 0"
];
  const free=kernelStrings.map(s=>Q(kernel(s)));
  const prepared=names.map(n=>P(raw[n]));
  check(prepared.every(rows=>rows.length===6&&rows.every(row=>row.reduce((a,b)=>a+b,0)===N&&row.every(Number.isSafeInteger))),"all prepared masses exact");
  const riskNum=(p,q)=>Math.max(...p.map((row,i)=>row.reduce((sum,x,j)=>sum+Math.abs(x-q[i][j]),0)));
  const retained=fixed.filter((_,i)=>i!==4),bank=[...retained,...free];
  const risk=prepared.map(p=>Math.min(...bank.map(q=>riskNum(p,q))));
  const maxRisk=Math.max(...risk);check(maxRisk===14400,"sharp upper is 4/7");
  const LNames=["W","J","A","B","C","X","Y","Z","T5","U","V"],lower=LNames.map(n=>prepared[names.indexOf(n)]);
  const fixedRisks=lower.map(p=>Math.min(...retained.map(q=>riskNum(p,q))));
  check(fixedRisks.every(x=>x*7>=TV_DEN*4),"all eleven need free kernels below 4/7");
  const forbidden=[],tight=[];
  for(let a=0;a<11;a++)for(let b=a+1;b<11;b++)for(let c=b+1;c<11;c++){
    const best=Math.max(...[0,1,2,3,4,5].map(row=>[0,1,2,3].reduce((v,atom)=>v+Math.max(lower[a][row][atom],lower[b][row][atom],lower[c][row][atom]),0)-N));
    if(best*7>=12*N){forbidden.push([a,b,c]);if(best*7===12*N)tight.push([a,b,c]);}
  }
  check(forbidden.length===111,"111 exact triple event certificates");
  for(let i=0;i<177147;i++){let code=i;const colors=[];for(let a=0;a<11;a++){colors.push(code%3);code=Math.floor(code/3);}check(forbidden.some(([a,b,c])=>colors[a]===colors[b]&&colors[b]===colors[c]),"monochromatic obstruction for coloring "+i);}
  const oldK5=[
  "10/21 11/21 0 0;10/21 11/21 0 0;1/21 10/21 0 10/21;0 11/21 10/21 0",
  "44/63 0 19/63 0;44/63 0 19/63 0;4/9 1/9 4/9 0;4/9 0 4/9 1/9",
  "8/105 97/210 97/210 0;1/7 113/210 0 67/210;97/210 113/210 0 0;97/210 0 0 113/210"
];
  const V=prepared[names.indexOf("V")],oldRisk=[...retained,...oldK5.map(s=>Q(kernel(s)))].map(q=>riskNum(V,q));
  check(oldRisk.every(x=>x===TV_DEN),"V defeats prior S17 bank at TV 1");
  function fmtRisk(n){let d=TV_DEN,a=n;const gcd=(x,y)=>{while(y){const t=x%y;x=y;y=t;}return x};const k=gcd(a,d);a/=k;d/=k;return d===1?String(a):a+"/"+d;}
  return {pass:"PASS_BRC_N4_S23_S18_T5_U_V_SHARP_FOUR_SEVENTHS_EXACT_20261102",scientific_input_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",U_binary_coordinates:"00110000001",V_binary_coordinates:"10000000000",released_original_decoder:5,original_six_prepared_sources:["AU0","AU1","AV","BU0","BU1","BV"],exact_integer_scale:12600,exact_TV_denominator:TV_DEN,S11_lower_names:LNames,S18_all_names:names,lower_fixed_seven_min_risks:Object.fromEntries(LNames.map((n,i)=>[n,fmtRisk(fixedRisks[i])])),upper_S18_min_risks:Object.fromEntries(names.map((n,i)=>[n,fmtRisk(risk[i])])),upper_exact_kernels:kernelStrings,old_ten_S17_bank_risks_on_V:oldRisk.map(fmtRisk),exact_radius:fmtRisk(maxRisk),forbidden_triples:forbidden.length,tight_triples:tight.length,exhaustive_three_label_colorings:177147,arithmetic:"exact safe integers; F and mixture computed with exact divisibility, TV denominator 25200; no floating-point approximation in evaluated mathematical quantities",status:"AUTHOR_ANALYTIC_PROOF_EXACT_INTEGER_EXECUTED_UNREVIEWED_NOT_ADMITTED"};
};
console.log(JSON.stringify(verifyS18(),null,2));
