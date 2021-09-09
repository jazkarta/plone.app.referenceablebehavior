# -*- coding: utf-8 -*-


def setup_referenceablebehavior(context):
    try:
        from Products.Archetypes.setuphandlers import install_uidcatalog
        from Products.Archetypes.setuphandlers import install_referenceCatalog
    except ImportError:
        return
    if context.readDataFile('referenceablebehavior.txt') is None:
        return
    site = context.getSite()
    install_uidcatalog([], site)
    install_referenceCatalog([], site)
