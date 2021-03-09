
import json

print('Loading function')


def lambda_handler(event, context):
    
    print(event['keyword'])

    
    return event['keyword']   # Echo back 
    #raise Exception('Something went wrong')

