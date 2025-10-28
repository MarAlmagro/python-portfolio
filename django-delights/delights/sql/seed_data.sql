-- seed_data.sql (para SQLite)
-- Run: sqlite3 db.sqlite3 < delights/sql/seed_data.sql
-- To avoid duplicate key errors, existing data is deleted before insertion

-- Delete existing data first  (important for reuse)
DELETE FROM delights_orderitem;
DELETE FROM delights_order;
DELETE FROM delights_customer;
DELETE FROM delights_menu_dishes;
DELETE FROM delights_menu;
DELETE FROM delights_dish_chefs;
DELETE FROM delights_dish_tags;
DELETE FROM delights_dish_ingredients;
DELETE FROM delights_dish;
DELETE FROM delights_allergen_ingredients;
DELETE FROM delights_allergen;
DELETE FROM delights_ingredient;
DELETE FROM delights_tag;
DELETE FROM delights_chef;
DELETE FROM delights_category;

-- Categories
INSERT INTO delights_category (id, name) VALUES
  (1, 'Starters'),
  (2, 'Main Courses'),
  (3, 'Desserts');

-- Chefs
INSERT INTO delights_chef (id, name) VALUES
  (1, 'Alice Brown'),
  (2, 'Marco Rossi'),
  (3, 'Li Wei');

-- Ingredients
INSERT INTO delights_ingredient (id, name) VALUES
  (1, 'Tomato'),
  (2, 'Mozzarella'),
  (3, 'Basil'),
  (4, 'Chocolate'),
  (5, 'Flour'),
  (6, 'Eggs');

-- Tags
INSERT INTO delights_tag (id, name) VALUES
  (1, 'Vegetarian'),
  (2, 'Spicy'),
  (3, 'Gluten-Free');

-- Allergens
INSERT INTO delights_allergen (id, name) VALUES
  (1, 'Gluten'),
  (2, 'Egg');
INSERT INTO delights_allergen_ingredients (allergen_id, ingredient_id) VALUES
  (1, 5),  -- Gluten -> Flour
  (2, 6);  -- Egg -> Eggs

-- Dishes
INSERT INTO delights_dish (id, name, description, price, category_id) VALUES
  (1, 'Caprese Salad', 'Fresh tomato, mozzarella and basil', 7.50, 1),
  (2, 'Spaghetti al Pomodoro', 'Classic pasta with tomato sauce', 10.00, 2),
  (3, 'Chocolate Cake', 'Dark chocolate layered cake', 5.50, 3);

-- Dishes: ingredients
INSERT INTO delights_dish_ingredients (dish_id, ingredient_id) VALUES
  (1, 1), (1, 2), (1, 3),     -- Caprese Salad
  (2, 1), (2, 5), (2, 6),     -- Spaghetti
  (3, 4), (3, 5), (3, 6);     -- Chocolate Cake

-- Dishes: tags
INSERT INTO delights_dish_tags (dish_id, tag_id) VALUES
  (1, 1),
  (2, 2),
  (3, 3);

-- Dishes: chefs
INSERT INTO delights_dish_chefs (dish_id, chef_id) VALUES
  (1, 1),
  (2, 2),
  (3, 3);

-- Menus
INSERT INTO delights_menu (id, name) VALUES
  (1, 'Lunch Menu'),
  (2, 'Dinner Menu');
INSERT INTO delights_menu_dishes (menu_id, dish_id) VALUES
  (1, 1), (1, 2),
  (2, 2), (2, 3);

-- Customers
INSERT INTO delights_customer (id, name, email) VALUES
  (1, 'John Smith', 'john@example.com'),
  (2, 'Elena García', 'elena@example.com');

-- Orders
INSERT INTO delights_order (id, customer_id, created_at) VALUES
  (1, 1, '2025-10-01 12:00:00'),
  (2, 2, '2025-10-02 13:30:00');

-- Order Items
INSERT INTO delights_orderitem (id, order_id, dish_id, quantity) VALUES
  (1, 1, 1, 2),  -- 2x Caprese Salad
  (2, 1, 2, 1),  -- 1x Spaghetti
  (3, 2, 3, 1);  -- 1x Chocolate Cake