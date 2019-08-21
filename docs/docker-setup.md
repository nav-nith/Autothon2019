# Docker Setup

## Environment

OS: Ubuntu 16.04LTS
Account; User with Sudo privilage

## Instructions

1. Update system to have the latest release SW

```
sudo apt-get update && sudo apt-get upgrade
```

2. Install packages to allow apt to use a repository over HTTPS:

```
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```

3. Install Docker

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update && sudo apt-get install docker-ce docker-ce-cli containerd.io
```

4. Add Current user to Docker Group

```
sudo usermod -aG docker $USER
```

5. Install Docker Compose

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo curl -L https://raw.githubusercontent.com/docker/compose/1.24.1/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
