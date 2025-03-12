python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo.
echo ========================================
echo Entorno virtual creado y activado correctamente!
echo Si ves (venv) al inicio de tu linea de comandos,
echo el entorno virtual esta activo.
echo.
echo Python actual: 
where python
echo.
echo Para activarlo en el futuro, usa: venv\Scripts\activate
echo Para desactivarlo, usa: deactivate
echo ========================================
