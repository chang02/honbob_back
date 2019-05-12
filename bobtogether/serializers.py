from bobtogether.models import *
from rest_framework import serializers

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'description', 'menu', 'location', 'times')

class MatchingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchingRequest
        fields = ('id', 'user', 'matching', 'requestMessage', 'status')

class MatchingSerializer(serializers.ModelSerializer):
    requests = MatchingRequestSerializer(many = True, read_only = True)

    class Meta:
        model = Matching
        fields = ('id', 'owner', 'restaurant', 'times', 'requestMessage',
                  'filter', 'totalNumber', 'status', 'requests')

class ProfileSerializer(serializers.ModelSerializer):
    requests = MatchingRequestSerializer(many = True, read_only = True)
    matchings = MatchingSerializer(many = True, read_only = True)

    class Meta:
        model = Profile
        fields = ('user', 'joined', 'name', 'gender', 'age', 'school', 'major',
                  'description', 'contact', 'matchings', 'requests')

    def validate(self, data):
        phone = re.compile('01\d-\d{3,4}-\d{4}')
        if re.fullmatch(phone, data.get('contact')) == None:
            raise serializers.ValidationError("연락처가 010-1234-5678 형태로 입력되지 않았습니다.")

        return data

class TimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Times
        fields = ('id', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')

    def validate(self, data):
        for day in ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']:
            time = data.get(day)
            if time >= (1 << 48) or time < 0:
                raise serializers.ValidationError('시간 값이 범위를 벗어났습니다.')

        return data
