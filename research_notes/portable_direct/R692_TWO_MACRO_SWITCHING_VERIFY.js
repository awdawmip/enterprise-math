// Enterprise Math R692, portable exact native X6/BRC source-path certificate.
// Node 18+ or ECMAScript, exact 32-bit-size integer counts, no dependencies.
// Freeze a72226e2430ffa4786321ac86e7f0c599d5f0389, R691 df5c9edbb18b123a828e3e6ead2a1a0f606511a5.
const verifyR692 = function verifyR692(){
 const G=[];const perms=(pre,rest)=>{if(!rest.length){G.push(pre.join(""));return;}for(const d of rest)perms([...pre,d],rest.filter(x=>x!==d));};perms([],["0","1","2"]);
 const SIGN=[[-1,-1],[-1,1],[1,-1],[1,1]],names=["--","-+","+-","++"];
 const T={"0,0":"012","1,0":"013","2,0":"014","0,1":"023","1,1":"123","2,1":"013"};
 const mod=(n,m)=>((n%m)+m)%m,phase=z=>[mod(z[0]+z[2]+z[4],3),mod(z[1]+z[3]+z[5],2)];
 const mul=(q,p)=>p.split("").map(t=>q[+t]).join(""),inverse=p=>["0","1","2"].map(t=>String(p.indexOf(t))).join("");
 const add=(C,g,n=1)=>{C[g]=(C[g]||0)+n;},sum=C=>Object.values(C).reduce((a,b)=>a+b,0);
 const eq=(x,y)=>JSON.stringify(Object.entries(x).sort())===JSON.stringify(Object.entries(y).sort());
 const square=(a,b,i,j,si,sj)=>{let z=[a,b,0,0,0,0],origin=z.join(","),root=T[phase(z).join(",")],frame=root;
   for(const [ax,d] of [[i,si],[j,sj],[i,-si],[j,-sj]]){
     const prior=T[phase(z).join(",")];z[ax]+=d;const next=T[phase(z).join(",")];
     const rem=prior.split("").filter(t=>!next.includes(t)),plus=next.split("").filter(t=>!prior.includes(t));
     if(rem.length!==1||plus.length!==1)throw Error("invalid E* frame step");
     frame=frame.split("").map(t=>t===rem[0]?plus[0]:t).join("");
   }
   if(z.join(",")!==origin)throw Error("Cell not returned");
   return frame.split("").map(t=>String(root.indexOf(t))).join("");
 };
 const table=[
 [{"012":6,"021":9},{"012":6,"021":6,"120":3},{"012":6,"021":3,"201":6},{"012":6,"120":3,"201":6}],
 [{"012":6,"120":6,"201":3},{"012":9,"120":6},{"012":12,"201":3},{"012":15}],
 [{"012":15},{"012":12,"021":3},{"012":9,"021":6},{"012":6,"021":9}]
 ];
 const closure=C=>{const seen=new Set(["012"]),stack=["012"];while(stack.length){const p=stack.pop();for(const q of Object.keys(C)){const r=mul(q,p);if(!seen.has(r)){seen.add(r);stack.push(r);}}}return [...seen].sort();};
 const conv=(after,before)=>{const R={};for(const [q,x] of Object.entries(after))for(const [p,y] of Object.entries(before))add(R,mul(q,p),x*y);return R;};
 const gcd=(x,y)=>{while(y){let z=x%y;x=y;y=z;}return x;};
 let paths=0,bChecks=0,pairs=0,entries=0,zeros=0,nontrivial=0,phaseResults={};
 for(let a=0;a<3;a++){
   let base=null;
   for(let b=0;b<2;b++){
     let current=SIGN.map(()=>({}));
     for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let s=0;s<4;s++){let [x,y]=SIGN[s];add(current[s],square(a,b,i,j,x,y));paths++;}
     for(let s=0;s<4;s++)if(!eq(current[s],table[a][s])||sum(current[s])!==15)throw Error("R691 source-table disagreement");
     if(b===0)base=current;else{for(let s=0;s<4;s++)if(!eq(base[s],current[s]))throw Error("b-invariance");bChecks+=60;}
   }
   const laws={};for(let mask=1;mask<=15;mask++){const c={};for(let s=0;s<4;s++)if(mask&(1<<s))for(const [g,n] of Object.entries(base[s]))add(c,g,n);laws[mask]=c;}
   const rec=[];let worst=null,proper=0,zeroPairs=0;
   for(let U=1;U<=15;U++)for(let V=1;V<=15;V++){
     const A=laws[U],B=laws[V],joined={...A};for(const [g,n] of Object.entries(B))add(joined,g,n);
     const H=closure(joined),N=sum(A)*sum(B),joint=conv(B,A);if(sum(joint)!==N)throw Error("mass");
     const columns={};
     for(const p of H){
       const pinv=inverse(p);columns[p]={};
       for(const r of H){
         const n=joint[mul(r,pinv)]||0;let independent=0;
         for(const mid of H)independent+=(A[mul(mid,pinv)]||0)*(B[mul(r,inverse(mid))]||0);
         if(n!==independent)throw Error("direct-matrix discrepancy");
         columns[p][r]=n;entries++;
       }
       if(sum(columns[p])!==N)throw Error("column not conservative");
     }
     let biggest=-1,witness=[];
     for(const p of H)for(const q of H){
       let d=0;for(const r of H)d+=Math.abs(columns[p][r]-columns[q][r]);
       if(d>biggest){biggest=d;witness=[p,q];}
     }
     if(biggest>=2*N)throw Error("zero overlap / no contraction");
     const div=gcd(biggest,2*N),numberZero=H.filter(g=>!(joint[g]||0)).length;
     if(numberZero){zeros++;zeroPairs++;}if(H.length>1)nontrivial++;
     const row=[U,V,H.length,biggest/div,2*N/div,numberZero,witness[0],witness[1],biggest,N];
     rec.push(row);pairs++;
     if(!worst||row[3]*worst[4]>worst[3]*row[4])worst=row;
     if(H.length<[6,3,2][a])proper++;
   }
   const max=[[23,25],[9,10],[4,5]][a];if(rec.length!==225||worst[3]*max[1]!==worst[4]*max[0])throw Error("incorrect exact maximum");
   phaseResults[a]={rows:rec,sharp_max:worst,proper_subgroup_pairs:proper,zero_support_pairs:zeroPairs};
 }
 if(paths!==360||bChecks!==180||pairs!==675||entries!==10955||zeros!==24||nontrivial!==673)throw Error("coverage");
 return {schema:"EM_R692_ESTAR_TWO_MACRO_EXACT_CERTIFICATE_V1",
   frozen_task_source:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
   prior_model_commit:"df5c9edbb18b123a828e3e6ead2a1a0f606511a5",
   mask_legend:names.map((x,i)=>[1<<i,x]),
   row_columns:["first_mask","second_mask","generated_subgroup_order","delta_numerator","delta_denominator","zero_group_values","argmax_p","argmax_q","max_l1_numerator","two_macro_labeled_paths"],
   phases:phaseResults,
   checks:{original_four_step_paths:paths,b_phase_path_checks:bChecks,ordered_mask_pairs:pairs,independent_matrix_entry_checks:entries,nontrivial_groups:nontrivial,two_macro_zero_support_pairs:zeros,status:"ALL_EXACT_CHECKS_PASS"}};
};
const result=verifyR692();
if (typeof process!=="undefined" && process.stdout) process.stdout.write(JSON.stringify(result)+"\n");
