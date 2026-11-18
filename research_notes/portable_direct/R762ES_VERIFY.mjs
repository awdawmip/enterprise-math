/* R762ES — exact BigInt BRC group-ring certificate. Run: node R762ES_VERIFY.mjs */
function verify(){
const Q=9,dim=729,lastN=407,branches=[[0,0,0],[1,0,0],[0,0,1],[1,1,0],[0,1,1],[1,1,1]];
const idx=(x,y,z)=>(((x%Q)*Q+(y%Q))*Q+(z%Q));
const powers=Array.from({length:9},(_,e)=>{let v=Array(6).fill(0);if(e<6)v[e]=1;else {v[e-6]=-1;v[e-3]=-1;}return v;});
let spectra=new Map();
for(let i=0;i<9;i++)for(let j=0;j<9;j++)for(let k=0;k<9;k++){let terms=[0,i,k,i+j,j+k,i+j+k],v=Array(6).fill(0);for(let e of terms)for(let h=0;h<6;h++)v[h]+=powers[e%9][h];let key=v.join(",");spectra.set(key,(spectra.get(key)||0)+1);}
if(spectra.size!==127||spectra.get("0,0,0,0,0,0")!==60)throw Error("spectral count");
const perms=branches.map(([a,b,c])=>{let p=[];for(let x=0;x<9;x++)for(let y=0;y<9;y++)for(let z=0;z<9;z++)p.push(idx(x+a,y+b,z+c));return p;});
let A=Array(dim).fill(0n);A[0]=1n;
let residues=new Map(),base=[],early=[],counts=[0,0,0],minSupport=[729,729,729],minAt=[null,null,null],mass=1n;
for(let n=0;n<=lastN;n++){
 if(A.reduce((s,v)=>s+v,0n)!==mass)throw Error("mass "+n);
 if(n<9){let witness=A.findIndex(v=>v%3n!==0n);if(witness<0)throw Error("early "+n);early.push({n,witness});}
 else{
  let k=Math.floor(n/3),factor=3n**BigInt(k-2),v=new Uint8Array(dim),support=0;
  for(let j=0;j<dim;j++){if(A[j]%factor!==0n)throw Error("lower "+n);v[j]=Number((A[j]/factor)%3n);if(v[j])support++;}
  if(!support)throw Error("upper "+n);let r=n%3;
  if(support<minSupport[r]){minSupport[r]=support;minAt[r]=n;}
  if(n<=26)base.push({n,support});
  if(n>=27){let old=residues.get(n-18);if(!old)throw Error("old missing");for(let j=0;j<dim;j++)if(v[j]!==old[j])throw Error("period "+n);counts[r]++;}
  residues.set(n,v);if(n>26)residues.delete(n-18);
 }
 if(n<lastN){let B=Array(dim).fill(0n);for(let p of perms)for(let j=0;j<dim;j++)if(A[j]!==0n)B[p[j]]+=A[j];A=B;mass*=6n;}
}
if(counts.some(c=>c!==127))throw Error("wrong checks");
return {schema:"R762ES_Q9_SHORT_CERTIFICATE_V1",modulus:9,positions:729,branches,character_eigenvalues:127,zero_characters:60,checked_n:[0,lastN],recurrence_order_bound:127,base_k:[3,129],period_k:6,period_n:18,exact_vector_comparisons:counts,total_comparisons:381,initial_residue_supports:base,early_mod3_witness_indices:early,min_support_by_r:minSupport,min_support_at_n:minAt,arithmetic:"exact six-named positive BRC path-count BigInt convolution; integer cyclotomic six-vector normalization",independent_review:"NOT_REVIEWED",result:"PASS"};
}
console.log(JSON.stringify(verify(),null,2));
