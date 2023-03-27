from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt =models.CharField(max_length=500)
    #image_name = models.CharField(max_length=80)
    image = models.ImageField(upload_to="post", null =True)         # Here post is subfolde name in main folder uploads
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(unique=True, default="",blank=True,
                            null=False, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null = True, related_name="post") # one to many reltionship
    tags = models.ManyToManyField(Tag)

    # def __str__(self) -> str:
    #     return self.title + " Blog"

     

