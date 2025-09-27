def format_empleado(empleado: dict) -> str:
    """Formatea la información de un empleado para mostrar en pantalla."""
    return f"""
    ID: {empleado.get('id_empleado', 'N/A')}
    Nombre: {empleado.get('nombre', 'N/A')} {empleado.get('apellido', '')}
    Edad: {empleado.get('edad', 'N/A')}
    Correo: {empleado.get('correo','N/A')}
    Rol ID: {empleado.get('rol_id', 'N/A')}
    Fecha de ingreso: {empleado.get('fecha_ingreso', 'N/A')}
    Salario: {empleado.get('salario', 'N/A')}
    Estado: {empleado.get('estado', 'N/A')}
    """