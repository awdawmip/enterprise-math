function verify() {
 const A=x=>x<0n?-x:x,G=(a,b)=>{a=A(a);b=A(b);while(b){let t=a%b;a=b;b=t}return a||1n},R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d}if(d===0n)throw Error("den=0");let g=G(n,d);return [n/g,d/g]};
 const add=(a,b)=>R(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>R(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>R(a[0]*b[0],a[1]*b[1]),div=(a,b)=>R(a[0]*b[1],a[1]*b[0]),eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],str=a=>`${a[0]}/${a[1]}`,Z=R(0),I=R(1),H=R(1,2);
 const S=["AU","AV","BU","BV"],W={AU:{Q:[10n,10n],P:[9n,11n]},AV:{Q:[20n,20n],P:[5n,5n]},BU:{Q:[15n,15n],P:[3n,27n]},BV:{Q:[15n,15n],P:[30n,30n]}};
 const jp=(s,b)=>{const v=W[s][b];return R(v[1],v[0]+v[1])};
 let sumP=0n,sumQ=0n,nleaf=0;
 for(const s of S)for(let j=0;j<2;j++)for(let k=0;k<2;k++){let p=W[s].P[j],q=W[s].Q[j];if(p<=0n||q<=0n)throw Error("zero leaf");sumP+=p;sumQ+=q;nleaf++}
 if(sumP!==240n||sumQ!==240n||nleaf!==16)throw Error("source mass");
 const prep=S.flatMap(s=>["Q","P"].map(b=>[s,b])),epses=[R(0),R(1,8),R(1,4),R(1,2)];
 const push=(m,k,v)=>m.set(k,add(m.get(k)||Z,v)),ident=(a,b)=>{for(const k of new Set([...a.keys(),...b.keys()]))if(!eq(a.get(k)||Z,b.get(k)||Z))return false;return true};
 function Wout(s,b,eps,via4=false){
   const p=jp(s,b),o=new Map();
   if(via4&&s!=="BU"){let q=s==="AV"?Z:s==="BV"?I:p;push(o,"3|P|none",q);push(o,"3|Q|none",sub(I,q));return o}
   for(let j=0;j<2;j++){const a=j?p:sub(I,p),d=s==="BV"||(s==="AU"&&j)||s==="BU"&&j?"P":"Q";
     if(s==="BU")for(let z=0;z<2;z++)push(o,`3|${d}|${z}`,mul(a,z===j?sub(I,eps):eps));
     else push(o,`3|${d}|none`,a);
   }return o
 }
 function rank(A0){
   let a=A0.map(row=>row.map(v=>[...v])),r=0;
   for(let c=0;c<a[0].length;c++){let q=r;while(q<a.length&&a[q][c][0]===0n)q++;if(q===a.length)continue;
     [a[r],a[q]]=[a[q],a[r]];let p=a[r][c];
     for(let j=c;j<a[0].length;j++)a[r][j]=div(a[r][j],p);
     for(let i=0;i<a.length;i++)if(i!==r){let f=a[i][c];if(f[0]!==0n)for(let j=c;j<a[0].length;j++)a[i][j]=sub(a[i][j],mul(f,a[r][j]))}
     r++;if(r===a.length)break
   }return r
 }
 function determinant(M){
   let a=M.map(row=>row.map(v=>[...v])),d=I;
   for(let i=0;i<a.length;i++){let q=i;while(q<a.length&&a[q][i][0]===0n)q++;if(q===a.length)return Z;
     if(q!==i){[a[i],a[q]]=[a[q],a[i]];d=mul(d,R(-1))}
     let v=a[i][i];d=mul(d,v);
     for(let k=i+1;k<a.length;k++){let c=div(a[k][i],v);for(let j=i;j<a.length;j++)a[k][j]=sub(a[k][j],mul(c,a[i][j]))}
   }return d
 }
 let fixed=0,policy=0;const atomOrder=["3|Q|none","3|P|none","3|Q|0","3|Q|1","3|P|0","3|P|1"];
 const classId=(s,j)=>s==="AU"?j:s==="AV"?2:s==="BU"?3+j:5;
 function lawful(s,b,eps,mask){
   const o=new Map(),p=jp(s,b);
   for(let j=0;j<2;j++){let d=(mask>>classId(s,j)&1)?"P":"Q",w=j?p:sub(I,p);
     if(s==="BU")for(let z=0;z<2;z++)push(o,`3|${d}|${z}`,mul(w,z===j?sub(I,eps):eps));
     else push(o,`3|${d}|none`,w);
   }return o
 }
 for(const eps of epses){
   let M=[];
   for(const [s,b] of prep){let a=Wout(s,b,eps),v=Wout(s,b,eps,true);if(!ident(a,v))throw Error("fixed factorization");M.push(atomOrder.map(q=>a.get(q)||Z));fixed++}
   if(rank(M)!==4)throw Error("fixed rank");
   for(let mask=0;mask<64;mask++)for(const [s,b] of prep){
     let z=lawful(s,b,eps,mask),q=lawful(s,s==="AV"||s==="BV"?"Q":b,eps,mask);
     if(!ident(z,q))throw Error("universal factorization");policy++
   }
 }
 const row=prep.map(([s,b])=>[...S.map(v=>v===s?I:Z),s==="AU"?jp(s,b):Z,s==="BU"?jp(s,b):Z]);
 if(rank(row)!==6)throw Error("six-witness rank");
 const minor=determinant([[I,Z,Z,Z,H,Z],[I,Z,Z,Z,R(11,20),Z],[Z,I,Z,Z,Z,Z],[Z,Z,I,Z,Z,H],[Z,Z,I,Z,Z,R(9,10)],[Z,Z,Z,I,Z,Z]]);
 if(!eq(minor,R(1,50)))throw Error("rank minor");
 return {status:"PASS_BRC_N4_COARSE_TERMINAL_EXACT_RANK",strict_positive_leaves:16,fixed_policy_rank:4,universal_policy_rank:6,minor_determinant:str(minor),noise_values:epses.map(str),fixed_factorizations:fixed,legal_S23_deterministic_stage3_policies:64,policy_state_checks:policy};
}
console.log(JSON.stringify(verify(),null,2));
