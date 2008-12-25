-- MySQL dump 10.11
--
-- Host: localhost    Database: pytpvdb
-- ------------------------------------------------------
-- Server version	5.0.51a-3ubuntu1

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `articulos` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `familia_FK_id` varchar(50) NOT NULL default '1',
  `descripcion` varchar(60) NOT NULL default '',
  `stock` float(5,2) default '0.00',
  `stock_minimo` float(5,2) default '0.00',
  `precio_venta` float(5,2) NOT NULL default '0.00',
  `imagen` varchar(256) default '',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `articulo_unique` (`id`),
  KEY `articulo_FK_Index` (`familia_FK_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `botonera` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `botonera_FK_Id` int(11) NOT NULL default '0',
  `row` int(11) NOT NULL default '0',
  `col` int(11) NOT NULL default '0',
  `article_FK_Id` varchar(13) default NULL,
  `label_button` varchar(30) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `botonera`
--

LOCK TABLES `botonera` WRITE;
/*!40000 ALTER TABLE `botonera` DISABLE KEYS */;
INSERT INTO `botonera` VALUES (1,0,0,1,NULL,NULL),(2,0,0,2,NULL,NULL),(3,0,0,3,NULL,NULL),(4,0,0,4,NULL,NULL),(5,0,0,5,NULL,NULL),(6,0,1,0,NULL,NULL),(7,0,1,1,NULL,NULL),(8,0,1,2,NULL,NULL),(9,0,1,3,NULL,NULL),(10,0,1,4,NULL,NULL),(11,0,1,5,NULL,NULL),(12,0,2,0,NULL,NULL),(13,0,2,1,NULL,NULL),(14,0,2,2,NULL,NULL),(15,0,2,3,NULL,NULL),(16,0,2,4,NULL,NULL),(17,0,2,5,NULL,NULL),(18,0,3,0,NULL,NULL),(19,0,3,1,NULL,NULL),(20,0,3,2,NULL,NULL),(21,0,3,3,NULL,NULL),(22,0,3,4,NULL,NULL),(23,0,3,5,NULL,NULL),(24,0,4,0,NULL,NULL),(25,0,4,1,NULL,NULL),(26,0,4,2,NULL,NULL),(27,0,4,3,NULL,NULL),(28,0,4,4,NULL,NULL),(29,0,4,5,NULL,NULL),(30,0,5,0,NULL,NULL),(31,0,5,1,NULL,NULL),(32,0,5,2,NULL,NULL),(33,0,5,3,NULL,NULL),(34,0,5,4,NULL,NULL),(35,0,5,5,NULL,NULL),(36,0,0,0,NULL,NULL);
/*!40000 ALTER TABLE `botonera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caja`
--

DROP TABLE IF EXISTS `caja`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `caja` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `seccion_FK_id` tinyint(3) unsigned NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `impresora_FK_id` tinyint(3) unsigned NOT NULL,
  `activo` tinyint(1) default '1',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `clientes` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nombre` varchar(120) NOT NULL default '',
  `direccion` varchar(120) default '',
  `telefono` varchar(100) default '',
  `fecha_alta` date default '0000-00-00',
  `ultima_compra` date default '0000-00-00',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `cliente_unique` (`id`),
  KEY `nombre` (`nombre`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `cobros` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `cliente_FK_id` tinyint(3) unsigned NOT NULL,
  `fecha_cobro` date NOT NULL,
  `hora_cobro` time NOT NULL,
  `importe_cobro` float NOT NULL default '0',
  PRIMARY KEY  (`id`),
  KEY `cobro_index` (`id`,`cliente_FK_id`,`fecha_cobro`,`hora_cobro`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 ROW_FORMAT=DYNAMIC;
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
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
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
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
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `familia` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nombre` varchar(20) NOT NULL default '',
  `descripcion` varchar(100) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `familia_unique` (`nombre`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `familia`
--

LOCK TABLES `familia` WRITE;
/*!40000 ALTER TABLE `familia` DISABLE KEYS */;
/*!40000 ALTER TABLE `familia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `impresora`
--

DROP TABLE IF EXISTS `impresora`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
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
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `impresora`
--

LOCK TABLES `impresora` WRITE;
/*!40000 ALTER TABLE `impresora` DISABLE KEYS */;
/*!40000 ALTER TABLE `impresora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_botonera`
--

DROP TABLE IF EXISTS `pages_botonera`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `pages_botonera` (
  `id` int(11) NOT NULL auto_increment,
  `label_page` varchar(100) NOT NULL default '',
  `id_page` int(11) NOT NULL default '0',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `pages_botonera`
--

LOCK TABLES `pages_botonera` WRITE;
/*!40000 ALTER TABLE `pages_botonera` DISABLE KEYS */;
INSERT INTO `pages_botonera` VALUES (1,'UNO',0);
/*!40000 ALTER TABLE `pages_botonera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `ticket` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `cliente_FK_id` int(10) unsigned default '0',
  `caja_FK_id` tinyint(3) unsigned default '0',
  `hora` time default '13:00:00',
  `fecha` date default '0000-00-00',
  `hora_llamada` time default '00:00:00',
  `credito` tinyint(1) default NULL,
  `servicioadomicilio` tinyint(1) default NULL,
  `comandaenviada` tinyint(1) default NULL,
  `servido` tinyint(1) default NULL,
  `oculto` tinyint(1) default '0',
  PRIMARY KEY  (`id`),
  KEY `TICKET_FK_Index1` (`caja_FK_id`),
  KEY `TICKET_FK_Index2` (`cliente_FK_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `ticket_linea` (
  `id` int unsigned NOT NULL auto_increment,
  `ticket_FK_id` int NOT NULL default '0',
  `cantidad` float(5,2) NOT NULL default '1.00',
  `articulo_FK_id` int NOT NULL default '0',
  `precio_venta` float(5,2) NOT NULL default '0.00',
  PRIMARY KEY  (`id`),
  KEY `ticket_linea_FK_Index1` (`ticket_FK_id`),
  KEY `ticket_linea_FK_Index2` (`articulo_FK_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
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
SET character_set_client = @saved_cs_client;

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

-- Dump completed on 2008-03-17  1:27:40
