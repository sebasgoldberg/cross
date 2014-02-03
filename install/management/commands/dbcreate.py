from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import subprocess
from django.template import loader
from django.template import Context
import logging
import traceback

class Command(BaseCommand):

  help=u'Instala la agencia y la deja lista para usar.'

  def crear_base_datos(self):

    import MySQLdb 
    from getpass import getpass
    
    mysql_root_password = getpass("Enter mysql root password: ")

    mysql_connection = MySQLdb.connect(
      'localhost', 
      'root',
      mysql_root_password
      )

    cursor = mysql_connection.cursor()
    
    try:
      cursor.execute('create database %s character set utf8'%settings.AMBIENTE.db.name)
      cursor.execute("create user '%s'@'localhost' identified by '%s'" % (settings.AMBIENTE.db.user, settings.AMBIENTE.db.password))
      cursor.execute("grant all on %s.* to %s" % (settings.AMBIENTE.db.name, settings.AMBIENTE.db.user))
      mysql_connection.commit()
    except:
      mysql_connection.rollback()

    mysql_connection.close()

  def crear_servicio(self):

    from django.core.management import call_command

    try:
      self.crear_base_datos()
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

  def handle(self,*args,**options):

    self.crear_servicio()

    self.stdout.write('Instalacion finalizada.\n')

