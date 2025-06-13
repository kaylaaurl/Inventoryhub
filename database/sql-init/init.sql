-- DATABASE CREATION
CREATE DATABASE IF NOT EXISTS user_service;
CREATE DATABASE IF NOT EXISTS supplier_service;
CREATE DATABASE IF NOT EXISTS category_service;
CREATE DATABASE IF NOT EXISTS inventory_service;
CREATE DATABASE IF NOT EXISTS notifications_service;

-- ========================
-- TABLE: users
-- ========================
USE user_service;
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(100) NOT NULL UNIQUE,
    `password` VARCHAR(100) NOT NULL,
    `role` VARCHAR(50) NOT NULL, -- admin / staff_logistik
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ========================
-- TABLE: suppliers
-- ========================
USE supplier_service;
CREATE TABLE IF NOT EXISTS `suppliers` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `contact_person` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(20),
    `email` VARCHAR(100),
    `address` VARCHAR(200),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ========================
-- TABLE: categories
-- ========================
USE category_service;
CREATE TABLE IF NOT EXISTS `categories` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL UNIQUE,
    `description` VARCHAR(255),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ========================
-- TABLE: items (inventory)
-- ========================
USE inventory_service;
CREATE TABLE IF NOT EXISTS `items` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `category` VARCHAR(100) NOT NULL,
    `quantity` INT NOT NULL,
    `location` VARCHAR(100),
    `status` ENUM('available', 'damaged', 'out_of_stock') DEFAULT 'available',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ========================
-- TABLE: notifications
-- ========================
USE notifications_service;
CREATE TABLE IF NOT EXISTS `notifications` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `item_id` INT NOT NULL,
    `message` VARCHAR(255) NOT NULL,
    `status` ENUM('sent', 'pending', 'read') DEFAULT 'pending',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
