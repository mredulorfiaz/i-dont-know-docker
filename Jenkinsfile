pipeline {
    agent any
    
    environment {
        // Define environment variables
        DOCKER_REGISTRY = '0rf1az'
        APP_NAME = 'front-end'
        VERSION = "${BUILD_NUMBER}"
        HELM_CHART_PATH = './charts'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        docker build -t "${DOCKER_REGISTRY}/${APP_NAME}:${VERSION}" .
                    """
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    sh """
                        docker push "${DOCKER_REGISTRY}/${APP_NAME}:${VERSION}"
                    """
                }
            }
        }
        
        stage('Package Helm Chart') {
            steps {
                script {
                    // Package Helm chart
                    sh """
                        helm package ${HELM_CHART_PATH} \
                        --version ${VERSION} \
                        --app-version ${VERSION}
                    """
                    
                    // Optional: Push to Helm registry if you're using one
                    // sh "helm push ${APP_NAME}-${VERSION}.tgz oci://your-registry"
                }
            }
        }
        
        // stage('Deploy to EKS') {
        //     steps {
        //         script {
        //             // Configure kubectl to use EKS cluster
        //             sh """
        //                 aws eks --region us-west-2 update-kubeconfig \
        //                 --name your-eks-cluster-name
        //             """
                    
        //             // Deploy using Helm
        //             sh """
        //                 helm upgrade --install ${APP_NAME} ${HELM_CHART_PATH} \
        //                 --namespace your-namespace \
        //                 --set image.repository=${DOCKER_REGISTRY}/${APP_NAME} \
        //                 --set image.tag=${VERSION} \
        //                 --wait
        //             """
        //         }
        //     }
        // }
        
        // stage('Verify Deployment') {
        //     steps {
        //         script {
        //             // Run some basic verification
        //             sh """
        //                 kubectl get deployments -n your-namespace
        //                 kubectl rollout status deployment/${APP_NAME} -n your-namespace
        //             """
        //         }
        //     }
        // }
    }
}
