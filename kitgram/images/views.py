from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


class Feed(APIView):

  def get(self, request, format=None):

    user = request.user

    following_users = user.following.all()

    image_list = []

    for following_user in following_users:

      user_images = following_user.images.all()[:2]

      for image in user_images:

        image_list.append(image)

    sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

    serializer = serializers.ImageSerializer(sorted_list, many=True)

    return Response(serializer.data)


class LikeImage(APIView):

  def post(self, request, image_id, format=None):

    user = request.user

    try:
      found_image = models.Image.objects.get(id=image_id)
    except models.Image.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    try:
      preexisting_like = models.Image.objects.get(
        create=user,
        image=found_image
      )

      return Response(status=status.HTTP_304_NOT_MODIFIED)

    except models.Like.DoesNotExist:

      new_like = models.Like.object.create(
        creator=user,
        image=found_image
      )

      new_like.save()

      return Response(status=status.HTTP_201_CREATED)


class UnLikeImage(APIView):

  def delete(self, request, image_id, format=None):

    user = request.user

    try:
      found_image = models.Image.objects.get(id=image_id)
    except models.Image.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    try:
      preexisting_like = models.Image.objects.get(
        create=user,
        image=found_image
      )

      preexisting_like.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except models.Like.DoesNotExist:

      return Response(status=status.HTTP_304_NOT_MODIFIED)


class CommentOnImage(APIView):

  def post(self, request, image_id, format=None):

    user = request.user

    try:

      found_image = models.Image.objects.get(id=image_id)
    
    except models.Image.DoesNotExist:
      
      return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.CommentSerializer(data=request.data)

    if serializer.is_valid():

      serializer.save(creator=user, image=found_image)

      return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    else:

      return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Comment(APIView):

  def delete(self, request, comment_id, format=None):

    user = request.user

    try:

      comment = models.Comment.objects.get(id=comment_id, creator=user)
      
      comment.delete()
      
      return Response(status=status.HTTP_204_NO_CONTENT)

    except models.Comment.DoesNotExist:
      
      return Response(status=status.HTTP_404_NOT_FOUND)


class Search(APIView):

  def get(self, request, format=None):

    hashtags = request.query_params.get('hashtag', None)

    if hashtags is not None:

      hashtags = hashtags.split(",")

      images = models.Image.objects.filter(tags__name__in=hashtags).distinct()
      # deep relation: 오브젝트내의 요소중 오브젝트가 있을 경우 __username을 찾으면 오브젝트내의 username 키를 찾는다 그 뒤에 __in을 넣으면 배열중에서 해당 요소를 갖고 있는 것을 찾는다
      serializer = serializers.CountImageSerializer(images, many=True)

      return Response(data=serializer.data, status=status.HTTP_200_OK)

    else:

      return Response(status=status.HTTP_400_BAD_REQUEST)
