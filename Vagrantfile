VAGRANT_ROOT = File.dirname(File.expand_path(__FILE__))

if ARGV[0] == "up" or ARGV[0] == "provision"
    system("ansible-galaxy install -p #{VAGRANT_ROOT}/roles/ -r requirements.yml")
end

Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.define "tendrl", primary: true do |tendrl|
    tendrl.vm.network :forwarded_port, guest: 80, host: 8080, id: "web"
    tendrl.vm.network :forwarded_port, guest: 9292, host: 9292, autocorrect:true
    tendrl.vm.network :forwarded_port, guest: 2379, host: 2379, autocorrect:true
    tendrl.vm.box = "centos/7"
    tendrl.vm.hostname = 'tendrl'
    tendrl.vm.box_url = "centos/7"
    tendrl.vm.network :private_network, ip: "192.168.56.101"
    tendrl.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
     # v.customize ["modifyvm", :id, "--name", "tendrl"]
    end

  end

  config.vm.define "gl01" do |gl01|
    gl01.vm.box = "centos/7"
    gl01.vm.box_url = "centos/7"
    gl01.vm.hostname = 'gl01'

    gl01.vm.network :private_network, ip: "192.168.56.102"

    gl01.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
     # v.customize ["modifyvm", :id, "--name", "gl01"]
    end
  end

  config.vm.define "gl02" do |gl02|
    #config.vm.network :forwarded_port, guest: 22, host: 2023, autocorrect:true
    gl02.vm.box = "centos/7"
    gl02.vm.hostname = 'gl02'
    gl02.vm.box_url = "centos/7"

    gl02.vm.network :private_network, ip: "192.168.56.103"

    gl02.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      #v.customize ["modifyvm", :id, "--name", "gl02"]
    end

    config.vm.provision "ansible" do |ansible|
      ansible.limit = "all"
      ansible.playbook = "site.yml"
      # ansible.verbose = true
      # ansible.verbose = 'vvvv'
      ansible.groups = {
        "tendrl-servers" => ["tendrl"],
        "storage-servers" => ["gl01,gl02]"], 
      }
    end
  end
end
