-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.4.3 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para funkomon_db
CREATE DATABASE IF NOT EXISTS `funkomon_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `funkomon_db`;

-- Volcando estructura para tabla funkomon_db.authtoken_token
CREATE TABLE IF NOT EXISTS `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.authtoken_token: ~5 rows (aproximadamente)
INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
	('0571c13ce83bbd757144780a617dd7a0abec2d1e', '2026-05-19 02:27:25.053021', 7),
	('0e95be2409fe137c99843624dfe4a7652b9ead9a', '2026-05-19 15:56:06.173474', 10),
	('731b0fbe58d8b0af9b86a5915f0125c6af8560a9', '2026-05-19 03:45:35.639692', 8),
	('a89e90f7bbfd66726a40dc1b116441e971a3e58c', '2026-05-18 03:40:00.271927', 6),
	('ad17b2474d621d23c75e8d8f3ffc8b9c0cce8b37', '2026-05-19 16:04:39.671978', 11),
	('ba11e3f926c663f27f6c0512841736db122cf581', '2026-05-19 15:50:58.967750', 9);

-- Volcando estructura para tabla funkomon_db.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.auth_group: ~0 rows (aproximadamente)

-- Volcando estructura para tabla funkomon_db.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.auth_group_permissions: ~0 rows (aproximadamente)

-- Volcando estructura para tabla funkomon_db.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.auth_permission: ~57 rows (aproximadamente)
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add Token', 7, 'add_token'),
	(26, 'Can change Token', 7, 'change_token'),
	(27, 'Can delete Token', 7, 'delete_token'),
	(28, 'Can view Token', 7, 'view_token'),
	(29, 'Can add Token', 8, 'add_tokenproxy'),
	(30, 'Can change Token', 8, 'change_tokenproxy'),
	(31, 'Can delete Token', 8, 'delete_tokenproxy'),
	(32, 'Can view Token', 8, 'view_tokenproxy'),
	(33, 'Can add Categoría', 9, 'add_categoria'),
	(34, 'Can change Categoría', 9, 'change_categoria'),
	(35, 'Can delete Categoría', 9, 'delete_categoria'),
	(36, 'Can view Categoría', 9, 'view_categoria'),
	(37, 'Can add Funko', 10, 'add_funko'),
	(38, 'Can change Funko', 10, 'change_funko'),
	(39, 'Can delete Funko', 10, 'delete_funko'),
	(40, 'Can view Funko', 10, 'view_funko'),
	(41, 'Can add profile', 11, 'add_profile'),
	(42, 'Can change profile', 11, 'change_profile'),
	(43, 'Can delete profile', 11, 'delete_profile'),
	(44, 'Can view profile', 11, 'view_profile'),
	(45, 'Can add log', 12, 'add_log'),
	(46, 'Can change log', 12, 'change_log'),
	(47, 'Can delete log', 12, 'delete_log'),
	(48, 'Can view log', 12, 'view_log'),
	(49, 'Can add Producto', 13, 'add_producto'),
	(50, 'Can change Producto', 13, 'change_producto'),
	(51, 'Can delete Producto', 13, 'delete_producto'),
	(52, 'Can view Producto', 13, 'view_producto'),
	(53, 'Can add Detalle de Orden', 14, 'add_detalleorden'),
	(54, 'Can change Detalle de Orden', 14, 'change_detalleorden'),
	(55, 'Can delete Detalle de Orden', 14, 'delete_detalleorden'),
	(56, 'Can view Detalle de Orden', 14, 'view_detalleorden'),
	(57, 'Can add Orden', 15, 'add_orden'),
	(58, 'Can change Orden', 15, 'change_orden'),
	(59, 'Can delete Orden', 15, 'delete_orden'),
	(60, 'Can view Orden', 15, 'view_orden');

