BOX_IMAGE = "generic/ubuntu2204" #debian based for Raspberry Pi
BOX_VERSION = "4.3.12"
NODE_COUNT = 1

Vagrant.configure("2") do |config| #2 being the API version
  config.vm.box = BOX_IMAGE
  config.vm.box_version = BOX_VERSION

  (1..NODE_COUNT).each do |i|
    config.vm.define "sensor#{i}" do |subconfig|
      subconfig.vm.box = BOX_IMAGE
      subconfig.vm.hostname = "node#{i}"
      subconfig.vm.network "forwarded_port", guest: 80, host: 8080
    end
    config.vm.provision "docker" do |d|
      d.pull_images "364573/my-iot-app:pub"
      d.pull_images "364573/eclipse-mosquitto:openssl"
      d.pull_images "364573/my-iot-app:sub"
      d.run "publisher", image: "364573/my-iot-app:pub"
      d.run "subscriber", image: "364573/my-iot-app:sub"
      d.run "mosquitto-broker",
        image: "364573/eclipse-mosquitto:openssl",
        args: "-p 1883:1883 -v /vagrant/src/config/mqtt_config:/mosquitto/config"
    end
  end
end