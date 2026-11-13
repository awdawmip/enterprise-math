// Exact compressed enumeration of all adjacent gaps for 510<=H<=649492.
// The shift (79,431) increments integer ordering key (2074774*v-380295*j) by 1.
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
constexpr ll P=2074774,D=380295;
constexpr int A=79,B=431,W=A+B;
struct Node {ll key;int v,j;bool operator>(const Node& o)const{return key>o.key;}};
struct Gap {int dv,dj;ll V,J,S,num;};
uint64_t tag(int dv,int dj){return (uint64_t(uint32_t(dv))<<32)|uint32_t(dj);}
void add(unordered_map<uint64_t,Gap>&g,int dv,int dj,ll V,ll J,ll S,ll cnt){
 auto key=tag(dv,dj);auto it=g.find(key);
 if(it==g.end())g.emplace(key,Gap{dv,dj,V,J,S,cnt});
 else {auto &r=it->second;r.V=max(r.V,V);r.J=max(r.J,J);r.S=min(r.S,S);r.num+=cnt;}
}
int main(int argc,char**argv){
 if(argc!=2)return 2;int H=atoi(argv[1]);if(H<510||H>649492)return 3;
 auto t0=chrono::steady_clock::now();
 priority_queue<Node,vector<Node>,greater<Node>> pq;
 for(int v=0;v<=H;v++){
  int jmax=v<A ? H-v : min(B-1,H-v);
  pq.push({P*v-D*jmax,v,jmax});
 }
 unordered_map<uint64_t,Gap> classes;classes.reserve(1024);
 ll count=0,chaincnt=0, prevEndKey=LLONG_MIN;int pv=0,pj=0;
 while(!pq.empty()){
  auto x=pq.top();pq.pop();
  if(chaincnt>0){
   if(x.key<=prevEndKey){cerr<<"OVERLAP chain="<<chaincnt<<"\n";return 4;}
   add(classes,x.v-pv,x.j-pj,pv,pj,pv+pj,1);
  }
  ll q=(H-x.v-x.j)/W;
  if(q>0) add(classes,A,B,x.v+A*(q-1),x.j+B*(q-1),x.v+x.j,q);
  pv=x.v+A*q;pj=x.j+B*q;
  prevEndKey=x.key+q;
  count+=q+1;chaincnt++;
  if(x.j>0)pq.push({x.key+D,x.v,x.j-1});
 }
 ll M=(ll(H)+1)*(H+2)/2,cnt=0;
 vector<Gap> rows;rows.reserve(classes.size());
 for(auto &p:classes){rows.push_back(p.second);cnt+=p.second.num;}
 if(count!=M||cnt!=M-1||chaincnt!=510LL*H-129285){
  cerr<<"BAD_COUNTS "<<count<<" "<<M<<" "<<cnt<<" chains="<<chaincnt<<"\n";return 5;
 }
 sort(rows.begin(),rows.end(),[](auto &a,auto &b){if(a.num!=b.num)return a.num>b.num;if(a.dv!=b.dv)return a.dv<b.dv;return a.dj<b.dj;});
 cout<<"SUMMARY,"<<H<<","<<M<<","<<rows.size()<<"\n";
 for(auto g:rows)cout<<"CLASS,"<<g.dv<<","<<g.dj<<","<<g.V<<","<<g.J<<","<<g.S<<","<<g.num<<"\n";
 cerr<<"CHAIN_PASS H="<<H<<" M="<<M<<" chains="<<chaincnt<<" classes="<<rows.size()<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n";
}
