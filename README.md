# Protocolo MCP - Sistema de Gestión de Personal y Clima

## 📋 Descripción

Este proyecto implementa el **Protocolo de Contexto de Modelo (MCP)**, un estándar abierto que permite la integración seamless entre modelos de lenguaje grandes (LLMs) y fuentes de datos externas. La implementación incluye dos servidores principales: un sistema de **Gestión de Personal** y un servidor de **Clima** para pruebas y práctica.

El proyecto demuestra cómo MCP puede ser utilizado para crear interfaces estandarizadas que permiten a los asistentes de IA acceder y manipular datos empresariales de manera segura y eficiente.

## 🏗️ Arquitectura

### Componente Principal: Servidor MCP
```
┌─────────────────────────────────────────┐
│              CLIENTE MCP                │
│            (Claude Desktop)             │
└─────────────────┬───────────────────────┘
                  │
                  │ Protocolo MCP
                  │ (JSON-RPC over stdio)
                  │
┌─────────────────▼───────────────────────┐
│             SERVIDOR MCP                │
│                                         │
│  ┌─────────────────────────────────────┐│
│  │          HERRAMIENTAS (Tools)       ││
│  │                                     ││
│  │  Gestión de Personal:               ││
│  │  • list_empleados                   ││
│  │  • get_empleado                     ││  
│  │  • add_empleado                     ││
│  │  • edit_empleado                    ││
│  │  • remove_empleado                  ││
│  │  • list_roles                       ││
│  │  • list_departamentos               ││
│  │                                     ││
│  │  Clima (Práctica):                  ││
│  │  • get_weather_forecast             ││
│  │  • get_weather_alerts               ││
│  └─────────────────────────────────────┘│
└─────────────────────────────────────────┘
```

### Módulos Implementados

#### 1. **Gestión de Personal**
- **Empleados**: CRUD completo 
- **Roles**: Gestion puestos que puede desempeñar una persona dentro de la organización.
- **Departamentos**: Organización empresarial
- **Estados**: Control de status de empleados (activo, inactivo, suspendido, baja)

#### 2. **Clima** (Módulo de Práctica)
- **Pronósticos**: Consulta de clima por coordenadas
- **Alertas**: Sistema de notificaciones meteorológicas

## 🔧 Tecnologías Utilizadas

- **Lenguaje**: Python 3.8+
- **Protocolo**: MCP (Model Context Protocol)
- **Base de Datos**: No especificada en el código (abstracción)
- **Comunicación**: JSON-RPC over stdio
- **Arquitectura**: Servidor MCP con Tools solamente
- **APIs Externas**: Servicios de clima y de gestion del personal

## 🚀 Instalación y Configuración

### Prerrequisitos
```bash
Python 3.8+
pip
git
```

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/Flores-cesar/Protocolo-MCP.git
cd Protocolo-MCP/api_gestion_del_personal

## instalar gestor de paquetes uv

## instalar dependencias 
uv sync #(se usa uv.lock)
```

### Integración con Claude
Agregar al archivo de configuración de Claude:

```json
{
  "mcpServers": {

    "Gestion de personal": {
      "command": "uv",
      "args": [
        "--directory",
        "path\\api_gestion_del_personal", // Ruta para Windows
        //"path/api_gestion_del_personal", // Ruta para Linux/Mac (usa "/")
        "run",
        "mcp_server.py"
      ]
  }
}
```

## 🔧 Funcionalidades Principales

### Gestión de Personal

#### Empleados
- ✅ **Crear empleado**: Registro completo con validaciones
- ✅ **Listar empleados**: Consulta con filtros
- ✅ **Obtener empleado**: Detalle individual
- ✅ **Actualizar empleado**: Modificación parcial o completa
- ✅ **Eliminar empleado**: Baja lógica o física

#### Campos de Empleado
```python
{
    "id_empleado": int,
    "nombre": str,
    "apellido": str,
    "correo": str,
    "edad": int,
    "salario": float,
    "fecha_ingreso": str,
    "rol": int,
    "estado": "activo|inactivo|suspendido|baja"
}
```

#### Roles y Departamentos
- **Roles**: Gestión de perfiles laborales
- **Departamentos**: Organización por áreas

### Módulo Clima (Práctica)
- **Pronósticos**: Consulta por coordenadas GPS
- **Alertas**: Notificaciones meteorológicas por estado/región

## 📖 Documentación API

### Herramientas Disponibles

| Herramienta | Descripción | Parámetros |
|-------------|-------------|------------|
| `list_empleados` | Lista todos los empleados | - |
| `get_empleado` | Obtiene un empleado específico | `id_empleado: int` |
| `add_empleado` | Crea un nuevo empleado | `empleado: dict` |
| `edit_empleado` | Actualiza un empleado | `id_empleado: int, datos: dict` |
| `remove_empleado` | Elimina un empleado | `id_empleado: int` |
| `list_roles` | Lista todos los roles | - |
| `list_departamentos` | Lista departamentos | - |

### Ejemplo de Uso con Claude
```
Usuario: "Muéstrame todos los empleados del departamento de IT"
Claude: Utiliza list_empleados y filtra por departamento

Usuario: "Crea un nuevo empleado llamado Juan Pérez"
Claude: Utiliza add_empleado con los datos proporcionados
```

## 🏗️ Partes Importantes del Desarrollo

### 1. **Arquitectura MCP**
- Implementación del protocolo JSON-RPC sobre stdio
- Manejo de herramientas (tools) y recursos (resources)
- Sistema de validación y error handling

### 4. **Integración con APIs Externas**
- Cliente HTTP para servicios de clima
- Manejo de rate limiting
- Cache de respuestas para optimización

### 5. **Logging y Monitoreo**
- Sistema de logs estructurado
- Error tracking y debugging

## 🔗 Enlaces Útiles

- [Documentación MCP Oficial](https://modelcontextprotocol.io/)
- [Claude MCP Integration](https://docs.anthropic.com/en/docs/mcp)
- [Ejemplos MCP](https://github.com/modelcontextprotocol/servers)
---
