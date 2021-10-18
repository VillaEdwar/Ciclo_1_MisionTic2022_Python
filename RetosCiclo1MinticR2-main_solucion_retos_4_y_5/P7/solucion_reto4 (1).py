def generar_nombre_usuario(nombre_estudiante={})->list:
    nom_est = [valor for clave, valor in nombre_estudiante.items()]
    usuario = ''
    if len(nom_est[0]) > 0 and len(nom_est[1]) > 0 and len(nom_est[2]) > 0 and len(nom_est[3]) > 0:
        usuario += nom_est[0][0] + nom_est[1] + '.' + nom_est[2] + '_' + nom_est[3][0]
    if len(nom_est[0]) > 0 and len(nom_est[1]) > 0 and len(nom_est[2]) > 0 and len(nom_est[3]) == 0:
        usuario += nom_est[0][0] + nom_est[1] + '.' + nom_est[2]
    if len(nom_est[0]) > 0 and len(nom_est[1]) == 0 and len(nom_est[2]) > 0 and len(nom_est[3]) > 0:
        usuario += nom_est[0] + '.' + nom_est[2] + '_' + nom_est[3][0]
    if len(nom_est[0]) > 0 and len(nom_est[1]) == 0 and len(nom_est[2]) > 0 and len(nom_est[3]) == 0:
        usuario += nom_est[0] + '.' + nom_est[2]
    usuario = usuario.lower()
    if 'á' in usuario:
        usuario = usuario.replace('á', 'a')
    if 'é' in usuario:
        usuario = usuario.replace('é', 'e')
    if 'í' in usuario:
        usuario = usuario.replace('í', 'i')
    if 'ó' in usuario:
        usuario = usuario.replace('ó', 'o')
    if 'ú' in usuario:
        usuario = usuario.replace('ú', 'u')
    if 'ñ' in usuario:
        usuario = usuario.replace('ñ', 'n')
    return usuario + '@itb.edu.co'