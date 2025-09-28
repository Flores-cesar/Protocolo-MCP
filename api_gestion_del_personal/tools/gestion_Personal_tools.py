from mcp.server.fastmcp import FastMCP
from typing import Literal
from services.empleados import (
    get_empleados, create_empleado, get_empleado_detail,
    update_empleado, delete_empleado
)
from services.roles import (
    get_roles, get_rol_detail
)
from services.departamentos import (
    get_departamentos, get_departamento_detail
)
from helpers.formatters import format_empleado, format_rol, format_departamento

mcp_gestion = FastMCP("gestion del personal")

# ================== EMPLEADOS ==================
@mcp_gestion.tool()
async def list_empleados() -> str:
    """Obtener lista completa de empleados."""
    data = await get_empleados()
    if not data:
        return "Error en la comunicación con la API."
    
    empleados = data.get("empleados", [])
    if not empleados:
        return "No hay empleados registrados en el sistema."
        
    return "\n".join(format_empleado(e) for e in empleados)


@mcp_gestion.tool()
async def get_empleado(id_empleado: int) -> str:
    """Obtener detalle de un empleado por su ID."""
    data = await get_empleado_detail(id_empleado)
    if not data:
        return "Error en la comunicación con la API."

    if data.get("message") != "success":
        return f"Error al obtener empleado con ID {id_empleado}."

    empleado = data.get("empleado")
    if not empleado:
        return f"No se encontró un empleado con ID {id_empleado}."

    return format_empleado(empleado)


@mcp_gestion.tool()
async def add_empleado(
    nombre: str, apellido: str, correo: str, rol: int,
    fecha_ingreso: str, salario: float, edad: int,
    estado: Literal["activo", "inactivo", "suspendido", "baja"] = "activo"
) -> str:
    """Crear un nuevo empleado."""
    nuevo = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "correo": correo,
        "rol": rol,
        "fecha_ingreso": fecha_ingreso,
        "salario": salario,
        "estado": estado
    }
    empleado_creado = await create_empleado(nuevo)
    return f"Empleado creado:\n{format_empleado(empleado_creado)}"


@mcp_gestion.tool()
async def edit_empleado(
    id_empleado: int, nombre: str, apellido: str, edad: int,
    fecha_ingreso: str, rol: int, salario: float,
    estado: Literal["activo", "inactivo", "suspendido", "baja"] = "activo"
) -> str:
    """Editar un empleado existente. Actualiza todos los campos provistos."""
    payload = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "estado": estado,
        "fecha_ingreso": fecha_ingreso,
        "rol": rol,
        "salario": salario
    }

    actualizado = await update_empleado(id_empleado, payload)
    if not actualizado:
        return f"No se pudo actualizar el empleado con ID {id_empleado}."

    return f"Empleado actualizado con ID {id_empleado}."

@mcp_gestion.tool()
async def remove_empleado(id_empleado: int) -> str:
    """Eliminar un empleado por su ID."""
    resultado = await delete_empleado(id_empleado)
    if not resultado:
        return f"No se encontró un empleado con ID {id_empleado}."
    return f"Empleado con ID {id_empleado} eliminado correctamente."


# ================== ROLES ==================
@mcp_gestion.tool()
async def list_roles() -> str:
    """Obtener lista completa de roles."""
    data = await get_roles()
    if not data:
        return "Error en la comunicación con la API."
    
    roles = data.get("roles", [])
    if not roles:
        return "No hay roles registrados en el sistema."
    
    return "\n".join(format_rol(r) for r in roles)


@mcp_gestion.tool()
async def get_rol(id_rol: int) -> str:
    """Obtener detalle de un rol por su ID."""
    data = await get_rol_detail(id_rol)
    if not data:
        return "Error en la comunicación con la API."
    
    rol = data.get("rol")
    if not rol:
        return f"No se encontró un rol con ID {id_rol}."
    
    return format_rol(rol)


# ================== DEPARTAMENTOS ==================
@mcp_gestion.tool()
async def list_departamentos() -> str:
    """Obtener lista completa de departamentos."""
    data = await get_departamentos()
    if not data:
        return "Error en la comunicación con la API."
    
    departamentos = data.get("departamentos", [])
    if not departamentos:
        return "No hay departamentos registrados en el sistema."

    return "\n".join(format_departamento(d) for d in departamentos)


@mcp_gestion.tool()
async def get_departamento(id_departamento: int) -> str:
    """Obtener detalle de un departamento por su ID."""
    data = await get_departamento_detail(id_departamento)
    if not data:
        return "Error en la comunicación con la API."
    
    departamento = data.get("departamento")
    if not departamento:
        return f"No se encontró un departamento con ID {id_departamento}."

    return format_departamento(departamento)
