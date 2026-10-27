'use strict';
// Exact rational verification. node VERIFY.js
const result=(function verify(){
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b!==0n){let t=a%b;a=b;b=t}return a};
  class F{constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denom");if(d<0n){n=-n;d=-d}let g=gcd(n,d);this.n=n/g;this.d=d/g}add(x){return new F(this.n*x.d+x.n*this.d,this.d*x.d)}sub(x){return new F(this.n*x.d-x.n*this.d,this.d*x.d)}mul(x){return new F(this.n*x.n,this.d*x.d)}div(x){return new F(this.n*x.d,this.d*x.n)}eq(x){return this.n===x.n&&this.d===x.d}str(){return this.d===1n?String(this.n):this.n+"/"+this.d}}
  const f=(n,d=1)=>new F(n,d), sum=arr=>arr.reduce((a,b)=>a.add(b),f(0));
  const eq=(a,b,msg)=>{if(!a.eq(b))throw Error(msg+": "+a.str()+" != "+b.str())};
  const P=[[f(1,4),f(1,4),f(1,2)],[f(1,12),f(3,4),f(1,6)],[f(1,6),f(1,2),f(1,3)]];
  const r=[f(2),f(1),f(1,2)], pi=f(1,3);
  const Q=P.map(row=>row.map((x,j)=>x.mul(r[j])));
  for(const row of P.concat(Q)){eq(sum(row),f(1),"row normalization");if(!row.every(x=>x.n>0n))throw Error("non-positive cell")}
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)eq(Q[i][j].div(P[i][j]),r[j],"LR");
  const ap=r.map((_,j)=>sum(P.map(row=>row[j])).mul(pi));
  const aq=r.map((_,j)=>sum(Q.map(row=>row[j])).mul(pi));
  ["1/6","1/2","1/3"].forEach((s,j)=>{if(ap[j].str()!==s)throw Error("P marginal")});
  ["1/3","1/2","1/6"].forEach((s,j)=>{if(aq[j].str()!==s)throw Error("Q marginal")});
  function observer(c,d,rows){let m=sum(c).mul(pi);let a=f(0);for(let i=0;i<3;i++)for(let j=0;j<3;j++)a=a.add(pi.mul(c[i]).mul(rows[i][j]).mul(d[i][j]));return [f(1).sub(m),m.sub(a),a]}
  const ones=[f(1),f(0),f(0)];
  const fullD=P.map(_=>[f(1),f(0),f(0)]);
  const fp=observer(ones,fullD,P),fq=observer(ones,fullD,Q);
  const cc=[pi,pi,pi],cd=P.map(_=>[f(1),f(1,4),f(0)]);
  const cp=observer(cc,cd,P),cq=observer(cc,cd,Q);
  const strings=a=>a.map(x=>x.str());
  if(strings(fp).join(",")!=="2/3,1/4,1/12"||strings(fq).join(",")!=="2/3,1/6,1/6")throw Error("full probabilities");
  if(strings(cp).join(",")!=="2/3,17/72,7/72"||strings(cq).join(",")!=="2/3,13/72,11/72")throw Error("compressed probabilities");
  const abs=x=>x.n<0n?new F(-x.n,x.d):x;
  const tv=(a,b)=>sum(a.map((x,i)=>abs(x.sub(b[i])))).div(f(2));
  eq(tv(fp,cp),f(1,72),"TV P");eq(tv(fq,cq),f(1,72),"TV Q");
  const Fscore=(p,q)=>q[2].sub(p[2]).sub(p[1].add(p[2]).div(f(6)));
  eq(Fscore(fp,fq),f(1,36),"full gap");eq(Fscore(cp,cq),f(0),"compressed tight");
  let vertexMax=f(-1);
  for(let mask=0;mask<8;mask++){const d=r.map((_,j)=>f((mask>>j)&1));const v=sum(d.map((x,j)=>aq[j].sub(ap[j]).mul(x)));if(v.n*vertexMax.d>vertexMax.n*v.d)vertexMax=v}
  eq(vertexMax,f(1,6),"cube corners");
  return {status:"PASS_EXACT_BIGINT_RATIONAL",model:"R1_N14_N2_three_symbol_two_law",ordered_prefixes:13,terminal_cube_vertices:8,
    P_J_marginal:strings(ap),Q_J_marginal:strings(aq),
    full_P_T1D0_T2D0_T2D1:strings(fp),full_Q_T1D0_T2D0_T2D1:strings(fq),
    compressed_P_T1D0_T2D0_T2D1:strings(cp),compressed_Q_T1D0_T2D0_T2D1:strings(cq),
    compressed_continue:"1/3",compressed_terminal_D1:["1","1/4","0"],
    full_separator_gap:Fscore(fp,fq).str(),compressed_separator:Fscore(cp,cq).str(),
    cube_max_contrast_per_reach:vertexMax.str(),TV_P:tv(fp,cp).str(),TV_Q:tv(fq,cq).str(),
    sharp_minimax_TV:"1/72",analytic_all_policy_lower_bound:"PROOF.md Lemma 2 + exact support inequality",
    caveat:"Finite arithmetic certificate; universal minimax lower bound derives from written proof; independent review and native X6 transfer pending"};
})();
process.stdout.write(JSON.stringify(result,null,2)+'\n');
