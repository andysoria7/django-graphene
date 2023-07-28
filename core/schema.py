import graphene
from graphene_django import DjangoObjectType
from books.models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "description", "created_at", "updated_at")

# Clase para crear un libro.
class CreateBookMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        
    book = graphene.Field(BookType)
    
    def mutate(self,info,title,description):
       book = Book(title=title, description=description)
       book.save()
       return CreateBookMutation(book=book)
   
# Clase para eliminar un libro
class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    message = graphene.String()
    
    def mutate(self,info,id):
        book = Book.objects.get(pk=id)
        book.delete()
        return DeleteBookMutation(message="Book Deleted")
    
# Clase para actualizar un libro
class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
    book = graphene.Field(BookType)
    
    def mutate(self,info,id,title,description):
        book = Book.objects.get(pk=id)
        book.title = title
        book.description = description
        book.save()
        return UpdateBookMutation(book=book)
    
    
    
class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello!")
    books = graphene.List(BookType) # Para obtener una lista de libros.
    book = graphene.Field(BookType, id=graphene.ID()) # Para obtener un libro de acuerdo al id.
    
    # Funcion para obtener una lista de libros.
    def resolve_books(self, info):
        return Book.objects.all()
    
    # Funcion para obtener un libro de acuerdo al id.
    def resolve_book(self,info,id):
        return Book.objects.get(pk=id)
    
# Clase padre con sus metodos.
class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()
    update_book= UpdateBookMutation.Field()
      
schema = graphene.Schema(query=Query, mutation=Mutation)

        