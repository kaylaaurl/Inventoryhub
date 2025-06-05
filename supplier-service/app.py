from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, load_schema_from_path
from resolvers import query, mutation
from models import Base, engine

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, [query, mutation])

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset=utf-8/>
        <title>GraphQL Playground</title>
        <link rel="stylesheet"
          href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css"
        />
        <link rel="shortcut icon"
          href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/favicon.png"
        />
        <script
          src="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"
        ></script>
      </head>
      <body>
        <div id="root"></div>
        <script>
          window.addEventListener('load', function (event) {
            GraphQLPlayground.init(document.getElementById('root'), {
              endpoint: '/graphql'
            })
          })
        </script>
      </body>
    </html>
    """, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=True)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True, port=5004)
