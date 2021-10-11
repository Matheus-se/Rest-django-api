# Rest-django-api

<img src="https://i.pinimg.com/originals/36/54/e7/3654e7e5cd4023d6a65bb172fb178be0.jpg" width="100%" />

## Before start

All the api documentation and description can be found at: https://documenter.getpostman.com/view/12570308/UV5RmKnT#4ecd0612-7d60-4422-b4a8-50ab01c25080

## Introduction

The vendor catalog API provide access for registration, searching, deletion, and updating of vendors and products. Each vendor has his API key, preventing accidental deletions and updations of other vendor's data and products.

##Especifications

This API was built using django rest framework, deployed in heroku and using PostgreSQL as database. The database was deployed in AWS RDS with a custom VPC, subnets, internet gateway, route table, and security groups.
