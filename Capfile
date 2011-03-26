role :servers, "lila.r.bravetstudio.com"

packages = [
            'git-core',
            'python',
            'python-pip'
           ]
python_packages = [
                   'kokki'
                  ]

set :repository,  "git://github.com/t0ster/bravet-cloud.git"
set :ssh_options, { :user => :ubuntu, :forward_agent => true }
set :deploy_to, "/home/#{ssh_options[:user]}/kokki"

desc "Bootstraps env on new servers"
task :bootstrap, :roles => :servers do
  set :ssh_options, { :user => :ubuntu, :forward_agent => true }
  run "#{sudo} apt-get install #{packages.join(' ')}"
  run "#{sudo} pip install #{python_packages.join(' ')}"
end

namespace :kokki do
  task :update do
    run "cd #{deploy_to}; git clone #{repository} ."
  end
end
