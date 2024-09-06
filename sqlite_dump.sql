BEGIN;

CREATE TABLE IF NOT EXISTS `django_migrations` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `app` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `applied` DATETIME NOT NULL
);

INSERT IGNORE  INTO `django_migrations` VALUES(1,'contenttypes','0001_initial','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(2,'auth','0001_initial','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(3,'admin','0001_initial','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(4,'admin','0002_logentry_remove_auto_add','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(5,'admin','0003_logentry_add_action_flag_choices','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(6,'contenttypes','0002_remove_content_type_name','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(7,'auth','0002_alter_permission_name_max_length','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(8,'auth','0003_alter_user_email_max_length','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(9,'auth','0004_alter_user_username_opts','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(10,'auth','0005_alter_user_last_login_null','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(11,'auth','0006_require_contenttypes_0002','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(12,'auth','0007_alter_validators_add_error_messages','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(13,'auth','0008_alter_user_username_max_length','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(14,'auth','0009_alter_user_last_name_max_length','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(15,'auth','0010_alter_group_name_max_length','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(16,'auth','0011_update_proxy_permissions','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(17,'auth','0012_alter_user_first_name_max_length','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(18,'reviews','0001_initial','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(19,'reviews','0002_alter_review_comment','2024-09-06 18:22:22');
INSERT IGNORE INTO `django_migrations` VALUES(20,'sessions','0001_initial','2024-09-06 18:22:22');

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `group_id` INT NOT NULL,
    `permission_id` INT NOT NULL
    -- You may add foreign keys here if needed
);

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `group_id` INT NOT NULL
    -- You may add foreign keys here if needed
);

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `permission_id` INT NOT NULL
    -- You may add foreign keys here if needed
);

CREATE TABLE IF NOT EXISTS `django_admin_log` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `object_id` TEXT,
    `object_repr` TEXT,
    `action_flag` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `django_content_type` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `app_label` VARCHAR(100) NOT NULL,
    `model` VARCHAR(100) NOT NULL
);

INSERT IGNORE INTO `django_content_type` VALUES(1,'admin','logentry');
INSERT IGNORE INTO `django_content_type` VALUES(2,'auth','permission');
INSERT IGNORE INTO `django_content_type` VALUES(3,'auth','group');
INSERT IGNORE INTO `django_content_type` VALUES(4,'auth','user');
INSERT IGNORE INTO `django_content_type` VALUES(5,'contenttypes','contenttype');
INSERT IGNORE INTO `django_content_type` VALUES(6,'sessions','session');
INSERT IGNORE INTO `django_content_type` VALUES(7,'reviews','review');

CREATE TABLE IF NOT EXISTS `auth_permission` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `content_type_id` INT NOT NULL,
    `codename` VARCHAR(100) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    CONSTRAINT `fk_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type`(`id`),
);

INSERT INTO `auth_permission` VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO `auth_permission` VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO `auth_permission` VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO `auth_permission` VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO `auth_permission` VALUES(5,2,'add_permission','Can add permission');
INSERT INTO `auth_permission` VALUES(6,2,'change_permission','Can change permission');
INSERT INTO `auth_permission` VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO `auth_permission` VALUES(8,2,'view_permission','Can view permission');
INSERT INTO `auth_permission` VALUES(9,3,'add_group','Can add group');
INSERT INTO `auth_permission` VALUES(10,3,'change_group','Can change group');
INSERT INTO `auth_permission` VALUES(11,3,'delete_group','Can delete group');
INSERT INTO `auth_permission` VALUES(12,3,'view_group','Can view group');
INSERT INTO `auth_permission` VALUES(13,4,'add_user','Can add user');
INSERT INTO `auth_permission` VALUES(14,4,'change_user','Can change user');
INSERT INTO `auth_permission` VALUES(15,4,'delete_user','Can delete user');
INSERT INTO `auth_permission` VALUES(16,4,'view_user','Can view user');
INSERT INTO `auth_permission` VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO `auth_permission` VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO `auth_permission` VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO `auth_permission` VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO `auth_permission` VALUES(21,6,'add_session','Can add session');
INSERT INTO `auth_permission` VALUES(22,6,'change_session','Can change session');
INSERT INTO `auth_permission` VALUES(23,6,'delete_session','Can delete session');
INSERT INTO `auth_permission` VALUES(24,6,'view_session','Can view session');
INSERT INTO `auth_permission` VALUES(25,7,'add_review','Can add review');
INSERT INTO `auth_permission` VALUES(26,7,'change_review','Can change review');
INSERT INTO `auth_permission` VALUES(27,7,'delete_review','Can delete review');
INSERT INTO `auth_permission` VALUES(28,7,'view_review','Can view review');

CREATE TABLE IF NOT EXISTS `auth_group` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS `auth_user` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `password` VARCHAR(128) NOT NULL,
    `last_login` DATETIME,
    `is_superuser` BOOLEAN NOT NULL,
    `username` VARCHAR(150) NOT NULL UNIQUE,
    `first_name` VARCHAR(150) NOT NULL,
    `last_name` VARCHAR(150) NOT NULL,
    `email` VARCHAR(254) NOT NULL,
    `is_staff` BOOLEAN NOT NULL,
    `is_active` BOOLEAN NOT NULL,
    `date_joined` DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS `reviews_review` (
    `review_id` CHAR(32) NOT NULL PRIMARY KEY,
    `rental_id` CHAR(32) NOT NULL,
    `item_id` CHAR(32) NOT NULL,
    `user_id` CHAR(32) NOT NULL,
    `rating` INT NOT NULL,
    `comment` TEXT NOT NULL,
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME NOT NULL
);

INSERT INTO `reviews_review` VALUES('aa8890e1ebd64060b3871f44ef8c4b71','7f7d000d82d74b7e9f5e8eb5ff938bb6','27becf02ae93433aa80c6c1297d1b6f4','7f7d000d82d74b7e9f5e8eb5ff938bb6',5,'Great rental!','2024-09-06 18:22:22','2024-09-06 18:22:22');
INSERT INTO `reviews_review` VALUES('2e9af76daa2b4ddb9a5f2dfa84904aa9','7f7d000d82d74b7e9f5e8eb5ff938bb6','470cf9f4ea70433da212761da12f3389','7f7d000d82d74b7e9f5e8eb5ff938bb6',4,'Very good experience.','2024-09-06 18:22:22','2024-09-06 18:22:22');


CREATE TABLE IF NOT EXISTS `django_session` (
    `session_key` VARCHAR(40) NOT NULL PRIMARY KEY,
    `session_data` TEXT NOT NULL,
    `expire_date` DATETIME NOT NULL
);

CREATE UNIQUE INDEX `auth_group_permissions_group_id_permission_id_uniq` ON `auth_group_permissions` (`group_id`, `permission_id`);
CREATE INDEX `auth_group_permissions_group_id` ON `auth_group_permissions` (`group_id`);
CREATE INDEX `auth_group_permissions_permission_id` ON `auth_group_permissions` (`permission_id`);

CREATE UNIQUE INDEX `auth_user_groups_user_id_group_id_uniq` ON `auth_user_groups` (`user_id`, `group_id`);
CREATE INDEX `auth_user_groups_user_id` ON `auth_user_groups` (`user_id`);
CREATE INDEX `auth_user_groups_group_id` ON `auth_user_groups` (`group_id`);

CREATE UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_uniq` ON `auth_user_user_permissions` (`user_id`, `permission_id`);
CREATE INDEX `auth_user_user_permissions_user_id` ON `auth_user_user_permissions` (`user_id`);
CREATE INDEX `auth_user_user_permissions_permission_id` ON `auth_user_user_permissions` (`permission_id`);

CREATE INDEX `django_admin_log_content_type_id` ON `django_admin_log` (`content_type_id`);
CREATE INDEX `django_admin_log_user_id` ON `django_admin_log` (`user_id`);

CREATE UNIQUE INDEX `django_content_type_app_label_model_uniq` ON `django_content_type` (`app_label`, `model`);

CREATE UNIQUE INDEX `auth_permission_content_type_id_codename_uniq` ON `auth_permission` (`content_type_id`, `codename`);
CREATE INDEX `auth_permission_content_type_id` ON `auth_permission` (`content_type_id`);

CREATE INDEX `django_session_expire_date` ON `django_session` (`expire_date`);

COMMIT;
