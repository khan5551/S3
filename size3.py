from __future__ import division
from datetime import datetime, timedelta
import boto3
import math
import sys
import botocore
def human_readable_size(size):
          splitter = ["B", "KB", "MB", "GB", "TB", "PB"]
          splitter_index = 0
          while size > 1024 and splitter_index < 5:
                    splitter_index += 1
                    size = size/1024
                    size = '{:0.2f}'.format(size)
          return '{}{}'.format(size,splitter[splitter_index])
def get_bucket_data(bucket_name):
          s3 = boto3.resource('s3')
          bucket = s3.Bucket(bucket_name)
          bucket_object_count = sum(1 for _ in bucket.objects.all())
          total_bucket_size = 0
          print 'Bucket name: {}'.format(bucket.name)
          print 'Bucket created at: {}'.format(bucket.creation_date)
          print 'Bucket objects:'
          for obj in bucket.objects.all():
            bucket_object = s3.Object(bucket.name, obj.key)
            total_bucket_size += int(bucket_object.content_length)
            size_hr = human_readable_size(int(bucket_object.content_length))
            print ' - {size: <10}:{object_name}'.format(size=size_hr,object_name=bucket_object.key)
            print '-----'
            print 'Bucket object count: {}'.format(bucket_object_count)
            print 'Total bucket size:              {}'.format(human_readable_size(total_bucket_size))
            print '-'*20
s3 = boto3.resource('s3', region_name='ap-southeast-1')
s3 = boto3.client('s3')
bl = s3.list_buckets()
try:
      for name in bl.get('Buckets'):
              get_bucket_data(name.get('Name'))
except botocore.exceptions.ClientError as e:
           print e.response['Error']['Code']