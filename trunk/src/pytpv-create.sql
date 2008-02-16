-- MySQL dump 10.11
--
-- Host: localhost    Database: pytpvdb
-- ------------------------------------------------------
-- Server version	5.0.51a

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
-- Table structure for table `articulo`
--

DROP TABLE IF EXISTS `articulo`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `articulo` (
  `id` varchar(13) NOT NULL,
  `seccion_FK_id` tinyint(3) unsigned NOT NULL default '1',
  `subfamilia_FK_id` tinyint(3) unsigned NOT NULL default '1',
  `nombre` varchar(30) NOT NULL,
  `descripcion` varchar(120) default NULL,
  `stock` float NOT NULL default '0',
  `stock_minimo` float NOT NULL default '0',
  `ultimo_precio_comprado` float NOT NULL default '0',
  `precio_venta` float NOT NULL default '0',
  `fecha_primera_caducidad` date default NULL,
  `descuento` float NOT NULL default '0',
  `porcentaje` float NOT NULL default '30',
  `tecla` varchar(3) default NULL,
  `activo` tinyint(1) NOT NULL default '1',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `articulo_unique` (`nombre`),
  KEY `ARTICULO_FK_Index` (`subfamilia_FK_id`),
  KEY `articulo_FKIndex2` (`seccion_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `articulo_X_proveedor`
--

DROP TABLE IF EXISTS `articulo_X_proveedor`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `articulo_X_proveedor` (
  `proveedor_FK_id` tinyint(3) unsigned NOT NULL,
  `articulo_FK_id` varchar(13) NOT NULL,
  `fecha` date NOT NULL,
  `referencia` varchar(10) default NULL,
  `pvd` float NOT NULL,
  `cant_por_caja` tinyint(3) unsigned default '1',
  PRIMARY KEY  (`proveedor_FK_id`,`articulo_FK_id`),
  KEY `articulo_has_proveedor_FKIndex2` (`proveedor_FK_id`),
  KEY `articulo_X_proveedor_FKIndex2` (`articulo_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
  `stock` float default '0',
  `stock_minimo` float default '0',
  `precio_venta` float NOT NULL default '0',
  `imagen` varchar(256) default '',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `articulo_unique` (`id`),
  KEY `articulo_FK_Index` (`familia_FK_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `botonera`
--

DROP TABLE IF EXISTS `botonera`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `botonera` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `articulo_FK_id` varchar(13) NOT NULL,
  `etiqueta_boton` varchar(30) default NULL,
  PRIMARY KEY  (`id`,`articulo_FK_id`),
  KEY `botonera_FK_Index` (`articulo_FK_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
  `fecha_alta` date default '2007-05-05',
  `ultima_compra` date default '2007-05-08',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `cliente_unique` (`id`),
  KEY `nombre` (`nombre`)
) ENGINE=MyISAM AUTO_INCREMENT=10133 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
-- Table structure for table `familia`
--

DROP TABLE IF EXISTS `familia`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `familia` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(100) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `familia_unique` (`nombre`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `formapago`
--

DROP TABLE IF EXISTS `formapago`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `formapago` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `codformapago` int(11) NOT NULL default '1',
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `funcion_caja`
--

DROP TABLE IF EXISTS `funcion_caja`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `funcion_caja` (
  `id` int(11) NOT NULL auto_increment,
  `nombre` varchar(20) default NULL,
  `descripcion` varchar(200) default NULL,
  `funcion` varchar(100) default NULL,
  `programador` varchar(50) default NULL,
  `fecha_alta` date default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `funcion_caja_unique` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `inventario` (
  `id` varchar(13) NOT NULL,
  `persona_FK_id` tinyint(3) unsigned NOT NULL,
  `Razon` varchar(200) default NULL,
  PRIMARY KEY  (`id`),
  KEY `INVENTARIO_FK_Index1` (`persona_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `inventario_linea`
--

DROP TABLE IF EXISTS `inventario_linea`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `inventario_linea` (
  `id` tinyint(3) unsigned NOT NULL,
  `inventario_FK_id` varchar(13) NOT NULL,
  `articulo_FK_id` varchar(13) NOT NULL,
  `cantidad_actual` float NOT NULL default '0',
  `cantidad_anterior` float NOT NULL default '0',
  PRIMARY KEY  (`id`),
  KEY `INVENTARIO_LINEA_FK_Index2` (`articulo_FK_id`),
  KEY `inventario_linea_FKIndex2` (`inventario_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `metodo_pedido`
--

DROP TABLE IF EXISTS `metodo_pedido`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `metodo_pedido` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `nombre` varchar(15) NOT NULL,
  `descripcion` varchar(50) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `metodo_pedido_unique` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `pedido` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `persona_FK_id` tinyint(3) unsigned NOT NULL,
  `proveedor_FK_id` tinyint(3) unsigned NOT NULL,
  `caja_FK_id` tinyint(3) unsigned NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `PEDIDO_FK_Index1` (`caja_FK_id`),
  KEY `PEDIDO_FK_Index2` (`persona_FK_id`),
  KEY `PEDIDO_FK_Index3` (`proveedor_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `pedido_linea`
--

DROP TABLE IF EXISTS `pedido_linea`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `pedido_linea` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `articulo_FK_id` varchar(13) NOT NULL,
  `pedido_FK_id` tinyint(3) unsigned NOT NULL,
  `cantidad` float NOT NULL default '0',
  `precio_compra` float NOT NULL default '0',
  PRIMARY KEY  (`id`),
  KEY `pedido_linea_FKIndex1` (`pedido_FK_id`),
  KEY `pedido_linea_FKIndex2` (`articulo_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `perfil`
--

DROP TABLE IF EXISTS `perfil`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `perfil` (
  `id` varchar(10) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(200) default NULL,
  `activo` tinyint(1) default '1',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `perfil_X_funcion_caja`
--

DROP TABLE IF EXISTS `perfil_X_funcion_caja`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `perfil_X_funcion_caja` (
  `funcion_caja_FK_id` int(11) NOT NULL,
  `perfil_FK_id` varchar(10) NOT NULL,
  PRIMARY KEY  (`funcion_caja_FK_id`,`perfil_FK_id`),
  KEY `perfil_has_funcion_caja_FK_Index` (`perfil_FK_id`),
  KEY `perfil_has_funcion_caja_FKIndex2` (`funcion_caja_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `persona` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `NIF` varchar(9) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellidos` varchar(40) NOT NULL,
  `perfil_FK_id` varchar(10) NOT NULL,
  `direccion_calle` varchar(40) NOT NULL,
  `direccion_numero_puerta` varchar(10) NOT NULL,
  `direccion_codigo_postal` varchar(6) NOT NULL default '12006',
  `direccion_ciudad` varchar(20) NOT NULL default 'Benicassim',
  `vendedor` tinyint(1) NOT NULL default '0',
  `fecha_alta` date default '2005-01-01',
  `usuario` varchar(10) NOT NULL,
  `passwd` varchar(10) NOT NULL default 'qwerty',
  `activo` tinyint(1) default '1',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `persona_unique` (`NIF`,`apellidos`,`usuario`),
  KEY `PERSONA_usuario_index` (`usuario`),
  KEY `persona_FK_id_index` (`perfil_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `proveedor` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `NIF` varchar(9) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `direccion` varchar(200) default NULL,
  `telefono_1` varchar(11) NOT NULL,
  `telefono_2` varchar(11) default NULL,
  `fax` varchar(11) default NULL,
  `correo_electronico` varchar(30) default NULL,
  `persona_contacto` varchar(20) NOT NULL,
  `vendedor_contacto` varchar(20) default NULL,
  `vendedor_mobil` varchar(9) default NULL,
  `calificacion` float NOT NULL default '4.9',
  `metodo_pedido_FK_id` tinyint(3) unsigned NOT NULL default '1',
  `notas` longtext,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `proveedor_unique` (`NIF`,`vendedor_mobil`),
  KEY `proveedor_FKIndex1` (`metodo_pedido_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `seccion`
--

DROP TABLE IF EXISTS `seccion`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `seccion` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `tienda_FK_id` varchar(9) NOT NULL default '1',
  `nombre` varchar(30) NOT NULL,
  `descripcion` varchar(120) default NULL,
  `activo` tinyint(1) default '1',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `seccion_nombre_index` (`nombre`),
  KEY `seccion_FKIndex1` (`tienda_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `subfamilia`
--

DROP TABLE IF EXISTS `subfamilia`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `subfamilia` (
  `id` tinyint(3) unsigned NOT NULL auto_increment,
  `familia_FK_id` tinyint(3) unsigned NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(100) default NULL,
  `descuento` float NOT NULL default '0',
  `porcentaje` float NOT NULL default '0',
  `activo` tinyint(1) NOT NULL default '1',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `subfamilia_unique` (`nombre`),
  KEY `SUBFAMILIA_FK_Index1` (`familia_FK_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `ticket` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `credito` tinyint(1) default NULL,
  `recogido` tinyint(1) default NULL,
  `servicioadomicilio` tinyint(1) default NULL,
  `cliente_FK_id` int(10) unsigned NOT NULL,
  `caja_FK_id` tinyint(3) unsigned NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `estado` varchar(10) NOT NULL default '1',
  `metalico` tinyint(1) NOT NULL default '1',
  PRIMARY KEY  (`id`),
  KEY `TICKET_FK_Index1` (`caja_FK_id`),
  KEY `TICKET_FK_Index2` (`cliente_FK_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `ticket_linea`
--

DROP TABLE IF EXISTS `ticket_linea`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `ticket_linea` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `ticket_FK_id` varchar(13) NOT NULL default '1',
  `cantidad` float NOT NULL default '1',
  `articulo_FK_id` varchar(13) NOT NULL,
  `precio_venta` float default '0',
  PRIMARY KEY  (`id`,`ticket_FK_id`),
  KEY `ticket_linea_FK_Index1` (`ticket_FK_id`),
  KEY `ticket_linea_FK_Index2` (`articulo_FK_id`)
) ENGINE=MyISAM AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2008-02-15  2:37:25
