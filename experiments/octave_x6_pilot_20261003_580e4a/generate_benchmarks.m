function generate_benchmarks(outdir)
  % External reference and all statistical parameter fitting run in GNU Octave.
  % Six q columns are POSITIONS. The six v columns are auxiliary velocities,
  % never the native six spatial axes. This is an explicitly declared bridge.
  if nargin < 1, outdir = fullfile(fileparts(mfilename('fullpath')), 'output'); end
  if ~exist(outdir,'dir'), mkdir(outdir); end
  rng(20261002, 'twister');
  h=0.1; N=400; train_last=81; denom=2^20;
  time=(0:N)'*h;
  L=2*eye(6)-circshift(eye(6),1)-circshift(eye(6),-1);
  ks=diag([0.64,0.81,1,1.21,1.44,1.69]);
  names={'independent','coupled','damped'};
  spec=struct('schema','OCTAVE_X6_EXTERNAL_BENCHMARK_V1',...
    'octave_version',version(),'seed',20261002,'h',h,'steps',N,...
    'train_end_time',8,'coefficient_denominator',denom,...
    'deltas',[1/64,1/256,1/1024],...
    'spatial_axis_count',6,'time_is_spatial_axis',false,...
    'source_pin','71d836784c9545867955e1c23cb5a964fc2a0482',...
    'semantic_pin','7035c8011938aa0baffbb22f3827322053f520d5',...
    'native_plane_exists',false,'all_research_basis','HEARTBEAT_WORLD_NATIVE_X6',...
    'time_modeling','AS_NEEDED_SEPARATELY_TYPED_PRESENT_FOR_THIS_MOTION_TASK');
  X0=2*rand(12,13)-1; % 8 fitting initial states, 4 new states, 1 parameter OOD
  allcases=cell(1,3);
  for ci=1:3
    if ci==1, K=ks; coupling=0; else, K=ks+0.18*L; coupling=0.18; end
    gamma=0; if ci==3, gamma=0.12; end
    F=[zeros(6),eye(6);-K,-gamma*eye(6)];
    E=expm(h*F); % external linear-ODE reference only; not a native law
    trajectories=cell(1,13); ode_gap=0; energy_drift=0;
    for tr=1:13
      localK=K; localF=F; localE=E;
      if tr==13, localK=1.15*K;localF=[zeros(6),eye(6);-localK,-gamma*eye(6)];localE=expm(h*localF);end
      exact=zeros(N+1,12); exact(1,:)=X0(:,tr)';
      for k=1:N, exact(k+1,:)=(localE*exact(k,:)')'; end
      [~,sol]=ode45(@(t,s) localF*s,time,X0(:,tr),odeset('RelTol',1e-11,'AbsTol',1e-13));
      ode_gap=max(ode_gap,max(abs(sol(:)-exact(:))));
      trajectories{tr}=sol;
      energy=0.5*sum(sol(:,7:12).^2,2)+0.5*sum((sol(:,1:6)*localK).*sol(:,1:6),2);
      if gamma==0,energy_drift=max(energy_drift,max(abs(energy-energy(1)))/energy(1));end
      dlmwrite(fullfile(outdir,sprintf('%s_truth_%02d.csv',names{ci},tr)),[time,sol],',','precision','%.17g');
    end
    caseinfo=struct('name',names{ci},'K',K,'gamma',gamma,'coupling',coupling,...
      'ode45_vs_expm_maxabs',ode_gap,'truth_energy_relative_drift',energy_drift,...
      'train_initial_states',1:8,'test_initial_states',9:12,'parameter_ood_state',13,...
      'parameter_ood_K_multiplier',1.15);
    variants=cell(1,2);
    for ni=1:2
      sigma=[0,1e-3](ni); % absolute training-position standard deviation
      X=[];Y=[];
      for tr=1:8
        q=trajectories{tr}(1:train_last,1:6);
        q=q+sigma*randn(size(q));
        X=[X; q(2:end-1,:),q(1:end-2,:)];Y=[Y;q(3:end,:)];
      end
      theta=(X\Y)'; % six outputs by twelve AR2 inputs; 72 fitted coefficients
      rational_numerators=round(theta*denom);
      diagtheta=zeros(6,12);
      for ax=1:6,ii=[ax,ax+6];diagtheta(ax,ii)=(X(:,ii)\Y(:,ax))';end
      variant=struct('noise_sigma',sigma,'full_parameter_count',72,'diagonal_parameter_count',12,...
        'theta',theta,'theta_numerators',rational_numerators,'diagonal_theta',diagtheta,...
        'training_rmse',sqrt(mean((X*theta'-Y)(:).^2)),...
        'design_rank',rank(X),'design_condition',cond(X),...
        'coefficient_max_quantization_error',max(abs(theta(:)-rational_numerators(:)/denom)));
      variants{ni}=variant;
      for tr=9:13
        truth=trajectories{tr};
        for model=1:2
          T=theta;if model==2,T=diagtheta;end
          pred=zeros(N+1,6);pred(1:2,:)=truth(1:2,1:6);
          for k=2:N,pred(k+1,:)=(T*[pred(k,:)';pred(k-1,:)'])';end
          label={'floatfull','diagonal'};
          dlmwrite(fullfile(outdir,sprintf('%s_n%d_%s_%02d.csv',names{ci},ni-1,label{model},tr)),[time,pred],',','precision','%.17g');
        end
      end
    end
    caseinfo.variants=variants;allcases{ci}=caseinfo;
  end
  spec.cases=allcases;
  fid=fopen(fullfile(outdir,'experiment.json'),'w');fprintf(fid,'%s\n',jsonencode(spec));fclose(fid);
  fid=fopen(fullfile(outdir,'octave_evidence.txt'),'w');
  fprintf(fid,'GNU Octave %s\nseed=20261002\ntruth=ode45 RelTol1e-11 AbsTol1e-13\nindependent check=expm(h*F) for external linear ODE only\ntraining=Octave backslash, 8 initial states, t<=8\nholdout=4 unseen initial states, no teacher forcing after first two samples\n',version());
  for ci=1:3,fprintf(fid,'%s ode_gap=%.17g energy_drift=%.17g\n',allcases{ci}.name,allcases{ci}.ode45_vs_expm_maxabs,allcases{ci}.truth_energy_relative_drift);end
  fclose(fid);
  assert(all(cellfun(@(c)c.ode45_vs_expm_maxabs<1e-7,allcases)),'External truth cross-check failed');
  disp('EXTERNAL_OCTAVE_GENERATION_AND_FITTING_PASS');
end
