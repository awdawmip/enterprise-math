/* PREFIX-281: exact C4 BRC source-labelled path-pair verification.
 * Evaluates conditional filter-branch observations; not a native heart-beat update.
 * Run with Node.js: node verify_prefix281.js
 */
const verifyPrefix281 = function verifyPrefix281() {
  "use strict";
  // Exact C4 source-labelled ordered-pair BRC. All masses and path-pair values are BigInt.
  // Filters are DECLARED formal branch-preserving source convolutions, not native heartbeat laws.
  const R = [1n,0n,-1n,0n], I = [0n,1n,0n,-1n];
  const pos = n => ((n % 4) + 4) % 4;
  const base = (weights, name) => weights.map((w,j) => [{w:BigInt(w),q:0,tag:`${name}:${j}`}]);
  const f=base([1,4,4],"f"), g=base([2,5,2],"g");
  function corr(packet,r) {
    let re=0n, im=0n;
    for(let j=0;j+r<packet.length;j++) {
      for(const u of packet[j]) for(const v of packet[j+r]) {
        let q=pos(u.q-v.q), w=u.w*v.w;
        re += w*R[q]; im += w*I[q];
      }
    }
    return [re,im];
  }
  const eq = (a,b) => a[0]===b[0] && a[1]===b[1];
  function conv(packet,h) {
    let out=Array.from({length:packet.length+h.length-1},()=>[]);
    for(let j=0;j<packet.length;j++)
      for(let k=0;k<h.length;k++)
        for(const u of packet[j])
          out[j+k].push({w:u.w*h[k].w,q:pos(u.q+h[k].q),tag:`${u.tag}|h${k}`});
    return out;
  }
  function externalRaw(packet,r,p) {
    let total=0n;
    for(let j=0;j<packet.length+r;j++){
      let branches=[];
      if(j<packet.length) for(const u of packet[j]) branches.push(u);
      if(j>=r && j-r<packet.length)
        for(const u of packet[j-r]) branches.push({w:u.w,q:pos(u.q+p+2),tag:u.tag+"|shift"});
      for(const u of branches) for(const v of branches)
        total += u.w*v.w*R[pos(u.q-v.q)];
    }
    return total;
  }
  function E(packet,r,p) {
    let m=corr(packet,0);
    if(m[1]!==0n||m[0]<=0n)throw Error("invalid BRC mass");
    // Stage50 ten external ports: 10*(BRC output mass/36)/(2*BRC input mass).
    return {n:5n*externalRaw(packet,r,p),d:36n*m[0]};
  }
  const fractionEq=(a,b)=>a.n*b.d===b.n*a.d;
  const gcd=(a,b)=>b===0n?(a<0n?-a:a):gcd(b,a%b);
  const formatted = o => {let d=gcd(o.n,o.d);return `${o.n/d}/${o.d/d}`;};
  const originalF=Array.from({length:3},(_,r)=>corr(f,r).map(String));
  const originalG=Array.from({length:3},(_,r)=>corr(g,r).map(String));
  if(JSON.stringify(originalF)!==JSON.stringify(originalG)||
      originalF[0][0]!=="33"||originalF[1][0]!=="20"||originalF[2][0]!=="4")
    throw Error("initial homometry failed");
  let filterCases=0, correlationComparisons=0, readoutComparisons=0, rawReadouts=0;
  let sample=null;
  for(let len=1;len<=3;len++){
    const choices=8**len;
    for(let t=0;t<choices;t++){
      let q=t, h=[];
      for(let k=0;k<len;k++){
        const digit=q%8; q=Math.floor(q/8);
        h.push({w:digit>=4?2n:1n,q:digit%4});
      }
      const af=conv(f,h),ag=conv(g,h);
      if(af.length!==ag.length) throw Error("shape mismatch");
      for(let r=0;r<af.length;r++){
        let cf=corr(af,r), cg=corr(ag,r);
        if(!eq(cf,cg))throw Error(`filter correlation mismatch len=${len},digit=${t},r=${r}`);
        correlationComparisons++;
      }
      for(let r=1;r<af.length;r++)for(let p=0;p<4;p++){
        const x=E(af,r,p),y=E(ag,r,p);
        rawReadouts+=2;
        if(!fractionEq(x,y)) throw Error(`BRC readout mismatch len=${len},digit=${t},r=${r},p=${p}`);
        readoutComparisons++;
      }
      if(len===2 && h[0].w===1n && h[0].q===0 &&
          h[1].w===1n && h[1].q===0)
        sample={filter:"(1,1)",C:[0,1,2,3].map(r=>corr(af,r)[0].toString()),
          external_r1_p0:formatted(E(af,1,0))};
      filterCases++;
    }
  }
  if(filterCases!==584 || correlationComparisons!==2840 ||
      readoutComparisons!==9024 || rawReadouts!==18048)
    throw Error("unexpected exhaustive coverage counts");
  if(!sample || JSON.stringify(sample.C)!==JSON.stringify(["106","77","28","4"]))
    throw Error("positive-filter witness failed");
  const flip0 = p=>p.map((x,j)=>x.map(u=>({...u,q:j===0?pos(u.q+2):u.q})));
  const maskedF=formatted(E(flip0(f),1,0));
  const maskedG=formatted(E(flip0(g),1,0));
  if(maskedF!=="35/198" || maskedG!=="5/18")
    throw Error("source-local gate witness failed");
  // A two-round observer-adaptive filter selection; proof covers arbitrarily many rounds.
  let adaptiveChecks=0;
  for(const h1 of [[{w:1n,q:0},{w:1n,q:0}],
                    [{w:1n,q:0},{w:1n,q:1}],
                    [{w:2n,q:3},{w:1n,q:0}],
                    [{w:1n,q:2},{w:2n,q:1}]]){
    let a1=conv(f,h1),b1=conv(g,h1), e1=E(a1,1,0),e2=E(b1,1,0);
    if(!fractionEq(e1,e2))throw Error("adaptive first observation mismatch");
    let branch=(5n*e1.n>e1.d);
    const h2=branch?[{w:1n,q:0},{w:1n,q:1}]:[{w:1n,q:0},{w:2n,q:0}];
    let a2=conv(a1,h2),b2=conv(b1,h2);
    for(let r=1;r<a2.length;r++)for(let p=0;p<4;p++){
      if(!fractionEq(E(a2,r,p),E(b2,r,p)))throw Error("adaptive second observation mismatch");
      adaptiveChecks++;
    }
  }
  return {status:"PREFIX281_EXACT_C4_BRC_CONVOLUTION_NO_GO_PASS",
    source_model:"ordered positive rational C4 paths; source labels and filter-branch provenance retained",
    filter_scope:"every nonzero length-1/2/3 source filter with each coefficient w∈{1,2}, phase∈Z/4",
    filter_cases:filterCases, full_raw_correlation_equalities:correlationComparisons,
    stage50_external_readout_equalities:readoutComparisons,
    direct_brc_port_readouts:rawReadouts, two_round_adaptive_readout_equalities:adaptiveChecks,
    initial_C0_C1_C2:["33","20","4"], positive_filter_example:sample,
    source_local_flip_witness:{E_f:maskedF,E_g:maskedG,distinguishes:true},
    limits:["Finite exhaustive filter family; unbounded convolution closure proved algebraically, not by enumeration.",
      "This verifier evaluates formal C4 BRC source path-pairs, not the original Stage50 Python package.",
      "Convolution and source-selective U0 are conditional candidate operations, not validated full-H_n physical gates.",
      "The original Stage50 source package was not rerun in this check."]};
};
console.log(JSON.stringify(verifyPrefix281(), null, 2));
