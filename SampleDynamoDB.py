import boto3


##boto3については以下。(本サンプルソース含む)
##https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html

##AWS IAMアクセスキーについては以下を参照
##https://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/id_credentials_access-keys.html
##設定ファイルのローカルディレクトリ(Mac)：~/.aws/config

# Get the service resource.
dynamodb = boto3.resource('dynamodb', 'ap-northeast-1')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)
