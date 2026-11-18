// Independent C++17 integer-only dynamic program for fixed seven raw BRC keys.
// stdin: one demand label 0..23 and a hex string of signed-X6 native-step bytes per line.
#include <bits/stdc++.h>
using namespace std;
struct Node {map<int,int> next; unsigned mask=0;};
vector<Node> tr(1);
unsigned subtree(int u){unsigned m=tr[u].mask;for(auto [c,v]:tr[u].next)m|=subtree(v);return m;}
using Costs=unordered_map<unsigned,int>;
Costs solve(int u, const array<int,24>& bit){
 unsigned t=0;
 for(int i=0;i<24;i++)if(bit[i]>=0 && (tr[u].mask>>i&1))t|=(1u<<bit[i]);
 Costs dp{{0,0}};if(t)dp[t]=0;
 for(auto [b,v]:tr[u].next){
  Costs child=solve(v,bit),out;
  for(auto [a,ca]:dp)for(auto [c,cb]:child){unsigned m=a|c;int x=ca+cb;
    auto it=out.find(m);if(it==out.end()||x<it->second)out[m]=x;}
  dp.swap(out);
 }
 for(auto &p:dp)if(p.first)p.second++;
 return dp;
}
struct Root {unsigned glob;array<int,24> bits;vector<int> best;};
Root rootSolve(int u){
 Root r; r.glob=subtree(u);r.bits.fill(-1);int k=0;
 for(int j=0;j<24;j++)if(r.glob>>j&1)r.bits[j]=k++;
 auto costs=solve(u,r.bits);r.best.assign(1u<<k,100000000);
 for(auto [m,v]:costs)r.best[m]=min(r.best[m],v);
 for(int j=0;j<k;j++)for(unsigned mask=0;mask<r.best.size();mask++)if(!(mask>>j&1))
   r.best[mask]=min(r.best[mask],r.best[mask|(1u<<j)]);
 return r;
}
unsigned local(unsigned global,const Root&r){unsigned z=0;for(int i=0;i<24;i++)if(r.bits[i]>=0&&(global>>i&1))z|=1u<<r.bits[i];return z;}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 int id,words=0;string hex;
 while(cin>>id>>hex){if(id<0||id>=24||hex.size()%2)throw runtime_error("bad instance");
  int u=0;for(size_t p=0;p<hex.size();p+=2){int ch=stoi(hex.substr(p,2),nullptr,16);
   if(!tr[u].next.count(ch)){int next=tr.size();tr[u].next[ch]=next;tr.emplace_back();}
   u=tr[u].next[ch];}
  tr[u].mask|=1u<<id;words++;
 }
 if(!tr[0].next.count(5)||!tr[0].next.count(6)||!tr[0].next.count(7)||tr[0].next.size()!=3)throw runtime_error("unexpected signed roots");
 Root a=rootSolve(tr[0].next[5]),b=rootSolve(tr[0].next[6]),c=rootSolve(tr[0].next[7]);
 if(__builtin_popcount(a.glob)!=12||__builtin_popcount(b.glob)!=12||__builtin_popcount(c.glob)!=8 || (a.glob&b.glob)!=0 || (a.glob|b.glob)!=((1u<<24)-1))throw runtime_error("unexpected root covering");
 int ans=1e9;vector<int> arg;vector<int> all;
 for(unsigned s=0;s<256;s++){
  unsigned cover=0;for(int lab=0;lab<24;lab++)if(c.bits[lab]>=0 && (s>>c.bits[lab]&1))cover|=1u<<lab;
  int val=a.best[local(a.glob&~cover,a)]+b.best[local(b.glob&~cover,b)]+c.best[s];
  all.push_back(val);if(val<ans){ans=val;arg.clear();arg.push_back(s);}else if(val==ans)arg.push_back(s);
 }
 cout<<"WORDS "<<words<<" PREFIX_NODES "<<tr.size()-1<<"\n";
 cout<<"ROOT_MINIMA "<<a.best.back()<<" "<<b.best.back()<<" "<<c.best.back()<<"\n";
 cout<<"OPTIMUM "<<ans<<" OPTIMAL_ALLOCATIONS";for(int x:arg)cout<<" "<<x;cout<<"\n";
 cout<<"ALL_COSTS ";for(int x:all)cout<<x<<" ";cout<<"\n";
}
