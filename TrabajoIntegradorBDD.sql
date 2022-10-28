-- Active: 1654168274613@@127.0.0.1@3306
CREATE DATABASE if not exists pedidosashe;

use pedidosashe;


create table Estados_Venta(
    id int PRIMARY KEY,
    nombre varchar(30),
    descripcion varchar(30)
);


create table Condiciones_Iva(
    id int PRIMARY KEY,
    nombre varchar(30),
    descripcion VARCHAR(30)
);


create table Localidades(
    id int PRIMARY KEY,
    nombre VARCHAR(30),
    descripcion varchar(30)
);


create table Proveedores(
    id int PRIMARY KEY,
    cuit BIGINT,
    razon_social VARCHAR(30),
    id_condicion_iva int,
    id_localidad int,
    calle VARCHAR(30),
    numero BIGINT,
    departamento VARCHAR(30),
    piso int,
    telefono BIGINT,
    fax VARCHAR(30),
    CONSTRAINT FOREIGN KEY(id_condicion_iva) REFERENCES Condiciones_Iva(id),
    constraint foreign key (id_localidad) references Localidades (id)
);


create table Unidad_Medida(
    id int primary KEY,
    nombre VARCHAR(30),
    descripcion VARCHAR(30)
);

create table Productos(
    id int PRIMARY KEY,
    nombre VARCHAR(30),
    stock int,
    precio_unidad BIGINT,
    id_unidad_medida int,
    constraint foreign key (id_unidad_medida) references Unidad_Medida (id)
);


create table Detalles(
    id int primary key,
    id_producto int,
    cantidad BIGINT,
    constraint foreign key (id_producto) references Productos (id)
);


create table Ventas(
    id int PRIMARY KEY,
    id_detalle int,
    id_proveedor int,
    id_estado int,
    fecha_solicitud DATETIME,
    fecha_recibido DATETIME,
    direccion_entrega VARCHAR(30),
    constraint foreign key (id_detalle) references Detalles (id),
    constraint foreign key (id_proveedor) references Proveedores (id),
    constraint foreign key (id_estado) references Estados_Venta (id)
);













    
