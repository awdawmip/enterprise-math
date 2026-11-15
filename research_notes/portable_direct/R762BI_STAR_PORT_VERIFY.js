'use strict';
// R762BI independent reproducible exact finite GF(2) witness; Node.js >=18.
function generateEvidence(){
  const choose=(xs,r)=>{const ans=[];const rec=(start,cur)=>{if(cur.length===r){ans.push(cur.slice());return;}for(let i=start;i<=xs.length-(r-cur.length);i++){cur.push(xs[i]);rec(i+1,cur);cur.pop();}};rec(0,[]);return ans};
  const triples=choose([0,1,2,3,4,5],3);
  const star=triples.filter(t=>t.includes(0));
  const other=triples.filter(t=>!t.includes(0));
  const parity=(x,t)=>t.reduce((v,i)=>v^((x>>i)&1),0);
  const wt=(x,H)=>H.reduce((w,t)=>w+parity(x,t),0);
  const spectrum=new Map(),designs=[];
  let scenarios=0,sourceVectors=0;
  for(let mask=0;mask<(1<<other.length);mask++){
    const selected=other.filter((_,i)=>((mask>>i)&1));
    const H=star.concat(selected);
    const out=new Set(),weights=[];
    for(let x=0;x<64;x++){
      let y=0,w=0;
      for(let j=0;j<H.length;j++){const bit=parity(x,H[j]);y|=(bit<<j);w+=bit;}
      out.add(y);if(x!==0) weights.push(w);
      sourceVectors++;
    }
    const rank=Math.log2(out.size);
    if(!Number.isInteger(rank))throw Error("noninteger rank");
    const d=Math.min(...weights.filter(w=>w>0));
    const k=selected.length,key=`${k}:${rank}:${d}`;
    spectrum.set(key,(spectrum.get(key)||0)+1);
    if(k>0&&rank!==6)throw Error("wrong extended rank");
    if(k===0&&(rank!==5||d!==4))throw Error("wrong base code");
    if(k>=1&&k<=4&&d!==k)throw Error("wrong low extension distance");
    designs.push({mask,k,rank,d});
    scenarios++;
  }
  const expected=[
   [0,5,4,1],[1,6,1,10],[2,6,2,45],[3,6,3,120],[4,6,4,210],
   [5,6,4,90],[5,6,5,162],[6,6,4,15],[6,6,5,180],[6,6,6,15],
   [7,6,5,60],[7,6,6,60],[8,6,6,45],[9,6,7,10],[10,6,8,1]
  ];
  for(const [k,r,d,c] of expected)if(spectrum.get(`${k}:${r}:${d}`)!==c)throw Error(`spectrum mismatch ${k},${r},${d}`);
  if([...spectrum.values()].reduce((a,b)=>a+b,0)!==1024||spectrum.size!==expected.length)throw Error("incomplete census");
  const sample=designs.find(t=>t.k===5&&t.d===5);
  const chosen=other.filter((_,i)=>(sample.mask>>i)&1);
  const sampleWeights=Array.from({length:64},(_,x)=>wt(x,star.concat(chosen)));
  const baseOutputs=new Set(Array.from({length:64},(_,x)=>star.reduce((v,t,j)=>v|(parity(x,t)<<j),0)));
  if(baseOutputs.size!==32)throw Error("star kernel");
  const v=62,swapped=((v>>0)&1)<<1|((v>>1)&1)<<0|(v&(~3));
  if(wt(v,star)!==0||wt(swapped,star)===0)throw Error("future observer witness");
  const byK=Array.from({length:11},(_,k)=>({
    additional_nonstar_probes:k,
    total_probes:10+k,
    distance_census:expected.filter(t=>t[0]===k).map(t=>({dimension:t[1],distance:t[2],count:t[3]}))
  }));
  const minimumByErrors=Array.from({length:4},(_,t)=>{
    const ok=designs.filter(z=>z.rank===6&&z.d>=2*t+1);
    const minimum=Math.min(...ok.map(z=>z.k));
    return {correctable_errors:t,minimum_total_probes:10+minimum,minimum_extra_probes:minimum,number_of_optimal_subsets:ok.filter(z=>z.k===minimum).length};
  });
  return {
    schema:"R762BI_STAR_PORT_OBSERVER_CERTIFICATE_V1",
    model:"conditional_binary_signed_triad_incidence_not_native_TRIADIC_CLOSURE_E",
    source_domain:{orientations:64,star_probes:10,complement_probes:10,subsets:1024},
    star_code:{rank:5,dimension:5,length:10,distance:4,kernel_generators:["011111"],codeword_weight_enumerator:{"0":1,"4":15,"6":15,"10":1}},
    appended_probe_census:byK,
    sharp_fixed_star_error_thresholds:minimumByErrors,
    first_five_probe_two_error_design:chosen.map(t=>t.map(i=>i+1).join("")),
    example_full_code_weight_census:Object.fromEntries([...new Set(sampleWeights)].sort((a,b)=>a-b).map(w=>[w,sampleWeights.filter(v=>v===w).length])),
    full_S6_witness:{star_kernel_state_binary:"011111",swap_axes:"1<->2",star_input_weight_before:0,star_input_weight_after:wt(swapped,star)},
    exact_checker:{subsets_enumerated:scenarios,state_vectors_enumerated:sourceVectors,arithmetic:"integer_GF2_bitwise",assertions:"all_passed",scope:"all 2^10 distinct nonstar subsets times all 2^6 signed orientation states"}
  };
}
const result=generateEvidence();
console.log(JSON.stringify(result,null,2));
