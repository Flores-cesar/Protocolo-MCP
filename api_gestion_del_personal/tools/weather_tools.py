from mcp.server.fastmcp import FastMCP
from utils.weather_utils import make_nws_request, format_alert, NWS_API_BASE

mcp = FastMCP("weather")

@mcp.tool()
async def get_alerts(state:str) -> str: 
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "No se pueden obtener alertas o no se encontraron alertas para este estado"
    
    if not data["feature"]:
        return "No hay alertas activadas para este Estado"
    
    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    data = await make_nws_request(url)

    if not data:    
        return "Unable to fetch forecast data for this location."

    forecast_url = data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:
        forecast = f"""
            {period['name']}:
            Temperature: {period['temperature']}°{period['temperatureUnit']}
            Wind: {period['windSpeed']} {period['windDirection']}
            ForeCast: {period['detailedForecast']}

        """
        forecasts.append(forecast)
    return "\n---\n".join(forecasts)

    
    