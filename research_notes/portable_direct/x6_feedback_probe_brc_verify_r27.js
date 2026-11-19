"use strict";
// R27 deterministic Boolean-BRC labeled successful-word language verifier.
// Carrier: Boolean trace support. Union and prefixed concatenation retain source and signed-Port labels.
// Node: node x6_feedback_probe_brc_verify_r27.js
function verifyR27() {
  const assert=(x,msg)=>{if(!x)throw Error(msg)};
  const allEdges=(n)=>{let a=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)a.push([i,j]);return a};
  const mask=(s,E)=>E.reduce((a,[i,j],k)=>a|(((s>>i&1)&&(s>>j&1))?(1<<k):0),0);
  const cases=[];let graphs=0,checkedPairs=0,checks=0,nodes=0;
  function runCase(n,E,name){
    const memo=new Map(),intern=new Map();let iid=1;
    const kE=E.length;
    function signature(h,theta,phase,returned,usedA,usedQ){
      if(h===0)return 0;
      const key=[h,theta,phase,returned,usedA,usedQ].join(',');
      if(memo.has(key))return memo.get(key);
      const outputs=[];
      for(let i=0;i<n;i++){
        const bit=1<<i,ret=(phase&bit)!==0;
        outputs.push(`B${i}${ret?'-':'+'}:${signature(h-1,theta,phase^bit,ret?(returned|bit):returned,usedA,usedQ)}`);
      }
      for(let k=0;k<kE;k++){
        const [i,j]=E[k],bi=(1<<i)|(1<<j);
        if(!(usedA&(1<<k))&&(returned&bi)===bi&&(theta&bi)===bi)
          outputs.push(`A${k}:${signature(h-1,theta,phase,returned,usedA|(1<<k),usedQ)}`);
      }
      if(usedA!==0){
        for(let i=0;i<n;i++){
          const bit=1<<i;
          if(!(usedQ&bit)&&(returned&bit)&&(theta&bit))
            outputs.push(`Q${i}:${signature(h-1,theta,phase,returned,usedA,usedQ|bit)}`);
        }
      }
      const canon=outputs.join('|');
      if(!intern.has(canon))intern.set(canon,iid++);
      const id=intern.get(canon);memo.set(key,id);return id;
    }
    const k=1<<n;let classCounts=[];
    const independent=Array.from({length:k},(_,s)=>mask(s,E)===0).filter(Boolean).length;
    const late=1+k-independent,early=new Set(Array.from({length:k},(_,s)=>mask(s,E))).size;
    for(let h=0;h<=8;h++){
      const ids=Array.from({length:k},(_,s)=>signature(h,s,0,0,0,0));
      const c=new Set(ids).size;classCounts.push(c);
      const expected=h<=4?1:h<=7?early:late;
      assert(c===expected,`class-count n=${n},E=${JSON.stringify(E)},h=${h}`);
      for(let s=0;s<k;s++)for(let t=s+1;t<k;t++){
        const es=mask(s,E),et=mask(t,E);
        const predicted=h<=4?true:h<=7?es===et:(s===t||(es===0&&et===0));
        assert((ids[s]===ids[t])===predicted,`language mismatch n=${n},E=${JSON.stringify(E)},h=${h},s=${s},t=${t}`);
        checkedPairs++;
      }
      checks+=k;
    }
    nodes+=memo.size;graphs++;
    cases.push({name,n,edges:E,independent_sets:independent,R26_classes:early,R27_classes:late,by_depth:classCounts,signature_states:memo.size});
  }
  for(let n=1;n<=4;n++){
    const pool=allEdges(n);
    for(let g=0;g<(1<<pool.length);g++)runCase(n,pool.filter((_,j)=>(g>>j)&1),`all_${n}_${g}`);
  }
  for(let name of ['empty','oneedge','path','star','complete']){
    const n=5;
    const E=name==='empty'?[]:name==='oneedge'?[[0,1]]:name==='path'?Array.from({length:n-1},(_,i)=>[i,i+1]):name==='star'?Array.from({length:n-1},(_,i)=>[0,i+1]):allEdges(n);
    runCase(n,E,name);
  }
  return {schema:'X6_R27_BOOLEAN_BRC_FEEDBACK_PROBE_V1',date:'2026-11-19',scope:'all 75 labeled simple graphs n<=4 plus five n=5 representative graphs; horizons h=0..8; exact deterministic successful-word Boolean BRC signatures',graphs_checked:graphs,initial_state_horizon_checks:checks,pairwise_comparisons:checkedPairs,visited_signature_states:nodes,result:'PASS',cases};
}
const output=verifyR27();
if(typeof require!=='undefined' && require.main===module)console.log(JSON.stringify(output,null,2));
if(typeof module!=='undefined')module.exports=verifyR27;
