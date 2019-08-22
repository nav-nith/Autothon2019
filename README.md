# Team SONY - TestAutothon 2019
Autothon Repository for STeP-IN Summit 2019

## Challenge
<img width="500" src="https://user-images.githubusercontent.com/13361053/63485414-eff3ad80-c4c0-11e9-8b93-251d2cd4bf85.jpeg" border="1">

## System Overview
<img width="900" src="https://user-images.githubusercontent.com/13361053/63485435-0ac62200-c4c1-11e9-8608-10a90bdc055e.png" border="1">

## SW Design
<img width="300" src="https://user-images.githubusercontent.com/13361053/63485418-f4b86180-c4c0-11e9-9f03-eeb608ebe3f9.png" border="1">

## Environment Setup
### CI/CD Setup
1. Setup Jenkins and Portainer
```
cd ci/compose
docker-compose up -d
```
2. Jenkins Plugin requirements
- Git
- Pipeline
- Blue Ocean
- xUnit
- Slack Notification

### Slave Setup
Install following SW in the jenkins slave system
- Python Latest Version
- Appium Desktop
- Chrome Browser
