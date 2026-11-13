#!/usr/bin/env node
'use strict';

function verify() {
  const A=(v,m)=>{if(!v)throw Error(m)};
  const root={children:new Map(),term:false};
  for(let i=0;i<1065;i++){
    const d=[Math.floor(i/225)+1,Math.floor(i/15)%15+1,i%15+1];
    const spare=Array.from({length:15},(_,k)=>k+1).filter(k=>!d.includes(k));
    const w=d.concat([spare[0]], i<673?[spare[1]]:[]);
    let z=root;
    for(const a of w){if(!z.children.has(a))z.children.set(a,{children:new Map(),term:false});z=z.children.get(a)}
    A(!z.term,"duplicate");z.term=true;
  }
  const nodes=[];
  function dfs(z,label){
    const id=nodes.length;nodes.push({label,sz:0,term:z.term});
    for(const [a,y] of [...z.children].sort((l,r)=>l[0]-r[0]))dfs(y,a);
    nodes[id].sz=nodes.length-id;
  }
  dfs(root,0);
  A(nodes.length===2880&&nodes[0].sz===2880,"node count");
  const T=nodes.map(z=>z.term?1:0),pairs=[];
  for(const z of nodes)if(z.term){
    const k=pairs.length;
    pairs.push(k<538?[3,300+k]:k<836?[12,315+k-538]:[15,250+k-836]);
  }
  A(pairs.length===1065,"terminals");
  const M3=pairs.map(z=>+(z[0]===3)),M12=pairs.map(z=>+(z[0]===12));
  function rankVec(bits){
    const L=bits.length,B=Math.ceil(L/64),S=Math.ceil(L/512);
    let total=0,superBase=0;const sup=[],rel=new Array(B).fill(0);
    for(let k=0;k<B;k++){
      if(k%8===0){superBase=total;if(k>0)sup.push(total)}
      else rel[k]=total-superBase;
      for(let j=k*64;j<Math.min(L,(k+1)*64);j++)total+=bits[j];
    }
    A(rel.every(x=>x<=448),"rank offset overflow");
    function rank(k){
      A(Number.isInteger(k)&&k>=0&&k<=L,"rank bounds");
      if(k===L)return total;
      const block=Math.floor(k/64),s=Math.floor(block/8);
      let count=(s?sup[s-1]:0)+rel[block];
      for(let j=block*64;j<k;j++)count+=bits[j];
      return count;
    }
    return{bits,L,rank,storage:(S-1)*Math.ceil(Math.log2(L+1))+(B-S)*9};
  }
  function wavelet(nums){
    const width=Math.ceil(Math.log2(Math.max(...nums)+1));let now=nums.slice(),rows=[],zeros=[];
    for(let d=width-1;d>=0;d--){
      const b=now.map(x=>(x>>d)&1);
      rows.push(rankVec(b));zeros.push(b.length-b.reduce((s,v)=>s+v,0));
      now=now.filter(x=>!((x>>d)&1)).concat(now.filter(x=>(x>>d)&1));
    }
    function upto(l,r,t){
      if(t<0)return 0;
      if(t>=2**width-1)return r-l;
      const x=t+1;let count=0;
      for(let i=0;i<width;i++){
        const d=width-1-i,ol=rows[i].rank(l),orr=rows[i].rank(r);
        const zl=l-ol,zr=r-orr;
        if((x>>d)&1){count+=zr-zl;l=zeros[i]+ol;r=zeros[i]+orr}
        else{l=zl;r=zr}
      }
      return count;
    }
    return{width,rows,upto};
  }
  const Q=[3,12,15],wv={};
  for(const q of Q)wv[q]=wavelet(pairs.filter(p=>p[0]===q).map(p=>p[1]));
  const rt=rankVec(T),r3=rankVec(M3),r12=rankVec(M12);
  A(wv[3].width===10&&wv[12].width===10&&wv[15].width===9,"wavelet widths");
  let rankChecks=0;
  for(const v of [rt,r3,r12,...Q.flatMap(q=>wv[q].rows)]){
    let sum=0;
    for(let k=0;k<=v.L;k++){if(k)sum+=v.bits[k-1];A(v.rank(k)===sum,"rank mismatch");rankChecks++}
  }
  const samples=[[-1,1],[-1,10],[-1,100],[0,1],[1,100],[1,50],[1,40],[1,30],[1,23]];
  let countChecks=0,edges=0;
  for(let i=0;i<nodes.length;i++){
    const l=rt.rank(i),r=rt.rank(i+nodes[i].sz),l3=r3.rank(l),r3e=r3.rank(r),l12=r12.rank(l),r12e=r12.rank(r);
    const ranges={3:[l3,r3e],12:[l12,r12e],15:[l-l3-l12,r-r3e-r12e]};
    A(Object.values(ranges).reduce((s,[a,b])=>s+b-a,0)===r-l,"class ranges");
    for(const [na,nb] of samples){
      const a=BigInt(na),b=BigInt(nb),delta=b-23n*a;
      let calc=0,brute=0;
      for(const q of Q){const t=delta===0n?Infinity:Number(36n*BigInt(q)*b/delta);calc+=wv[q].upto(...ranges[q],t)}
      for(let t=l;t<r;t++){const [q,n]=pairs[t];if(delta===0n||BigInt(n)*delta<=36n*BigInt(q)*b)brute++}
      A(calc===brute,"count mismatch");countChecks++;
    }
    let child=i+1;while(child<i+nodes[i].sz){A(nodes[child].label>=1&&nodes[child].label<=15,"edge label");child+=nodes[child].sz;edges++}
    A(child===i+nodes[i].sz,"skip mismatch");
  }
  const wavebits=wv[3].width*538+wv[12].width*298+wv[15].width*229;
  const dirwaves=Q.reduce((s,q)=>s+wv[q].rows.reduce((z,v)=>z+v.storage,0),0);
  const rankbits=rt.storage+r3.storage+r12.storage+dirwaves;
  const fields={subtree_size_bits:34560,edge_label_bits:11516,terminal_flag_bits:2880,q_class_mask_bits:2130,wavelet_bits:wavebits,rank_directory_bits:rankbits};
  const sum=Object.values(fields).reduce((a,b)=>a+b,0);
  A(rankbits===2040&&wavebits===10421,"support size");
  A(sum===63547&&Math.ceil(sum/8)===7944,"serialization");
  return{pass:"PASS_R5_PREORDER_SKIP_RANK_SYNTHETIC",scope:"independent synthetic 2880-node, 1065-word trie (not frozen R5 corpus)",nodes:2880,terminals:1065,rank_checks:rankChecks,prefix_parameter_checks:countChecks,child_edges_checked:edges,fields,packed_bits:sum,packed_bytes:Math.ceil(sum/8)};
}

console.log(JSON.stringify(verify(),null,2));
