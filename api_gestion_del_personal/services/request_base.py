from typing import Any, Optional
import httpx

# Configuración de la API
API_BASE = "http://localhost:8000/api"
USER_AGENT = "django-client/1.0"

async def make_api_request(url: str, method: str = "GET", data: Optional[dict] = None) -> dict[str, Any] | None:

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers, timeout=30.0)
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers, json=data, timeout=30.0)
            elif method.upper() == "PUT":
                response = await client.put(url, headers=headers, json=data, timeout=30.0)
            elif method.upper() == "DELETE":
                response = await client.delete(url, headers=headers, timeout=30.0)
            else:
                raise ValueError(f"Método HTTP no soportado: {method}")
            
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error en petición {method} a {url}: {e}")
            return None
