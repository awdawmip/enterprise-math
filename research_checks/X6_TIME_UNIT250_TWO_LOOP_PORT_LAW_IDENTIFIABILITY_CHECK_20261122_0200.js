"use strict";
/* X6 Unit250: source-frozen conditional Port precision-observer inverse check.
 * Unit249 original immutable source c0116bf2ee4970493fcb6e7c55da4692202c4547:research_checks/X6_TIME_UNIT249_ORIGINAL_BRC_PRECISION_LAW_REPLAY_RESULTS_20261122.json
 * Original Git blob 1d822a82adaa899c72a7d206d8407a713aec0ad5; source rows below preserve per-Port excursion counts.
 * Observer: labelled endpoint C24 precision, with fixed calibrated ring g5=g10=3.
 * THIS IS NOT A PHYSICAL/NATIVE PORT EXECUTION.
 */
const SOURCE_ROWS = [[0,0,1],[0,2,6],[0,4,3],[0,6,2],[0,8,3],[0,10,6],[2,0,6],[2,2,1],[2,4,6],[2,6,3],[2,8,2],[2,10,3],[4,0,3],[4,2,6],[4,4,1],[4,6,6],[4,8,3],[4,10,2],[6,0,2],[6,2,3],[6,4,6],[6,6,1],[6,8,6],[6,10,3],[8,0,3],[8,2,2],[8,4,3],[8,6,6],[8,8,1],[8,10,6],[10,0,6],[10,2,3],[10,4,2],[10,6,3],[10,8,6],[10,10,1]];
function calculate() {
  let assertions=0;
  const ok=(b,msg)=>{assertions++;if(!b)throw Error(msg)};
  const mod=(a,n)=>((a%n)+n)%n;
  const gcd=(a,b)=>b?gcd(b,a%b):a;
  const ports=[0,2,4,6,8,10];
  const seen=new Set();
  ok(SOURCE_ROWS.length===36,"36 original source cases");
  for(const [i,j,c] of SOURCE_ROWS){
    const id=i+","+j,d=mod(j-i,12);
    ok(ports.includes(i)&&ports.includes(j),"original signed ring endpoint");
    ok(!seen.has(id),"distinct original Port case");seen.add(id);
    ok(c===12/gcd(12,d),"original shortest BRC excursion count");
  }
  const crt=(a8,a3)=>{
    for(let x=0;x<24;x++)if(x%8===a8 && x%3===a3)return x;
    throw Error("no CRT residue");
  };
  const residual=(law,i,j)=>mod(law.alpha[i/2]+law.beta[j/2],24);
  const classes=[];
  // Normalize the common centre gauge by delta_alpha[0]=0.
  // Mod 8: alpha_even=0, alpha_odd=b in {0,4}.
  // Mod 3: alpha_k has classes k mod 3; class zero is 0.
  for(const b of [0,4])for(let r1=0;r1<3;r1++)for(let r2=0;r2<3;r2++){
    const r=[0,r1,r2];
    const alpha=ports.map((_,k)=>crt(k%2===0?0:b,r[k%3]));
    const beta=alpha.map(a=>mod(-a,24));
    const law={b,r1,r2,alpha,beta};
    for(const [i,j,c] of SOURCE_ROWS)
      ok(mod(c*residual(law,i,j),24)===0,"all original C24 endpoint observations unchanged");
    classes.push(law);
  }
  ok(classes.length===18,"18 inequivalent modulo-gauge laws");
  ok(new Set(classes.map(x=>x.alpha.join(","))).size===18,"class uniqueness");
  const histogram={};
  let minAfterOne=18;
  for(const i of ports)for(const j of ports){
    const survivors=classes.filter(l=>residual(l,i,j)===0).length;
    histogram[survivors]=(histogram[survivors]||0)+1;
    minAfterOne=Math.min(minAfterOne,survivors);
    ok(survivors>=3,"one extra scalar readout leaves 3-primary ambiguity");
  }
  const afterFirst=classes.filter(l=>residual(l,0,2)===0);
  const afterTwo=afterFirst.filter(l=>residual(l,2,4)===0);
  ok(afterFirst.length===3,"x0 P x2 x1 x0 leaves 3 laws");
  ok(afterTwo.length===1 && afterTwo[0].alpha.every(x=>x===0),
     "two additional four-primitive-event loops identify up to centre gauge");
  const witness=classes.find(l=>l.alpha.join(",")==="0,16,0,0,16,0");
  ok(!!witness,"non-gauge counterlaw present");
  ok(residual(witness,0,2)===8,"four-event loop distinguishes C24 counterlaw by 8");
  // Every informative single-passage loop has i!=j; its two centre events plus
  // at least two ring events cost >=4. Two scalar readouts are necessary at mod 3.
  ok(ports.every(i=>ports.every(j=>i===j || 2+Math.min(mod(j-i,12),mod(i-j,12))>=4)),
     "informative elementary loop cost lower bound");
  const result={
    schema:"X6_UNIT250_PORT_LAW_OBSERVER_INVERSE_CERT_V1",
    provenance:{
      frozen_p000:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
      case_source_commit:"c0116bf2ee4970493fcb6e7c55da4692202c4547",
      case_source_path:"research_checks/X6_TIME_UNIT249_ORIGINAL_BRC_PRECISION_LAW_REPLAY_RESULTS_20261122.json",
      case_source_blob_sha1:"1d822a82adaa899c72a7d206d8407a713aec0ad5"
    },
    modulus:24,original_traces_checked:SOURCE_ROWS.length,
    normalized_law_fibre_size:classes.length,
    full_kernel_size_including_centre_gauge:24*classes.length,
    one_extra_elementary_loop:{minimum_remaining_laws:minAfterOne,survivor_histogram:histogram},
    two_extra_loops:[
      {ordered_cells:["x0","P","x2","x1","x0"],native_events:4},
      {ordered_cells:["x2","P","x4","x3","x2"],native_events:4}
    ],
    remaining_after_first:afterFirst.length,
    remaining_after_both:afterTwo.length,
    extra_native_events:8,
    witness:{delta_alpha:witness.alpha,delta_beta:witness.beta,
             original_36_C24_readout_difference:0,
             first_four_event_loop_C24_readout_difference:8},
    checked_integer_assertions:assertions,
    mismatch_count:0,
    scope:"exact finite conditional model; no Source-admitted physical Port transition or measured C24 sensor"
  };
  return result;
}
const result=calculate();
if(typeof module!=="undefined" && typeof require!=="undefined" && require.main===module)
  console.log(JSON.stringify(result,null,2));
