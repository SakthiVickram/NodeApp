pipeline {
  agent any
  stages {
    stage('stage1') {
      parallel {
        stage('stage1') {
          steps {
            echo 'hello'
          }
        }

        stage('stage1.1') {
          steps {
            echo 'world'
          }
        }

      }
    }

    stage('stage2') {
      steps {
        slackSend(color: 'green', message: 'success', channel: 'jenkinsbuild2')
      }
    }

  }
}