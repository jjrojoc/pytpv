-- MySQL dump 10.11
--
-- Host: localhost    Database: pytpvdb
-- ------------------------------------------------------
-- Server version	5.0.38-Ubuntu_0ubuntu1-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `pytpvdb`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `pytpvdb` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `pytpvdb`;

--
-- Table structure for table `articulos`
--

DROP TABLE IF EXISTS `articulos`;
CREATE TABLE `articulos` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `familia_FK_id` tinyint(3) unsigned NOT NULL default '1',
  `descripcion` varchar(60) NOT NULL,
  `stock` float default '0',
  `stock_minimo` float default '0',
  `precio_venta` float NOT NULL default '0',
  `imagen` blob,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `articulo_unique` (`id`),
  KEY `articulo_FK_Index` (`familia_FK_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `articulos`
--

LOCK TABLES `articulos` WRITE;
/*!40000 ALTER TABLE `articulos` DISABLE KEYS */;
/*!40000 ALTER TABLE `articulos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `botonera`
--

DROP TABLE IF EXISTS `botonera`;
CREATE TABLE `botonera` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `articulo_FK_id` varchar(13) NOT NULL,
  `etiqueta_boton` varchar(30) default NULL,
  PRIMARY KEY  (`id`,`articulo_FK_id`),
  KEY `botonera_FK_Index` (`articulo_FK_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `botonera`
--

LOCK TABLES `botonera` WRITE;
/*!40000 ALTER TABLE `botonera` DISABLE KEYS */;
/*!40000 ALTER TABLE `botonera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caja`
--

DROP TABLE IF EXISTS `caja`;
CREATE TABLE `caja` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `seccion_FK_id` tinyint(3) unsigned NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `impresora_FK_id` tinyint(3) unsigned NOT NULL,
  `activo` tinyint(1) default '1',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `caja`
--

LOCK TABLES `caja` WRITE;
/*!40000 ALTER TABLE `caja` DISABLE KEYS */;
/*!40000 ALTER TABLE `caja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE `clientes` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nombre` varchar(120) NOT NULL,
  `direccion` varchar(120) NOT NULL,
  `fecha_alta` date NOT NULL default '2007-05-26',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `cliente_unique` (`id`),
  KEY `nombre` (`nombre`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cobros`
--

DROP TABLE IF EXISTS `cobros`;
CREATE TABLE `cobros` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `cliente_FK_id` tinyint(3) unsigned NOT NULL,
  `fecha_cobro` date NOT NULL,
  `hora_cobro` time NOT NULL,
  `importe_cobro` float NOT NULL default '0',
  PRIMARY KEY  (`id`),
  KEY `cobro_index` (`id`,`cliente_FK_id`,`fecha_cobro`,`hora_cobro`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cobros`
--

LOCK TABLES `cobros` WRITE;
/*!40000 ALTER TABLE `cobros` DISABLE KEYS */;
/*!40000 ALTER TABLE `cobros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalledeudas`
--

DROP TABLE IF EXISTS `detalledeudas`;
CREATE TABLE `detalledeudas` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `cliente_FK_id` tinyint(3) unsigned NOT NULL,
  `articulo_FK_id` varchar(10) NOT NULL,
  `descripcion` varchar(60) NOT NULL,
  `cantidad` float NOT NULL,
  `importe` float NOT NULL default '0',
  PRIMARY KEY  (`id`),
  KEY `cobro_index` (`id`,`cliente_FK_id`,`articulo_FK_id`,`descripcion`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `detalledeudas`
--

LOCK TABLES `detalledeudas` WRITE;
/*!40000 ALTER TABLE `detalledeudas` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalledeudas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deudas`
--

DROP TABLE IF EXISTS `deudas`;
CREATE TABLE `deudas` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `cliente_FK_id` varchar(10) NOT NULL,
  `fecha_deuda` date NOT NULL,
  `hora_deuda` time NOT NULL,
  `ticket_FK_id` varchar(13) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `articulos_FK_id` varchar(10) NOT NULL,
  `importe` float NOT NULL,
  PRIMARY KEY  (`id`,`fecha_deuda`,`hora_deuda`,`articulos_FK_id`),
  KEY `deuda_FK_index1` (`ticket_FK_id`),
  KEY `deuda_index` (`fecha_deuda`,`hora_deuda`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `deudas`
--

LOCK TABLES `deudas` WRITE;
/*!40000 ALTER TABLE `deudas` DISABLE KEYS */;
/*!40000 ALTER TABLE `deudas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `familia`
--

DROP TABLE IF EXISTS `familia`;
CREATE TABLE `familia` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(100) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `familia_unique` (`nombre`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `familia`
--

LOCK TABLES `familia` WRITE;
/*!40000 ALTER TABLE `familia` DISABLE KEYS */;
/*!40000 ALTER TABLE `familia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formapago`
--

DROP TABLE IF EXISTS `formapago`;
CREATE TABLE `formapago` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `codformapago` int(11) NOT NULL default '1',
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `formapago`
--

LOCK TABLES `formapago` WRITE;
/*!40000 ALTER TABLE `formapago` DISABLE KEYS */;
/*!40000 ALTER TABLE `formapago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `impresora`
--

DROP TABLE IF EXISTS `impresora`;
CREATE TABLE `impresora` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `nombre` varchar(20) NOT NULL default '',
  `marca_modelo` varchar(50) NOT NULL default '',
  `comentario` varchar(100) default NULL,
  `compatibles` varchar(100) default NULL,
  `init_printer` varchar(20) default NULL,
  `select_lang` varchar(20) default NULL,
  `spain` varchar(20) default NULL,
  `select_charset` varchar(20) default NULL,
  `europage` varchar(20) default NULL,
  `cols` tinyint(3) unsigned default NULL,
  `colsu` tinyint(3) unsigned default NULL,
  `style` varchar(20) default NULL,
  `style_font_a` varchar(20) default NULL,
  `style_font_b` varchar(20) default NULL,
  `style_emph` varchar(20) default NULL,
  `style_dheight` varchar(20) default NULL,
  `style_dwidth` varchar(20) default NULL,
  `style_underl` varchar(20) default NULL,
  `j_left` varchar(20) default NULL,
  `j_center` varchar(20) default NULL,
  `j_rigth` varchar(20) default NULL,
  `color_black` varchar(20) default NULL,
  `color_red` varchar(20) default NULL,
  `advance` varchar(20) default NULL,
  `cut` varchar(20) default NULL,
  `opendrawer` varchar(20) default NULL,
  `charset` varchar(20) default NULL,
  `activo` tinyint(1) default '1',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `impresora_nombre_index` (`marca_modelo`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `impresora`
--

LOCK TABLES `impresora` WRITE;
/*!40000 ALTER TABLE `impresora` DISABLE KEYS */;
INSERT INTO `impresora` VALUES (1,'texto','txt','Fichero de texto en /tmp/gtpv-printer-txt-(temporal)','cualquiera','','','','','19',40,33,'','','','','','','','','','','','','','','','',1),(2,'Epson TMU220B','TMU220B','Epson\nTM-U220B','TM-220A y TM-220D','ESC @','ESC R','7','ESC t','19',40,33,'ESC !','0x00','0x01','0x08','0x10','0x20','0x80','ESC a0','ESC a1','ESC a2','ESC r NUL','ESC r SOH','ESC d','GS V B NUL','ESC p NUL LF d','PC585',1);
/*!40000 ALTER TABLE `impresora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
CREATE TABLE `ticket` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `cliente_FK_id` tinyint(3) unsigned NOT NULL,
  `caja_FK_id` tinyint(3) unsigned NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `estado` varchar(10) NOT NULL default '1',
  `metalico` tinyint(1) NOT NULL default '1',
  PRIMARY KEY  (`id`),
  KEY `TICKET_FK_Index1` (`caja_FK_id`),
  KEY `TICKET_FK_Index2` (`cliente_FK_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_linea`
--

DROP TABLE IF EXISTS `ticket_linea`;
CREATE TABLE `ticket_linea` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `ticket_FK_id` varchar(13) NOT NULL default '1',
  `cantidad` float NOT NULL default '1',
  `articulo_FK_id` varchar(13) NOT NULL,
  `precio_venta` float default '0',
  PRIMARY KEY  (`id`,`ticket_FK_id`),
  KEY `ticket_linea_FK_Index1` (`ticket_FK_id`),
  KEY `ticket_linea_FK_Index2` (`articulo_FK_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ticket_linea`
--

LOCK TABLES `ticket_linea` WRITE;
/*!40000 ALTER TABLE `ticket_linea` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket_linea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tienda`
--

DROP TABLE IF EXISTS `tienda`;
CREATE TABLE `tienda` (
  `id` varchar(9) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `NIF` varchar(9) default NULL,
  `direccion` varchar(50) NOT NULL,
  `codigo_postal` varchar(5) NOT NULL,
  `ciudad` varchar(30) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `logotipo` blob,
  `tiempo_mensajes` tinyint(3) unsigned NOT NULL default '10',
  `decimales` tinyint(3) unsigned NOT NULL default '2',
  `descuento` float NOT NULL default '0',
  `porcentaje` float NOT NULL default '30',
  `cbar_prefijo` varchar(4) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `tienda_unique` (`NIF`,`nombre`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tienda`
--

LOCK TABLES `tienda` WRITE;
/*!40000 ALTER TABLE `tienda` DISABLE KEYS */;
/*!40000 ALTER TABLE `tienda` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2007-06-16 16:35:09
