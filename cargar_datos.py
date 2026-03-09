#!/usr/bin/env python
"""
Script para cargar datos de ejemplo en el sistema de transporte de madera
Ejecutar con: python cargar_datos.py
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')
django.setup()

from api.models import Conductor, Camion, Cliente, TipoMadera, Carga

def crear_conductores():
    """Crear conductores de ejemplo"""
    conductores_data = [
        {
            'nombre': 'Carlos Mendoza Silva',
            'licencia_conducir': 'A12345678',
            'telefono': '+56 9 1234 5678',
            'direccion': 'Av. Los Robles 123, Temuco'
        },
        {
            'nombre': 'María González Pérez',
            'licencia_conducir': 'B87654321',
            'telefono': '+56 9 2345 6789',
            'direccion': 'Calle Principal 456, Temuco'
        },
        {
            'nombre': 'Roberto Torres López',
            'licencia_conducir': 'C11223344',
            'telefono': '+56 9 3456 7890',
            'direccion': 'Pasaje Los Pinos 789, Temuco'
        },
        {
            'nombre': 'Ana Herrera Morales',
            'licencia_conducir': 'D55667788',
            'telefono': '+56 9 4567 8901',
            'direccion': 'Av. Libertad 321, Temuco'
        },
        {
            'nombre': 'Luis Ramírez Castro',
            'licencia_conducir': 'E99887766',
            'telefono': '+56 9 5678 9012',
            'direccion': 'Calle Central 654, Temuco'
        }
    ]
    
    for conductor_data in conductores_data:
        conductor, created = Conductor.objects.get_or_create(
            licencia_conducir=conductor_data['licencia_conducir'],
            defaults=conductor_data
        )
        if created:
            print(f"✅ Conductor creado: {conductor.nombre}")
        else:
            print(f"⚠️ Conductor ya existe: {conductor.nombre}")

def crear_tipos_madera():
    """Crear tipos de madera"""
    tipos_data = [
        {
            'nombre': 'Pino Radiata',
            'descripcion': 'Madera de pino radiata, ideal para construcción y mueblería. Color amarillento claro.'
        },
        {
            'nombre': 'Roble',
            'descripcion': 'Madera de roble, muy resistente y duradera. Color marrón oscuro con vetas pronunciadas.'
        },
        {
            'nombre': 'Cedro',
            'descripcion': 'Madera de cedro, aromática y resistente a insectos. Color rojizo claro.'
        },
        {
            'nombre': 'Eucalipto',
            'descripcion': 'Madera de eucalipto, de rápido crecimiento. Color blanquecino a marrón claro.'
        },
        {
            'nombre': 'Araucaria',
            'descripcion': 'Madera de araucaria, nativa de Chile. Color amarillento con vetas rojizas.'
        }
    ]
    
    for tipo_data in tipos_data:
        tipo, created = TipoMadera.objects.get_or_create(
            nombre=tipo_data['nombre'],
            defaults=tipo_data
        )
        if created:
            print(f"✅ Tipo de madera creado: {tipo.nombre}")
        else:
            print(f"⚠️ Tipo de madera ya existe: {tipo.nombre}")

def crear_clientes():
    """Crear clientes de ejemplo"""
    clientes_data = [
        {
            'nombre_empresa': 'Carpintería Los Robles',
            'direccion': 'Av. Industrial 123, Temuco',
            'telefono': '+56 45 2345 678',
            'correo_electronico': 'ventas@carpinterialosrobles.cl'
        },
        {
            'nombre_empresa': 'Constructora Sur S.A.',
            'direccion': 'Calle O\'Higgins 456, Temuco',
            'telefono': '+56 45 3456 789',
            'correo_electronico': 'compras@constructorasur.cl'
        },
        {
            'nombre_empresa': 'Maderas del Norte Ltda.',
            'direccion': 'Zona Industrial Sector A, Temuco',
            'telefono': '+56 45 4567 890',
            'correo_electronico': 'pedidos@maderasdelnorte.cl'
        },
        {
            'nombre_empresa': 'Muebles Artesanales Temuco',
            'direccion': 'Pasaje Artesanos 789, Temuco',
            'telefono': '+56 45 5678 901',
            'correo_electronico': 'info@mueblesartesanales.cl'
        },
        {
            'nombre_empresa': 'Inmobiliaria Los Pinos',
            'direccion': 'Av. Alemania 321, Temuco',
            'telefono': '+56 45 6789 012',
            'correo_electronico': 'proyectos@inmobiliarialospinos.cl'
        }
    ]
    
    for cliente_data in clientes_data:
        cliente, created = Cliente.objects.get_or_create(
            nombre_empresa=cliente_data['nombre_empresa'],
            defaults=cliente_data
        )
        if created:
            print(f"✅ Cliente creado: {cliente.nombre_empresa}")
        else:
            print(f"⚠️ Cliente ya existe: {cliente.nombre_empresa}")

def crear_camiones():
    """Crear camiones de ejemplo"""
    conductores = Conductor.objects.all()
    
    camiones_data = [
        {
            'placa': 'ABC-123',
            'modelo': 'Mercedes Benz 754',
            'capacidad_carga': 15.5,
            'conductor': conductores[0]
        },
        {
            'placa': 'DEF-456',
            'modelo': 'Volvo FH16',
            'capacidad_carga': 20.0,
            'conductor': conductores[1]
        },
        {
            'placa': 'GHI-789',
            'modelo': 'Scania R500',
            'capacidad_carga': 18.5,
            'conductor': conductores[2]
        },
        {
            'placa': 'JKL-012',
            'modelo': 'Iveco Stralis',
            'capacidad_carga': 16.0,
            'conductor': conductores[3]
        },
        {
            'placa': 'MNO-345',
            'modelo': 'MAN TGX',
            'capacidad_carga': 22.0,
            'conductor': conductores[4]
        }
    ]
    
    for camion_data in camiones_data:
        camion, created = Camion.objects.get_or_create(
            placa=camion_data['placa'],
            defaults=camion_data
        )
        if created:
            print(f"✅ Camión creado: {camion.placa} - {camion.modelo}")
        else:
            print(f"⚠️ Camión ya existe: {camion.placa} - {camion.modelo}")

def crear_cargas():
    """Crear cargas de ejemplo"""
    tipos_madera = TipoMadera.objects.all()
    camiones = Camion.objects.all()
    clientes = Cliente.objects.all()
    
    cargas_data = [
        {
            'tipo_madera': tipos_madera[0],  # Pino Radiata
            'cantidad': 25.5,
            'peso': 12.8,
            'camion': camiones[0],
            'cliente': clientes[0]
        },
        {
            'tipo_madera': tipos_madera[1],  # Roble
            'cantidad': 15.0,
            'peso': 18.5,
            'camion': camiones[1],
            'cliente': clientes[1]
        },
        {
            'tipo_madera': tipos_madera[2],  # Cedro
            'cantidad': 30.0,
            'peso': 15.2,
            'camion': camiones[2],
            'cliente': clientes[2]
        },
        {
            'tipo_madera': tipos_madera[3],  # Eucalipto
            'cantidad': 40.0,
            'peso': 20.0,
            'camion': camiones[3],
            'cliente': clientes[3]
        },
        {
            'tipo_madera': tipos_madera[4],  # Araucaria
            'cantidad': 20.0,
            'peso': 16.5,
            'camion': camiones[4],
            'cliente': clientes[4]
        },
        {
            'tipo_madera': tipos_madera[0],  # Pino Radiata
            'cantidad': 35.0,
            'peso': 17.5,
            'camion': camiones[0],
            'cliente': clientes[1]
        },
        {
            'tipo_madera': tipos_madera[1],  # Roble
            'cantidad': 12.5,
            'peso': 15.8,
            'camion': camiones[1],
            'cliente': clientes[2]
        },
        {
            'tipo_madera': tipos_madera[2],  # Cedro
            'cantidad': 22.0,
            'peso': 11.0,
            'camion': camiones[2],
            'cliente': clientes[3]
        }
    ]
    
    for i, carga_data in enumerate(cargas_data):
        carga, created = Carga.objects.get_or_create(
            tipo_madera=carga_data['tipo_madera'],
            camion=carga_data['camion'],
            cliente=carga_data['cliente'],
            defaults=carga_data
        )
        if created:
            print(f"✅ Carga creada: {carga.tipo_madera} - {carga.cantidad} m³ → {carga.cliente}")
        else:
            print(f"⚠️ Carga ya existe: {carga.tipo_madera} - {carga.cantidad} m³ → {carga.cliente}")

def main():
    """Función principal para cargar todos los datos"""
    print("🚛 Iniciando carga de datos para Transportes Madera...")
    print("=" * 50)
    
    print("\n👨‍💼 Creando conductores...")
    crear_conductores()
    
    print("\n🌲 Creando tipos de madera...")
    crear_tipos_madera()
    
    print("\n🏢 Creando clientes...")
    crear_clientes()
    
    print("\n🚛 Creando camiones...")
    crear_camiones()
    
    print("\n📦 Creando cargas...")
    crear_cargas()
    
    print("\n" + "=" * 50)
    print("✅ ¡Carga de datos completada exitosamente!")
    print("\n📊 Resumen de datos cargados:")
    print(f"   • Conductores: {Conductor.objects.count()}")
    print(f"   • Tipos de Madera: {TipoMadera.objects.count()}")
    print(f"   • Clientes: {Cliente.objects.count()}")
    print(f"   • Camiones: {Camion.objects.count()}")
    print(f"   • Cargas: {Carga.objects.count()}")

if __name__ == "__main__":
    main()

