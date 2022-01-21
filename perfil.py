#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ruowu
#
# Created:     03/06/2019
# Copyright:   (c) ruowu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

inputdem = arcpy.GetParameterAsText(0)
inputlinea = arcpy.GetParameterAsText(1)
salidatabla = arcpy.GetParameterAsText(2)
salidagraf = arcpy.GetParameterAsText(3)

if inputdem == '#' or not inputdem:
    inputdem = "DEM"

if inputlinea == '#' or not inputlinea:
    inputlinea = "Linea"
    
if salidatabla == '#' or not salidatabla:
    salidatabla = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\Tabla" 

nombre_grafico = "Perfil"
if nombre_grafico == '#' or not nombre_grafico:
    nombre_grafico = "Grafica"

if arcpy.CheckExtension('3D') == 'Available':
    arcpy.CheckOutExtension('3D')
    arcpy.StackProfile_3d(inputlinea, inputdem, salidatabla, nombre_grafico)
    arcpy.management.SaveGraph(nombre_grafico, salidagraf)
    arcpy.CheckInExtension('3D')

