from flask import Flask, render_template, request, redirect, url_for, Response
import requests

app = Flask(__name__)

GRAPHQL_ENDPOINTS = {
    "user" : "http://user-service:5001/graphql",
    "supplier" : "http://supplier-service:5003/graphql",
    "inventory" : "http://inventory-service:5002/graphql",
    "notification" : "http://notifications-service:5005/graphql",
    "category" : "http://category-service:5004/graphql",
}

@app.route("/")
def index():
    return render_template("index.html")

# ------------------- USER SERVICE -------------------
@app.route("/user", methods=["GET", "POST"])
def user():
    endpoint = GRAPHQL_ENDPOINTS["user"]

    if request.method == "POST":
        action = request.form.get("action")
        if action == "add":
            query = """
            mutation Register($username: String!, $password: String!, $role: String!) {
              register(username: $username, password: $password, role: $role) {
                id
              }
            }
            """
            variables = {
                "username": request.form["username"],
                "password": request.form["password"],
                "role": request.form["role"]
            }
            requests.post(endpoint, json={"query": query, "variables": variables})

        elif action == "delete":
            query = """
            mutation DeleteUser($id: ID!) {
              deleteUser(id: $id)
            }
            """
            variables = {"id": request.form["id"]}
            requests.post(endpoint, json={"query": query, "variables": variables})

        elif action == "update":
            query = """
            mutation UpdateUser($id: ID!, $username: String, $password: String, $role: String) {
              updateUser(id: $id, username: $username, password: $password, role: $role) {
                id
              }
            }
            """
            variables = {
                "id": request.form["id"],
                "username": request.form.get("username"),
                "password": request.form.get("password"),
                "role": request.form.get("role")
            }
            requests.post(endpoint, json={"query": query, "variables": variables})

        return redirect(url_for("user"))

    query = """
    query {
      getUsers {
        id
        username
        role
      }
    }
    """
    response = requests.post(endpoint, json={"query": query})
    users = response.json().get("data", {}).get("getUsers", [])

    return render_template("user.html", users=users)

# ------------------- INVENTORY SERVICE -------------------
@app.route("/inventory", methods=["GET", "POST"])
def inventory():
    endpoint = GRAPHQL_ENDPOINTS["inventory"]

    if request.method == "POST":
        action = request.form.get("action")
        if action == "add":
            query = """
            mutation AddItem($name: String!, $category: String!, $quantity: Int!, $location: String, $status: String) {
              addItem(name: $name, category: $category, quantity: $quantity, location: $location, status: $status) {
                id
              }
            }
            """
            variables = {
                "name": request.form["name"],
                "category": request.form["category"],
                "quantity": int(request.form["quantity"]),
                "location": request.form.get("location"),
                "status": request.form.get("status")
            }
            requests.post(endpoint, json={"query": query, "variables": variables})

        elif action == "delete":
            query = """
            mutation DeleteItem($id: ID!) {
              deleteItem(id: $id)
            }
            """
            variables = {"id": request.form["id"]}
            requests.post(endpoint, json={"query": query, "variables": variables})

        elif action == "update":
            query = """
            mutation UpdateItem($id: ID!, $name: String, $category: String, $quantity: Int, $location: String, $status: String) {
              updateItem(id: $id, name: $name, category: $category, quantity: $quantity, location: $location, status: $status) {
                id
              }
            }
            """
            variables = {
                "id": request.form["id"],
                "name": request.form.get("name"),
                "category": request.form.get("category"),
                "quantity": int(request.form.get("quantity", 0)),
                "location": request.form.get("location"),
                "status": request.form.get("status")
            }
            requests.post(endpoint, json={"query": query, "variables": variables})

        return redirect(url_for("inventory"))

    query = """
    query {
      getItems {
        id
        name
        category
        quantity
        location
        status
      }
    }
    """
    response = requests.post(endpoint, json={"query": query})
    items = response.json().get("data", {}).get("getItems", [])

    return render_template("inventory.html", items=items)

# ------------------- CATEGORY SERVICE -------------------
@app.route("/category", methods=["GET", "POST"])
def category():
    endpoint = GRAPHQL_ENDPOINTS["category"]

    if request.method == "POST":
        action = request.form.get("action")
        if action == "add":
            query = """
            mutation AddCategory($name: String!, $description: String) {
              addCategory(name: $name, description: $description) {
                id
              }
            }
            """
            variables = {
                "name": request.form["name"],
                "description": request.form.get("description")
            }
            requests.post(endpoint, json={"query": query, "variables": variables})

        elif action == "delete":
            query = """
            mutation DeleteCategory($id: ID!) {
              deleteCategory(id: $id)
            }
            """
            variables = {"id": request.form["id"]}
            requests.post(endpoint, json={"query": query, "variables": variables})

        elif action == "update":
            query = """
            mutation UpdateCategory($id: ID!, $name: String, $description: String) {
              updateCategory(id: $id, name: $name, description: $description) {
                id
              }
            }
            """
            variables = {
                "id": request.form["id"],
                "name": request.form.get("name"),
                "description": request.form.get("description")
            }
            requests.post(endpoint, json={"query": query, "variables": variables})

        return redirect(url_for("category"))

    query = """
    query {
      getCategories {
        id
        name
        description
      }
    }
    """
    response = requests.post(endpoint, json={"query": query})
    categories = response.json().get("data", {}).get("getCategories", [])

    return render_template("category.html", categories=categories)

