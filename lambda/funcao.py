def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Olá, mundo!'
    }

# if __name__ == "__main__":
#     a = lambda_handler(None, None)
#     print(a)