-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SecondHandSourcingSchema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `SecondHandSourcingSchema` ;

-- -----------------------------------------------------
-- Schema SecondHandSourcingSchema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SecondHandSourcingSchema` DEFAULT CHARACTER SET utf8 ;
USE `SecondHandSourcingSchema` ;

-- -----------------------------------------------------
-- Table `SecondHandSourcingSchema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SecondHandSourcingSchema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `birthdate` DATE NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idusers_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SecondHandSourcingSchema`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SecondHandSourcingSchema`.`categories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `furniture` VARCHAR(45) NULL,
  `clothing` VARCHAR(45) NULL,
  `electronics` VARCHAR(45) NULL,
  `outdoors` VARCHAR(45) NULL,
  `toys` VARCHAR(45) NULL,
  `home` VARCHAR(45) NULL,
  `pet_supply` VARCHAR(45) NULL,
  `cars` VARCHAR(45) NULL,
  `cleaning` VARCHAR(45) NULL,
  `miscellanous` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SecondHandSourcingSchema`.`items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SecondHandSourcingSchema`.`items` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `item_name` VARCHAR(45) NOT NULL,
  `cost` INT NOT NULL,
  `location` VARCHAR(45) NOT NULL,
  `image` VARCHAR(45) NOT NULL,
  `brief_desc` VARCHAR(25) NOT NULL,
  `details` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` VARCHAR(45) NULL DEFAULT 'NOW() ON UPDATE NOW()',
  `user_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_items_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_items_categories1_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_items_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `SecondHandSourcingSchema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_items_categories1`
    FOREIGN KEY (`category_id`)
    REFERENCES `SecondHandSourcingSchema`.`categories` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
