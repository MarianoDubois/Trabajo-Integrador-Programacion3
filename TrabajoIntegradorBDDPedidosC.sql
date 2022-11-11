-- Active: 1654168274613@@127.0.0.1@3306
CREATE DATABASE if not exists PedidosC;

use PedidosC;


create table Estados_Venta(
    id int PRIMARY KEY,
    nombre varchar(30),
    descripcion varchar(30)
);

insert into Estados_Venta (id, nombre, descripcion) values (0, "Juan", "Entregado");
insert into Estados_Venta (id, nombre, descripcion) values (1, "Thiago", "Entregado");
insert into Estados_Venta (id, nombre, descripcion) values (2, "Facundo", "Entregado");

create table Condiciones_Iva(
    id int PRIMARY KEY,
    nombre varchar(30),
    descripcion VARCHAR(30)
);

insert into Condiciones_Iva (id, nombre, descripcion) values (0, "Juan", "Responsable Inscripto");
insert into Condiciones_Iva (id, nombre, descripcion) values (1, "Thiago", "Responsable Inscripto");
insert into Condiciones_Iva (id, nombre, descripcion) values (2, "Facundo", "Responsable Inscripto");

create table Localidades(
    id int PRIMARY KEY,
    nombre VARCHAR(30),
    descripcion varchar(30)
);

insert into Localidades (id, nombre, descripcion) values (0, "Juan", "Miguel de Cervantes 552");
insert into Localidades (id, nombre, descripcion) values (1, "Thiago", "Jose de Maturana 1442");
insert into Localidades (id, nombre, descripcion) values (2, "Facundo", "Donaciano del Campillo 1446");


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

insert into Proveedores (id, cuit, razon_social, id_condicion_iva, id_localidad, calle, numero, departamento,
piso, telefono, fax) values (0, 20-37858374-6, "ByC", 0, 0, "San Martin", 1226, "-" , "-", 3518659932, 313414515);
insert into Proveedores (id, cuit, razon_social, id_condicion_iva, id_localidad, calle, numero, departamento,
piso, telefono, fax) values (1, 20-38538934-5, "Walmart", 1, 1, "Av. Colón", 6051, "-" , "-", 3515386642, 313473892);
insert into Proveedores (id, cuit, razon_social, id_condicion_iva, id_localidad, calle, numero, departamento,
piso, telefono, fax) values (2, 20-65875375-3, "Pepsico", 2, 2, "Xavi", 777, "-" , "-", 3518290023, 313492402);


create table Unidad_Medida(
    id int primary KEY,
    nombre VARCHAR(30),
    descripcion VARCHAR(30)
);

insert into Unidad_Medida (id, nombre, descripcion) values (0, "Juan", "Paquetes");
insert into Unidad_Medida (id, nombre, descripcion) values (1, "Thiago", "Paquetes");
insert into Unidad_Medida (id, nombre, descripcion) values (2, "Facundo", "Paquetes");

create table Productos(
    id int PRIMARY KEY,
    nombre VARCHAR(30),
    stock int,
    precio_unidad BIGINT,
    id_unidad_medida int,
    constraint foreign key (id_unidad_medida) references Unidad_Medida (id)
);

insert into Productos (id, nombre, stock, precio_unidad, id_unidad_medida) values (0, "Mayonesa", 120, $176.00, 0);
insert into Productos (id, nombre, stock, precio_unidad, id_unidad_medida) values (1, "Savora", 60, $350.00, 1);
insert into Productos (id, nombre, stock, precio_unidad, id_unidad_medida) values (2, "Pepsi", 300, $418.00, 2);


create table Detalles(
    id int primary key,
    id_producto int,
    cantidad BIGINT,
    constraint foreign key (id_producto) references Productos (id)
);

insert into Detalles (id, id_producto, cantidad) values (0, 0, 50);
insert into Detalles (id, id_producto, cantidad) values (1, 1, 23);
insert into Detalles (id, id_producto, cantidad) values (2, 2, 225);

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

insert into Ventas (id, id_detalle, id_proveedor, id_estado, fecha_solicitud, fecha_recibido, direccion_entrega)
values (0, 0, 0, 0, "2022-11-11", "2022-11-11", "Jose Araujo 1223");
insert into Ventas (id, id_detalle, id_proveedor, id_estado, fecha_solicitud, fecha_recibido, direccion_entrega)
values (1, 1, 1, 1, "2022-11-17", "2022-11-17", "Av. Fuerza Aerea");
insert into Ventas (id, id_detalle, id_proveedor, id_estado, fecha_solicitud, fecha_recibido, direccion_entrega)
values (2, 2, 2, 2, "2022-11-23", "2022-11-23", "La Estanzuela");













    
