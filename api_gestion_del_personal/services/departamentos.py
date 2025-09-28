from typing import Any
from services.request_base import make_api_request

API_BASE = "http://localhost:8000/api"

# ============= DEPARTAMENTOS =============
async def get_departamentos() -> dict[str, Any] | None:
    """Obtener lista de departamentos"""
    url = f"{API_BASE}/departamentos/list/"
    return await make_api_request(url, "GET")

async def create_departamento(nuevo_departamento: dict) -> dict[str, Any] | None:
    """Crear un nuevo departamento"""
    url = f"{API_BASE}/departamentos/create/"
    return await make_api_request(url, "POST", nuevo_departamento)

async def get_departamento_detail(id_departamento: int) -> dict[str, Any] | None:
    """Obtener detalles de un departamento específico"""
    url = f"{API_BASE}/departamentos/{id_departamento}/"
    return await make_api_request(url, "GET")

async def update_departamento(id_departamento: int, departamento_actualizado: dict) -> dict[str, Any] | None:
    """Actualizar un departamento existente"""
    url = f"{API_BASE}/departamentos/{id_departamento}/update/"
    return await make_api_request(url, "PUT", departamento_actualizado)

async def delete_departamento(id_departamento: int) -> dict[str, Any] | None:
    """Eliminar un departamento"""
    url = f"{API_BASE}/departamentos/{id_departamento}/delete/"
    return await make_api_request(url, "DELETE")