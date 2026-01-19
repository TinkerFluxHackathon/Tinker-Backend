from rest_framework.serializers import ModelSerializer, SlugRelatedField;
from produtos.models.product import Product;
from uploader.models import Image
from uploader.serializers import ImageSerializer;

class ProductSerializer(ModelSerializer):
    imagem_attachment_key = SlugRelatedField(
        source = 'imagem',
        queryset = Image.objects.all(),
        slug_field = "attachment_key",
        required = False,
        write_only = True,
    )
    
    imagem = ImageSerializer(required=False, read_only = True);

    class Meta:
        model = Product;
        fields = '__all__';