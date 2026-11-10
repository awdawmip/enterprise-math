/* R700 exact positive-BRC candidate -> V29 typed PASS ring finite certificate.
   Execution: node R700_V29_BRC_RING_VERIFY.js. No physical X6 admission. */
const result=(function certify() {
  const N=[24,18,6,12], R=[[0,1],[1,2],[2,3],[3,0]];
  const fibers=new Map(), signatures=new Set();
  let states=0;
  for(let e=0;e<=N[0];e++)for(let t=0;t<=N[1];t++)
  for(let c=0;c<=N[2];c++)for(let z=0;z<=N[3];z++){
    const v=[e,t,c,z],s=e+t+c+z;if(!s)continue;
    const M=Array.from({length:4},()=>[0,0,0,0]);
    for(let j=0;j<4;j++)for(let k=1;k<=v[j];k++){
      const [a,b]=R[j];M[a][b]++; // distinct positive-BRC token (j,k) -> one V29 PASS
    }
    const u=Array.from({length:4},(_,i)=>M[i].reduce((a,b)=>a+b,0)-M.reduce((a,row)=>a+row[i],0));
    const inverse=(s+u[0]-2*u[1]-u[2])/4;
    const w=[inverse,inverse+u[1],inverse+u[1]+u[2],inverse-u[0]];
    if(w.some((x,i)=>x!==v[i])||u.reduce((a,b)=>a+b,0)!==0||
      M.reduce((a,row)=>a+row.reduce((x,y)=>x+y,0),0)!==s||
      (s-(2*u[1]+u[2]-u[0]))%4!==0)throw Error("V29 PASS ring failed");
    const key=u.join(",");
    if(!fibers.has(key))fibers.set(key,[]);
    fibers.get(key).push(v);
    const sig=key+"|"+s;
    if(signatures.has(sig))throw Error("contrast/total collision");
    signatures.add(sig);states++;
  }
  if(states!==43224||fibers.size!==12121)throw Error("population/fibers");
  const maxFiber=Math.max(...[...fibers.values()].map(v=>v.length));
  const witness=Array.from({length:7},(_,k)=>[k+1,k,k,k]);
  if(maxFiber!==7||!witness.every(v=>fibers.get("1,-1,0,0").some(x=>x.join()==v.join())))
    throw Error("fiber sharpness");
  return {schema:"EM_R700_V29_BRC_RING_V1",status:"R700_EXACT_BRC_V29_RING_PASS",
    capacities:N,ring_arcs:R,histograms_checked:states,unique_count_plus_contrast:signatures.size,
    contrast_fiber_count:fibers.size,max_contrast_fiber:maxFiber,
    worst_case_additional_bits:3,witness_contrast:[1,-1,0,0],
    seven_witness_histograms:witness,seven_witness_totals:witness.map(v=>v.reduce((a,b)=>a+b,0)),
    decoder:"e=(s+u0-2*u1-u2)/4; t=e+u1; c=e+u1+u2; z=e-u0",
    modulus:"s ≡ 2u1+u2-u0 (mod 4)",
    sharp_noise:"Given exact u, |s_measured-s|<2 suffices; s=1 and s=5 share u and meet at measured s=3 at error 2",
    scope:"Positive BRC E* candidate group tokens encoded as syntactic V29 PASS ring; genuine X6 Link/Port and V39 legal-loop lifting pending."};
})();
console.log(JSON.stringify(result,null,2));
