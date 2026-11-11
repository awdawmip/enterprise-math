/** R730: exact positive 90-state lifted transfer and Birkhoff cross-ratio certificate.
 * Run: node R730_BRC_PROJECTIVE_MIXING_VERIFY.js > R730_BRC_PROJECTIVE_MIXING_RESULTS.json
 * No dependencies; 90x90 powers use exact safe integers (max power-9 cell 18).
 * Finite proof covers all 4005 row pairs and each row-pair's 90 column ratios.
 */
const certificate = function certificate(){
"use strict";
const triples=["012","013","014","023","024","034","123","124","134","234"];
const universe=[];
for(const u of triples) for(const v of triples) if([...u].filter(c=>v.includes(c)).length===2)universe.push([u,v]);
if(universe.length!==60)throw Error("universe arc count");
const permutations=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
const permutationIndex=new Map(permutations.map((p,i)=>[p.join(""),i]));
function edgePermutation([u,v]){
 const leaving=[...u].find(c=>!v.includes(c)),entering=[...v].find(c=>!u.includes(c));
 return [...u.replace(leaving,entering)].map(c=>v.indexOf(c));
}
const output={schema:"R730_CNB_BIRKHOFF_PROJECTIVE_CERTIFICATE_V1",arithmetic:"exact integer power and exact rational cross-product comparisons",source:"R729 immutable sharp representatives A=211733226574 B=5363347296468",systems:{}};
for(const [label,maskText] of Object.entries({A:"211733226574",B:"5363347296468"})){
 const mask=BigInt(maskText);
 const arcs=universe.filter((_,i)=>(mask&(1n<<BigInt(i)))!==0n);
 if(arcs.length!==15)throw Error("not 15 arcs");
 const J=Array.from({length:90},()=>[]);
 for(let i=0;i<15;i++)for(let j=0;j<15;j++){
  if(arcs[i][1]!==arcs[j][0]||arcs[i][0]===arcs[j][1])continue;
  const p=edgePermutation(arcs[j]);
  for(let k=0;k<6;k++){
   const idx=permutationIndex.get(permutations[k].map(z=>p[z]).join(""));
   if(idx===undefined)throw Error("bad frame update");
   J[6*i+k].push(6*j+idx);
  }
 }
 if(J.some(row=>row.length===0))throw Error("zero transfer row");
 const columnCounts=Array(90).fill(0);
 for(const row of J)for(const j of row)columnCounts[j]++;
 if(columnCounts.some(z=>z===0))throw Error("zero transfer column");
 let M=Array.from({length:90},(_,i)=>Array.from({length:90},(_,j)=>Number(i===j)));
 let zeros8=null;
 for(let t=1;t<=9;t++){
  const N=Array.from({length:90},()=>Array(90).fill(0));
  for(let i=0;i<90;i++)for(let j=0;j<90;j++)if(M[i][j]!==0)for(const k of J[j])N[i][k]+=M[i][j];
  M=N;
  if(t===8)zeros8=M.flat().filter(z=>z===0).length;
 }
 const cells=M.flat();
 if(cells.some(x=>!Number.isSafeInteger(x)||x<=0))throw Error("ninth power lacks positive integer entries");
 const min=Math.min(...cells),max=Math.max(...cells),sum=cells.reduce((a,b)=>a+b,0);
 let N=1,D=1,witness=null;
 let rowPairCount=0,ratioComparisons=0;
 for(let i=0;i<90;i++)for(let j=i+1;j<90;j++){
  rowPairCount++;
  let maxN=M[i][0],maxD=M[j][0],minN=maxN,minD=maxD,maxK=0,minK=0;
  for(let k=1;k<90;k++){
   ratioComparisons+=2;
   const n=M[i][k],d=M[j][k];
   if(n*maxD>maxN*d){maxN=n;maxD=d;maxK=k;}
   if(n*minD<minN*d){minN=n;minD=d;minK=k;}
  }
  const a=maxN*minD,b=maxD*minN;
  if(a*D>N*b){N=a;D=b;witness={row_i:i,row_j:j,column_k:maxK,column_l:minK,four_entries:[M[i][maxK],M[j][maxK],M[i][minK],M[j][minK]]};}
 }
 const g=(a,b)=>b?g(b,a%b):a;
 const div=g(N,D);N/=div;D/=div;
 if(label==="A" && !(min===1&&max===18&&zeros8===108&&sum===58764&&N===25&&D===1))throw Error("A reference mismatch");
 if(label==="B" && !(min===1&&max===18&&zeros8===72&&sum===61080&&N===21&&D===1))throw Error("B reference mismatch");
 output.systems[label]={arc_mask:maskText,arcs:arcs.map(e=>e.join(">")),states:90,transition_entries:J.reduce((z,row)=>z+row.length,0),L8_zero_entries:zeros8,L9_positive_entries:cells.length,L9_min:min,L9_max:max,L9_sum:sum,row_pairs_tested:rowPairCount,strict_ratio_comparisons:ratioComparisons,maximum_cross_ratio:[String(N),String(D)],cross_ratio_witness:witness,hilbert_contraction:label==="A"?"2/3":"(sqrt(21)-1)/(sqrt(21)+1)",error_bound:"|6*count_m(h)/total_m-1| <= exp(log(K)*q^floor((m-10)/9))-1 for m>=10",epsilon_10_percent_length_at_most:label==="A"?91:82,epsilon_1_percent_length_at_most:label==="A"?145:127};
}
output.status="PASS";
return output;
};
const result=certificate();
process.stdout.write(JSON.stringify(result,null,2)+'\n');
