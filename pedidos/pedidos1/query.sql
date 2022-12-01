<<<<<<< Updated upstream
-- Active: 1654168274613@@127.0.0.1@3306@Pedidos
=======
-- Active: 1653564627884@@127.0.0.1@3306@Pedidos
>>>>>>> Stashed changes
CREATE DATABASE if not exists Pedidos;

use Pedidos;


create table Estados_Venta(    
    id int not null AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(30),
    descripcion varchar(30)
);
insert into Estados_Venta (nombre, descripcion) values ("Entregado", "El pedido a sido entregado");
insert into Estados_Venta (nombre, descripcion) values ("Pendiente", "Su pedido esta en espera");
insert into Estados_Venta (nombre, descripcion) values ("Confirmado", "Su pedido esta en proceso");

create table Condiciones_Iva(
    id int not NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(30),
    descripcion VARCHAR(30)
);

insert into Condiciones_Iva (nombre, descripcion) values ("Responsable Inscripto", "Factura A");
insert into Condiciones_Iva (nombre, descripcion) values ("Sujeto Externo", "Factura C");
insert into Condiciones_Iva (nombre, descripcion) values ("Consumidor Final", "Factura B");

create table Localidades(
    id int not NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    descripcion varchar(30)
);

insert into Localidades (nombre, descripcion) values ("La Calera", "Miguel de Cervantes 552");
insert into Localidades (nombre, descripcion) values ("Urca", "Jose de Maturana 1442");
insert into Localidades (nombre, descripcion) values ("Cerro de las Rosas", "Donaciano del Campillo 1446");


create table Proveedores(
    id int not NULL AUTO_INCREMENT PRIMARY KEY,
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

insert into Proveedores (cuit, razon_social, id_condicion_iva, id_localidad, calle, numero, telefono, fax) values (20-37858374-6, "ByC", 1, 1, "San Martin", 1226, 3518659932, 313414515);
insert into Proveedores (cuit, razon_social, id_condicion_iva, id_localidad, calle, numero, telefono, fax) values (20-38538934-5, "Walmart", 2, 2, "Av. Colón", 6051, 3515386642, 313473892);
insert into Proveedores (cuit, razon_social, id_condicion_iva, id_localidad, calle, numero, telefono, fax) values (20-65875375-3, "Pepsico", 3, 3, "Xavi", 777, 3518290023, 313492402);


create table Unidad_Medida(
    id int not null AUTO_INCREMENT primary KEY,
    nombre VARCHAR(30),
    descripcion VARCHAR(30)
);

insert into Unidad_Medida (nombre, descripcion) values ("Kg", "Kilogramos");
insert into Unidad_Medida (nombre, descripcion) values ("Kg", "Kilogramos");
insert into Unidad_Medida (nombre, descripcion) values ("L", "Litros");

create table Productos(
    id int not null AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    stock int,
    precio_unidad decimal(11,2),
    id_unidad_medida int,
    constraint foreign key (id_unidad_medida) references Unidad_Medida (id)
);

insert into Productos (nombre, stock, precio_unidad, id_unidad_medida) values ("Mayonesa", 120, 176.00, 1);
insert into Productos (nombre, stock, precio_unidad, id_unidad_medida) values ("Savora", 60, 350.00, 2);
insert into Productos (nombre, stock, precio_unidad, id_unidad_medida) values ("Pepsi", 300, 418.00, 3);


 create table Ventas(
    id int not null AUTO_INCREMENT PRIMARY KEY,
    id_proveedor int,
    id_estado int,
    fecha_solicitud DATETIME,
    fecha_recibido DATETIME,
    direccion_entrega VARCHAR(30),
    constraint foreign key (id_proveedor) references Proveedores (id),
    constraint foreign key (id_estado) references Estados_Venta (id)
);
insert into Ventas (id_proveedor, id_estado, fecha_solicitud, fecha_recibido, direccion_entrega)
values (1, 1, "2022-11-11", "2022-11-11", "Jose Araujo 1223");
insert into Ventas (id_proveedor, id_estado, fecha_solicitud, fecha_recibido, direccion_entrega)
values (2, 2, "2022-11-17", "2022-11-17", "Av. Fuerza Aerea");
insert into Ventas (id_proveedor, id_estado, fecha_solicitud, fecha_recibido, direccion_entrega)
values (3, 3, "2022-11-23", "2022-11-23", "La Estanzuela");

create table Detalles(
    id int not NULL AUTO_INCREMENT primary key,
    id_producto int,
    id_venta int,
    cantidad BIGINT,
    constraint foreign key (id_producto) references Productos (id),
    constraint foreign key (id_venta) references Ventas (id)
);

insert into Detalles (id_producto, id_venta, cantidad) values (1, 1, 50);
insert into Detalles (id_producto, id_venta, cantidad) values (2, 2, 23);
insert into Detalles (id_producto, id_venta, cantidad) values (3, 3, 225);