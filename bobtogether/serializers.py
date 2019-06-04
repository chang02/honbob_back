from bobtogether.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile')

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'description', 'menu', 'location', 'hours')

class MatchingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchingRequest
        fields = ('id', 'user', 'matching', 'requestMessage', 'status')

class MatchingSerializer(serializers.ModelSerializer):
    requests = MatchingRequestSerializer(many = True, read_only = True)

    class Meta:
        model = Matching
        fields = ('id', 'owner', 'restaurant', 'since', 'till', 'matchingMessage',
                  'keyword', 'maxNumber', 'status', 'requests')

    def validate(self, data):
        if data.get('till') != None and data.get('since') != None:
            duration = data.get('till') - data.get('since')
            if duration.days < 0:
                raise serializers.ValidationError("시작 시간이 종료 시간보다 늦습니다.")

            if duration.days > 0 or duration.seconds > 7200:
                raise serializers.ValidationError("식사는 2시간을 초과할 수 없습니다.")

            if data.get('status') not in (1, 2, 3):
                raise serializers.ValidationError("상태의 값이 범위를 벗어났습니다.")

        return data

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'matching', 'message')

class ProfileSerializer(serializers.ModelSerializer):
    requests = MatchingRequestSerializer(many = True, read_only = True)
    matchings = MatchingSerializer(many = True, read_only = True)
    notifications = NotificationSerializer(many = True, read_only = True)

    class Meta:
        model = Profile
        fields = ('user', 'joined', 'name', 'gender', 'age', 'school', 'major',
                  'description', 'contact', 'matchings', 'requests', 'notifications')

    def validate(self, data):
        import re
        phone = re.compile('01\d-\d{3,4}-\d{4}')
        if re.fullmatch(phone, data.get('contact')) == None:
            raise serializers.ValidationError("연락처가 010-1234-5678 형태로 입력되지 않았습니다.")

        return data

class MatchingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchingReview
        fields = ('id', 'user', 'matching', 'score', 'title', 'detail')

    def validate(self, data):
        if data.get('score') not in (1, 2, 3, 4, 5):
            raise serializers.ValidationError("평점의 값이 범위를 벗어났습니다.")

        return data