# ------------------- SUPPLIER SERVICE -------------------
@app.route("/supplier", methods=["GET", "POST"])
def supplier():
    endpoint = GRAPHQL_ENDPOINTS["supplier"]

    if request.method == "POST":
        action = request.form.get("action")
        if action == "add":
            query = """
            mutation AddSupplier($name: String!, $contact_person: String, $phone: String, $email: String, $address: String) {
              addSupplier(name: $name, contact_person: $contact_person, phone: $phone, email: $email, address: $address) {
                id
              }
            }
            """
            variables = {
                "name": request.form["name"],
                "contact_person": request.form.get("contact_person"),
                "phone": request.form.get("phone"),
                "email": request.form.get("email"),
                "address": request.form.get("address")
            }
            requests.post(endpoint, json={"query": query, "variables": variables})

        elif action == "delete":
            query = """
            mutation DeleteSupplier($id: ID!) {
              deleteSupplier(id: $id)
            }
            """
            variables = {"id": request.form["id"]}
            requests.post(endpoint, json={"query": query, "variables": variables})

        elif action == "update":
            query = """
            mutation UpdateSupplier($id: ID!, $name: String, $contact_person: String, $phone: String, $email: String, $address: String) {
              updateSupplier(id: $id, name: $name, contact_person: $contact_person, phone: $phone, email: $email, address: $address) {
                id
              }
            }
            """
            variables = {
                "id": request.form["id"],
                "name": request.form.get("name"),
                "contact_person": request.form.get("contact_person"),
                "phone": request.form.get("phone"),
                "email": request.form.get("email"),
                "address": request.form.get("address")
            }
            requests.post(endpoint, json={"query": query, "variables": variables})

        return redirect(url_for("supplier"))

    query = """
    query {
      getSuppliers {
        id
        name
        contact_person
        phone
        email
        address
      }
    }
    """
    response = requests.post(endpoint, json={"query": query})
    suppliers = response.json().get("data", {}).get("getSuppliers", [])

    return render_template("supplier.html", suppliers=suppliers)

# ------------------- NOTIFICATION SERVICE -------------------
@app.route("/notification", methods=["GET", "POST"])
def notification():
    endpoint = GRAPHQL_ENDPOINTS["notification"]

    if request.method == "POST":
        action = request.form.get("action")
        if action == "add":
            query = """
            mutation AddNotification($user_id: Int!, $item_id: Int!, $message: String!, $status: String) {
              addNotification(user_id: $user_id, item_id: $item_id, message: $message, status: $status) {
                id
              }
            }
            """
            variables = {
                "user_id": int(request.form["user_id"]),
                "item_id": int(request.form["item_id"]),
                "message": request.form["message"],
                "status": request.form.get("status")
            }
            requests.post(endpoint, json={"query": query, "variables": variables})

        elif action == "delete":
            query = """
            mutation DeleteNotification($id: ID!) {
              deleteNotification(id: $id)
            }
            """
            variables = {"id": request.form["id"]}
            requests.post(endpoint, json={"query": query, "variables": variables})

        return redirect(url_for("notification"))

    query = """
    query {
      getNotifications {
        id
        user_id
        item_id
        message
        status
      }
    }
    """
    response = requests.post(endpoint, json={"query": query})
    notifications = response.json().get("data", {}).get("getNotifications", [])

    return render_template("notification.html", notifications=notifications)

@app.route("/graphql", methods=["POST"])
def proxy_user_graphql():
    user_graphql_url = "http://user-service:5001/graphql"
    resp = requests.post(user_graphql_url, json=request.get_json())
    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))

@app.route("/inventory-graphql", methods=["POST"])
def proxy_inventory_graphql():
    inventory_graphql_url = "http://inventory-service:5002/graphql"
    resp = requests.post(inventory_graphql_url, json=request.get_json())
    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))

@app.route("/category-graphql", methods=["POST"])
def proxy_category_graphql():
    category_graphql_url = "http://category-service:5004/graphql"
    resp = requests.post(category_graphql_url, json=request.get_json())
    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))

@app.route("/supplier-graphql", methods=["POST"])
def proxy_supplier_graphql():
    supplier_graphql_url = "http://supplier-service:5003/graphql"
    resp = requests.post(supplier_graphql_url, json=request.get_json())
    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))

@app.route("/notification-graphql", methods=["POST"])
def proxy_notification_graphql():
    notification_graphql_url = "http://notifications-service:5005/graphql"
    resp = requests.post(notification_graphql_url, json=request.get_json())
    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
