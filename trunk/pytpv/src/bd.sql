CREATE DATABASE acreditaciones;
USE acreditaciones;
CREATE TABLE acreditaciones (
  id INT NOT NULL AUTO_INCREMENT,
  nombre varchar(50) NOT NULL default '',
  apellidos varchar(100) NOT NULL default '',
  correo varchar(50) NOT NULL default '',
  ciudad varchar(50) default NULL,
  organizacion varchar(50) default NULL,
  rol varchar(50) not null default 'Visitante',
  PRIMARY KEY  (id)
);

