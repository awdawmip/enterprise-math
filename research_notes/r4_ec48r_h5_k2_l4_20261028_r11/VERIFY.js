"use strict";
// Exact support verification for EC48R; run: node VERIFY.js
// Advantage uses 1/64 units; tauP+tauQ uses 1/16 units.
const verifySharp = function verifySharp() {
  const words=[[0,0],[0,1],[1,0],[1,1]], dens=[128,64,32];
  const p=[],q=[];
  for(const w of words){
    p.push(16,8);q.push(8,16);
    for(const bit of w){if(bit){p.push(3,1);q.push(1,3)}else{p.push(4);q.push(4)}}
  }
  if(p.length!==20||p.reduce((a,b)=>a+b,0)!==128||q.reduce((a,b)=>a+b,0)!==128||p.some(x=>x<=0)||q.some(x=>x<=0))throw Error("mass failure");
  const gcd=(a,b)=>b?gcd(b,a%b):Math.abs(a);
  const frac=(n,d)=>{const g=gcd(n,d);return d/g===1?String(n/g):`${n/g}/${d/g}`};
  const fullMax=dens.map(()=>-Infinity),threeMax=dens.map(()=>-Infinity);
  let nF=0,n3=0;
  function compare(a,t,dests){for(let i=0;i<dens.length;i++){let value=dens[i]*a-4*t;if(value>dests[i])dests[i]=value}}
  for(let group=0;group<4;group++)for(let ct=0;ct<16;ct++)for(let mask=0;mask<256;mask++){
    let a=0,t=64+16*((group&1)?1:0)+16*((group&2)?1:0);
    for(let i=0;i<4;i++){
      if(!(group&(1<<(i>>1)))||!(ct&(1<<i)))continue;
      a+=4;t+=8;
      for(let j=0;j<2;j++)if(mask&(1<<(2*i+j))){t++;a+=words[i][j]}
    }
    compare(a,t,fullMax);nF++;
  }
  for(let group=0;group<4;group++)for(let code=0;code<256;code++)for(let mask=0;mask<64;mask++){
    let a=0,t=64+16*((group&1)?1:0)+16*((group&2)?1:0),qcode=code,labels=[];
    for(let i=0;i<4;i++){labels.push((qcode%4)-1);qcode=Math.floor(qcode/4)}
    for(let i=0;i<4;i++){
      const label=labels[i];
      if(!(group&(1<<(i>>1)))||label<0)continue;
      a+=4;t+=8;
      for(let j=0;j<2;j++)if(mask&(1<<(2*label+j))){t++;a+=words[i][j]}
    }
    compare(a,t,threeMax);n3++;
  }
  if(nF!==16384||n3!==65536)throw Error("coverage failure");
  const tested=dens.map((D,i)=>{
    if(fullMax[i]!==20*D-528||threeMax[i]!==20*D-532)throw Error("exact formula failure");
    return {c:frac(1,D),full:frac(fullMax[i],64*D),three_states:frac(threeMax[i],64*D),gap:frac(fullMax[i]-threeMax[i],64*D)}
  });
  return {schema:"ENTERPRISE_MATH_EC48R_EXACT_SUPPORT_V1",terminal_leaves:20,positive:true,p_mass:"128/128",q_mass:"128/128",three_state_policies:n3,full_policies:nF,tested,analytic_real_interval:"0<c<=1/32",analytic_full:"5/16-33*c/4",analytic_3state:"5/16-133*c/16",analytic_gap:"c/16",arithmetic:"integer numerator support; fractions reduced by gcd",admission:"AUTHOR_PROVED / EXACT_COMPUTATION_PASS / UNREVIEWED / NOT_ADMITTED"};
};
console.log(JSON.stringify(verifySharp(),null,2));