-- Volcando estructura para tabla funkomon_db.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.auth_user: ~8 rows (aproximadamente)
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$600000$WTIG0yjSjicmFee9nGQ3Rc$tmYiBdCchdQpPG2PMYS1UzPNzRZJteI58Rq36to3Mdo=', '2026-05-17 21:11:33.406145', 1, 'seba', '', '', '', 1, 1, '2026-05-17 21:10:37.549781'),
	(4, 'pbkdf2_sha256$600000$zgPTZBKMPKjLfwzXqtN5vc$vrMeb6H1KVU5iEmys/WIe4tC1zg0wBd+XrF/J3Hp8yE=', NULL, 0, 'test', '', '', '', 0, 1, '2026-05-18 01:01:23.195993'),
	(5, 'pbkdf2_sha256$600000$srilPlBgFlIcqsQ9C0VVyd$bhIh2eVbSYqlykRZtpNLCuiHyXiRXN61HKaAJkHc0GA=', NULL, 0, 'postprueba', '', '', '', 0, 1, '2026-05-18 03:34:25.250216'),
	(6, 'pbkdf2_sha256$600000$jC5PqWowVWKFLr5ShffFgR$dl3fYzvoD6TXurywmsGTQqxsY4NQc+GtrAC4dYVc5xE=', NULL, 0, 'entrenador_ash', '', '', 'ash@pueblopaleta.com', 0, 1, '2026-05-18 03:39:58.434926'),
	(7, 'pbkdf2_sha256$1000000$wZXk1gCJ7wfXdUyQdZddIV$00HXFJEI2QfeAdLtG4XQze3lxzuRIjgelmP1JE9WOHw=', NULL, 0, 'sebis', '', '', 'sebasarielopez@gmail.com', 0, 1, '2026-05-19 02:27:21.041139'),
	(8, 'pbkdf2_sha256$1000000$BLKP7mogH1sEI99YuSxiLD$+1K4d4n+wHLG1njY+my8Uc6GPSB7vx2T9kcad4EQeH4=', NULL, 0, 'lucio', '', '', 'lucio@gmail.com', 0, 1, '2026-05-19 03:45:33.962636'),
	(9, 'pbkdf2_sha256$1000000$B5eiJpHVvkae1xQz6LbHKR$0p9TkTKWnZNCivUs6Rgmc+psXmFaepaPF3HrdVbCBB8=', NULL, 0, 'gero', '', '', 'gero@lol.com', 0, 1, '2026-05-19 15:50:54.294751'),
	(10, 'pbkdf2_sha256$1000000$Z1DgaOfdF8Y17wJu1HmIMk$e/ZvX5foi66hpBnzMZuSaYwe0QETIGEV33F4+7Ngm1Q=', NULL, 0, 'ariel', '', '', 'ari@gmail.com', 0, 1, '2026-05-19 15:56:04.235622'),
	(11, 'pbkdf2_sha256$1000000$qk9LpgmZNHTrWO9JR6DDh4$DkSWo4PRPBeBfHEwbuE2A4D5/TIeENJ9E1CKy8VTCdA=', NULL, 0, 'more', '', '', 'more@gmail.com', 0, 1, '2026-05-19 16:04:37.685700');

-- Volcando estructura para tabla funkomon_db.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.auth_user_groups: ~0 rows (aproximadamente)

-- Volcando estructura para tabla funkomon_db.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.auth_user_user_permissions: ~0 rows (aproximadamente)

-- Volcando estructura para tabla funkomon_db.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.django_admin_log: ~14 rows (aproximadamente)
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2026-05-17 21:52:12.711973', '1', 'Agua', 1, '[{"added": {}}]', 9, 1),
	(2, '2026-05-17 21:52:28.866399', '2', 'Fuego', 1, '[{"added": {}}]', 9, 1),
	(3, '2026-05-17 21:52:41.465686', '3', 'Planta', 1, '[{"added": {}}]', 9, 1),
	(4, '2026-05-17 22:11:51.932440', '1', 'Funko Pop Pokémon Charmander 455', 1, '[{"added": {}}]', 10, 1),
	(5, '2026-05-17 22:15:06.793830', '2', 'Muñeco Funko Pop Pokémon Squirtle 504', 1, '[{"added": {}}]', 10, 1),
	(6, '2026-05-17 22:15:40.892782', '2', 'Muñeco Funko Pop Pokémon Squirtle 504', 3, '', 10, 1),
	(7, '2026-05-17 22:16:17.241455', '3', 'Funko Pop Pokémon Squirtle 504', 1, '[{"added": {}}]', 10, 1),
	(8, '2026-05-17 22:17:52.525738', '4', 'Funko Pop Pokémon Bulbasaur 453', 1, '[{"added": {}}]', 10, 1),
	(9, '2026-05-18 01:00:08.190061', '2', 'test', 1, '[{"added": {}}]', 4, 1),
	(10, '2026-05-18 01:00:56.957560', '2', 'test', 3, '', 4, 1),
	(11, '2026-05-18 01:01:24.156597', '4', 'test', 1, '[{"added": {}}]', 4, 1),
	(12, '2026-05-18 02:44:03.940538', '4', 'Legendarios', 1, '[{"added": {}}]', 9, 1),
	(13, '2026-05-18 03:34:26.529672', '5', 'postprueba', 1, '[{"added": {}}]', 4, 1),
	(14, '2026-05-18 04:04:19.689263', '1', 'Arceus', 1, '[{"added": {}}]', 13, 1),
	(15, '2026-05-18 04:30:30.986406', '1', 'Orden #1 - entrenador_ash', 1, '[{"added": {}}, {"added": {"name": "Detalle de Orden", "object": "1 x Arceus (Orden #1)"}}]', 15, 1),
	(16, '2026-05-18 18:37:22.702197', '5', 'Perfil de seba', 1, '[{"added": {}}]', 11, 1);

