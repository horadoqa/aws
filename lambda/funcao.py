def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Olá, mundo!'
    }

lambda_handler()

