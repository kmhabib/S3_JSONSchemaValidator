import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

object = s3.Object('companyjsonlibrary', 'dataSchema.json').put(Body=open('dataSchema.json','rb'))
