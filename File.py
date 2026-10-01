vboxuser@Ubuntu22:~/Collaborative-UAV-Dataset-main$ pwd
/home/vboxuser/Collaborative-UAV-Dataset-main
vboxuser@Ubuntu22:~/Collaborative-UAV-Dataset-main$ nl -ba Makefile | sed -n '10,20p'
    10	
    11	install-containernet-and-requirements-part1: ## not tested
    12	# 	sudo sed -i 's|http://us.archive.ubuntu.com|https://us.archive.ubuntu.com|g' /etc/apt/sources.list
    13		sudo apt-get update
    14		sudo apt-get install -y ansible python3.10-venv tshark parallel htop
    15		cd $(home_dir) && git clone https://github.com/containernet/containernet.git
    16		cd $(home_dir) && sudo ansible-playbook -i "localhost," -c local containernet/ansible/install.yml
    17		cd $(home_dir) && python3 -m venv venv
    18		sudo su
    19		sudo docker build --no-cache --tag=uav_nodes -f Docker/Dockerfile.node Docker/
    20	
vboxuser@Ubuntu22:~/Collaborative-UAV-Dataset-main$ echo $HOME
/home/vboxuser
