-- Active: 1654168274613@@127.0.0.1@3306
CREATE DATABASE if not exists pedidosashe;

use pedidosashe;


create table Estados_Venta(
    id int PRIMARY KEY,
    nombre varchar(30),
    descripcion varchar(30),
    constraint foreign key (id) references Ventas (id_estado),
    constraint foreign key (nombre) references Ventas (nombre_estado)
);


create table Condiciones_Iva(
    id PRIMARY KEY,
    nombre varchar(30),
    descripcion VARCHAR(30),
    constraint foreign key (id) references Proveedores (id_condicion_iva),
    constraint foreign key (nombre) references Proveedores (nombre_condicion_iva)
);


create table Localidades(
    id PRIMARY KEY,
    nombre VARCHAR(30),
    descripcion varchar(30),
    constraint foreign key (id) references Proveedores (id_localidad),
    constraint foreign key (nombre) references Proveedores (nombre_localidad)
);


create table Proveedores(
    id int PRIMARY KEY,
    cuit BIGINT,
    razon_social VARCHAR(30),
    id_condicion_iva int,
    nombre_condicion_iva VARCHAR(30),
    id_localidad int,
    nombre_localidad VARCHAR(30),
    calle VARCHAR(30),
    numero BIGINT,
    departamento VARCHAR(30),
    piso int,
    telefono BIGINT,
    fax VARCHAR(30),
    constraint foreign key (id) references Ventas (id_proveedor),
    constraint foreign key (razon_social) references Ventas (nombre_proveedor),
    constraint foreign key (id_condicion_iva) references Condiciones_iva (id),
    constraint foreign key (nombre_condicion_iva) references Condicion_Iva (nombre),
    constraint foreign key (id_localidad) references Localidades (id),
    constraint foreign key (nombre_localidad) references Localidades (nombre)
);


create table Ventas(
    id int PRIMARY KEY,
    id_detalle int,
    id_proveedor int,
    nombre_proveedor VARCHAR(30),
    id_estado int,
    nombre_estado VARCHAR(30),
    fecha_solicitud DATETIME,
    fecha_recibido DATETIME,
    direccion_entrega VARCHAR(30),
    constraint foreign key (id_detalle) references Detalles (id),
    constraint foreign key (id_proveedor) references Proveedores (id),
    constraint foreign key (nombre_proveedor) references Proveedores (razon_social),
    constraint foreign key (id_estado) references Estados_Venta (id),
    constraint foreign key (nombre_estado) references Estados_Venta (nombre)
);


create table Unidad_Medida(
    id int primary KEY,
    nombre VARCHAR(30),
    descripcion VARCHAR(30),
    constraint foreign key (id) references Productos (id_unidad_medida),
    constraint foreign key (nombre) references Productos (nombre_unidad_medida)
);


create table Detalles(
    id int primary key,
    id_producto int,
    nombre_producto VARCHAR(30),
    precio_unidad BIGINT,
    cantidad BIGINT,
    constraint foreign key (id) references Ventas (id_detalle),
    constraint foreign key (id_producto) references Productos (id),
    constraint foreign key (nombre_producto) references Productos (nombre),
    constraint foreign key (precio_unidad) references Productos (precio_unidad)
);


create table Productos(
    id int PRIMARY KEY,
    nombre VARCHAR(30),
    stock int,
    precio_unidad BIGINT,
    id_unidad_medida int,
    nombre_unidad_medida VARCHAR(30),
    constraint foreign key (id) references Detalles (id_producto),
    constraint foreign key (nombre) references Detalles (Nombre_producto)
    constraint foreign key (precio_unidad) references Detalles (precio_unidad),
    constraint foreign key (id_unidad_medida) references Unidad_Medida (id),
    constraint foreign key (nombre_unidad_medida) references Unidad_Medida (nombre)
);








    
