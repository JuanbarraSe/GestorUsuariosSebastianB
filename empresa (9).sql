-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-04-2026 a las 20:32:33
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
-- Base de datos: `empresa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `idArea` int(11) NOT NULL,
  `NombreDepartamento` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`idArea`, `NombreDepartamento`) VALUES
(1, 'Recursos Humanos'),
(3, 'Administracion'),
(4, 'Aseo'),
(5, 'Cafeteria'),
(7, 'Aseo'),
(8, 'Red de medios'),
(9, 'Gerente'),
(10, 'Sistemas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id` int(11) NOT NULL,
  `DocumentoEmplea` varchar(50) DEFAULT NULL,
  `NombreEmplea` varchar(50) DEFAULT NULL,
  `ApellidoEmplea` varchar(50) DEFAULT NULL,
  `Cargo` varchar(50) DEFAULT NULL,
  `SalarioB` decimal(10,2) DEFAULT NULL,
  `HorasExtras` int(11) NOT NULL,
  `Bonificacion` decimal(10,2) NOT NULL,
  `Salud` decimal(10,2) NOT NULL,
  `Pension` decimal(10,2) NOT NULL,
  `SalarioNeto` decimal(10,2) NOT NULL,
  `idDepa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id`, `DocumentoEmplea`, `NombreEmplea`, `ApellidoEmplea`, `Cargo`, `SalarioB`, `HorasExtras`, `Bonificacion`, `Salud`, `Pension`, `SalarioNeto`, `idDepa`) VALUES
(4, '1029838282', 'Joan', 'Suarez', 'Gerente', 5660000.00, 20, 600000.00, 226400.00, 226400.00, 5207200.00, 3),
(5, '1028883619', 'Sebastian', 'Barragan', 'Administracion', 2290000.00, 30, 400000.00, 91600.00, 91600.00, 2106800.00, 1),
(6, '28540', 'Luisa', 'Serrato', 'Gerente', 25090000.00, 30, 20000000.00, 1003600.00, 1003600.00, 23082800.00, 1),
(8, '548954', 'Amaury', 'Hernandez', 'Contador', 3400120.00, 40, 600000.00, 136004.80, 0.00, 3264115.20, 5),
(10, '10247981741', 'Karen', 'Prieto', 'contador', 3090000.00, 30, 200000.00, 123600.00, 123600.00, 2842800.00, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `Usuario` varchar(50) NOT NULL,
  `PASSWORD` varchar(255) NOT NULL,
  `rol` varchar(20) NOT NULL,
  `DocumentoEmplea` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `Usuario`, `PASSWORD`, `rol`, `DocumentoEmplea`) VALUES
(1, 'joansua897', '34567', 'empleado', '1029838282'),
(2, 'sebasjuan13', '123456', 'empleado', '1028883619'),
(3, 'Admin', '201508', 'Administrador', NULL),
(7, 'Amaury', '4878', 'empleado', '548954'),
(12, 'joanjoansuarez12', '3456', 'Empleado', '1029838282'),
(13, 'Santiago', '54884', 'Empleado', '28540');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`idArea`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `DocumentoEmplea` (`DocumentoEmplea`),
  ADD KEY `fk_empleado_area` (`idDepa`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`),
  ADD KEY `DocumentoEmplea` (`DocumentoEmplea`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `idArea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `fk_empleado_area` FOREIGN KEY (`idDepa`) REFERENCES `departamentos` (`idArea`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`DocumentoEmplea`) REFERENCES `empleados` (`DocumentoEmplea`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
