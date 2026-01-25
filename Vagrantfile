BOX_IMAGE = "fkrull/fedora-iot"
BOX_VERSION = "38.20230419.2-1.4.1"
NODE_COUNT = 1

Vagrant.configure("2") do |config| #2 being the API version
  config.vm.box = BOX_IMAGE
  config.vm.box_version = BOX_VERSION

  (1..NODE_COUNT).each do |i|
    config.vm.define "sensor#{i}" do |subconfig|
      subconfig.vm.box = BOX_IMAGE
      subconfig.vm.hostname = "node#{i}"
      subconfig.vm.network :private_network, ip: "10.0.0.#{i + 10}"
    end
  end
end