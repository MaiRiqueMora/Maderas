@echo off
echo Activando entorno virtual...
call env\Scripts\activate.bat

echo Ejecutando script de carga de datos...
python cargar_datos.py

echo.
echo Presiona cualquier tecla para continuar...
pause