-- Volcando estructura para tabla funkomon_db.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.django_content_type: ~15 rows (aproximadamente)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(7, 'authtoken', 'token'),
	(8, 'authtoken', 'tokenproxy'),
	(5, 'contenttypes', 'contenttype'),
	(12, 'logs', 'log'),
	(14, 'pedidos', 'detalleorden'),
	(15, 'pedidos', 'orden'),
	(9, 'productos', 'categoria'),
	(10, 'productos', 'funko'),
	(13, 'productos', 'producto'),
	(11, 'profiles', 'profile'),
	(6, 'sessions', 'session');

-- Volcando estructura para tabla funkomon_db.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.django_migrations: ~26 rows (aproximadamente)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2026-05-17 20:58:02.057776'),
	(2, 'auth', '0001_initial', '2026-05-17 20:58:03.008119'),
	(3, 'admin', '0001_initial', '2026-05-17 20:58:03.225941'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2026-05-17 20:58:03.243130'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-05-17 20:58:03.334794'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2026-05-17 20:58:03.539976'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2026-05-17 20:58:03.694293'),
	(8, 'auth', '0003_alter_user_email_max_length', '2026-05-17 20:58:03.777660'),
	(9, 'auth', '0004_alter_user_username_opts', '2026-05-17 20:58:03.795872'),
	(10, 'auth', '0005_alter_user_last_login_null', '2026-05-17 20:58:03.964136'),
	(11, 'auth', '0006_require_contenttypes_0002', '2026-05-17 20:58:03.971173'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2026-05-17 20:58:04.010107'),
	(13, 'auth', '0008_alter_user_username_max_length', '2026-05-17 20:58:04.152952'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2026-05-17 20:58:04.323112'),
	(15, 'auth', '0010_alter_group_name_max_length', '2026-05-17 20:58:04.401715'),
	(16, 'auth', '0011_update_proxy_permissions', '2026-05-17 20:58:04.421967'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2026-05-17 20:58:04.560841'),
	(18, 'authtoken', '0001_initial', '2026-05-17 20:58:04.694861'),
	(19, 'authtoken', '0002_auto_20160226_1747', '2026-05-17 20:58:04.761915'),
	(20, 'authtoken', '0003_tokenproxy', '2026-05-17 20:58:04.772131'),
	(21, 'authtoken', '0004_alter_tokenproxy_options', '2026-05-17 20:58:04.791587'),
	(22, 'sessions', '0001_initial', '2026-05-17 20:58:04.922150'),
	(23, 'productos', '0001_initial', '2026-05-17 21:18:39.491461'),
	(24, 'profiles', '0001_initial', '2026-05-17 22:27:26.024319'),
	(25, 'logs', '0001_initial', '2026-05-17 22:27:26.466035'),
	(26, 'productos', '0002_producto_alter_categoria_nombre_delete_funko_and_more', '2026-05-18 02:34:12.062119'),
	(27, 'pedidos', '0001_initial', '2026-05-18 04:28:30.280353'),
	(28, 'profiles', '0002_profile_biometria_facial', '2026-05-18 04:40:07.216368');

-- Volcando estructura para tabla funkomon_db.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.django_session: ~1 rows (aproximadamente)
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('k8v556a2ykb2zs4xd82wzv66u1ia4sor', '.eJxVjEEOwiAQAP-yZ0MolC706N03kIUFqRpISnsy_t006UGvM5N5g6d9K37vafULwwwDXH5ZoPhM9RD8oHpvIra6rUsQRyJO28WtcXpdz_ZvUKgXmMFprS06adWoMCFOxgakJK1mMjmkwKPJUYWBsotGO4PolGSKFnnKGuHzBcQ-N5U:1wOilp:vWN0h7DFZz1QusMNbtsr5PCS1sNSyms0gNnOZUOe0ek', '2026-05-31 21:11:33.422594');

-- Volcando estructura para tabla funkomon_db.logs_log
CREATE TABLE IF NOT EXISTS `logs_log` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `photo` varchar(100) NOT NULL,
  `is_correct` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `profile_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `logs_log_profile_id_41ff81c7_fk_profiles_profile_id` (`profile_id`),
  CONSTRAINT `logs_log_profile_id_41ff81c7_fk_profiles_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.logs_log: ~0 rows (aproximadamente)

-- Volcando estructura para tabla funkomon_db.pedidos_detalleorden
CREATE TABLE IF NOT EXISTS `pedidos_detalleorden` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int unsigned NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `orden_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pedidos_detalleorden_orden_id_05da307b_fk_pedidos_orden_id` (`orden_id`),
  KEY `pedidos_detalleorden_producto_id_280265a8_fk_productos` (`producto_id`),
  CONSTRAINT `pedidos_detalleorden_orden_id_05da307b_fk_pedidos_orden_id` FOREIGN KEY (`orden_id`) REFERENCES `pedidos_orden` (`id`),
  CONSTRAINT `pedidos_detalleorden_producto_id_280265a8_fk_productos` FOREIGN KEY (`producto_id`) REFERENCES `productos_producto` (`id`),
  CONSTRAINT `pedidos_detalleorden_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.pedidos_detalleorden: ~0 rows (aproximadamente)
INSERT INTO `pedidos_detalleorden` (`id`, `cantidad`, `precio_unitario`, `orden_id`, `producto_id`) VALUES
	(1, 1, 900000.00, 1, 1);

-- Volcando estructura para tabla funkomon_db.pedidos_orden
CREATE TABLE IF NOT EXISTS `pedidos_orden` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_creacion` datetime(6) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pedidos_orden_usuario_id_75ad4775_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `pedidos_orden_usuario_id_75ad4775_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.pedidos_orden: ~0 rows (aproximadamente)
INSERT INTO `pedidos_orden` (`id`, `fecha_creacion`, `estado`, `total`, `usuario_id`) VALUES
	(1, '2026-05-18 04:30:30.969664', 'pendiente', 9000000.00, 6);

-- Volcando estructura para tabla funkomon_db.productos_categoria
CREATE TABLE IF NOT EXISTS `productos_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.productos_categoria: ~2 rows (aproximadamente)
INSERT INTO `productos_categoria` (`id`, `nombre`, `descripcion`) VALUES
	(1, 'Agua', 'Pokemónes de tipo Agua'),
	(2, 'Fuego', 'Pokemones de tipo fuego'),
	(3, 'Planta', 'Pokemones de tipo planta'),
	(4, 'Legendarios', 'Categoría para Pokemones Legendarios');

-- Volcando estructura para tabla funkomon_db.productos_producto
CREATE TABLE IF NOT EXISTS `productos_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  `descripcion` longtext NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int unsigned NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `categoria_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `productos_producto_categoria_id_1fef506a_fk_productos` (`categoria_id`),
  CONSTRAINT `productos_producto_categoria_id_1fef506a_fk_productos` FOREIGN KEY (`categoria_id`) REFERENCES `productos_categoria` (`id`),
  CONSTRAINT `productos_producto_chk_1` CHECK ((`stock` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.productos_producto: ~0 rows (aproximadamente)
INSERT INTO `productos_producto` (`id`, `nombre`, `descripcion`, `precio`, `stock`, `imagen`, `fecha_creacion`, `categoria_id`) VALUES
	(1, 'Arceus', 'DIOS', 99999999.00, 1, 'funkos/WhatsApp_Image_2025-05-24_at_21.35.56_2.jpeg', '2026-05-18 04:04:19.604442', 4);

-- Volcando estructura para tabla funkomon_db.profiles_profile
CREATE TABLE IF NOT EXISTS `profiles_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bio` longtext,
  `photo` varchar(100) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `biometria_facial` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `profiles_profile_user_id_a3e81f91_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla funkomon_db.profiles_profile: ~9 rows (aproximadamente)
INSERT INTO `profiles_profile` (`id`, `bio`, `photo`, `created`, `user_id`, `biometria_facial`) VALUES
	(2, NULL, '', '2026-05-18 01:01:24.155639', 4, NULL),
	(3, NULL, '', '2026-05-18 03:34:26.520672', 5, NULL),
	(4, NULL, '', '2026-05-18 03:40:00.221919', 6, '[-0.140939399600029, 0.07469505071640015, 0.04925377666950226, -0.12102959305047989, -0.10038098692893982, -0.021973446011543274, 0.055968936532735825, -0.023490697145462036, 0.1964247077703476, -0.09142943471670151, 0.1077011302113533, -0.08355893939733505, -0.19256453216075897, -0.017436154186725616, -0.015571562573313713, 0.1254434436559677, -0.04726864770054817, -0.1302911341190338, -0.12497423589229584, -0.0323009192943573, 0.05378716439008713, 0.03251957148313522, -0.02862553857266903, 0.09630278497934341, -0.13901470601558685, -0.3052559494972229, -0.061586134135723114, -0.09972614794969559, 0.02267266809940338, -0.09151583909988403, -0.004446753300726414, 0.045755308121442795, -0.2145257294178009, -0.10527948290109634, 0.04561392217874527, 0.08799614012241364, -0.02458665706217289, 0.016323789954185486, 0.22180461883544922, -0.0020263250917196274, -0.24033261835575104, 0.019026611000299454, 0.08219238370656967, 0.25485026836395264, 0.11495174467563629, 0.06182440370321274, 0.007302030920982361, -0.05069504305720329, 0.09996950626373291, -0.23550915718078613, 0.0771188735961914, 0.07586514949798584, 0.12478962540626526, 0.05083669349551201, 0.17043915390968323, -0.16907446086406708, 0.0655788779258728, 0.12107294052839279, -0.21904988586902618, 0.08042573928833008, 0.0343346931040287, -0.04249157756567001, -0.034606389701366425, -0.02063453570008278, 0.15425701439380646, 0.0369858592748642, -0.05515895038843155, -0.12025092542171478, 0.1759503334760666, -0.1489172875881195, 0.03670705854892731, 0.1456822007894516, -0.04853314161300659, -0.1762358844280243, -0.24709635972976685, 0.058000802993774414, 0.41445469856262207, 0.25558561086654663, -0.19218862056732178, 0.02884090319275856, -0.025103947147727013, -0.008008474484086037, 0.12439282238483429, 0.012840023264288902, -0.09382360428571701, 0.04773290827870369, -0.027446769177913666, 0.087200827896595, 0.1301535665988922, 0.033716294914484024, -0.0184169989079237, 0.17859716713428497, 0.056571900844573975, 0.01771865040063858, -0.02202824130654335, -0.02901381067931652, -0.09492340683937073, 4.1606370359659195e-05, -0.14528150856494904, 0.0024150521494448185, 0.08200185000896454, -0.0008041299879550934, 0.04728354141116142, 0.12675175070762634, -0.23724155128002167, 0.12497381120920181, -0.024212108924984932, -0.09656323492527008, -0.11101417243480682, 0.11404063552618027, -0.0889984518289566, 0.027020148932933807, 0.10453788936138153, -0.26428478956222534, 0.15547111630439758, 0.18427437543869019, -0.08311106264591217, 0.0941903218626976, 0.06627839803695679, -0.03319377079606056, 0.09154149144887924, -0.03198571130633354, -0.14858658611774445, -0.09081971645355225, 0.14307579398155212, -0.05799389258027077, 0.13561442494392395, 0.02121613547205925]'),
	(5, '', '', '2026-05-18 18:37:22.651640', 1, ''),
	(6, NULL, '', '2026-05-19 02:27:24.965294', 7, '[-0.1323494166135788, 0.03653872013092041, 0.05523137003183365, -0.09094462543725967, -0.10083206743001938, -0.06450753659009933, 0.061488449573516846, -0.0693822130560875, 0.20912881195545197, -0.1301192343235016, 0.14694218337535858, -0.04707283526659012, -0.18176858127117157, 0.021842822432518005, -0.023595765233039856, 0.11864782124757767, -0.05959974601864815, -0.10707993805408478, -0.12900817394256592, -0.09717120230197906, 0.06129040569067001, 0.0483994334936142, -0.01774289645254612, 0.06776367872953415, -0.13997752964496613, -0.2949123680591583, -0.058973975479602814, -0.121962770819664, 0.09804967790842056, -0.06052408367395401, 0.060611188411712646, 0.055652838200330734, -0.2113480120897293, -0.056660182774066925, 0.04383289813995361, 0.0668986588716507, -0.018353790044784546, 0.014099730178713799, 0.23620517551898956, 0.004699052311480045, -0.21744407713413239, 0.03987983986735344, 0.05629011243581772, 0.25052550435066223, 0.07511075586080551, 0.049384232610464096, 0.029987920075654984, -0.08191325515508652, 0.0843065157532692, -0.242590069770813, 0.07456744462251663, 0.05771125853061676, 0.0970839112997055, 0.026489678770303726, 0.1786353886127472, -0.16530820727348328, 0.07829096913337708, 0.060270458459854126, -0.2617330551147461, 0.11293299496173859, 0.08833283931016922, -0.03530677780508995, -0.09078128635883331, -0.013741985894739628, 0.1875878870487213, 0.05296139791607857, -0.09146171808242798, -0.09002654999494553, 0.17660441994667053, -0.20006659626960754, 0.02223246544599533, 0.12287646532058716, -0.044126179069280624, -0.14258286356925964, -0.2825441360473633, 0.048150911927223206, 0.47522130608558655, 0.23791362345218658, -0.17101050913333893, 0.055733755230903625, -0.012787946499884129, 0.005734915845096111, 0.14082522690296173, 0.0543704628944397, -0.11052414029836655, 0.03661954402923584, 0.0014258353039622307, 0.10216124355792999, 0.10370268672704697, 0.0478401817381382, -0.04058044031262398, 0.2095174491405487, 0.0568525493144989, 0.028756754472851753, -0.040509775280952454, -0.027186153456568718, -0.10489070415496826, -0.08857585489749908, -0.10387705266475677, -0.01343226246535778, 0.07307057827711105, 0.025891369208693504, 0.056944962590932846, 0.1342221200466156, -0.22678162157535553, 0.15405499935150146, -0.05327332019805908, -0.10272268950939178, -0.057074207812547684, 0.14632518589496613, -0.07757237553596497, 0.0043028960935771465, 0.07982586324214935, -0.2634483873844147, 0.16039405763149261, 0.18109294772148132, -0.052336253225803375, 0.08448528498411179, 0.048554062843322754, -0.040575794875621796, 0.07241175323724747, 0.0169603880494833, -0.16639778017997742, -0.09827126562595367, 0.0738779753446579, -0.09602349996566772, 0.10824243724346161, 0.015295661985874176]'),
	(7, NULL, '', '2026-05-19 03:45:35.619363', 8, '[-0.07533591240644455, 0.06344421952962875, -0.03377474471926689, -0.08117145299911499, -0.032071858644485474, -0.005669709760695696, 0.012763559818267822, -0.05427956208586693, 0.26240214705467224, -0.08282266557216644, 0.2095530927181244, -0.008611117489635944, -0.23619526624679565, -0.030300883576273918, -0.03911630064249039, 0.10189039260149002, -0.0734768956899643, -0.07603045552968979, -0.09234277158975601, -0.07379095256328583, 0.04858811944723129, 0.03154711052775383, 0.030298419296741486, 0.12300019711256027, -0.09920790791511536, -0.29627758264541626, -0.07556901127099991, -0.1344318836927414, 0.08818753063678741, -0.0795428454875946, -0.045421499758958817, 0.04964181408286095, -0.17563633620738983, -0.06754592061042786, 0.07335727661848068, 0.07674255967140198, 0.001002675388008356, 0.0021066544577479362, 0.2473960667848587, 0.05392862856388092, -0.1896592378616333, 0.00949140265583992, 0.038482021540403366, 0.20774801075458527, 0.14589758217334747, 0.008442330174148083, 0.03812985122203827, -0.0908634215593338, 0.13509750366210938, -0.17712028324604034, 0.1177026778459549, 0.1365547478199005, 0.13655808568000793, 0.0509476475417614, 0.12366297841072083, -0.21981331706047058, -0.027064159512519836, 0.1691443920135498, -0.20087358355522156, 0.1064126193523407, 0.041247960180044174, -0.008652063086628914, -0.07817910611629486, 0.02056771144270897, 0.14091037213802338, 0.09349597990512848, -0.12785841524600983, -0.16638530790805817, 0.2068675309419632, -0.14605440199375153, 0.0638938769698143, 0.17969585955142975, -0.11069072782993317, -0.21086427569389343, -0.1492052525281906, 0.1192367747426033, 0.44856542348861694, 0.19625669717788696, -0.13100221753120422, 0.06258556246757507, -0.08347608149051666, -0.06661701202392578, 0.044349413365125656, 0.04397640377283096, -0.07426434755325317, 0.03030848130583763, -0.021276136860251427, 0.0625675618648529, 0.11330737918615341, 0.07510499656200409, -0.030610717833042145, 0.23356953263282776, -0.03727327659726143, 0.0770934447646141, 0.0019809496589004993, 0.03981466591358185, -0.12194909900426865, -0.025279637426137924, -0.12516191601753235, -0.06608302891254425, 0.022050678730010986, -0.07082390785217285, 0.034320902079343796, 0.04730791971087456, -0.20100899040699005, 0.1121501699090004, -0.025386955589056015, -0.032848283648490906, -0.04831385239958763, 0.0965866893529892, -0.06578387320041656, 0.029565686360001564, 0.14016327261924744, -0.2874186635017395, 0.22931897640228271, 0.09705404937267303, 0.05178328976035118, 0.1265294849872589, 0.07224557548761368, 0.016151828691363335, 0.12644143402576447, -0.09565931558609009, -0.1411585807800293, -0.06741321831941605, 0.046202316880226135, -0.05464576929807663, 0.09295022487640381, -0.016805268824100494]'),
	(8, NULL, '', '2026-05-19 15:50:58.936497', 9, NULL),
	(9, NULL, '', '2026-05-19 15:56:06.163560', 10, '[-0.14527565240859985, -0.027057025581598282, 0.07971812784671783, -0.05045965686440468, -0.06231161579489708, -0.06789958477020264, -0.06578034162521362, -0.03269844874739647, 0.15832358598709106, -0.10279055684804916, 0.16507554054260254, 0.0037027266807854176, -0.18955877423286438, -0.03907887265086174, -0.023717287927865982, 0.1096445843577385, -0.1265547275543213, -0.1015394777059555, -0.051816511899232864, -0.05306277796626091, 0.009210842661559582, -0.02118685655295849, -0.01864110492169857, 0.07118253409862518, -0.15509118139743805, -0.3574311137199402, -0.06436443328857422, -0.10414071381092072, -0.09449881315231323, -0.08382748812437057, 0.05813806876540184, 0.08309681713581085, -0.16730211675167084, 0.012959158048033714, -0.022095773369073868, 0.10719934850931168, 0.04710260406136513, -0.0035509485751390457, 0.1590690016746521, 0.013633950613439083, -0.21451275050640106, -0.013409473933279514, 0.024853799492120743, 0.20577077567577362, 0.1431875377893448, 0.1438770741224289, 0.011102885007858276, -0.017846256494522095, 0.12783774733543396, -0.22737814486026764, 0.0676649957895279, 0.09871535003185272, 0.0476534329354763, -0.0358240082859993, 0.09746978431940079, -0.18473027646541595, -0.0075423214584589005, 0.057126257568597794, -0.16746902465820312, 0.003155376762151718, -0.05442199856042862, -0.046026650816202164, -0.015139825642108917, -0.05576062574982643, 0.23733054101467133, 0.13044877350330353, -0.09770370274782181, -0.0641731321811676, 0.214297354221344, -0.17571581900119781, -0.038740456104278564, 0.026256250217556953, -0.10682898759841919, -0.18234555423259735, -0.2867996394634247, 0.07551826536655426, 0.39187610149383545, 0.12404590845108032, -0.14554443955421448, 0.05961140990257263, -0.03455614298582077, -0.036154501140117645, 0.04164978489279747, 0.10141761600971222, -0.06375047564506531, 0.015104055404663086, -0.022000372409820557, -0.01873539388179779, 0.19599805772304535, 0.050119441002607346, -0.024950912222266197, 0.14982199668884277, -0.02506706491112709, 0.020275652408599854, -0.003149164840579033, -0.07068340480327606, -0.07781759649515152, 0.02635883539915085, -0.10943356156349182, -0.0042864372953772545, 0.04922258481383324, 0.001117737963795662, 0.01893056184053421, 0.09736737608909607, -0.19888554513454437, 0.07319184392690659, -0.018691563978791237, -0.08281783014535904, 0.0035209939815104008, 0.15126651525497437, -0.13367174565792084, -0.0994388684630394, 0.12103009223937988, -0.245439812541008, 0.19537615776062012, 0.17667442560195923, 0.03906845673918724, 0.169305682182312, 0.06935521960258484, 0.08667127788066864, 0.03663726896047592, 0.04818190261721611, -0.14835956692695618, -0.07040422409772873, 0.08675387501716614, -0.03998933359980583, 0.07485548406839371, 0.04490372911095619]'),
	(10, NULL, '', '2026-05-19 16:04:39.654448', 11, '[-0.05975897237658501, 0.1474725306034088, 0.09528292715549469, -0.07407315075397491, -0.14147338271141052, -0.0012679900974035263, -0.09304557740688324, -0.05788411945104599, 0.29130780696868896, -0.14761488139629364, 0.1606357842683792, 0.049778588116168976, -0.23828712105751038, 0.10806995630264282, -0.15335458517074585, 0.22267070412635803, -0.22246260941028595, -0.21469299495220184, -0.014015684835612774, -0.06590734422206879, 0.057833291590213776, 0.05092831701040268, -0.002270469907671213, 0.07908403128385544, -0.05429478734731674, -0.41823911666870117, -0.03101922944188118, -0.06479819864034653, 0.09456368535757065, -0.05818384513258934, -0.07596556842327118, 0.09786072373390198, -0.16958454251289368, 0.014636201784014702, 0.045074574649333954, 0.033431053161621094, 0.003444380359724164, -0.08766141533851624, 0.20360079407691956, 0.06101495772600174, -0.2673399746417999, -0.0342646948993206, 0.06584107875823975, 0.2467946708202362, 0.23087625205516815, 0.025019682943820953, 0.0511440634727478, -0.1368548572063446, 0.15768633782863617, -0.22235096991062164, 0.0563122034072876, 0.22346486151218414, 0.10508645325899124, 0.08536570519208908, 0.10070927441120148, -0.19354300200939178, 0.008088300004601479, 0.12414925545454025, -0.1665431708097458, 0.07517196983098984, 0.03465782850980759, -0.07121414691209793, 0.027384914457798004, -0.07290978729724884, 0.2354927957057953, 0.10571790486574173, -0.0611441433429718, -0.18257777392864227, 0.2489568144083023, -0.1869492083787918, -0.09068848937749863, 0.034555234014987946, -0.11439146846532822, -0.13355162739753723, -0.19240731000900269, -0.087558813393116, 0.3841569721698761, 0.18124248087406158, -0.1430395096540451, 0.14673057198524475, -0.05488399788737297, -0.08723751455545425, 0.026902368292212486, 0.16526636481285095, -0.0878094732761383, 0.015529392287135124, -0.07004085183143616, -0.03697936236858368, 0.24774998426437378, 0.043481484055519104, -0.009157516993582249, 0.24732963740825653, -0.043061960488557816, 0.006946403533220291, 0.04454231634736061, 0.06297390908002853, -0.19049468636512756, -0.005815959069877863, -0.15248629450798035, -0.17755621671676636, -0.058341819792985916, -0.034326694905757904, -0.03414647653698921, 0.11946897208690643, -0.2360767275094986, 0.10714533179998398, -0.08855821192264557, 0.06355179846286774, 0.011542615480720997, 0.08319558203220367, -0.0019271103665232658, -0.08023545891046524, 0.14788088202476501, -0.17850326001644135, 0.2193843275308609, 0.14019201695919037, 0.02589626982808113, 0.14518922567367554, 0.03335819020867348, 0.08145728707313538, 0.024466630071401596, -0.11093766242265701, -0.15248912572860718, -0.07894780486822128, 0.027102544903755188, -0.09289568662643433, 0.04037771746516228, 0.05218985676765442]');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
