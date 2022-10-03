import graphene
from graphene_django import DjangoObjectType
from .models import Books


# DjangoObjectType : same as Serializer in REST Framework
# This class creates a GraphQL type for the Book model
# type Book{
#     id: ID!
#     title: String!
#     author: String!
#     published: String!
# }

class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        # fields = ('id', 'title', 'author', 'published')

# now we can create a Query type
# type Query{
#     books: [Book]  ## a query to get all books
# }

class Query(graphene.ObjectType):
    get_books = graphene.List(BooksType)

    def resolve_get_books(self, info):  # resolve_books is a resolver
        return Books.objects.all()   # resolvers are defined inside Query class in graphene

# let's try to make mutations

class CreateBook(graphene.Mutation): #create_book mutation
    class Arguments:
        # input arguments goes here (basically fields or input variables)
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        published = graphene.types.datetime.DateTime()

    # The class attrbutes define the response of the mutation (what to return)
    book = graphene.Field(BooksType)

    #All mutation logic goes here
    @classmethod
    def mutate(cls, root, info, title, author, published=None):
        book = Books.objects.create(
            title=title,
            author=author,
            published=published
        )
        return CreateBook(book=book)


    
class Mutation(graphene.ObjectType):
    add_book = CreateBook.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)