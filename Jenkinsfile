pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        echo 'hello'
      }
    }

    stage('stage2') {
      steps {
        slackSend(color: 'green', message: 'success', channel: 'jenkinsbuild2')
      }
    }

  }
}