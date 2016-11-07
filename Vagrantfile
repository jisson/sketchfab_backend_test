Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |v|
    v.name = "sf-backend-test"
  end
  
  config.vm.box = "hashicorp/precise64"
  config.vm.provision :shell, path: "bootstrap.sh", privileged: false
  config.vm.network "forwarded_port", guest: 8040, host: 8040
end
