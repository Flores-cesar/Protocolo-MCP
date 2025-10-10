from typing import Any
from services.request_base import make_api_request
from dotenv import load_dotenv
import os

load_dotenv()
API_BASE = f"{os.getenv('API_BASE')}/api"

# ============= ROLES =============
async def get_roles() -> dict[str, Any] | None:
    """Obtener lista de roles"""
    url = f"{API_BASE}/roles/list/"
    return await make_api_request(url, "GET")

async def create_rol(nuevo_rol: dict) -> dict[str, Any] | None:
    """Crear un nuevo rol"""
    url = f"{API_BASE}/roles/create/"
    return await make_api_request(url, "POST", nuevo_rol)

async def get_rol_detail(id_rol: int) -> dict[str, Any] | None:
    """Obtener detalles de un rol específico"""
    url = f"{API_BASE}/roles/{id_rol}/"
    return await make_api_request(url, "GET")

async def update_rol(id_rol: int, rol_actualizado: dict) -> dict[str, Any] | None:
    """Actualizar un rol existente"""
    url = f"{API_BASE}/roles/{id_rol}/update/"
    return await make_api_request(url, "PUT", rol_actualizado)

async def delete_rol(id_rol: int) -> dict[str, Any] | None:
    """Eliminar un rol"""
    url = f"{API_BASE}/roles/{id_rol}/delete/"
    return await make_api_request(url, "DELETE")
