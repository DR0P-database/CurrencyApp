pipeline {
    agent any
    parameters {
        string(name: 'VERSION', defaultValue: '1.0.0', description: 'Version to deploy')
    }
    stages {
        stage("Checkout repo") { //Объявляем секцию с именем «Checkout repo»
            steps {
                checkout scmGit(branches: [[name: '${BRANCH_NAME}']],
                userRemoteConfigs: [[credentialsId: '1', url: 'https://gitlab-pub.yadro.com/devops-school-2024/student/a.ukhanov.git']])
            }
        }
        stage('Build docker image') {
            steps {
                withCredentials([usernamePassword(credentialsId: '4', passwordVariable: 'HUB_PASSWORD',
                                usernameVariable: 'HUB_USERNAME')]) {
                    sh("buildah bud --tag ${HUB_USERNAME}/currency_app:${params.VERSION} -f ./Dockerfile .")
                }
            }
        }
        stage('Push docker image to docker hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: '4', passwordVariable: 'HUB_PASSWORD',
                                usernameVariable: 'HUB_USERNAME')]) {
                    sh """
                        buildah login -u ${HUB_USERNAME} -p ${HUB_PASSWORD} docker.io
                        buildah push ${HUB_USERNAME}/currency_app:${params.VERSION}
                        buildah logout docker.io
                    """
                }
            }
        }
    }
}
