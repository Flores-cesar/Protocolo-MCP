from typing import Any
from services.request_base import make_api_request
from dotenv import load_dotenv
import os

load_dotenv()
API_BASE = f"{os.getenv('API_BASE')}/api"

async def get_empleados() -> dict[str, Any] | None:
    """Obtener lista de empleados"""
    url = f"{API_BASE}/empleados/list/"
    return await make_api_request(url, "GET")

async def create_empleado(nuevo_empleado: dict) -> dict[str, Any] | None:
    """Crear un nuevo empleado"""
    url = f"{API_BASE}/empleados/create/"
    return await make_api_request(url, "POST", nuevo_empleado)

async def get_empleado_detail(id_empleado: int) -> dict[str, Any] | None:
    """Obtener detalles de un empleado específico"""
    url = f"{API_BASE}/empleados/{id_empleado}/"
    return await make_api_request(url, "GET")

async def update_empleado(id_empleado: int, empleado_actualizado: dict) -> dict[str, Any] | None:
    """Actualizar un empleado existente"""
    url = f"{API_BASE}/empleados/{id_empleado}/update/"
    return await make_api_request(url, "PUT", empleado_actualizado)

async def delete_empleado(id_empleado: int) -> dict[str, Any] | None:
    """Eliminar un empleado"""
    url = f"{API_BASE}/empleados/{id_empleado}/delete/"
    return await make_api_request(url, "DELETE")
