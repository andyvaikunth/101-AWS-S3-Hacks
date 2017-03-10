#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create an Bucket in S3
"""

import boto3

if __name__ == "__main__":
#   client = boto3.client('s3')
   client = boto3.client('s3',region_name="us-west-2")
   #bucketname = "101-s3-aws"
   bucketname = "us-west-2.nag"
   print client.put_bucket_tagging(Bucket=bucketname,Tagging={
        'TagSet': [
            {
                'Key': 'Name',
                'Value': 'Nag'
            },
        ]
    })
