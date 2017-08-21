# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Class_GetFamiliar
                                 A QGIS plugin
 Description; getting familiar with QT and plugin builder
                             -------------------
        begin                : 2017-08-21
        copyright            : (C) 2017 by Kasper Skjeggestad
        email                : kasper.skjeggestad@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Class_GetFamiliar class from file Class_GetFamiliar.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Module_GetFamiliar import Class_GetFamiliar
    return Class_GetFamiliar(iface)
