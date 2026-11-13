// Compiled integer-key stream; matching output is checked by VERIFY_CLASS_CERTIFICATES.py
// Model and bounds documented in PROOF.md.
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
static constexpr ll P=2074774,D=380295;
struct Node {ll key;int v,j;bool operator>(const Node& o)const{return key>o.key;}};
struct Gap {int dv,dj;ll V,J,S,num;};
static uint64_t class_key(int dv,int dj){return (uint64_t(uint32_t(dv))<<32)|uint32_t(dj);}
int main(int argc,char**argv){
 if(argc!=2)return 2;
 int H=atoi(argv[1]);if(H<1||H>=D)return 3;
 auto t0=chrono::steady_clock::now();
 priority_queue<Node,vector<Node>,greater<Node>> q;
 for(int v=0;v<=H;v++)q.push(Node{P*v-D*(H-v),v,H-v});
 unordered_map<uint64_t,Gap> groups;groups.reserve(128);
 bool have=false;int pv=0,pj=0;ll count=0,prev_key=LLONG_MIN;
 while(!q.empty()){
  auto x=q.top();q.pop();
  if(x.key<=prev_key){cerr<<"KEY_NOT_INCREASING "<<count<<"\n";return 4;}
  if(have){
   int dv=x.v-pv,dj=x.j-pj;uint64_t tag=class_key(dv,dj);
   auto it=groups.find(tag);
   if(it==groups.end())groups.emplace(tag,Gap{dv,dj,pv,pj,pv+pj,1});
   else{auto &z=it->second;z.V=max(z.V,(ll)pv);z.J=max(z.J,(ll)pj);
        z.S=min(z.S,(ll)pv+pj);z.num++;}
  }
  prev_key=x.key;pv=x.v;pj=x.j;have=true;count++;
  if(x.j>0)q.push(Node{x.key+D,x.v,x.j-1});
 }
 ll M=(ll(H)+1)*(H+2)/2,total=0;vector<Gap> out;
 for(auto &x:groups){total+=x.second.num;out.push_back(x.second);}
 if(count!=M||total!=M-1){cerr<<"COUNT_FAILURE\n";return 5;}
 sort(out.begin(),out.end(),[](const Gap&a,const Gap&b){
  if(a.num!=b.num)return a.num>b.num;
  if(a.dv!=b.dv)return a.dv<b.dv;
  return a.dj<b.dj;
 });
 cout<<"SUMMARY,"<<H<<","<<M<<","<<out.size()<<"\n";
 for(auto z:out)cout<<"CLASS,"<<z.dv<<","<<z.dj<<","<<z.V<<","<<z.J<<","<<z.S<<","<<z.num<<"\n";
 double sec=chrono::duration<double>(chrono::steady_clock::now()-t0).count();
 cerr<<"STREAM_PASS "<<H<<" "<<M<<" "<<out.size()<<" seconds "<<sec<<"\n";
}
