#!/usr/bin/python
# -*- coding: latin-1 -*-

import py3270

print "Teste extensão pw3270"

print py3270.Revision()

term = py3270.Terminal("")

print "Using pw3270 version " + term.Version() + " revision " + term.Revision()

term.Connect("192.168.240.1:51004",10);

print term.IsConnected()
print term.IsReady()

print term.GetStringAt(18,61,3)

print "-----------------------------------------------------------------------"
print term
print "-----------------------------------------------------------------------"
