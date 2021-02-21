import boto3

def upload_model(model_path='', s3_bucket='', key_prefix='', aws_profile='default'):
    s3 = boto3.session.Session(profile_name=aws_profile)
    client = s3.client('s3')
    client.upload_file(model_path, s3_bucket, key_prefix)


s3_bucket = 'my-bert-models'
model_path = './model/squad-distilbert.tar.gz'
key_prefix = 'qa/squad-distilbert.tar.gz'
upload_model(model_path, s3_bucket, key_prefix)