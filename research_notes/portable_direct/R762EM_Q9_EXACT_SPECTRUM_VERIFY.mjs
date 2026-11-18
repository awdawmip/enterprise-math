// R762EM: all integer arithmetic; complete 729-character enumeration.
// Run: node R762EM_Q9_EXACT_SPECTRUM_VERIFY.mjs
const certificate=(function compute(){
 const Q=9,D=6,U=[1,2,4,5,7,8];
 const zero=()=>[0,0,0,0,0,0], one=[1,0,0,0,0,0];
 const equal=(a,b)=>a.every((x,i)=>x===b[i]);
 const assert=(b,m)=>{if(!b)throw new Error(m)};
 const zpow=(n)=>{n=((n%Q)+Q)%Q;const r=zero();if(n<D){r[n]=1}else{r[n-6]-=1;r[n-3]-=1}return r};
 const Z=Array.from({length:Q},(_,i)=>zpow(i));
 const add=(a,b)=>a.map((v,i)=>v+b[i]);
 const neg=a=>a.map(v=>-v);
 const mul=(a,b)=>{const c=Array(11).fill(0);for(let i=0;i<D;i++)for(let j=0;j<D;j++)c[i+j]+=a[i]*b[j];for(let k=10;k>=6;k--){const v=c[k];c[k]=0;c[k-3]-=v;c[k-6]-=v}return c.slice(0,D)};
 const chr=(i,j,k)=>{const es=[0,i,k,i+j,j+k,i+j+k],r=zero();for(let e of es){let z=Z[e%Q];for(let b=0;b<D;b++)r[b]+=z[b]}return r};
 const aut=(a,u)=>{let r=zero();for(let i=0;i<D;i++)if(a[i])r=add(r,Z[(i*u)%Q].map(v=>v*a[i]));return r};
 const key=a=>a.join(','), unkey=s=>s.split(',').map(Number);
 const cmp=(a,b)=>{for(let i=0;i<a.length;i++){if(a[i]!==b[i])return a[i]-b[i]}return 0};
 const counts=new Map();
 for(let i=0;i<Q;i++)for(let j=0;j<Q;j++)for(let k=0;k<Q;k++){const v=key(chr(i,j,k));counts.set(v,(counts.get(v)||0)+1)}
 assert(counts.size===127,"127 distinct values");assert(counts.get(key(zero()))===60,"zero multiplicity");
 for(let i=0;i<Q;i++)for(let j=0;j<Q;j++)assert(equal(mul(Z[i],Z[j]),Z[(i+j)%Q]),"ring table");
 const left=new Set(counts.keys()),cert=[];
 const evalpoly=(pol,root)=>{let result=zero();for(let i=pol.length-1;i>=0;i--)result=add(mul(result,root),[pol[i],0,0,0,0,0]);return result};
 while(left.size){
  const rep=Array.from(left).map(unkey).sort(cmp)[0],orbit=new Map();
  for(let u of U){const v=aut(rep,u);orbit.set(key(v),v)}
  const roots=Array.from(orbit.values()).sort(cmp);
  for(let r of roots){assert(left.has(key(r)),"unassigned orbit");assert(counts.get(key(r))===counts.get(key(rep)),"Galois multiplicity")}
  let p=[one];
  for(let root of roots){const next=Array.from({length:p.length+1},zero);for(let h=0;h<p.length;h++){next[h]=add(next[h],neg(mul(root,p[h])));next[h+1]=add(next[h+1],p[h])}p=next}
  assert(p.every(v=>v.slice(1).every(n=>n===0)),"factor in Z[T]");
  const co=p.map(v=>v[0]);assert(co[co.length-1]===1&&co.length===roots.length+1,"monic");
  for(let r of roots){assert(equal(evalpoly(co,r),zero()),"factor not vanishing");left.delete(key(r))}
  cert.push({representative:rep,degree:roots.length,multiplicity:counts.get(key(rep)),polynomial_low_to_high:co});
 }
 cert.sort((a,b)=>a.degree-b.degree||cmp(a.representative,b.representative));
 const degs={};for(let r of cert)degs[r.degree]=(degs[r.degree]||0)+1;
 const totalDistinct=cert.reduce((s,r)=>s+r.degree,0),totalSpectral=cert.reduce((s,r)=>s+r.degree*r.multiplicity,0);
 const trace=zero();for(let [s,m] of counts){let v=unkey(s);for(let j=0;j<D;j++)trace[j]+=m*v[j]}
 assert(JSON.stringify(degs)===JSON.stringify({'1':3,'2':2,'3':4,'6':18}),"orbit degrees");
 assert(totalDistinct===127&&totalSpectral===729,"dimensions");assert(equal(trace,[729,0,0,0,0,0]),"trace");
 return {schema:"R762EM_Q9_EXACT_SPECTRAL_CERTIFICATE_V1",model:"P=1+X+Z+XY+YZ+XYZ in Z[(Z/9)^3]",ring:"Z[zeta_9]/(zeta_9^6+zeta_9^3+1)",characters_enumerated:729,distinct_eigenvalues:totalDistinct,zero_eigenvalue_multiplicity:60,galois_orbit_count:cert.length,degree_histogram:degs,minimal_polynomial_degree:totalDistinct,characteristic_polynomial_degree:totalSpectral,trace_of_operator:trace[0],factor_convention:"Each monic irreducible F_O(T) from polynomial_low_to_high; charpoly=prod(F_O^multiplicity); minpoly=prod(F_O).",factors:cert,review:"AUTHOR_EXACT_FINITE_CERTIFICATE_NOT_INDEPENDENTLY_REVIEWED"}
})();
console.log(JSON.stringify(certificate,null,2));
