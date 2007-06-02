-- ------------------------------------------------------------
-- Mantiene un listado actualizado de las información y los stocks de productos de almacén.
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS articulo (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  familia_FK_id TINYINT UNSIGNED NOT NULL DEFAULT '1' REFERENCES familia(id),
  descripcion VARCHAR(60) NOT NULL,
  stock FLOAT NOT NULL DEFAULT '0',
  stock_minimo FLOAT NOT NULL DEFAULT '0',
  precio_venta FLOAT NOT NULL DEFAULT '0',
  PRIMARY KEY(id),
  UNIQUE INDEX articulo_unique(id),
  INDEX articulo_FK_Index(familia_FK_id)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ------------------------------------------------------------
-- El nombre de una caja viene determinado por su nombre de host
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS caja (
  id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  seccion_FK_id TINYINT UNSIGNED NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  descripcion VARCHAR(250) NOT NULL,
  impresora_FK_id TINYINT UNSIGNED NOT NULL REFERENCES impresora(id),
  activo BOOL NULL DEFAULT '1',
  PRIMARY KEY(id)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS familia (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(20) NOT NULL,
  descripcion VARCHAR(100) NULL,
  PRIMARY KEY(id),
  UNIQUE INDEX familia_unique(nombre)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;


-- ------------------------------------------------------------
-- Esta tabla almacena la definición y características de cada uno de los modelos de impresoras que podemos conectar a una caja.
-- Hay que mirar el manual subministrado por el fabricante respecto de los códigos para realizar cada acción.
-- En impresoras Epson se gastan código ESC/POS
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS impresora (
  id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(20) NOT NULL,
  marca_modelo VARCHAR(50) NOT NULL,
  comentario VARCHAR(100) NULL,
  compatibles VARCHAR(100) NULL,
  init_printer VARCHAR(20) NULL,
  select_lang VARCHAR(20) NULL,
  spain VARCHAR(20) NULL,
  select_charset VARCHAR(20) NULL,
  europage VARCHAR(20) NULL,
  cols TINYINT UNSIGNED NULL,
  colsu TINYINT UNSIGNED NULL,
  style VARCHAR(20) NULL,
  style_font_a VARCHAR(20) NULL,
  style_font_b VARCHAR(20) NULL,
  style_emph VARCHAR(20) NULL,
  style_dheight VARCHAR(20) NULL,
  style_dwidth VARCHAR(20) NULL,
  style_underl VARCHAR(20) NULL,
  j_left VARCHAR(20) NULL,
  j_center VARCHAR(20) NULL,
  j_rigth VARCHAR(20) NULL,
  color_black VARCHAR(20) NULL,
  color_red VARCHAR(20) NULL,
  advance VARCHAR(20) NULL,
  cut VARCHAR(20) NULL,
  opendrawer VARCHAR(20) NULL,
  charset VARCHAR(20) NULL,
  activo BOOL NULL DEFAULT '1',
  PRIMARY KEY(id),
  UNIQUE INDEX impresora_nombre_index(marca_modelo)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ------------------------------------------------------------
-- La entidad Cliente hace referencia a cliente.
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS cliente (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(120) NOT NULL,
  direccion VARCHAR(120) NOT NULL,
  fecha_alta DATE NULL DEFAULT '2007/01/01',
  PRIMARY KEY(id),
  UNIQUE INDEX cliente_unique(id),
  INDEX(nombre)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ------------------------------------------------------------
-- Almacena información de las distintas secciones de la tienda.
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS ticket (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  cliente_FK_id TINYINT UNSIGNED NOT NULL REFERENCES clientes(id),
  caja_FK_id TINYINT UNSIGNED NOT NULL REFERENCES caja(id),
  fecha DATETIME NOT NULL,
  estado VARCHAR(10) NOT NULL DEFAULT '1',
  metalico BOOL NOT NULL DEFAULT '1',
  PRIMARY KEY(id),
  INDEX TICKET_FK_Index1(caja_FK_id),
  INDEX TICKET_FK_Index2(cliente_FK_id)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS deuda (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  cliente_FK_id INT UNSIGNED NOT NULL REFERENCES clientes(id),
  fecha_deuda DATE NOT NULL,
  hora_deuda TIME NOT NULL,
  ticket_FK_id VARCHAR(13) NOT NULL REFERENCES ticket(id),
  formapago_FK_id VARCHAR(10) NOT NULL REFERENCES formapago(id),
  descripcion VARCHAR(255),
  articulo_FK_id VARCHAR(13) NOT NULL REFERENCES articulo(id),
  importe FLOAT NOT NULL,
  PRIMARY KEY(id, fecha_deuda, hora_deuda, articulo_FK_id),
  INDEX deuda_FK_index1(ticket_FK_id),
  INDEX deuda_index(fecha_deuda, hora_deuda)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;  
  
CREATE TABLE IF NOT EXISTS cobro (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  cliente_FK_id TINYINT UNSIGNED NOT NULL REFERENCES clientes(id),
  fecha_cobro DATE NOT NULL,
  hora_cobro TIME NOT NULL,
  importe_cobro FLOAT NOT NULL DEFAULT '0',
  PRIMARY KEY(id),
  INDEX cobro_index(id, cliente_FK_id, fecha_cobro, hora_cobro)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;  
  	  
-- ------------------------------------------------------------
-- Una linea de ticket (ticket_linea) almacena la información completa de cada uno de los artículos que vendemos.
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS ticket_linea (
  id TINYINT UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
  ticket_FK_id VARCHAR(13) NOT NULL REFERENCES ticket(id),
  articulo_FK_id VARCHAR(13) NOT NULL REFERENCES articulo(id),
  cantidad FLOAT NOT NULL DEFAULT '0',
  precio_venta FLOAT NOT NULL DEFAULT '0',
  PRIMARY KEY(id, ticket_FK_id),
  INDEX ticket_linea_FK_Index1(ticket_FK_id),
  INDEX ticket_linea_FK_Index2(articulo_FK_id)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS tienda (
  id VARCHAR(9) NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  NIF VARCHAR(9) NULL,
  direccion VARCHAR(50) NOT NULL,
  codigo_postal VARCHAR(5) NOT NULL,
  ciudad VARCHAR(30) NOT NULL,
  telefono VARCHAR(12) NOT NULL,
  logotipo BLOB NULL,
  tiempo_mensajes TINYINT UNSIGNED NOT NULL DEFAULT '10',
  decimales TINYINT UNSIGNED NOT NULL DEFAULT '2',
  descuento FLOAT NOT NULL DEFAULT '0',
  porcentaje FLOAT NOT NULL DEFAULT '30',
  cbar_prefijo VARCHAR(4) NOT NULL,
  PRIMARY KEY(id),
  UNIQUE INDEX tienda_unique(NIF, nombre)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;

------------------------------------------------
--Configuración de la botonera
------------------------------------------------

CREATE TABLE IF NOT EXISTS botonera (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  articulo_FK_id VARCHAR(13) NOT NULL REFERENCES articulo(id),
  etiqueta_boton VARCHAR(30),
  PRIMARY KEY(id, articulo_FK_id),
  INDEX	botonera_FK_Index(articulo_FK_id)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;
  
-----------------------
--Forma de pago
-----------------------
CREATE TABLE IF NOT EXISTS formapago (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  codformapago INT NOT NULL DEFAULT 1,
  nombre VACHAR(100) NOT NULL,     
  PRIMARY KEY(id),
  INDEX formapago_Index(id)
)
ENGINE=MyISAM DEFAULT CHARSET=latin1;
