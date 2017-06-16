
VMs = 1 # number of storage nodes to deploy

# This Vagrantfile has been tested to work on VirtualBox and macOS

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
      v.customize ["modifyvm", :id, "--memory", 2048]
    end

  end

(1..VMs).each do |i|
  config.vm.define "stg0#{i}" do |node|
  node.vm.box = "centos/7"
  node.vm.box_url = "centos/7"
  node.vm.hostname = "stg0#{i}"

  node.vm.network :private_network, ip: "192.168.56.1#{i}"

  node.vm.provider :virtualbox do |v|
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--memory", 512]
    v.customize ['storagectl', :id, '--name', 'SATAController', '--add', 'sata', \
	         '--controller', 'IntelAHCI']

    disk1="stg0#{i}d1.vdi"
    v.customize ['createhd', '--filename', "#{disk1}", '--size', 11000]
    v.customize ['storageattach', :id,
                       '--storagectl', 'IDE Controller',
                       '--port', 0,
                       '--device', 1,
                       '--type', 'hdd',
                       '--medium', "#{disk1}"]

    disk2="stg0#{i}d2.vdi"
    v.customize ['createhd', '--filename', "#{disk2}", '--size', 11000]
    v.customize ['storageattach', :id,
                       '--storagectl', 'IDE Controller',
                       '--port', 1,
                       '--device', 0,
                       '--type', 'hdd',
                       '--medium', "#{disk2}"]
  end
  end
end
    config.vm.provision "ansible" do |ansible|
      ansible.limit = "all"
      ansible.playbook = "site.yml"
      ansible.raw_arguments = "--user=vagrant", "-b"
      # ansible.verbose = true
      # ansible.verbose = 'vvvv'
      ansible.groups = {
        "tendrl-server" => ["tendrl"],
        "gluster-servers" => ["stg0[1:#{VMs}]"], 
      }
    end
end

