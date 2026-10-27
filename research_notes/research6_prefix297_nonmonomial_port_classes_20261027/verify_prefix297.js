// PREFIX-297; typed exact Z[i] ordered-source-pair BRC; no native H_n claim.
const c=(x,y=0)=>[BigInt(x),BigInt(y)], z=c(0), o=c(1), i=c(0,1);
const add=(a,b)=>[a[0]+b[0],a[1]+b[1]], neg=a=>[-a[0],-a[1]],
 mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],
 co=a=>[a[0],-a[1]], norm=a=>a[0]*a[0]+a[1]*a[1],
 sum=a=>a.reduce(add,z),eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
const mat=a=>a.map(row=>row.map(v=>Array.isArray(v)?c(...v):c(v)));
const M=mat([[[6,3],[-1,-1],1],[[1,1],[-5,-2],[-4,-1]],[0,-1,[5,-2]]]);
const N=mat([[[2,1],[-1,-1],[5,2]],[[1,1],[-5,-2],[-4,-1]],[[6,-2],-1,-1]]);
const S=mat([[1,0,-1],[0,0,0],[-1,0,1]]),H=mat([[3,-1,0],[-1,2,1],[0,1,3]]);
const gram=rows=>Array.from({length:3},(_,j)=>Array.from({length:3},(_,k)=>sum(rows.map(r=>mul(co(r[j]),r[k])))));
const same=(a,b)=>JSON.stringify(a.map(r=>r.map(t=>t.map(String))))===JSON.stringify(b.map(r=>r.map(t=>t.map(String))));
const G=H.map((r,j)=>r.map((h,k)=>add(mul(c(16),h),neg(S[j][k]))));
if(!same(gram(M),G)||!same(gram(N),G)||!same(gram([mat([[1,0,-1]])[0]]),S))throw Error('G/S');
const A=mat([[1,0,[2,2]],[0,3,0],[[2,-2],0,-1]]);
const matrixProduct=(a,b)=>a.map(row=>[0,1,2].map(k=>sum(row.map((x,j)=>mul(x,b[j][k])))));
const adj=a=>[0,1,2].map(j=>[0,1,2].map(k=>co(a[k][j])));
if(!same(matrixProduct(adj(A),A),mat([[9,0,0],[0,9,0],[0,0,9]]))||
   !same(matrixProduct(A,M),N.map(row=>row.map(t=>mul(c(3),t)))))throw Error('U3');
const rowNorms=rows=>rows.map(r=>sum(r.map(x=>c(norm(x))))[0].toString()).sort();
if(rowNorms(M).join()!=['30','48','48'].join()||rowNorms(N).join()!=['36','42','48'].join())throw Error('left orbit');
const B=mat([[1,[1,1],1],[[1,-1],0,[-1,1]],[1,[-1,-1],1]]);
if(!same(matrixProduct(adj(B),B),mat([[4,0,0],[0,4,0],[0,0,4]])))throw Error('U4');
const W={
 1:mat([[[6,2],-3,[-2,-1]],[[2,2],[2,-1],[3,4]],[0,[-4,1],[-1,4]]]),
 2:mat([[[6,2],-1,[2,-1]],[[2,2],[-2,-3],-5],[0,[-4,-1],[-1,-4]]]),
 5:mat([[[6,3],[-1,-1],1],[1,-3,[-3,5]],[1,[-4,2],[-3,-2]]]),
 6:mat([[[6,2],[-2,1],-1],[[2,1],[0,-5],[1,-3]],[[1,1],-1,[1,6]]])};
let witnessed=1; const classes=[];
for(const [type,old] of Object.entries(W)){
 const twice=matrixProduct(B,old);
 if(twice.some(row=>row.some(x=>x[0]%2n||x[1]%2n)))throw Error('nonintegral');
 const fresh=twice.map(row=>row.map(x=>[x[0]/2n,x[1]/2n]));
 if(!same(gram(old),gram(fresh))||rowNorms(old).join()===rowNorms(fresh).join())throw Error('orbit type '+type);
 witnessed++;classes.push({type,row_norms_original:rowNorms(old),row_norms_new:rowNorms(fresh)});
}
classes.push({type:'3',row_norms_original:rowNorms(M),row_norms_new:rowNorms(N)});
classes.sort((x,y)=>Number(x.type)-Number(y.type));
const alphabet=[z,o,c(-1),i,c(0,-1),c(1,1)],phases=[o,i,c(-1),c(0,-1)];
let cases=0,bins=0,pairs=0,gramChecks=0;
function brc(row,a){const legs=row.map((r,j)=>mul(r,a[j]));let m=z;
 for(let j=0;j<3;j++)for(let k=0;k<3;k++){m=add(m,mul(co(legs[j]),legs[k]));pairs++;}
 bins++;if(m[1]||m[0]!==norm(sum(legs)))throw Error('BRC mass');return m[0];}
for(const q of phases){const d=[o,q,mul(q,q)],E=[[c(4),mul(c(4),q),z],[z,c(-4),mul(c(4),q)]];
 for(const [label,R] of [['M',M],['N',N]]){
  const rows=R.map(r=>r.map((x,j)=>mul(x,d[j]))), L=[[o,z,neg(d[2])]], full=[...E,...rows,...L], gg=gram(full);
  for(let j=0;j<3;j++)for(let k=0;k<3;k++){if(!eq(gg[j][k],c(j===k?64:0)))throw Error('full Gram');gramChecks++;}
  for(const a of alphabet)for(const b of alphabet)for(const h of alphabet){const input=[a,b,h],out=full.map(r=>brc(r,input));
   if(out.reduce((u,v)=>u+v,0n)!==64n*input.reduce((u,v)=>u+norm(v),0n))throw Error('total mass');
   if(eq(q,o)&&eq(a,o)&&eq(b,z)&&eq(h,z)){
    const correct=label==='M'?[45n,2n,0n]:[5n,2n,40n];
    if(out[0]!==16n||out[1]!==0n||out[5]!==1n||correct.some((v,j)=>out[j+2]!==v))throw Error('port witness');}
   cases++;
  }
 }
}
if(cases!==1728||bins!==10368||pairs!==93312||gramChecks!==72||witnessed!==5)throw Error('count');
console.log(JSON.stringify({schema:'EM_PREFIX297_EXACT_BRC_JS_V1',status:'PASS',C4_phases:4,alphabet_size:6,inputs_per_phase:216,construction_count:2,case_count:cases,direct_BRC_bin_readouts:bins,ordered_source_pair_terms:pairs,Gram_entry_checks:gramChecks,nonunique_S_types_lower_bound:witnessed,classes,port_mass_e0_over_64:{event:[16,0],retained_M:[45,2,0],retained_N:[5,2,40],leak:[1]},native_Hn_checked:false},null,2));
