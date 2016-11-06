from rest_framework import serializers

from badgify.models.badge import Badge
from django.contrib.auth.models import User
from sketchfab.models import Model3d

__author__ = 'Pierre Rodier | pierre@buffactory.com'


class Model3dSerializer(serializers.ModelSerializer):
    """
    Api serializer for Badge model.
    """

    user = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = Model3d
        fields = ('id', 'name', 'picture', 'user')

    def create(self, validated_data):
        return super(Model3dSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        return super(Model3dSerializer, self).update(instance, validated_data)

    def to_representation(self, value):
        return super(Model3dSerializer, self).to_representation(value)

    def to_internal_value(self, data):
        return super(Model3dSerializer, self).to_internal_value(data)


class BadgeSerializer(serializers.ModelSerializer):
    """
    Api serializer for Badge model.
    """

    class Meta:
        model = Badge
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        return super(BadgeSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        return super(BadgeSerializer, self).update(instance, validated_data)

    def to_representation(self, value):
        return super(BadgeSerializer, self).to_representation(value)

    def to_internal_value(self, data):
        return super(BadgeSerializer, self).to_internal_value(data)


class UserSerializer(serializers.ModelSerializer):
    """
    Api serializer for Django User model.
    """

    badges = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='badge-detail'
    )

    model3ds = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='model3d-detail'
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'model3ds', 'badges')

    def create(self, validated_data):
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        return super(UserSerializer, self).update(instance, validated_data)

    def to_representation(self, value):
        return super(UserSerializer, self).to_representation(value)

    def to_internal_value(self, data):
        return super(UserSerializer, self).to_internal_value(data)