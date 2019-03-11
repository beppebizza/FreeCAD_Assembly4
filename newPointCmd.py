#!/usr/bin/env python3
# coding: utf-8
# 
# Command template 

from PySide import QtGui, QtCore
import FreeCADGui as Gui
import FreeCAD as App
import Part, os, math, re

__dir__ = os.path.dirname(__file__)
iconPath = os.path.join( __dir__, 'Resources', 'icons' )


class newPoint:
	"My tool object"

	def GetResources(self):
		return {"MenuText": "Create a new Point",
				"ToolTip": "Create a new Datum Point in the Model",
				"Pixmap" : os.path.join( iconPath , 'Point.svg')
				}

	def IsActive(self):
		if App.ActiveDocument == None:
			return False
		else:
			return True

	def Activated(self):
		# do something here...
		# input dialog to ask the user the name of the LCS:
		pointName = 'Point_1'
		text,ok = QtGui.QInputDialog.getText(None,'Create new Datum Point','Enter Datum Point name :                              ', text = pointName)
		# if everything went well:
		if ok and text:
			App.activeDocument().getObject('Model').newObject( 'PartDesign::Point', text )


# add the command to the workbench
Gui.addCommand( 'newPointCmd', newPoint() )