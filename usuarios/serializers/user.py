from rest_framework.serializers import ModelSerializer, SlugRelatedField;
from usuarios.models.user import User;
from uploader.models import Image;
from uploader.serializers import ImageSerializer;

class UserSerializer(ModelSerializer):

    photo_attachment_key = SlugRelatedField(
        source = 'photo',
        queryset = Image.objects.all(),
        slug_field = "attachment_key",
        required = False,
        write_only = True,
    )

    photo = ImageSerializer(required = False, read_only = True);

    class Meta:
        model = User;
        fields = '__all__';
