# Django GraphQL API with Graphiql
## Books App

This Django project demonstrates the implementation of a GraphQL API using the Graphiql library. It provides a simple and efficient way to interact with the API, enabling clients to query and mutate data in a flexible manner.

## Features

- GraphQL API implementation with Django and Graphiql
- Query data using GraphQL syntax
- Mutate data through GraphQL mutations
- Intuitive and interactive documentation using Graphiql interface
- Secure and efficient data retrieval
- Scalable architecture for handling complex data requirements

## Tech Stack

- Django
- Graphene-Django
- Graphiql
- Python
- GraphQL

## Setup and Installation

To run the Django GraphQL API project locally, follow these steps:

1. Clone the repository or download the project files.
2. Install Python 3.x and Django.
3. Create a virtual environment and activate it.
4. Install project dependencies from `requirements.txt`.
5. Set up the database and run migrations.
6. Start the Django development server.


## Example Queries and Mutations

Here are some example GraphQL queries and mutations that you can try:

- Query all books:

```graphql
query {
  books {
    id
    name
  }
}
