python -m venv jenkins-venv
source jenkins-venv/bin/activate
pip install - r src/requirements.txt
pip install src / .


{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 2000,
  "LoanAmount": 1200,
  "Loan_Amount_Term": 36,
  "Credit_History": 1.0,
  "Property_Area": "Rural"
}


docker build -t himanshuchoudhary3004/loan_pred_jenkins:latest .
docker run -it loan_pred_jenkins:latest
docker push himanshuchoudhary3004/loan_pred_jenkins:latest
docker run -d -it --name predmodeljenklatest -p 8005:8005 himanshuchoudhary3004/loan_pred_jenkins:latest bash
docker exec predmodeljenklatest python prediction_model/training_pipeline.py

docker exec predmodeljenklatest pytest -v --junitxml TestResults.xml --cache-clear
docker cp predmodeljenklatest:/code/src/TestResults.xml .

docker exec -d -w /code predmodeljenklatest python main.py            # THis might not work so use below command
docker exec -d predmodeljenklatest bash -c "cd /code && python main.py"


## Install and run jenkins 

'''
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

'''
sudo apt update
sudo apt install fontconfig openjdk-17-jre
java -version

'''
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
'''

## Install and run docker

'''
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

'''
# Install the Docker packages
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
'''
# Provide user ID permission to docker 
sudo usermod -a -G docker $USER
# provide jenkins permissions to interact with docker
sudo usermod -a -G docker jenkins



