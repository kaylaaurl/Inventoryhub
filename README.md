# 📦 Inventory Hub

Inventory Hub adalah sistem manajemen inventaris berbasis **microservices** yang terdiri dari beberapa backend service terpisah dan satu frontend terintegrasi. Setiap service berjalan secara independen dan saling terhubung melalui **GraphQL API**.

---

## 🧩 Daftar Service

| No | Service              | Fungsi                                    | Endpoint                           |
|----|----------------------|-------------------------------------------|------------------------------------|
| 1  | Category Service     | Mengelola kategori barang                 | `http://localhost:5001/graphql`    |
| 2  | Inventory Service    | Mengelola data barang dan stok            | `http://localhost:5002/graphql`    |
| 3  | Supplier Service     | Mengelola data supplier/pemasok barang    | `http://localhost:5010/graphql`    |
| 4  | User Service         | Mengelola data user/admin sistem          | `http://localhost:5004/graphql`    |
| 5  | Notification Service | Mengelola notifikasi aktivitas inventaris | `http://localhost:5005/graphql`    |
| 6  | Frontend             | Antarmuka web                             | `http://localhost:8000/`           |

---

## 🚀 Cara Menjalankan Project

### 🔁 1. Jalankan dengan Docker (Rekomendasi)

Pastikan Docker sudah terinstall.

```bash
docker-compose up --build
```

Semua service akan berjalan otomatis sesuai `docker-compose.yml`.

### 🔧 2. Jalankan Manual (Tanpa Docker)

Masuk ke masing-masing folder service, lalu jalankan:

```bash
pip install -r requirements.txt
python app.py
```

Lakukan ini untuk semua folder: `category-service`, `inventory-service`, `supplier-service`, `user-service`, `notifications-service`, dan `frontend`.

---

## 📋 Contoh Query & Mutation CRUD

### 👤 User Service – `http://localhost:5004/graphql`

#### Get All Users
```graphql
query {
  getUsers {
    id
    username
    role
  }
}
```

#### Register User
```graphql
mutation {
  register(username: "staff", password: "staff123", role: "staff") {
    id
    username
    role
  }
}
```

#### Update User
```graphql
mutation {
  updateUser(id: 1, username: "admin_updated", role: "staff_logistik") {
    id
    username
    role
  }
}
```

#### Delete User
```graphql
mutation {
  deleteUser(id: 2)
}
```

---

### 📦 Inventory Service – `http://localhost:5002/graphql`

#### Get All Items
```graphql
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
```

#### Add Item
```graphql
mutation {
  addItem(
    name: "Printer Epson",
    category: "Elektronik",
    quantity: 10,
    location: "Gudang A",
    status: "available"
  ) {
    id
    name
  }
}
```

#### Update Item
```graphql
mutation {
  updateItem(
    id: "4",
    name: "mandi sayang",
    category: "wkwkwkw",
    quantity: 7,
    location: "Gudang b",
    status: "available"
  ) {
    id
    name
  }
}
```

#### Delete Item
```graphql
mutation {
  deleteItem(id: 3)
}
```

---

### 🏢 Supplier Service – `http://localhost:5003/graphql`

#### Get All Suppliers
```graphql
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
```

#### Add Supplier
```graphql
mutation {
  addSupplier(
    name: "PT Sumber Makmur",
    contact_person: "Budi Santoso",
    phone: "081234567890",
    email: "budi@sumbermakmur.co.id",
    address: "Jl. Industri No. 123, Jakarta"
  ) {
    id
    name
  }
}
```

#### Update Supplier
```graphql
mutation {
  updateSupplier(
    id: 5,
    name: "PT Sumber Makmur Baru",
    contact_person: "Budi S.",
    phone: "081234567891",
    email: "budi@sumbermakmurbaru.co.id",
    address: "Jl. Baru Industri No. 456, Jakarta"
  ) {
    id
    name
  }
}
```

#### Delete Supplier
```graphql
mutation {
  deleteSupplier(id: 3)
}
```

---

### 📂 Category Service – `http://localhost:5001/graphql`

#### Get All Categories
```graphql
query {
  getCategories {
    id
    name
    description
  }
}
```

#### Add Category
```graphql
mutation {
  addCategory(
    name: "Elektronik",
    description: "Kategori barang-barang elektronik"
  ) {
    id
    name
  }
}
```

#### Update Category
```graphql
mutation {
  updateCategory(
    id: 1,
    name: "Elektronik & Gadget",
    description: "Kategori elektronik dan gadget"
  ) {
    id
    name
  }
}
```

#### Delete Category
```graphql
mutation {
  deleteCategory(id: 1)
}
```

---

### 🔔 Notification Service – `http://localhost:5005/graphql`

#### Get All Notifications
```graphql
query {
  getNotifications {
    id
    user_id
    item_id
    message
    status
  }
}
```

#### Add Notification
```graphql
mutation {
  addNotification(
    user_id: 1,
    item_id: 1001,
    message: "Barang akan segera habis",
    status: "pending"
  ) {
    id
    message
  }
}
```

#### Update Notification
```graphql
mutation {
  updateNotification(
    id: 1,
    message: "Stok barang telah diperbarui",
    status: "read"
  ) {
    id
    message
  }
}
```

#### Delete Notification
```graphql
mutation {
  deleteNotification(id: 1)
}
```

---

## 🌐 Frontend

Akses melalui browser:

```
http://localhost:8000/
```

---

## 🧾 Penutup

Inventory Hub memudahkan pengelolaan inventaris secara **terintegrasi**, **terstruktur**, dan **scalable**. Cocok digunakan untuk perusahaan logistik, retail, dan gudang. Silakan sesuaikan konfigurasi environment & endpoint saat deployment.

---
