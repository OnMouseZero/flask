node('jenkins-slave') {
    stage('Clone') {
      echo "1.Clone Stage"
      script {
            build_tag = "v11.0.1"
      }
    }
    stage('Test') {
      echo "2.Test Stage"
    }
    stage('Build') {
      echo "3.Build Docker Image Stage"
      sh "docker build -t onmouse/flask:${build_tag} ."
    }
    stage('Push') {
      echo "4.Push Docker Image Stage"
      withCredentials([usernamePassword(credentialsId: 'dockerHub1', passwordVariable: 'dockerHub1Password', usernameVariable: 'dockerHub1User')]) {
            sh "docker login -u ${dockerHub1User} -p ${dockerHub1Password}"
            sh "docker push onmouse/flask:${build_tag}"
        }
    }
    stage('YAML') {
      echo "5. Change YAML File Stage"
      sh "sed -i 's/<BUILD_TAG>/${build_tag}/' flask-deployment.yaml"
    }
    stage('Deploy') {
      echo "6. Deploy Stage"
      sh "kubectl apply -f flask-deployment.yaml"
      sh "kubectl apply -f flask-svc.yaml"
    }
    stage('Test') {
      echo "7. Test OK!!!!"
    }
}
