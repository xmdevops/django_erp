#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@author:    olinex
@time:      2017/11/17 下午10:14
"""

__all__ = ['MessageSerializer']

from .. import models
from rest_framework import serializers
from .content_type import ContentTypeSerializer

class MessageSerializer(serializers.ModelSerializer):
    creater = serializers.PrimaryKeyRelatedField(read_only=True)
    content_type = ContentTypeSerializer(read_only=True)
    create_time = serializers.ReadOnlyField()
    object_id = serializers.ReadOnlyField()

    class Meta:
        model = models.Message
        fields = '__all__'