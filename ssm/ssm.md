# SSM (Secure Session Manager)

Conectando a uma EC2 na AWS com SSM

1. Criar a instância, já estão com SSM habilitados

2. Criar a role com as permissões

IAM/Roles

Criar


AWS SErvice

EC2

amazonSSMManagerInstanceCore

role-acesso-ssm


Adicionar role no terraform


Polices

Adicionar permissão

Create police

{
    "Version": "2025-02-25",
    "Statement": [
        {
            "Effect": "Alow",
            "Action": "ssm:StartSession",
            "Resource": ["*"]
        }
    ]
}

Name: police-acesso-ssm

aws ssm start-session --target <id da instância>

