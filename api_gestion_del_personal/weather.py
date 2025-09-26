import logging
import sys
from tools.weather_tools import mcp

# Configurar logging para debug
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr  # Usar stderr para no interferir con stdio
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Iniciando servidor MCP Weather...")
    logger.info("Herramientas disponibles: get_alerts, get_forecast")
    logger.info("Servidor corriendo, esperando conexiones...")
    
    try:
        mcp.run(transport='stdio')
    except KeyboardInterrupt:
        logger.info("Servidor detenido por el usuario")
    except Exception as e:
        logger.error(f"Error en el servidor: {e}")
        raise