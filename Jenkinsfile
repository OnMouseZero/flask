node('jenkins-slave') {
    stage('Clone') {
      echo "1.Clone Stage"
      checkout dev
      script {
<<<<<<< HEAD
            build_tag = "v11.0"
=======
            build_tag = sh(returnStdout: true, script: 'git describe').trim()
>>>>>>> 44fe6e28fc5d9ce26d211cab966b3f64ad0ee833
      }
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
