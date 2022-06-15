from rest_framework import generics, serializers
from rest_framework.response import Response
from .models import Match, Team, Comment

class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('team_1_name', 'team_2_name', 'team_1_score', 'team_2_score', 'match_date', 'match_set')

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'rank', 'win', 'defeat', 'v_point', 'info')

class CommentListSerializer(serializers.ModelSerializer):
    author_email = serializers.CharField(source='author.email')
    author_name = serializers.CharField(source='author.name')
    team_name = serializers.CharField(source="team.name")
    class Meta:
        model = Comment
        fields = ['author_email', 'author_name', 'team_name', 'contents']

class MatchListView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)
