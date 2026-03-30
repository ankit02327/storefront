# 0 All Tables

SHOW TABLES;

```text
| Tables_in_storefront       |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| store_address              |
| store_cart                 |
| store_cartitem             |
| store_collection           |
| store_customer             |
| store_order                |
| store_orderitem            |
| store_product              |
| store_product_promotions   |
| store_promotion            |
| store_review               |
| tags_likeditem             |
| tags_tag                   |
| tags_taggeditem            |
```

---

# 1 store_address

`DESCRIBE store_address;`

```text
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | bigint       | NO   | PRI |         | auto_increment |
| street      | varchar(255) | NO   |     |         |                |
| city        | varchar(255) | NO   |     |         |                |
| customer_id | bigint       | NO   | MUL |         |                |
```

`SHOW CREATE TABLE store_address;`

```text
| Table         | Create Table                                                                                                                                                                                                                                             |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_address | CREATE TABLE `store_address` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `street` varchar(255) NOT NULL,¶ `city` varchar(255) NOT NULL,¶ `customer_id` bigint NOT NULL,¶ PRIMARY KEY (`id`),¶ KEY `store_address_customer_id_080cf871_fk_store_customer_id` |
```

```sql
CREATE TABLE `store_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `street` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_address_customer_id_080cf871_fk_store_customer_id` (`customer_id`),
  CONSTRAINT `store_address_customer_id_080cf871_fk_store_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `store_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 2 store_cart

`DESCRIBE store_cart;`

```text
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| id         | bigint      | NO   | PRI |         | auto_increment |
| created_at | datetime(6) | NO   |     |         |                |
```

`SHOW CREATE TABLE store_cart;`

```text
| Table      | Create Table                                                                                                                                                                                 |
+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_cart | CREATE TABLE `store_cart` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `created_at` datetime(6) NOT NULL,¶ PRIMARY KEY (`id`)¶) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
```

```sql
CREATE TABLE `store_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 3 store_cartitem

`DESCRIBE store_cartitem;`

```text
| Field      | Type              | Null | Key | Default | Extra          |
+------------+-------------------+------+-----+---------+----------------+
| id         | bigint            | NO   | PRI |         | auto_increment |
| quantity   | smallint unsigned | NO   |     |         |                |
| cart_id    | bigint            | NO   | MUL |         |                |
| product_id | bigint            | NO   | MUL |         |                |
```

`SHOW CREATE TABLE store_cartitem;`

```text
| Table          | Create Table                                                                                                                                                                                                                                              |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_cartitem | CREATE TABLE `store_cartitem` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `quantity` smallint unsigned NOT NULL,¶ `cart_id` bigint NOT NULL,¶ `product_id` bigint NOT NULL,¶ PRIMARY KEY (`id`),¶ KEY `store_cartitem_cart_id_4f60ac05_fk_store_cart_id` (`c |
```

```sql
CREATE TABLE `store_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` smallint unsigned NOT NULL,
  `cart_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_cartitem_cart_id_4f60ac05_fk_store_cart_id` (`cart_id`),
  KEY `store_cartitem_product_id_4238d443_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_cartitem_cart_id_4f60ac05_fk_store_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `store_cart` (`id`),
  CONSTRAINT `store_cartitem_product_id_4238d443_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`),
  CONSTRAINT `store_cartitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 4 store_collection

`DESCRIBE store_collection;`

```text
| Field               | Type         | Null | Key | Default | Extra          |
+---------------------+--------------+------+-----+---------+----------------+
| id                  | bigint       | NO   | PRI |         | auto_increment |
| title               | varchar(255) | NO   |     |         |                |
| featured_product_id | bigint       | YES  | MUL |         |                |
```

`SHOW CREATE TABLE store_collection;`

```text
| Table            | Create Table                                                                                                                                                                                                                                               |
+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_collection | CREATE TABLE `store_collection` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `title` varchar(255) NOT NULL,¶ `featured_product_id` bigint DEFAULT NULL,¶ PRIMARY KEY (`id`),¶ KEY `store_collection_featured_product_id_001d6455_fk_store_pro` (`featured_prod |
```

```sql
CREATE TABLE `store_collection` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `featured_product_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `store_collection_featured_product_id_001d6455_fk_store_pro` (`featured_product_id`),
  CONSTRAINT `store_collection_featured_product_id_001d6455_fk_store_pro` FOREIGN KEY (`featured_product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 5 store_customer

`DESCRIBE store_customer;`

```text
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | bigint       | NO   | PRI |         | auto_increment |
| first_name | varchar(255) | NO   |     |         |                |
| last_name  | varchar(255) | NO   |     |         |                |
| email      | varchar(254) | NO   | UNI |         |                |
| phone      | varchar(255) | NO   |     |         |                |
| birth_date | date         | YES  |     |         |                |
| membership | varchar(1)   | NO   |     |         |                |
```

`SHOW CREATE TABLE store_customer;`

```text
| Table          | Create Table                                                                                                                                                                                                                                             |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_customer | CREATE TABLE `store_customer` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `first_name` varchar(255) NOT NULL,¶ `last_name` varchar(255) NOT NULL,¶ `email` varchar(254) NOT NULL,¶ `phone` varchar(255) NOT NULL,¶ `birth_date` date DEFAULT NULL,¶ `member |
```

```sql
CREATE TABLE `store_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `membership` varchar(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 6 store_order

`DESCRIBE store_order;`

```text
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| id             | bigint      | NO   | PRI |         | auto_increment |
| placed_at      | datetime(6) | NO   |     |         |                |
| payment_status | varchar(1)  | NO   |     |         |                |
| customer_id    | bigint      | NO   | MUL |         |                |
```

`SHOW CREATE TABLE store_order;`

```text
| Table       | Create Table                                                                                                                                                                                                                                              |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_order | CREATE TABLE `store_order` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `placed_at` datetime(6) NOT NULL,¶ `payment_status` varchar(1) NOT NULL,¶ `customer_id` bigint NOT NULL,¶ PRIMARY KEY (`id`),¶ KEY `store_order_customer_id_13d6d43e_fk_store_custome |
```

```sql
CREATE TABLE `store_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `placed_at` datetime(6) NOT NULL,
  `payment_status` varchar(1) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_order_customer_id_13d6d43e_fk_store_customer_id` (`customer_id`),
  CONSTRAINT `store_order_customer_id_13d6d43e_fk_store_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `store_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 7 store_orderitem

`DESCRIBE store_orderitem;`

```text
| Field      | Type              | Null | Key | Default | Extra          |
+------------+-------------------+------+-----+---------+----------------+
| id         | bigint            | NO   | PRI |         | auto_increment |
| quantity   | smallint unsigned | NO   |     |         |                |
| unit_price | decimal(6,2)      | NO   |     |         |                |
| order_id   | bigint            | NO   | MUL |         |                |
| product_id | bigint            | NO   | MUL |         |                |
```

`SHOW CREATE TABLE store_orderitem;`

```text
| Table           | Create Table                                                                                                                                                                                                                                             |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_orderitem | CREATE TABLE `store_orderitem` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `quantity` smallint unsigned NOT NULL,¶ `unit_price` decimal(6,2) NOT NULL,¶ `order_id` bigint NOT NULL,¶ `product_id` bigint NOT NULL,¶ PRIMARY KEY (`id`),¶ KEY `store_orderit |
```

```sql
CREATE TABLE `store_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` smallint unsigned NOT NULL,
  `unit_price` decimal(6,2) NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_orderitem_order_id_acf8722d_fk_store_order_id` (`order_id`),
  KEY `store_orderitem_product_id_f2b098d4_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_orderitem_order_id_acf8722d_fk_store_order_id` FOREIGN KEY (`order_id`) REFERENCES `store_order` (`id`),
  CONSTRAINT `store_orderitem_product_id_f2b098d4_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`),
  CONSTRAINT `store_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 8 store_product

`DESCRIBE store_product;`

```text
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | bigint       | NO   | PRI |         | auto_increment |
| title         | varchar(255) | NO   |     |         |                |
| description   | longtext     | YES  |     |         |                |
| price         | decimal(6,2) | NO   |     |         |                |
| inventory     | int          | NO   |     |         |                |
| last_update   | datetime(6)  | NO   |     |         |                |
| collection_id | bigint       | NO   | MUL |         |                |
| slug          | varchar(50)  | NO   | MUL |         |                |
```

`SHOW CREATE TABLE store_product;`

```text
| Table         | Create Table                                                                                                                                                                                                                                             |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_product | CREATE TABLE `store_product` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `title` varchar(255) NOT NULL,¶ `description` longtext,¶ `price` decimal(6,2) NOT NULL,¶ `inventory` int NOT NULL,¶ `last_update` datetime(6) NOT NULL,¶ `collection_id` bigint NO |
```

```sql
CREATE TABLE `store_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` longtext,
  `price` decimal(6,2) NOT NULL,
  `inventory` int NOT NULL,
  `last_update` datetime(6) NOT NULL,
  `collection_id` bigint NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_product_collection_id_2914d2ba_fk_store_collection_id` (`collection_id`),
  KEY `store_product_slug_6de8ee4b` (`slug`),
  CONSTRAINT `store_product_collection_id_2914d2ba_fk_store_collection_id` FOREIGN KEY (`collection_id`) REFERENCES `store_collection` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 9 store_product_promotions

`DESCRIBE store_product_promotions;`

```text
| Field        | Type   | Null | Key | Default | Extra          |
+--------------+--------+------+-----+---------+----------------+
| id           | bigint | NO   | PRI |         | auto_increment |
| product_id   | bigint | NO   | MUL |         |                |
| promotion_id | bigint | NO   | MUL |         |                |
```

`SHOW CREATE TABLE store_product_promotions;`

```text
| Table                    | Create Table                                                                                                                                                                                                                                               |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_product_promotions | CREATE TABLE `store_product_promotions` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `product_id` bigint NOT NULL,¶ `promotion_id` bigint NOT NULL,¶ PRIMARY KEY (`id`),¶ UNIQUE KEY `store_product_promotions_product_id_promotion_id_d02f5543_uniq` (`produc |
```

```sql
CREATE TABLE `store_product_promotions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_id` bigint NOT NULL,
  `promotion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `store_product_promotions_product_id_promotion_id_d02f5543_uniq` (`product_id`,`promotion_id`),
  KEY `store_product_promot_promotion_id_4bd05cf2_fk_store_pro` (`promotion_id`),
  CONSTRAINT `store_product_promot_promotion_id_4bd05cf2_fk_store_pro` FOREIGN KEY (`promotion_id`) REFERENCES `store_promotion` (`id`),
  CONSTRAINT `store_product_promotions_product_id_c302ec3a_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 10 store_promotion

`DESCRIBE store_promotion;`

```text
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | bigint       | NO   | PRI |         | auto_increment |
| description | varchar(255) | NO   |     |         |                |
| discount    | double       | NO   |     |         |                |
```

`SHOW CREATE TABLE store_promotion;`

```text
| Table           | Create Table                                                                                                                                                                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_promotion | CREATE TABLE `store_promotion` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `description` varchar(255) NOT NULL,¶ `discount` double NOT NULL,¶ PRIMARY KEY (`id`)¶) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
```

```sql
CREATE TABLE `store_promotion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `discount` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 11 store_review

`DESCRIBE store_review;`

```text
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | bigint       | NO   | PRI |         | auto_increment |
| name        | varchar(255) | NO   |     |         |                |
| description | longtext     | NO   |     |         |                |
| date        | date         | NO   |     |         |                |
| product_id  | bigint       | NO   | MUL |         |                |
```

`SHOW CREATE TABLE store_review;`

```text
| Table        | Create Table                                                                                                                                                                                                                                             |
+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store_review | CREATE TABLE `store_review` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `name` varchar(255) NOT NULL,¶ `description` longtext NOT NULL,¶ `date` date NOT NULL,¶ `product_id` bigint NOT NULL,¶ PRIMARY KEY (`id`),¶ KEY `store_review_product_id_abc413b2_f |
```

```sql
CREATE TABLE `store_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_review_product_id_abc413b2_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_review_product_id_abc413b2_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 12 tags_tag

`DESCRIBE tags_tag;`

```text
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | bigint       | NO   | PRI |         | auto_increment |
| label | varchar(255) | NO   |     |         |                |
```

`SHOW CREATE TABLE tags_tag;`

```text
| Table    | Create Table                                                                                                                                                                           |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tags_tag | CREATE TABLE `tags_tag` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `label` varchar(255) NOT NULL,¶ PRIMARY KEY (`id`)¶) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
```

```sql
CREATE TABLE `tags_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `label` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 13 tags_taggeditem

`DESCRIBE tags_taggeditem;`

```text
| Field           | Type         | Null | Key | Default | Extra          |
+-----------------+--------------+------+-----+---------+----------------+
| id              | bigint       | NO   | PRI |         | auto_increment |
| object_id       | int unsigned | NO   |     |         |                |
| content_type_id | int          | NO   | MUL |         |                |
| tag_id          | bigint       | NO   | MUL |         |                |
```

`SHOW CREATE TABLE tags_taggeditem;`

```text
| Table    | Create Table                                                                                                                                                                           |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tags_tag | CREATE TABLE `tags_tag` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `label` varchar(255) NOT NULL,¶ PRIMARY KEY (`id`)¶) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
```

```sql
CREATE TABLE `tags_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `label` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# 14 tags_likeditem

`DESCRIBE tags_likeditem;`

```text
| Field           | Type         | Null | Key | Default | Extra          |
+-----------------+--------------+------+-----+---------+----------------+
| id              | bigint       | NO   | PRI |         | auto_increment |
| object_id       | int unsigned | NO   |     |         |                |
| content_type_id | int          | NO   | MUL |         |                |
| user_id         | int          | NO   | MUL |         |                |
```

`SHOW CREATE TABLE tags_likeditem;`

```text
| Table          | Create Table                                                                                                                                                                                                                                              |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tags_likeditem | CREATE TABLE `tags_likeditem` (¶ `id` bigint NOT NULL AUTO_INCREMENT,¶ `object_id` int unsigned NOT NULL,¶ `content_type_id` int NOT NULL,¶ `user_id` int NOT NULL,¶ PRIMARY KEY (`id`),¶ KEY `tags_likeditem_content_type_id_ef1f0e6a_fk_django_co` (`co |
```

```sql
CREATE TABLE `tags_likeditem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `object_id` int unsigned NOT NULL,
  `content_type_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tags_likeditem_content_type_id_ef1f0e6a_fk_django_co` (`content_type_id`),
  KEY `tags_likeditem_user_id_012f8f02_fk_auth_user_id` (`user_id`),
  CONSTRAINT `tags_likeditem_content_type_id_ef1f0e6a_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `tags_likeditem_user_id_012f8f02_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `tags_likeditem_chk_1` CHECK ((`object_id` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

# Relationships

```sql
SELECT
    table_name,
    column_name,
    referenced_table_name,
    referenced_column_name
FROM information_schema.key_column_usage
WHERE table_schema = DATABASE()
AND referenced_table_name IS NOT NULL
AND table_name IN (
    'store_address',
    'store_cart',
    'store_cartitem',
    'store_collection',
    'store_customer',
    'store_order',
    'store_orderitem',
    'store_product',
    'store_product_promotions',
    'store_promotion',
    'store_review',
    'tags_tag',
    'tags_taggeditem',
    'tags_likeditem'
);
```

```text
| TABLE_NAME               | COLUMN_NAME         | REFERENCED_TABLE_NAME | REFERENCED_COLUMN_NAME |
+--------------------------+---------------------+-----------------------+------------------------+
| store_address            | customer_id         | store_customer        | id                     |
| store_cartitem           | cart_id             | store_cart            | id                     |
| store_cartitem           | product_id          | store_product         | id                     |
| store_collection         | featured_product_id | store_product         | id                     |
| store_order              | customer_id         | store_customer        | id                     |
| store_orderitem          | order_id            | store_order           | id                     |
| store_orderitem          | product_id          | store_product         | id                     |
| store_product            | collection_id       | store_collection      | id                     |
| store_product_promotions | product_id          | store_product         | id                     |
| store_product_promotions | promotion_id        | store_promotion       | id                     |
| store_review             | product_id          | store_product         | id                     |
| tags_likeditem           | content_type_id     | django_content_type   | id                     |
| tags_likeditem           | user_id             | auth_user             | id                     |
| tags_taggeditem          | content_type_id     | django_content_type   | id                     |
| tags_taggeditem          | tag_id              | tags_tag              | id                     |
```
