# Listing all S3 Buckets and calculating its size from a account 
Configure your AWS credenatils - # aws configure \
Execute # Python size2.py\
For the PY - size2.py  it create output CSV file in your same folder for all the Buckets in AWS account\
Size of the bucket will be in MBs\
return '{0:.2f} MB'.format(bucket_size_bytes/1024/1024)  --> MB\
return '{0:.2f} KB'.format(bucket_size_bytes/1024) --> KB\
