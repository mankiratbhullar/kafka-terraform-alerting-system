# kafka-terraform-alerting-system
Implemented a real-time Terraform deployment monitoring and alerting system using Apache Kafka and Azure Queue Storage. Built Python-based producer and consumer services to stream deployment events from Azure DevOps pipelines and trigger asynchronous email notifications for monitoring

Project Overview

This project simulates a real-world cloud infrastructure monitoring workflow where:

Azure DevOps pipelines deploy Terraform infrastructure
Deployment events are streamed into Apache Kafka
A monitoring consumer continuously checks deployment status
Failed deployments trigger alerts into Azure Queue
Email notifications are sent for critical failures

This project demonstrates:

Event-driven architecture
Real-time streaming using Apache Kafka
Cloud messaging using Azure Queue
Infrastructure monitoring concepts
Python automation
CI/CD integration concepts
