pipeline {
  agent any
  stages {
    stage('stage1') {
      parallel {
        stage('stage1') {
          steps {
            echo 'hello'
            slackSend(channel: 'jenkinsbuild2', message: "started now  (<${env.BUILD_URL}|Open>)", tokenCredentialId: 'jenkins-slack-integration', color: '#2056e8')
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
