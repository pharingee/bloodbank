from base import *

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL + '/static/'
MEDIA_URL = S3_URL + '/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
