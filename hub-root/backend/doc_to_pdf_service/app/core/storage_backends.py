from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# if we use default_acl = 'public-read'
# it will raise  the following error
# An error occurred (AccessControlListNotSupported) when calling the PutObject operation: The bucket does not allow ACLs


class StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION
    # default_acl = 'public-read'

class PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    # default_acl = 'public-read'
    
class PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    # default_acl = 'private'