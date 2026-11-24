// Exact five-original-mask minimax lower certificate, 0<=f<=30.
// Input action file was derived from all 101 budgets at tau=L.
#include <bits/stdc++.h>
using namespace std;
struct Act{int k; vector<uint8_t> supports;};
vector<Act> actions;
unordered_map<uint64_t,int> memo;
int max_errors;uint64_t visited=0,edges=0;
inline int d(uint64_t s,int i){return (s>>(i*5))&31;}
inline bool terminal(uint64_t s){int live=0;for(int i=0;i<5;i++)if(d(s,i)<=max_errors&&++live>1)return false;return true;}
inline uint64_t succ(uint64_t s,uint8_t mask){
 for(int i=0;i<5;i++)if(!(mask&(1<<i)) && d(s,i)<=max_errors)s+=uint64_t(1)<<(5*i);
 return s;
}
int solve(uint64_t s){
 if(terminal(s))return 0;
 auto it=memo.find(s);if(it!=memo.end())return it->second;
 int best=INT_MAX/2;
 for(const Act&a:actions){
   int worst=0;bool possible=true;
   for(uint8_t sup:a.supports){
      uint64_t t=succ(s,sup);
      if(t==s){possible=false;break;}
      ++edges;int value=solve(t);
      if(value>worst)worst=value;
      if(a.k+worst>=best){possible=false;break;}
   }
   if(possible)best=min(best,a.k+worst);
 }
 if(best==INT_MAX/2){cerr<<"NO_PROGRESS "<<s<<"\n";exit(3);}
 memo.emplace(s,best);return best;
}
int main(int argc,char**argv){if(argc!=3){cerr<<"usage actions_file f\n";return 2;}max_errors=stoi(argv[2]);if(max_errors<0||max_errors>30)return 2;
 ifstream in(argv[1]);int n;in>>n;
 for(int j=0;j<n;j++){Act a;int c,t;in>>a.k>>c;for(int i=0;i<c;i++){in>>t;a.supports.push_back(t);}actions.push_back(move(a));}
 auto st=chrono::steady_clock::now();int res=solve(0);
 cout<<"{\"f\":"<<max_errors<<",\"lower_bound\":"<<res<<",\"memo_states\":"<<memo.size()<<",\"evaluated_children\":"<<edges<<",\"method\":\"exact_packed_five_state_bellman_all101_reduced_to7_equal_families\",\"elapsed_seconds\":"<<fixed<<setprecision(3)<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<"}"<<endl;
}
