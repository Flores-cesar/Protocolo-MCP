import logging 
import sys      
from tools.gestion_Personal_tools import mcp_gestion

# Configuración global de logging
logging.basicConfig(
    level=logging.INFO,  # Solo mostrar logs de nivel INFO o superior (WARNING, ERROR)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato de salida del log
    stream=sys.stderr    # Enviar los logs a stderr para no interferir con la comunicación stdio
)

# Crear un logger específico para este módulo
logger = logging.getLogger(__name__)

if __name__ == "__main__":

    logger.info("Iniciando servidor MCP gestion del personal...")
    logger.info("Servidor corriendo, esperando conexiones...")
    
    try:
        mcp_gestion.run(transport='stdio')

    except KeyboardInterrupt:
        # Captura Ctrl+C y finaliza de forma limpia
        logger.info("Servidor detenido por el usuario")

    except Exception as e:
        logger.error(f"Error en el servidor: {e}")
        raise  
