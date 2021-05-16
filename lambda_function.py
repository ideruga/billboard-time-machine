import json
import main


def lambda_handler(event, context):
    main.fill_playlist()
    return {
        'statusCode': 200,
        'body': json.dumps('Playlist regenerated')
    }
