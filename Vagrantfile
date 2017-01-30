# -*- mode: ruby -*-
# vi: set ft=ruby :

awsInformation = {
  'access_key_id' = "AKIAIXXXXXXXXXXXXX",
  'secret_access_key' = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  'keypair_name' = "vagrant",
  'instance_type' = "m4.large",
  'ami' = "ami-af4333cf",
  'availability_zone' = "us-west1a",
  'region' = "us-west-1",
  'security_groups' = ["sg-group1", "sg-group2"],
  'subnet_id' = "subnet-abcabc123"
}

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
    # The most common configuration options are documented and commented below.
    # For a complete reference, please see the online documentation at
    # https://docs.vagrantup.com.

    # Every Vagrant development environment requires a box. You can search for
    # boxes at https://atlas.hashicorp.com/search.
    config.vm.box = "dummy"
    config.vm.synced_folder ".", "/vagrant", disabled: true

    config.vm.define "tendrl_server" do |tendrl_server|
        tendrl_server.vm.provider :aws do |aws, override|
            aws.access_key_id = awsInformation.access_key_id
            aws.secret_access_key = awsInformation.secret_access_key
            aws.keypair_name = awsInformation.keypair_name
            aws.instance_type = awsInformation.instance_type
            aws.ami = awsInformation.ami
            aws.availability_zone = awsInformation.availability_zone
            aws.region = awsInformation.region
            aws.security_groups = [awsInformation.security_groups
            aws.associate_public_ip = true
            aws.subnet_id = awsInformation.subnet_id
            aws.tags = {
                        "Name" => "Tendrl-Server",
                    }
            # Since it's the default cloud image - we don't have a vagrant user :'(
            override.ssh.username = "cloud-user"
            override.ssh.private_key_path = "vagrant_rsa"
        end

        tendrl_server.vm.provision "shell", inline: <<-SHELL
            echo "r3dh4t1!!" | sudo passwd root --stdin
            sudo hostname tendrl-server
            hostname | sudo tee /etc/hostname
            sudo systemctl disable firewalld
            sudo systemctl stop firewalld
        SHELL
    end
end
