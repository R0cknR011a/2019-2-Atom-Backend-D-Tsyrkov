from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from users.models import User
import boto3
import jwt


class UserSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()
    cent_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'url', 'cent_token']

    def get_url(self, user):
        session = boto3.session.Session()
        s3_client = session.client(
            service_name='s3',
            endpoint_url='http://hb.bizmrg.com',
            aws_access_key_id='6Da62vVLUi6AKbFnnRoeA3',
            aws_secret_access_key='gDYg4Bu15yUpNYGKmmpiVNGvLRWhUAJ3m1GGRvg8KTbU',
        )
        return s3_client.generate_presigned_url('get_object', Params={
            'Bucket': 'tsyrkov_messanger_bucket',
            'Key': user.avatar,
        }, ExpiresIn=3600)

    def get_cent_token(self, user):
        return jwt.encode({'sub': user.username}, '6c33f23a-33f9-4edb-9982-7f5fbde64a94').decode()


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'id')
