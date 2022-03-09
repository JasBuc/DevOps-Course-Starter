
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    sudo apt-get install build-essential
    
    echo 'sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev' >> ~/.profile
    
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv

    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.profile
    echo 'eval "$(pyenv init --path)"' >> ~/.profile

    echo 'eval "$(pyenv init -)"' >> ~/.bashrc

    gcc

    sudo pyenv install 3.8.5

    sudo pyenv global 3.8.5

    sudo curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

    export PATH="$HOME/.poetry/bin:$PATH"
    echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.profile

  SHELL

  config.trigger.after :up do |trigger|
    trigger.name = "Launching App"
    trigger.info = "Running the TODO app setup script"
    trigger.run_remote = {privileged: false, inline: "
      cd /vagrant
      poetry install
      nohup poetry run flask run --host 0.0.0.0 > logs.txt 2>&1 &
    "}
  end
end
