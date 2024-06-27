-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-06-2024 a las 01:35:03
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `medi_connect`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `additional_data`
--

CREATE TABLE `additional_data` (
  `id` int(11) NOT NULL,
  `document` varchar(50) DEFAULT NULL,
  `document_type` int(11) NOT NULL,
  `names` varchar(225) NOT NULL,
  `lastnames` varchar(225) NOT NULL,
  `department` int(11) NOT NULL,
  `city` int(11) NOT NULL,
  `address` varchar(225) NOT NULL,
  `phone` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `additional_data`
--

INSERT INTO `additional_data` (`id`, `document`, `document_type`, `names`, `lastnames`, `department`, `city`, `address`, `phone`, `created_at`, `updated_at`) VALUES
(1, '12345678', 1, 'EPS', 'mediconnect', 1, 1, 'calle 33e-2', 1234562, '2024-06-07 02:50:03', '2024-06-07 02:50:03'),
(15, '12345678', 2, 'super', 'super', 1, 1, 'calle 33', 123456789, '2024-06-13 16:08:33', '2024-06-13 16:08:33'),
(16, '12345678', 2, 'test', 'test', 1, 1, 'calle 33', 123456789, '2024-06-13 16:22:26', '2024-06-13 16:22:26'),
(17, '12345678', 2, 'other test', 'test', 1, 1, 'calle 33', 123456789, '2024-06-13 16:23:11', '2024-06-20 17:47:29'),
(18, '12345678', 2, 'test', 'test', 1, 1, 'calle 33', 123456789, '2024-06-13 16:46:11', '2024-06-13 16:46:11'),
(19, '12345678', 2, 'test', 'test', 1, 1, 'calle 33', 123456789, '2024-06-13 16:46:15', '2024-06-13 16:46:15'),
(20, '12345678', 2, 'test', 'test', 1, 1, 'calle 33', 123456789, '2024-06-20 17:16:34', '2024-06-20 17:16:34'),
(21, '1001872235', 2, 'Moisés Daniel', 'Bueno Macias', 4, 144, 'Cra 2C1 # 33F - 27', 2147483647, '2024-06-25 20:50:09', '2024-06-26 23:12:07'),
(22, '1866531231', 2, 'Leonardo', 'Cervera', 4, 144, 'Cra 58 # 68 ', 2147483647, '2024-06-26 23:12:58', '2024-06-26 23:12:58'),
(23, '2151561', 3, 'Alexis', 'Barrios', 14, 497, 'Cra 54 # 68', 2115654564, '2024-06-26 23:15:27', '2024-06-26 23:15:27'),
(24, '7845564', 1, 'James', 'Alandette', 5, 167, 'Cra 54 # 68', 2147483647, '2024-06-26 23:21:06', '2024-06-26 23:29:40');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `additional_data_appointments`
--

CREATE TABLE `additional_data_appointments` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `medical_appointment_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `additional_data_appointments`
--

INSERT INTO `additional_data_appointments` (`id`, `user_id`, `medical_appointment_id`, `created_at`, `updated_at`) VALUES
(1, 9, 1, '2024-06-26 23:30:18', '2024-06-26 23:30:18'),
(2, 11, 1, '2024-06-26 23:30:18', '2024-06-26 23:30:18');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `document_types`
--

CREATE TABLE `document_types` (
  `id` int(11) NOT NULL,
  `code` varchar(50) NOT NULL,
  `description` varchar(225) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `document_types`
--

INSERT INTO `document_types` (`id`, `code`, `description`, `name`, `active`, `created_at`, `updated_at`) VALUES
(1, 'N', 'NIT', 'Número de identificación tributaria', 1, '2024-06-06 23:40:34', '2024-06-06 23:46:26'),
(2, 'C', 'C.C', 'Cédula de ciudadanía', 1, '2024-06-06 23:40:51', '2024-06-06 23:48:10'),
(3, 'E', 'C.E', 'Cédula de extranjería', 1, '2024-06-06 23:48:03', '2024-06-06 23:48:03'),
(4, 'T', 'T.I', 'Tarjeta de identidad', 1, '2024-06-07 02:23:59', '2024-06-07 02:23:59');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medical_appointments`
--

CREATE TABLE `medical_appointments` (
  `id` int(11) NOT NULL,
  `sub_symptom_id` int(11) NOT NULL,
  `appointment_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medical_appointments`
--

INSERT INTO `medical_appointments` (`id`, `sub_symptom_id`, `appointment_date`, `active`, `created_at`, `updated_at`) VALUES
(1, 19, '2024-07-09 05:00:00', 1, '2024-06-26 23:30:18', '2024-06-26 23:30:18');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `membership`
--

CREATE TABLE `membership` (
  `id` int(11) NOT NULL,
  `code` varchar(50) NOT NULL,
  `description` varchar(225) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `membership`
--

INSERT INTO `membership` (`id`, `code`, `description`, `active`, `created_at`, `updated_at`) VALUES
(1, 'NA', 'No aplica', 1, '2024-06-06 23:35:46', '2024-06-06 23:43:02'),
(2, 'CO', 'Contributivo', 1, '2024-06-06 23:37:41', '2024-06-07 02:15:04'),
(3, 'SU', 'Subsidiado', 1, '2024-06-06 23:38:06', '2024-06-06 23:43:13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `code` varchar(50) NOT NULL,
  `description` varchar(225) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `code`, `description`, `active`, `created_at`, `updated_at`) VALUES
(1, 'AD', 'Administrador', 1, '2024-06-06 23:33:30', '2024-06-06 23:42:22'),
(2, 'DO', 'Doctor', 1, '2024-06-06 23:34:26', '2024-06-06 23:34:26'),
(3, 'PA', 'Paciente', 1, '2024-06-06 23:34:37', '2024-06-06 23:42:27'),
(4, 'SU', 'Super', 1, '2024-06-13 14:43:00', '2024-06-13 14:43:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sub_symptoms`
--

CREATE TABLE `sub_symptoms` (
  `id` int(11) NOT NULL,
  `symptom_id` int(11) NOT NULL,
  `code` varchar(50) NOT NULL,
  `description` varchar(225) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `sub_symptoms`
--

INSERT INTO `sub_symptoms` (`id`, `symptom_id`, `code`, `description`, `active`, `created_at`, `updated_at`) VALUES
(7, 1, 'To', 'sss', 0, '2024-06-16 02:05:10', '2024-06-16 02:09:22'),
(12, 1, 'TA', 'Test', 0, '2024-06-16 02:05:27', '2024-06-26 23:25:27'),
(17, 1, 'TR', 'Test', 0, '2024-06-16 02:07:13', '2024-06-26 23:25:29'),
(19, 4, '001', 'Vomito', 1, '2024-06-26 23:25:40', '2024-06-26 23:25:40'),
(20, 4, '002', 'Diarrea', 1, '2024-06-26 23:25:54', '2024-06-26 23:25:54'),
(22, 5, '003', 'Relaciones sexuales dolorosas', 1, '2024-06-26 23:26:13', '2024-06-26 23:26:13'),
(23, 5, '004', 'Dolor testicular', 1, '2024-06-26 23:26:24', '2024-06-26 23:26:24'),
(24, 6, '005', 'Alteración del gusto', 1, '2024-06-26 23:26:38', '2024-06-26 23:26:38'),
(25, 6, '006', 'Enrojecimiento e inflamación', 1, '2024-06-26 23:26:53', '2024-06-26 23:26:53'),
(26, 7, '007', 'Dolor o presión en el pecho', 1, '2024-06-26 23:27:13', '2024-06-26 23:27:13'),
(27, 7, '008', 'Dificultad para respirar', 1, '2024-06-26 23:27:25', '2024-06-26 23:27:25'),
(28, 8, '009', 'Cuerpo extraño en oído', 1, '2024-06-26 23:27:39', '2024-06-26 23:27:39'),
(29, 8, '010', 'Sangrado en el oído', 1, '2024-06-26 23:27:47', '2024-06-26 23:27:47');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `symptoms`
--

CREATE TABLE `symptoms` (
  `id` int(11) NOT NULL,
  `code` varchar(50) NOT NULL,
  `description` varchar(225) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `symptoms`
--

INSERT INTO `symptoms` (`id`, `code`, `description`, `active`, `created_at`, `updated_at`) VALUES
(1, 'T', 'Test', 0, '2024-06-16 01:40:10', '2024-06-16 01:42:16'),
(3, 'TE', 'Test', 0, '2024-06-16 01:41:35', '2024-06-26 23:24:45'),
(4, '001', 'Abdominal o gastrointestinal', 1, '2024-06-26 23:23:59', '2024-06-26 23:23:59'),
(5, '002', 'Salud sexual', 1, '2024-06-26 23:24:06', '2024-06-26 23:24:06'),
(6, '003', 'Boca, garganta y cuello', 1, '2024-06-26 23:24:22', '2024-06-26 23:24:22'),
(7, '004', 'Cardiovascular', 1, '2024-06-26 23:24:29', '2024-06-26 23:24:29'),
(8, '006', 'Oidos', 1, '2024-06-26 23:24:36', '2024-06-26 23:24:36');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `additional_data_id` int(11) NOT NULL,
  `membership_id` int(11) NOT NULL,
  `role` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` text DEFAULT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `additional_data_id`, `membership_id`, `role`, `email`, `password`, `active`, `created_at`, `updated_at`) VALUES
(1, 1, 1, 1, 'admin@gmail.com', '$2b$12$dDFA1slqVhXxF0sWsYtn6e0iRnUlTtGCd0oJnTHhlmLcCNwGKO2GO', 1, '2024-06-07 02:55:46', '2024-06-26 23:34:44'),
(2, 15, 1, 4, 'super@gmail.com', '$2b$12$o9itMXf7TVn/wSEyW6Os9ujM2bATJ7jzLUBG6Jux9D.Dq9eBtfv1.', 1, '2024-06-13 16:08:33', '2024-06-13 16:08:33'),
(8, 21, 2, 3, 'buenomoises2302@gmail.com', '$2b$12$bSAiU55aB1Yt6xYT430dBOmOigGBt9CxAy73GIIGoTk2XmkOds1cS', 1, '2024-06-25 20:50:09', '2024-06-26 23:12:07'),
(9, 22, 3, 3, 'lcervera@gmail.com', '$2b$12$Jpdl3e/IF4uVqM6T2Ghi8uaL13PWkq3.ISGiAF8smDxQjmpe2E1K2', 1, '2024-06-26 23:12:58', '2024-06-26 23:12:58'),
(10, 23, 1, 3, 'abarrios@gmail.com', '$2b$12$hL/7LS70p81MbVpi.D9umOmHtMrZoyO/KByvTMLygXd71xz8Gf55q', 1, '2024-06-26 23:15:27', '2024-06-26 23:15:27'),
(11, 24, 1, 2, 'jalandette@gmail.com', '$2b$12$p959Tf6uTvg7tfBj4ResLe6MSnMb0rgzPJ1us/zY0HVmDQ47LXgla', 1, '2024-06-26 23:21:06', '2024-06-26 23:29:40');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `verification_codes`
--

CREATE TABLE `verification_codes` (
  `id` int(11) NOT NULL,
  `code` int(11) NOT NULL,
  `active` tinyint(4) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `verification_codes`
--

INSERT INTO `verification_codes` (`id`, `code`, `active`, `created_at`, `updated_at`) VALUES
(1, 31710, 0, '2024-06-20 16:59:21', '2024-06-20 17:08:51'),
(2, 96772, 1, '2024-06-20 17:00:19', '2024-06-20 17:00:19');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `additional_data`
--
ALTER TABLE `additional_data`
  ADD PRIMARY KEY (`id`),
  ADD KEY `document_type` (`document_type`),
  ADD KEY `additional_data_indexes` (`document`,`names`,`lastnames`,`department`,`city`);

--
-- Indices de la tabla `additional_data_appointments`
--
ALTER TABLE `additional_data_appointments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `medical_appointment_id` (`medical_appointment_id`);

--
-- Indices de la tabla `document_types`
--
ALTER TABLE `document_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `document_type_indexes` (`active`);

--
-- Indices de la tabla `medical_appointments`
--
ALTER TABLE `medical_appointments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sub_symptom_id` (`sub_symptom_id`),
  ADD KEY `medical_appointments_indexes` (`active`);

--
-- Indices de la tabla `membership`
--
ALTER TABLE `membership`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `membership_indexes` (`active`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `role_indexes` (`active`),
  ADD KEY `user_indexes` (`active`);

--
-- Indices de la tabla `sub_symptoms`
--
ALTER TABLE `sub_symptoms`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `symptom_id` (`symptom_id`),
  ADD KEY `sub_symptoms_indexes` (`active`);

--
-- Indices de la tabla `symptoms`
--
ALTER TABLE `symptoms`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `symptoms_indexes` (`active`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `additional_data_id` (`additional_data_id`),
  ADD KEY `membership_id` (`membership_id`),
  ADD KEY `role` (`role`),
  ADD KEY `user_indexes` (`active`);

--
-- Indices de la tabla `verification_codes`
--
ALTER TABLE `verification_codes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `additional_data`
--
ALTER TABLE `additional_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `additional_data_appointments`
--
ALTER TABLE `additional_data_appointments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `document_types`
--
ALTER TABLE `document_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `medical_appointments`
--
ALTER TABLE `medical_appointments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `membership`
--
ALTER TABLE `membership`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `sub_symptoms`
--
ALTER TABLE `sub_symptoms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `symptoms`
--
ALTER TABLE `symptoms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `verification_codes`
--
ALTER TABLE `verification_codes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `additional_data`
--
ALTER TABLE `additional_data`
  ADD CONSTRAINT `additional_data_ibfk_1` FOREIGN KEY (`document_type`) REFERENCES `document_types` (`id`);

--
-- Filtros para la tabla `additional_data_appointments`
--
ALTER TABLE `additional_data_appointments`
  ADD CONSTRAINT `additional_data_appointments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `additional_data_appointments_ibfk_2` FOREIGN KEY (`medical_appointment_id`) REFERENCES `medical_appointments` (`id`);

--
-- Filtros para la tabla `medical_appointments`
--
ALTER TABLE `medical_appointments`
  ADD CONSTRAINT `medical_appointments_ibfk_1` FOREIGN KEY (`sub_symptom_id`) REFERENCES `sub_symptoms` (`id`);

--
-- Filtros para la tabla `sub_symptoms`
--
ALTER TABLE `sub_symptoms`
  ADD CONSTRAINT `sub_symptoms_ibfk_1` FOREIGN KEY (`symptom_id`) REFERENCES `symptoms` (`id`);

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`additional_data_id`) REFERENCES `additional_data` (`id`),
  ADD CONSTRAINT `users_ibfk_2` FOREIGN KEY (`membership_id`) REFERENCES `membership` (`id`),
  ADD CONSTRAINT `users_ibfk_3` FOREIGN KEY (`role`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
