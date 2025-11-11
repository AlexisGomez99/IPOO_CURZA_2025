CREATE DATABASE negocio_bd;

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio NUMERIC(10,2) NOT NULL,
    stock INTEGER NOT NULL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP DEFAULT NULL
);