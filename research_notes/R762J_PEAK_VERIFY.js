// R762J — named-source peak-memory exact observer verification (Node.js >=16)
// Four-state? No: U=0, A=1, C=2, plus separate running peak P.
function peakAudit(n) {
 const states=new Set(["0".repeat(n)+"|0"]);let frontier=new Set(states);
 let layerCounts=[1];
 for(let t=0;t<2*n;t++){
   const next=new Set();
   for(const key of frontier){
     const [status,p]=key.split("|"); const peak=Number(p);
     for(let i=0;i<n;i++)if(status[i]!=="2"){
       const dst=status.slice(0,i)+(status[i]==="0"?"1":"2")+status.slice(i+1);
       const live=[...dst].filter(x=>x==="1").length;
       const target=dst+"|"+Math.max(peak,live);
       next.add(target); states.add(target);
     }
   }
   layerCounts.push(next.size);
   frontier=next;
 }
 const statusToPeaks=new Map();
 for(const key of states){
   const [status,p]=key.split("|");
   const existing=statusToPeaks.get(status)||[];existing.push(Number(p));statusToPeaks.set(status,existing);
 }
 for(const [status,peaks] of statusToPeaks){
   const a=[...status].filter(x=>x==="1").length;
   const c=[...status].filter(x=>x==="2").length;
   const low=(a+c===0)?0:Math.max(1,a);
   const high=a+c;
   const expected=Array.from({length:high-low+1},(_,j)=>low+j);
   peaks.sort((x,y)=>x-y);
   if(JSON.stringify(peaks)!==JSON.stringify(expected))throw Error("incomplete peak fiber: "+status);
 }
 const theoretical=(n+3)*3**(n-1)-2**n+1;
 if(states.size!==theoretical)throw Error("closed-form peak cardinality mismatch");
 const booleanSet=new Set([...states].map(key=>{const [s,p]=key.split("|");return s+"|"+(Number(p)===n?1:0)}));
 const booleanExpected=n===1?3:3**n+2**n-1;
 if(booleanSet.size!==booleanExpected)throw Error("closed-form full-copresence history flag cardinality mismatch");
 return {n,peakAugmentedStates:states.size,fullCoPresenceFlagAugmentedStates:booleanSet.size,peakBits:Math.ceil(Math.log2(states.size)),flagBits:Math.ceil(Math.log2(booleanSet.size)),layerStateCounts:layerCounts};
}
const result={schema:"R762J_PEAK_RESIDUAL_EXACT_V1",model:"Source-tagged U/A/C single-outbound-single-return model; abstract event indices",proofStatus:"author-side exact constructive proof and finite full-state checks",allChecks:"PASS",testedN:[1,8],rows:Array.from({length:8},(_,i)=>peakAudit(i+1)),nativeTriadicForceAdmission:"UNTESTED",V29V39:"NOT_EXECUTED"};
console.log(JSON.stringify(result,null,2));
