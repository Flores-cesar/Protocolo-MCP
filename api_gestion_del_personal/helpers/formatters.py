def format_empleado(empleado: dict) -> str:
    """Formatea la información de un empleado para mostrar en pantalla."""
    return f"""
    ID Empleado: {empleado.get('id_empleado', 'N/A')}
    Nombre: {empleado.get('nombre', 'N/A')} {empleado.get('apellido', '')}
    Edad: {empleado.get('edad', 'N/A')}
    Correo: {empleado.get('correo','N/A')}
    Rol ID: {empleado.get('rol_id', 'N/A')}
    Fecha de ingreso: {empleado.get('fecha_ingreso', 'N/A')}
    Salario: {empleado.get('salario', 'N/A')}
    Estado: {empleado.get('estado', 'N/A')}
    """

def format_rol(rol: dict) -> str:
    """Formatea la información de un rol para mostrar en pantalla."""
    return f"""
    ID Rol: {rol.get('id_rol', 'N/A')}
    Departamento ID: {rol.get('departamento', 'N/A')}
    Nombre: {rol.get('nombre', 'N/A')}
    Responsabilidades: {rol.get('responsabilidades', 'N/A')}
    """

def format_departamento(departamento: dict) -> str:
    """Formatea la información de un departamento para mostrar en pantalla."""
    return f"""
    ID Departamento: {departamento.get('id_departamento', 'N/A')}
    Parent ID: {departamento.get('parent_id', 'N/A')}
    Responsable ID: {departamento.get('responsable_id', 'N/A')}
    Nombre: {departamento.get('nombre', 'N/A')}
    Descripción: {departamento.get('descripcion', 'N/A')}
    """